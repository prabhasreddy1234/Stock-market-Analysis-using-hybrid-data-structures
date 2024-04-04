import random
from datetime import datetime, timezone

import networkx as nx
from matplotlib import pyplot as plt

import avl
import portfolio
import indexing
import graph
import bst

print("========Stock Market Analysis=======")
print("1. Extracting Data and Time Series")
print("2. Portfolio")
print("3. Indexing")
print("4. Graph")
print("5. AVL_Tree_implementation")
print("6. Quit")

while True:

    choice = input("\nEnter your choice: ")
    if choice == "1":
        time_series = avl.TimeSeriesData()
        time_series.read_csv('AAPL_data.csv')

        start_date = datetime(2014, 1, 1, tzinfo=timezone.utc)
        end_date = datetime(2015, 1, 1, tzinfo=timezone.utc)

        data_range = time_series.get_data_range(start_date, end_date)
        for data_point in data_range:
            print(data_point)

    elif choice == "2":
        portfolio = portfolio.Portfolio()

        # Interactive menu for portfolio management
        print("==== Portfolio Management ====")
        print("1. Add Position")
        print("2. Remove Position")
        print("3. Update Position")
        print("4. Get Position")
        print("5. Get Securities")
        print("6. Get Portfolio Value")
        print("7. Quit")
        while True:

            choice = input("\nEnter your choice(portfolio managment): ")

            if choice == "1":
                security = input("Enter the security symbol: ")
                quantity = int(input("Enter the quantity: "))
                cost_basis = float(input("Enter the cost basis: "))
                portfolio.add_position(security, quantity, cost_basis)
            elif choice == "2":
                security = input("Enter the security symbol: ")
                portfolio.remove_position(security)
            elif choice == "3":
                action = input("Enter the action (buy/sell): ")
                security = input("Enter the security symbol: ")
                quantity = int(input("Enter the new quantity (leave blank to skip): "))
                cost_basis = float(input("Enter the new cost basis (leave blank to skip): "))
                portfolio.update_position(security, action, quantity, cost_basis)
            elif choice == "4":
                security = input("Enter the security symbol: ")
                position = portfolio.get_position(security)
                if position:
                    print(f"Position of {security}: {position}")
                else:
                    print(f"No position found for {security} in the portfolio.")
            elif choice == "5":
                securities = portfolio.get_securities()
                for security, quantity in securities:
                    print(f"Security: {security}, Quantity: {quantity}")
            elif choice == "6":
                portfolio_value = portfolio.get_portfolio_value()
                print("Portfolio Value:", portfolio_value)
            elif choice == "7":
                print("Exiting Portfolio Management.")
                break
            else:
                print("Invalid choice. Please try again.")
    elif choice == "3":
        keywords = ["new", "product", "Apple"]
        matching_docs = indexing.index.search_documents(keywords)

        # Output the search results
        print(f"\nDocuments containing the keywords '{', '.join(keywords)}': {matching_docs}")

        # Remove a document from the index
        indexing.index.remove_document(4)

        # Search for documents again after removal
        matching_docs = indexing.index.search_documents(keywords)
        print(f"Documents containing the keywords '{', '.join(keywords)}' (after removal): {matching_docs}\n")

        # Print metadata for the matching documents
        for doc_id in matching_docs:
            if doc_id in indexing.index.document_metadata:
                print(f"Metadata for document {doc_id}: {indexing.index.document_metadata[doc_id]}")
    elif choice == "4":
        stock_graph = graph.StockMarketGraph()
        # Adding nodes
        stocks = ["AAPL", "GOOGL", "MSFT", "AMZN", "NVDA", "FB", "TSLA", "NFLX", "V", "JPM", "WMT", "DIS"]
        for stock in stocks:
            stock_graph.add_node(stock)

        # Adding edges
        stock_graph.add_edge("AAPL", "GOOGL")
        stock_graph.add_edge("AAPL", "MSFT")
        stock_graph.add_edge("GOOGL", "AMZN")
        stock_graph.add_edge("GOOGL", "FB")
        stock_graph.add_edge("AMZN", "FB")
        stock_graph.add_edge("AMZN", "NFLX")
        stock_graph.add_edge("NFLX", "FB")
        stock_graph.add_edge("NFLX", "TSLA")
        stock_graph.add_edge("TSLA", "NVDA")
        stock_graph.add_edge("NVDA", "MSFT")
        stock_graph.add_edge("V", "JPM")
        stock_graph.add_edge("JPM", "WMT")
        stock_graph.add_edge("WMT", "DIS")
        stock_graph.add_edge("DIS", "AAPL")

        neighbors = stock_graph.get_neighbors("AAPL")
        print("Neighbors of AAPL:", [neighbor.data for neighbor in neighbors])

        start_stock = input("Enter the Start Node")
        traversal_order = stock_graph.bfs_traversal(start_stock)
        print(f"BFS traversal starting from {start_stock}: {traversal_order}")

        common_neighbors = stock_graph.get_common_neighbors("AAPL", "AMZN")
        print("Common Neighbors of AAPL and AMZN:", [neighbor.data for neighbor in common_neighbors])

        graph = nx.Graph()
        for stock, node in stock_graph.nodes.items():
            graph.add_node(stock)
        for stock, node in stock_graph.nodes.items():
            for neighbor in node.neighbors:
                graph.add_edge(stock, neighbor.data)

        # Set the layout seed for reproducibility
        layout_seed = random.randint(0, 100)
        pos = nx.spring_layout(graph, seed=layout_seed)

        pos = nx.spring_layout(graph)
        nx.draw_networkx_nodes(graph, pos, node_color='lightblue', node_size=500)
        nx.draw_networkx_edges(graph, pos, edge_color='gray')
        nx.draw_networkx_labels(graph, pos, font_color='black', font_size=8)
        plt.axis('off')
        plt.title("Stock Market Graph")
        plt.show()


    elif choice == "5":
        time_series1 = bst.AVLTree()

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
        print("AVL Tree of Time Series Printed")

    elif choice == "6":
        print("Exiting the program. Thank You😊👍!")
        break
    else:
        print("Invalid choice. Please try again.\n")


