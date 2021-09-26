''' Function to search for names for specified Nodes once provide Node label name (variable: node_label_name)'''
# Neo4J First party Python Binding
from neo4j import GraphDatabase

# Neo4J Server Credentials
# uri = "neo4j://localhost:7687"
uri = "bolt://localhost:7687"  # From Dr. Pershing graph.py script
userName = "neo4j"
password = "climate"

# Connect to the Neo4j database server
graphDB_Driver = GraphDatabase.driver(uri , auth=(userName , password))

# List of node label names
Indicator = "Indicator"
SpaceRegion = "SpaceRegion"
ClimatologyTime = "ClimatologyTime"
Topic = "Topic"
TimeRange = "TimeRange"
# Statement Nodes
Causal = "Causal"
Adaptation = "Adaptation"
Projection = "Projection"
Solution = "Solution"
Impact = "Impact"

# Function to generate Cypher string for Node query
def create_cypher_query_string(node_label_name):
    # Example of completed built query string
    # cql = "MATCH (x:SpaceRegion) RETURN x.name AS Space" # SpaceRegion

    # Portions of query string
    cql1 = "MATCH (x:"
    label_name= str(node_label_name)
    cql2= ") RETURN x.name AS name_needed"

    # Concatenate full query string
    complete_query_string = cql1 + label_name + cql2
    # print(complete_query_string) # Debug Print line
    return complete_query_string

# create_cypher_query_string(Impact) # Debug Print line

# Execute the CQL query
def find_node_names(node_label_name):
    node_label_name = str(node_label_name)
    node_query_string = create_cypher_query_string(node_label_name)
    # print(node_query_string) # Debug Print line

    with graphDB_Driver.session() as graphDB_Session :
        list_of_names = [] # Initialize empty list which stores all node names
        data_to_return = {} # Initialize dictionary
        nodes = graphDB_Session.run(node_query_string) # Find all nodes with Node label name provided
        for node in nodes :
            list_of_names.append(node["name_needed"].strip())  # Append list and remove white spaces on left and right of string
        # pprint(list_of_spaces)
        # print(len(list_of_spaces))
        # print(type(list_of_spaces[0]))  # each element is of type string

        # Sorting list in case-insensitive manner
        # https://www.geeksforgeeks.org/python-ways-to-sort-list-of-strings-in-case-insensitive-manner/
        # print(sorted(list_of_names , key=lambda s : s.casefold())) # Debug Print line
        new_list_of_names = (sorted(list_of_names , key=lambda s : s.casefold()))
        # print()
        # print(new_list_of_names) # Debug Print line

    # Terminate connection to Neo4J Server
    graphDB_Driver.close()

    # Make dictionary for return
    data_to_return = {
        node_label_name : new_list_of_names
    }

    # print(data_to_return) # Debug Print line
    return data_to_return

# find_node_names(Impact)