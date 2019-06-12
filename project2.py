# u played me on this one 
import itertools
from collections import deque

# retrieve data from txt file
with open('input1.txt') as textFile:
    graph = [line.split() for line in textFile]

#functions
def findCycles(graph): 
  # dfs is used to find cycles and add them to a list

  # variable declaration
  stack = []
  stack.append(0)
  visitedArray = [False]  * len(graph)
  visitedArray[0] = True
  overallPath = [-1]
  cycles = []
  # dfs
  while len(stack) != 0: 
    currentNode = stack.pop()
    visitedArray[currentNode] = True
    previousNode = 0
    previousNode = overallPath[-1]
    # keep track of path, this will be used to detect cycles
    overallPath.append(currentNode)
    i = 0
    adjacentEdges = [] #used to properly add adjacent nodes onto the stack in the right order
    # adding adjacent nodes
    for node in graph[currentNode]:
      # determine if a cycle has been found 
      if i !=previousNode and i !=currentNode and node=='1':
        if graph[currentNode][previousNode]=='1': #extra if check to deal with instances where the travelsal "jumps to a whole different place" because of the order of the stack
          # if node i is in the path, found a cycle, add this cycle onto cycles list
          if i in overallPath: 
            cycleStart = overallPath.index(i)
            currentCycle = overallPath[cycleStart:]
            currentCycle = set(currentCycle)
            if currentCycle not in cycles: 
              cycles.append(currentCycle)
      # add adjancent edges
      if visitedArray[i] == False and node == '1':
        if i not in stack:
          adjacentEdges.append(i)
        else:
          del stack[stack.index(i)]
          adjacentEdges.append(i)
      i +=1
    for node in reversed(adjacentEdges):
      stack.append(node)
  return cycles

def CountLayerNumber(graph):
  #bfs is used to determine layers

  # variable declaration
  queue = deque([])  
  levels = -1
  visitedArray = [False] * len(graph)
  # starting algo, beginning node is always '0'
  queue.append(0)
  queue.append(-1)
  visitedArray[0] = True
  while len(queue) != 0:
    currentNode = queue.popleft()
    # check for number of levels, -1 is used as a flag to check each level
    if currentNode == -1: 
      levels +=1
      queue.append(-1)
      # peek to see if head is -1, if so all levels have been reached so kill the algo
      if queue[0] == -1: 
        break
      else: 
        continue
    # adding adjacent nodes to queue
    index = 0
    for node in graph[currentNode]:
      if visitedArray[index] == False and node == '1':
        visitedArray[index] = True
        queue.append(index)
      index = index +1
  return levels   

def main():

  cycles= findCycles(graph)
  longestCycle= 0
  # iterate through arrays
  for cycle in cycles:
    if len(cycle) > longestCycle: 
      longestCycle = len(cycle)

  print('Number of cycles: %d' %len(cycles))
  print('longest Cycle: %s' %longestCycle)
  print('Number of layers : %d' %CountLayerNumber(graph))




main()
