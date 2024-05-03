GraftIQ:  Multiclass Neural Network Model for Predicting Multiple Diagnosis Categories in Liver Transplant Recipients

GraftIQ is a predictive model designed to forecast multiple diagnosis categories using a combination of clinical insight and multiclass neural networks (NN). This repository contains the implementation of the GraftIQ model, as well as associated files for clinical insight computation, evaluation, feature importance analysis, and result visualization.

File Structure

multiclassNNmodel.py: This main file contains the implementation of the multiclass neural network model for predicting diagnosis categories.
Clinical_Insight.py: This file includes the computation of clinical probabilities, providing insights into the diagnosis predictions.
Evaluation.py: The Evaluation file contains scripts for evaluating the performance of the GraftIQ model and generating result illustrations.
Integrated_Gradient_Feature_Importance.py: This file contains scripts for analyzing feature importance using integrated gradients.
Pie_Chart_RiskofInjury.py: The Pie Chart file contains scripts for visualizing the risk of injury predictions using pie charts.
Bayesian_Fusion.py: This file implements the Bayesian fusion technique to combine probabilities from the multiclass NN and clinical insight models.
Usage

To utilize the GraftIQ model and associated functionalities, follow these steps:

Run multiclassNNmodel.py to train and deploy the multiclass neural network model.
Execute Clinical_Insight.py to compute clinical probabilities and gain insights into diagnosis predictions.
Implement Bayesian fusion of probabilities from the multiclass NN and clinical insight models with Bayesian_Fusion.py.
Use Evaluation.py to evaluate the performance of the GraftIQ model and visualize the results.
Analyze feature importance by running Integrated_Gradient_Feature_Importance.py.
Generate pie charts depicting the risk of injury predictions using Pie_Chart_RiskofInjury.py.
