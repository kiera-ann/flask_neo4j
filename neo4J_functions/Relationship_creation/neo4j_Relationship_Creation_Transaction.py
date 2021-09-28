''' Neo4J Database Cypher Statements for executing Relationship Creation Transaction. '''

# Neo4J First party Python Binding
from neo4j import GraphDatabase

# Custom Modules for Neo4J Database Cypher Statements for Node Relationship Creation
from neo4J_functions.Relationship_creation.neo4j_Relationship_Creation_Cypher import create_INCREASE_IN_Relationship_to_Statement_Node
from neo4J_functions.Relationship_creation.neo4j_Relationship_Creation_Cypher import create_DECREASE_IN_Relationship_to_Statement_Node
from neo4J_functions.Relationship_creation.neo4j_Relationship_Creation_Cypher import create_INCREASES_Relationship_to_Statement_Node
from neo4J_functions.Relationship_creation.neo4j_Relationship_Creation_Cypher import create_DECREASES_Relationship_to_Statement_Node
from neo4J_functions.Relationship_creation.neo4j_Relationship_Creation_Cypher import create_INFLUENCES_Relationship_to_Indicator_Nodes
from neo4J_functions.Relationship_creation.neo4j_Relationship_Creation_Cypher import create_IN_SEASON_Relationship_to_Statement_Node
from neo4J_functions.Relationship_creation.neo4j_Relationship_Creation_Cypher import create_IN_LOCATION_Relationship_to_Statement_Node
from neo4J_functions.Relationship_creation.neo4j_Relationship_Creation_Cypher import create_RELEVANT_TO_Relationship_to_Statement_Node
from neo4J_functions.Relationship_creation.neo4j_Relationship_Creation_Cypher import create_USING_Relationship_to_Statement_Node
from neo4J_functions.Relationship_creation.neo4j_Relationship_Creation_Cypher import create_SUBREGION_OF_Relationship_to_SpaceRegion_Node

# Neo4J Server Credentials
# uri = "neo4j://localhost:7687"
uri = "bolt://localhost:7687"  # From Dr. Pershing graph.py script
userName = "neo4j"
password = "password"


def perform_neo4j_write_transaction_Relationship_creation(data_dict) :
    data_for_node_creation = data_dict
    # print(data_for_node_creation)

    # Connect to the Neo4j database server
    graphDB_Driver = GraphDatabase.driver(uri , auth=(userName , password))

    # Perform checks in data_dict dictionary and execute Node relationship write transactions only as needed
    if "Statement" in data_for_node_creation :
        statementType = data_for_node_creation['Statement']['statementType']
        name_of_statement = data_for_node_creation['Statement']['name']
        if "INCREASE_IN" in data_for_node_creation :
            for index in range(len(data_for_node_creation['INCREASE_IN'])) :
                name_of_Indicator = data_for_node_creation['INCREASE_IN'][index]['name']
                with graphDB_Driver.session() as graphDB_Session :
                    graphDB_Session.write_transaction(create_INCREASE_IN_Relationship_to_Statement_Node ,
                                                      name_of_statement=name_of_statement ,
                                                      name_of_Indicator=name_of_Indicator ,
                                                      statementType=statementType)

        if "DECREASE_IN" in data_for_node_creation :
            for index in range(len(data_for_node_creation['DECREASE_IN'])) :
                name_of_Indicator = data_for_node_creation['DECREASE_IN'][index]['name']
                with graphDB_Driver.session() as graphDB_Session :
                    graphDB_Session.write_transaction(create_DECREASE_IN_Relationship_to_Statement_Node ,
                                                      name_of_statement=name_of_statement ,
                                                      name_of_Indicator=name_of_Indicator ,
                                                      statementType=statementType)

        if "INCREASES" in data_for_node_creation :
            for index in range(len(data_for_node_creation['INCREASES'])) :
                name_of_Indicator = data_for_node_creation['INCREASES'][index]['name']
                with graphDB_Driver.session() as graphDB_Session :
                    graphDB_Session.write_transaction(create_INCREASES_Relationship_to_Statement_Node ,
                                                      name_of_statement=name_of_statement ,
                                                      name_of_Indicator=name_of_Indicator ,
                                                      statementType=statementType)

        if "DECREASES" in data_for_node_creation :
            for index in range(len(data_for_node_creation['DECREASES'])) :
                name_of_Indicator = data_for_node_creation['DECREASES'][index]['name']
                with graphDB_Driver.session() as graphDB_Session :
                    graphDB_Session.write_transaction(create_DECREASES_Relationship_to_Statement_Node ,
                                                      name_of_statement=name_of_statement ,
                                                      name_of_Indicator=name_of_Indicator ,
                                                      statementType=statementType)

        if "INCREASE_IN" in data_for_node_creation :
            for index in range(len(data_for_node_creation['INCREASE_IN'])) :
                name_of_Indicator_IN = data_for_node_creation['INCREASE_IN'][index]['name']
                if "INCREASES" in data_for_node_creation :
                    for index in range(len(data_for_node_creation['INCREASES'])) :
                        name_of_Indicator_S = data_for_node_creation['INCREASES'][index]['name']
                        with graphDB_Driver.session() as graphDB_Session :
                            graphDB_Session.write_transaction(create_INFLUENCES_Relationship_to_Indicator_Nodes ,
                                                              name_of_Indicator_IN=name_of_Indicator_IN ,
                                                              name_of_Indicator_S=name_of_Indicator_S)
                if "DECREASES" in data_for_node_creation :
                    for index in range(len(data_for_node_creation['DECREASES'])) :
                        name_of_Indicator_S = data_for_node_creation['DECREASES'][index]['name']
                        with graphDB_Driver.session() as graphDB_Session :
                            graphDB_Session.write_transaction(create_INFLUENCES_Relationship_to_Indicator_Nodes ,
                                                              name_of_Indicator_IN=name_of_Indicator_IN ,
                                                              name_of_Indicator_S=name_of_Indicator_S)
        if "DECREASE_IN" in data_for_node_creation :
            for index in range(len(data_for_node_creation['DECREASE_IN'])) :
                name_of_Indicator_IN = data_for_node_creation['DECREASE_IN'][index]['name']
                if "INCREASES" in data_for_node_creation :
                    for index in range(len(data_for_node_creation['INCREASES'])) :
                        name_of_Indicator_S = data_for_node_creation['INCREASES'][index]['name']
                        with graphDB_Driver.session() as graphDB_Session :
                            graphDB_Session.write_transaction(create_INFLUENCES_Relationship_to_Indicator_Nodes ,
                                                              name_of_Indicator_IN=name_of_Indicator_IN ,
                                                              name_of_Indicator_S=name_of_Indicator_S)
                if "DECREASES" in data_for_node_creation :
                    for index in range(len(data_for_node_creation['DECREASES'])) :
                        name_of_Indicator_S = data_for_node_creation['DECREASES'][index]['name']
                        with graphDB_Driver.session() as graphDB_Session :
                            graphDB_Session.write_transaction(create_INFLUENCES_Relationship_to_Indicator_Nodes ,
                                                              name_of_Indicator_IN=name_of_Indicator_IN ,
                                                              name_of_Indicator_S=name_of_Indicator_S)

        if "SpaceRegion" in data_for_node_creation :
            for index in range(len(data_for_node_creation['SpaceRegion'])) :
                name_of_SpaceRegion = data_for_node_creation['SpaceRegion'][index]['name']
                with graphDB_Driver.session() as graphDB_Session :
                    graphDB_Session.write_transaction(create_IN_LOCATION_Relationship_to_Statement_Node ,
                                                      name_of_statement=name_of_statement ,
                                                      name_of_SpaceRegion=name_of_SpaceRegion ,
                                                      statementType=statementType)

        if "ClimatologyTime" in data_for_node_creation :
            for index in range(len(data_for_node_creation['ClimatologyTime'])) :
                name_of_ClimatologyTime = data_for_node_creation['ClimatologyTime'][index]['name']
                with graphDB_Driver.session() as graphDB_Session :
                    graphDB_Session.write_transaction(create_IN_SEASON_Relationship_to_Statement_Node ,
                                                      name_of_statement=name_of_statement ,
                                                      name_of_ClimatologyTime=name_of_ClimatologyTime ,
                                                      statementType=statementType)

        if "Topic_Interests" in data_for_node_creation :
            for index in range(len(data_for_node_creation['Topic_Interests'])) :
                name_of_Topic_Interests = data_for_node_creation['Topic_Interests'][index]['name']
                with graphDB_Driver.session() as graphDB_Session :
                    graphDB_Session.write_transaction(create_RELEVANT_TO_Relationship_to_Statement_Node ,
                                                      name_of_statement=name_of_statement ,
                                                      name_of_Topic_Interests=name_of_Topic_Interests ,
                                                      statementType=statementType)

        if "Topic_Strategy" in data_for_node_creation :
            for index in range(len(data_for_node_creation['Topic_Strategy'])) :
                name_of_Topic_Strategy = data_for_node_creation['Topic_Strategy'][index]['name']
                with graphDB_Driver.session() as graphDB_Session :
                    graphDB_Session.write_transaction(create_USING_Relationship_to_Statement_Node ,
                                                      name_of_statement=name_of_statement ,
                                                      name_of_Topic_Strategy=name_of_Topic_Strategy ,
                                                      statementType=statementType)

    graphDB_Driver.close()
