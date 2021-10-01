import math
def return_coins(coffee_price,eur_inserted):
    print ('This machine accepts banknotes and coins in EURO denomination')
    drink = int(input('How many coffee do you want: '))
    #checking to check if the required amount is valid
    if eur_inserted < (coffee_price*drink) or (eur_inserted < 1):
        print(' error for this transcation!!!!', 'make sure you have'
            ' the right amount and the money is a positive value')
    else:
        change = (eur_inserted-(coffee_price*drink))
        if change <= 0:
            print('you have no change, have a nice coffee')
        else:
            print(' you have been given', "{0:.2f}".format(change),'euors' ' ' 'as your change')
            # coins denomination in euros
            coins = [50, 25, 10, 5, 2, 1]
            coins_returned = []
            for i in coins:
                while change >= i:
                    coins_returned.append(i)
                    #getting the cents from the coins
                    cents = (change%(math.trunc(change)))
                    change = change - i

            print('since this machine only returns coins. take this coins', *coins_returned,"{0:.2f}".format(cents))

return_coins(3.44,500)