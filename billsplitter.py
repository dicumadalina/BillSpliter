# write your code here
import random

my_dict = {}
total_number = int(input('Enter the number of friends joining (including you):\n'))
if total_number <= 0:
    print('No one is joining for the party')
else:
    print('Enter the name of every friend (including you), each on a new line:')
    for i in range(total_number):
        input_name = input()
        my_dict[input_name] = 0
    print()
    total_bill = float(input("Enter the total bill value:\n"))
    print()
    lucky = input("Do you want to use the \"Who is lucky?\" feature? Write Yes/No:\n")
    if lucky.lower() == "yes":
        random_value = random.choice(list(my_dict.keys()))
        print()
        print(f"{random_value} is the lucky one!")
        rounded_bill = round(total_bill / (total_number-1), 2)
        for item in my_dict.keys():
            my_dict.update({item: rounded_bill})
        my_dict.update({random_value: 0})
        print()
        print(my_dict)
    elif lucky.lower() == "no":
        print("No one is going to be lucky")
        rounded_bill = round(total_bill / total_number, 2)
        for item in my_dict.keys():
            my_dict.update({item: rounded_bill})
        print()
        print(my_dict)
    else:
        print(my_dict)
