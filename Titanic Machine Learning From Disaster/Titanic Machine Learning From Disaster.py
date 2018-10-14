import pandas
import numpy

# ************training*************

df = pandas.read_csv(r'C:\Users\pc\Desktop\Titanic Machine Learning From Disaster\train.csv', header =0)
cols = ['Ticket', 'Name' , 'Cabin' ]
df = df.drop ( cols , axis = 1 )
l = []
cols = ['Sex', 'Pclass', 'Embarked']
for col in cols:
    l.append( pandas.get_dummies( df[col]))
dum = pandas.concat( l , axis=1)
df = pandas.concat( [df, dum], axis =1)
df = df.drop( cols , axis=1)
df['Age'] = df['Age'].interpolate()

y = df['Survived'].values

x = df.values
x = numpy.delete( x, 1, axis=1 )


from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split( x, y ,test_size=0.3,random_state=0)

from sklearn import tree
clf = tree.DecisionTreeClassifier(max_depth=5)

clf.fit(x_train, y_train)
print(clf.score(x_test , y_test) )


# put all test data into fit
#clf.fit(x, y)

# ***********working on test***************

df = pandas.read_csv(r'C:\Users\pc\Desktop\Titanic Machine Learning From Disaster\test.csv', header =0)
cols = ['Ticket', 'Name' , 'Cabin' ]
df = df.drop ( cols , axis = 1 )
l = []
cols = ['Sex', 'Pclass', 'Embarked']
for col in cols:
    l.append( pandas.get_dummies( df[col]))
dum = pandas.concat( l , axis=1)
df = pandas.concat( [df, dum], axis =1)
df = df.drop( cols , axis=1)

#to see if there are nans
print( df.info())

#interpolate missing values
df['Age'] = df['Age'].interpolate()
df['Fare'] = df['Fare'].interpolate()

x = df.values
	       
y = clf.predict(x)
	
print(y)

#to upload csv file to kaggle
output = numpy.column_stack( ( x[:,0], y) )
df_results = pandas.DataFrame(output.astype('int'),columns=['PassengerID','Survived'])
df_results.to_csv(r'C:\Users\pc\Desktop\titanic_results.csv',index=False)

print( " hello world \n") 





