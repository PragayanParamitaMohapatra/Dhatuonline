def product_info():
    l = []
    while len( l ) <= 5:
        name_product = input( "name of the the product : " )
        make = input( "product maker : " )
        while name_product and make:
            k = dict( {name_product: make} )
            l.append( k )
            print( l )
            break
    usage_top_materials = {"1": "DrillBushing", "2": "coolant tube", "3": "Adapter", "4": "spanner", "5": "Hammer",
                           "6": "srews", "7": "bolts", "8": "nuts"}
    usage_top_materials_input = input( "Select the materials : " )
    if usage_top_materials_input in usage_top_materials:
        print( usage_top_materials.get( usage_top_materials_input ) )
    else:
        print( "choose correct materials" )
    consumable = {"1": "YG1", "2": "MIRANDA TOOLS", "3": "TOTEM", "4": "OMEGA", "5": "TRUMIL", "6": "ROHIT",
                  "7": "TOOLS", "8": "MAGICUT"}
    consumable_input = input( "Enter the consumable : " )
    if consumable_input in consumable.keys():
        print( consumable.get( consumable_input ) )
    else:
        print( "select the correct one " )


product_info()
print( "THANK YOU FOR REGISTREING IN DHATUONLINE" )
