import requests
import json
import csv

# TODO: Update this script to capture live market data in order to truly predict

# Params
output_file_name = 'market_data_daily.csv'

days_to_include = 1

resp = requests.get('https://api.iextrading.com/1.0/stock/market/batch?symbols=nflx&types=chart&range=1m&last=1&filter=date,open,high,low,close,changePercent,change')
print(resp)
print('Response: ' + str(resp.status_code))
if resp.status_code != 200:
    # This means something went wrong.
    raise ApiError('GET /chart/ {}'.format(resp.status_code))

print('Starting process...')
data = resp.json()
print(data)

dataSet = data['NFLX']['chart']
numDays = len(dataSet)  # Current day point of view
loopDays = numDays-1    # Previous day point of view for 14 day averages

# Write header record to CSV file
with open(output_file_name, 'w', newline='') as csvfile:  # a = append, w = overwrite
    fieldnames = ['pctChg1', 'pctChg2', 'pctChg3', 'pctChg4', 'pctChg5', 'pctChg6', 'pctChg7',
                  'pctChg8', 'pctChg9', 'pctChg10', 'pctChg11', 'pctChg12', 'pctChg13', 'pctChg14']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()


for idx in range(days_to_include):
    # Set fields for export
    pctChg = data['NFLX']['chart'][numDays-1]['changePercent']
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

    # NOTE: Below we are shifting the data for prediction purposes so pctChg1 = pctChg, pctChg2 = pctChg1...
    # This will provide the algorithm with current data to be used for predictions where as training can use historical
    with open(output_file_name, 'a', newline='') as csvfile:  # a = append, w = overwrite
        fieldnames = ['pctChg1', 'pctChg2', 'pctChg3', 'pctChg4', 'pctChg5', 'pctChg6', 'pctChg7', 'pctChg8', 'pctChg9', 'pctChg10', 'pctChg11', 'pctChg12', 'pctChg13', 'pctChg14']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'pctChg1': pctChg, 'pctChg2': pctChg1, 'pctChg3': pctChg2, 'pctChg4': pctChg3, 'pctChg5': pctChg4, 'pctChg6': pctChg5, 'pctChg7': pctChg6, 'pctChg8': pctChg7, 'pctChg9': pctChg8, 'pctChg10': pctChg9, 'pctChg11': pctChg10, 'pctChg12': pctChg11, 'pctChg13': pctChg12, 'pctChg14': pctChg13})

    numDays -= 1

print('Done.')

