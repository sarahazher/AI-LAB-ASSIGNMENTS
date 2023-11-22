class Router:
    def __init__(self, name):
        self.name = name
        self.routing_table = {}  # Routing table: destination -> (next_hop, cost)

    def update_routing_table(self, destination, next_hop, cost):
        self.routing_table[destination] = (next_hop, cost)


def main():
    # Create routers
    router_a = Router('A')
    router_b = Router('B')
    router_c = Router('C')

    # Initialize routing tables
    router_a.update_routing_table('A', None, 0)
    router_a.update_routing_table('B', 'B', 1)
    router_a.update_routing_table('C', 'C', 3)

    router_b.update_routing_table('A', 'A', 1)
    router_b.update_routing_table('B', None, 0)
    router_b.update_routing_table('C', 'C', 2)

    router_c.update_routing_table('A', 'A', 3)
    router_c.update_routing_table('B', 'B', 2)
    router_c.update_routing_table('C', None, 0)

    # Simulate distance-vector routing (Bellman-Ford algorithm)
    routers = [router_a, router_b, router_c]
    num_iterations = 5  # Number of iterations

    for _ in range(num_iterations):
        for router in routers:
            for destination, (next_hop, cost) in router.routing_table.items():
                for neighbor in routers:
                    if neighbor != router:
                        neighbor_cost = neighbor.routing_table[destination][1]
                        total_cost = neighbor_cost + cost
                        if destination not in router.routing_table or total_cost < router.routing_table[destination][1]:
                            router.update_routing_table(destination, neighbor.name, total_cost)

    # Print the final routing tables
    for router in routers:
        print(f"Routing table for Router {router.name}:")
        for destination, (next_hop, cost) in router.routing_table.items():
            print(f"Destination: {destination}, Next Hop: {next_hop}, Cost: {cost}")

if __name__ == '__main__':
    main()



class Router:
    def __init__(self, name):
        self.name = name
        self.routing_table = {}  # Routing table: destination -> (next_hop, cost)

    def update_routing_table(self, destination, next_hop, cost):
        self.routing_table[destination] = (next_hop, cost)



# class Router:: Defines a class named Router to represent a network router.

# def __init__(self, name):: Defines the initialization method for the Router class.
# Initializes attributes name (router's name) and routing_table (an empty dictionary to store routing information).

# def update_routing_table(self, destination, next_hop, cost):: Defines a method to update 
# the router's routing table. It takes parameters for destination, next hop, and cost, and updates 
# the routing_table dictionary with this information.

# python
# Copy code
# def main():
#     # Create routers
#     router_a = Router('A')
#     router_b = Router('B')
#     router_c = Router('C')

#     # Initialize routing tables
#     router_a.update_routing_table('A', None, 0)
#     router_a.update_routing_table('B', 'B', 1)
#     router_a.update_routing_table('C', 'C', 3)
    
#     # (Similar initialization for router_b and router_c)

# if __name__ == '__main__':
#     main()
# def main():: Defines the main function of the program.

# Creating Routers: Creates three routers (router_a, router_b, router_c) with names 
# 'A', 'B', 'C' using the Router class.

# Initializing Routing Tables: Initializes the routing tables for each router using 
# the update_routing_table() method. This simulates initial routing information, setting 
# costs for direct connections.

# python
# Copy code
#     # Simulate distance-vector routing (Bellman-Ford algorithm)
#     routers = [router_a, router_b, router_c]
#     num_iterations = 5  # Number of iterations
    
#     # (DVR algorithm simulation)
# routers = [router_a, router_b, router_c]: Creates a list containing 
# all the routers created.

# num_iterations = 5: Defines the number of iterations for the DVR 
# algorithm simulation.

# python
# Copy code
#     for _ in range(num_iterations):
#         for router in routers:
#             for destination, (next_hop, cost) in router.routing_table.items():
#                 for neighbor in routers:
#                     if neighbor != router:
#                         # (Routing table update logic)
    
#     # Print the final routing tables
#     for router in routers:
#         # (Printing routing tables)
# DVR Algorithm Simulation Loop: Iterates through each router's routing table for a 
# specified number of iterations.

# Routing Table Update Logic: For each router, iterates through its routing table, considers 
# neighbors' routing tables, and updates its own routing table based on the Bellman-Ford algorithm.

# Printing Final Routing Tables: Prints the final routing tables for each router after 
# the iterations, showing the destination, next hop, and cost to reach each destination.

# This code simulates the distance-vector routing algorithm among routers in a simple
#  network and prints the resulting routing tables after the simulation.