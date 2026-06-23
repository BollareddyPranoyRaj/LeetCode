class Solution:
    def calPoints(self, op: List[str]) -> int:
        new=[]
        def is_empty():
            return len(new)==0
        for i in range(len(op)):
            if op[i]=="C":
                if not is_empty():
                    new.pop()
                continue
            if op[i]=="D":
                if not is_empty():
                    new.append(new[-1]*2)
                continue
            if op[i]=="+":
                if not is_empty():
                    new.append(new[-1]+new[-2])
                continue
            new.append(int(op[i]))
        return sum(new)
        