"""Given an array arr[] of n integers, construct a Sum Array sum[] (of same size)
such that sum[i] is equal to the sum of all the elements of arr[] except arr[i]."""

array = [4, 5, 7, 3, 10, 1]

sum_minus_element = [sum(array) - item for item in array]
print(sum_minus_element)
