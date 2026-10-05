class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0 :
            return 0

        win_freq = {} 
        longest = float("-inf")
        curr_length =  0
        left = 0 

        for right in range(len(s)):
            letter = s[right]

            if letter not in win_freq:
                win_freq[letter] = 1

            elif letter in win_freq:
                win_freq[letter] += 1

                #here having some way to store postiion seen so you just jump to this point instead of looping through to find. 
                while win_freq[letter] > 1:
                    left_letter = s[left]
                    win_freq[left_letter] -= 1 
                    left += 1 

            curr_length = right - left + 1 
            longest = max(curr_length, longest)

        return longest  # O(n)

        #maybe instead use a set since it never relaly extends like to more than 1 liek in our case it does but we can have a check and reduce first or soemthing like that 

        """
            abc a bcbb 
             L  R

            win_freq = {
                a : 1 
                b : 1 
                c : 1 
            }

            curr_length = 3

            longest = 3
        """

            