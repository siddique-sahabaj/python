import pandas
import seaborn
import matplotlib.pyplot as plt

# Getting the Electric Vehicles Data and converting it into pandas dataframe
electric_vehicles_data = pandas.read_csv("Electric_Vehicle_Population_Data.csv")

# Cleaning the data

electric_vehicles_data.isnull().sum() # Checking the null values of each column
electric_vehicles_data = electric_vehicles_data.dropna() # Removing the rows who have null values

def plot_graph(title, xlabel, ylabel):
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.tight_layout()
    plt.show()

def ev_sales_per_year():
    ev_sales_per_year = electric_vehicles_data["Model Year"].value_counts().sort_index()

    # Creating and showing the figure
    seaborn.set_style("whitegrid")
    plt.figure(figsize=(10, 5))
    seaborn.barplot(x=ev_sales_per_year.index, y=ev_sales_per_year.values, palette="pastel")
    plot_graph(title="EV Sales Per Year", xlabel="Model Year", ylabel="Number of Registered/Sold Vehicles")

def top_cities_by_ev_sales():

    # EV Sales According to the Counties
    ev_sales_acc_to_counties = electric_vehicles_data['County'].value_counts()
    top_counties = ev_sales_acc_to_counties.head(3).index

    # Filtering and Getting the data of top Counties
    top_counties_data = electric_vehicles_data[electric_vehicles_data['County'].isin(top_counties)]

    # Analyzing the Sales of EVs within the cities of these top counties
    ev_sales_acc_to_cities = top_counties_data.groupby(['County', 'City']).size().sort_values(
        ascending=False).reset_index(name='Number of Vehicles')

    # Selecting the top 10 Cities
    top_cities = ev_sales_acc_to_cities.head(10)

    # Plotting the figure
    plt.figure(figsize=(10, 5))
    seaborn.barplot(x="Number of Vehicles", y="City", hue="County", data=top_cities, palette="muted")
    plt.legend(title='County')
    plot_graph(title="Top Cities by EV Registrations", xlabel="Number of Registered/Sold Vehicles", ylabel="City")

def sales_per_ev_types():

    # Getting the sales per ev types.
    sales_per_ev_types = electric_vehicles_data['Electric Vehicle Type'].value_counts()

    plt.figure(figsize=(10, 6))
    seaborn.barplot(x=sales_per_ev_types.values, y=sales_per_ev_types.index, palette="deep")
    plot_graph(title="Sales according to the types of Electric Vehicles", xlabel="Number of Registered/Sold Vehicles",
               ylabel="Type of Electric Vehicle")

def top_ev_makes():

    # Selecting the top 10 EV Makes
    top_ev_makes = electric_vehicles_data['Make'].value_counts().head(10)

    plt.figure(figsize=(10, 5))
    seaborn.barplot(x=top_ev_makes.values, y=top_ev_makes.index, palette="cubehelix")
    plot_graph(title="Top 10 Popular EV Makes", xlabel="Number of Vehicles Registered", ylabel="Make")

def distribution_of_ev_ranges():

    plt.figure(figsize=(10, 5))
    seaborn.histplot(electric_vehicles_data['Electric Range'], bins=30, kde=True, color='royalblue')
    plt.axvline(electric_vehicles_data['Electric Range'].mean(), color='red', linestyle='--',
                label=f'Mean Range: {electric_vehicles_data["Electric Range"].mean():.2f} miles')
    plot_graph(title="Distribution of Electric Vehicle Ranges", xlabel="Electric Range (miles)", ylabel="Number of Vehicles")

########################

print("\n\nWELCOME TO THE USA EV MARKET ANALYSIS PLATFORM\n"
      "==============================================\n"
      "\n"
      "Tell us what you want us to analyze.\n"
      "We will analyze the data according to the options you selected and show you the relevant graphs.\n"
      "\n"
      "1) Show the Electric Vehicles Growth Over Time\n"
      "2) Show which Cities have most electric vehicle sales\n"
      "3) Show the Sales per Electric Vehicle types\n"
      "4) Show the top EV Makes"
      "5) Show the Distribution of EV Ranges\n")
should_continue = True

while should_continue:
    choice = input("Enter your choice : ")
    if choice == "exit":
        break
    choice = int(choice)
    if choice == 1:
        ev_sales_per_year()
    elif choice == 2:
        top_cities_by_ev_sales()
    elif choice == 3:
        sales_per_ev_types()
    elif choice == 4:
        top_ev_makes()
    elif choice == 5:
        distribution_of_ev_ranges()
    else:
        print("\nInvalid Choice ! Please Choose correct option")
