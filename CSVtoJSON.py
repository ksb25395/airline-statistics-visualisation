import json
import csv
from itertools import islice
import collections

with open('/home/bhargav/Downloads/Table_3_Countrywise_DGCA__Q4_OCT-DEC_2017.csv') as csvfile:
    reader = csv.DictReader(islice(csvfile, 0, 59), fieldnames=("id", "name", "passengersToIndia", "passengersFromIndia", "freightToIndia", "freightFromIndia"))
    next(csvfile)
    outDict = collections.OrderedDict()
    outDict.setdefault('nodes', [])
    outDict.setdefault('pLinksTo', [])
    outDict.setdefault('pLinksFrom', [])
    outDict.setdefault('fLinksTo', [])
    outDict.setdefault('fLinksFrom', [])
    listReader = list(reader)
    pToMax = max([float(x['passengersToIndia']) for x in listReader])
    pFromMax = max([float(x['passengersFromIndia']) for x in listReader])
    fToMax = max([float(x['freightToIndia']) for x in listReader])
    fFromMax = max([float(x['freightFromIndia']) for x in listReader])

    for row in listReader:
        nodeval = {'id': int(float(row['id'])), 'name': row['name']}
        outDict['nodes'].append(nodeval)
        link1 = {'source': int(float(row['id'])), 'target': 0, 'value': int(float(row['passengersToIndia'])),
                 'weight': float(row['passengersToIndia'])/pToMax}
        outDict['pLinksTo'].append(link1)
        link2 = {'target': int(float(row['id'])), 'source': 0, 'value': int(float(row['passengersFromIndia'])),
                 'weight': float(row['passengersFromIndia']) / pFromMax}
        outDict['pLinksFrom'].append(link2)
        link3 = {'source': int(float(row['id'])), 'target': 0, 'value': int(float(row['freightToIndia'])),
                 'weight': float(row['freightToIndia']) / fToMax}
        outDict['fLinksTo'].append(link3)
        link4 = {'target': int(float(row['id'])), 'source': 0, 'value': int(float(row['freightFromIndia'])),
                 'weight': float(row['freightToIndia']) / fFromMax}
        outDict['fLinksFrom'].append(link4)
    print(json.dumps(outDict))
