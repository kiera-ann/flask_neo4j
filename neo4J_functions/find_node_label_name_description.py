''' Function to search for names for specified Nodes once provide Node label name (variable: node_label_name)'''
# Neo4J First party Python Binding
from neo4j import GraphDatabase

from collections import OrderedDict

# Neo4J Server Credentials
# uri = "neo4j://localhost:7687"
uri = "bolt://localhost:7687"  # From Dr. Pershing graph.py script
userName = "neo4j"
password = "climate"

# Connect to the Neo4j database server
graphDB_Driver = GraphDatabase.driver(uri , auth=(userName , password))

# List of Node label names
Indicator = "Indicator"
SpaceRegion = "SpaceRegion"
ClimatologyTime = "ClimatologyTime"
Topic = "Topic"
TimeRange = "TimeRange"
# Statement Node label names
Causal = "Causal"
Adaptation = "Adaptation"
Projection = "Projection"
Solution = "Solution"
Impact = "Impact"
Statement_Node_Labels = [Causal , Adaptation , Projection , Solution , Impact]
Other_Node_Labels = [Indicator , SpaceRegion , ClimatologyTime , Topic , TimeRange , Causal , Adaptation , Projection , Solution , Impact]
Other_Node_Labels_wo_SpaceRegion = [Indicator , ClimatologyTime , Topic , TimeRange , Causal , Adaptation , Projection , Solution , Impact]


# Function to generate Cypher string for Node query
def create_cypher_query_string(node_label_name) :
    # Example of completed built query string
    # cql = "MATCH (x:SpaceRegion) RETURN x.name AS Space" # SpaceRegion

    # Portions of query string
    cypher_query_str_1 = "MATCH (x:"
    label_name = str(node_label_name)
    cypher_query_str_2 = ") RETURN x.name AS node_label_name, x.description AS node_label_description"

    # Concatenate full query string
    complete_query_string = cypher_query_str_1 + label_name + cypher_query_str_2
    # print(complete_query_string) # Debug Print line
    return complete_query_string


# create_cypher_query_string(Impact) # Debug Function Print line


# Still to decide which to do; merely stylistic
# Remove period at the end if it exists
# if temp_dict_value[-1] == ".":
#     temp_dict_value = temp_dict_value[:-1]
# Adds period at the end if it does not exists
# if temp_dict_value[-1] != ".":
#     temp_dict_value = temp_dict_value + "."

def find_node_names_and_description(node_label_name) :
    data_dict = { }  # Initialize dictionary
    if node_label_name != "SpaceRegion" :
        if node_label_name == "Statements" :
            list_of_cypher_queries = []  # Initialize list
            # Makes list of cypher query strings
            for index in range(len(Statement_Node_Labels)) :
                node_label_name_statement_str = str(Statement_Node_Labels[index])
                list_of_cypher_queries.append(create_cypher_query_string(node_label_name_statement_str))  # List of Statement Query Cypher Strings
                # Executes queries to Neo4j database
                with graphDB_Driver.session() as graphDB_Session :
                    nodes = graphDB_Session.run(list_of_cypher_queries[index])
                    for node in nodes :
                        temp_dict_key = node["node_label_name"].strip()
                        temp_dict_value = node["node_label_description"].strip()
                        # Fills the dictionary with data from query
                        data_dict[temp_dict_key] = temp_dict_value

        else :
            if node_label_name in Other_Node_Labels_wo_SpaceRegion :
                with graphDB_Driver.session() as graphDB_Session :
                    node_query_string = create_cypher_query_string(node_label_name)
                    nodes = graphDB_Session.run(node_query_string)  # Find all nodes with Node label name provided
                    for node in nodes :
                        temp_dict_key = node["node_label_name"].strip()
                        temp_dict_value = node["node_label_description"].strip()
                        # Fills the dictionary with data from query
                        data_dict[temp_dict_key] = temp_dict_value

        data_dict_ordered = dict(OrderedDict(sorted(data_dict.items() , key=lambda i : i[0].lower())))
        # Make dictionary for data to be returned
        # data_to_return = {
        #     node_label_name : data_dict_ordered
        # }

        data_to_return = {
            'data' : data_dict_ordered
        }


    else :
        if node_label_name == "SpaceRegion" :
            with graphDB_Driver.session() as graphDB_Session :
                list_of_names = []  # Initialize empty list which stores all node names
                node_query_string = create_cypher_query_string(node_label_name)
                nodes = graphDB_Session.run(node_query_string)  # Find all nodes with Node label name provided
                for node in nodes :
                    list_of_names.append(node["node_label_name"].strip())

        # Sorting list in case-insensitive manner
        new_list_of_names = (sorted(list_of_names , key=lambda s : s.casefold()))

        # Make dictionary for data to be returned
        # data_to_return = {
        #     node_label_name : new_list_of_names
        # }
        data_to_return = {
            'data' : new_list_of_names
        }

    # Terminate connection to Neo4J Server
    graphDB_Driver.close()

    return data_to_return

# find_node_names_and_description(Impact) # Debug Function Print line
