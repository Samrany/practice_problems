
def numIslands(grid):
        
    length = len(grid[0])
    grid.insert(0, [0]*length)
    grid.append([0]*length)
    
    
    for row in grid:
        for idx, value in enumerate(row):
            if value == 0 and row[idx-1] == 0 and row[idx+1] == 0:
                print("yes")
            else:
                print("no")



numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
])