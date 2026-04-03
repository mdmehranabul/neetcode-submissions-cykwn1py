class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # res_right, res_left =[],[]
        # prod=1
        # res=[]
        # for n in nums:
        #     prod*=n
        #     res_right.append(prod)
        
        # prod = 1

        # for n in (nums[::-1]):
        #     prod*=n
        #     res_left.append(prod)

        # res_left = res_left[::-1]

        # for i in range(len(nums)):
        #     right = res_right[i-1] if i-1>=0 else 1
        #     left = res_left[i+1] if i+1<len(nums) else 1
        #     res.append(left*right)

        # return res

# Time Complexity - O(n)
# Space Complexity - O(n)

        res=[1]*len(nums)
        pre,post=1,1

        for i in range(len(nums)):
            res[i]=pre
            pre*=nums[i]

        for i in range(len(nums)-1,-1,-1):
            res[i]*=post
            post*=nums[i]
        return res

# Time Complexity - O(n)
# Space Complexity - O(1)