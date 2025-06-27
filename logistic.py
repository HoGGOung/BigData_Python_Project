import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# 1. 데이터 로드 및 전처리
iris = load_iris()
X = iris.data
y = iris.target

# 이진 분류만 (클래스 0과 1)
binary_mask = y < 2
X_binary = X[binary_mask]
y_binary = y[binary_mask]

# 2. 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(X_binary, y_binary, test_size=0.2, random_state=42)

# 3. 모델 학습
model = LogisticRegression()
model.fit(X_train, y_train)

# 4. 모델평가
y_pred = model.predict(X_test)

# 정확도 평가
accuracy = accuracy_score(y_test, y_pred)
print("정확도:", accuracy)

# 5. 새로운 데이터 예측
new_data = [[5.0, 3.4, 1.5, 0.2]]  # 꽃받침 길이/너비, 꽃잎 길이/너비
prediction = model.predict(new_data)
print("\n새 데이터의 클래스 예측:", prediction)
flower_type = prediction[0]

if flower_type == 0:
    print("꽃은 setosa 종입니다")
else:
    print("꽃은 versicolor 종입니다")


#모델저장
import joblib
joblib.dump(model, "logistic_model.pkl")


#모델 사용
model = joblib.load("logistic_model.pkl")