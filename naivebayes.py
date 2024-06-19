import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("darkgrid")

data = pd.read_csv("Breast_cancer_data.csv")
data.head(10)

data["diagnosis"].hist()