#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pymongo

def delete_document(database_name, collection_name, query):
    # Connect to the MongoDB server
    client = pymongo.MongoClient()
    
    # Get the database and collection
    db = client[database_name]
    collection = db[collection_name]
    
    # Delete the matching document from the collection
    result = collection.delete_one(query)
    
    # Print the number of documents deleted
    print(result.deleted_count, "document deleted.")
    
    # Close the MongoDB connection
    client.close()


# In[5]:


query = {"name": "Jane Doe"}

delete_document("mydatabase", "mycollection", query)

