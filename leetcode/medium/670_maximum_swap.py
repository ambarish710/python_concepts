# 670. Maximum Swap
# Medium
# Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.
#
# Example 1:
# Input: 2736
# Output: 7236
# Explanation: Swap the number 2 and the number 7.
#
# Example 2:
# Input: 9973
# Output: 9973
# Explanation: No swap.
#
# Note:
# The given number is in the range [0, 108]

# Brute Force
# Have a temp num and swap each digit with other
# And then check the biggest num

class Solution:
    def maximumSwap(self, num: int) -> int:
        if len(str(num)) == 1 or all(x == str(num)[0] for x in str(num)):
            return num

        max_num = num

        num_list = list(str(num))
        print(num_list)

        for i in range(0, len(num_list)):
            for j in range(i+1, len(num_list)):
                #print("1: {}".format(num_list))
                num_list[i], num_list[j] = num_list[j], num_list[i]
                #print("2: {}".format(num_list))
                temp_num = int(''.join(num_list))
                if temp_num > max_num:
                    max_num = temp_num
                num_list[i], num_list[j] = num_list[j], num_list[i]
                #print("3: {}".format(num_list))
                #print("\n")

        return max_num


if __name__ == "__main__":
    s_obj = Solution()
    print(s_obj.maximumSwap(num=2736))
