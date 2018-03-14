import numpy as np
import pandas as pd
import statsmodels.api as sm
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split

iris = pd.read_csv('iris.csv',sep=',', header=0)
iris.columns = [heading.lower() for heading in \
                iris.columns.str.replace(".","_")]

iris['iris01'] = np.where(iris['name'] == 'Iris-versicolor',1.,0.)
# print(iris['iris01']) 1,0으로 setosa가 있으면 1 없으면 0

dependent_variable = iris['iris01']
independent_variables = iris[['sepallength','sepalwidth','petallength','petalwidth']]
independent_variables_with_constant = sm.add_constant(independent_variables, prepend=True)

logit_model = sm.Logit(dependent_variable, independent_variables_with_constant).fit_regularized()

# new_observations = iris.ix[iris.index.isin(range(100)), independent_variables.columns]
# new_observations_with_constant = sm.add_constant(new_observations, prepend=True)

train_data, test_data, train_label, test_label = \
train_test_split(independent_variables, dependent_variable)
# train_test_split(independent_variables_with_constant, dependent_variable)

# 데이터 학습시키고 예측하기 --- (※4)
logit_model = sm.Logit(dependent_variable, independent_variables_with_constant).fit_regularized()
y_predicted = logit_model.predict(test_data)
# y_predicted_rounded = [round(score, 2) for score in y_predicted]

# 정답률 구하기 --- (※5)
ac_score = metrics.accuracy_score(test_label, y_predicted)
# print("전체 데이터 수: %d" %(len(iris)))
# print("학습 전용 데이터 수: %d" %(len(train_data)))
# print("테스트 데이터 수: %d" %(len(test_data)))
# print("정답률 =", ac_score)

# print(new_observations_with_constant) 선정된 인덱스값을 넣어주는 변수 설정

# print("\n샘플링 데이터 예측 테스트")
# print(new_observations_with_constant)
# y_predicted = logit_model.predict(new_observations_with_constant)
# y_predicted_rounded = [round(score, 2) for score in y_predicted]

# index = 1
# for pridicted_value in y_predicted_rounded:
#     if pridicted_value == 1.0:
#         print("%d번째 샘플링 데이터 예측 결과: Setosa 확실"%index)
#     else:
#         print("%d번째 샘플링 데이터 예측 결과: Setosa 아닌 다른 품종"%index)
#     index+=1