# Customer Intelligence AI

A comprehensive Streamlit-based application for customer analytics, predictive modeling, and business intelligence.

## Features

- **Dashboard**: Overview of customer metrics and key performance indicators
- **Prediction**: AI-powered customer value and behavior prediction
- **Segmentation**: Advanced customer segmentation and clustering analysis
- **Churn Prediction**: Identify at-risk customers with machine learning models
- **Recommendations**: Personalized product recommendations using collaborative filtering

## Project Structure

```
customer-ai-project/
├── app.py                          # Main Streamlit application
├── data/
│   └── customer_dataset.csv        # Sample customer data
├── models/
│   ├── model.pkl                   # Main prediction model
│   ├── churn_model.pkl             # Churn prediction model
│   └── segment_encoder.pkl         # Segmentation encoder
├── pages/
│   ├── dashboard.py                # Dashboard page
│   ├── prediction.py               # Prediction page
│   ├── segmentation.py             # Segmentation page
│   ├── churn.py                    # Churn analysis page
│   └── recommendation.py           # Recommendation page
├── utils/
│   ├── dataset_generator.py        # Generate sample data
│   ├── model.py                    # Model utilities
│   ├── churn_model.py              # Churn model utilities
│   └── recommendation_engine.py    # Recommendation system
├── assets/
│   ├── logo.png                    # Application logo
│   └── styles.css                  # Custom styles
├── requirements.txt                # Python dependencies
└── README.md                       # This file
```

## Installation

1. Clone the repository or navigate to the project directory
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the Streamlit application:
```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`

## Data Preparation

To generate sample customer data:
```bash
python utils/dataset_generator.py
```

This will create a CSV file with sample customer data in `data/customer_dataset.csv`

## Model Training

Models are loaded from the `models/` directory. To train new models:

1. Update training data in `data/customer_dataset.csv`
2. Use the utilities in `utils/` directory to train and save models
3. Models will be saved as pickle files (.pkl)

## Dependencies

Key dependencies:
- **streamlit**: Web application framework
- **pandas**: Data manipulation and analysis
- **scikit-learn**: Machine learning models
- **plotly**: Interactive visualizations
- **joblib**: Model serialization

See `requirements.txt` for complete list.

## Features Description

### Dashboard
Displays key metrics including:
- Total number of customers
- Average customer value
- Active customer count
- Customer distribution by segment

### Prediction
Predict customer metrics based on:
- Customer age
- Tenure duration
- Monthly charges
- Total charges

### Segmentation
Analyze customers by:
- Segment distribution
- Segment-specific metrics
- Customer profiles

### Churn Prediction
Identify churn risk by:
- Individual customer analysis
- Risk probability calculation
- Risk level classification

### Recommendations
Generate product recommendations based on:
- Customer history
- Segment characteristics
- Purchase patterns

## Configuration

Modify configuration in respective page files:
- `pages/dashboard.py`: Dashboard metrics
- `pages/prediction.py`: Prediction parameters
- `pages/segmentation.py`: Segmentation criteria
- `pages/churn.py`: Churn model thresholds
- `pages/recommendation.py`: Recommendation rules

## Future Enhancements

- [ ] Real-time data integration
- [ ] Advanced visualization dashboard
- [ ] Multi-model ensemble predictions
- [ ] Export reports functionality
- [ ] User authentication
- [ ] Database integration
- [ ] API endpoints for external integrations

## Links

🚀 Live Demo: https://nec-project-1-m4lx.onrender.com

## License

This project is provided as-is for educational and business purposes.

## Support

For questions or issues, please contact the development team.

---

**Last Updated**: 2024
