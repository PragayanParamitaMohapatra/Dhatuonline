import re


def basic_info():
    company_name = input( "Name of the company: " )
    print( company_name )
    constitution_of_company = {"1": "Public Limited", "2": "Private Limited", "3": "Parternship", "4": "LLP",
                               "5": "Proprietoriship"}
    constitution_of_company_input = input( "Name of constitution_of_company: " )
    # constitution_of_company_input = temp
    # while temp is True:
    if constitution_of_company_input in constitution_of_company.keys():
        print( constitution_of_company.get( constitution_of_company_input ) )
    else:
        print( 'constitution_of_company is invalid' )
        exit()
    company_category_input = input( "company category: " )
    company_category = {"1": "micro", "2": "small", "3": "large", "4": "medium"}
    if company_category_input in company_category:
        print( company_category.get( company_category_input ) )
    else:
        print( "please select go through valid choice" )
        exit()
    manufacture_trader_input = input( "select the manufacture: " )
    manufacture_trader = {"1": "manufacturer", "2": "trader1", "3": "trader2", "4": "trader3"}
    if manufacture_trader_input in manufacture_trader:
        print( manufacture_trader.get( manufacture_trader_input ) )
    else:
        print( "select the valid manufacture" )
        exit()
    Address = input( " Give the Address: " )
    print( Address )
    country = input( " Enter the country: " )
    print( country )
    city = input( " Enter the city : " )
    city_select = {"1": "calcuttta", "2": "banglore", "3": "chennai", "4": "delhi", "5": "mumbai", "6": "kochin",
                   "7": "vizag"}
    if city in city_select:
        print( city_select.get( city ) )
    else:
        print( "select the proper city:" )
        exit()
    state = input( " Enter the state : " )
    state_select = {"1": "odisha", "2": "karnatk", "3": "andhra", "4": "up"}
    if state in state_select:
        print( state_select.get( state ) )
    else:
        print( " please go through proper choice :" )
        exit()
    pin_code = input( " Enter the pincode : " )
    if re.match( "[0,9] {6}", pin_code ):
        print( "match" )
    else:
        print( "Not Match" )
    print( pin_code )
    registered_phoneno = (input( "Entered the phone number : " ))
    print( registered_phoneno )
    if re.match( "[0,9] {10}", registered_phoneno ):
        print( "match" )
    else:
        print( "Not Match" )
    register_email_id = input( "Enter the email id :" )

    print( register_email_id )
    corporate_phoneno = input( "corporate phoneno :" )
    if re.match( "[0,9] {10}", corporate_phoneno ):
        print( "match" )
    else:
        print( "Not Match" )
    print( corporate_phoneno )
    Branch_phoneno = input( "Enter the Branch phoneno: " )
    if re.match( "[0,9] {10}", Branch_phoneno ):
        print( "match" )
    else:
        print( "Not Match" )
    # print(Branch_phoneno)
    contact_person_name = input( "contacted person name : " )
    print( contact_person_name )
    contact_person_designation = input( "conatct person designation : " )
    print( contact_person_designation )
    contact_person_phoneno = (input( "contact person phoneno : " ))
    if re.match( "[0,9] {10}", contact_person_phoneno ):
        print( "match" )
    else:
        print( "Not Match" )
    print( contact_person_phoneno )
    contact_person_Email = input( "Enter the contact_person_email : " )
    if re.match( '[a-zA-Z0-9@a-z.a-z]', contact_person_Email ):
        print( "match" )
    else:
        print( "Not Match" )
    print( contact_person_Email )


basic_info()
