from pymongo import MongoClient
import os

client = MongoClient("mongodb://cds-mongodb-1:27017")
db = client.credit_underwriting

def save_underwriting(applicant_id, decision):
    print(f"Saving underwriting decision for applicant ID: {applicant_id}")
    db.underwriting.insert_one({
        'applicant_id': applicant_id,
        'decision': decision
    })
    print(f"Underwriting decision saved for applicant ID: {applicant_id}")