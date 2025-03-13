class Solution(object):
    def calculateTax(self, brackets, income):
        """
        :type brackets: List[List[int]]
        :type income: int
        :rtype: float
        """
        taxes_due = 0.0 # Sum of taxes due from each bracket
        prev_bracket = 0.0 # Keeps track of the brackets taxed already
        taxed_income = income
        for idx, bracket in enumerate(brackets):
            if taxed_income <= 0:
                return taxes_due

            taxable = abs(bracket[0] - prev_bracket)
            if idx >= len(brackets) - 1 or taxed_income < taxable:
                # In the last bracket, tax all remaining
                taxable = taxed_income

            taxes_due += taxable * (bracket[1]/100.0)
            taxed_income -= taxable
            prev_bracket = bracket[0]
        
        return taxes_due

        