import matplotlib.pyplot as plt

# AVL Tree Node
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.height = 1
        self.left = None
        self.right = None

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

        balance = self._get_balance(node)

        # Perform rotations if the node is unbalanced
        if balance > 1 and key < node.left.key:
            return self._rotate_right(node)
        if balance < -1 and key > node.right.key:
            return self._rotate_left(node)
        if balance > 1 and key > node.left.key:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        if balance < -1 and key < node.right.key:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def _rotate_left(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _rotate_right(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

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

    # Visualize the AVL tree using matplotlib
    def visualize(self):
        fig, ax = plt.subplots(figsize=(10, 6))
        self._visualize_node(ax, self.root, None, 0, 0)
        ax.axis('off')
        plt.gca().invert_yaxis()
        plt.show()

    def _visualize_node(self, ax, node, parent_node, x, y):
        if node is None:
            return

        # Calculate the coordinates of child nodes
        left_x = x - 1 / (2 ** (y + 1))
        right_x = x + 1 / (2 ** (y + 1))
        next_y = y + 1

        # Recursively draw the left and right child nodes
        self._visualize_node(ax, node.left, (x, y), left_x, next_y)
        self._visualize_node(ax, node.right, (x, y), right_x, next_y)

        # Draw the node
        ax.text(x, y, f"{node.key}", ha='center', va='center',
                bbox=dict(facecolor='lightblue', edgecolor='black', boxstyle='circle'))

        # Draw edge from parent node to current node
        if parent_node:
            ax.plot([parent_node[0], x], [parent_node[1], y], color='black', linewidth=1)


# Create an instance of the AVLTree
time_series1 = AVLTree()

# Add sample stock data points to the AVL tree
time_series1.insert('2023-06-01', 100)
time_series1.insert('2023-06-02', 105)
time_series1.insert('2023-06-03', 98)
time_series1.insert('2023-06-04', 102)
time_series1.insert('2023-06-05', 110)
time_series1.insert('2023-06-06', 95)
time_series1.insert('2023-06-07', 108)
time_series1.insert('2023-06-08', 103)
time_series1.insert('2023-06-09', 112)
time_series1.insert('2023-06-10', 115)
time_series1.insert('2023-06-11', 107)
time_series1.insert('2023-06-12', 109)
time_series1.insert('2023-06-13', 120)
time_series1.insert('2023-06-14', 114)
time_series1.insert('2023-06-15', 117)

# Visualize the AVL tree
time_series1.visualize()