import pandas as pd
import matplotlib.pyplot as plt


#Reading test and training set
train_df=pd.read_csv('mitbih_train.csv',header=None)
test_df=pd.read_csv('mitbih_test.csv',header=None)


#since dataset is unblanced need to be balanced
# train_df[187]=train_df[187].astype(int)
# equilibre=train_df[187].value_counts()

#balncing
from sklearn.utils import resample
df_1=train_df[train_df[187]==1]
df_2=train_df[train_df[187]==2]
df_3=train_df[train_df[187]==3]
df_4=train_df[train_df[187]==4]

df_0=(train_df[train_df[187]==0]).sample(n=20000,random_state=42)
df_1_upsample=resample(df_1,replace=True,n_samples=20000,random_state=123)
df_2_upsample=resample(df_2,replace=True,n_samples=20000,random_state=124)
df_3_upsample=resample(df_3,replace=True,n_samples=20000,random_state=125)
df_4_upsample=resample(df_4,replace=True,n_samples=20000,random_state=126)

train_df=pd.concat([df_0,df_1_upsample,df_2_upsample,df_3_upsample,df_4_upsample])


#Training set
X_train=train_df.iloc[:,:186].values
X_test=test_df.iloc[:,:186].values

X_train = X_train.reshape(X_train.shape[0],-1)
X_test = X_test.reshape(X_test.shape[0],-1)
#label
y_train=train_df[187]
y_test=test_df[187]


#svm
'''It has score of 94% accuracy'''
##from sklearn.svm import SVC
##
##from sklearn.model_selection import GridSearchCV
##clf = GridSearchCV(SVC(gamma='auto'),
##                   {'C':[1,10,100],
##                    'kernal':['rbf','linear'],                       
##                   },cv=5,return_train_score=False)
##clf.fit(X_train,y_train)
##
##clf.best_score_
##clf.best_params_

#Random forest Classifier
#99% accuracy
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()

##from sklearn.model_selection import cross_val_score
##print(cross_val_score(model, X_train, y_train, cv=3, scoring="accuracy"))




