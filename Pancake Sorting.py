class Solution:
    def pancakeSort(self, arr):
        res = []
        n = len(arr)
        for x in range(n, 1, -1):
            i = arr.index(x)
            if i != x - 1:
                if i != 0:
                    res.append(i + 1)
                    arr[:i + 1] = arr[:i + 1][::-1]
                res.append(x)
                arr[:x] = arr[:x][::-1]
        return res
