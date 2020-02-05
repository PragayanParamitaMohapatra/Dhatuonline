def phone_no(phone):
    if len( phone ) > 10:
        return False
    elif len( phone ) == 10:
        return True
    elif phone.isalpha():
        return False
    else:
        False


option = {"1": "Register with phone_number", "2": "Register with Email"}
# print("select one of them\n")
# print("1. Register_phone_number")
# print("2. Register_Email_Id")
choice = input( " choose one of them for reset your password 1/2:  " )
var1 = "guddi123"
if option[choice] == "Register with phone_number":
    mob_var = True
    while mob_var:
        register_num_entry = input( "Enter your phoneno: " )
        val = phone_no( register_num_entry )
        if val:
            print( "your phone number is {}".format( register_num_entry ) )
            mob_var = False
            reset_pass = input( "Reset your password:" )

            if var1 != reset_pass:

                print( "Your password is reset " )
            else:
                print( "Re-enter the password" )

if option[choice] == "Register with Email":
    email_var = True
    while email_var:
        email_input = input( "Enter your registered id:\n " )
        print( email_input )
        email_var = False
    reset_pass = input( "Reset your password:" )
    new_pass = []
    if var1 != reset_pass:
        new_pass.append( reset_pass )
        print( "Your password is reset and your new password is".format( new_pass ) )
    else:
        print( "Re-enter the password" )
