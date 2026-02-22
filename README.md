# ML_Git_Lab - House Price Prediction

Name:Hitanshi
**Roll Number:** 1024170327 
**Batch:** 2q32  
**Assignment:** Assignment 4 - Version Control with Git for ML Projects

---

## Project Overview

This project demonstrates the use of Git version control in a Machine Learning workflow. The goal is to predict house prices using various ML models.

## Dataset

The dataset (`dataset.csv`) contains 30 house records with the following features:
- `area_sqft` – Area of the house in square feet
- `bedrooms` – Number of bedrooms
- `bathrooms` – Number of bathrooms
- `age_years` – Age of the house in years
- `garage` – Number of garage spaces
- `neighborhood_score` – Neighborhood quality score (1–10)
- `price` – Target variable (house price in USD)

## Project Structure

```
ML_Git_Lab/
├── dataset.csv      # House price dataset
├── model.py         # ML model script
└── README.md        # Project documentation
```

## Models Used

1. **Linear Regression** (main branch) – Baseline model with feature scaling
2. **Decision Tree** (decision-tree-model branch) – Experimental alternative model

## How to Run

```bash
pip install pandas scikit-learn numpy
python model.py
```

## Git Workflow

- `main` branch: Production-ready Linear Regression model with feature scaling
- `decision-tree-model` branch: Decision Tree experimentation (merged into main)

## Team Roles (Simulated)
- Member A → Data Preprocessing
- Mem
ber B → Feature Engineering  
- Member C → Model Training
"# AI-Lab-Assignment-4" 
