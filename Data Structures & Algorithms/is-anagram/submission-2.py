class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}
        for i in s:
            dict_s[i] = 0
        for i in t:
            dict_t[i] = 0
        for i in s:
            dict_s[i] += 1
        for i in t:
            dict_t[i] += 1
        dictionary = {}
        if len(dict_s) > len(dict_t):
            dictionary = dict_s
        else:
            dictionary = dict_t
        for i in dictionary:
            try:
                if not(dict_s[i] == dict_t[i]):
                    return False
            except:
                return False
        return True        