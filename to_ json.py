import json
from data import nounlist 
from data import nounlist2 


def convertToJSON():
    with open("table1.json", "w") as write_file:
        json.dump(nounlist, write_file)


def convertInJSON():
    with open("table2.json", "w") as write_file:
        json.dump(nounlist2, write_file)