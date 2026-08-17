# Climate Related Knowledge Graph Project

This project is a significant refactor of the pre-existing backend the knowledge base graph system that utilized a 
climate based ontology for categorizing and linking climate related events and factors. 

The previous implementation, not written by myself, loaded all data from the Neo4J graph backend into computer memory 
from a local CSV and presented the data use Python's Plotly Dash framework.

Under the previous method, students manually entered data into a CSV without knowledge of pre-existing data which 
meant that exact duplicates, or duplicate-like nodes were recreated and there was a loss in the number of 
relationships that could be made by this approach. For example: 

Release of Carbon Dioxide [NODE]  INCREASES [RElATIONSHIP] -> Global Temperatures [NODE]
Release of CO2 [NODE]  INCREASES [RElATIONSHIP] -> Average Global Temperatures [NODE]

Because the data entry are being done by multiple students at different times without collaboration, the same 
relationship could be entered using different Nodes which results in a separate linking of two concepts. This 
reduces the number of relationships from which inferences can be made from.

With this backend, the Cypher language of the Neo4J framework was utilized for querying of similar words while data 
entry was done on a front end webpage. This allowed students to select an already existing Node that is similar to 
what they were about to enter minimizing duplicates.

In addition, with the use of the Cypher Query Language, data from an all encompassing CSV file was not pulled into 
memory at run time, but only selected (or queried) Nodes and their relationships were fetched. This meant that the 
UI was much more responsive at startup and when a visual representation of the knowledge base was viewed.

Lastly, this approach used in refactoring the project meant that the project was decoupled in a manner that allowed 
different 
visualization approaches, be it web based data entry and viewing or a native application for a desktop where as the 
previous approach did not allow for this separation and reusability.


