class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        dic = defaultdict(int)

        for i in s1:
            dic[i] += 1

        print(dic)

        for l in range(len(s2)):
            r = l
            temp = dic.copy()

            while temp[s2[r]] > 0:
                #print(f"elem: {s2[r]} l: {l} r: {r} temp: {temp}")
                temp[s2[r]] -= 1
                if r == len(s2)-1:
                    break
                r += 1
            
            isEmpty = True
            for i in temp.values():
                if i > 0:
                    isEmpty = False
            if isEmpty:
                return True

        
        return False