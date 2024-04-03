from pymongo import MongoClient

from config import MONGODB_URI, MONGODB_DATASET_NAME


# MongoDB Data Layer
class MongoDBDataLayer:
    """
       Represents a data layer for interacting with MongoDB for CRUD operations.
       Utilizes PyMongo for database interactions.
       """

    def __init__(self):
        """
                Initializes the MongoDBDataLayer with a connection to the MongoDB server.
                """
        self.client = MongoClient(MONGODB_URI, maxPoolSize=50, connectTimeoutMS=30000)
        self.db = self.client[MONGODB_DATASET_NAME]
        self.documents = self.db['documents']
        self.discrepancies = self.db['discrepancies']

    def clear_collections(self):
        self.documents.drop()
        self.discrepancies.drop()

    # Or if you want to drop the entire database
    def drop_database(self):
        self.client.drop_database('document_db')

    # CRUD operations
    def insert_document(self, data):
        return self.documents.insert_one(data).inserted_id

    def get_document(self, document_id):
        return self.documents.find_one({'document_id': document_id})

    def update_document(self, document_id, data):
        return self.documents.update_one({'document_id': document_id}, {'$set': data})

    def delete_document(self, document_id):
        return self.documents.delete_one({'document_id': document_id})

    def insert_discrepancy(self, data):
        return self.discrepancies.insert_one(data).inserted_id
