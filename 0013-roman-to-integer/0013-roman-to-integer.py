class Solution(object):
    def romanToInt(self, s):
        values = {
            "I": 1, "V": 5, "X": 10, "L": 50,
            "C": 100, "D": 500, "M": 1000
        }

        total = 0
        for i, symbol in enumerate(s):
            # Subtract if the next symbol has a larger value
            if i + 1 < len(s) and values[symbol] < values[s[i + 1]]:
                total -= values[symbol]
            else:
                total += values[symbol]

        return total
