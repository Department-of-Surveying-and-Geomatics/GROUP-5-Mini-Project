# GROUP-5-Mini-Project

This project was developed by Shaun Chigogora R1911272P, Osely T. Mtandabute R226360J and Tinevimbo L. Mudzibwi R2211745T

# Traverse Analyzer

# Overview
The Traverse Analyzer is a Python-based application that allows users to analyse and visualise traverse data. It provides the following functionalities:

1. **Data Parsing**: The application can read traverse data from a CSV file and validate the input data to ensure it meets the required criteria.
2. **Traverse Analysis**: The application calculates the total number of traverse legs, the minimum and maximum easting and northing values, and the distance and bearing between any two specified traverse points.
3. **Visualization**: The application generates a plot that displays the traverse points and legs, along with the selected points and their labels.

# Instructions

1. **Install Dependencies**: Ensure that you have the following Python packages installed: `pandas`, `geopandas`, `matplotlib`, and `tkinter`. You can install them using pip:

   ```
   pip install pandas geopandas matplotlib
   ```

2. **Run the Application**: Execute the `Main.py` file to start the Traverse Analyzer application. This will launch a graphical user interface (GUI) window.

3. **Select Traverse Data File**: Click the "Browse" button in the GUI to select the CSV file containing the traverse data.

4. **Specify Points of Interest**: Enter the point numbers (e.g., 1, 2) for which you want to calculate the distance and bearing.

5. **Analyze the Traverse Data**: Click the "Analyze" button to perform the traverse analysis. The results will be displayed in the text box on the right side of the GUI.

6. **View the Traverse Plot**: The application will generate a plot of the traverse data, indicating the selected points and display it in the GUI.

## Tools Functionality 
1.	The `dataParsing.py` file handles the parsing and validation of the traverse data CSV file.
2.	The `traverseAnalysis.py` file contains the functions responsible for performing the traverse analysis calculations.
3.	The `Plotting.py` file generates the visual representation of the traverse data and analysis results.
4.	The `Main.py` file is the main entry point of the application and coordinates the interaction between the GUI and the other modules.

