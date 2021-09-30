# Neo4J First party Python Binding
from neo4j import GraphDatabase

uri = "bolt://localhost:7687"
userName = "neo4j"
password = "password"

# Connect to the Neo4j database server
graphDB_Driver = GraphDatabase.driver(uri , auth=(userName , password))


# Detach and Delete Indicator nodes in Neo4J
def delete_indicator_data_in_neo4j(tx) :
    tx.run("MATCH (a:Indicator) "
           "DETACH DELETE a ")


# Detach and Delete Causal nodes in Neo4J
def delete_Causal_data_in_neo4j(tx) :
    tx.run("MATCH (b:Causal) "
           "DETACH DELETE b ")


# Detach and Delete Adaptation nodes in Neo4J
def delete_Adaptation_data_in_neo4j(tx) :
    tx.run("MATCH (b:Adaptation) "
           "DETACH DELETE b ")


# Detach and Delete Projection nodes in Neo4J
def delete_Projection_data_in_neo4j(tx) :
    tx.run("MATCH (b:Projection) "
           "DETACH DELETE b ")


# Detach and Delete Solution nodes in Neo4J
def delete_Solution_data_in_neo4j(tx) :
    tx.run("MATCH (b:Solution) "
           "DETACH DELETE b ")


# Detach and Delete Impact nodes in Neo4J
def delete_Impact_data_in_neo4j(tx) :
    tx.run("MATCH (b:Impact) "
           "DETACH DELETE b ")


# Detach and Delete SpaceRegion nodes in Neo4J
def delete_SpaceRegion_data_in_neo4j(tx) :
    tx.run("MATCH (c:SpaceRegion) "
           "DETACH DELETE c ")


# Detach and Delete Topic nodes in Neo4J
def delete_Topic_data_in_neo4j(tx) :
    tx.run("MATCH (d:Topic) "
           "DETACH DELETE d ")


# Detach and Delete TimeRange nodes in Neo4J
def delete_TimeRange_data_in_neo4j(tx) :
    tx.run("MATCH (e:TimeRange) "
           "DETACH DELETE e ")


# Detach and Delete ClimatologyTime nodes in Neo4J
def delete_ClimatologyTime_data_in_neo4j(tx) :
    tx.run("MATCH (f:ClimatologyTime) "
           "DETACH DELETE f")


with graphDB_Driver.session() as graphDB_Session :
    print("Attempting to delete all specified Neo4j Entries")
    graphDB_Session.write_transaction(delete_indicator_data_in_neo4j)
    graphDB_Session.write_transaction(delete_Causal_data_in_neo4j)
    graphDB_Session.write_transaction(delete_Adaptation_data_in_neo4j)
    graphDB_Session.write_transaction(delete_Projection_data_in_neo4j)
    graphDB_Session.write_transaction(delete_Solution_data_in_neo4j)
    graphDB_Session.write_transaction(delete_Impact_data_in_neo4j)
    graphDB_Session.write_transaction(delete_SpaceRegion_data_in_neo4j)
    graphDB_Session.write_transaction(delete_Topic_data_in_neo4j)
    graphDB_Session.write_transaction(delete_TimeRange_data_in_neo4j)
    graphDB_Session.write_transaction(delete_ClimatologyTime_data_in_neo4j)
    print("Deleted all specified Neo4j Entries")
