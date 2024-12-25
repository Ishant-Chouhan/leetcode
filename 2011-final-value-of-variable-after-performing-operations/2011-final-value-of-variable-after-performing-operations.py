class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        
        
        return (operations.count("--X")+operations.count("X--"))*-1 + (operations.count("X++")+operations.count("++X")) 