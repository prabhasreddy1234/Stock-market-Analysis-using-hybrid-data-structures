import csv
from datetime import datetime, timezone

# AVL Tree Node
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


# AVL Tree
class AVLTree:
    def __init__(self):
        self.root = None

    # Insert a new data point into the tree
    def insert(self, key, value):
        self.root = self._insert(self.root, key, value)

    def _insert(self, node, key, value):
        if node is None:
            return Node(key, value)
        elif key < node.key:
            node.left = self._insert(node.left, key, value)
        else:
            node.right = self._insert(node.right, key, value)

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        return self._balance(node)

    def _balance(self, node):
        balance = self._get_balance(node)
        if balance > 1:
            if self._get_balance(node.left) < 0:
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        elif balance < -1:
            if self._get_balance(node.right) > 0:
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        return node

    def _rotate_right(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _rotate_left(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _get_height(self, node):
        if node is None:
            return 0
        return node.height

    def _get_balance(self, node):
        if node is None:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    # Retrieve data points within a specified range of dates
    def get_data_range(self, start_date, end_date, results):
        self._get_data_range(self.root, start_date, end_date, results)

    def _get_data_range(self, node, start_date, end_date, results):
        if node is None:
            return
        if start_date <= node.key <= end_date:
            results.append(node.value)
        if start_date <= node.key:
            self._get_data_range(node.left, start_date, end_date, results)
        if node.key <= end_date:
            self._get_data_range(node.right, start_date, end_date, results)


# Time Series Data
class TimeSeriesData:
    def __init__(self):
        self.data_by_date = AVLTree()

    # Insert a new data point into the time series
    def insert_data_point(self, date, value):
        self.data_by_date.insert(date, value)

    # Read data from CSV file and populate the time series
    def read_csv(self, filename):
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                date_str = row['date']
                open_price = row['open']
                low_price = row['low']
                high_price = row['high']
                close_price = row['close']
                volume = row['volume']
                name = row['Name']

                date = datetime.strptime(date_str, '%Y-%m-%d').replace(tzinfo=timezone.utc)
                data_point = {
                    'Date': date_str,
                    'open': open_price,
                    'low': low_price,
                    'high': high_price,
                    'close': close_price,
                    'volume': volume,
                    'name': name
                }
                self.insert_data_point(date, data_point)

    # Retrieve data points within a specified range of dates
    def get_data_range(self, start_date, end_date):
        results = []
        self.data_by_date.get_data_range(start_date, end_date, results)
        return results

