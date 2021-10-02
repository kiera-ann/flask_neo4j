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
    # Initialize key variables in function
    node_label_name = str(node_label_name)  # Ensure variable "node_label_name" is of type string
    intermediate_list_of_dict_to_return = []  # Initialize list for temporary storage of list of data to return
    sorted_list_of_dict_to_return = []  # Initialize list for final return of sorted dictionary data

    # Since SpaceRegion Labelled Nodes do not contain "description" property, they are handled differently
    if node_label_name != "SpaceRegion" :
        # Special case if fetch request is for all Statements
        if node_label_name == "Statements" :
            list_of_node_label_name_statement_str = []  # Initialize list for storing all Statement Label Names
            for index in range(len(Statement_Node_Labels)) :
                node_label_name_statement_str = str(Statement_Node_Labels[index])
                list_of_node_label_name_statement_str.append(node_label_name_statement_str)

            temp_data_dict = { }  # Initialize dictionary for temporary storage of key: Node Label, values: list of names in specified Statement Node Label
            for node_label_name in list_of_node_label_name_statement_str :
                cypher_query_string = create_cypher_query_string(node_label_name)  # Build Statement Query Cypher String
                list_of_dictionary_name_description_nodes = []  # Initialize empty list which stores dictionary of node name and description
                with graphDB_Driver.session() as graphDB_Session :
                    nodes = graphDB_Session.run(cypher_query_string)  # Find all nodes with Statement Node label name provided
                    for node in nodes :
                        data_dict = { }  # Initialize dictionary
                        temp_dict_key = node["node_label_name"].strip()
                        temp_dict_value = node["node_label_description"].strip()
                        # Fills the dictionary with data from query
                        data_dict[temp_dict_key] = temp_dict_value
                        list_of_dictionary_name_description_nodes.append(data_dict)  # Append list with dictionary data
                temp_data_dict[node_label_name] = list_of_dictionary_name_description_nodes

            # Format dictionary with keys "name", "description", and "statementType"
            for statementType , NodeNames_w_Description in temp_data_dict.items() :
                for node_name_description in NodeNames_w_Description :
                    for node_name , node_description in node_name_description.items() :
                        dict_to_return = { }  # Initialize dictionary
                        dict_to_return['name'] = node_name
                        dict_to_return['description'] = node_description
                        dict_to_return['statementType'] = statementType
                        intermediate_list_of_dict_to_return.append(dict_to_return)
            sorted_list_of_dict_to_return = (sorted(intermediate_list_of_dict_to_return , key=lambda s : s['name'].casefold()))


        else :
            # Case where fetch is for Nodes with Labels other than "SpaceRegion" or "Statements"
            if node_label_name in Other_Node_Labels_wo_SpaceRegion :
                data_dict_to_sort = { }  # Initialize dictionary
                list_of_dictionary_name_description_nodes = []  # Initialize empty list which stores dictionary of node name and description
                temp_data_dict = { }  # Initialize dictionary for temporary storage of key: Node Label, values: list of names in specified Statement Node Label
                with graphDB_Driver.session() as graphDB_Session :
                    list_of_names = []  # Initialize empty list which stores all node names
                    cypher_query_string = create_cypher_query_string(node_label_name)  # Build Statement Query Cypher String
                    nodes = graphDB_Session.run(cypher_query_string)  # Find all nodes with Node label name provided
                    for node in nodes :
                        data_dict = { }  # Initialize dictionary
                        temp_dict_key = node["node_label_name"].strip()
                        temp_dict_value = node["node_label_description"].strip()
                        # Fills the dictionary with data from query
                        data_dict[temp_dict_key] = temp_dict_value
                        list_of_dictionary_name_description_nodes.append(data_dict)  # Append list with dictionary data
                    temp_data_dict[node_label_name] = list_of_dictionary_name_description_nodes

                # Format dictionary with keys "name", "description", and "statementType"
                for nodeType , NodeNames_w_Description in temp_data_dict.items() :
                    for node_name_description in NodeNames_w_Description :
                        for node_name , node_description in node_name_description.items() :
                            dict_to_return = { }  # Initialize dictionary
                            dict_to_return['name'] = node_name
                            dict_to_return['description'] = node_description
                            if node_label_name in Statement_Node_Labels :
                                dict_to_return['statementType'] = node_label_name
                            else :
                                dict_to_return['nodeType'] = node_label_name
                            intermediate_list_of_dict_to_return.append(dict_to_return)
                sorted_list_of_dict_to_return = (sorted(intermediate_list_of_dict_to_return , key=lambda s : s['name'].casefold()))


    else :
        if node_label_name == "SpaceRegion" :
            with graphDB_Driver.session() as graphDB_Session :
                list_of_names = []  # Initialize empty list which stores all node names
                node_query_string = create_cypher_query_string(node_label_name)  # Build Statement Query Cypher String
                nodes = graphDB_Session.run(node_query_string)  # Find all nodes with Node label name provided
                for node in nodes :
                    list_of_names.append(node["node_label_name"].strip())  # Append list and remove white spaces on left and right of string

            # Sorting list in case-insensitive manner
            new_list_of_names = (sorted(list_of_names , key=lambda s : s.casefold()))
            # Formatting of returned data into list of dictionary with keys "name" and type of node
            for node_name in new_list_of_names :
                dict_to_return = { }  # Initialize dictionary
                dict_to_return['name'] = node_name
                dict_to_return['nodeType'] = node_label_name
                sorted_list_of_dict_to_return.append(dict_to_return)

    data_to_return = {
        'data' : sorted_list_of_dict_to_return
    }

    # Terminate connection to Neo4J Server
    graphDB_Driver.close()

    return data_to_return

# find_node_names_and_description(Impact) # Debug Function Print line
# find_node_names_and_description("Statements")
# print(find_node_names_and_description("TimeRange"))
