import csv
import json
import urllib.request


def download_file(src_url, output_filename):
    csv_file_path, _ = urllib.request.urlretrieve(src_url)

    with open(csv_file_path, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        with open(output_filename, mode='w') as json_file:
            for csv_row in csv_reader:
                json_row = {k: v for k, v in csv_row.items() if not k.startswith('_')}
                json.dump(json_row, json_file)
                json_file.write('\n')


def parse_json_file(file_name, json_parser):
    for json_data in iterate_file_rows(file_name):
        yield json_parser.parse_json(json_data)


def iterate_file_rows(file_name):
    with open(file_name, 'r') as data_file:
        for row in data_file:
            yield row

