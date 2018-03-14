import numpy as np
import pandas as pd
import statsmodels.api as sm
import random

iris = pd.read_csv('iris.csv',sep=',', header=0)
iris.columns = [heading.lower() for heading in \
                iris.columns.str.replace(".","_")]

iris['iris01'] = np.where(iris['name'] == 'Setosa',1.,0.)
# print(iris['iris01']) 1,0으로 setosa가 있으면 1 없으면 0

dependent_variable = iris['iris01']
independent_variables = iris[['sepallength','sepalwidth','petallength','petalwidth']]
independent_variables_with_constant = sm.add_constant(independent_variables, prepend=True)

logit_model = sm.Logit(dependent_variable, independent_variables_with_constant).fit_regularized()

new_observations = iris.ix[iris.index.isin(range(100)), independent_variables.columns]
new_observations_with_constant = sm.add_constant(new_observations, prepend=True)
# print(new_observations_with_constant) 선정된 인덱스값을 넣어주는 변수 설정

print("\n샘플링 데이터 예측 테스트")
print(new_observations_with_constant)
y_predicted = logit_model.predict(new_observations_with_constant)
y_predicted_rounded = [round(score, 2) for score in y_predicted]

index = 1
for pridicted_value in y_predicted_rounded:
    if pridicted_value == 1.0:
        print("%d번째 샘플링 데이터 예측 결과: Setosa 확실"%index)
    else:
        print("%d번째 샘플링 데이터 예측 결과: Setosa 아닌 다른 품종"%index)
    index+=1