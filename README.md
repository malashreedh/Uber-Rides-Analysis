# **🚖 Uber Rides Data Analysis 📊**

Analyzing Uber ride data using Python for insights into ride categories, usage patterns, and trends. 

Includes data visualization, feature engineering, and a comprehensive PDF report of findings.


### **📌 Key Features**

🛠 Data Cleaning & Preprocessing: Handling missing values, converting dates, and feature engineering.

📊 Data Visualization: Charts & graphs using Matplotlib and Seaborn.

🔎 Insights Extraction: Ride categories, popular times, distance patterns.

📄 Comprehensive PDF Report: All charts saved in Uber_Rides_Analysis.pdf.

⚡ Easy Setup: Install dependencies with pip install -r requirements.txt and run python3 uber_analysis.py.

### **🚀 How to Use**
1. Clone this repository:

        git clone https://github.com/YOUR_USERNAME/Uber-Rides-Analysis.git
        cd Uber-Rides-Analysis

2. Install dependencies:

        pip install -r requirements.txt

3. Run the analysis:

        python3 uber_analysis.py

4. Open Uber_Rides_Analysis.pdf to view all visualizations.

## 📂 Dataset Information

The dataset (`UberDataset.csv`) contains real Uber ride data from **January 2016**. 

It includes trip details such as the start and end times, ride category (Business or Personal), distance traveled, and trip purpose.

### 📊 **Dataset Columns**

| Column Name  | Description |
|-------------|------------|
| **START_DATE** | Date and time when the ride started. |
| **END_DATE** | Date and time when the ride ended. |
| **CATEGORY** | Type of ride (**Business or Personal**). |
| **START** | Pickup location. |
| **STOP** | Drop-off location. |
| **MILES** | Distance of the ride in miles. |
| **PURPOSE** | Purpose of the ride (Meeting, Meal/Entertainment, Customer Visit, etc.). |


🚀 **This dataset helps analyze ride patterns, busiest times, and business vs. personal travel trends.**



#### **Sample chart**
![Uber Rides Analysis](https://github.com/malashreedh/Uber-Rides-Analysis/blob/main/sample_chart.png)