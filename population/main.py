import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


file_path = '/Users/srijitaseth/population_dataset/world_population.csv'  
df = pd.read_csv(file_path)


sns.set_style('darkgrid')


plt.figure(figsize=(12, 7))
plt.hist(df['2022 Population'], bins=10, edgecolor='black', color='cornflowerblue')
plt.title('Population Distribution in 2022', fontsize=16)
plt.xlabel('Population', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.show()


plt.figure(figsize=(14, 8))
bars = plt.bar(df['Country/Territory'], df['Density (per km²)'], color='skyblue')
plt.title('Population Density by Country/Territory in 2022', fontsize=16)
plt.xlabel('Country/Territory', fontsize=14)
plt.ylabel('Density (per km²)', fontsize=14)
plt.xticks(rotation=90, fontsize=12)
plt.yticks(fontsize=12)
plt.grid(axis='y', linestyle='--', linewidth=0.5)


for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 5, round(yval, 2), ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.show()
