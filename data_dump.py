import pymongo
import pandas as pd
import json

client = pymongo.MongoClient('mongodb+srv://imshrey26:Spencer123@cluster0.agcbkqv.mongodb.net/?retryWrites=true&w=majority')

DATA_FILE_PATH = (r"C:\Users\Shrey Singh\Documents\ML projects\Insurance\Insurance Project\Insurance-Project\insurance.csv")
DATABASE_NAME = 'INSURANCE'
COLLECTION_NAME = 'INSURANCE_PROJECT'

if __name__ == '__main__':
    df = pd.read_csv(DATA_FILE_PATH)
    print(f'Rows and Columns:{df.shape}')

    df.reset_index(drop=True,inplace=True)

    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])

    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)