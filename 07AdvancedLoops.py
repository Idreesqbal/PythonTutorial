num1 = [1, 2, 3, 4, 5, 6]
for num in num1:
    if num == 3:
        print('Found')
        continue  # Using continue function inside the loop will allow the conditional function to execute
    # the rest of the code after the condition is meet.
    print(num)
for num in num1:
    if num == 3:
        break  # Using break function inside the loop will break the conditional function
# and the rest of the code will not run.
    print('found')

for num in num1:  # This method is called loop inside loop which basically used to create
    # Combination of all elements between two lists or string
    for letter in 'abc':
        print(num, letter)
for i in range(10):
    print(i)  # used to the repeated tasks over a limited time .
    #nothing


