# Import Python's native json library
import json
from pprint import pprint


# Get the Json data from the response data
form_json_data = '''{
   "submit_form_data":{
      "Statement":{
         "statementType":"Causal",
         "existing":false,
         "name":"Humans produce CO2",
         "description":"CO2 levels in the atmosphere are rising due to human actions.",
         "source":"IPCC-AR5",
         "ShortQuote":""
      },
      "Indicator":{
         "INCREASE_IN":{
            "filled":true,
            "data":[
               {
                  "existing":false,
                  "name":"fossil fuel burning",
                  "description":""
               },
               {
                  "existing":false,
                  "name":"deforestation",
                  "description":""
               }
            ]
         },
         "DECREASE_IN":{
            "filled":true,
            "data":[
               {
                  "existing":false,
                  "name":"local humidity",
                  "description":""
               },
               {
                  "existing":false,
                  "name":"snowpack",
                  "description":""
               }
            ]
         },
         "INCREASES":{
            "filled":true,
            "data":[
               {
                  "existing":false,
                  "name":"atmospheric CO2",
                  "description":""
               },
               {
                  "existing":false,
                  "name":"water quality",
                  "description":""
               }
            ]
         },
         "DECREASES":{
            "filled":true,
            "data":[
               {
                  "existing":false,
                  "name":"forest biodiversity",
                  "description":""
               },
               {
                  "existing":false,
                  "name":"traditional culture",
                  "description":""
               }
            ]
         }
      },
      "ClimatologyTime":{
         "filled":true,
         "data":[
            {
               "existing":false,
               "name":"annual",
               "description":"",
               "start_date":"",
               "end_date":""
            }
         ]
      },
      "SpaceRegion":{
         "filled":true,
         "data":[
            {
               "existing":false,
               "name":"global",
               "abbreviation":"",
               "poly_x":"",
               "poly_y":"",
               "postalCode":""
            }
         ]
      },
      "Topic":{
         "Interests":{
            "filled":true,
            "data":[
               {
                  "existing":false,
                  "name":"energy",
                  "description":""
               },
               {
                  "existing":false,
                  "name":"policy",
                  "description":""
               },
               {
                  "existing":false,
                  "name":"economy",
                  "description":""
               },
               {
                  "existing":false,
                  "name":"society",
                  "description":""
               }
            ]
         },
         "Strategy":{
            "filled":true,
            "data":[
               {
                  "existing":false,
                  "name":"diversify agriculture practices to combat vulnerability",
                  "description":""
               },
               {
                  "existing":false,
                  "name":"STRIPS use for prairie lands",
                  "description":""
               }
            ]
         }
      },
      "TimeRange":{
         "filled":false,
         "data":[
            {
               "existing":false,
               "name":"",
               "description":"",
               "start_date":"",
               "end_date":""
            }
         ]
      }
   }
}'''

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