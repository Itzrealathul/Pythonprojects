total=int(input("Enter total number of numbers:"))
mean=float(input("Enter the mean:"))
correct_number=int(input("Enter the correct number:"))
wrong_number=int(input("Enter the wrong number:"))
sum=(mean*total)
correct_sum=sum-wrong_number+correct_number
print("The correct sum is=",correct_sum)
correct_mean=correct_sum/total
print("The correct mean is=",correct_mean)