class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        array = []
        print(array)

        for n in nums:
            array.append(n)
  
        for n in array:
            print('current n value ', n)
            print('removing ', n, ' from ', nums)
            if n == val:
                nums.remove(n)

        return len(nums)