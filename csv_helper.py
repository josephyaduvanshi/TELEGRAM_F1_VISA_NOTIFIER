import csv


class CSVHelper:
    @staticmethod
    def read_csv_email_number():
        """
        It opens the csv file, reads the emails and numbers, and returns them as lists
        return: A list of emails and a list of numbers
        """
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
