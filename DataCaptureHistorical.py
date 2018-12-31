import requests
import json
import csv

#####################################################
# Historical market data collection
#####################################################

# Params
output_file_name = 'market_data_hist_2y.csv'
years_of_data = 2
days_per_year = 250
days_to_include = years_of_data * days_per_year

resp = requests.get('https://api.iextrading.com/1.0/stock/market/batch?symbols=nflx&types=chart&range=2y&last=1&filter=date,open,high,low,close,changePercent,change')

print('Response: ' + str(resp.status_code))
if resp.status_code != 200:
    # This means something went wrong.
    raise ApiError('GET /chart/ {}'.format(resp.status_code))

print('Starting process...')
data = resp.json()

dataSet = data['NFLX']['chart']
numDays = len(dataSet)  # Current day point of view

# Write header record to CSV file
with open(output_file_name, 'w', newline='') as csvfile:  # a = append, w = overwrite
    fieldnames = ['pctChg1', 'pctChg2', 'pctChg3', 'pctChg4', 'pctChg5', 'pctChg6', 'pctChg7',
                  'pctChg8', 'pctChg9', 'pctChg10', 'pctChg11', 'pctChg12', 'pctChg13', 'pctChg14', 'y']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

for idx in range(days_to_include):
    # Set fields for export
    pctChg = data['NFLX']['chart'][numDays-1]['changePercent']  # TODO: Don't include this in the data only to label y
    pctChg1 = data['NFLX']['chart'][numDays-2]['changePercent']
    pctChg2 = data['NFLX']['chart'][numDays-3]['changePercent']
    pctChg3 = data['NFLX']['chart'][numDays-4]['changePercent']
    pctChg4 = data['NFLX']['chart'][numDays-5]['changePercent']
    pctChg5 = data['NFLX']['chart'][numDays-6]['changePercent']
    pctChg6 = data['NFLX']['chart'][numDays-7]['changePercent']
    pctChg7 = data['NFLX']['chart'][numDays-8]['changePercent']
    pctChg8 = data['NFLX']['chart'][numDays-9]['changePercent']
    pctChg9 = data['NFLX']['chart'][numDays-10]['changePercent']
    pctChg10 = data['NFLX']['chart'][numDays-11]['changePercent']
    pctChg11 = data['NFLX']['chart'][numDays-12]['changePercent']
    pctChg12 = data['NFLX']['chart'][numDays-13]['changePercent']
    pctChg13 = data['NFLX']['chart'][numDays-14]['changePercent']
    pctChg14 = data['NFLX']['chart'][numDays-15]['changePercent']

    y = 0
    if(pctChg >= 1):
        y = 1
    else:
        y = 0

    with open(output_file_name, 'a', newline='') as csvfile:  # a = append, w = overwrite
        fieldnames = ['pctChg1', 'pctChg2', 'pctChg3', 'pctChg4', 'pctChg5', 'pctChg6', 'pctChg7', 'pctChg8', 'pctChg9', 'pctChg10', 'pctChg11', 'pctChg12', 'pctChg13', 'pctChg14', 'y']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'pctChg1': pctChg1, 'pctChg2': pctChg2, 'pctChg3': pctChg3, 'pctChg4': pctChg4, 'pctChg5': pctChg5, 'pctChg6': pctChg6, 'pctChg7': pctChg7, 'pctChg8': pctChg8, 'pctChg9': pctChg9, 'pctChg10': pctChg10, 'pctChg11': pctChg11, 'pctChg12': pctChg12, 'pctChg13': pctChg13, 'pctChg14': pctChg14, 'y': y})

    numDays -= 1

print('Done.')

