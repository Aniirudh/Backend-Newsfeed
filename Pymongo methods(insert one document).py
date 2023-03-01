#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pymongo

def insert_document(database_name, collection_name, document):
    # Connect to the MongoDB server
    client = pymongo.MongoClient("mongodb://localhost:27017")
    
    # Get the database and collection
    db = client[database_name]
    collection = db[collection_name]
    
    # Insert the document into the collection
    result = collection.insert_one(document)
    
    # Print the ID of the inserted document
    #print("Inserted document with ID:", result.inserted_id)
    
    # Close the MongoDB connection
    client.close()


# In[3]:


document = {
    "name": "Jane Doe",
    "age": 30,
    "email": "jane.doe@example.com"
}

insert_document("mydatabase", "mycollection", document)

