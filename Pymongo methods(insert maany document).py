#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pymongo

def insert_documents(database_name, collection_name, documents):
    # Connect to the MongoDB server
    client = pymongo.MongoClient()
    
    # Get the database and collection
    db = client[database_name]
    collection = db[collection_name]
    
    # Insert the documents into the collection
    result = collection.insert_many(documents)
    
    # Print the IDs of the inserted documents
    print("Inserted", len(result.inserted_ids), "documents:")
    for inserted_id in result.inserted_ids:
        print(inserted_id)
    
    # Close the MongoDB connection
    client.close()


# In[7]:


documents = [
    {
        "name": "John Smith",
        "age": 35,
        "email": "john.smith@example.com"
    },
    {
        "name": "Jane Doe",
        "age": 30,
        "email": "jane.doe@example.com"
    }
]

insert_documents("mydatabase", "mycollection", documents)

