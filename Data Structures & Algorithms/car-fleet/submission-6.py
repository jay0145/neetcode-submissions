class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        tg = zip(position, speed)
        s = sorted(tg, key=lambda tup: tup[0])

        i = len(s)-1
        fleets = 1
        prevTime = (target-s[i][0]) / s[i][1]

        #print(s)
        while i > -1:
            pos1, sp1 = s[i]

            t1 = (target-pos1) / sp1

            if t1 > prevTime:
                print(f"i: {i} pos1:{pos1}")
                fleets +=1
                prevTime = t1

            i -=1

        #print(fleets)



        return fleets