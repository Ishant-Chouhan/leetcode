class Solution:
    def maxKelements(self, nums, k):
        # Max heap by negating the values (since heapq in Python is a min heap by default)
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)
        
        score = 0
        for _ in range(k):
            n = -heapq.heappop(max_heap)  # Get the largest element
            score += n  # Add to score
            heapq.heappush(max_heap, -(n // 3 + (1 if n % 3 else 0)))  # Push ceil(n / 3) back
            
        return score

        