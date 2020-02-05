def phone_no(phone):
    if len( phone ) > 10:
        return False
    elif len( phone ) == 10:
        return ("your phone number is {} ".format( phone ))
    else:
        return False
    return phone


def email(email):
    if '@' in email and 'gmail' in email and '.' in email:
        return ("your email is{}".format( email ))
    else:
        print( "Not Match" )


def person(people):
    for pep in people:
        if pep.isalpha():
            return True
        else:
            return False
    return people


def pincode(pin):
    if pin.isalpha():
        return False
    elif len( pin ) == 6:
        return ("your pin code is {}".format( pin ))
    else:
        return False
    return pin


def basic_info():
    company_name = input( "Name of the company: " )

    print( company_name )
    const_var = True
    while const_var:
        constitution_of_company = {"1": "Public Limited", "2": "Private Limited", "3": "Parternship", "4": "LLP",
                                   "5": "Proprietoriship"}
        constitution_of_company_input = input( "Name of constitution_of_company: " )
        if constitution_of_company_input in constitution_of_company.keys():
            print( constitution_of_company.get( constitution_of_company_input ) )
            const_var = False
        elif constitution_of_company_input == "":
            print( "Invalid input" )
        else:
            print( 'constitution_of_company is invalid' )
    category_var = True
    while category_var:
        company_category = {"1": "micro", "2": "small", "3": "large", "4": "medium"}

        company_category_input = input( "company category: " )

        if company_category_input in company_category:
            print( company_category.get( company_category_input ) )
            category_var = False

        else:
            print( "please select go through valid choice" )
    manufact_var = True
    while manufact_var:
        manufacture_trader_input = input( "select the manufacture: " )
        manufacture_trader = {"1": "manufacturer", "2": "trader1", "3": "trader2", "4": "trader3"}
        if manufacture_trader_input in manufacture_trader:
            print( manufacture_trader.get( manufacture_trader_input ) )
            manufact_var = False
        else:
            print( "select the valid manufacture" )

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

    state = input( " Enter the state : " )
    state_select = {"1": "odisha", "2": "karnatk", "3": "andhra", "4": "up"}
    if state in state_select:
        print( state_select.get( state ) )
    else:
        print( " please go through proper choice :" )

    # pin_var=True
    # while pin_var:
    pin_code = input( " Enter the pincode : " )
    x = pincode( pin_code )
    print( x )
    #     if re.match("[0,9] {6}", pin_code):
    #         print("your pincode is".format(pin_code ))
    #         pin_var=False
    #     else:
    #         print("Not Match")
    phn_var = True
    while True:
        registered_phone = input( "Enter the Registered phoneno. :" )

        res = phone_no( registered_phone )
        print( res )
        phn_var = False
        break

    registered_email = input( "Enter the Registered email :" )
    result = email( registered_email )
    print( result )
    corporate_phone = (input( "Enter the Corporate phoneno. :" ))
    res1 = phone_no( corporate_phone )
    print( res1 )
    branch_phone = input( "Enter the branch phoneno. :" )
    res2 = phone_no( branch_phone )
    print( res2 )
    contact_person_name = input( "contacted person name : " )
    val = person( contact_person_name )
    print( val )
    contact_person_designation = input( "conatct person designation : " )
    val1 = person( contact_person_designation )
    print( val1 )
    contactperson_phone = input( "Enter the Registered phoneno. :" )
    val2 = phone_no( contactperson_phone )
    print( val2 )
    contact_person_email = input( "Enter contact person email : " )
    val3 = email( contact_person_email )
    print( val3 )


basic_info()

# basic_info()
