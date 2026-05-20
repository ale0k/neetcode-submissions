class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        u = 0
        d = len(matrix) - 1
        while u <= d:
            midr = (u + d) // 2
            if matrix[midr][-1] < target:
                u = midr + 1
            elif matrix[midr][0] > target:
                d = midr - 1
            else:
                break

        l = 0
        r = len(matrix[0]) - 1
        while l <= r:
            midc = (l + r) // 2
            check = matrix[midr][midc]
            print(check)
            if check == target:
                return True
            elif check < target:
                l = midc + 1
            else:
                r = midc - 1
    
        return False
