def second_largest(nums):
    if len(nums) < 2:
        return "List must contain at least two numbers"

    largest =0
    second_largest = 0
    for i in nums:
        if i > largest:
            second_largest = largest
            largest = i
        elif i > second_largest and i != largest:
            second_largest = i

    return second_largest


num_list = [int(x) for x in input("Enter the list of numbers separated by ,: ").split(",")]
print("Second largest number in the list:", second_largest(num_list))
