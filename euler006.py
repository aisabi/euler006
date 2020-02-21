# difference between the:
# sum of the squares of the first n natural numbers and the square of the sum
# example : sumSquareDifference(10) should return 3025 − 385 = 2640 
def sumSquareDifference(n):
    # use i = n as a counter and as number I'll put in empty list 'listeB'
    i = n
    listeA =[]
    listeB =[]
    # in this while loop : append n calculation square in 'listeA' and append i number in 'listeA'
    while i > 0:
        n = i ** 2
        listeA.append(n)
        listeB.append(i)
        i = i - 1

    # sum of 'ListA' and sum of 'listeB' is squared
    resultatA = sum(listeA)
    resultatB = (sum(listeB))**2
    
    difference = resultatB - resultatA
    return difference


print('Sum Square Difference : ',sumSquareDifference(10))