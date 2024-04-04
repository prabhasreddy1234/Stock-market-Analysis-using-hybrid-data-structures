import random
import networkx as nx
import matplotlib.pyplot as plt
random.seed(42)

class Node:
    def __init__(self, data):
        self.data = data
        self.neighbors = []

    def __repr__(self):
        return self.data


class StockMarketGraph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, stock):
        if stock not in self.nodes:
            new_node = Node(stock)
            self.nodes[stock] = new_node

    def add_edge(self, stock1, stock2):
        if stock1 not in self.nodes:
            self.add_node(stock1)
        if stock2 not in self.nodes:
            self.add_node(stock2)

        node1 = self.nodes[stock1]
        node2 = self.nodes[stock2]
        node1.neighbors.append(node2)
        node2.neighbors.append(node1)

    def get_neighbors(self, stock):
        if stock in self.nodes:
            node = self.nodes[stock]
            return node.neighbors
        return []

    def bfs_traversal(self, start_stock):
        visited = set()
        queue = []
        traversal_order = []

        if start_stock in self.nodes:
            start_node = self.nodes[start_stock]
            queue.append(start_node)
            visited.add(start_node)

            while queue:
                node = queue.pop(0)
                traversal_order.append(node.data)

                for neighbor in node.neighbors:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)
            return traversal_order

    def get_common_neighbors(self, stock1, stock2):
        neighbors1 = self.get_neighbors(stock1)
        neighbors2 = self.get_neighbors(stock2)
        common_neighbors = [neighbor for neighbor in neighbors1 if neighbor in neighbors2]
        return common_neighbors

# # Adding nodes
# stock_graph.add_node("AAPL")
# stock_graph.add_node("GOOGL")
# stock_graph.add_node("MSFT")
# stock_graph.add_node("AMZN")
# stock_graph.add_node("NVDA")
#
# # Adding edges
# stock_graph.add_edge("AAPL", "GOOGL")
# stock_graph.add_edge("AAPL", "MSFT")
# stock_graph.add_edge("GOOGL", "AMZN")
# stock_graph.add_edge("MSFT", "AMZN")
# stock_graph.add_edge("MSFT", "NVDA")

