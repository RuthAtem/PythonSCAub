numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20] 

# this is the section "a" of exercise 4
for i in range(len(numbers)):
    print(numbers[i])
print("\n") 

# this is the section "b" of exercise 4
for i in range(len(numbers)):
    print(numbers[i] ,"and its square is",numbers[i]**2)
print("\n") 
  
# this is the section "b" of exercise 4
total_numbers = 0
for i in range(len(numbers)):
    total_numbers = total_numbers + numbers[i]
print("total of all the numbers is",total_numbers)
print("\n") 

# this is the section "b" of exercise 4
product_numbers = 1
for i in range(len(numbers)):
    product_numbers = product_numbers*numbers[i]
print("product of all the numbers is",product_numbers)
print("\n") 