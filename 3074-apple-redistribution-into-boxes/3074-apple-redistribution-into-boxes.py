class Solution(object):
    def minimumBoxes(self, apple, capacity):
        """
        :type apple: List[int]
        :type capacity: List[int]
        :rtype: int
        """
        lenght=len(capacity)
        total_apples=sum(apple)
        boxes=0
        while boxes < total_apples :
            
            boxes+=max(capacity)
            capacity.pop(capacity.index(max(capacity)))

        return lenght-len(capacity)