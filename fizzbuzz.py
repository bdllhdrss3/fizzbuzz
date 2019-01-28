#making a fizz buzz app
#creating input of list

list1 = input("Enter list one : ")
list2 = input("Enter list two : ")
length1 = len(list(list1))
length2 = len(list(list2))
sumation = length1 + length2
fizz = sumation%3
buzz = sumation%5

#now creating the fizzbuzz function
def fizzbuzz():
    if buzz == 0 and fizz == 0:
        print('fizzbuzz')
    elif buzz == 0:
        print('buzz')
    elif fizz == 0:
        print('fizz')
    else:
        print('the lists are neither  a fizzbuzz nor buzz nor fizz')
    
       
    
    
fizzbuzz()


        