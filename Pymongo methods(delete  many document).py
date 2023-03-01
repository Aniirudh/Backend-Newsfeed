#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pymongo

def delete_documents(database_name, collection_name, query):
    # Connect to the MongoDB server
    client = pymongo.MongoClient()
    
    # Get the database and collection
    db = client[database_name]
    collection = db[collection_name]
    
    # Delete the matching documents from the collection
    result = collection.delete_many(query)
    
    # Print the number of documents deleted
    print(result.deleted_count, "documents deleted.")
    
    # Close the MongoDB connection
    client.close()


# In[4]:


query = {"age": {"$gt": 25}}

delete_documents("mydatabase", "mycollection", query)

