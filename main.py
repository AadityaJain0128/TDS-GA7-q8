import matplotlib.pyplot as plt
import numpy as np

# --- Data ---
quarters = ['Q1 2024', 'Q2 2024', 'Q3 2024', 'Q4 2024']
cac = [225.3, 230.2, 230.34, 232.91]
industry_target = 150

# --- Analysis ---
average_cac = np.mean(cac)
print(f"Average Customer Acquisition Cost (CAC): {average_cac:.2f}")

# --- Visualization ---
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the CAC trend
ax.plot(quarters, cac, marker='o', linestyle='-', color='b', label='Quarterly CAC')

# Plot the industry target
ax.axhline(y=industry_target, color='r', linestyle='--', label=f'Industry Target: ${industry_target}')

# Add data labels
for i, txt in enumerate(cac):
    ax.annotate(f'${txt}', (quarters[i], cac[i]), textcoords="offset points", xytext=(0,10), ha='center')

# --- Formatting ---
ax.set_title('Customer Acquisition Cost (CAC) Trend - 2024', fontsize=16)
ax.set_xlabel('Quarter', fontsize=12)
ax.set_ylabel('Customer Acquisition Cost ($)', fontsize=12)
ax.legend()
ax.grid(True)

# Improve y-axis to give context
ax.set_ylim(bottom=140, top=max(cac) + 20)

plt.tight_layout()

# Save the figure
plt.savefig('chart.png')

# Show the plot
plt.show()