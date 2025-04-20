import pandas as pd
import matplotlib.pyplot as plt

def create_graph(df: pd.DataFrame,c1,c2):
    plt.figure(figsize=(10, 6))
    plt.bar(df[c1], df[c2],bottom=0)
    plt.title('Line Plot of Boxes Shipped by Country')
    plt.xlabel('Product')
    plt.ylabel('Country')
    plt.grid(False)
    plt.show()