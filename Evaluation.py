

#####AUC metrics#########

auc_scores_combined = []
conf_matrices_combined = []
from sklearn.preprocessing import LabelEncoder



# Calculate AUC and confusion matrix for each category
class_labels = ['BO', 'AH','ACR', 'MASH', 'HCV', 'Congestion']

for i, label in enumerate(class_labels):
    # Calculate AUC using combined probabilities
    auc_combined = roc_auc_score(y_test[:, i], combined_probs_df.iloc[:, i])
    auc_scores_combined.append(auc_combined)

    print(f"Category {label} - AUC with combined probabilities: {auc_combined}")
    
