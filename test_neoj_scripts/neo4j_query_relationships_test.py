# Neo4J First party Python Binding
from neo4j import GraphDatabase

uri = "bolt://localhost:7687"
userName = "neo4j"
password = "password"

# Connect to the Neo4j database server
graphDB_Driver = GraphDatabase.driver(uri , auth=(userName , password))

# Example of completed built query string
# cql = "MATCH (x:DIRECTED) RETURN x"
cql = "MATCH p=(a)-[r:PRODUCED]->(b) RETURN a, b, r"  # This is how you search for relationships


# with graphDB_Driver.session() as graphDB_Session :
#     list_of_names = []  # Initialize empty list which stores all node names
#     nodes = graphDB_Session.run(cql)  # Find all nodes with Node label name provided
#     for node in nodes :
#         print(node['a'])
#         print(node['a']['name'])
#         print(node['b']['tagline'])
#         # print(type(node))
#         # string = str(node)
#         # string_eval = eval(string)
#         # print(string_eval)
#         # list_of_names.append(node["name_needed"].strip())
#         # print(node["Person"].name)
#         # print(node['a.name'])
#         # # print(node["p.Person.name"])
#         # print(node["p"]["Person"]['name'])

#  You can use CREATE to insert nodes, relationships, and patterns into Neo4j.
def create_new_person(tx, name):
    tx.run("CREATE (:Person {name: $name})", name=name,)
    # tx.run("MATCH (a:Person) WHERE a.name = $name "
    #        "CREATE (a)-[:KNOWS]->(:Person {name: $friend})",
    #        name=name,)

# we run two MATCH queries before we create a relationship between the nodes
def create_relationship(tx , person_A, person_B) :
    tx.run("MATCH (a:Person {name: $person_A}) "
           "MATCH (b:Person) WHERE b.name = $person_B "
           "CREATE (a)-[rel:DOES_NOT_LIKE]->(b)"
           , person_A=person_A, person_B=person_B )
    # tx.run("MATCH (a:Person) WHERE a.name = $name "
    #        "CREATE (a)-[:KNOWS]->(:Person {name: $friend})",
    #        name=name,)

# Creating nodes (.write_transaction)
# tx = transaction_function
# with graphDB_Driver.session() as graphDB_Session :
#     graphDB_Session.write_transaction(create_new_person, "Jane")

with graphDB_Driver.session() as graphDB_Session :
    graphDB_Session.write_transaction(create_relationship, "Alice" ,"Jane")


#  Finding nodes. (.read_transaction)
# with graphDB_Driver.session() as graphDB_Session :
#     graphDB_Session.read_transaction(transaction_function, "Alice")

# MODIFY
# to modify the properties of a node, first matching the pattern you want to find and
# use the SET keyword to add, remove, or update properties
# MATCH (p:Person {name: 'Jennifer'})
# SET p.birthdate = date('1980-01-01')

# DELETE
#  To delete a relationship, you need to find the start and end nodes for the relationship you want to delete
#  and then use the DELETE keyword ont he relationship
# Note: you cannot delete a node if it still has relationships
# MATCH (j:Person {name: 'Jennifer'})-[r:IS_FRIENDS_WITH]->(m:Person {name: 'Mark'})
# DELETE r
# To delete a node that does not have any relationships,
# you need to find the node you want to delete and then use the DELETE keyword
# MATCH (m:Person {name: 'Mark'})
# DELETE m

# OR we can actually run a single statement to delete the node and relationship at the same time.
# Using the DETACH DELETE syntax tells Cypher to delete any relationships the node has, as well as remove the node itself
# MATCH (m:Person {name: 'Mark'})
# DETACH DELETE m

# Delete Properties
# first option is to use REMOVE on the property
# delete property using REMOVE keyword
# MATCH (n:Person {name: 'Jennifer'})
# REMOVE n.birthdate
# second option is to use the SET keyword from earlier to set the property value to null
# delete property with SET to null value
# MATCH (n:Person {name: 'Jennifer'})
# SET n.birthdate = null

# Avoiding Duplicate Data Using MERGE
# to avoid creating duplicate data. One of those ways is by using the MERGE keyword.
# MERGE does a "select-or-insert" operation that first checks if the data exists in the database
# MERGE (mark:Person {name: 'Mark'})
# RETURN mark