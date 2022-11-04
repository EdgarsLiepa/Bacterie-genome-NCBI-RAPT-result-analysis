## !!! This project is curently under development. Some functions might not work properly

# Description

Create summary from NCBI RAPT pipeline results files.


## **Notebooks**

### **RAPT result analysis File:** 

combineResults.ipynb - parse results files and create summuries 

## Python Scripts

combine.py - create gene product summary in a excel file

**IN:** Result folders from NCBI RAPT pipline with:
- assembly_stat_report.tsv
- annot.gbk
- ani-tax-report.xml

**Out:**
    CSV summary - anotationStat.csv

### Dependencies

- pandas https://pandas.pydata.org/
- BioPython https://biopython.org/