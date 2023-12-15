
list_of_numbers =(input("Enter a list of numbers separated by comma").split(","))

total_sum=0
even_num_list=[]
odd_num_list=[]

for i in range(0,len(list_of_numbers)):
    total_sum += int(list_of_numbers[i])
    avg=total_sum/len(list_of_numbers)
    max_value=max(list_of_numbers)
    min_value=min(list_of_numbers)

    if int(list_of_numbers[i]) % 2 ==0:
        even_num_list.append(int(list_of_numbers[i]))

    else:
        odd_num_list.append(int(list_of_numbers[i]))



print("Your List of NUmber: ",list_of_numbers)
print("total sum of your numbers: ",total_sum)
print("Your average is: ",avg)
print("Maximum value in your list: ",max_value)
print("Minimum value in your list: ",min_value)
print("Even numbers in your list: ",even_num_list)
print("Odd numbers in your list: ",odd_num_list)

