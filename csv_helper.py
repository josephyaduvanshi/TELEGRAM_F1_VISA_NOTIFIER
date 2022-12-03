import csv


class CSVHelper:
    @staticmethod
    def read_csv_email_number():
        with open('user_responses.csv', 'r') as file:
            reader = csv.reader(file)
            emails = []
            numbers = []
            for row in reader:
                emails.append(row[2])
                numbers.append(row[3])
            emails.pop(0)
            numbers.pop(0)
            return emails, numbers


