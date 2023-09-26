This package is for analyzing survey data from Deliberative Polling experiments. Although designed for Deliberative Polling, this package can be used to analyze survey data from any experiment.

The package is designed with a single, specialized function called `outputs`. This function is engineered to accept input files exclusively in the IBM SPSS Statistics `.SAV` format. Upon execution, it generates output files in both `.xlsx` and `.docx` formats. These output files contain comprehensive comparisons of responses across all designated treatment groups, time intervals, and statistical weights.

# Installation

To install SPSS, go to [Software at Stanford](https://software.stanford.edu) if you are a Stanford affiliate. Othwerwise, go to [IBM SPSS Software](https://www.ibm.com/spss).

To install Python, go to [Download Python](https://www.python.org/downloads/).

To install DeliberativePolling, run the following in Terminal.

\`\`\`bash
pip install DeliberativePolling
\`\`\`

# In SPSS

To import data into SPSS, open SPSS and navigate to `File`, `Import Data` or simply copy and paste the data directly into the tab `Data View`.

Once the data has been imported into SPSS, you need to provide metadata about the variables in the data.

## Measures

In the "Measure" column of "Variable View", variables can be classified as "Nominal", "Ordinal", or "Scale".

### Nominal

These are categorical variables that do not have an intrinsic order. For example, Gender, where categories like male, female, and non-binary do not have a specific sequence. There may be some exceptions to this rule. For example, some variables like Income Level may have some order to them, so it may be tempting to classify them as Ordinal. In general, that would be a mistake.

### Ordinal

These are categorical variables with a clear, definable order. For example, data derived from a Likert scale ranging from 0 to 10. The values indicate a progression from least to most favorable (or vice versa).

### Scale

Variables not classified as either Nominal or Ordinal are listed under this category. These can be continuous or discrete variables. In order for `outputs()` to identify the different times, experiment groups, and participants in the data, it needs at least three variables classified as "Scale": "ID", "Time", and "Group".

#### Weights

[Explain]

### Variable Identification

- **ID**: A variable indicating individuals within the sample. IDs are necessary because the code compares the responses of individuals at multiple times.
- **Time**: A variable indicating when the responses were given.
- **Group**: A variable indicating what kind of experiment treatment, for example, "Treatment" or "Control".

## Data Cleaning

1. **Column Labels**: Column labels explain the meaning of variables. For example, for the Nominal variable "Education" in Sample.SAV, a good label would be something short but more descriptive like "Highest Education Level".
2. **Value Labels**: Value labels explain the meaning of the values in the variables. For example, the Variable "Age" in Sample.SAV has the values "1", "2", "3", and "4".

> **Note**: Ensure that all values have labels, otherwise the `outputs` function will return an error message explaining which values are unlabeled.

# In Python

Once the data has been cleaned and all metadata has been inputted, the `outputs` function can now be run. If there is missing metadata, then the `outputs` function will return an error and indicate what the missing data is.

In a directory containing the `.SAV` file, run:

\`\`\`bash
Python3
\`\`\`

\`\`\`python
from DeliberativePolling import outputs
outputs("your_file.SAV")
\`\`\`

For example, `outputs("Sample.SAV")`.

## Output

The `outputs` function will create a folder in the directory named "Outputs", which will contain all the outputting Tables and Reports. All tables and reports will be outputted in XLSX format. If the tables and reports are reasonable sized (under 50,000 cells) then they will also be exported in a Word document format.













Purpose: This guide is designed to assist professionals in efficiently leveraging a Python package tailored for the analysis of survey data in Deliberative Polling experiments.

The first step in analyzing a data set of surveys of treatment and control from a Deliberative Polling experiment is to produce tables comparing the responses of these groups before deliberation and after deliberations — and, in some cases, midway through deliberation and follow ups some period of time after the deliberation has concluded.

The function outputs() in this python package takes an SPSS file and outputs comparisons of the responses of all treatment groups at all times with data weighted by all statistical weights provided.

Note: If you are a Stanford affiliate you can likely get SPSS for free at (link) software.stanford.edu.

While the data may be provided to you as an XLSX or CSV file, the function that outputs tables and reports python package requires that the data be an SAV file from IBM SPSS Statistics. As such, you must ensure your data is in an  `.SAV` file format from IBM SPSS Statistics.

Once the data has been imported into SPSS, you need to provide metadata about the variables in the data.

In the "Measure" column of "Variable View", variables can be classified into three kinds of "Measure": "Nominal", "Ordinal", or "Scale".

[Image of measure options]

Nominal Variables: These are categorical variables that do not have an intrinsic order. For exmaple, Gender, where categories like male, female, and non-binary do not have a specific sequence. There may be some exceptions to this rule. For example, some variables like Income Level may have some order to them, so it may be tempting to classiy them as Ordinal. In general, that would be a mistake. This code compares how Ordinal variables change with respect to Nominal variables. For example, how participants in a Deliberative Polling experiment change how they rate our democracy from 0 to 10 (Ordinal) with respect to a demographic variables like income level (Nominal).

Ordinal Variables: These are categorical variables with a clear, definable order. For example, data derived from a Likert scale ranging from 0 to 10. The values indicate a progression from least to most favorable (or vice versa). Again, these are the response variables we are interested in seeing how they change.

Scale Variables: Variables not classified as either Nominal or Ordinal are listed under this category. These can be continuous or discrete variables. In order for outputs() to identify the different times, experiment groups, and participants in the data, it needs at least three variables classified as "Scale": "ID", "Time", and "Group".

"ID" is a variable indicating individuals within the sample. IDs are necessary because the code compares the responses of individuals at multiple times. By matching IDs, it is clear how the invidiuals responses change from say, "Pre-Deliberation" to "Post-Deliberation". IDs need not be numeric. They may also be emails or any other identifying value that is consistent for the same individuals across survey responses.

"Time" is a variable indicating when the responses wre given. For example, a value of "T1" in "Time" would indicate that all the responses in that row were given at T1 (which usually means before deliberation). Whereas, a value of "T2" would indicate that responses were given after T1 (which would generally mean after deliberation). While using values of "T1" or "T2" is common in experimental analysis, you can use more descriptive values like "Pre-Deliberation" and "Post-Deliberation."

"Group" is variable indicating what kind of experiment treatment, for example, "Treatment" or "Control".

[Image of these variables]

CLEAN DATA "10-Strongly disgaree"

Once your variables are properly classified by Measure, you need to label the data. There are two types of labels.

Column Labels: Column labels explain the meaning of variables. Variables in SPSS cannot have spaces or punctuation in them. As such, you need to put full, descriptive labels in to explain the meaning of variables in the "Label" column in "Variable View". For example, for the Nominal variable "Education" in Sample.SAV, a good label would be something short but more descriptive like "Highest Education Level". Keep Nominal variable labels short, as they will go in the file name of ordinal tables. For Ordinal variable labels, you can put full, descriptive labels in. For example, for the Ordinal Variable "Question1" in Sample.SAV, the column label is the question itself: "How well does democracy function?". The length of column labels for ordinal variables is less important than for nominal values as these column labels do not appear in file names, merely cells within XLSX and DOCX files and so can be many characters long.

Value Labels: Value labels explain the meaning of the values in the variables. For example, the Variable "Age" in Sample.SAV has the values "1", "2", "3", and "4". Without prior knowledge of how the data has been coded, these values have no meaning. In the "Values" column in "Variable View", you input value labels to give these codes meaning. In "Age" in Sample.SAV, "1" corresponds to "18-30", "2" corresponds to "30-50", etc. Note that multiple values can share the same label. For example, for Ordinal variable "Question1" values 0 through 4 are labeled as "Poorly" and values "6-10" are labeled as "Well".

Note: Some survey programs label nonresponses like NA or "Don't Know" as 99 or 98. Because the average of Ordinal values are taken by outputs

[Image of age value labels]

Ensure that all values have labels, otherwise the outputs function will return an error message explaining which values are unlabeled.

Note that columns "Width", "Decimals", "Missing", "Columns", "Align" and "Role" in "Variable View" can generally be ignored when preparing the SPSS file for use in outputs().

In the "Type" column of "Variable View", Ordinal and Nominal variables must be set to "Numeric".

The data must be cleaned before use. In order to make all responses in Ordinal and Nominal variables numeric, Nominal values of, for example, "Male" should be recoded into numeric versions like "1" and the appropriate value labels indicating this coding put into the "Values" column in "Variable View". For Ordinal, for example, an entry of "10-Strongly disagree" should be rewritten as "10" in numeric with a value label put in to indicate that "10" is "Strongly Disagree" (or simply "Disagree" along with "9", "8", "7", and "6").

Once the data has been cleaned and all metadata has been inputted, the Outputs function can now be run. If there is missing metadata, then the Outputs function will return an error and indicate what the missing data is.

To run the function, install this Python package to your device by running Python in the terminal or an IDE.

Note: To install Python go to python.org/downloads. To activate Python in a terminal run "Python3".

In a Python terminal, run:
"pip install DeliberativePolling"

\Then in a directory containing the .SAV file run:
"from DeliberativePolling import outputs"
"outputs("your_file.SAV")"
For example, "outputs("Sample.SAV")"

The Outputs function will then creatre a folder in the directory named "Outputs", which will contain all the outputting Tables and Reports.

All tables and reports will be outputted in XLSX format. If the tables and reports are reasonable sized (under 50,000 cells) then they will also be exported in a Word document format.