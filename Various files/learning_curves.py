# It seems that the pandas and matplotlib libraries need to be re-imported
import pandas as pd
import matplotlib.pyplot as plt

# Data from the new table
new_data = {
    'Step': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250],
    'Training Loss': [2.8395, 1.557, 0.485, 0.328, 0.345, 0.306, 0.287, 0.286, 0.276, 0.279, 0.254, 0.251, 0.256, 0.2515, 0.2514, 0.252, 0.224, 0.237, 0.234, 0.230, 0.212, 0.215, 0.216, 0.212, 0.228],
    'Validation Loss': [2.204, 0.708, 0.363, 0.3312, 0.3024, 0.286, 0.278, 0.270, 0.266, 0.262, 0.259, 0.257, 0.250, 0.248, 0.246, 0.243, 0.244, 0.241, 0.240, 0.240, 0.241, 0.240, 0.239, 0.239, 0.238]
}

# Convert the new data into a pandas DataFrame
df_new = pd.DataFrame(new_data)

# Plotting the learning curve for the new data
plt.figure(figsize=(10, 6))
plt.plot(df_new['Step'], df_new['Training Loss'], label='Training Loss', marker='o')
plt.plot(df_new['Step'], df_new['Validation Loss'], label='Validation Loss', marker='o')
plt.xlabel('Steps')
plt.ylabel('Loss')
plt.title('Norm-Simple-Trunc-8 Learning Curves')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
