import random 
import string

def psw_generator():
    while True:  
        try:
            lenght_psw = input('How many characters should your password have? :D\n-------> ')
            lenght_pswI = int(lenght_psw)
            if lenght_pswI >= 6:            
                pwd = ''.join(random.choice(str(random.randint(1,9))+ string.ascii_letters + string.ascii_uppercase + string.ascii_lowercase + string.digits + '!@#$%^&*()') for l in range(lenght_pswI))
                print('<----Your Password is: ' + pwd + '---->')
                break
            else:
                print('Your password must be at least 6 characters long!!')
                pass
        except (ValueError):
            print('Error! Invalid number!')

psw_generator()
