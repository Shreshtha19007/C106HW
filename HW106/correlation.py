import plotly.express as px
import csv
import numpy as np
 
def get_data_source(data_path):
    sleep_in_hours=[]
    coffee_in_ml=[]
    with open(data_path) as csv_file :
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader :
            coffee_in_ml.append(float(row["week"]))
            sleep_in_hours.append(float(row["sleep in hours"]))
    return {"x":coffee_in_ml,"y":sleep_in_hours}

def find_corelation(data_source):
    corelation=np.corrcoef(data_source["x"],data_source["y"])
    print("Coorelation is ",corelation[0,1])
