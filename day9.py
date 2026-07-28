import seaborn as sns
import matplotlib.pyplot as plt

tips=sns.load_dataset("tips")
print(tips.head())
corr=tips.corr(numeric_only=True)
#sns.countplot(data=tips,x="day")
#sns.barplot(data=tips,y="total_bill",x="day")
#sns.histplot(data=tips,x="total_bill")
#sns.scatterplot(data=tips,x="total_bill",y="tip",hue="smoker")
#sns.boxplot(data=tips,x="day",y="total_bill")
#sns.heatmap(corr,annot=True,cmap="coolwarm")
plt.show()