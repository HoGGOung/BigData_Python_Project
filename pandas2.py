import pandas as pd

path = "data_resource/employee_data.json"

df = pd.read_json(path)  # ✅ 올바른 함수
print(df.head())


sorted_df = df.sort_values(by="나이", ascending=False)
print(sorted_df)

# 부서별로 그룹화하여 나이의 평균 계산
grouped_df = df.groupby('부서')['나이'].mean()
print(grouped_df)


