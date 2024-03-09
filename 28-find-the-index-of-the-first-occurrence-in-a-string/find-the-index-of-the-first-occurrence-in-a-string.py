class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        input param :
        haystack : str
        needle : str 
        
        output : int 
        """
        if len(needle) > len(haystack):
            return -1
        if not needle:
            return 0
        
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                print(haystack[i:i+len(needle)])
                return i

        return -1