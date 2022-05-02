# Khaoula Ait Soussi: 79155
import sys

# This is to read the text file as an array of lines
with open('inp1.txt', 'r') as file:
  Lines = file.readlines()

# Read the number of vertices from the first line of the file/array
verts = eval(Lines[0])

# Read the number of edges from the second line of the file/array
edges = eval(Lines[1])

# Create an adjacency list that has empty rows. The number of rows is the number of vertices
# Here the index of each row represents a vertex, and each row represents the adjacency list of that vertex
adjLst = [list() for i in range(verts)]

# Fill in the adjacency list while asking the user for edges in the format a b
for i in range(2, len(Lines)):
  a,b = Lines[i].split(" ")
  a = eval(a)
  b = eval(b)
  # Whenever an edge is read from the file/array of lines, we append its vertices to the corresponding rows in the adjacency list
  adjLst[a-1].append(b-1)   
  adjLst[b-1].append(a-1)

# Here we try to get rid of duplicated adjacencies between hair vertices.
# And we try to keep cycles alone (i.e., no cycle's vertex will be attached to a hair vertex)
# For example, the adjacency list of the following edges 
# [(1,2) (2,4) (4,7) (7,3) (3,4)] would become ==> 1: 2 || 2: 4 || 4: 7,3 || 7: 3,4 || 3: 4,7
# As you can see the vertex 2 does not have 1 as an adjacent vertex because 1 already mentions 2 in its adjacency list
# Why? Three reasons:
# To distinquish between hairs that are attached to cycles, and those that are not attached to any cycle which will end up with degree 0 
# So that only cycle vertices are left with degree 2
# We do not want to completely delete hair vertices because we want to compute the surrounding number of hair vertices for each cycle

hairLength = [0] * verts    # This array stores the hair length of each vertex
hairVerts = []              # This array stores vertices that belong to hairs
flag = 0
while(flag == 0):
  flag = 1
  for i in range(verts):
    if len(adjLst[i]) == 1:
      if (not i in hairVerts):
        hairVerts.append(i)
      if i in adjLst[adjLst[i][0]]:
        hairLength[adjLst[i][0]] += 1
        hairLength[adjLst[i][0]] = hairLength[i] + hairLength[adjLst[i][0]]   # Here we keep track of the length of the path coming off of each vertex
        flag = 0      # This means we still have work to clean (i.e., there are still hair vertices adjacent to other vertices)
        adjLst[adjLst[i][0]].remove(i)

# Check if there is any vertex of degree 0, that means a potential hair is not attached to any cycle
# Also do some prepwork for the next stage which is to assemble all degree 2 vertices in one list
twoDegVer = []
for i in range(verts):
  if len(adjLst[i]) == 2:
    twoDegVer.append(i)
  elif len(adjLst[i]) == 0:
    print("The graph is not a collection of hairy cycles because there is a potential hair that is not attached to any cycle!")
    sys.exit()
  elif len(adjLst[i]) > 2:
    print("The graph is not a collection of hairy cycles because there is at least one component that is made up of more than one cycle!")
    sys.exit()

# All the remaining vertices now must be of length 2, i.e., part of a cycle
visited = 0
length = len(twoDegVer)
closedCycle = 0
while(visited != length):
  hairVerCount = 0               # This keeps track of the number of vertices surrounding each cycle
  start = twoDegVer[0]
  hairVerCount += hairLength[start]
  prev_ver = start
  next_ver = adjLst[start][0]
  twoDegVer.remove(next_ver)    # Here whenever a 2-degree vertex is visited, we remove it from the array twoDegVer so that we can easily access the start of the next cycle
  current_ver = next_ver
  cycleDeg = 0
  while(current_ver != start):
    for i in range(2):
      if(adjLst[current_ver][i] != prev_ver):
        next_ver = adjLst[current_ver][i]
        break
    hairVerCount += hairLength[current_ver]
    visited += 1
    cycleDeg += 1
    twoDegVer.remove(next_ver)
    prev_ver = current_ver
    current_ver = next_ver
  visited += 1
  closedCycle += 1
  adjLst[start].append(cycleDeg)    # This stores the size of each cycle at the end of its starting vertex
  adjLst[start].append(hairVerCount)  # This stores the number of vertices surrounding each cycle at the end of its adjacency list

print("Number of Hairy Cycle Components: ", closedCycle)
k = 1
for i in range(verts):
  length = len(adjLst[i])
  if(length == 4):
    print("\tComponent", k ," ==> Cycle Start: ", i+1 ,"; Cycle Size: ", adjLst[i][2] + 1 , "; Number of hair vertices: ", adjLst[i][3])
    k += 1
