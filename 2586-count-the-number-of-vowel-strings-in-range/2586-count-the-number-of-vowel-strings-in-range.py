class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        c=0
        vowel="aeiouAEIOU"
        while left<=right:
            x=words[left]
            if x[0] in vowel and x[len(x)-1] in vowel:
                c+=1
            left+=1
        return c
        