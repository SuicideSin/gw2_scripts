#!/usr/bin/env	python3
# vim: set fileencoding=utf-8 tabstop=4 shiftwidth=4 softtabstop=4:

import json
from urllib.request import *
import urllib.error
import http.cookiejar

class GW2Spidy:
	def __init__(self):
		self.cookieJar = http.cookiejar.CookieJar()
		cookieProcessor = HTTPCookieProcessor(self.cookieJar)
		proxyProcessor = ProxyHandler()
		httpProcessor = HTTPHandler()
		errorProcessor = HTTPDefaultErrorHandler()

		self.urlopener = build_opener(proxyProcessor, errorProcessor,
									cookieProcessor, httpProcessor)
		self.urlopener.addheaders = [
				('User-agent', 'gw2spidy.py'),
				('Accept', 'text/plain'),
				('Accept-Charset', 'utf-8'),
		]

		install_opener(self.urlopener)
		try:
			urlopen("http://www.gw2spidy.com/api/v0.9/json/types")
		except urllib.error.HTTPError as e:
			raise RuntimeError("couldn't access GW2Spidy: {}".format(e.reason))

	def _installOpener(self):
		install_opener(self.urlopener)

	def _makeRequest(self, req):
		self._installOpener()
		url = "http://www.gw2spidy.com/api/v0.9/json/{}".format(req)
		try:
			resp = urlopen(url)
			resp = json.loads(str(resp.read(), 'utf-8'), 'utf-8')

			return resp
		except urllib.error.HTTPError as e:
			raise RuntimeError("couldn't access GW2Spidy: ({}, {})".format(url, 
								e.reason))
		except UnicodeError as e:
			raise RuntimeError("couldn't encode the response from GW2Spidy")

	def _getItem(self, itemid):
		return self._makeRequest("item/{}".format(itemid))

	def getItem(self, itemid):
		item = self._makeRequest("item/{}".format(itemid))
		return item["result"]

	def getBuyOfferPrice(self, itemid):
		item = self._getItem(itemid)
		return int(item["result"]["max_offer_unit_price"]) + 1

	def getSaleOfferPrice(self, itemid):
		item = self._getItem(itemid)
		return int(item["result"]["min_sale_unit_price"]) - 1

