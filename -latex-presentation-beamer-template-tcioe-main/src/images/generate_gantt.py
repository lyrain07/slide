import matplotlib.pyplot as plt
import numpy as np

# Set style
fig, ax = plt.subplots(figsize=(10, 4.5), dpi=300)

# Tasks ordered from top to bottom on the horizontal bar chart
tasks = [
    "5. Final Integration, Prototype Development & Reporting",
    "4. System Validation Testing",
    "3. Two-Stage Matching Engine Development",
    "2. U-Net Skyline Extraction Model Training",
    "1. DEM Data Acquisition & Database Generation"
]

# Corresponding start days and durations aligned with the tasks list above
start_days = [55, 35, 25, 5, 0]
durations = [5, 20, 10, 20, 5]
colors = ['#A51E37', '#D97706', '#059669', '#0284C7', '#4F46E5'] 

# Plot bars
bars = ax.barh(tasks, durations, left=start_days, height=0.55, align='center', color=colors, alpha=0.9, edgecolor='none')

# Styling
ax.set_xlabel('Project Timeline (Days)', fontsize=11, fontweight='bold', labelpad=10, color='#0F172A')
ax.set_title('Minor Project Tentative Timeline (60 Days)', fontsize=13, fontweight='bold', pad=15, color='#0F172A')
ax.set_xlim(-2, 62)
ax.set_xticks(np.arange(0, 61, 5))
ax.set_xticklabels([f"Day {x}" if x % 10 == 0 else f"{x}" for x in np.arange(0, 61, 5)], fontsize=9, color='#475569')
ax.tick_params(axis='y', colors='#0F172A', labelsize=10)
ax.grid(True, axis='x', linestyle='--', alpha=0.5, color='#CBD5E1')
ax.grid(False, axis='y')

# Add values on the bars
for bar, sd, dur in zip(bars, start_days, durations):
    width = bar.get_width()
    ax.text(sd + dur/2, bar.get_y() + bar.get_height()/2, f"{dur} Days", 
            ha='center', va='center', color='white', fontweight='bold', fontsize=9)

# Clean spines
for spine in ['top', 'right', 'left', 'bottom']:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.savefig('src/images/gantt.png', dpi=300, bbox_inches='tight')
print("Gantt chart generated successfully.")import matplotlib.pyplot as plt
import numpy as np

# Set style
fig, ax = plt.subplots(figsize=(10, 4.5), dpi=300)

# Tasks ordered from top to bottom on the horizontal bar chart
tasks = [
    "5. Final Integration, Prototype Development & Reporting",
    "4. System Validation Testing",
    "3. Two-Stage Matching Engine Development",
    "2. U-Net Skyline Extraction Model Training",
    "1. DEM Data Acquisition & Database Generation"
]

# Corresponding start days and durations aligned with the tasks list above
start_days = [55, 35, 25, 5, 0]
durations = [5, 20, 10, 20, 5]
colors = ['#A51E37', '#D97706', '#059669', '#0284C7', '#4F46E5'] 

# Plot bars
bars = ax.barh(tasks, durations, left=start_days, height=0.55, align='center', color=colors, alpha=0.9, edgecolor='none')

# Styling
ax.set_xlabel('Project Timeline (Days)', fontsize=11, fontweight='bold', labelpad=10, color='#0F172A')
ax.set_title('Minor Project Tentative Timeline (60 Days)', fontsize=13, fontweight='bold', pad=15, color='#0F172A')
ax.set_xlim(-2, 62)
ax.set_xticks(np.arange(0, 61, 5))
ax.set_xticklabels([f"Day {x}" if x % 10 == 0 else f"{x}" for x in np.arange(0, 61, 5)], fontsize=9, color='#475569')
ax.tick_params(axis='y', colors='#0F172A', labelsize=10)
ax.grid(True, axis='x', linestyle='--', alpha=0.5, color='#CBD5E1')
ax.grid(False, axis='y')

# Add values on the bars
for bar, sd, dur in zip(bars, start_days, durations):
    width = bar.get_width()
    ax.text(sd + dur/2, bar.get_y() + bar.get_height()/2, f"{dur} Days", 
            ha='center', va='center', color='white', fontweight='bold', fontsize=9)

# Clean spines
for spine in ['top', 'right', 'left', 'bottom']:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.savefig('src/images/gantt.png', dpi=300, bbox_inches='tight')
print("Gantt chart generated successfully.")