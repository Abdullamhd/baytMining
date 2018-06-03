import requests
import requests.exceptions
import sys

"""end poing to reloading the core"""
reload_url = "http://localhost:8983/solr/admin/collections?action=RELOAD&name=job"

"""end point to posting the document and indexing the data """
index_url = "http://localhost:8983/solr/job/update/json/docs"

"""delete the all index end point """
delete_index_url = "http://localhost:8983/solr/job/update"

"""Headers"""
headers = {'content-type': 'application/json'}




# DONE
def delete_Index():
    headers = {'Content-type': 'application/json'}

    body = {
        "delete": {
            "query": "*:*"
        },
        "commit": {}
    }

    res = requests.post(headers=headers, url=delete_index_url, json=body)
    if res.status_code == 200 :
        print("Index deleted successfully ..")
        return True
    else:
        print("index not deleted , Response Code :", res.status_code)
        return False



# TODO
def index_document(document):
    print('indexing..')
    try:
        response = requests.post(url=index_url, json=document, headers=headers)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException as e:
        print(e)
        sys.exit(1)


# TODO
def reload_core():
    print('reloading core..')

    try:
        res = requests.get(reload_url)
        if res.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException as e:
        print(e)
        sys.exit(1)


