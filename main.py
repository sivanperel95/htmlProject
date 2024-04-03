from datetime import datetime

from db.mongo_db_layer import MongoDBDataLayer
from parser.html_parser import Parser
from strategies.date_discrepancy_strategy import DateDiscrepancyStrategy
from strategies.sum_discrepancy_strategy import SumDiscrepancyStrategy
from strategies.title_length_strategy import TitleLengthStrategy
from validators.document_validator import DocumentValidator

if __name__ == "__main__":
    db_layer = MongoDBDataLayer()
    db_layer.clear_collections()  # Clear collections before starting

    parser = Parser(db_layer)
    folder_path = 'documents'
    parser.parse(folder_path)

    # Setting up the maximum date for date discrepancy strategy
    max_date_str = '30Jan2023'
    max_date = datetime.strptime(max_date_str, '%d%b%Y')

    # Instantiate strategies with desired criteria
    strategies = [
        TitleLengthStrategy(min_length=5),
        DateDiscrepancyStrategy(max_date=max_date),
        SumDiscrepancyStrategy(max_sum=10000)
    ]

    validator = DocumentValidator(db_layer, strategies)

    # Retrieve and sort the document IDs in numerical order before validation
    document_ids = [doc['document_id'] for doc in db_layer.documents.find({}, {'document_id': 1})]
    sorted_doc_ids = sorted(document_ids, key=lambda x: int(x.split('_')[0]))

    # Validator usage with sorted documents
    for doc_id in sorted_doc_ids:
        validation_result = validator.validate(doc_id)  # Adjusted to match the new signature
        print(f'Validation for {doc_id}:', validation_result)

