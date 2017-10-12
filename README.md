# drongo-lime-surveys
Scripts for lime survey for Drongo festival 2017
In particular the js scripts for the dialect survey and what's in the face survey.
it also contains helper classes to generate surveys from data.

##Getting Started
You will need npm installed and preferable nodemon.

##Overview of scripts

###Generating Surveys
To generate surveys see the package survey_generator. In particular start with the survey_creator.py file.
It explains what you need to provide/implement to create a survey.


###Analysis
in name-face/analysis are functions to clean up the results of the survey


###static-files
In the static files folder is the code that needs to be staticly served on a uu server to make the surveys work


### secure copy to server
In both name-face and dialect are bash script to copy the necessary files to the server.




