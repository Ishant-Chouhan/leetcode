class Solution(object):
    def minimizeXor(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        # Count the number of set bits in num2
        countSetBits = bin(num2).count('1')
        
        # Initialize x to 0
        x = 0
        
        # Start from the highest bit and try to set bits in x
        for i in range(30, -1, -1):
            # Check if the current bit is set in num1
            if (num1 & (1 << i)) != 0:
                # If we still need to set bits in x, set this bit
                if countSetBits > 0:
                    x |= (1 << i)
                    countSetBits -= 1
        
        # If we still need to set bits in x, set the lowest bits
        for i in range(31):
            if countSetBits > 0 and (x & (1 << i)) == 0:  # If this bit is not already set
                x |= (1 << i)
                countSetBits -= 1
        
        return x
        


            
            
        


        