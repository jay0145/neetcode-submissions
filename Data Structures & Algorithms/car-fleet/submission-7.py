class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        tg = zip(position, speed)
        s = sorted(tg, key=lambda tup: tup[0])

        i = len(s) - 1
        stack = []

        #print(s)
        while i > -1:
            pos1, sp1 = s[i]
            t1 = (target - pos1) / sp1
            if i == len(s) - 1:
                stack.append(t1)
                i-=1
                continue

            if t1 > stack[-1]:
                stack.append(t1)
                #print(f"i: {i} pos1:{pos1}, pos2:{pos2}")
                
            i -=1




        return len(stack)