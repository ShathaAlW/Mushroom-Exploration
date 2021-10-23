import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


df = pd.read_csv("mushroom_data.csv")
print(df.head())


# a function to avoid plotting percentages that are less than 2% on pie charts
def my_autopct(wedge_size):
  return ('%0.1f%%' % wedge_size) if wedge_size > 2 else ''


# list of all column headers
columns = df.columns.tolist()


# if column has only one variable, there is no point of plotting it
# if column has more than 6 variables, plot it using a bar chart
# if column has 6 or less variables, plot it using a pie chart

for column in columns:
  if (len(df[column].unique())) == 1:
    continue
  if (len(df[column].unique())) > 6:
     sns.countplot(df[column], order= df[column].value_counts().index, palette= "Set2")
     plt.title(column + " Value Counts")
     plt.xticks(rotation= 30, fontsize= 10)
     plt.xlabel(column, fontsize=12)
     plt.show()
     plt.clf()
  else:
    wedge_size = df[column].value_counts(normalize= True)
    wedge_label = df[column].value_counts().index.tolist()
    wedge_color = ['#b8a9c9', '#eeac99', '#5b9aa0', '#622569', '#f9d5e5', '#e06377']
    plt.pie(wedge_size, colors= wedge_color, autopct= my_autopct)
    plt.title(column + " Value Counts", fontsize= 12)
    plt.legend(labels = wedge_label, loc= 1)
    plt.axis('equal')
    center_circle = plt.Circle((0,0), 0.70, fc= 'white')
    fig = plt.gcf()
    fig.gca().add_artist(center_circle)
    plt.show()
    plt.clf()
