##############Feature Importance through Integrated Gradients#### Run by each class###

##For only class 1

X_test = np.random.rand(832, 25)  # Example X_test data
baseline = np.zeros_like(X_test[0])  # Baseline
target_class_idx = 1  # Index of the target class
num_classes = 6 # Number of output classes in your model
batch_size = 32 

class_idx = 1  # Index of the class you want to compute integrated gradients for

feature_importance_for_class = []

for sample in X_test:
    sample_tensor = tf.convert_to_tensor(sample.reshape(1, -1), dtype=tf.float32)
    integrated_grads = integrated_gradients(model, baseline, sample_tensor, class_idx)
    feature_importance_for_class.append(np.mean(integrated_grads, axis=0))

# Average feature importance across all samples for the specified class
average_feature_importance_for_class = np.abs(np.mean(feature_importance_for_class, axis=0))

import matplotlib.pyplot as plt
average_feature_importance_for_class = np.abs(average_feature_importance_for_class)
# Generate feature indices
feature_names = list(df.columns[:-1])  # Exclude the last column
feature_names = feature_names[:-1]
# Plot average feature importance with feature names
plt.figure(figsize=(12, 6))
plt.bar(feature_names, average_feature_importance_for_class[:-1])  # Exclude the importance of the last feature
plt.xlabel('Feature Names')
plt.ylabel('Average Feature Importance')
plt.title(f'Average Feature Importance for Class {class_idx}')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
plt.grid(True)
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()


