from _datetime import datetime

from strategies.discrepancy_strategy import DiscrepancyStrategy


class DateDiscrepancyStrategy(DiscrepancyStrategy):
    def __init__(self, max_date):
        self.max_date = max_date

    def detect(self, doc):
        doc_date = self.convert_date(doc.get('date_of_creation', ''))
        if doc_date and doc_date > self.max_date:
            return {'date': 'Date in footer is beyond the given date'}
        return {}

    def convert_date(self, date_str):
        try:
            return datetime.strptime(date_str, '%d%b%Y')
        except ValueError:
            return None