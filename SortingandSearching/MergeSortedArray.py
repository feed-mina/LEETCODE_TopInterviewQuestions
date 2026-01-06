from typing import Optional, List
# Definition for a binary tree node. 
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        print("nums1", nums1)
        print("nums2", nums2)

        print("m", len(nums1))
        print("n", len(nums2))

        nums1[m:] = nums2
        nums1.sort()
        print("nums1", nums1)
        return nums1



        
if __name__ == "__main__":
    sol = Solution()
    result = sol.merge([1,2,3,0,0,0],3,[1,2,3,0,0,0],3)
    print("result", result)
