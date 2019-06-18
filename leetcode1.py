"""
    leetcode 31 下一个排列
    实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典中下一个更大的序列
    如果不存在下一个更大的序列，则将数字重新排列成最小的排序(即升序排列)
    必须原地修改，只允许使用额外常数空间
    例：
        1,2,3-->1,3,2
        3,2,1-->1,2,3
        1,1,5-->1,5,1
"""
class Solution:
    def nextPermutation(self,nums):
        r=0
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                nums[i],nums[i+1]=nums[i+1],nums[i]
                r=1
                break
        if r==0:
            for i in range(len(nums)-1):
                for j in range(i+1,len(nums)):
                    if nums[i]>nums[j]:
                        nums[i],nums[j]=nums[j],nums[i]

#测试代码
a=Solution()
s=[1,1,3]
a.nextPermutation(s)
print(s)

时间超时
