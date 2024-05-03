########################Bayesian Fusion#################

alpha = 0.2

# Combine probabilities using Bayesian fusion
combined_probs = alpha * subject_probs_df.values + (1 - alpha) * y_pred_prob

# Create a DataFrame for combined probabilities
combined_probs_normalized = combined_probs / np.sum(combined_probs, axis=1, keepdims=True)

# Create a DataFrame for normalized combined probabilities
combined_probs_df = pd.DataFrame(combined_probs_normalized, columns=subject_probs_df.columns)
predicted_classes = np.argmax(combined_probs_normalized, axis=1)

class_labels = {0: 'BO', 1: 'ACR', 2: 'AH', 3: 'MASH', 4: 'HCV', 5: 'congestion'}
predicted_labels = [class_labels[idx] for idx in predicted_classes]


# Add the predicted class column to the combined probabilities DataFrame
combined_probs_df['Predicted_Class'] = predicted_labels

# Print the combined probabilities DataFrame with the predicted class

print(combined_probs_df)
