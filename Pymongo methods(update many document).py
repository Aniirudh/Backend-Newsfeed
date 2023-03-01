#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pymongo

def update_documents(database_name, collection_name, query, update):
    # Connect to the MongoDB server
    client = pymongo.MongoClient()
    
    # Get the database and collection
    db = client[database_name]
    collection = db[collection_name]
    
    # Update the documents in the collection
    result = collection.update_many(query, update)
    
    # Print the result of the update
    print(result.modified_count, "document(s) updated.")
    
    # Close the MongoDB connection
    client.close()


# In[5]:


query = {"name": {"$regex": "^J"}}
update = {"$set": {"age": 36}}

update_documents("mydatabase", "mycollection", query, update)

