''' Neo4J Database Cypher Statements for Node Creation. '''


# Function to create Statement Node in Neo4J database
def create_Statement_Node(tx , statementType , name , description , source , ShortQuote) :
    statement_type_string = f"CREATE (:{statementType}"
    tx.run(statement_type_string+ " {name: $name, description: $description, source: $source, statementType: $statementType, ShortQuote: $ShortQuote})" ,
           name=name ,
           description=description ,
           source=source ,
           statementType=statementType ,
           ShortQuote=ShortQuote)


# Function to create Indicator Node in Neo4J database
def create_Indicator_Node(tx , name , description) :
    tx.run("CREATE (:Indicator {name: $name, description: $description})" ,
           name=name ,
           description=description)


# Function to create ClimatologyTime Node in Neo4J database
def create_ClimatologyTime_Node(tx , name , description , start_date , end_date) :
    tx.run("CREATE (:ClimatologyTime {name: $name, description: $description, start_date: $start_date, end_date: $end_date})" ,
           name=name ,
           description=description ,
           start_date=start_date ,
           end_date=end_date)


# Function to create SpaceRegion (that has postalCode) Node in Neo4J database
def create_SpaceRegion_postalCode_Node(tx , name , abbreviation , poly_x , poly_y , postalCode) :
    tx.run("CREATE (:SpaceRegion {name: $name, abbreviation: $abbreviation, poly_x: $poly_x, poly_y: $poly_y, postalCode: $postalCode})" ,
           name=name ,
           abbreviation=abbreviation ,
           poly_x=poly_x ,
           poly_y=poly_y ,
           postalCode=postalCode)


# Function to create SpaceRegion (that does not have postalCode) Node in Neo4J database
def create_SpaceRegion_Node(tx , name , abbreviation , poly_x , poly_y) :
    tx.run("CREATE (:SpaceRegion {name: $name, abbreviation: $abbreviation, poly_x: $poly_x, poly_y: $poly_y})" ,
           name=name ,
           abbreviation=abbreviation ,
           poly_x=poly_x ,
           poly_y=poly_y)


# Function to create Topic_Interests Node in Neo4J database
def create_Topic_Interests_Node(tx , name , description) :
    tx.run("CREATE (:Topic {name: $name, description: $description})" ,
           name=name ,
           description=description)


# Function to create Topic_Strategy Node in Neo4J database
def create_Topic_Strategy_Node(tx , name , description) :
    tx.run("CREATE (:Topic {name: $name, description: $description})" ,
           name=name ,
           description=description)


# Function to create TimeRange Node in Neo4J database
def create_TimeRange_Node(tx , name , description , start_date , end_date) :
    tx.run("CREATE (:TimeRange {name: $name, description: $description, start_date: $start_date, end_date: $end_date})" ,
           name=name ,
           description=description ,
           start_date=start_date ,
           end_date=end_date)
