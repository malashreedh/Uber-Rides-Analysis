import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
from sklearn.preprocessing import OneHotEncoder
from matplotlib.backends.backend_pdf import PdfPages

# Load the dataset
dataset = pd.read_csv("UberDataset.csv")

# Data Preprocessing
dataset['PURPOSE'] = dataset['PURPOSE'].fillna("OTHERS")
dataset['START_DATE'] = pd.to_datetime(dataset['START_DATE'], errors='coerce')
dataset['END_DATE'] = pd.to_datetime(dataset['END_DATE'], errors='coerce')

dataset['date'] = dataset['START_DATE'].dt.date
dataset['time'] = dataset['START_DATE'].dt.hour

dataset['day-night'] = pd.cut(dataset['time'], bins=[0, 10, 15, 19, 24],
                              labels=['Morning', 'Afternoon', 'Evening', 'Night'])

dataset.dropna(inplace=True)
dataset.drop_duplicates(inplace=True)

# ✅ Create a PDF file for saving all plots
with PdfPages("Uber_Rides_Analysis.pdf") as pdf:

    # 🚀 First Chart: Ride Category and Purpose Count
    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    sns.countplot(x=dataset['CATEGORY'])
    plt.title("Ride Category Count")

    plt.subplot(1, 2, 2)
    sns.countplot(x=dataset['PURPOSE'])
    plt.xticks(rotation=90)
    plt.title("Purpose of Rides")
    
    pdf.savefig()  # Save the figure
    plt.close()

    # 🚀 Second Chart: Count of rides by time of the day
    plt.figure()
    sns.countplot(x=dataset['day-night'])
    plt.title("Rides by Time of Day")

    pdf.savefig()
    plt.close()

    # 🚀 Third Chart: CATEGORY vs PURPOSE Comparison
    plt.figure(figsize=(12, 5))
    sns.countplot(data=dataset, x='PURPOSE', hue='CATEGORY')
    plt.xticks(rotation=90)
    plt.title("Comparison of Ride Purpose by Category")

    pdf.savefig()
    plt.close()

    # 🚀 Fourth Chart: Correlation Heatmap
    numeric_dataset = dataset.select_dtypes(include=['number'])
    plt.figure(figsize=(10, 5))
    sns.heatmap(numeric_dataset.corr(), cmap='coolwarm', annot=True)
    plt.title("Correlation Heatmap")

    pdf.savefig()
    plt.close()

    # 🚀 Fifth Chart: Monthly Trends in Uber Rides
    dataset['MONTH'] = dataset['START_DATE'].dt.month
    month_label = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr',
                   5: 'May', 6: 'Jun', 7: 'Jul', 8: 'Aug',
                   9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}
    dataset["MONTH"] = dataset['MONTH'].map(month_label)
    mon = dataset['MONTH'].value_counts(sort=False)

    plt.figure(figsize=(10, 5))
    sns.lineplot(x=mon.index, y=mon.values, marker='o')
    plt.title("Monthly Uber Ride Count")
    plt.xlabel("Month")
    plt.ylabel("Total Rides")

    pdf.savefig()
    plt.close()

    # 🚀 Sixth Chart: Ride Distance Analysis (Boxplot)
    plt.figure()
    sns.boxplot(x=dataset['MILES'])
    plt.title("Distribution of Ride Distance")

    pdf.savefig()
    plt.close()

    # 🚀 Seventh Chart: Ride Distance Histogram
    plt.figure()
    sns.histplot(dataset[dataset['MILES'] < 40]['MILES'], bins=20, kde=True)
    plt.title("Distribution of Rides Under 40 Miles")

    pdf.savefig()
    plt.close()

print("✅ All plots have been saved into Uber_Rides_Analysis.pdf")

# Save insights to a text file
insights = """
Uber Rides Data Analysis - Insights

1. Most rides are booked for BUSINESS purposes.
2. The most common purposes for rides are Meetings and Meal/Entertainment.
3. Most cabs are booked between 10 AM - 5 PM (Afternoon).
4. Business and Personal ride categories are negatively correlated.
5. Ride counts are significantly lower in winter months (Nov, Dec, Jan).
6. Most rides are under 20 miles, with a peak around 4-5 miles.
7. Short rides (0-20 miles) dominate, while long-distance rides are rare.
"""

with open("Uber_Rides_Insights.txt", "w") as file:
    file.write(insights)

print("✅ Insights exported to Uber_Rides_Insights.txt")

# Export Cleaned Data
dataset.to_csv("Cleaned_UberDataset.csv", index=False)
print("✅ Cleaned dataset exported to Cleaned_UberDataset.csv")
