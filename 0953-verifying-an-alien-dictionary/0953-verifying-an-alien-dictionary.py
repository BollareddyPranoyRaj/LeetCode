class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dct={}
        for i in range(len(order)):
            dct[order[i]]=i
        for i in range(len(words)-1):
            fir=words[i]
            sec=words[i+1]
            found=False
            for j in range(min(len(sec),len(fir))):
                if fir[j]==sec[j]:
                    continue
                elif dct[fir[j]]<dct[sec[j]]:
                    found=True
                    break
                else:
                    return False
            if not found and len(fir)>len(sec):
                return False      
        return True