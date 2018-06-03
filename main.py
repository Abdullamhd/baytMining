import extractor
from time import sleep
from random import randint
import solr
import  pandas as pd

total_docs = list()
for numbers in range(200):
    documents = extractor.extract(numbers)
    total_docs.append(documents)
    print(documents)
    sleep(randint(3, 8))


    # if solr.index_document(documents):
    #     print('document indexed ')
    #     if solr.reload_core():
    #         print('core reloaded ')
    # for doc in documents:
    #     total_docs.append(doc)
    #     print(doc)
    # sleep(randint(3,8))


