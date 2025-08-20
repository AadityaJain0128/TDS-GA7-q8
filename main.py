import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# --- Data ---
# Quarterly Customer Acquisition Cost (CAC) data for 2024
data = {
    'Quarter': ['Q1 2024', 'Q2 2024', 'Q3 2024', 'Q4 2024'],
    'CAC': [225.3, 230.2, 230.34, 232.91]
}
df = pd.DataFrame(data)

# --- Analysis ---
# Calculate the average CAC
average_cac = df['CAC'].mean()
# Industry target benchmark
industry_target = 150

# Print key metrics for verification
print(f"Quarterly CAC Data:\n{df}\n")
print(f"Calculated Average CAC: {average_cac:.2f}") # Output: 229.69
print(f"Industry Target CAC: {industry_target}")

# --- Visualization ---
# Create a plot to visualize the trend
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the quarterly CAC
ax.plot(df['Quarter'], df['CAC'], marker='o', linestyle='-', color='b', label='Quarterly CAC')
ax.fill_between(df['Quarter'], df['CAC'], color="blue", alpha=0.1)


# Plot the average CAC
ax.axhline(y=average_cac, color='r', linestyle='--', label=f'Average CAC: ${average_cac:.2f}')

# Plot the industry target
ax.axhline(y=industry_target, color='g', linestyle='--', label=f'Industry Target: ${industry_target}')

# Add value labels to the data points
for index, value in enumerate(df['CAC']):
    ax.text(index, value + 1, f'${value}', ha='center')

# --- Formatting ---
ax.set_title('Customer Acquisition Cost (CAC) Trend vs. Target - 2024', fontsize=16, fontweight='bold')
ax.set_xlabel('Quarter', fontsize=12)
ax.set_ylabel('Cost ($)', fontsize=12)
ax.legend(fontsize=10)
ax.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.ylim(bottom=140) # Ensure target line is visible with good spacing
plt.tight_layout()

# Save the figure to a file
# In a real scenario, you would uncomment the line below to save the plot
# plt.savefig('cac_trend_visualization.png', dpi=300)

# Display the plot
plt.show()