from strategies.discrepancy_strategy import DiscrepancyStrategy


class SumDiscrepancyStrategy(DiscrepancyStrategy):
    def __init__(self, max_sum):
        self.max_sum = max_sum

    def detect(self, doc):
        try:
            row_sum = sum(int(''.join(filter(str.isdigit, value))) for value in doc['body'][0] if value.replace('%', '').isdigit())
            if row_sum > self.max_sum:
                return {'first_row_sum': 'Sum of the first row is higher than the given value'}
        except ValueError:
            return {'first_row_sum': 'Cannot compute the sum'}
        return {}