# DeliberativePolling Roadmap

Future features and improvements planned for the package.

---

## High Priority

### Database-First Architecture

**Goal:** Refactor to use a database as the primary data storage layer, with Excel outputs serving as a presentation layer that queries the database.

**Benefits:**
- Separation of data processing from presentation
- Enable machine-readable statistical outputs (not just Excel)
- Better support for custom queries and analysis
- Improved performance for large datasets
- Version control of statistical outputs

**Considerations:**
- Database format (SQLite for portability? PostgreSQL for advanced features?)
- Schema design for statistical outputs (means, t-tests, chi-square, crosstabs)
- Migration path for existing workflows
- Export formats: JSON, CSV, Parquet for machine-readable outputs

---

## Medium Priority

### Configuration System

**Goal:** Provide configuration options beyond SPSS metadata for analysis parameters.

**Current Issue:** Attaching all analysis logic to SPSS metadata is smart but unconventional. It forces users to modify datasets and maintain separate versions for different analyses.

**Potential Solutions:**
- YAML/JSON config files for analysis parameters
- Python API for programmatic configuration
- CLI arguments for common overrides
- Hybrid approach: SPSS metadata as defaults, config file for overrides

**Config Examples:**
```yaml
variables:
  weight: 
    - column: "post_weight"
      label: "Post-Deliberation Weight"
  groups:
    treatment: ["Treatment", "Experimental"]
    control: ["Control"]
  ignore:
    - "timestamp"
    - "ip_address"
```

---

### Excel Output Formatting Improvements

**Goal:** Make statistical outputs clearer in Excel files.

**Current Issue:** Rows with variable names and labels contain means and paired t-test results, but have no label identifying them as such. This can be confusing.

**Proposed Changes:**
- Add explicit column headers: "Mean", "Paired t-test p-value", "Chi-square p-value"
- Consider separate sheets for different test types
- Add color coding or formatting to highlight significant results
- Include metadata sheet with analysis parameters

---

### Standardized Ordering

**Goal:** Ensure consistent, predictable ordering of elements in folder names, file names, and output tables.

**Current Issue:** 
- Folder/file names sometimes appear as "Parents vs Teachers" or "Teachers vs Parents" (possibly alphabetical or data order)
- Worst case: "Post vs Pre" instead of "Pre vs Post"
- Inconsistent with value label ordering used for column headers

**Proposed Solution:**
- Use SPSS value label ordering (numeric code order) for all naming elements
- Apply same ordering to:
  - Folder names
  - File names
  - Column headers in crosstabs
  - Table row order
- Document the ordering logic clearly in README

---

## Long-Term / Research Needed

### Statistical Output Framework

**Goal:** Create a flexible framework for storing diverse statistical test outputs, especially for database-first architecture.

**Challenges:**
- Different tests have different output structures
  - Chi-square: statistic, df, p-value
  - t-test: t-statistic, df, p-value, mean difference, CI
  - Crosstabs: multi-dimensional tables with percentages
  - Regression: coefficients, SEs, multiple p-values
- How to represent in database schema?
- How to export to different formats (Excel, JSON, CSV)?

**Research Areas:**
- Survey existing statistical software output formats
- Explore schema-less solutions (JSONB in PostgreSQL)
- Look into statistical result object standards (e.g., R's broom package)

---

### R Rewrite for Survey Design Support

**Goal:** Rewrite package in R to leverage mature survey analysis ecosystem.

**Motivation:**
- Better support for complex survey designs
- Proper statistical handling of survey weights
- Access to R survey packages: `survey`, `srvyr`, `lavaan.survey`
- Design effect calculations
- Variance estimation for complex designs (stratification, clustering)

**Considerations:**
- Maintain compatibility with current `.sav` workflow
- Python wrapper for existing users?
- Which R packages to build on: `survey`, `tidyverse`, `haven`
- Performance implications

---

### Multiple Testing Correction

**Goal:** Add support for p-value adjustments when running many statistical tests.

**Current Issue:** 
- Package runs many statistical tests (hundreds or thousands depending on data)
- All p-values are currently unadjusted
- Risk of false positives (Type I error inflation) with many comparisons

**Questions to Resolve:**
1. **Scope:** What should be considered a "family" of tests for correction?
   - All tests in entire analysis?
   - Tests within each nominal category slice?
   - Tests for each ordinal variable?
   - User-defined scope?

2. **Method:** Which correction to use?
   - Bonferroni (conservative, simple)
   - Holm-Bonferroni (less conservative)
   - Benjamini-Hochberg FDR (controls false discovery rate)
   - User choice?

3. **Reporting:** How to present corrected results?
   - Replace original p-values?
   - Report both adjusted and unadjusted?
   - Flag significant results after correction?

**Proposed Approach:**
- Add `correction` parameter: `"none"` (default), `"bonferroni"`, `"holm"`, `"fdr"`
- Add `correction_scope` parameter: `"global"`, `"nominal_category"`, `"variable"`
- Report both adjusted and unadjusted p-values in Excel
- Add visual indicators (highlighting) for significant results post-correction

---

## Contributing Ideas

Have ideas for features or improvements? We'd love to hear them!

- 🐛 **Bug reports:** [Open an issue](https://github.com/stanford-ddl/DeliberativePolling/issues)
- 💡 **Feature requests:** [Start a discussion](https://github.com/stanford-ddl/DeliberativePolling/discussions)
- 💬 **Questions:** Contact deliberation@stanford.edu
