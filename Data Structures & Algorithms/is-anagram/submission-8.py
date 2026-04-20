class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}
        for x in s:
            count[x] = count.get(x, 0) + 1

        for x in t:
            if x not in count:
                return False
            
            # Subtract 1 from the tally
            count[x] -= 1

            # THIS MUST BE INDENTED: Check immediately after subtracting
            if count[x] < 0:
                return False 

        return True