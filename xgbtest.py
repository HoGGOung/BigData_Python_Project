import xgboost as xgb
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

# 1. 데이터 로드
data = fetch_california_housing()
X = data.data
y = data.target

# 2. 학습/테스트 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. DMatrix로 변환 (XGBoost 고유 포맷, 선택사항)
dtrain = xgb.DMatrix(X_train, label=y_train)
dtest = xgb.DMatrix(X_test, label=y_test)

# 4. 모델 하이퍼파라미터 설정
params = {
    'objective': 'reg:squarederror',  # 회귀 문제
    'max_depth': 6,
    'eta': 0.1,  # 학습률
    'eval_metric': 'rmse'
}

# 5. 모델 학습
evallist = [(dtrain, 'train'), (dtest, 'eval')]
model = xgb.train(params, dtrain, num_boost_round=100, evals=evallist, early_stopping_rounds=10)

# 6. 예측
y_pred = model.predict(dtest)

# 7. 평가
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print(f"MSE: {mse:.4f}")
print(f"RMSE: {rmse:.4f}")
print(f"R^2 Score: {r2:.4f}")


#8 모델 저장
model.save_model("xgb_california_model.json")  
print("모델이 'xgb_california_model.json' 파일로 저장되었습니다.")