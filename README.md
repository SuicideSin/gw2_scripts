gw2_scripts
===========

This is a small collection of scripts that can be used to make crafting and
trading on tp in Guild Wars 2 more convenient (these are NO ingame-macros!)

gw2_food_calc.py
----------------

Prints the necessary resources with their attached prices on tp to craft
certain foods.

Example:

	$ ./gw2_food_calc.py Rare_Veggie_Pizza 10

More information and possible food-recipes:

	$ ./gw2_food_calc.py --help

The script always rounds down to the perfect amount (all bought resources will
be used for crafting).

Both sale- and buy-prices derived from the corresponding sale-/buy-OFFER price
- no instant-sale or buy. The data for these prices are collected from the
  database of [gw2spidy](http://www.gw2spidy.com/).

Items that can/shall not be bought on tp are distinguished by a `... 0 ...`
before their name. The same holds for items that can only be bought from
karma-vendors - they are marked by a `... 2 ...` before their name.

filter_buylist.sh
-----------------

Can be used to filter the output of `gw2_food_calc.py`. Used by piping in the
output of the former script, it will then only display the resources that can
be bought on tp or a karma-vendor, sorted by their names.

	$ ./gw2_food_calc.py Rare_Veggie_Pizza 10 | ./filter_buylist.sh

gw2_spidy.py
------------

Thin abstraction layer for [gw2spidy's](http://www.gw2spidy.com/) API. This is
not comprehensive for all functions that the API offers - only for what I need
in the scripts.

gw2_item_recipes.py
-------------------

A collection of gw2 recipe-data. If you want to compute anything else with
`gw2_food_calc.py` then you need to extend this.

A tuple for identifying a item consists of: `(<data_id>, <times>,
<sub_items>)`. The `data_id` is the corresponding if from gw2spidy.
