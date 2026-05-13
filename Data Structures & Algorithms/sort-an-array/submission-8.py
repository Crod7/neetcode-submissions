class Solution:

    def sortArray(self, nums: List[int]) -> List[int]:
        # sort an array -> sorting algo
        # nlogn linearithmic time, heap sort or mergesort
        # 
        # mergesort
        # break my array down to single indicie arrays
        # recombine them back in order

        def breakdown(arr, l,r):
            #
            if l == r:
                return arr

            m = (l + r) // 2
            breakdown(arr, l, m)
            breakdown(arr, m + 1, r)

            return combine(arr, l,m,r)

        def combine(arr, l, m, r):
            #
            left, right = arr[l:m + 1], arr[m + 1 : r + 1]
            i,j,k = l, 0, 0

            while j < len(left) and k < len(right):
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    j += 1
                else:
                    arr[i] = right[k]
                    k += 1
                i += 1
            
            while j < len(left):
                arr[i] = left[j]
                j += 1
                i += 1

            while k < len(right):
                arr[i] = right[k]
                k += 1
                i += 1

            return arr

        return breakdown(nums, 0, len(nums)-1)



