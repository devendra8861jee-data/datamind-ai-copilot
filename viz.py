import matplotlib.pyplot as plt
import seaborn as sns

def plot_chart(df):
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns

    if len(numeric_cols) >= 2:
        plt.figure()
        sns.scatterplot(data=df, x=numeric_cols[0], y=numeric_cols[1])
        plt.title("Data Visualization")
        return plt
    return None