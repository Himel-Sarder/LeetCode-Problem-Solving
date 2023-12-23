class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x, y = 0, 0
        match_with_me = {(0,0)}
        for direction in path:
            if direction == 'N':
                y += 1
            elif direction == 'S':
                y -= 1
            elif direction == 'E':
                x += 1
            elif direction == 'W':
                x -= 1
                
            if (x, y) in match_with_me:
                return True
        
            match_with_me.add((x, y))
        
        return False

  #Himel Sarder
  #Dept. Of CSE, BSFMSTU
