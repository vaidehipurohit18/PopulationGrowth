# Population Growth and Migration Analysis System
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
# Display project title
print("Population Project")


# Initial population
population = 1000
print("Initial Population:", population)

# Calculate yearly growth (8%)
growth = population * 0.08
print("Growth:", growth)

# Calculate yearly migration loss (2%)
migration = population * 0.02
print("Migration Loss:", migration)

# Calculate final population after one year
final_population = population + growth - migration
print("Final Population After 1 Year:", final_population)

# Simulate first 5 years
population = 1000
for year in range(1, 6):
    growth = population * 0.08
    migration = population * 0.02
    population = population + growth - migration
    print("Year", year, "Population:", round(population, 2))

# Create list to store yearly records
records = []

# Reset population for 50-year simulation
population = 1000

# Display table heading
print("Year\tPopulation")

# Simulate 50 years
for year in range(1, 51):
    growth = population * 0.08
    migration = population * 0.02
    population = population + growth - migration
    print(year, round(population, 2))

    # Store data for each year
    records.append([
        year,
        round(population, 2),
        round(growth, 2),
        round(migration, 2)
    ])

# Import pandas for table creation
import pandas as pd

# Convert list into DataFrame
df = pd.DataFrame(
    records,
    columns=["Year", "Population", "Growth", "Migration Loss"]
)

# Display DataFrame
print(df)

# Export data to CSV file
df.to_csv("population_data.csv", index=False)

# Find year when population exceeds 5000
population = 1000
year = 0

while population < 5000:
    population = population * 1.06
    year += 1

print("Population exceeds 5000 in Year:", year)

# Import matplotlib for graph
import matplotlib.pyplot as plt

# Plot population growth graph
plt.plot(df["Year"], df["Population"])
plt.title("Population Growth Over Time")
plt.xlabel("Year")
plt.ylabel("Population")
plt.grid(True)
plt.show()

# Part 3 - Population Milestone Detection

milestones = [5000, 10000, 50000, 100000, 1000000]

print("\nPopulation Milestone Report")

for target in milestones:
    population = 1000
    year = 0

    while population < target:
        population = population * 1.06
        year += 1

    print("Population exceeds", target, "in Year", year)
    
# Part 4 - Mathematical Verification
formula_population = 1000*(1.06**50)
print("Population after 50 years using formula:",round(formula_population,2))

# Part 5 - Long Term Forecasting
forecast_years=[50,100,200,500]
print("\nLong Term Forecast")
for year in forecast_years:
    population=1000*(1.06**year)
    multiplier=population/1000
    print("Years:",year,"Population:",round(population,2),"Growth Rate: 6%","Multiplier:",round(multiplier,2))
    
# Part 6 - Population Doubling Analysis
population=1000
year=0
while population<2000:
    population=population*1.06
    year+=1
print("\nPopulation doubles in Year:",year)
print("Population:",round(population,2))

# Part 7 - Population Growth Comparison
city_a=1000
city_b=1000
city_c=1000
for year in range(100):
    city_a=city_a*(1+0.08-0.02)
    city_b=city_b*(1+0.10-0.03)
    city_c=city_c*(1+0.12-0.05)
print("\nCity Comparison After 100 Years")
print("City A:",round(city_a,2))
print("City B:",round(city_b,2))
print("City C:",round(city_c,2))
if city_a>city_b and city_a>city_c:
    print("Fastest Growing City: City A")
elif city_b==city_c:
    print("Fastest Growing Cities: City B and City C (Tie)")
elif city_b>city_c:
    print("Fastest Growing City: City B")
else:
    print("Fastest Growing City: City C")
    
# Part 8 - Population Decline Scenario
population=1000
below500=None
below100=None
for year in range(1,101):
    population=population*(1+0.03-0.05)
    if population<500 and below500 is None:
        below500=year
    if population<100 and below100 is None:
        below100=year
print("\nDecline Analysis")
print("Falls below 500 in Year:",below500)
print("Falls below 100 in Year:",below100)
if population<1:
    print("Extinction Occurs")
else:
    print("No Extinction Within 100 Years")
    
# Part 9 - Monte Carlo Simulation
import random
import numpy as np
results=[]
for simulation in range(100):
    population=1000
    for year in range(100):
        growth=random.uniform(0.05,0.10)
        migration=random.uniform(0.01,0.04)
        population=population*(1+growth-migration)
    results.append(population)
print("\nMonte Carlo Simulation")
print("Best Outcome:",round(max(results),2))
print("Worst Outcome:",round(min(results),2))
print("Average Outcome:",round(np.mean(results),2))

# Part 10 - Statistical Analysis
population_values=df["Population"]
print("\nStatistical Analysis")
print("Maximum Population:",round(np.max(population_values),2))
print("Minimum Population:",round(np.min(population_values),2))
print("Average Population:",round(np.mean(population_values),2))
print("Median Population:",round(np.median(population_values),2))
print("Standard Deviation:",round(np.std(population_values),2))
print("Growth Variance:",round(np.var(population_values),2))

# Part 11 - Population Growth Graph
plt.figure(figsize=(10,5))
plt.plot(df["Year"],df["Population"])
plt.title("Population Growth Over Time")
plt.xlabel("Year")
plt.ylabel("Population")
plt.grid(True)
plt.savefig("population_growth.png")
plt.show()

# Part 11 - Bar Chart
plt.figure(figsize=(10,5))
plt.bar(df["Year"],df["Growth"])
plt.title("Yearly Growth")
plt.xlabel("Year")
plt.ylabel("Growth")
plt.savefig("yearly_growth.png")
plt.show()

# Part 11 - Pie Chart
total_growth=df["Growth"].sum()
total_migration=df["Migration Loss"].sum()
plt.figure(figsize=(6,6))
plt.pie([total_growth,total_migration],labels=["Growth","Migration Loss"],autopct="%1.1f%%")
plt.title("Growth vs Migration Loss")
plt.savefig("growth_vs_migration.png")
plt.show()

# Part 11 - City Comparison Graph
cities=["City A","City B","City C"]
populations=[city_a,city_b,city_c]
plt.figure(figsize=(8,5))
plt.bar(cities,populations)
plt.title("City Population Comparison")
plt.xlabel("Cities")
plt.ylabel("Population")
plt.savefig("city_comparison.png")
plt.show()

# Part 12 - Prepare Data For Reports
milestone_data=[]
for target in milestones:
    population=1000
    year=0
    while population<target:
        population=population*1.06
        year+=1
    milestone_data.append([target,year])

milestone_df=pd.DataFrame(
    milestone_data,
    columns=["Population Target","Year Reached"]
)

forecast_data=[]
for year in forecast_years:
    population=1000*(1.06**year)
    multiplier=population/1000
    forecast_data.append([
        year,
        round(population,2),
        "6%",
        round(multiplier,2)
    ])

forecast_df=pd.DataFrame(
    forecast_data,
    columns=["Years","Population","Growth Rate","Multiplier"]
)

# Part 12 - Excel Report
with pd.ExcelWriter("population_report.xlsx") as writer:
    df.to_excel(writer,sheet_name="Yearly Population",index=False)
    forecast_df.to_excel(writer,sheet_name="Growth Analysis",index=False)
    milestone_df.to_excel(writer,sheet_name="Milestone Report",index=False)

print("Excel Report Generated")

# Part 13 - CSV Export
df.to_csv("population_data.csv",index=False)
forecast_df.to_csv("growth_analysis.csv",index=False)
milestone_df.to_csv("milestone_report.csv",index=False)

print("CSV Files Generated")

# Part 14 - Population Query System
query_year=int(input("Enter Year (1-50): "))

if 1<=query_year<=50:
    row=df.iloc[query_year-1]
    print("Population:",row["Population"])
    print("Growth:",row["Growth"])
    print("Migration Loss:",row["Migration Loss"])
else:
    print("Invalid Year")