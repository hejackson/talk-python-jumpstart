#!/usr/local/bin/python3

import os
import csv
import datatypes
import statistics


def main():
    print_header()
    filename = get_data_file()
    data = load_file(filename)
    query_data(data)


def print_header():
    print('------------------------------')
    print('      REAL ESTATE APP')
    print('------------------------------')


def get_data_file():
    base_folder = os.path.dirname(__file__)
    return os.path.abspath(os.path.join(base_folder, 'data',
                           'SacramentoRealEstateTransactions2008.csv'))


def load_file(filename):
    with open(filename, 'r', encoding='utf-8') as fin:
        # header = fin.readline().strip()
        # reader = csv.reader(fin)
        reader = csv.DictReader(fin)
        purchases = []

        for row in reader:
            # print(row)
            # print(type(row), row)
            # print('Bed count: {}'.format(row['beds']))
            p = datatypes.Purchase.create_from_dict(row)
            purchases.append(p)

        return purchases


def load_file_basic(filename):
    with open(filename, 'r', encoding='utf-8') as fin:
        header = fin.readline().strip()
        print('found header: ' + header)

        lines = []
        for line in fin:
            line_data = line.strip().split(',')
            bed_count = line_data[4]
            lines.append(line_data)

        print(lines[:5])


def query_data(data):
    # most expensive
    # least expensive
    # average price
    # average price of 2 bedroom house

    # data.sort(key=get_price)
    data.sort(key = lambda p: p.price)

    high_purchase = data[-1]
    print('The most expensive house is ${:,} with {} beds and {} baths.'.format(high_purchase.price,high_purchase.beds, high_purchase.baths))

    low_purchase = data[0]
    print('The least expensive house is ${:,} with {} beds and {} baths.'.format(low_purchase.price,low_purchase.beds, low_purchase.baths))

    # average price
    prices = []
    for pur in data:
        prices.append(pur.price)

    ave_price = statistics.mean(prices)
    print('The average home price is ${:,}'.format(int(ave_price)))

    prices = []
    for pur in data:
        if pur.beds == 2:
            prices.append(pur.price)

    ave_price = statistics.mean(prices)
    print('The average home price of a 2-bedroom home is ${:,}'.format(int(ave_price)))


if __name__ == '__main__':
    main()
