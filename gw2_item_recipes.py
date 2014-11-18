#!/usr/bin/env	python3
# vim: set fileencoding=utf-8 tabstop=4 shiftwidth=4 softtabstop=4:

_karma = { 'karma' : (0, 0, None), }
_vendor = { 'vendor' : (0, 0, None), }
_dont_buy = ( 'dontbuy', (0, 0, None) )

_gear = {
	'Deldrimor_Steel_Ingot' : (46738, 1,
	{
		'Darksteel Ingot' : (19681, 20,
		{
			'Platinum Ore' : (19702, 40, None),
			'Lump of Primordium' : (19924, 20, _vendor),
		}),
		'Iron Ingot' : (19683, 20,
		{
			'Iron Ore' : (19699, 60, None),
		}),
		'Steel Ingot' : (19688, 10,
		{
			'Iron Ore' : (19699, 30, None),
			'Lump of Coal' : (19750, 10, _vendor),
		}),
		'Lump of Mithrillium' : (46742, 1,
		{
			'Mithril Ingot' : (19684, 50,
			{
				'Mithril Ore' : (19700, 100, None),
			}),
			'Glob of Ectoplasm' : (19721, 1, None),
			'Thermocatalytic Reagent' : (46747, 10, _vendor),

			_dont_buy[0] : _dont_buy[1],
		}),
	}),

	'Spiritwood_Plank' : (46736, 1,
	{
		'Hard Wood Plank' : (19711, 20, {
			'Hard Wood Log' : (19724, 60, None),
		}),
		'Soft Wood Plank' : (19713, 20, {
			'Soft Wood Log' : (19726, 80, None),
		}),
		'Seasoned Wood Plank' : (19714, 10, {
			'Seasoned Wood Log' : (19727, 30, None),
		}),
		'Glob of Elder Spirit Residue' : (46744, 1, {
			'Elder Wood Plank' : (19709, 50, {
				'Elder Wood Log' : (19722, 150, None),
			}),
			'Glob of Ectoplasm' : (19721, 1, None),
			'Thermocatalytic Reagent' : (46747, 10, _vendor),

			_dont_buy[0] : _dont_buy[1],
		}),
	}),

	'Bolt_of_Damask' : (46741, 1,
	{
	    'Bolt of Wool' : (19740, 20, {
	        'Wool Scrap' : (19739, 40, None),
		}),
	    'Bolt of Cotton' : (19742, 10, {
	        'Cotton Scrap' : (19741, 20, None),
		}),
	    'Bolt of Linen' : (19744, 20, {
	        'Linen Scrap' : (19743, 40, None),
		}),
	    'Spool of Silk Weaving Thread' : (46740, 1, {
	        'Glob of Ectoplasm' : (19721, 1, None),
	        'Bolt of Silk' : (19747, 100, {
	            'Silk Scrap' : (19748, 300, None),
			}),
	        'Spool of Gossamer Thread' : (19790, 25, _vendor),

			_dont_buy[0] : _dont_buy[1],
		}),
	}),

	'Zojja_s_Berserker_Inscription' : (46695, 1,
	{
		'Berserker_s Orichalcum Imbued Inscription' : (19920, 1,
		{
			'Orichalcum Plated Dowel' : (12988, 5,
			{
				'Orichalcum Ingot' : (19685, 15,
				{
					'Orichalcum Ore' : (19701, 30, None),
				}),
				'Ancient Wood Plank' : (19712, 10,
				{
					'Ancient Wood Log' : (19725, 30, None),
				}),
			}),
			'Glob of Ectoplasm' : (19721, 5, None),
			'Vial of Powerful Blood' : (24295, 5, None),
		}),
		'Pile of Crystalline Dust' : (24277, 10, None),
		'Deldrimor Steel Plated Dowel' : (45832, 1,
		{
			'Spiritwood Plank' : (46736, 3,
			{
				'Hard Wood Plank' : (19711, 60,
				{
					'Hard Wood Log' : (19724, 180, None),
				}),
				'Soft Wood Plank' : (19713, 60,
				{
					'Soft Wood Log' : (19726, 240, None),
				}),
				'Seasoned Wood Plank' : (19714, 30,
				{
					'Seasoned Wood Log' : (19727, 90, None),
				}),
				'Glob of Elder Spirit Residue' : (46744, 3,
				{
					'Elder Wood Plank' : (19709, 150,
					{
						'Elder Wood Log' : (19722, 450, None),
					}),
					'Glob of Ectoplasm' : (19721, 3, None),
					'Thermocatalytic Reagent' : (46747, 30, _vendor),

					_dont_buy[0] : _dont_buy[1],
				}),
			}),
			'Deldrimor Steel Ingot' : (46738, 3,
			{
				'Darksteel Ingot' : (19681, 60,
				{
					'Platinum Ore' : (19702, 120, None),
					'Lump of Primordium' : (19924, 60, _vendor),
				}),
				'Iron Ingot' : (19683, 60,
				{
					'Iron Ore' : (19699, 180, None),
				}),
				'Steel Ingot' : (19688, 30,
				{
					'Iron Ore' : (19699, 90, None),
					'Lump of Coal' : (19750, 30, _vendor),
				}),
				'Lump of Mithrillium' : (46742, 3,
				{
					'Mithril Ingot' : (19684, 150,
					{
						'Mithril Ore' : (19700, 300, None),
					}),
					'Glob of Ectoplasm' : (19721, 3, None),
					'Thermocatalytic Reagent' : (46747, 30, _vendor),

					_dont_buy[0] : _dont_buy[1],
				}),
			}),
		}),
		'Glob of Dark Matter' : (46681, 10, { _dont_buy[0] : _dont_buy[1] }),
	}),
}

_utils = {
	'Superior_Sharpening_Stone' : (9443, 5,
	{
		'Orichalcum Ingot' : (19685, 1,
		{
			'Orichalcum Ore' : (19701, 2, None),
		}),
		'Pile of Crystalline Dust' : (24277, 3, None),
	}),

	'Master_Tuning_Crystal' : (9476, 5,
	{
		'Pile of Crystalline Dust' : (24277, 5, None),
	}),

	'Master_Maintenance_Oil' : (9461, 5,
	{
		'Jug of Water' : (12156, 20, _vendor),
		'Pile of Crystalline Dust' : (24277, 3, None),
	}),
}

_food = {
	'Bowl_of_Lemongrass_Poultry_Soup' : (12481, 3, {
		'coconut' : (12350, 3, _karma),
		'bowl_of_herbeb_poultry_stock' : (12490, 3,
		{
			'pile_of_simple_stew_herbs' : (12179, 1,
				{
					'bay_leaf' : (12247, 1, None),
					'thyme_leaf' : (12248, 1, None),
				}),
				'bowl_of_poultry_stock' : (12202, 1,
				{
					'carrot' : (12134, 2, None),
					'onion'	: (12142, 2, None),
					'jug_of_water' : (12156, 1, None),
					'slab_of_poultry_meat' : (24360, 1, None),
				}),
			'sage_leaf' : (12243, 1, None),
			'rosemary_sprig' : (12335, 1, None),
		}),
		'lemongrass' : (12546, 3, None),
		'slab_of_poultry_meat' : (24360, 3, None),
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

	'Bowl_of_Sweet_and_Spicy_Beans' : (66528, 1, {
	    'Pile of Salt and Pepper' : (12178, 5, {
	        'Packet of Salt' : (12153, 5, _vendor),
	        'Black Peppercorn' : (12236, 5, None),
		}),
	    'Kidney Bean' : (12239, 10, _karma),
	    'Ghost Pepper' : (12544, 10, None),
	    'Prickly Pear' : (66522, 10, None),
	}),

	'Plate_of_Steak_and_Asparagus' : (12430, 1, {
	    'Stick of Butter' : (12138, 1, None),
	    'Pile of Salt and Pepper' : (12178, 1, {
			'Packet of Salt' : (12153, 1, _vendor),
	        'Black Peppercorn' : (12236, 1, None),
		}),
	    'Asparagus Spear' : (12505, 1, None),
	    'Slab of Red Meat' : (24359, 1, None),
	}),

	'Super_Veggie_Pizza' : (12427, 8, {
	    'Fancy Veggie Pizza' : (12391, 4, {
	        'Bell Pepper' : (12235, 2, _karma),
	        'Spinach Leaf' : (12241, 2, None),
	        'Mushroom Pizza' : (12368, 2, {
	            'Mushroom' : (12147, 1, None),
	            'Cheese Pizza' : (12218, 1, {
	                'Cheese Wedge' : (12159, 1, _karma),
	                'Ball of Dough' : (12166, 1, {
						'Bag of Flour' : (12136, 1, _vendor),
	                    'Stick of Butter' : (12138, 1, None),
						'Jug of Water' : (12156, 1, _vendor),
					}),
	                'Jar of Tomato Sauce' : (12172, 1, {
						'Tomato' : (12141, 1, _vendor),
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

	'Bowl_of_Poultry_and_Leek_Soup' : (12444, 2, {
	    'Bowl of Cream Soup Base' : (12268, 1, {
	        'Glass of Buttermilk' : (12137, 1, _karma),
	        'Pile of Salt and Pepper' : (12178, 1, {
	            'Packet of Salt' : (12153, 1, _vendor),
	            'Black Peppercorn' : (12236, 1, None)
			}),
	        'Bowl of Poultry Stock' : (12202, 1, {
	            'Carrot' : (12134, 2, None),
	            'Onion' : (12142, 2, None),
	            'Jug of Water' : (12156, 1, _vendor),
	            'Slab of Poultry Meat' : (24360, 1, None),
			}),
	        'Bowl of Roux' : (12267, 1, {
	            'Bag of Flour' : (12136, 1, _vendor),
	            'Stick of Butter' : (12138, 1, None),
			}),
		}),
	    'Leek' : (12508, 1, None),
	    'Slab of Poultry Meat' : (24360, 1, None),
	}),
}

GW2Recipes = {
	'food' : _food,
	'utils' : _utils,
	'gear' : _gear,
}
