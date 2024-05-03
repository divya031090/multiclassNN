#######################Pie Chart#####################

import matplotlib.pyplot as plt

# Subject index (e.g., subject 1)
subject_index = 1
#for subject_index in range(len(combined_probs_df)):

# Extract combined probabilities for subject 1
subject_combined_probs = combined_probs_df.iloc[subject_index, :-1].values
predicted_class = combined_probs_df.iloc[subject_index, -1]

# Class labels
class_labels = ['BO', 'ACR', 'AH', 'MASH', 'HCV', 'congestion']

# Plot pie chart
plt.figure(figsize=(8, 8))
plt.pie(subject_combined_probs, labels=class_labels, autopct='%1.1f%%')
plt.title(f'Combined Probabilities for Subject {subject_index + 1} (Predicted Class: {predicted_class})')
plt.show()
