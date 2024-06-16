import matplotlib as mpl 
import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np
import seaborn as sb
import seaborn.objects as ob

df = sb.load_dataset("penguins")
sb.pairplot(df, hue="species")

plt.show()