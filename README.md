# FreedmenColonies
Freedmen Colonies Mapping
# GitHub Documentation

## Introduction
This documentation provides an overview and explanation of the code snippet provided. The code is written in Python and utilizes the Census API to retrieve demographic data for specific locations based on latitude and longitude values provided in a CSV file. The retrieved data is processed and stored in a list, which is then converted into a formatted table and saved to a CSV file.

## Code Explanation
Below is a step-by-step explanation of the code:

1. Installation:
   Before running the code, ensure that the `census` and `tabulate` packages are installed. If not, you can install them by running the following command:
   ```python
   # Commented out IPython magic to ensure Python compatibility.
   # %pip install census
   ```

2. Importing Required Libraries:
   The necessary libraries are imported at the beginning of the code:
   ```python
   import csv
   from census import Census
   from tabulate import tabulate
   ```

3. Setting up the Census API:
   To use the Census API, an API key is required. Replace `"xyz123"` with your actual API key:
   ```python
   api_key = "xyz123"  # Replace with your actual API key
   census_client = Census(api_key)
   ```

4. Creating Data Storage:
   An empty list, `census_data_list`, is created to store the retrieved census data:
   ```python
   census_data_list = []
   ```

5. Specifying CSV File Path:
   Specify the actual path to your CSV file by replacing `"/content/fcoi.csv"`:
   ```python
   csv_file_path = "/content/fcoi.csv"  # Replace with the actual path to your CSV file
   ```

6. Reading CSV File:
   The CSV file is opened using `csv.DictReader` to read the file and treat each row as a dictionary:
   ```python
   with open(csv_file_path, "r") as csv_file:
       csv_reader = csv.DictReader(csv_file)
   ```

7. Retrieving Census Data:
   For each row in the CSV file, latitude and longitude values are extracted, and a request is made to the Census API to retrieve relevant data:
   ```python
   for row in csv_reader:
       state = row["STATEFIPS"]
       county = row["COUNTYFIPS"]
       tract = row["TRACT"]
       latitude = row["latitude"]  # Replace with the correct column name for latitude
       longitude = row["longitude"]  # Replace with the correct column name for longitude

       census_data = census_client.acs5.state_county_tract(
           ("NAME","B01003_001E", "B01001_002E", "B01001_026E", "B01001B_001E", "B01001I_001E", "B06012_004E"),
           state,
           county,
           tract,
           year=2020,
           lat=latitude,
           lon=longitude
       )
   ```

8. Processing Census Data:
   The retrieved census data is processed by iterating over the results and extracting the required information:
   ```python
   for result in census_data:
       name = result["NAME"]
       total_population = result["B01003_001E"]
       male_population = result["B01001_002E"]
       female_population = result["B01001_026E"]
       black = result["B01001B_001E"]
       latino = result["B01001I_001E"]
       poverty = result["B06012_004E"]

       census_row = {
           "name": name,
           "total_population

          
          Sure! Here's a GitHub README documentation for the code you provided:

```markdown
# Streamlit Interactive Dashboard and Map

This is a Streamlit application that displays an interactive dashboard and map based on GeoJSON data.

## Getting Started

To run this application locally, follow the steps below:

1. Clone the repository:

```bash
git clone https://github.com/your-username/your-repo.git
```

2. Install the required dependencies:

```bash
pip install streamlit pandas geopandas requests
```

3. Run the Streamlit application:

```bash
streamlit run app.py
```

4. Access the application in your web browser at `http://localhost:8501`.

## Usage

Once you have the application running, you can explore the following features:

### GeoJSON Data

The GeoJSON data is displayed as a GeoDataFrame. It shows the geographic features and associated properties.

### Map

The map visualizes the GeoJSON data on an interactive map. You can zoom in and out to explore the data.

### Individual Variables

The individual variables are displayed for each feature in the GeoJSON data. The variables include:

- Name
- Total Population
- Male Population
- Female Population
- Black Population
- Latino Population
- Poverty
- Prime Name
- Other Name
- Risk Score
- SOVI Score

## Data Source

The GeoJSON data used in this application is obtained from the following URL:

- [FreedmenColonies GeoJSON](https://raw.githubusercontent.com/ChisholmLegacyProject/FreedmenColonies/main/FC.geojson)

Please make sure you have a stable internet connection to access the data.

## Dependencies

- streamlit
- pandas
- geopandas
- requests

You can install the required dependencies using the following command:

```bash
pip install -r requirements.txt
```

## License

This project is licensed under the [MIT License](LICENSE).
```

Feel free to modify the content based on your specific needs.
