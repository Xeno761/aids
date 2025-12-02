# 📘 Data Mining & Warehousing – Complete Practical Notes (1–6)

This document provides **in‑depth AIM, THEORY, SOFTWARE REQUIREMENTS, ALGORITHM, and CONCLUSION** for Practicals 1–6.  
All explanations are written based on the **exact code you provided** and aligned with **DMW syllabus standards**.

---

# ✅ **PRACTICAL 1 – DATA CLEANING & INTEGRATION**

## **Aim**
To clean, preprocess, and integrate multi‑source retail data (Village A & Village B) derived from the Kaggle *Supermarket Sales* dataset by handling missing values, removing duplicate records, standardizing selected fields, and merging datasets into a unified table ready for mining.

## **Software Requirements**
- Python 3.8+
- Jupyter Notebook / VS Code / Google Colab  
- Libraries:
  - `pandas`
  - `numpy`
- Dataset:
  - *Supermarket Sales* – Kaggle

## **Theory**
Data cleaning and integration are the **first and most important** steps in the data mining process. Real‑world data often contains:
- Missing values  
- Inconsistent formatting  
- Duplicate records  
- Noisy or incorrect values  

### **Key Cleaning Operations**
1. **Missing Value Treatment**  
   - Numeric data uses *mean* imputation:  
     
\( 	ext{new value} = 	ext{mean of available values} \)
2. **Duplicate Removal**  
   Ensures no redundant rows appear in the dataset.
3. **Renaming and Standardizing Columns**  
   Converts dataset columns (Branch, Product line, Unit price) into meaningful mining attributes.
4. **Data Integration**  
   Merges separate subsets:  
   - Village A → Branch A  
   - Village B → Branch B  
   using row-wise concatenation.

### **Why Integration?**
Integrated datasets provide:
- Larger sample size  
- Better patterns  
- Unified mining structure  

## **Algorithm**
1. Import `pandas` and `numpy`  
2. Load dataset using `read_csv()`  
3. Select necessary attributes  
4. Rename columns to standard names  
5. Filter dataset into Village A (branch A), Village B (branch B)  
6. Handle missing values using mean imputation  
7. Remove duplicates using `drop_duplicates()`  
8. Merge both datasets using `concat()`  
9. Save clean dataset to CSV  

## **Conclusion**
Data was successfully cleaned and integrated. Missing values were replaced, duplicates removed, and the merged dataset is now consistent, complete, and ready for further mining techniques.

---

# ✅ **PRACTICAL 2 – DESCRIPTIVE STATISTICS**

## **Aim**
To compute and interpret essential descriptive statistics such as mean, median, mode, variance, standard deviation, quartiles, and range for understanding distributions in numeric datasets.

## **Software Requirements**
- Python 3.8+
- Libraries:  
  - `pandas`
  - `scipy` (optional)

## **Theory**
Descriptive statistics summarize and explore dataset behavior. They are essential before applying machine learning.

### **Measures of Central Tendency**
- **Mean** – average value  
- **Median** – middle value  
- **Mode** – most frequent value  

### **Measures of Dispersion**
- **Variance** – spread of values  
  
\( \sigma^2 = rac{\sum (x - ar{x})^2}{n - 1} \)
- **Standard Deviation** – square root of variance  
- **Range** – max − min  
- **Quartiles (Q1, Q2, Q3)** – divide data into four equal partitions  

### **Why Important?**
They allow understanding:
- Distribution spread  
- Skewness  
- Outliers  
- Variability  

## **Algorithm**
1. Load numeric series (example: Price)  
2. Compute: mean, median, mode  
3. Compute variance, standard deviation  
4. Determine quartiles Q1, Q2, Q3  
5. Compute range  
6. Display results  

## **Conclusion**
All descriptive measures were calculated, enabling a deeper understanding of distribution shape and variability of the Price attribute.

---

# ✅ **PRACTICAL 3 – DATA TRANSFORMATION**

## **Aim**
To perform data scaling and discretization using normalization, standardization, equal‑width binning, and equal‑frequency binning techniques.

## **Software Requirements**
- Python 3.8+
- Libraries:  
  - `pandas`
  - `numpy`
  - `scikit-learn`

## **Theory**
Data transformation re-scales or reorganizes data to improve the performance of mining algorithms.

### **1. Normalization (Min‑Max)**
Scales values between 0 and 1:  
\[
x' = rac{x - x_{min}}{x_{max} - x_{min}}
\]

### **2. Standardization (Z‑Score)**
Rescales distribution to mean 0, standard deviation 1:  
\[
z = rac{x - \mu}{\sigma}
\]

### **3. Equal-Width Binning**
Divides numeric values into bins of equal range.

### **4. Equal-Frequency Binning**
Each bin has the same number of values.

### **Why Transform Data?**
- Reduces outlier impact  
- Improves accuracy of algorithms (e.g., KNN, clustering)  
- Makes attributes comparable  

## **Algorithm**
1. Load dataset  
2. Apply Min‑Max normalization  
3. Apply Z‑score standardization  
4. Apply equal‑width binning  
5. Apply equal‑frequency binning  
6. Display every transformed version  

## **Conclusion**
Normalization, standardization, and binning were successfully applied. These transformed datasets are now more suitable for machine learning algorithms.

---

# ✅ **PRACTICAL 4 – ASSOCIATION RULE MINING (APRIORI)**

## **Aim**
To identify frequent itemsets and generate association rules using Apriori on the Iris dataset after discretizing its numeric attributes.

## **Software Requirements**
- Python 3.8+
- Libraries:  
  - `pandas`
  - `mlxtend`
  - `scikit-learn`

## **Theory**
Apriori discovers meaningful relationships in large datasets.

### **Key Concepts**
- **Support**: how often an itemset appears  
- **Confidence**: likelihood that Y occurs when X occurs  
- **Lift**: strength of association  
  - Lift > 1 → strong positive correlation  

### **Process**
1. Numerical data → discretized into Low/Medium/High using `qcut()`  
2. One-hot encoding prepares dataset for Apriori  
3. Apriori generates frequent itemsets  
4. Rules extracted using confidence and lift  

### **Why Iris Dataset Works**
Though not transactional, discretization allows conversion into categorical form suitable for Apriori.

## **Algorithm**
1. Load Iris dataset  
2. Discretize numeric columns  
3. Apply one‑hot encoding  
4. Generate frequent itemsets using Apriori  
5. Generate rules using min confidence  
6. Display results  

## **Conclusion**
Apriori successfully identified strong associations between attribute ranges within Iris species. Generated rules show patterns useful for classification and pattern recognition.

---

# ✅ **PRACTICAL 5 – CLASSIFICATION (Decision Tree vs Naive Bayes)**

## **Aim**
To build and compare classification models using Decision Tree and Gaussian Naive Bayes on the Iris dataset.

## **Software Requirements**
- Python 3.8+
- Libraries:  
  - `pandas`
  - `scikit-learn`

## **Theory**
### **Decision Tree**
- Hierarchical model  
- Splits data using information gain / Gini impurity  
- Handles nonlinear patterns well  

### **Naive Bayes**
- Probability-based  
- Assumes feature independence  
- Requires less training time  

### **Evaluation Metrics**
- Accuracy  
- Confusion Matrix  
- Precision  
- Recall  
- F1‑Score  

## **Algorithm**
1. Load Iris dataset  
2. Split into train/test (70/30)  
3. Train Decision Tree  
4. Train Gaussian Naive Bayes  
5. Predict for both models  
6. Evaluate using accuracy & metrics  
7. Compare models  

## **Conclusion**
Decision Tree achieved higher accuracy than Naive Bayes for the Iris dataset. Both algorithms performed well, validating them as strong classification tools.

---

# ✅ **PRACTICAL 6 – CLUSTERING (K-Means & DBSCAN)**

## **Aim**
To apply K-Means and DBSCAN clustering on standardized synthetic blob data to visually analyze clustering behavior.

## **Software Requirements**
- Python 3.8+
- Libraries:  
  - `numpy`
  - `matplotlib`
  - `scikit-learn`

## **Theory**
### **K-Means**
- Centroid‑based  
- Requires specifying number of clusters  
- Minimizes within-cluster sum of squares (WCSS)

### **DBSCAN**
- Density-based  
- Groups points within `eps` radius  
- Identifies noise/outliers  
- Does not require number of clusters  

### **Key Differences**
| Feature | K-Means | DBSCAN |
|--------|---------|--------|
| Need k? | Yes | No |
| Handles noise? | Poorly | Excellent |
| Cluster shape | Spherical | Arbitrary |

## **Algorithm**
1. Generate synthetic data  
2. Standardize using StandardScaler  
3. Apply K-Means  
4. Apply DBSCAN  
5. Count clusters & noise  
6. Plot results  

## **Conclusion**
K-Means grouped well-separated clusters effectively, while DBSCAN identified noise points and clusters of varying density. Both algorithms complement each other depending on dataset characteristics.

---

# ✅ END OF NOTES

This file contains deep explanations aligned with your code and academic requirements.

