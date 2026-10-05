class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        result = []

        #need to sort first 
        intervals.sort(key=lambda x: x[0]) #O(nlog n) sort within

        for i in range(len(intervals)): #O(n)

            #intial just append in 
            if i == 0 :
                result.append(intervals[i])
                continue
            
            #compare to the last thing inside 
            prev_intvl = result[-1]

            #compare first of second is within last of first  
            curr_intvl = intervals[i]

            if (curr_intvl[0] <= prev_intvl[-1]):
                #remove from result previous
                result.pop()

                if prev_intvl[-1] > curr_intvl[-1]:
                    result.append([prev_intvl[0], prev_intvl[-1]])
                else:
                    result.append([prev_intvl[0], curr_intvl[-1]])
            else:
                result.append(curr_intvl)

        return result

        #O(nlog n)


        """
        result = []

        for i in range(len(intervals)):


            first_inter = intervals[i]
            sec_inter = intervals[i+1]

            first_last = first_inter[-1]
            sec_last = sec_inter[-1]

            if sec_last >= first_last:
                new_int = [first_inter[0], sec_inter[0]] 

                result.append(new_int)
        """
