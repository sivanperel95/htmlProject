from models.validation_status import ValidationStatus


# DocumentValidator using Strategy Pattern
class DocumentValidator:
    def __init__(self, db_layer, strategies):
        self.db_layer = db_layer
        self.strategies = strategies

    def validate(self, doc_id):
        doc = self.db_layer.get_document(doc_id)
        if not doc:
            return ValidationStatus.NOT_FOUND, {}

        discrepancies_info = {}
        for strategy in self.strategies:
            discrepancies_info.update(strategy.detect(doc))

        validation_status = ValidationStatus.VALID if not discrepancies_info else ValidationStatus.INVALID
        return validation_status, discrepancies_info
