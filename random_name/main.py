import random
f = open('First_Names.txt', 'r+')
first_name = [line for line in f.readlines()]
f.close()
f = open('Last_Names.txt', 'r+')
last_name = [line for line in f.readlines()]
f.close()
i = int(input("How Many Names Would You Like To Generate?: "))
j = 0
while j < i:
    print(random.choice(first_name).replace('\n', ' ')+random.choice(last_name).replace('\n', ' '))
    j+=1