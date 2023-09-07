numbers = [1, 2, 34, 56, 7, 23, 23, 12, 1, 2, 3, 34, 56]
sumOfNums = 0
count = 0
for number in numbers:
    sumOfNums += number
    count += 1
average = sumOfNums / count
print("The list of numbers is:", numbers)
print("The average of all the numbers is:", average)

test_list = [4, 5, 8, 9, 10, 17]

# printing list
print("The original list : " + str(test_list))
# Median of list
# Using loop + "~" operator
test_list.sort()
mid = len(test_list) // 2
res = (test_list[mid] + test_list[~mid]) / 2

print("something")