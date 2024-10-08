class Solution:
    def platesBetweenCandles(self, s, queries):
        nextCandlePosition = {}
        prevCandlePosition = {}
        nextPos, prevPos = -1, -1

        for pos in range(len(s)-1, -1, -1):
            currChar = s[pos]
            if currChar == "|":
                nextPos = pos
            nextCandlePosition[pos] = nextPos

        prefixPlates = []
        count = 0

        for ind, ch in enumerate(s):
            if ch == "*": count += 1
            prefixPlates.append(count)

            if ch == "|": prevPos = ind
            prevCandlePosition[ind] = prevPos

        ans = []
        for query in queries:
            start_candle_pos = nextCandlePosition[query[0]]
            end_candle_pos = prevCandlePosition[query[1]]

            if end_candle_pos == -1 or start_candle_pos == -1 or start_candle_pos >= query[1] : ans.append(0)
            else:
                ans.append(prefixPlates[end_candle_pos] - prefixPlates[start_candle_pos])
        return ans
        