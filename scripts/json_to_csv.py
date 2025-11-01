import json
import pandas as pd

# Load JSON file
with open('path_to_your_file.json') as f:
    data = json.load(f)

# Extract BGC data
clusters = data.get("clusters", [])

# Store results in a list
bgc_data = []
for cluster in clusters:
    bgc_data.append({
        "Cluster ID": cluster.get("id"),
        "Product Prediction": cluster.get("product_prediction"),
        "Start": cluster.get("start"),
        "End": cluster.get("end"),
        "Score": cluster.get("score"),
        "Gene Count": len(cluster.get("genes", []))
    })

# Convert to DataFrame for easier analysis
df = pd.DataFrame(bgc_data)
print(df)

# Save to CSV
df.to_csv('bgc_output.csv', index=False)