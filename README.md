# NASA Battery Dataset Analysis

## Project Overview

This project analyzes Li-ion battery degradation data from NASA's Battery Dataset to understand battery aging characteristics through electrochemical impedance spectroscopy (EIS) measurements and charge/discharge cycles. The analysis focuses on visualizing impedance changes over battery lifecycle and predicting battery capacity using machine learning.

## Dataset

**Source**: [NASA Battery Dataset on Kaggle](https://www.kaggle.com/datasets/patrickfleith/nasa-battery-dataset/data)

### Dataset Description
- Li-ion batteries tested under different operational profiles (charge, discharge, impedance)
- Various temperature conditions
- Electrochemical Impedance Spectroscopy (EIS) frequency measurements
- Repeated charge/discharge cycles for accelerated aging analysis
- Experiments continued until End-of-Life (EOL) criteria
- Data organized in batches of 6 experiments
- Format: MATLAB (.mat) files with accompanying README.txt files

### Applications
- **Remaining Charge Prediction**: Predict remaining charge for a given discharge cycle
- **Remaining Useful Life (RUL)**: Predict battery lifespan
- **Battery Health Monitoring**: Track degradation patterns over time

## Project Objectives

### 1. EIS Impedance Analysis (3D Visualization)
- **Objective**: Create 3D plots showing impedance evolution with aging
- **Axes**: 
  - X-axis: Real Impedance Re(Z) [kΩ]
  - Y-axis: Imaginary Impedance -Im(Z) [kΩ]  
  - Z-axis: Aging (Cycle Count)
- **Assumptions**: Constant temperature and other conditions

### 2. Incremental Capacity Analysis (3D Visualization)
- **Objective**: Analyze charge/discharge cycle characteristics
- **Process**:
  - Derive incremental capacity (dQ/dV) from voltage-capacity curves
  - Visualize how dQ/dV peaks change with aging
- **Axes**:
  - X-axis: Voltage (V)
  - Y-axis: Incremental Capacity (Ah/V)
  - Z-axis: Aging (Cycle Count)

### 3. Machine Learning Capacity Prediction
- **Objective**: Train ML model to predict current battery capacity
- **Input Features**: EIS signature characteristics
- **Target**: Current battery capacity
- **Approach**: Regression analysis using impedance parameters

## Technical Implementation

### Technologies Used
- **Python 3.x**
- **Data Analysis**: pandas, numpy
- **Visualization**: matplotlib, plotly, seaborn
- **Machine Learning**: scikit-learn
- **Data Processing**: scipy (for .mat file handling)
- **Jupyter Notebook**: For interactive analysis

### Key Analysis Components

#### 1. Data Preprocessing
```python
# Load MATLAB files
# Extract EIS measurements
# Process charge/discharge cycles
# Handle missing values and outliers
```

#### 2. EIS Analysis
```python
# Extract Re(Z) and Im(Z) components
# Map impedance to cycle numbers
# Create 3D impedance evolution plots
```

#### 3. Incremental Capacity Analysis
```python
# Calculate dQ/dV from charge/discharge data
# Identify capacity peaks
# Track peak evolution over cycles
```

#### 4. Machine Learning Pipeline
```python
# Feature engineering from EIS data
# Model training and validation
# Capacity prediction evaluation
```

## Expected Deliverables

### Visualizations
1. **3D EIS Impedance Plot**: Shows impedance trajectory evolution over battery lifecycle
2. **3D Incremental Capacity Plot**: Demonstrates how capacity characteristics change with aging
3. **ML Model Performance**: Accuracy metrics and prediction plots

### Analysis Results
- Battery degradation patterns identification
- Key impedance parameters affecting capacity
- ML model performance metrics
- Insights into battery aging mechanisms

## Repository Structure
```
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_eis_analysis.ipynb
│   ├── 03_incremental_capacity.ipynb
│   └── 04_ml_capacity_prediction.ipynb
├── src/
│   ├── data_processing.py
│   ├── visualization.py
│   └── ml_models.py
├── data/
│   └── (NASA battery .mat files)
├── results/
│   ├── plots/
│   └── models/
├── requirements.txt
└── README.md
```

## Getting Started

### Prerequisites
```bash
pip install numpy pandas matplotlib plotly scikit-learn scipy jupyter
```

### Installation
1. Clone the repository
```bash
git clone https://github.com/yourusername/nasa-battery-analysis.git
cd nasa-battery-analysis
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Download dataset from Kaggle and place in `data/` directory

4. Launch Jupyter Notebook
```bash
jupyter notebook
```

## Usage

1. **Data Exploration**: Start with `01_data_exploration.ipynb`
2. **EIS Analysis**: Run `02_eis_analysis.ipynb` for impedance visualization
3. **Capacity Analysis**: Execute `03_incremental_capacity.ipynb`
4. **ML Modeling**: Use `04_ml_capacity_prediction.ipynb` for predictive modeling

## Key Findings

*(To be updated after analysis completion)*

- Battery impedance evolution patterns
- Critical aging indicators from EIS measurements
- ML model accuracy for capacity prediction
- Practical implications for battery management systems

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/analysis-improvement`)
3. Commit changes (`git commit -am 'Add new analysis method'`)
4. Push to branch (`git push origin feature/analysis-improvement`)
5. Create Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- NASA for providing the comprehensive battery dataset
- Kaggle for hosting the dataset
- ThinkClock Battery Labs for project guidance

## Contact

**Project Assignment by**: ThinkClock Battery Labs  
**Website**: www.thinkclock.com  
**Email**: contact@thinkclock.com

---

*This project is part of a Python Developer assignment focusing on battery analytics and machine learning applications in energy storage systems.*
