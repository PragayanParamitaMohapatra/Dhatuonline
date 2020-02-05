def bussiness_info():
    while True:
        choice = ["True", "False"]
        while True:
            user_input = input( "Enter the choice  True or False : " )
            # while True:
            if user_input in choice:
                if user_input == "True":
                    # while True:
                    user_gstin = input( "Enter your GSTIN : " )
                    print( "GSTIN Number is {}".format( user_gstin ) )
                # break
                # else:
                #     print("Not Match")
                #     print(user_gstin, "\n")
                else:
                    print( "enter valid gstin" )
            else:
                print( "You are unregistered." )
                break
        quality_mgmt = input( "Enter the Quality Management System : " )
        print( quality_mgmt )
        turn_over = {"2017": "1000", "2018": "2000", "2019": "3000"}
        while True:
            turn_over_lastyear = input( "Enter the turn over year from (2017-2019): " )
            if turn_over_lastyear in turn_over.keys():
                print( "The result of turn over  year is : ", turn_over.get( turn_over_lastyear ) )
            else:
                print( 'this year is not there' )
        payment_term = {"1": "immediatepayment", "2": "credit"}
        while True:
            user_input_payment = input( "Enter the payment option 1(imediate)/2(credit) :" )

            if user_input_payment in payment_term:
                if user_input_payment == "1":
                    print( "you can payment immediately." )
                if user_input_payment == "2":
                    p = int( input( "If you select credit then how many days:" ) )
                    print( p )
                bank = {"1": "SBI", "2": "UCO", "3": "HDFC", "4": "ICICI", "5": "union bank of india",
                        "6": "CORPORATION", "7": "Canara"}
                existing_facility = input( "select your bank : " )
                if existing_facility in bank.keys():
                    print( bank.get( existing_facility ) )
                else:
                    print( "No more option" )
                name_principal_bank = input( "Enter the principal bank :  " )
                if name_principal_bank in bank:
                    print( bank.get( name_principal_bank ) )
                else:
                    print( "principal bank is not available." )
            else:
                print( "invalid input" )


bussiness_info()
