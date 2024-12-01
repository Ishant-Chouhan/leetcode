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
            larger_box=max(capacity)
            boxes+=larger_box
            capacity.pop(capacity.index(larger_box))

        return lenght-len(capacity)