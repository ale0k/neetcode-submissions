class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ''
        for string in strs:
            string_len = len(string)
            encoded_string += f'{string_len}#{string}'
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strings = []
        encoded_string_len = len(s)
        i = 0
        print(s)
        while i < encoded_string_len:
            string_len_indicator = ''
            string = ''
            while True:
                string_len_indicator += s[i]
                i += 1
                if s[i] == '#':
                    i += 1
                    break
            string_len = int(string_len_indicator)
            for j in range(i, i + string_len):
                string += s[j]
            decoded_strings.append(string)
            i += string_len
        return decoded_strings

