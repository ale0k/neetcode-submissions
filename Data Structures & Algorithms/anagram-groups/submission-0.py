class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        string_map = {}
        for string in strs:
            string_hash = str(sorted(string))
            if string_hash not in string_map:
                string_map[string_hash] = []
            string_map[string_hash].append(string)
        return list(string_map.values())