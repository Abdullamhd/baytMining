import pandas as pd


#TODO
def save_to_sql(document):
    print('saving to SQL')
    return False

#TODO
def save_to_csv(document):
    try:
        df = pd.DataFrame(document)
        df.to_csv()
        return True
    except ValueError:
        print("the data is not valid")
        return False




#TODO
def save_as_json(document):
    print("saving as JSON")
    return False


