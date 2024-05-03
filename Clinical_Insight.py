##########Clinical probabilities########################



# Load clinical features data from main_data.xlsx
clinical_data = pd.read_excel('main_dataset_up.xlsx', index_col=0)
X_test_df = pd.DataFrame(X_test)
clinical_data_test = clinical_data.iloc[X_test_df.index]
print(clinical_data.columns.tolist())

# Define clinical rules for each class
clinical_rules = {
    'BO': {'ALP_high': 0.8, 'Bilirubin_high': 0.8},
    'ACR': {'Age_of_graft_low': 0.6},
    'AH': {'ALT_higher_than_ALP': 0.7},
    'MASH': {'Age_of_graft_high': 0.7, 'BMI_high': 0.6},
    'HCV': {'ALT_higher_than_AST': 0.8 ,'Age_of_graft_low': 0.6 },
    'congestion': {'ALP_high': 0.8, 'INR_high': 0.8}
}


subject_probs = []

# Iterate through each row in the clinical data
for index, row in clinical_data_test.iterrows():
    # Initialize probabilities dictionary for the current subject
    subject_prob = {}

    # Set clinical features for the current subject
    clinical_features = {
        'ALP': row['ALK_PHOS'],
        'Bilirubin': row['BILT'],
        'ALT': row['ALT'],
        'AST': row['AST'],
        'BMI': row['BMI at tx'],
        'INR': row['INR'],
        'Age_of_graft': row['Age of graft in weeks']
    }
    total_prob = 0.0  # Total probability for normalization
    # Calculate probabilities for each class based on clinical rules
    for class_name, rules in clinical_rules.items():
        prob = 1.0
        for rule, rule_value in rules.items():
            if rule.endswith('_high'):
                if clinical_features.get(rule[:-5], 0) > 0:
                    prob *= rule_value
                else:
                    prob *= (1 - rule_value)
            elif rule.endswith('_low'):
                if clinical_features.get(rule[:-4], 0) < 0:
                    prob *= rule_value
                else:
                    prob *= (1 - rule_value)
            elif rule == 'ALT_higher_than_ALP':
                if clinical_features.get('ALT', 0) > clinical_features.get('ALP', 0):
                    prob *= rule_value
                else:
                    prob *= (1 - rule_value)
            elif rule == 'ALT_higher_than_AST':
                if clinical_features.get('ALT', 0) > clinical_features.get('AST', 0):
                    prob *= rule_value
                else:
                    prob *= (1 - rule_value)
            else:
                if clinical_features.get(rule, False):
                    prob *= rule_value
                else:
                    prob *= (1 - rule_value)
        total_prob += prob  # Accumulate probability for normalization
        subject_prob[class_name] = prob

        
    
    
    # Normalize probabilities for the current subject
    for class_name in subject_prob:
        subject_prob[class_name] /= total_prob
    
    
    # Append the probabilities for the current subject to the list
    subject_probs.append(subject_prob)

# Convert the list of probabilities into a DataFrame
subject_probs_df = pd.DataFrame(subject_probs)
