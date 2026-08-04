class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_hash = [0] * 26
        s2_hash = [0] * 26

        for i in range(len(s1)):
            s1_hash[ord(s1[i]) - ord('a')] += 1
            s2_hash[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(len(s1_hash)):
            if s1_hash[i] == s2_hash[i]:
                matches += 1

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[l]) - ord('a')
            s2_hash[index] -= 1
            if s1_hash[index] == s2_hash[index]:
                matches += 1
            elif s1_hash[index] - 1 == s2_hash[index]:
                matches -= 1

            index = ord(s2[r]) - ord('a')
            s2_hash[index] += 1
            if s1_hash[index] == s2_hash[index]:
                matches += 1
            elif s1_hash[index] + 1 == s2_hash[index]:
                matches -= 1

            l += 1
        return matches == 26