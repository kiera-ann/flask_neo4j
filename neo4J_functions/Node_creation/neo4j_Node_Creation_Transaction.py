''' Neo4J Database Node Creation Write Transaction. '''

# Neo4J First party Python Binding
from neo4j import GraphDatabase

# Custom Modules for Neo4J Database Cypher Statements for Node Creation
from neo4J_functions.Node_creation.neo4j_Node_Creation_Cypher import create_Statement_Node
from neo4J_functions.Node_creation.neo4j_Node_Creation_Cypher import create_Indicator_Node
from neo4J_functions.Node_creation.neo4j_Node_Creation_Cypher import create_ClimatologyTime_Node
from neo4J_functions.Node_creation.neo4j_Node_Creation_Cypher import create_SpaceRegion_postalCode_Node
from neo4J_functions.Node_creation.neo4j_Node_Creation_Cypher import create_SpaceRegion_Node
from neo4J_functions.Node_creation.neo4j_Node_Creation_Cypher import create_Topic_Interests_Node
from neo4J_functions.Node_creation.neo4j_Node_Creation_Cypher import create_Topic_Strategy_Node
from neo4J_functions.Node_creation.neo4j_Node_Creation_Cypher import create_TimeRange_Node

# Neo4J Server Credentials
# uri = "neo4j://localhost:7687"
uri = "bolt://localhost:7687"  # From Dr. Pershing graph.py script
userName = "neo4j"
password = "password"

def perform_neo4j_write_transaction_Node_creation(data_dict) :
    data_for_node_creation = data_dict
    print(data_for_node_creation)
    # Connect to the Neo4j database server
    graphDB_Driver = GraphDatabase.driver(uri , auth=(userName , password))

    # Perform checks in data_dict dictionary and execute Node creation write transactions only as needed
    if "Statement" in data_for_node_creation :
        statementType = data_for_node_creation['Statement']['statementType']
        name = data_for_node_creation['Statement']['name']
        description = data_for_node_creation['Statement']['description']
        source = data_for_node_creation['Statement']['source']
        ShortQuote = data_for_node_creation['Statement']['ShortQuote']
        with graphDB_Driver.session() as graphDB_Session :
            graphDB_Session.write_transaction(create_Statement_Node ,
                                              statementType=statementType ,
                                              name=name ,
                                              description=description ,
                                              source=source ,
                                              ShortQuote=ShortQuote)

    if "INCREASE_IN" in data_for_node_creation :
        for index in range(len(data_for_node_creation['INCREASE_IN'])) :
            name = data_for_node_creation['INCREASE_IN'][index]['name']
            description = data_for_node_creation['INCREASE_IN'][index]['description']
            with graphDB_Driver.session() as graphDB_Session :
                graphDB_Session.write_transaction(create_Indicator_Node ,
                                                  name=name ,
                                                  description=description)

    if "DECREASE_IN" in data_for_node_creation :
        for index in range(len(data_for_node_creation['DECREASE_IN'])) :
            name = data_for_node_creation['DECREASE_IN'][index]['name']
            description = data_for_node_creation['DECREASE_IN'][index]['description']
            with graphDB_Driver.session() as graphDB_Session :
                graphDB_Session.write_transaction(create_Indicator_Node ,
                                                  name=name ,
                                                  description=description)

    if "INCREASES" in data_for_node_creation :
        for index in range(len(data_for_node_creation['INCREASES'])) :
            name = data_for_node_creation['INCREASES'][index]['name']
            description = data_for_node_creation['INCREASES'][index]['description']
            with graphDB_Driver.session() as graphDB_Session :
                graphDB_Session.write_transaction(create_Indicator_Node ,
                                                  name=name ,
                                                  description=description)

    if "DECREASES" in data_for_node_creation :
        for index in range(len(data_for_node_creation['DECREASES'])) :
            name = data_for_node_creation['DECREASES'][index]['name']
            description = data_for_node_creation['DECREASES'][index]['description']
            with graphDB_Driver.session() as graphDB_Session :
                graphDB_Session.write_transaction(create_Indicator_Node ,
                                                  name=name ,
                                                  description=description)

    if "SpaceRegion" in data_for_node_creation :
        for index in range(len(data_for_node_creation['SpaceRegion'])) :
            if data_for_node_creation['SpaceRegion'][index]['postalCode'] != "" :
                name = data_for_node_creation['SpaceRegion'][index]['name']
                abbreviation = data_for_node_creation['SpaceRegion'][index]['abbreviation']
                poly_x = data_for_node_creation['SpaceRegion'][index]['poly_x']
                poly_y = data_for_node_creation['SpaceRegion'][index]['poly_y']
                postalCode = data_for_node_creation['SpaceRegion'][index]['postalCode']
                with graphDB_Driver.session() as graphDB_Session :
                    graphDB_Session.write_transaction(create_SpaceRegion_postalCode_Node ,
                                                      name=name ,
                                                      abbreviation=abbreviation ,
                                                      poly_x=poly_x ,
                                                      poly_y=poly_y ,
                                                      postalCode=postalCode)
            else :
                name = data_for_node_creation['SpaceRegion'][index]['name']
                abbreviation = data_for_node_creation['SpaceRegion'][index]['abbreviation']
                poly_x = data_for_node_creation['SpaceRegion'][index]['poly_x']
                poly_y = data_for_node_creation['SpaceRegion'][index]['poly_y']
                with graphDB_Driver.session() as graphDB_Session :
                    graphDB_Session.write_transaction(create_SpaceRegion_Node ,
                                                      name=name ,
                                                      abbreviation=abbreviation ,
                                                      poly_x=poly_x ,
                                                      poly_y=poly_y)

    if "ClimatologyTime" in data_for_node_creation :
        for index in range(len(data_for_node_creation['ClimatologyTime'])) :
            name = data_for_node_creation['ClimatologyTime'][index]['name']
            description = data_for_node_creation['ClimatologyTime'][index]['description']
            start_date = data_for_node_creation['ClimatologyTime'][index]['start_date']
            end_date = data_for_node_creation['ClimatologyTime'][index]['end_date']
            with graphDB_Driver.session() as graphDB_Session :
                graphDB_Session.write_transaction(create_ClimatologyTime_Node ,
                                                  name=name ,
                                                  description=description ,
                                                  start_date=start_date ,
                                                  end_date=end_date)

    if "Topic_Interests" in data_for_node_creation :
        for index in range(len(data_for_node_creation['Topic_Interests'])) :
            name = data_for_node_creation['Topic_Interests'][index]['name']
            description = data_for_node_creation['Topic_Interests'][index]['description']
            with graphDB_Driver.session() as graphDB_Session :
                graphDB_Session.write_transaction(create_Topic_Interests_Node ,
                                                  name=name ,
                                                  description=description)

    if "Topic_Strategy" in data_for_node_creation :
        for index in range(len(data_for_node_creation['Topic_Strategy'])) :
            name = data_for_node_creation['Topic_Strategy'][index]['name']
            description = data_for_node_creation['Topic_Strategy'][index]['description']
            with graphDB_Driver.session() as graphDB_Session :
                graphDB_Session.write_transaction(create_Topic_Strategy_Node ,
                                                  name=name ,
                                                  description=description)

    if "TimeRange" in data_for_node_creation :
        for index in range(len(data_for_node_creation['TimeRange'])) :
            name = data_for_node_creation['TimeRange'][index]['name']
            description = data_for_node_creation['TimeRange'][index]['description']
            start_date = data_for_node_creation['TimeRange'][index]['start_date']
            end_date = data_for_node_creation['TimeRange'][index]['end_date']
            with graphDB_Driver.session() as graphDB_Session :
                graphDB_Session.write_transaction(create_TimeRange_Node ,
                                                  name=name ,
                                                  description=description ,
                                                  start_date=start_date ,
                                                  end_date=end_date)

    graphDB_Driver.close()
