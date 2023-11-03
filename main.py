import csv
import os
import random


class csvProcessor():
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = []
        self.columns = []
        self.load_data()

    def load_data(self):
        with open(self.file_path, 'r') as file:
            reader = csv.reader(file)
            self.columns = next(reader)

            for row in reader:
                self.data.append(row)

    def Show(self, output_type='top', num_rows=5, separator=','):
        if output_type == 'top':
            output_data = self.data[:num_rows]

        elif output_type == 'bottom':
            output_data = self.data[-num_rows]

        elif output_type == 'random':
            output_data = random.sample(self.data, num_rows)

        else:
            print("Выбран неверный тип вывода.\n Варианты типов вывода: 'top', 'bottom', 'random'.")

            return

        for row in output_data:
            print(separator.join(row))

    def Info(self):
        num_rows = len(self.data)
        num_columns = len(self.columns)
        print(f'Размерность файла без учета строки заголовков: {num_rows} x {num_columns}')

        for column in self.columns:
            non_empty_values = sum(1 for row in self.data if row[self.columns.index(column)] != ' ')
            data_type = type(self.data[0][self.columns.index(column)])
            print(f"{column} \t {non_empty_values} \t {data_type}")

    def delNaN(self):
        self.data = [row for row in self.data if all(field != '' for field in row)]

    def makeDS(self):
        learning_dir = os.path.join(os.getcwd(), 'workdata', 'Learning')
        testing_dir = os.path.join(os.getcwd(), 'workdata', 'Testing')

        os.makedirs(learning_dir, exist_ok=True)
        os.makedirs(testing_dir, exist_ok=True)

        learning_data = random.sample(self.data, int(len(self.data) * 0.70))
        testing_data = [row for row in self.data if row not in learning_data]

        learning_file_path = os.path.join(learning_dir, 'train.csv')
        testing_file_path = os.path.join(testing_dir, 'test.csv')

        with open(learning_file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(self.columns)
            writer.writerows(learning_data)

        with open(testing_file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(self.columns)
            writer.writerows(testing_data)


file_path = 'data.csv'
processor = csvProcessor(file_path)
#processor.Info()
#processor.Show()
#processor.delNaN()
#processor.makeDS()
