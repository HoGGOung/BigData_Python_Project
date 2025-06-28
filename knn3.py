from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 한글 폰트 설정 (Windows: 맑은 고딕)
plt.rcParams['font.family'] = 'Malgun Gothic'     # Mac은 'AppleGothic', Linux는 'NanumGothic'
plt.rcParams['axes.unicode_minus'] = False        # 마이너스 부호 깨짐 방지

# 데이터 준비
X, y = make_regression(n_samples=100, n_features=1, noise=15, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 다양한 K값으로 MSE 비교
k_values = [1, 3, 5, 7, 9, 11, 15, 20]
mse_scores = []

print("=== 다양한 K값에 따른 MSE 비교 ===")
for k in k_values:
    knn_reg = KNeighborsRegressor(n_neighbors=k)
    knn_reg.fit(X_train, y_train)
    y_pred = knn_reg.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    mse_scores.append(mse)
    print(f"K={k}: MSE={mse:.2f}")

# 최적 K값 찾기
best_k = k_values[np.argmin(mse_scores)]
print(f"\n최적 K값: {best_k} (MSE: {min(mse_scores):.2f})")

# 최적 모델로 재훈련
best_knn = KNeighborsRegressor(n_neighbors=best_k)
best_knn.fit(X_train, y_train)
y_pred_best = best_knn.predict(X_test)

print(f"\n=== 최적 모델 성능 ===")
print(f"최적 K={best_k}일 때 MSE: {mean_squared_error(y_test, y_pred_best):.2f}")

# 시각화
plt.figure(figsize=(12, 4))

# K값에 따른 MSE 변화
plt.subplot(1, 2, 1)
plt.plot(k_values, mse_scores, 'bo-')
plt.xlabel('K값')
plt.ylabel('MSE')
plt.title('K값에 따른 MSE 변화')
plt.grid(True)

# 예측 결과 시각화
plt.subplot(1, 2, 2)
plt.scatter(X_test, y_test, color='blue', alpha=0.6, label='실제값')
plt.scatter(X_test, y_pred_best, color='red', alpha=0.6, label='예측값')
plt.xlabel('X')
plt.ylabel('y')
plt.title(f'K={best_k}일 때 예측 결과')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
