# Privacy-Preserving Synthetic Tabular Data Generator

## Project Description
**Privacy-Preserving Synthetic Tabular Data Generator** is a Python-based tool designed to generate synthetic tabular data while ensuring privacy. It uses advanced machine learning algorithms to learn the patterns of real-world data and generate synthetic data that mimics these patterns. This tool is useful when real-world data cannot be shared due to privacy concerns, but synthetic data is needed for testing or training purposes.

### Key Features:
- **Tabular Data Generation**: Create synthetic data for single or multiple related tables.
- **Privacy Preservation**: Ensures that the generated data does not leak sensitive or personal information.
- **Anonymization and Constraints**: Allows data to be anonymized and apply logical constraints to improve data quality.
- **Evaluation**: Provides tools for evaluating the quality of synthetic data.

## Project Requirements

1. **Python 3.8+**  
   Install Python from [python.org](https://www.python.org/).

2. **Required Libraries**  
   Install the dependencies using:
   ```bash
   pip install -r requirements.txt
Additional Tools:

Ensure you have Git installed for version control.

You may also need Jupyter Notebook for running tutorials or experiments.

How to Run the Project Locally
Step 1: Clone the Repository
Clone the repository to your local machine:

bash
Copy code
git clone https://github.com/NMANISH9800/Privacy-Preserving-Synthetic-Tabular-Data-Generator.git
cd Privacy-Preserving-Synthetic-Tabular-Data-Generator
Step 2: Set Up the Virtual Environment
Create and activate a virtual environment:

bash
Copy code
python -m venv venv
Activate the virtual environment:

Windows:

bash
Copy code
venv\Scripts\activate
macOS/Linux:

bash
Copy code
source venv/bin/activate
Step 3: Install Dependencies
Install all the necessary dependencies:

bash
Copy code
pip install -r requirements.txt
Step 4: Generate Synthetic Data
Run the generator to create synthetic data from real data:

bash
Copy code
python generate_synthetic_data.py
This will generate synthetic data based on the configuration set in the script.

Step 5: Evaluate the Results
After generating the synthetic data, use the provided evaluation functions to compare it with real data:

bash
Copy code
python evaluate_synthetic_data.py
Step 6: Modify the Experiment
You can adjust the script settings and experiment with different data types, algorithms, and parameters as needed.
