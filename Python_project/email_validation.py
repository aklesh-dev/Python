# Email validation using String function.
email = input('Enter your email :') #a@g.in
k,j,d = 0,0,0
if len(email) >= 6:
    if email[0].isalpha():
        # to check @ is only one in the email.
        if ("@" in email) and (email.count("@") == 1):
            # ^ (exjort) operator used to get one of it True.
            if (email[-4] == ".") ^ (email[-3] == "."):
                for i in email:
                    # check space in email
                    if i == i.isspace():
                        k = 1
                        # check i is alphabet
                    elif i.isalpha():
                        # check alphabet in uppercase
                        if i == i.upper():
                            j = 1
                    elif i.isdigit():
                        continue
                    elif i == '_' or i == '.' or i == '@':
                        continue
                    # check other special character or symbols.
                    else:
                        d = 1
                if k == 1 or j == 1 or d == 1:
                    print("wrong email 5")
                else:
                    print(" Right Email.")
            else:
                print(" wrong email 4.")
        else:
            print(" wrong email 3 ")
    else:
        print(" Wrong email 2 / first letter must be alphabet. ")
else:
    print('Wrong email 1 / length of the email must more than 6 character. ')