# Pakistan Election Prediction System 2024

![Python](https://img.shields.io/badge/python-v3.10+-blue.svg)
![Scikit-learn](https://img.shields.io/badge/scikit--learn-latest-green.svg)
![Pandas](https://img.shields.io/badge/pandas-latest-orange.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)


![Dashboard](https://github.com/user-attachments/assets/9658feb7-9a06-402f-af72-5cee2177f2e9)

A comprehensive machine learning system for predicting Pakistan's 2024 General Election outcomes using historical election data and advanced data science techniques.

## 📋 Project Description

This project leverages machine learning algorithms to predict election results for Pakistan's 2024 General Elections. The system analyzes historical election data from 2002-2018 to forecast outcomes for all 266 National Assembly constituencies, providing seat-wise predictions and party-wise vote distributions.

**Key Capabilities:**
- Predicts election outcomes for all 266 National Assembly seats
- Forecasts vote counts, turnout percentages, and seat distributions
- Provides party-wise vote aggregations and winner predictions
- Uses Random Forest Regression for multi-target prediction

## ✨ Features & Benefits

### 🎯 Core Features
- **NA-wise Seat Prediction**: Detailed predictions for each National Assembly constituency
- **Multi-target Regression**: Simultaneous prediction of votes, turnout, and vote percentages
- **Party Consolidation**: Intelligent grouping of similar political parties (PTI, PMLN, PPP, MQM, GDA, Others)
- **Data Preprocessing**: Comprehensive outlier detection and data cleaning
- **Feature Engineering**: Vote percentage calculations and categorical encoding

### 📊 Benefits
- **Strategic Planning**: Helps political parties and analysts understand potential outcomes
- **Data-Driven Insights**: Provides statistical backing for election predictions
- **Historical Analysis**: Leverages 16+ years of election data for accurate forecasting
- **Scalable Architecture**: Easy to extend for future elections or additional features

## 🚀 Installation

### Prerequisites
- Python 3.10 or higher
- pip package manager

### Dependencies
Install the required packages:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn jupyter
```

### Environment Setup
1. Clone the repository:
```bash
git clone <repository-url>
cd "Anomaly Detection in Large intestine"
```

2. Navigate to the project directory:
```bash
cd "Data-Science-Projects/Election prediction System"
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## 📖 Usage

### Running the Analysis

#### Option 1: Jupyter Notebook (Recommended)
```bash
jupyter notebook ELECTION_2024_PREDICTION.ipynb
```

#### Option 2: Python Script
```bash
python script.py
```

### Training the Model

The model training process includes:

1. **Data Loading**: Load historical election data (2002-2018)
2. **Data Preprocessing**: Clean and standardize party names, handle outliers
3. **Feature Engineering**: Create vote percentage features
4. **Model Training**: Train Random Forest Regressor
5. **Prediction**: Generate predictions for 2024 elections

### Example Usage

```python
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler, OneHotEncoder

# Load historical data
election_data = pd.read_csv('all elections.csv')

# Prepare features and targets
X = election_data[['Constituency_Title', 'Party', 'Total_Registered_Voters']]
y = election_data[['Votes', 'Total_Valid_Votes', 'Total_Rejected_Votes', 
                   'Total_Votes', 'Turnout', 'vote percent']]

# Train model
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_transformed, y)

# Make predictions
predictions = rf_model.predict(X_2024_transformed)
```

## 📁 Project Structure

```
Data-Science-Projects/
├── Election prediction System/
│   ├── ELECTION_2024_PREDICTION.ipynb    # Main analysis notebook
│   ├── script.py                          # Web scraping script
│   ├── Project Read me                    # Project documentation
│   ├── Data Files/
│   │   ├── NA_RESULT_2002.csv            # 2002 election results
│   │   ├── NA_RESULT_2008.csv            # 2008 election results
│   │   ├── NA_RESULT_2013.csv            # 2013 election results
│   │   ├── NA_RESULT_2018.csv            # 2018 election results
│   │   ├── NA_WISE_2024.csv              # 2024 constituency data
│   │   ├── all elections.csv              # Combined historical data
│   │   ├── na_wise_predictions.csv        # Model predictions
│   │   ├── winners.csv                    # Predicted winners
│   │   └── Turnout_outliers.csv           # Outlier analysis
│   ├── Visualizations/
│   │   ├── Dashboard.jpg                   # Dashboard screenshot
│   │   └── 2024_Pakistani_general_election_-_Results.svg.png
│   └── Documentation/
│       ├── Final Document Project.docx    # Project report
│       └── Total Votes Prediction_PArty_Wise.xlsx
└── README.md                              # Main project documentation
```

## 📊 Dataset Details

### Historical Data (2002-2018)
- **Total Records**: 11,740 election entries
- **Time Period**: 2002, 2008, 2013, 2018 elections
- **Constituencies**: All National Assembly seats
- **Features**: 
  - Constituency information
  - Candidate details
  - Party affiliations
  - Vote counts and percentages
  - Turnout statistics

### 2024 Prediction Data
- **Constituencies**: 266 National Assembly seats
- **Parties**: 6 major party categories (PTI, PMLN, PPP, MQM, GDA, Others)
- **Predictions**: Vote counts, turnout, and seat winners

### Data Preprocessing
- **Outlier Detection**: IQR-based outlier removal for turnout and vote data
- **Party Standardization**: Consolidated similar party names
- **Feature Engineering**: Created vote percentage features
- **Missing Data**: Handled zero votes and invalid entries

## 📈 Results & Evaluation Metrics

### Model Performance
The Random Forest Regressor achieved the following performance metrics:

| Target Variable | R² Score | MAE | MSE |
|----------------|----------|-----|-----|
| Total Valid Votes | 0.947 | 6,196 | 190,956,125 |
| Total Votes | 0.947 | 6,354 | 199,905,492 |
| Turnout | 0.860 | 1.994 | 18.076 |
| Total Rejected Votes | 0.783 | 519 | 3,068,104 |
| Votes | 0.148 | 12,581 | 537,226,115 |
| Vote Percent | 0.071 | 8.181 | 208.252 |

### 2024 Election Predictions
Based on the trained model, the predicted seat distribution:

| Party | Predicted Seats | Predicted Votes |
|-------|----------------|-----------------|
| PMLN | 132 | 18,942,454 |
| PTI | 118 | 22,616,118 |
| PPP | 12 | 5,179,680 |
| Others | 2 | 8,822,164 |
| MQM | 2 | 1,237,376 |
| Independent | - | 9,748,611 |

## 🔧 Technical Implementation

### Machine Learning Pipeline
1. **Data Preprocessing**: OneHotEncoder for categorical variables, StandardScaler for numerical features
2. **Model**: Random Forest Regressor with 100 estimators
3. **Validation**: Train-test split with cross-validation
4. **Multi-target Prediction**: Simultaneous prediction of 6 target variables

### Key Libraries Used
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computing
- **scikit-learn**: Machine learning algorithms
- **matplotlib/seaborn**: Data visualization
- **jupyter**: Interactive development environment

## 🚀 Future Improvements

### Planned Enhancements
- [ ] **Real-time Data Integration**: Incorporate live polling data
- [ ] **Advanced Models**: Implement ensemble methods and deep learning
- [ ] **Confidence Intervals**: Add uncertainty quantification
- [ ] **Interactive Dashboard**: Web-based visualization interface
- [ ] **API Development**: RESTful API for prediction services
- [ ] **Provincial Analysis**: Extend to provincial assembly predictions

### Technical Debt
- [ ] **Code Refactoring**: Modularize the analysis pipeline
- [ ] **Error Handling**: Improve robustness and error management
- [ ] **Documentation**: Add comprehensive API documentation
- [ ] **Testing**: Implement unit tests and validation frameworks
- [ ] **Performance Optimization**: Optimize for larger datasets

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Project Developer**: [Your Name]
**Supervisor**: Mazhar Javed

## 🙏 Acknowledgments

- **Mazhar Javed** for project supervision and guidance
- **Election Commission of Pakistan** for providing historical election data
- **Open Source Community** for the excellent Python data science ecosystem
- **Contributors** who provided valuable feedback and suggestions

## 📞 Contact

For questions, suggestions, or collaboration opportunities, please reach out through:
- **Email**: [your-email@domain.com]
- **LinkedIn**: [Your LinkedIn Profile]
- **GitHub**: [Your GitHub Profile]

---

*This project is developed for educational and research purposes. Election predictions should be interpreted as statistical forecasts and not as definitive outcomes.*
