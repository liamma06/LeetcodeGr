class Solution:
    def decodeString(self, s: str) -> str:
        final = [] 
        curNum = 0
        curString =""

        for char in s:
            if char == "[":
                final.append(curString)
                final.append(curNum)
                curNum = 0
                curString =""
            elif char == "]":
                num = final.pop()
                prevString = final.pop()
                curString = prevString + num*curString
            elif char.isdigit():
                curNum = curNum*10 +int(char)
            else:
                curString += char
        return curString


                