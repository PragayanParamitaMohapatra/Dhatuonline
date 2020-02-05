def phone_no(phone):
    if len( phone ) > 10:
        return False
    elif len( phone ) == 10:
        return True
    elif phone.isalpha():
        return False
    else:
        False


def otp_validate(otp):
    try:
        if len( otp ) > 6:
            return False
        elif len( otp ) < 6:
            return False
        elif len( otp ) == "":
            return ("Enter the valid otp: ")
        else:
            return ("your otp is{}".format( otp ))
    except:
        print( 'something went wrong' )


def passwd_validate(passwd):
    if len( passwd ) > 6 or len( passwd ) < 10:
        return True

    else:
        return False


def register():
    mob_var = True
    while mob_var:

        phone_num = input( "Enter your phoneno: " )
        val = phone_no( phone_num )
        if val:
            print( "your phone number is{}".format( phone_num ) )
            mob_var = False

    otp_var = True
    while otp_var:
        otp_entry = input( "Enter your otp : " )
        val2 = otp_validate( otp_entry )
        if val2:
            print( "your otp is{}".format( otp_entry ) )
            otp_var = False

    passwd_var = True
    while passwd_var:
        passwd_entry = input( "Give the password: " )
        confirmpass_entry = input( "Confirm the password: " )
        passwd_validate( passwd_entry )
        if passwd_entry == confirmpass_entry:
            print( "congratulation you have successfully registered!!!!!!!!" )
            passwd_var = False


register()
