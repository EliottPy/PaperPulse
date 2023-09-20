# PaperPulse

This aim of this project is to have a script editing regularly a personnal database with new research papers, using differents keywords. When I'll be satisfied with the scope of publishers, I will create a way to store the search results in a proper database.

## Using the project
You can use the *PaperPulse.sh* file for a direct execution. You can find below a complete list of arguments you can pass to *getPaper.py*.

| Parameter | type | default       | description                |
| --------- | ---- | ------------- | -------------------------- |
| -H        | bool | False         | Get articles from HAL      |
| -X        | bool | False         | Get articles from arXiv    |
| --nb      | int  | 1             | Number of articles to grab |
| --keys    | str  | keywords.yaml | Path to your keywords      | 

## Current scope 

| **Current publishers**  |  
|-------------------------|
| HAL                     |   
| arXiv                   |

## Current ways to find papers
The system takes all keywords from a yaml file, and search for them with AND operators

| **Ways to find papers**            |
|------------------------------------|
| Keywords in title                  |
| Keywords in abstract               |
| Authors' names                     |
| Companies the authors publish from |

## Futur archives that will be in the project

Futur publishers :
- papers with code

I'm open to suggestions to be able to search



Thank you to arXiv for use of its open access interoperability