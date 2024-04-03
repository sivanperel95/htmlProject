from strategies.discrepancy_strategy import DiscrepancyStrategy


class TitleLengthStrategy(DiscrepancyStrategy):
    def __init__(self, min_length):
        self.min_length = min_length

    def detect(self, doc):
        if len(doc['title']) < self.min_length:
            return {'title_length': 'Title is shorter than expected'}
        return {}
