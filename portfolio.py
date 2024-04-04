# Node class for the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked list for storing securities in the portfolio
class SecuritiesList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node

# Portfolio Management
class Portfolio:
    def __init__(self):
        self.positions = {}
        self.securities_list = SecuritiesList()

    def add_position(self, security, quantity, cost_basis):
        if security not in self.positions:
            self.positions[security] = {'quantity': quantity, 'cost_basis': cost_basis}
            self.securities_list.append(security)
            print(f"Position for {security} has been added to the portfolio.")
        else:
            print(f"Position for {security} already exists in the portfolio.")

    def remove_position(self, security):
        if security in self.positions:
            del self.positions[security]
            self._remove_security_from_list(security)
            print(f"Position for {security} has been removed from the portfolio.")
        else:
            print(f"No position found for {security} in the portfolio.")

    def update_position(self, security, action, quantity=None, cost_basis=None):
        if security in self.positions:
            if action == "buy":
                if quantity is not None:
                    existing_quantity = self.positions[security]['quantity']
                    new_quantity = existing_quantity + quantity
                    self.positions[security]['quantity'] = new_quantity
                if cost_basis is not None:
                    self.positions[security]['cost_basis'] = cost_basis
                print(f"Position for {security} has been updated in the portfolio.")
            elif action == "sell":
                del self.positions[security]
                self._remove_security_from_list(security)
                print(f"Position for {security} has been sold and removed from the portfolio.")
            else:
                print("Invalid action. Please specify 'buy' or 'sell'.")
        else:
            print(f"No position found for {security} in the portfolio.")

    def get_position(self, security):
        if security in self.positions:
            return self.positions[security]
        return None

    def get_securities(self):
        securities = []
        current_node = self.securities_list.head
        while current_node:
            security = current_node.data
            quantity = self.positions[security]['quantity']
            securities.append((security, quantity))
            current_node = current_node.next
        return securities

    def _remove_security_from_list(self, security):
        current_node = self.securities_list.head
        previous_node = None
        while current_node:
            if current_node.data == security:
                if previous_node:
                    previous_node.next = current_node.next
                else:
                    self.securities_list.head = current_node.next
                break
            previous_node = current_node
            current_node = current_node.next

    def get_portfolio_value(self):
        total_value = 0
        for security, position in self.positions.items():
            quantity = position['quantity']
            cost_basis = position['cost_basis']
            total_value += quantity * cost_basis
        return total_value


