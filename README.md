# The online map-based accent-recognition task: a new pathway for perceptual dialectology

Perceptual dialectologists have come up with diverse methods to investigate how listeners represent the spatial structure of language variation. The diversity in methodological approaches however has made it difficult to generalize perceptual boundaries between language varieties and perceptual isoglosses for any given variety over different speakers, limiting their interpretability. 

Pinget & Voeten (2023) have developed a novel task-independent methodology to solve this problem: the map-based accent-recognition task. In Pinget & Voeten (2023) and Voeten & Pinget (under review), this task is applied to Dutch as spoken in the Netherlands, a language which lends itself well to the study due to notable regional accents within a well-defined standard language. Using the map-based recognition task in which 1,578 listeners placed 40 representative speakers on a map based on fragments of their speech, the regional biases in accent recognition are investigated.

The aim is to demonstrate how the task can be used to reach novel conclusions about listeners’ mental representations of the spoken diatopic variation in a given linguistic situation. It demonstrates one very relevant type of output that the task can produce: a map showing direct perceptual associations between speech and space. The map-based accent-recognition allows to draw new conclusions on the nature of the Dutch dialect continuum as it exists throughout the Netherlands by charting out an empirical map of the dialect regions, based entirely in perception. 

## References

Pinget, A.C.H. & Voeten, C. C. (2023). Social factors in accent recognition: a large-scale study in perceptual dialectology. Journal of Linguistic Geography, 11(2), 78-90.

Voeten, C.C & A.C.H. Pinget (under review). The online map-based accent-recognition task: a new pathway for perceptual dialectology.


## Code
Scripts for lime survey for Drongo festival 2017 It contains in particular the static files that are needed to make the surveys work. It also contains helper classes to generate surveys from data.

### Getting Started
You will need npm installed and preferable nodemon.

### Overview of scripts

#### Generating Surveys
To generate surveys see the package survey_generator. In particular start with the survey_creator.py file.
It explains what you need to provide/implement to create a survey.


#### Analysis
in name-face/analysis are functions to clean up the results of the survey


#### Static-files
In the static files folder is the code that needs to be staticly served on a uu server to make the surveys work


#### secure copy to server
In both name-face and dialect are bash script to copy the necessary files to the server.




