# DeliberativePolling

**Statistical analysis toolkit for Deliberative Polling experiments**

[![Python Version](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)

## What is this?

DeliberativePolling automates statistical analysis of survey data from Deliberative Polling experiments. It generates comprehensive comparison tables and reports across treatment groups, waves, and statistical weights.

**Input:** `.sav` files with survey data (from Jamovi, SPSS, or other compatible software)  
**Output:** Statistical tables (`.xlsx`) and reports (`.docx`)

Developed by the [Stanford Deliberative Democracy Lab](https://ddl.stanford.edu/).

---

## Quick Start

```bash
# Install
pip install git+https://github.com/stanford-ddl/DeliberativePolling.git

# Run analysis
python3
>>> from DeliberativePolling import outputs
>>> outputs("your_data.sav")
```

Done! Check the `Outputs/` folder for results.

---

## Features

- ✅ Automated statistical comparisons (χ² tests, t-tests)
- ✅ Handles nominal and ordinal variables based on SPSS metadata
- ✅ Multiple waves (pre/post, T1/T2/T3, etc.)
- ✅ Treatment vs control group comparisons
- ✅ Generates tables for every combination of nominal variable and weight
- ✅ Uses SPSS value labels and column labels for organization and output

---

## How It Works

The package reads SPSS metadata (variable measures, value labels, column labels) to:

1. **Identify variable types:** Uses "Measure" settings (`Nominal`, `Ordinal`, `Scale`)
2. **Slice by nominal variables:** Creates separate output folders/files for each nominal variable
3. **Generate crosstabs:** For each ordinal variable, creates crosstabs sliced by each nominal variable
4. **Apply weights:** Produces separate analyses for each weight variable (unweighted + any columns with "weight" in the name)

**Key insight:** The package treats ordinal variables as the primary data to analyze, and slices them across all combinations of nominal variables. This means you get detailed breakdowns like "How did opinions on democracy (ordinal) differ by education level (nominal) between waves?"

---

## Installation

### Requirements
- Python 3.11+
- macOS or Linux recommended (Windows may require additional setup for pyreadstat)

### Install from GitHub

The PyPI package is outdated and orphaned. Install directly from this GitHub repository instead.

```bash
pip install git+https://github.com/stanford-ddl/DeliberativePolling.git
```

### Install for Development

```bash
git clone https://github.com/stanford-ddl/DeliberativePolling.git
cd DeliberativePolling
pip install -e .
```

---

## Usage

### 1. Prepare Your SPSS File

Your `.sav` file must contain three essential variables:

| Variable | Description | Example Values |
|----------|-------------|----------------|
| `ID` | Unique identifier for each person within each wave | 1, 2, 3... or email addresses |
| `Group` | Treatment or control group | "Treatment", "Control" |
| `Time` | Measurement wave/time point | "T1", "T2", "Pre", "Post" |

**Important:** Your data should be in **long format** with one row per person per wave. The `Time` variable indicates which wave each row represents. Each participant will appear multiple times (once per wave they participated in). The `ID` should uniquely identify each person - duplicate IDs within the same `Group` and `Time` combination will cause an error.

**See [Data Preparation Guide](#data-preparation) below for detailed setup instructions.**

### 2. Run Analysis

```python
from DeliberativePolling import outputs

# Basic usage
outputs("my_data.sav")

# Fast mode (Excel only, skips Word docs)
outputs("my_data.sav", fast=True)
```

### 3. View Results

Results are saved in `Outputs/` directory:
```
Outputs/
├── T1 v. T2/
│   ├── Treatment at T1 v. T2/
│   │   ├── Education Level/
│   │   │   ├── Tables - Ordinal Variables - ...xlsx
│   │   │   └── Report - Ordinal Variables - ...docx
```

**Note on Duplicate Tables:** If a nominal variable has different values between waves (e.g., a demographic variable changed or has missing data in one wave), you may see multiple Tables files with wave/time labels like `Tables - Ordinal Variables - T1 - ...xlsx` and `Tables - Ordinal Variables - T2 - ...xlsx`. For fixed demographic variables (like education, gender, etc.), use the earliest wave's file. If you see differing data between waves for what should be a fixed variable, investigate why the discrepancy exists.

---

## Recent Updates

### v1.4.3 (Apr 2026) - Packaging Cleanup

Modernized packaging with `pyproject.toml`, bumped the release version, and simplified dependency metadata.

### v1.4.2 (Nov 2024) - Crosstab NaN Handling Fix

Fixed critical issue where crosstabs would fail when nominal categories had missing values that differed across waves.

**Problem:** Index errors and inconsistent tables when categories existed in one wave but not another (e.g., a nominal category present in T1 but all NaN in T2).

**Solution:** 
- Now uses all category labels from SPSS metadata (not just values present in data)
- Adds proper bounds checking in crosstab calculations
- Shows missing categories explicitly as 0% rather than omitting them
- Ensures consistent table structure across all comparisons

[View detailed fix →](https://github.com/stanford-ddl/DeliberativePolling/tree/fix/nominal-crosstab-nan)

---

## Data Preparation

### Installing Software

The package works with `.sav` files, which can be created by several tools:

- **Jamovi (Recommended, Free & Open Source):** [jamovi.org](https://www.jamovi.org/) - Cross-platform statistical software with excellent SPSS compatibility
- **SPSS Statistics:**
  - **Stanford affiliates:** [Software at Stanford](https://stanford.onthehub.com/WebStore/ProductsByMajorVersionList.aspx?cmi_mnuMain_child=883de5b3-9f82-de11-8cd1-0030487d8897&cmi_mnuMain=0b57b739-b182-de11-8cd1-0030487d8897)
  - **Others:** [IBM SPSS Software](https://www.ibm.com/spss)

The instructions below use terminology common to both Jamovi and SPSS. Screenshots and specific menu paths may differ slightly between software.

### SPSS File Setup

To import data, open your statistical software and navigate to the import data function (e.g., `File` → `Import Data` in SPSS).

#### Essential Variables

The `.sav` file must contain three variables: `ID`, `Time`, and `Group`. If not already present, you will need to create these variables.

**ID**

A unique identifier for each person. This can be a number, an email address, or any other unique value. Each participant should have the same ID across all waves they participated in.

**Note:** The package checks for duplicate IDs within each (`Group`, `Time`) combination. If you have the same person appearing twice in the same group at the same time point, you'll get an error asking you to fix the duplicates.

**Group**

Indicates which experimental condition a participant is in—either the `Treatment` group (receives the intervention) or the `Control` group (does not). This enables comparison of treatment effects.

**Time**

Shows which wave or measurement period each row represents. You can use any labels: "T1", "T2", "Pre", "Post", "Pre-Deliberation", "Post-Deliberation", etc. Each participant should appear once per wave (one row per wave).

**Data Structure:** Your data must be in **long format** - one row per person per wave. For example, if you surveyed 100 people at 2 waves, you should have 200 rows (assuming no attrition). The `Time` variable differentiates which wave each row represents. Wide format (one row per person with separate columns for T1 and T2 responses) will not work.

*Note: The package runs comparisons for every `Group` at every `Time` (wave) for every weight. Keep the number of groups, waves, and weights reasonable to ensure manageable runtime.*

#### Optional Variables

**Weights**

By default, the package generates unweighted tables. You can add weighting by including columns with `weight` in the header (e.g., `Weight1`, `post_weight`). These weight variables must be numeric with their `Measure` set to `Scale`. The package will automatically generate separate analyses for each weight it finds.

**Ignored Variables**

To keep variables in your file that you don't want included in analysis but might use later, set their `Measure` to `Scale` (unless they're weight variables). Examples: timestamps, IP addresses, device info. Generally include in analysis: opinion questions, demographic questions, evaluation questions.

#### Measures (Variable Types)

In the `Measure` column of Variable View, variables can be classified as `Nominal`, `Ordinal`, or `Scale`. **This setting is critical** - the package uses it to determine how to analyze each variable.

**Nominal Variables**

Nominal variables are categorical variables without a sequential order. Examples: `Employment` (Employed, Unemployed, Student, Other), `Gender`, `Region`. 

The package uses nominal variables to **slice** the data - it creates separate output folders and crosstabs for each nominal variable. Generally advisable (but not mandatory) to categorize demographic variables as `Nominal`.

**⚠️ Label tip:** Nominal variable labels appear in folder/file names. Avoid using `/` slashes in labels or the software will try to create nested folders and cause errors!

**Ordinal Variables**

Ordinal variables are categorical variables with a well-defined order. Examples: Likert scales (0-10, 1-5), agreement scales (Strongly Disagree → Strongly Agree), frequency scales (Never → Always).

The package treats ordinal variables as the **primary data to analyze**. It creates crosstabs showing how ordinal responses differ across nominal categories and waves. Means are calculated for ordinal variables. Typically used for: opinion questions, evaluation questions, knowledge questions.

**⚠️ Nonresponse codes:** The package automatically converts user-defined missing values (marked as missing in your statistical software) to NaN and excludes them from mean calculations. However, if you use numeric codes like `-1`, `77`, `98`, or `99` for non-response but **don't mark them as missing values** in your software's missing value settings, they will be treated as real data. This would severely distort means (e.g., a `99` on a 1-5 scale). Either mark these codes as missing values in your software, or replace them with blank cells before analysis.

**Scale Variables**

Variables that don't fit into `Nominal` or `Ordinal` categories should be classified as `Scale`. The package **ignores** Scale variables unless they're weight variables (contain "weight" in the name). All weight variables must be `Scale`.

#### Labels

Labels help clarify the meaning of variable names and values. The package uses these labels extensively for organizing outputs.

**Column Labels**

Variable names can't have spaces or punctuation. Set descriptive column labels (e.g., the `Label` field in SPSS Variable View or the variable label/property in Jamovi/R) so outputs are readable.

- **Nominal Variables**: Use concise labels. Example: variable `Education` → label `Education Level`. These labels appear in **folder and file names**, so keep them short and avoid special characters (especially `/` slashes).

- **Ordinal Variables**: Use fuller, descriptive labels. Example: variable `Question1` → label `How well does democracy function?`. These labels appear **inside tables**, not in filenames, so length doesn't matter.

**Value Labels**

For many software packages it's common to store categorical (ordinal/nominal) variables as numeric codes and attach human-readable value labels. Make sure your ordinal and nominal variables have value labels that map each numeric code to a label (e.g., `1` = "18-30", `2` = "30-50"). In SPSS this is the `Values` column in Variable View; in Jamovi or R you can set labels via the variable properties or label functions.

**Shared Labels:** Multiple numeric codes can have the same label. When calculating percentages for crosstabs, responses with the same label are grouped together. For instance, in a 0-10 scale question, codes `0-4` might all be labeled "Poorly" while `6-10` are labeled "Well" - the percentages would show the combined percentage for each label group. Note that paired t-tests use the underlying numeric values, not the grouped labels.

**⚠️ Important:** Ensure that **all values** in nominal and ordinal variables have labels. The `outputs` function will return an error if it finds unlabeled values, telling you exactly which ones are missing. Don't add labels to Scale variables.

---

## Running the Analysis

Once you've set up your `.sav` file with the required variables and labels:

1. Open a terminal in the directory containing your `.sav` file
2. Run Python and execute the analysis:

```bash
python3
>>> from DeliberativePolling import outputs
>>> outputs("your_file.sav")
```

### Output Files

A new `Outputs/` folder will be created containing all generated tables and reports in `.xlsx` and `.docx` format.

**Fast Mode:** Generating Word `.docx` files significantly slows down execution. To speed up analysis, generate only Excel files:

```python
outputs("your_file.sav", fast=True)
```

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `ValueError: "ID" variable not found` | Your `.sav` file must have variables named exactly `ID`, `Group`, and `Time` (case-sensitive) |
| `ValueError: Value labels for [...] not found` | All values in nominal and ordinal variables must have labels. The error tells you which values are missing labels. |
| `Error creating folders/files` | Check that nominal variable labels don't contain `/` slashes or other special characters that can't be used in file names |
| `IndexError` or inconsistent tables | This was fixed in v1.4.2. Reinstall from GitHub to get the latest version: `pip install --upgrade git+https://github.com/stanford-ddl/DeliberativePolling.git` |
| Package runs very slowly | Use `fast=True` to skip Word document generation, which significantly speeds up execution |
| Installation issues on Windows | The `pyreadstat` dependency may require additional compilation steps on Windows. See [pyreadstat Windows guide](https://github.com/Roche/pyreadstat/blob/master/windows_compilation.md) |

---

## Development

### Installing for Local Development

To make changes to the package code and test them without reinstalling:

```bash
# Clone the repository
git clone https://github.com/stanford-ddl/DeliberativePolling.git
cd DeliberativePolling

# Create virtual environment (recommended)
python3 -m venv env
source env/bin/activate  # On macOS/Linux

# Install in editable mode
pip install -e .
```

The `-e` flag installs in "editable" mode - changes to source files take effect immediately without reinstalling.

### Branch Naming Conventions

- `fix/` - Bug fixes (e.g., `fix/nominal-crosstab-nan`)
- `feature/` - New functionality (e.g., `feature/db-export`)
- `refactor/` - Code cleanup
- `docs/` - Documentation updates

### Making Contributions

1. Create a branch from `main`:
   ```bash
   git checkout -b fix/your-fix-name
   ```

2. Make changes and test locally

3. Commit with clear messages:
   ```bash
   git commit -m "Fix: Brief description
   
   - Detailed explanation
   - What the problem was
   - How you solved it"
   ```

4. Push and create a Pull Request on GitHub

---

## Support

- 🐛 **Bug reports:** [Open an issue](https://github.com/stanford-ddl/DeliberativePolling/issues)
- 💬 **Questions:** Contact deliberation@stanford.edu
- 📖 **Example data:** See [Sample.sav](Sample.sav) for a properly formatted `.sav` file

---

## About

Developed by the [Stanford Deliberative Democracy Lab](https://ddl.stanford.edu/).

The lab studies how ordinary citizens can make informed decisions about complex policy issues through structured deliberation.
