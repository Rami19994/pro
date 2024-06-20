import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("the-legend-e6853-firebase-adminsdk-arn02-0dc20fc57a.json")
firebase_admin.initialize_app(cred)
