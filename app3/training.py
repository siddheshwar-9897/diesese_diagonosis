import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix,classification_report,accuracy_score


df=pd.read_csv(r'C:\\Users\\91932\\OneDrive\\Desktop\\d jango\\kideny\\app3\\ckd_clean.csv')
print(df.head())
print(df.info())
print(df.shape)
print(df.describe())
print(df.duplicated().sum())


#Analysis
print(df.isna().sum())
print(df.nunique().sort_values())
sns.countplot(x='Class',data=df)


"""feature selection =>Manual"""
x=df.drop(['Age','Class'],axis=1)

##data=data.dropna()
print(type(x))

y=df['Class']
print(type(y))


from sklearn.model_selection import train_test_split
x_train, x_test ,y_train, y_test = train_test_split(x,y,test_size=0.20,random_state=1234)


#svcclassifier = SVC()



#from sklearn.ensemble import RandomForestClassifer
from sklearn.svm import SVC
svcclassifer=SVC()



svcclassifer.fit(x_train,y_train)
y_pred = svcclassifer.predict(x_test)
print(y_pred)


print("="*40)
print("==========")
print("classification report :",(classification_report(y_test,y_pred)))
print("Accuracy :",accuracy_score(y_test,y_pred))
accuracy = accuracy_score(y_test,y_pred)
print("Accuracy:%.2f%%" % (accuracy*100.0))



#CONFUSION MATRIX
conf_matrix=confusion_matrix(y_test,y_pred)
print("==========")
print("confusion matrix : \n",conf_matrix)


#plot the confusion matrix

plt.figure(figsize=(10,7))
sns.heatmap(conf_matrix,annot=True,fmt='d',cmap='Blues')
plt.xlabel=('predicted')
plt.ylabel=('Actual')
plt.title('confusion matrix')
plt.show()


from joblib import dump
dump(svcclassifer,"model.joblinb")
print("Model saved as model.joblib")

