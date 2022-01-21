# Import Python's native json library
import json

# Custom Python modules
from neo4J_functions.Node_creation.neo4j_Node_Creation_Transaction import perform_neo4j_write_transaction_Node_creation
from neo4J_functions.Relationship_creation.neo4j_Relationship_Creation_Transaction import perform_neo4j_write_transaction_Relationship_creation


# Function to convert response string data to python dictionary for further processing
def convert_form_data_json(form_data_string) :
    list_of_fields_filled = []  # Initialize List
    dict_of_fields_filled = { }  # Initialize dictionary
    # Convert string to JSON data as python dictionary
    form_json_object = json.loads(form_data_string)

    # Extract relevant dictionary data to variables
    Statement_data = form_json_object['submit_form_data']['Statement']  # Statement_data
    Indicator_data = form_json_object['submit_form_data']['Indicator']  # Indicator Data
    SpaceRegion_data = form_json_object['submit_form_data']['SpaceRegion']  # SpaceRegion Data
    ClimatologyTime_data = form_json_object['submit_form_data']['ClimatologyTime']  # ClimatologyTime Data
    Topic_Interests_data = form_json_object['submit_form_data']['Topic']['Interests']  # Topic Data - Interests
    Topic_Strategy_data = form_json_object['submit_form_data']['Topic']['Strategy']  # Topic Data - Strategy
    TimeRange_data = form_json_object['submit_form_data']['TimeRange']  # TimeRange Data

    # Conditional checks for new node creation
    # if filled = True in data received, then append to 'list_of_fields_filled', and add to 'dict_of_fields_filled'
    # Since Statement field must always have data, include Statement in 'list_of_fields_filled' and 'dict_of_fields_filled' by default
    list_of_fields_filled.append("Statement")
    dict_of_fields_filled['Statement'] = Statement_data
    # Indicator_data
    if Indicator_data['INCREASE_IN']['filled'] == True :
        list_of_fields_filled.append("INCREASE_IN")
        dict_of_fields_filled['INCREASE_IN'] = Indicator_data['INCREASE_IN']['data']
    if Indicator_data['DECREASE_IN']['filled'] == True :
        list_of_fields_filled.append("DECREASE_IN")
        dict_of_fields_filled['DECREASE_IN'] = Indicator_data['DECREASE_IN']['data']
    if Indicator_data['INCREASES']['filled'] == True :
        list_of_fields_filled.append("INCREASES")
        dict_of_fields_filled['INCREASES'] = Indicator_data['INCREASES']['data']
    if Indicator_data['DECREASES']['filled'] == True :
        list_of_fields_filled.append("DECREASES")
        dict_of_fields_filled['DECREASES'] = Indicator_data['DECREASES']['data']
    # SpaceRegion_data
    if SpaceRegion_data['filled'] == True :
        list_of_fields_filled.append("SpaceRegion")
        dict_of_fields_filled['SpaceRegion'] = SpaceRegion_data['data']
    # ClimatologyTime_data
    if ClimatologyTime_data['filled'] == True :
        list_of_fields_filled.append("ClimatologyTime")
        dict_of_fields_filled['ClimatologyTime'] = ClimatologyTime_data['data']
    # Topic_Interests_data
    if Topic_Interests_data['filled'] == True :
        list_of_fields_filled.append("Topic_Interests")
        dict_of_fields_filled['Topic_Interests'] = Topic_Interests_data['data']
    # Topic_Strategy_data
    if Topic_Strategy_data['filled'] == True :
        list_of_fields_filled.append("Topic_Strategy")
        dict_of_fields_filled['Topic_Strategy'] = Topic_Strategy_data['data']
    # TimeRange_data
    if TimeRange_data['filled'] == True :
        list_of_fields_filled.append("TimeRange")
        dict_of_fields_filled['TimeRange'] = TimeRange_data['data']

    # Debug print lines
    # print(list_of_fields_filled)
    # print(len(list_of_fields_filled))
    # pprint(dict_of_fields_filled)

    # Write Nodes
    perform_neo4j_write_transaction_Node_creation(dict_of_fields_filled)
    # Write relationships
    perform_neo4j_write_transaction_Relationship_creation(dict_of_fields_filled)
