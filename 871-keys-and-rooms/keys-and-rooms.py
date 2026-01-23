class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        queue = [0]

        while queue:
            room = queue.pop(0)

            if room in visited:
                continue

            visited.add(room)
            
            #add all keys and when loop through check if all is already visisted 
            for key in rooms[room]:
                queue.append(key)

        return len(visited) == len(rooms)