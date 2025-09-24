
# Privacy-Preserving Synthetic Tabular Data Generator

## Project Description
The **Privacy-Preserving Synthetic Tabular Data Generator** is a Python-based library designed to generate synthetic tabular data while ensuring privacy. This tool uses advanced machine learning algorithms to learn the patterns of real-world data and generate synthetic data that mimics these patterns. It is useful for situations where real-world data cannot be shared due to privacy concerns but synthetic data is needed for testing or training purposes.

### Key Features:
- **Tabular Data Generation**: Create synthetic data for single or multiple related tables.
- **Privacy Preservation**: Ensures that the generated data does not leak sensitive or personal information.
- **Evaluation**: Provides tools for evaluating the quality of synthetic data.
- **Anonymization and Constraints**: Allows data to be anonymized and apply logical constraints to improve data quality.

## Project Requirements

1. **Python 3.8+**  
   Install Python from [python.org](https://www.python.org/).

2. **Required Libraries**  
   Install the dependencies using:
   ```bash
   pip install -r requirements.txt
````

3. **Additional Tools**:

   * Ensure you have **Git** installed for version control.
   * You may also need **Jupyter Notebook** for running tutorials or experiments.

## How to Run the Project Locally

### Step 1: Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/NMANISH9800/Privacy-Preserving-Synthetic-Tabular-Data-Generator.git
cd Privacy-Preserving-Synthetic-Tabular-Data-Generator
```

### Step 2: Set Up the Virtual Environment

Create and activate a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

* **Windows**:

  ```bash
  venv\Scripts\activate
  ```
* **macOS/Linux**:

  ```bash
  source venv/bin/activate
  ```

### Step 3: Install Dependencies

Install all the necessary dependencies:

```bash
pip install -r requirements.txt
```

### Step 4: Generate Synthetic Data

Run the generator to create synthetic data from real data:

```bash
python generate_synthetic_data.py
```

This will generate synthetic data based on the configuration set in the script.

### Step 5: Evaluate the Results

After generating the synthetic data, use the provided evaluation functions to compare it with real data:

```bash
python evaluate_synthetic_data.py
```

### Step 6: Modify the Experiment

You can adjust the script settings and experiment with different data types, algorithms, and parameters as needed.

---

## Conclusion

The **Privacy-Preserving Synthetic Tabular Data Generator** is a powerful tool for generating synthetic datasets that closely resemble real-world data, while ensuring that sensitive information is protected. It is ideal for applications in testing, model training, and data sharing without compromising privacy.

```

This README provides a complete overview with the necessary steps to run the project locally, including project setup and data generation. Let me know if you need further adjustments!
```
