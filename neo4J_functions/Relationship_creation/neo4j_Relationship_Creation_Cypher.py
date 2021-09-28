''' Neo4J Database Cypher Statements for Relationship Creation. '''


# Function to create INCREASE_IN relationship from Statement Node to Indicator Node in Neo4J database
def create_INCREASE_IN_Relationship_to_Statement_Node(tx , statementType , name_of_statement , name_of_Indicator) :
    statement_type_string = f"MATCH (statement:{statementType}"
    tx.run(statement_type_string + " {name: $name_of_statement}) "
                                   "MATCH (INCREASE_IN_Indicator:Indicator {name: $name_of_Indicator }) "
                                   "CREATE (statement)-[relationship:INCREASE_IN]->(INCREASE_IN_Indicator)" ,
           name_of_statement=name_of_statement ,
           name_of_Indicator=name_of_Indicator ,
           statementType=statementType)


# Function to create DECREASE_IN relationship from Statement Node to Indicator Node in Neo4J database
def create_DECREASE_IN_Relationship_to_Statement_Node(tx , statementType , name_of_statement , name_of_Indicator) :
    statement_type_string = f"MATCH (statement:{statementType}"
    tx.run(statement_type_string + " {name: $name_of_statement}) "
                                   "MATCH (DECREASE_IN_Indicator:Indicator {name: $name_of_Indicator }) "
                                   "CREATE (statement)-[relationship:DECREASE_IN]->(DECREASE_IN_Indicator)" ,
           name_of_statement=name_of_statement ,
           name_of_Indicator=name_of_Indicator ,
           statementType=statementType)


# Function to create INCREASES relationship from Statement Node to Indicator Node in Neo4J database
def create_INCREASES_Relationship_to_Statement_Node(tx , statementType , name_of_statement , name_of_Indicator) :
    statement_type_string = f"MATCH (statement:{statementType}"
    tx.run(statement_type_string + " {name: $name_of_statement}) "
                                   "MATCH (INCREASES_Indicator:Indicator {name: $name_of_Indicator }) "
                                   "CREATE (statement)-[relationship:INCREASES]->(INCREASES_Indicator)" ,
           name_of_statement=name_of_statement ,
           name_of_Indicator=name_of_Indicator ,
           statementType=statementType)


# Function to create DECREASES relationship from Statement Node to Indicator Node in Neo4J database
def create_DECREASES_Relationship_to_Statement_Node(tx , statementType , name_of_statement , name_of_Indicator) :
    statement_type_string = f"MATCH (statement:{statementType}"
    tx.run(statement_type_string + " {name: $name_of_statement}) "
                                   "MATCH (DECREASES_Indicator:Indicator {name: $name_of_Indicator }) "
                                   "CREATE (statement)-[relationship:DECREASES]->(DECREASES_Indicator)" ,
           name_of_statement=name_of_statement ,
           name_of_Indicator=name_of_Indicator ,
           statementType=statementType)


# Function to create INFLUENCES relationship from INCREASE_IN | :DECREASE_IN Indicator Nodes to INCREASES | :DECREASES Indicator Nodes in Neo4J database
def create_INFLUENCES_Relationship_to_Indicator_Nodes(tx , name_of_Indicator_IN , name_of_Indicator_S) :
    tx.run("MATCH (Indicator_IN:Indicator {name: $name_of_Indicator_IN }) "
           "MATCH (Indicator_S:Indicator {name: $name_of_Indicator_S }) "
           "CREATE (Indicator_IN)-[relationship:INFLUENCES]->(Indicator_S)" ,
           name_of_Indicator_IN=name_of_Indicator_IN ,
           name_of_Indicator_S=name_of_Indicator_S)


# Function to create IN_SEASON relationship from Statement Node to ClimatologyTime Node in Neo4J database
def create_IN_SEASON_Relationship_to_Statement_Node(tx , statementType , name_of_statement , name_of_ClimatologyTime) :
    statement_type_string = f"MATCH (statement:{statementType}"
    tx.run(statement_type_string + " {name: $name_of_statement}) "
                                   "MATCH (ClimatologyTime:ClimatologyTime {name: $name_of_ClimatologyTime }) "
                                   "CREATE (statement)-[relationship:IN_SEASON]->(ClimatologyTime)" ,
           name_of_statement=name_of_statement ,
           name_of_ClimatologyTime=name_of_ClimatologyTime ,
           statementType=statementType)


# Function to create IN_LOCATION relationship from Statement Node to SpaceRegion Node in Neo4J database
def create_IN_LOCATION_Relationship_to_Statement_Node(tx , statementType , name_of_statement , name_of_SpaceRegion) :
    statement_type_string = f"MATCH (statement:{statementType}"
    tx.run(statement_type_string + " {name: $name_of_statement}) "
                                   "MATCH (SpaceRegion:SpaceRegion {name: $name_of_SpaceRegion }) "
                                   "CREATE (statement)-[relationship:IN_LOCATION]->(SpaceRegion)" ,
           name_of_statement=name_of_statement ,
           name_of_SpaceRegion=name_of_SpaceRegion ,
           statementType=statementType)


# Function to create RELEVANT_TO relationship from Statement Node to Topic_Interests Node in Neo4J database
def create_RELEVANT_TO_Relationship_to_Statement_Node(tx , statementType , name_of_statement , name_of_Topic_Interests) :
    statement_type_string = f"MATCH (statement:{statementType}"
    tx.run(statement_type_string + " {name: $name_of_statement}) "
                                   "MATCH (Topic_Interests:Topic {name: $name_of_Topic_Interests }) "
                                   "CREATE (statement)-[relationship:RELEVANT_TO]->(Topic_Interests)" ,
           name_of_statement=name_of_statement ,
           name_of_Topic_Interests=name_of_Topic_Interests ,
           statementType=statementType)


# Function to create USING relationship from Statement Node to Topic_Strategy Node in Neo4J database
def create_USING_Relationship_to_Statement_Node(tx , statementType , name_of_statement , name_of_Topic_Strategy) :
    statement_type_string = f"MATCH (statement:{statementType}"
    tx.run(statement_type_string + " {name: $name_of_statement}) "
                                   "MATCH (Topic_Strategy:Topic {name: $name_of_Topic_Strategy }) "
                                   "CREATE (statement)-[relationship:USING]->(Topic_Strategy)" ,
           name_of_statement=name_of_statement ,
           name_of_Topic_Strategy=name_of_Topic_Strategy ,
           statementType=statementType)


# Not yet in use
# Function to create SUBREGION_OF relationship from primary_region SpaceRegion Node to secondary_region SpaceRegion Node in Neo4J database
def create_SUBREGION_OF_Relationship_to_SpaceRegion_Node(tx , name_of_primary_region , name_of_secondary_region) :
    tx.run("MATCH (primary_region:SpaceRegion {name: $name_of_primary_region }) "
           "MATCH (secondary_region:SpaceRegion {name: $name_of_secondary_region }) "
           "CREATE (primary_region)-[relationship:SUBREGION_OF]->(secondary_region)" ,
           name_of_primary_region=name_of_primary_region ,
           name_of_secondary_region=name_of_secondary_region)
