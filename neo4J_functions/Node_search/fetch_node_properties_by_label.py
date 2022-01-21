''' Function to search for names for specified Nodes once provide Node label name (variable: node_label_name)'''
# Imports
from neo4J_functions.DB_utiliy_functions.Neo4J_DB_utility_functions import GraphDB_Driver  # Neo4J Graph Driver Object
from neo4J_functions.Node_search.parse_fetch_node_properties_by_label import parse_fetch_SpaceRegion_properties
from neo4J_functions.Node_search.parse_fetch_node_properties_by_label import parse_fetch_TimeRange_properties
from neo4J_functions.Node_search.parse_fetch_node_properties_by_label import parse_fetch_ClimatologyTime_properties
from neo4J_functions.Node_search.parse_fetch_node_properties_by_label import parse_fetch_Node_name_description
from neo4J_functions.Node_search.parse_fetch_node_properties_by_label import parse_fetch_individual_Statement_properties
from neo4J_functions.Node_search.parse_fetch_node_properties_by_label import parse_fetch_all_Statement_properties

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


# Fetch detailed Node Properties by Node label Name
def fetch_node_properties_by_label(nodeType) :
    graphDB_Driver_object = GraphDB_Driver()  # Initialize Neo4j database server object
    graphDB_Driver = graphDB_Driver_object.Connect_to_Neo4j_database_server()  # Connect to Neo4j database server

    # Initialize key variables in function
    nodeType = str(nodeType)  # Ensure variable "node_label_name" is of type string
    sorted_list_of_dict_to_return = []  # Initialize list for final return of sorted dictionary data

    # If SpaceRegion
    if nodeType == "SpaceRegion" :
        sorted_list_of_dict_to_return = parse_fetch_SpaceRegion_properties(graphDB_Driver , nodeType="SpaceRegion")

    # If TimeRange
    if nodeType == "TimeRange" :
        sorted_list_of_dict_to_return = parse_fetch_TimeRange_properties(graphDB_Driver , nodeType="TimeRange")

    # If ClimatologyTime
    if nodeType == "ClimatologyTime" :
        sorted_list_of_dict_to_return = parse_fetch_ClimatologyTime_properties(graphDB_Driver , nodeType="ClimatologyTime")

    # If Topic, Indicator
    if nodeType == "Topic" or nodeType == "Indicator" :
        sorted_list_of_dict_to_return = parse_fetch_Node_name_description(graphDB_Driver , nodeType)

    # If Statements (all) or individual Statements (Causal , Adaptation , Projection , Solution , Impact)
    if nodeType == "Statements" :
        nodeType = Statement_Node_Labels
        sorted_list_of_dict_to_return = parse_fetch_all_Statement_properties(graphDB_Driver , nodeType)

    # If individual Statements (Causal , Adaptation , Projection , Solution , Impact)
    if nodeType in Statement_Node_Labels :
        sorted_list_of_dict_to_return = parse_fetch_individual_Statement_properties(graphDB_Driver , nodeType)

    data_to_return = {
        'data' : sorted_list_of_dict_to_return
    }

    graphDB_Driver_object.Disconnect_from_Neo4j_database_server()  # Disconnect from Neo4J Database

    return data_to_return

# find_node_names_and_description(Impact) # Debug Function Print line
# find_node_names_and_description("Statements")
# print(find_node_names_and_description("TimeRange"))
