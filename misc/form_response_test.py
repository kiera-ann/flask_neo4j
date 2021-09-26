# Import Python's native json library
import json
from pprint import pprint
import pandas as pd

# Get the Json data from the response data
form_json_data = '''{
   "submit_form_data":{
      "Statement":{
         "statementType":{
            "Causal":false,
            "Adaptation":false,
            "Projection":false,
            "Solution":false,
            "Impact":false
         },
         "statement_properties":{
            "existing":false,
            "name":"",
            "description":"",
            "source":""
         }
      },
      "Indicator":{
         "INCREASES_IN":[
            {
               "existing":false,
               "name":"",
               "description":""
            }
         ],
         "DECREASES_IN":[
            {
               "existing":false,
               "name":"",
               "description":""
            }
         ],
         "INCREASES":[
            {
               "existing":false,
               "name":"",
               "description":""
            }
         ],
         "DECREASES":[
            {
               "existing":false,
               "name":"",
               "description":""
            }
         ]
      },
      "ClimatologyTime":[
         [
            {
               "existing":false,
               "name":"",
               "description":"",
               "start_date":"",
               "end_date":""
            }
         ]
      ],
      "SpaceRegion":[
         {
            "existing":false,
            "name":"",
            "abbreviation":"",
            "poly_x":"",
            "poly_y":"",
            "postalCode":""
         }
      ],
      "Topic":{
         "Interests":[
            {
               "existing":false,
               "name":"",
               "description":""
            }
         ],
         "Strategy":[
            {
               "existing":false,
               "name":"",
               "description":""
            }
         ]
      },
      "TimeRange":[
         {
            "existing":false,
            "name":"",
            "description":"",
            "start_date":"",
            "end_date":""
         }
      ]
   }
}'''

# https://appdividend.com/2020/11/07/how-to-convert-python-string-to-json-object/#:~:text=To%20convert%20a%20Python%20string,dictionary%20to%20access%20all%20elements.

form_json_object = json.loads(form_json_data)
# print(form_json_object)

dict_form_data = form_json_object['submit_form_data']
# print(dict_form_data)
# Statement Data
Statement_data = form_json_object['submit_form_data']['Statement']
print('Statement_data')
print(Statement_data)
print()

# Indicator Data
Indicator_data = form_json_object['submit_form_data']['Indicator']
print('Indicator_data')
print(Indicator_data)
print()

# SpaceRegion Data
SpaceRegion_data = form_json_object['submit_form_data']['SpaceRegion']
print('SpaceRegion_data')
print(SpaceRegion_data)
print()

# ClimatologyTime Data
ClimatologyTime_data = form_json_object['submit_form_data']['ClimatologyTime']
print('ClimatologyTime_data')
print(ClimatologyTime_data)
print()

# Topic Data - Interests
Topic_Interests_data = form_json_object['submit_form_data']['Topic']['Interests']
print('Topic_Interests_data')
print(Topic_Interests_data)
print()

# Topic Data - Strategy
Topic_Strategy_data = form_json_object['submit_form_data']['Topic']['Strategy']
print('Topic_Strategy_data')
print(Topic_Strategy_data)
print()


# TimeRange Data
TimeRange_data = form_json_object['submit_form_data']['TimeRange']
print('TimeRange_data')
print(TimeRange_data)
print()
print('End')






# print()
# print(stud_obj['submit_form_data'])
# print()
# print(stud_obj['submit_form_data'][0])
# print("The type of object is: ", type(stud_obj))
# json_obj = json.dumps(stud_obj)
# print(json_obj)
# print("The type of object is: ", type(json_obj))

# print(json_body)
# print(type(json_body))

# Convert that data into a python object...
# info = json.dumps(json_body)
# print(info)

# load_json = json.loads(info)
# print()
# print(load_json["submit_form_data"])


