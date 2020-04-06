'''
when you are going to call the methods: readDB, readDoc, createDoc, createEmptyDoc, setDocVals, or deleteDoc. The arguments for collec
and docName should be in the form of   u'collection/document name'  and any method that has the argument attrList should
contain the attrList list from preprocessing.py

the hierarchy exists as such collection->documents, in documents, data is held

Keep in mind that, as far as I know, you cannot create a collection in python. if you'd like a new collection tell me and i'll add one
for now though, there is one collection at the moment titled, family. To reference, see above, or here   u'family'
'''

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import pandas as pd
import csv

cred = credentials.Certificate('./ecosight01-firebase-adminsdk-122wv-3582c284d9.json')
default_app = firebase_admin.initialize_app(cred)
db = firestore.client()



def readDB(collec):
    Test = db.collection(collec).stream()

    # Opening a CSV file for users data
    with open('./firebase.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        # Writing header row of CSV file. Change it according to your needs ;)
        writer.writerow(["area", "perimeter", "thresholImg", "aspectRatio", "rectangularity", "circularity", "equiDiameter", "angle", "classification"])

        # Writing all the users data
        for i in Test:
            writer.writerow([i.get("area"), i.get("perimeter"), i.get("thresholdImg"), i.get("aspectRatio"), i.get("rectangularity"), i.get("circularity"), i.get("equiDiameter"), i.get("angle"),i.get("classification")])

def readDoc(collec, docName):
    Test = db.collection(collec).document(docName).get()

    # Opening a CSV file for users data
    with open('./firebase.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        # Writing header row of CSV file. Change it according to your needs ;)
        writer.writerow(["area", "perimeter", "thresholImg", "aspectRatio", "rectangularity", "circularity", "equiDiameter", "angle", "classification"])
        writer.writerow([Test.get("area"), Test.get("perimeter"), Test.get("thresholdImg"), Test.get("aspectRatio"), Test.get("rectangularity"), Test.get("circularity"), Test.get("equiDiameter"), Test.get("angle"),Test.get("classification")])

def createDoc(collec, docName, attrList):
    col_ref = db.collection(collec)
    new_val = {
        u'aspectRatio': attrList[aspectRatio],
        u'area': attrList[area],
        u'perimeter': attrList[perimeter],
        u'thresholdImg': attrList[thresholdImg],
        u'rectangularity': attrList[rectangularity],
        u'circularity': attrList[circularity],
        u'equiDiameter': attrList[equiDiameter],
        u'angle': attrList[angle],
        u'classification': attrList[classification],
    }
    col_ref.document(docName).create(new_val)

def createEmptyDoc(collec, docName):
    col_ref = db.collection(collec)
    new_val = {
        u'aspectRatio': 0,
        u'area': 0,
        u'perimeter': 0,
        u'thresholdImg': 0,
        u'rectangularity': 0,
        u'circularity': 0,
        u'equiDiameter': 0,
        u'angle': 0,
        u'classification': 'empty',
    }
    col_ref.document(docName).create(new_val)

def setDocVals(collec, docName,attrList):
    doc_ref = db.collection(collec).document(docName)
    doc_ref.set({
        u'aspectRatio': attrList[0],
        u'area': attrList[1],
        u'perimeter': attrList[2],
        u'thresholdImg': attrList[thresholdImg],
        u'rectangularity': attrList[rectangularity],
        u'circularity': attrList[circularity],
        u'equiDiameter': attrList[equiDiameter],
        u'angle': attrList[angle],
        u'classification': attrList[classification],
    })

def deleteDoc(collec, docName):
    db.collection(collec).document(docName).delete()

createCollec(u'family')
deleteDoc(u'family',u'Test')