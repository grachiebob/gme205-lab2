# Gme 205: Laboratory 2
## Simple Spatial Objects in Python

### *Description*
This project teaches how to design and implement spatial objects (points and pointsets) in Python using object-oriented programming. 

### *Dependencies*
* Python 3.14
* Visual Studio Code
* GitHub
* pandas
* matplotlib

### *How to set up the virtual environment?*
This is the first thing to do before starting this project. Here are the steps to set up a virtual environment:
1. Open the Visual Studio Code.
2. Under the VS Code Terminal tab, select "New Terminal."
3. Run this code:<br>
        `py -m venv .venv`<br>
        `.\.venv\Scripts\activate`<br>

### *Help*
While performing this project, I encountered a simple error that took me about 30 minutes to 1 hour to discover the error. In the `points.csv` file, I mistakenly loaded the file in a tab separation instead of using commas. We need to check for common syntax error such a misisng `)`, `}`, incorrect indentation, or other misplaced punctuation.

### *Reflection*
1. Object VS Geometry<br>
  Opening *points.csv* in Excel shows a tabulated data such as ID, longitude, latitude, names, and tags. It simply shows the values without doing anything, just a mere display of table. These data cannot manipulate themselves. However, modeling points as objects changed the way how I thought about the data by giving each point a behavior and identity. As objects, points could validate or measure distances on their own.<br>
2. Responsibility<br>
   The `Point` class focuses on a single identity. For instance, Point A has a longitude of 121.0 and a latitude of 14.6. This class is used for validation, distance function (`distance_to`), and organization (`to_tuple`). For instance, we calculate the distance of Point P to Point Q, or represent points as a group that cannot be changed. On the other hand, the `PointSet` class focuses on lists or collection of points. It can count and filter `POIs` in the `points.csv` using `count` and `filter_by_tag`, or compute the boundaries such as the lowest and highest coordinates using `bbox`. Lastly, the runner script, `run_lab2.py`, is responsible for the execution of tasks with the assigned spatial objects. For example, plotting a scatter plot and creating a summary report is implemeted in the runner script as it visualizes the assigned `Point` and `PointSet`.<br>
3. Modeling Insight<br>
    Separating geometry, meaning, and behavior made the spatial logic easier to understand because it kept things simple and clear. Geometry are the raw numbers like the longitude and latitude. Meaning is what the object represents, such as a building or a POI. Behavior is what the object can do, such as the distance function. Separating these features avoids "*God Object*" or mixing everything all together that keeps the collection messy and confusing. It is also easier to find errors and fix them quickly.<br> 

## Author
Maria Graciella L. Roque  
Discord:[@grachiebob]

## Acknowledgements
* GmE 205 Laboratory Exercise 2 Manual
* [MarkDown] (https://www.markdownguide.org/cheat-sheet/)
* [W3Schools] (https://www.w3schools.com/python/python_lists.asp)

Edited on VS Code