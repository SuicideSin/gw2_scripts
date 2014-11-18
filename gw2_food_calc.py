#!/usr/bin/env	python3
# vim: set fileencoding=utf-8 tabstop=4 shiftwidth=4 softtabstop=4:

import functools, itertools, operator
import sys, os, os.path
import fileinput, glob
import string, re
import decimal

import argparse

from gw2_item_recipes import *
from gw2_spidy import *

#
# program code
#

def currency_to_copper(c):
	return c[2] + 100 * c[1] + 10000 * c[0]

def copper_to_currency(c):
	gold = int(c / 10000)
	silver = int((c - gold * 10000) / 100)
	copper = int((c - (gold * 10000) - (silver * 100)) / 1)
	return (gold, silver, copper)

def currency_to_string(c):
	return "({0[0]:>3}, {0[1]:>2}, {0[2]:>2})".format(c)

def calc_item_cost(spidy, item, name, times_needed, rec):
	one_item = spidy.getBuyOfferPrice(item[0])
	times = item[1] * times_needed
	buy_cost = one_item * times

	item_desc = []

	prod_costs = 0
	not_buyable = 0
	if item[2] is not None:
		if 'karma' in item[2]:
			not_buyable = 1
		elif 'vendor' in item[2]:
			not_buyable = 3
		else:
			for k in sorted(item[2].keys()):
				if k == 'dontbuy':
					not_buyable = 2
					continue

				(subcost, subdesc) = calc_item_cost(spidy, item[2][k], k, times_needed,	rec + 1)
				prod_costs = prod_costs + subcost
				item_desc = item_desc + subdesc

	buy = 0
	if not_buyable == 1:
		one_item = 0
		cost = 0
		buy = 2
	elif ( buy_cost > prod_costs and prod_costs > 0 ) or not_buyable == 2:
		one_item = prod_costs / times
		cost = prod_costs
	elif not_buyable == 3:
		buy = 3
		cost = buy_cost
	else:
		buy = 1
		cost = buy_cost

	desc = "{0} = {5}{1:>2} * {2} ... {3} ... {4}".format(
				currency_to_string(copper_to_currency(cost)), times,
				currency_to_string(copper_to_currency(one_item)), buy, name,
				'\t'.expandtabs(rec*4)
			)

	if buy == 1:
		item_desc = [desc]
	else:
		item_desc = [desc] + item_desc

	return (cost, item_desc)

def calc_cost(spidy, item, times, name):
	costs = 0
	for k in sorted(item[2].keys()):
		(subcost, subdesc) = calc_item_cost(spidy, item[2][k], k, times, 0)

		if len(subdesc) > 1:
			item_desc = functools.reduce(lambda old, new: "{}\n{}".format(old, new), subdesc)
		else:
			item_desc = subdesc[0]

		print(item_desc)

		costs = costs + subcost

	print("-------------")

	print("{0} = {1:>2} * {2} ... {3}".format(
		currency_to_string(copper_to_currency(costs)),
		item[1] * times,
		currency_to_string(
			copper_to_currency(costs / (item[1] * times))), name))
	return copper_to_currency(costs)

def main(item_name, times):
	spidy = GW2Spidy()

	dict = [d for d in GW2Recipes.values() if item_name in d]
	item_recipe = dict[0][item_name]
	item_spidy = spidy.getItem(item_recipe[0])

	times = int(times / item_recipe[1])
	if times < 1:
		times = 1

	print("item_recipe is: {}".format(item_name))
	print()

	#  5% posting fee of total (not refunded)
	#		when posted; calculated on the sum of ALL items
	# 10% tax on successful sales
	#
	# both are rounded mathematically

	costs = currency_to_copper(calc_cost(spidy, item_recipe, times, item_name))
	sale = item_spidy["min_sale_unit_price"] - 1
	batch = item_recipe[1] * times

	income = batch * sale

	tax_posting = int((0.05 * income) + 0.5)
	tax_buying = int((0.10 * income) + 0.5)

	income_tax = income - tax_posting - tax_buying

	print()
	print("income before taxes: {}".format(copper_to_currency(income)))
	print("income after taxes:  {}".format(copper_to_currency(income_tax)))

	print()
	if float(item_spidy["sale_availability"]) != 0:
		print("request - sale - ratio: {} - {} - {}".format(
			item_spidy["offer_availability"], item_spidy["sale_availability"],
			float(item_spidy["offer_availability"]) / float(item_spidy["sale_availability"])))
	print("sale/offer price change (last hour): {} / {}".format(
		item_spidy["sale_price_change_last_hour"], item_spidy["offer_price_change_last_hour"]))

	print()
	print("profit per item (before tax): {}".format(
		copper_to_currency(sale - (costs / batch))
	))
	print("profit per item (after tax): {}".format(
		copper_to_currency(sale - int(sale * 0.05 + 0.5) - \
				int(sale * 0.10 + 0.5) - (costs / batch))
	))
	print("profit per batch (before tax): {}".format(
		copper_to_currency(income - costs)
	))
	print("profit per batch (after  tax): {}".format(
		copper_to_currency(income_tax - costs)
	))

class SmartFormatter(argparse.HelpFormatter):
	def _split_lines(self, text, width):
		# this is the RawTextHelpFormatter._split_lines
		if text.startswith('R|'):
			return text[2:].splitlines()
		return argparse.HelpFormatter._split_lines(self, text, width)

valid_items = []
for c in sorted(GW2Recipes.keys()):
	valid_items.extend(sorted(GW2Recipes[c].keys()))

parser = argparse.ArgumentParser(description='calculate profit for item-production', formatter_class=SmartFormatter)
parser.add_argument('item', type=str, choices=valid_items,
					help="R|what item shall be produced, valid items are: \n"+", \n".join(valid_items),
					metavar='ITEM')
parser.add_argument('times', type=int, nargs='?', default=1,
					help="how many items shall be produced")

args = parser.parse_args()

main(args.item, int(args.times))
