import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from xgboost import XGBClassifier,plot_importance

dataset = np.loadtxt('dataset/pima-indians-diabetes.csv', delimiter=',')

x = dataset[:, :8]
y = dataset[:, 8]
seed = 7
size = 0.33
x_train,x_test,y_train,y_test = train_test_split(x, y, test_size=size, random_state=seed)

# 通过不断添加小模型，监测loss值变化来看model的效果
model = XGBClassifier()
eval_set = [(x_test, y_test)]  # 每次添加模型时，都会用eval_set进行测试loss
model.fit(x_train, y_train, early_stopping_rounds=10, eval_metric='logloss', eval_set=eval_set, verbose=True)
# early_stopping_rounds，指定model经过多少次数没有提升就停止。 verbose显示每次加模型后的效果

pred = model.predict(x_test)
predictions = [round(value) for value in pred]
accuracy = accuracy_score(y_test, predictions)
print("Accuracy:%.2f%%" % (accuracy * 100.0))

# 各个特征的重要程度
model.fit(x, y)
plot_importance(model)
plt.show()

