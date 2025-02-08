from collections import defaultdict, Counter
import heapq

class NumberContainers:

    def __init__(self):
        self.elementIndices = defaultdict(list)
        self.indexToElement = {}
        self.indicesRemoved = defaultdict(Counter)

    def change(self, index, number) :
        # element already exists on this index
        if index in self.indexToElement and self.indexToElement[index] == number:
            return
        
        # if some other element exists at the index, mark it to remove
        if index in self.indexToElement:
            prevVal = self.indexToElement[index]
            self.indicesRemoved[prevVal][index] += 1
        
        self.indexToElement[index] = number
        heapq.heappush(self.elementIndices[number], index)
            

    def find(self, number):
        ## if the element exists in array
        if self.elementIndices[number]:
            mn = self.elementIndices[number][0]
            while self.indicesRemoved[number][mn] and self.elementIndices[number]:
                self.indicesRemoved[number][mn] -= 1
                heapq.heappop(self.elementIndices[number])
                if not self.elementIndices[number]:
                    break
                mn = self.elementIndices[number][0]
            if self.elementIndices[number]:
                return mn
        return -1



# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)