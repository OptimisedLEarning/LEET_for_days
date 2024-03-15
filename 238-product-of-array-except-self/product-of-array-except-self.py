class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
    

        p = [1] * n
        s = [1] * n
    
    
        for i in range(1, n):
            p[i] = p[i - 1] * nums[i - 1]
    
    # Calculate suffix products
        for i in range(n - 2, -1, -1):
            s[i] = s[i + 1] * nums[i + 1]
    
    # Calculate the final result by multiplying prefix and suffix products
        result = [p[i] * s[i] for i in range(n)]
    
        return result


        
        
        