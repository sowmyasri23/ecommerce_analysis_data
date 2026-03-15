import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("e-commerce.csv")

# Create new columns
df["Revenue"] = df["Price"] * df["Quantity"]
df["Cost"] = df["Price"] * 0.7
df["Profit"] = df["Revenue"] - df["Cost"]

# Customer type classification
df["Customer_Type"] = np.where(df["Revenue"] > 40000, "High Value", "Regular")

while True:

    print("\n===== E-Commerce Data Analysis Menu =====")
    print("1. Show Total Sales and Profit")
    print("2. Show Revenue by Product")
    print("3. Show Revenue by City")
    print("4. Show Profit by Product")
    print("5. Show Revenue Histogram")
    print("6. Search Product Sales")
    print("7. Show Top Products by Revenue")
    print("8. Show Sales by City")
    print("9. Export Data to CSV")
    print("10. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("\nTotal Sales:", df["Revenue"].sum())
        print("Total Profit:", df["Profit"].sum())

    elif choice == 2:
        revenue_product = df.groupby("Product")["Revenue"].sum()
        print("\nRevenue by Product")
        print(revenue_product)

        revenue_product.plot(kind="bar", title="Revenue by Product")
        plt.xlabel("Product")
        plt.ylabel("Revenue")
        plt.show()

    elif choice == 3:
        revenue_city = df.groupby("City")["Revenue"].sum()
        print("\nRevenue by City")
        print(revenue_city)

        revenue_city.plot(kind="pie", autopct="%1.1f%%")
        plt.title("Revenue by City")
        plt.ylabel("")
        plt.show()

    elif choice == 4:
        profit_product = df.groupby("Product")["Profit"].sum()
        print("\nProfit by Product")
        print(profit_product)

        profit_product.plot(kind="bar", title="Profit by Product")
        plt.xlabel("Product")
        plt.ylabel("Profit")
        plt.show()

    elif choice == 5:
        plt.hist(df["Revenue"])
        plt.title("Revenue Distribution")
        plt.xlabel("Revenue")
        plt.ylabel("Frequency")
        plt.show()

    elif choice == 6:
        product_name = input("Enter product name: ")

        product_data = df[df["Product"].str.lower() == product_name.lower()]

        if product_data.empty:
            print("Product not found!")
        else:
            print("\nProduct Details")
            print(product_data)

            print("Total Revenue:", product_data["Revenue"].sum())
            print("Total Profit:", product_data["Profit"].sum())

            product_data["Revenue"].plot(kind="bar", title=f"{product_name} Revenue")
            plt.show()

    elif choice == 7:
        n = int(input("How many top products to show? "))

        top_products = df.groupby("Product")["Revenue"].sum().sort_values(ascending=False).head(n)

        print("\nTop Products by Revenue")
        print(top_products)

        top_products.plot(kind="bar", title="Top Products by Revenue")
        plt.show()

    elif choice == 8:
        city = input("Enter city name: ")

        city_data = df[df["City"].str.lower() == city.lower()]

        if city_data.empty:
            print("City not found")
        else:
            print(city_data)

            print("Total Sales:", city_data["Revenue"].sum())
            print("Total Profit:", city_data["Profit"].sum())

    elif choice == 9:
        filename = input("Enter file name to save: ")

        df.to_csv(filename + ".csv", index=False)

        print("Data exported successfully!")

    elif choice == 10:
        print("Exiting program...")
        break

    else:
        print("Invalid choice")