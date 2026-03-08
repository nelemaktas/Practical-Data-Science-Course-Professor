# Week 6: Working with External Data & APIs

## 📚 Overview

Practical week focused on fetching and integrating external data via public APIs and remote datasets. Exercises emphasize safe requests, JSON normalization, caching, and merging API data with local files for analysis.

## 🎯 Learning Objectives

By the end of this week you will be able to:

- Explain REST API basics and common formats (JSON, CSV)
- Implement safe API requests with retries and timeouts
- Normalize nested JSON into pandas DataFrames
- Cache and persist API responses during development
- Merge external metadata with local datasets and document provenance

## 🎓 Session Resources

- Lecture: [Working with External Data & APIs](https://docs.google.com/presentation/d/1oeIQs-J0VXUy-q47VLeAYVMNk4Ae69iWFZPsh5oDBqQ/edit?slide=id.g230b312f0cd_0_28#slide=id.g230b312f0cd_0_28)
- Tutorial: [Working with External Data & APIs](notebooks/tutorial_apis.ipynb)

## 🏁 Mini-Deliverable

Create a reproducible notebook that:

1. Implements a `safe_request` helper with retries and timeouts
2. Fetches and caches API responses (or saves raw JSON locally)
3. Normalizes JSON to a DataFrame and documents transformation steps
4. Joins the API data with a local dataset in this repo and shows a short analysis

---

**Previous Week**: [Week 5: Organizing Projects with GitHub + AI Helpers](../week5/README.md)
**Next Week**: [Week 7: Inform I: Describing the Current State with Data](../week7/README.md)
