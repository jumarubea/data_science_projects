# Nobel Prize Analysis 

## Table of Content
- [#Overview](#overview)
- [#Prerequisites](#prerequisites)
- [#Usage](#usage)
- [#Code-Explanation](#code-explanation)
- [#Output](#output)
- [#Note](#note)

## Overview
This Python script analyzes Nobel Prize data to extract insights about the gender and birth country of laureates, as well as trends over decades in terms of USA-born winners, female laureates, and repeat winners.

## Prerequisites
- Python 3
- Pandas
- Seaborn
- NumPy

## Usage
1. Ensure you have Python 3 installed on your system.
2. Install the required libraries by running:
   ```
   pip install pandas seaborn numpy
   ```
3. Download the `nobel.csv` file containing the Nobel Prize data.
4. Run the provided Python script in your preferred Python environment.

## Code Explanation
- The script reads the Nobel Prize data from the `nobel.csv` file into a Pandas DataFrame.
- It identifies the most commonly awarded gender and birth country of Nobel laureates.
- It calculates the proportion of USA-born winners per decade and identifies the decade with the highest proportion of US-born winners.
- It optionally plots the proportion of USA-born winners over decades using Seaborn.
- It calculates the proportion of female laureates per decade and category and identifies the decade and category with the highest proportion of female laureates.
- It optionally plots the proportion of female winners over decades by category using Seaborn.
- It identifies the first woman to win a Nobel Prize and her respective category.
- It selects laureates who have received 2 or more prizes and displays their names.

## Output
The script outputs the following information:
- The most commonly awarded gender and birth country of Nobel laureates.
- The decade with the highest proportion of USA-born winners.
- Optionally, a plot showing the proportion of USA-born winners over decades.
- The decade and category with the highest proportion of female laureates.
- Optionally, a plot showing the proportion of female winners over decades by category.
- The first woman to win a Nobel Prize and her respective category.
- The names of laureates who have received 2 or more prizes.

## Note
- Ensure the `nobel.csv` file is present in the same directory as the script or provide the correct path to the file.
