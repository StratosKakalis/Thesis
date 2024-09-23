# It seems that the pandas and matplotlib libraries need to be re-imported
import pandas as pd
import matplotlib.pyplot as plt

# Data from the new table
new_data = {
    'Step': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370],
    'Training Loss': [1.739600, 1.139500, 0.529900, 0.399900, 0.352200, 0.301300, 0.287600, 0.296000, 0.281900, 0.265400, 0.265900, 0.253680, 0.253300, 0.246000, 0.223500, 0.215600, 0.223300, 0.225400, 0.220300, 0.202300, 0.206300, 0.213500, 0.20250, 0.192500, 0.190400, 0.197500, 0.189000, 0.189900, 0.179500, 0.173400, 0.172000, 0.182800, 0.18080, 0.162400, 0.172300, 0.172600, 0.168300],
    'Validation Loss': [1.559345, 0.718919, 0.432377, 0.362587, 0.328678, 0.313414, 0.303795, 0.292212, 0.283960, 0.279835, 0.271191, 0.266573, 0.264406, 0.259101, 0.261106, 0.256645, 0.253065, 0.253050, 0.247555, 0.251507, 0.246796, 0.243952, 0.245366, 0.243025, 0.244151, 0.243072, 0.240951, 0.241467, 0.244546, 0.247878, 0.241941, 0.239014, 0.240891, 0.242569, 0.242886, 0.243582, 0.242901]
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
