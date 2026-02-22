# Assignment 4 - Version Control with Git for ML Projects
Name: HItanshi  
Roll Number: 1024170327 
Batch: 2q32  

---

## Part 1: Understanding Version Control in ML

### Q1. Why is version control important in ML projects?

Version control is critical in ML projects for several reasons:

1. **Experiment Tracking** – ML development involves running many experiments with different hyperparameters, features, and algorithms. Git lets us tag and revisit any experiment state.
2. **Collaboration** – Multiple team members (data engineers, ML engineers, researchers) work simultaneously. VCS prevents overwriting each other's work.
3. **Reproducibility** – By committing model code and configuration, we can reproduce exact results at any point in time.
4. **Rollback** – If a new model performs worse, we can revert to a previous working version instantly.
5. **Audit Trail** – Every change is documented with who made it, when, and why — important for debugging and compliance.

---

### Q2. What problems occur if Git is not used?

Without Git in an ML project:

1. **Code Conflicts** – Two team members editing the same script overwrite each other's changes with no way to recover lost work.
2. **No Experiment History** – Once you try a new approach, the old approach is gone. There's no way to compare or return to it.
3. **Broken Pipelines** – A bad change to preprocessing can break the entire pipeline with no easy way to identify what changed.
4. **Duplication Chaos** – Teams resort to naming files `model_v1.py`, `model_v2_final.py`, `model_FINAL_ACTUAL.py` — leading to confusion.
5. **No Collaboration** – Without branches, parallel development is impossible, slowing down the entire team.
6. **Deployment Risk** – Without version tags, deploying the wrong model version is easy and hard to detect.

---

### Q3. Why should datasets and trained models be handled carefully in Git?

1. **File Size** – Datasets and model binaries (`.pkl`, `.h5`, `.pt`) can be hundreds of MB or GBs. Git is not designed for large binary files; pushing them bloats the repository and slows cloning.
2. **Git LFS** – Large files should use Git Large File Storage (LFS) or external storage (S3, DVC) while only metadata/pointers are tracked in Git.
3. **Data Privacy** – Raw datasets may contain personally identifiable information (PII). Committing them to a public repo is a serious privacy and legal violation.
4. **Binary Diffs** – Git cannot meaningfully diff binary model files, so storing every retrained model version is wasteful.
5. **Reproducibility via DVC** – Tools like DVC (Data Version Control) are purpose-built to version datasets and models alongside Git commits without the bloat.

**Best Practice:** Track code and configs in Git; track data and models with DVC or cloud storage references.

---

## Part 2: Git Setup and Repository Creation

### Commands Run:

```bash
# Check git version
git --version
# Output: git version 2.x.x

# Configure identity
git config --global user.name "Aditya Kumar"
git config --global user.email "aditya.kumar@example.com"

# Created folder ML_Git_Lab with dataset.csv, model.py, README.md

# Initialize repository
git init

# Check status
git status

# Stage and commit
git add .
git commit -m "Initial commit - ML project structure"
```

---

## Part 3: Working with ML Code Versions

### Steps Performed:

1. Created `model.py` with Linear Regression to predict house prices.
2. Modified `model.py` to add **StandardScaler** feature scaling.
3. Ran `git diff` to inspect changes before committing.
4. Committed the update:

```bash
git add model.py
git commit -m "Added feature scaling"
git log
```

### git log output:
```
279967f Implemented Decision Tree model
25a5d1f Added feature scaling
684886b Initial commit - ML project structure
```

---

## Part 4: Branching for ML Experimentation

```bash
# Create and switch to experimental branch
git branch decision-tree-model
git checkout decision-tree-model

# Modified model.py to use DecisionTreeRegressor instead of LinearRegression
git add .
git commit -m "Implemented Decision Tree model"

# Return to main and merge
git checkout main
git merge decision-tree-model
```

The Decision Tree branch allowed safe experimentation without touching the main working code. After validation, it was merged into `main`.

---

## Part 5: Remote Repository Integration

```bash
# Commands ready to push to GitHub (GitHub repo to be created separately)
git remote add origin https://github.com/<username>/ML_Git_Lab.git
git branch -M main
git push -u origin main
```

*(GitHub repository creation and push to be done separately as per assignment instructions.)*
