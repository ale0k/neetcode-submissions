class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        u = 0
        d = len(matrix) - 1
        while u <= d:
            midr = (u + d) // 2
            l = 0
            r = len(matrix[0]) - 1
            closest_diff = 10000
            while l <= r:
                midc = (l + r) // 2
                check = matrix[midr][midc]
                if check == target:
                    return True
                elif check < target:
                    l = midc + 1
                else:
                    r = midc - 1
                print(closest_diff, check)
                closest_diff = min(closest_diff, target - check)
            if closest_diff > 0:
                u = midr + 1
            else:
                d = midr - 1
        
        return False
