# Geospatial Threat Analysis - Wildfire Prediction using ML

This project focuses on the geospatial analysis and prediction of wildfire threats in Madhya Pradesh and nearby regions in India using historical data from NASA's FIRMS (Fire Information for Resource Management System). By leveraging machine learning algorithms such as Random Forest and Autoencoder, the model aims to detect wildfire-prone areas with high accuracy.

## 📊 Dataset

- **Source**: [NASA FIRMS](https://earthdata.nasa.gov/firms)
- **Region**: Madhya Pradesh and neighboring Indian states
- **Duration**: Last 13 years
- **Records**: 126,745 fire detection points
- **Format**: CSV (Latitude, Longitude, Brightness, Date, Confidence, FRP, etc.)

## 🧠 Machine Learning Models

### 🔍 Random Forest Classifier
- Used for supervised classification of fire vs. non-fire zones
- Handles non-linear relationships and imbalanced datasets well
- Achieved accuracy: **98%**

### 🧬 Autoencoder (Unsupervised)
- Detects anomalies in spatio-temporal patterns
- Helps in capturing latent fire features and reducing false positives


## ⚙️ Implementation Workflow

1. **Data Preprocessing**: Cleaning nulls, removing duplicates, normalizing fields
2. **Feature Extraction**: Geolocation encoding, brightness thresholding, etc.
3. **Model Training & Testing**: 80-20 split with k-fold cross-validation
4. **Evaluation Metrics**: Accuracy, Precision, Recall, F1-Score, Confusion Matrix
5. **Deployment**: Flask-based web application (can be dockerized)
6. **Prediction**: Upload a CSV or stream real-time FIRMS data to detect wildfire threats


## 🚀 How to Run

bash
# Step 1: Clone the repository
git clone https://github.com/yourusername/wildfire-threat-analysis.git
cd wildfire-threat-analysis

# Step 2: Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Step 3: Install dependencies
pip install -r requirements.txt

# Step 4: Run the prediction script
python src/predict.py --input data/new_firms_data.csv

