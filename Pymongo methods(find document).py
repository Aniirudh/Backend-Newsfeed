#!/usr/bin/env python
# coding: utf-8

# In[42]:


import pymongo

def find_documents(database_name, collection_name, query={}, projection=None):
    # Connect to the MongoDB server
    client = pymongo.MongoClient()
    
    # Get the database and collection
    db = client[database_name]
    collection = db[collection_name]
    
    # Find the documents in the collection
    result = collection.find(query, projection)
   
    # Print the documents
    #print("Found", result.count(), "documents:")
    for document in result:
        print(document)
    
    # Close the MongoDB connection
    client.close()


# In[43]:


query = {"name": "Jane Doe"}
projection = {"_id": 0, "name": 1, "age": 1}

#query (optional): A dictionary specifying the query parameters. The default value is an empty dictionary,
#which means all documents in the collection will be returned.
#projection (optional): A dictionary specifying which fields to include or exclude in the returned documents.
#The default value is None, which means all fields will be returned.


find_documents("mydatabase", "mycollection", query, projection)

