def Emerald(amount, weight):
    amount == int
    consective = 0
    weight == list()
    count = 0
    for amount in list(weight):
        count += 1
        if weight % 2 == int:
            weight += consective
        elif weight % 2 == float:
            consective == 0
        if count == amount:
            print (consective)
            break
Emerald(13,[2,3,4,4,5,6,1,2,2,2,1,8,2])