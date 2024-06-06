from sklearn.tree import
DecisionTreeClassifier
x =[
    [1,0,1,0], # febre, tosse, congestao nasal, dor de garganta
    [0,1,0,1] # sem febre, tosse, sem congestao nasal, dor de garganta
    [1,1,1,0] # febre, tosse, congestao nasal, sem dor de garganta
    [0,1,1,1] # sem febre, tosse, congestao nasal, dor de garganta
    [0,0,1,1] # sem febre, sem tosse, congestao nasal, dor de garganta
    ]
y = ["gripe","resfriado comum","gripe","resfriado comum"]
clf = DecisionTreeClassifier
clf.fit(x,y)

print(clf.predict([[1,0,1,1]]))