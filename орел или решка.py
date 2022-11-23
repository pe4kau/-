import random #
import time
print('your balance: 100')
balans = 100

while balans > 0:   
    stavkaM = int(input('your bid:'))   
    if stavkaM > balans:    
        print('It is too much!')
        while stavkaM < balans:
            stavkaM = int(input('your bid:'))   
            while balans > 0:                                       #
                a = int(random.randint(1, 3))
                if a == 1:
                    balans = balans + stavkaM
                    print('you have won! your balance:', balans)
                else:
                    balans = balans - stavkaM
                    print('you have lost! your balance:', balans)
                    if balans == 0:
                        print('YOU HAVE LOST EVERYTHING!!!')
                        break

            
    else:
        a = int(random.randint(1, 3))
        if a == 1:
            balans = balans + stavkaM
            print('you have won! your balance:', balans)
        else:
            balans = balans - stavkaM
            print('you have lost! your balance:', balans)
            if balans == 0:
                        print('YOU HAVE LOST EVERYTHING!!!')
                        break
time.sleep(10)
exit()
