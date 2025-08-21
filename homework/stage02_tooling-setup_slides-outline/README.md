# Homework 2 – Tooling Setup

This project sets up a clean Python environment and basic structure for data projects.

## Structure

- `data/` – raw and processed data (not pushed)
- `notebooks/` – Jupyter notebooks
- `src/` – source code modules
- `.env` – local environment variables (ignored in git)
- `requirements.txt` – frozen dependencies

## Setup

1. Create and activate environment:

   ```bash
   conda create -n fe-course python=3.11 -y
   conda activate fe-course
   pip install python-dotenv numpy jupyter

   ```

2. Copy .env.example → .env

3. Run the setup notebook: notebooks/00_project_setup.ipynb
