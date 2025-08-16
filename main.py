import array as arr
array_num = arr.array('i', [1, 3, 7, 1, 7, 3, 9])
print("The array is",array_num)
print("The number of times '3' occurs ",array_num.count(3))
array_num.reverse()
print("The reverse of array is",str(array_num))

