class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        ones = 0
        zeros = 0

        for s in students:
            if s == 0:
                zeros +=1 
            if s == 1:
                ones += 1

        for s in sandwiches:
            if s == 0:
                if zeros > 0:
                    zeros -= 1
                else:
                    break
            if s == 1:
                if ones > 0:
                    ones -= 1
                else:
                    break
        
        return zeros + ones
                
                    

