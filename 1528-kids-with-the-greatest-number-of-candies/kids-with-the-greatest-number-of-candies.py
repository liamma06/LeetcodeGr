class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        max_candy = 0 
        result = []

        for candy in candies:
            max_candy = max(candy, max_candy)

        for candy in candies:
            if (candy + extraCandies) >= max_candy:
                result.append(True)
            else:
                result.append(False)

        return result