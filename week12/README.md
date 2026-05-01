# Week 12: Optimize II – LLMs for Decision Support & Automation

## 📚 Overview

This week you'll take automation further by adding AI intelligence to your workflows. You'll learn the key vocabulary around Large Language Models (tokens, models, APIs, MCP), run models locally using Ollama, and build no-code automation pipelines with tools like n8n and Zapier. You'll also connect LLMs to real data using DuckDB and MotherDuck so non-technical staff can query databases in plain English.

## 🎯 Learning Objectives

By the end of this week, you will be able to:

- Explain key LLM vocabulary: models, tokens, APIs, MCP
- Run open-source LLMs locally using Ollama (free, private, offline)
- Write effective prompts for structured data tasks
- Connect LLMs to databases via MCP for natural language queries
- Ingest CSV data into DuckDB and query it with plain English
- Design automation workflows using n8n or Zapier

## 🎓 Session Resources

- Lecture: [LLMs for Decision Support & Automation](https://docs.google.com/presentation/d/1ISZLdX3NGXf1uMiqEaGd3hlMb5hrRwovwxOmRV0yd-k/edit?usp=sharing)
- Tutorial: [DuckDB + MCP Natural Language Queries](notebooks/tutorial_duckdb_mcp.ipynb)

## 🏗️ Mini-Deliverable

**Assignment:** Design and prototype an LLM-powered automation workflow for an NGO or social good use case.

**Requirements:**
1. **Choose a repetitive task** at an NGO that currently takes significant manual effort (e.g., grant screening, donor communications, volunteer matching)
2. **Design the workflow:**
   - Trigger (what starts it)
   - LLM task (what intelligence is added)
   - Connected tools (database, email, calendar, etc.)
   - Output (what is produced)
3. **Write 2–3 effective prompts** for your LLM task
4. **Run a local demo** using Ollama + DuckDB (use the lab notebook as a starting point)

**Example Ideas:**
- Grant eligibility screener: LLM reads grant description, scores fit vs. mission
- Donor thank-you generator: LLM writes personalized letters from donation records
- Volunteer matcher: LLM recommends best roles based on applicant skills
- Event feedback summariser: LLM distils exit survey responses into action points

**Bonus:**
- Build the workflow in n8n or Zapier
- Add a cost estimate (tokens × price) if using an API model
- Deploy a simple Streamlit interface on top of your DuckDB queries


---
---

**Next Week**: [Week 13: TBD](../week12/README.md)

**Previous Week**: [Week 11: Optimize I – Automating Analysis with Functions & Pipelines](../week11/README.md)
