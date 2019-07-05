# -*- coding: utf-8 -*-
# @Time        : 2019/6/24 9:07
# @Author      : tianyunzqs
# @Description : 


def firstMissingPositive(nums):
	miss_num = 1
	nums.sort()
	for num in nums:
		if num < miss_num:
			continue
		elif num > miss_num:
			return miss_num
		else:
			miss_num += 1

	return miss_num


# nums = [1,2,0]
# nums = [3,4,-1,1]
nums = [7,8,9,11,12]

print(firstMissingPositive(nums))
