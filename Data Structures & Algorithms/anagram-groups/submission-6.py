class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_anagrams = {}
        for string in strs:
            char_map = [0] * 26
            for char in string:
                index = ord(char) - ord('a')
                char_map[index] += 1
            tup = tuple(char_map)
            if tup not in grouped_anagrams:
                grouped_anagrams[tup] = []
            grouped_anagrams[tup].append(string)
        
        return list(grouped_anagrams.values())