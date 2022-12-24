import csv

from src.Constants.constants import Constants


class CSVHelper:
    @staticmethod
    def read_csv_email_number():
        with open(f'{Constants.root_dir}/user_responses.csv', 'r') as file:
            reader = csv.reader(file)
            emails = []
            numbers = []
            for row in reader:
                emails.append(row[2])
                numbers.append(row[3])
            emails.pop(0)
            numbers.pop(0)
            return emails, numbers

# print(Constants.root_dir)
# print(CSVHelper.read_csv_email_number())

