#!/usr/bin/env	python3
# vim: set fileencoding=utf-8 tabstop=4 shiftwidth=4 softtabstop=4:

_karma = { 'karma' : (0, 0, None), }

_food = {
	'bowl_of_lemongrass_poultry_soup' : (12481, 3, {
		'coconut'							: (12350, 3, _karma),
		'bowl_of_herbeb_poultry_stock'		: (12490, 3,
		{
			'pile_of_simple_stew_herbs' 	: (12179, 1,
				{
					'bay_leaf'				: (12247, 1, None),
					'thyme_leaf'		    : (12248, 1, None),
				}),
				'bowl_of_poultry_stock'	    : (12202, 1,
				{
					'carrot'				: (12134, 2, None),
					'onion'					: (12142, 2, None),
					'jug_of_water'			: (12156, 1, None),
					'slab_of_poultry_meat'	: (24360, 1, None),
				}),
			'sage_leaf'						: (12243, 1, None),
			'rosemary_sprig'				: (12335, 1, None),
		}),
		'lemongrass'						: (12546, 3, None),
		'slab_of_poultry_meat'				: (24360, 3, None),
	}),

	'loaf_of_saffron_bread' : (12474, 1, {
		'bag_of_flour'		: (12136, 1, None),
		'packet_of_yeast'	: (12152, 1, _karma),
		'jug_of_water'		: (12156, 1, None),
		'saffron_thread'	: (12547, 1, None),
	}),

	'Rare_Veggie_Pizza' : (12464, 8,
	{
		'Snow Truffle' : (12144, 8, None),
		'Super Veggie Pizza' : (12427, 8,
		{
			'Fancy Veggie Pizza' : (12391, 4,
			{
				'Bell Pepper' : (12235, 2, _karma),
				'Spinach Leaf' : (12241, 2, None),
				'Mushroom Pizza' : (12368, 2,
				{
					'Mushroom' : (12147, 1, None),
					'Cheese Pizza' : (12218, 1,
					{
						'Cheese Wedge' : (12159, 1, _karma),
						'Ball of Dough' : (12166, 1,
						{
							'Bag of Flour' : (12136, 1, None),
							'Stick of Butter' : (12138, 1, None),
							'Jug of Water' : (12156, 1, None),
						}),
						'Jar of Tomato Sauce' : (12172, 1,
						{
							'Tomato' : (12141, 1, None),
							'Onion' : (12142, 1, None),
							'Head of Garlic' : (12163, 1, None),
							'Basil Leaf' : (12245, 1, _karma),
						}),
					}),
					'Portobello Mushroom' : (12334, 1, None),
				}),
				'Shallot' : (12517, 2, _karma),
			}),
			'Eggplant' : (12502, 4, _karma),
			'Artichoke' : (12512, 4, None),
		}),
		'Orrian Truffle' : (12545, 8, None)
	}),

	'Plate_of_Orrian_Steak_Frittes' : (12468, 1,
	{
		'Cup of Lotus Fries' : (12472, 1,
		{
			'Jar of Vegetable Oil' : (12158, 1, None),
			'Pile of Salt and Pepper' : (12178, 1,
			{
				'Packet of Salt' : (12153, 1, None),
				'Black Peppercorn' : (12236, 1, None),
			}),
			'Lotus Root' : (12510, 1, None),
		}),
		'Slab of Red Meat' : (24359, 1, None),
	}),

	'Bowl_of_Truffle_Risotto' : (12465, 3,
	{
		'Snow Truffle' : (12144, 3, None),
		'Bowl of Mushroom Risotto' : (12392, 3,
		{
			'Mushroom' : (12147, 3, None),
			'Cheese Wedge' : (12159, 3, _karma),
			'Portobello Mushroom' : (12334, 3, None),
			'Bowl of Risotto Base' : (12529, 3,
			{
				'Bottle of Rice Wine' : (8576, 3, None),
				'Rice Ball' : (12145, 3, _karma),
				'Bowl of Herbed Poultry Stock' : (12490, 3,
				{
					'Pile of Simple Stew Herbs' : (12179, 1,
					{
						'Bay Leaf' : (12247, 1, None),
						'Thyme Leaf' : (12248, 1, None),
					}),
					'Bowl of Poultry Stock' : (12202, 1,
					{
						'Carrot' : (12134, 2, None),
						'Onion' : (12142, 2, None),
						'Jug of Water' : (12156, 1, None),
						'Slab of Poultry Meat' : (24360, 1, None),
					}),
					'Sage Leaf' : (12243, 1, None),
					'Rosemary Sprig' : (12335, 1, None),
				}),
				'Bowl of Fancy Tangy Sautee Mix' : (12528, 3,
				{
					'Onion' : (12142, 3, None),
					'Jar of Vegetable Oil' : (12158, 3, None),
					'Head of Garlic' : (12163, 3, None),
					'Shallot' : (12517, 3, _karma),
				}),
			}),
		}),
		'Orrian Truffle' : (12545, 3, None),
	}),

	'Bowl_of_Orrian_Truffle_and_Meat_Stew' : (12488, 3,
	{
		'Bowl of Staple Soup Vegetables' : (12167, 3,
		{
			'Carrot' : (12134, 3, None),
			'Potato' : (12135, 3, None),
			'Onion' : (12142, 3, None),
			'Celery Stalk' : (12240, 3, _karma),
		}),
		'Bowl of Herbed Meat Stock' : (12489, 3,
		{
			'Pile of Simple Stew Herbs' : (12179, 1,
			{
				'Bay Leaf' : (12247, 1, None),
				'Thyme Leaf' : (12248, 1, None),
			}),
			'Bowl of Red Meat Stock' : (12199, 1,
			{
				'Carrot' : (12134, 2, None),
				'Onion' : (12142, 2, None),
				'Jug of Water' : (12156, 1, None),
				'Slab of Red Meat' : (24359, 2, None),
			}),
			'Sage Leaf' : (12243, 1, None),
			'Rosemary Sprig' : (12335, 1, None),
		}),
		'Orrian Truffle' : (12545, 3, None),
		'Slab of Red Meat' : (24359, 3, None),
	}),

	'Bowl_of_Curry_Butternut_Squash_Soup' : (12486, 6,
	{
		'Coconut' : (12350, 3, _karma),
		'Bowl of Herbed Vegetable Stock' : (12491, 3,
		{
			'Pile of Simple Stew Herbs' : (12179, 1,
			{
				'Bay Leaf' : (12247, 1, None),
				'Thyme Leaf' : (12248, 1, None),
			}),
			'Bowl of Vegetable Stock' : (12206, 1,
			{
				'Carrot' : (12134, 2, None),
				'Onion' : (12142, 2, None),
				'Jug of Water' : (12156, 1, None),
				'Celery Stalk' : (12240, 1, _karma),
			}),
			'Sage Leaf' : (12243, 1, None),
			'Rosemary Sprig' : (12335, 1, None),
		}),
		'Butternut Squash' : (12511, 3, None),
		'Jar of Red Curry Paste' : (12542, 3,
		{
			'Lime' : (12339, 3, _karma),
			'Pile of Stirfry Spice Mix' : (12496, 3,
			{
				'Onion' : (12142, 3, None),
				'Head of Garlic' : (12163, 3, None),
				'Ginger Root' : (12328, 3, _karma),
				'Chili Pepper' : (12331, 3, None),
			}),
			'Cayenne Pepper' : (12504, 3, None),
			'Lemongrass' : (12546, 3, None),
		}),
	}),

}

GW2Recipes = {
	'food' : _food,
}
