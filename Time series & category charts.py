import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv(
    r"C:\Users\kenneth.ngono\OneDrive - Cipla Limited\Documents\Python\Data Science\sales_data.csv",
    sep=";"
)

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

# Display column names
print("Columns:", df.columns.tolist())

# Convert Date column to datetime format
df["Date"] = pd.to_datetime(df["Date"])

# Create a Month column
df["Month"] = df["Date"].dt.month_name()

# Group sales by month
monthly_sales = df.groupby("Month")["Sales"].sum()

# Arrange months in correct order
month_order = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

monthly_sales = monthly_sales.reindex(month_order)

# Create line chart
plt.figure(figsize=(8, 5))

plt.plot(
    monthly_sales.index,
    monthly_sales.values,
    marker="o",
    color="blue"
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.grid(True)

# Save image
plt.savefig("monthly_sales_line_chart.png")

# Show chart
plt.show()

print("Chart created successfully!")


# Group sales by category
category_sales = df.groupby("Catogory")["Sales"].sum()

# Create bar chart
plt.figure(figsize=(8, 5))

category_sales.plot(
    kind="bar",
    color=["blue", "green", "orange"]
)

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")

plt.savefig("category_bar_chart.png")

plt.show()

# Group sales by category
category_sales = df.groupby("Catogory")["Sales"].sum()

# Create pie chart
plt.figure(figsize=(8, 6))

plt.pie(
    category_sales,
    labels=category_sales.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Sales Distribution by Category")

plt.savefig("category_pie_chart.png")

plt.show()