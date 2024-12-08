# Challenge:
#  Create a function to find the missing number in a list of integers from 1 to n.

# Test Cases:
# assert find_missing_number([1, 2, 4, 5]) == 3
# assert find_missing_number([3, 5, 6, 1, 2]) == 4
# assert find_missing_number([2]) == []


def find_missing_num(nums):

    if len(nums) <= 1:
        print([])
    else:
        n = len(nums) + 1

        expected_sum = 0
        for i in range(1, n + 1):
            expected_sum += i

        actual_sum = sum(nums)

        missing_num = expected_sum - actual_sum

        print(missing_num)


find_missing_num([3, 5, 6, 1, 2])