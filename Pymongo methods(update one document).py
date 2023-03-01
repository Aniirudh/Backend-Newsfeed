#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pymongo

def update_document(database_name, collection_name, query, update):
    # Connect to the MongoDB server
    client = pymongo.MongoClient()
    
    # Get the database and collection
    db = client[database_name]
    collection = db[collection_name]
    
    # Update the document in the collection
    result = collection.update_one(query, update)
    
    # Print the result of the update
    print(result.modified_count, "document(s) updated.")
    
    # Close the MongoDB connection
    client.close()


# In[4]:


query = {"name": "Jane Doe"}
update = {"$set": {"age": 36}}

update_document("mydatabase", "mycollection", query, update)

