import copy


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        tempList = copy.deepcopy(nums)
        tempList.sort()
        result = []

        for i in nums:
            if i in nums:
                result.append(tempList.index(i))
            else:
                result.append(0)

        return result