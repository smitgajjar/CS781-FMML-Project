CS781 Project File submission

Tool: Synplicate

As per project report, to simulate the described cases, following folders contain the required files:
1. Car - Decision Tree Classifier verification (Decision Tree classifier model- "clf_gini")
2. CarNN - Nerual Network trained on publicly available data (Nerual Network model- "mlp_model_carNN")
3. CarNNBais1 - Nerual Network trained on induced bias (Nerual Network model- "mlp_model_carNNBias1DR")

Steps:
1. Copy the above directories into examples folder of synplicate tool
2. Change the maximum explainability weight on line 271 in synthesizer/max_sat/dd_encoder.py  to 6 (refer Synplicate readme for further instructions)
3. Run synplicate as follows "python3 synplicate.py examples/CarNN"
