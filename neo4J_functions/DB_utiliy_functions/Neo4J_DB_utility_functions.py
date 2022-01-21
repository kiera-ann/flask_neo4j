'''Neo4J Database Utility Functions using Neo4J First party Python Binding'''
# Imports
from neo4j import GraphDatabase  # Neo4J First party Python Binding


# Alternative Neo4J Server Credentials
# uri = "neo4j://localhost:7687"

# graphDB_Driver Object for connection to Neo4J database
class GraphDB_Driver() :
    # Credentials from Dr. Pershing graph.py script
    def __init__(self , uri="bolt://localhost:7687" , username="neo4j" , password="climate") :
        # Initialize Neo4j database server connection
        self.graphDB_Driver = GraphDatabase.driver(uri , auth=(username , password))

    # Connect to Neo4J Database
    def Connect_to_Neo4j_database_server(self) :
        return self.graphDB_Driver

    # Disconnect from Neo4J Database
    def Disconnect_from_Neo4j_database_server(self) :
        return self.graphDB_Driver.close()
