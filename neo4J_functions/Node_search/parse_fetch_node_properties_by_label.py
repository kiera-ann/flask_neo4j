# Parse Fetch of Nodes by label type

# Imports
from neo4J_functions.Node_search.node_search_cypher_string_builder import create_cypher_query_string_SpaceRegion_properties
from neo4J_functions.Node_search.node_search_cypher_string_builder import create_cypher_query_string_TimeRange_properties
from neo4J_functions.Node_search.node_search_cypher_string_builder import create_cypher_query_string_ClimatologyTime_properties
from neo4J_functions.Node_search.node_search_cypher_string_builder import create_cypher_query_string_Name_Description
from neo4J_functions.Node_search.node_search_cypher_string_builder import create_cypher_query_string_Statement_properties


# SpaceRegion
def parse_fetch_SpaceRegion_properties(graphDB_Driver , nodeType) :
    sorted_list_of_dict_to_return = []  # Initialize list for final return of sorted dictionary data
    with graphDB_Driver.session() as graphDB_Session :
        list_of_names = []  # Initialize empty list which stores all node names
        node_query_string = create_cypher_query_string_SpaceRegion_properties(nodeType)  # Build Statement Query Cypher String
        nodes = graphDB_Session.run(node_query_string)  # Find all nodes with Node label name provided
        data_dict = { }
        for node in nodes :
            node_label_name = node["node_label_name"].strip()
            data_dict[node_label_name] = {
                "name" : node_label_name ,
                "nodeType" : nodeType ,
                "poly_x" : node["SpaceRegion_poly_x"] ,
                "poly_y" : node["SpaceRegion_poly_y"] ,
                "abbreviation" : node["SpaceRegion_abbreviation"] ,
                "postalCode" : node["SpaceRegion_postalCode"] ,
                "existing" : True
            }
            list_of_names.append(node_label_name)  # Append list with node names

        # Sorting list in case-insensitive manner
        new_list_of_names = (sorted(list_of_names , key=lambda s : s.casefold()))

        for sorted_name in new_list_of_names :
            sorted_list_of_dict_to_return.append(data_dict[sorted_name])

    return sorted_list_of_dict_to_return


# TimeRange
def parse_fetch_TimeRange_properties(graphDB_Driver , nodeType) :
    sorted_list_of_dict_to_return = []  # Initialize list for final return of sorted dictionary data
    with graphDB_Driver.session() as graphDB_Session :
        list_of_names = []  # Initialize empty list which stores all node names
        node_query_string = create_cypher_query_string_TimeRange_properties(nodeType)  # Build Statement Query Cypher String
        nodes = graphDB_Session.run(node_query_string)  # Find all nodes with Node label name provided
        data_dict = { }
        for node in nodes :
            node_label_name = node["node_label_name"].strip()
            data_dict[node_label_name] = {
                "name" : node_label_name ,
                "nodeType" : nodeType ,
                "description" : node["node_label_description"] ,
                "start_date" : node["TimeRange_start_date"] ,
                "end_date" : node["TimeRange_end_date"] ,
                "existing" : True
            }
            list_of_names.append(node_label_name)  # Append list with node names

        # Sorting list in case-insensitive manner
        new_list_of_names = (sorted(list_of_names , key=lambda s : s.casefold()))

        for sorted_name in new_list_of_names :
            sorted_list_of_dict_to_return.append(data_dict[sorted_name])

    return sorted_list_of_dict_to_return


# ClimatologyTime
def parse_fetch_ClimatologyTime_properties(graphDB_Driver , nodeType) :
    sorted_list_of_dict_to_return = []  # Initialize list for final return of sorted dictionary data
    with graphDB_Driver.session() as graphDB_Session :
        list_of_names = []  # Initialize empty list which stores all node names
        node_query_string = create_cypher_query_string_ClimatologyTime_properties(nodeType)  # Build Statement Query Cypher String
        nodes = graphDB_Session.run(node_query_string)  # Find all nodes with Node label name provided
        data_dict = { }
        for node in nodes :
            node_label_name = node["node_label_name"].strip()
            data_dict[node_label_name] = {
                "name" : node_label_name ,
                "nodeType" : nodeType ,
                "description" : node["node_label_description"] ,
                "start_date" : node["ClimatologyTime_start_date"] ,
                "end_date" : node["ClimatologyTime_end_date"] ,
                "existing" : True
            }
            list_of_names.append(node_label_name)  # Append list with node names

        # Sorting list in case-insensitive manner
        new_list_of_names = (sorted(list_of_names , key=lambda s : s.casefold()))

        for sorted_name in new_list_of_names :
            sorted_list_of_dict_to_return.append(data_dict[sorted_name])

    return sorted_list_of_dict_to_return


# Topic, Indicator
def parse_fetch_Node_name_description(graphDB_Driver , nodeType) :
    sorted_list_of_dict_to_return = []  # Initialize list for final return of sorted dictionary data
    with graphDB_Driver.session() as graphDB_Session :
        list_of_names = []  # Initialize empty list which stores all node names
        node_query_string = create_cypher_query_string_Name_Description(nodeType)  # Build Statement Query Cypher String
        nodes = graphDB_Session.run(node_query_string)  # Find all nodes with Node label name provided
        data_dict = { }
        for node in nodes :
            node_label_name = node["node_label_name"].strip()
            data_dict[node_label_name] = {
                "name" : node_label_name ,
                "nodeType" : nodeType ,
                "description" : node["node_label_description"] ,
                "existing" : True
            }
            list_of_names.append(node_label_name)  # Append list with node names

        # Sorting list in case-insensitive manner
        new_list_of_names = (sorted(list_of_names , key=lambda s : s.casefold()))

        for sorted_name in new_list_of_names :
            sorted_list_of_dict_to_return.append(data_dict[sorted_name])

    return sorted_list_of_dict_to_return


# Individual Statements – EITHER ONE: Causal , Adaptation , Projection , Solution , Impact)
def parse_fetch_individual_Statement_properties(graphDB_Driver , nodeType) :
    sorted_list_of_dict_to_return = []  # Initialize list for final return of sorted dictionary data
    with graphDB_Driver.session() as graphDB_Session :
        list_of_names = []  # Initialize empty list which stores all node names
        node_query_string = create_cypher_query_string_Statement_properties(nodeType)  # Build Statement Query Cypher String
        nodes = graphDB_Session.run(node_query_string)  # Find all nodes with Node label name provided
        data_dict = { }
        for node in nodes :
            node_label_name = node["node_label_name"].strip()
            data_dict[node_label_name] = {
                "name" : node_label_name ,
                "nodeType" : nodeType ,
                "description" : node["node_label_description"] ,
                "source" : node["Statement_source"] ,
                "existing" : True
            }
            list_of_names.append(node_label_name)  # Append list with node names

        # Sorting list in case-insensitive manner
        new_list_of_names = (sorted(list_of_names , key=lambda s : s.casefold()))

        for sorted_name in new_list_of_names :
            sorted_list_of_dict_to_return.append(data_dict[sorted_name])

    return sorted_list_of_dict_to_return


# All inclusive Statements (Causal , Adaptation , Projection , Solution , Impact)
def parse_fetch_all_Statement_properties(graphDB_Driver , nodeType) :
    sorted_list_of_dict_to_return = []  # Initialize list for final return of sorted dictionary data
    list_of_names = []  # Initialize empty list which stores all node names
    data_dict = { }
    for statement_type in nodeType :
        with graphDB_Driver.session() as graphDB_Session :
            node_query_string = create_cypher_query_string_Statement_properties(statement_type)  # Build Statement Query Cypher String
            nodes = graphDB_Session.run(node_query_string)  # Find all nodes with Node label name provided
            for node in nodes :
                node_label_name = node["node_label_name"].strip()
                data_dict[node_label_name] = {
                    "name" : node_label_name ,
                    "nodeType" : statement_type ,
                    "description" : node["node_label_description"] ,
                    "source" : node["Statement_source"] ,
                    "existing" : True
                }
                list_of_names.append(node_label_name)  # Append list with node names

    # Sorting list in case-insensitive manner
    new_list_of_names = (sorted(list_of_names , key=lambda s : s.casefold()))

    for sorted_name in new_list_of_names :
        sorted_list_of_dict_to_return.append(data_dict[sorted_name])

    return sorted_list_of_dict_to_return
