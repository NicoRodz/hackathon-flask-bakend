import firebase_admin
from firebase_admin import credentials, firestore

class FirebaseHelperSingleton:

    db = None

    def __new__(cls):
        if cls.db is None:
            cls.db = super(FirebaseHelperSingleton, cls).__new__(cls)
        return cls.db

    def __init__(self):
        print("__init__")
        cred = credentials.Certificate('./helpers/firebase_key_hackaton.json')
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()

    def create_data(self, collection, document, data):
        doc_ref = self.db.collection(collection).document(document)
        doc_ref.set(data)

    def read_data(self, document_id):
        doc_ref = self.db.collection('collection_name').document(document_id)
        doc = doc_ref.get()
        if doc.exists:
            print(doc.to_dict())
        else:
            print("No such document!")

    def update_data(self, document_id):
        doc_ref = self.db.collection('collection_name').document(document_id)
        doc_ref.update({
            'field_name': 'new_value',
            # ... update more fields ...
        })

    def delete_data(self, document_id):
        self.db.collection('collection_name').document(document_id).delete()
