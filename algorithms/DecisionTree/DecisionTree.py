import csv
from sklearn.feature_extraction import DictVectorizer
from sklearn import preprocessing
from sklearn import tree
from sklearn.externals.six import StringIO

allData = open(r"D:/DATA/ML/buyersDTree.csv")
reader = csv.reader(allData)
headers = reader.next()
print(headers)

featureList = []
labelList = []

for row in reader:
    labelList.append(row[len(row) - 1])
    rowDict = {}
    for i in range(1,len(row) - 1):
        rowDict[headers[i]] = row[i]
    featureList.append(rowDict)
print(featureList)

# make feature's values transform matrix
vec = DictVectorizer()
dummyX = vec.fit_transform(featureList).toarray()
print("dummyX: ")
print(str(dummyX))
print(vec.get_feature_names())

lb = preprocessing.LabelBinarizer()
dummyY = lb.fit_transform(labelList)
print("dummyY: ")
print(str(dummyY))

clf = tree.DecisionTreeClassifier(criterion='entropy')
clf = clf.fit(dummyX,dummyY)
print ("clf:" + str(clf))

# output result to .dot
with open("allElectronicInformationGainDri.dot",'w') as f:
    f = tree.export_graphviz(clf,feature_names = vec.get_feature_names(),out_file = f)