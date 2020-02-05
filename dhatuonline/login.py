def phone_no(phone):
    if len( phone ) > 10:
        return False
    elif len( phone ) == 10:
        return True
    elif phone.isalpha():
        return False
    else:
        False


def passwd_validate(passwd):
    if len( passwd ) > 6 or len( passwd ) < 10:
        return True

    else:
        return False


def login():
    mob_var = True
    while mob_var:
        phone_num = input( "Enter your phoneno: " )
        val = phone_no( phone_num )
        if val:
            print( "your phone number is{}".format( phone_num ) )
            mob_var = False
    passwd_var = True
    while passwd_var:
        passwd_entry = input( "Give the password: " )
        confirmpass_entry = input( "Confirm the password: " )
        passwd_validate( passwd_entry )
        if passwd_entry == confirmpass_entry:
            print( "congratulation you have successfully login into our Dhatuonline!!!!!!!!" )
            passwd_var = False


login()
