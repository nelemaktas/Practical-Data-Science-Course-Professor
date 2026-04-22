# Week 11: Optimize I – Automating Analysis with Functions & Pipelines

## 📚 Overview

This week you'll learn how to automate repetitive data analysis tasks by building reusable functions and creating data pipelines. Instead of writing similar code over and over, you'll structure your work modularly for efficiency, maintainability, and scalability. This foundation speeds up analysis and reduces errors.

## 🎯 Learning Objectives

By the end of this week, you will be able to:

- Write reusable functions to avoid code duplication
- Create data processing pipelines for efficient workflows
- Use Streamlit and Marimo to quickly build interactive data apps
- Organize code for readability and maintenance
- Automate repetitive analysis tasks
- Deploy simple web applications without complex backend setup

## 🎓 Session Resources

- Lecture: [Automate & Optimize: Functions, Pipelines & Streamlit](https://docs.google.com/presentation/d/1UfKC5MSrujtCE41y15FYod7NNNb3HDNo-Ud5FghHX5o/edit?usp=sharing)
- Tutorial: [Streamlit Basics for Data Apps](notebooks/tutorial_streamlit_basics.ipynb)


## 🏗️ Mini-Deliverable

**Assignment:** Create a reusable data analysis workflow with functions and a simple Streamlit app.

**Requirements:**
1. **Build at least 3 reusable functions:**
   - Data loading/cleaning function
   - Analysis/calculation function
   - Visualization function
2. **Create a simple data pipeline** that chains these functions
3. **Build a Streamlit app** that:
   - Takes user input (file upload, parameter selection)
   - Runs your pipeline
   - Displays results and visualizations
4. **Document your code:**
   - Clear function names and docstrings
   - Comments explaining pipeline steps
   - README with usage instructions

**Example Ideas:**
- CSV analyzer: Upload any CSV, auto-generate summary statistics and plots
- Data quality checker: Identify missing values, outliers, data type issues
- Quick dashboard: Load data, select metrics to display in interactive table
- Batch processor: Process multiple files using same functions

**Bonus:**
- Add error handling (what if file is missing or invalid?)
- Add logging to track what your pipeline does
- Deploy your Streamlit app publicly on Streamlit Cloud

---

**Next Week**: [Week 12: Optimize II: LLMs for Decision Support & Automation](../week12/README.md)

**Previous Week**: [Week 10: Guide II – Interpreting Predictions & Understanding Limits](../week10/README.md)
