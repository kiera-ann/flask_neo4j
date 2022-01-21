''' Functions that generate cypher strings for search of Nodespecified properties once provide Node label name (variable: node_label_name)'''


# Function to generate Cypher string for Node query of Name and Description
def create_cypher_query_string_Name_Description(node_label_name) :
    # Example of completed built query string
    # cql = "MATCH (x:SpaceRegion) RETURN x.name AS Space" # SpaceRegion

    # Portions of query string
    cypher_query_str_1 = "MATCH (x:"
    label_name = str(node_label_name)
    cypher_query_str_2 = ") RETURN x.name AS node_label_name, x.description AS node_label_description"
    complete_query_string = cypher_query_str_1 + label_name + cypher_query_str_2  # Concatenate full query string
    return complete_query_string


# Function to generate Cypher string for all TimeRange Node Properties
def create_cypher_query_string_TimeRange_properties(node_label_name) :
    cypher_query_str_1 = "MATCH (x:"
    label_name = str(node_label_name)
    cypher_query_str_2 = ") RETURN x.name AS node_label_name, " \
                         "x.description AS node_label_description, " \
                         "x.start_date AS TimeRange_start_date, " \
                         "x.end_date AS TimeRange_end_date"
    complete_query_string = cypher_query_str_1 + label_name + cypher_query_str_2  # Concatenate full query string
    return complete_query_string


# Function to generate Cypher string for all SpaceRegion Node Properties
def create_cypher_query_string_SpaceRegion_properties(node_label_name) :
    cypher_query_str_1 = "MATCH (x:"
    label_name = str(node_label_name)
    cypher_query_str_2 = ") RETURN x.name AS node_label_name, " \
                         "x.abbreviation AS SpaceRegion_abbreviation, " \
                         "x.poly_x AS SpaceRegion_poly_x," \
                         "x.poly_y AS SpaceRegion_poly_y," \
                         "x.postalCode AS SpaceRegion_postalCode"

    complete_query_string = cypher_query_str_1 + label_name + cypher_query_str_2  # Concatenate full query string
    return complete_query_string


# Function to generate Cypher string for all ClimatologyTime Node Properties
def create_cypher_query_string_ClimatologyTime_properties(node_label_name) :
    cypher_query_str_1 = "MATCH (x:"
    label_name = str(node_label_name)
    cypher_query_str_2 = ") RETURN x.name AS node_label_name, " \
                         "x.description AS node_label_description, " \
                         "x.start_date AS ClimatologyTime_start_date, " \
                         "x.end_date AS ClimatologyTime_end_date"
    complete_query_string = cypher_query_str_1 + label_name + cypher_query_str_2  # Concatenate full query string
    return complete_query_string

# Function to generate Cypher string for all Statement Node Properties
def create_cypher_query_string_Statement_properties(node_label_name) :
    cypher_query_str_1 = "MATCH (x:"
    label_name = str(node_label_name)
    cypher_query_str_2 = ") RETURN x.name AS node_label_name, " \
                         "x.description AS node_label_description, " \
                         "x.source AS Statement_source"
    complete_query_string = cypher_query_str_1 + label_name + cypher_query_str_2  # Concatenate full query string
    return complete_query_string
