# Import Python's native json library
import json

# Custom Python modules

# Function to convert response string data to python dictionary for further processing
def convert_form_data_json(form_data_string):
    # Convert string to JSON data as python dictionary
    form_json_object = json.loads(form_data_string)

    # Extract relevant dictionary data to variables
    Statement_data = form_json_object['submit_form_data']['Statement'] # Statement_data
    Indicator_data = form_json_object['submit_form_data']['Indicator'] # Indicator Data
    SpaceRegion_data = form_json_object['submit_form_data']['SpaceRegion'] # SpaceRegion Data
    ClimatologyTime_data = form_json_object['submit_form_data']['ClimatologyTime'] # ClimatologyTime Data
    Topic_Interests_data = form_json_object['submit_form_data']['Topic']['Interests'] # Topic Data - Interests
    Topic_Strategy_data = form_json_object['submit_form_data']['Topic']['Strategy'] # Topic Data - Strategy
    TimeRange_data = form_json_object['submit_form_data']['TimeRange'] # TimeRange Data

    # Conditional for new node creation
    # if existing = False in data received