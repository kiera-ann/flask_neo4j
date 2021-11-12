from flask import Flask , jsonify , request , Response

app = Flask(__name__)

# Disable sorting app-wide
app.config['JSON_SORT_KEYS'] = False

# from flask_accept import accept
from waitress import serve

# Custom functions=
from neo4J_functions.find_node_label_names import find_node_names  # Find Node name
from neo4J_functions.find_node_label_name_description import find_node_names_and_description  # Find Node name and description
# timestamp function
from utility_functions.time_stamp_api_call import utc_timestamp_data_api_call
# Handle submitted form data
from neo4J_functions.parse_submitted_form_data import convert_form_data_json


# General
# Get existing label name based on "label_name" sent in get request
@app.route('/api/v1/neo4j/existing_label_name/<label_name>' , methods=['GET'])
def fetch_existing_Neo4J_Node_label_names(label_name) :
    # Get Names of Nodes of interest
    names_of_nodes_dict = find_node_names(label_name)

    # Timestamp API call
    timestamp_utc_data_dict = utc_timestamp_data_api_call()

    # Combines data from all functions
    total_data_dict = {
        **names_of_nodes_dict ,
        **timestamp_utc_data_dict
    }
    json_data = jsonify(total_data_dict)

    # Enables CORS in Flask servers
    # Source: https://dev.to/matheusguimaraes/fast-way-to-enable-cors-in-flask-servers-42p0
    # Enable Access-Control-Allow-Origin
    json_data.headers.add("Access-Control-Allow-Origin" , "*")
    return json_data , 200


# Get existing label name and description based on "label_name" sent in get request
@app.route('/api/v1/neo4j/existing_label_name_description/<label_name>' , methods=['GET'])
def fetch_existing_Neo4J_Node_label_names_with_description(label_name) :
    # Get Names of Nodes and corresponding description of Interest
    names_of_nodes_description_dict = find_node_names_and_description(label_name)

    # Timestamp API call
    timestamp_utc_data_dict = utc_timestamp_data_api_call()

    # Combines data from all functions
    total_data_dict = {
        **names_of_nodes_description_dict ,
        **timestamp_utc_data_dict
    }
    json_data = jsonify(total_data_dict)
    json_data.headers.add("Access-Control-Allow-Origin" , "*")
    return json_data , 200


# Handles the JSON submitted through front end web form that handles Node creation and Node relationship creation
@app.route('/api/v1/process_form_data' , methods=['GET' , 'POST'])
def parse_request() :
    # data = request.data  # data is empty
    #  to decode the data sent by the client-side to UTF-8
    #  Source: https://stackoverflow.com/questions/57337321/flask-b-text-appears-before-request-data-results
    data_received_decoded = request.data.decode('UTF-8')
    # Processes the creation of Nodes and Node relationship
    convert_form_data_json(data_received_decoded)

    # if data_received_decoded:
    #     return Response(status=201)
    return Response(status=201)


if __name__ == '__main__' :
    # app.run(port=4567 , host='0.0.0.0' , ssl_context='adhoc')
    # app.run(port=4567 , host='0.0.0.0' , ssl_context='adhoc')
    # app.run(port=1234 , host='0.0.0.0', debug=True, ssl_context=('cert.pem', 'key.pem'))
    # serve(app , host='140.180.132.43' , port=4545)

    # Serve with waitress; Increase number of threads
    # serve(app, host='0.0.0.0', port=4545, threads= 10)
    app.run(port=4545 , host='0.0.0.0' , debug=True)
