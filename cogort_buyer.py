import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Загрузка данных из файла CSV
file_path = 'buyer_cohort_analysis_data.csv'
data = pd.read_csv(file_path)

# Преобразование столбца registration_date в формат даты
data['registration_date'] = pd.to_datetime(data['registration_date'])

# Создание столбцов с именами месяцев активности
activity_columns = ['activ_1_month', 'activ_3_month', 'activ_6_month', 'activ_12_month']

# Расчет общего числа пользователей, зарегистрированных в каждом месяце
data['registration_month'] = data['registration_date'].dt.to_period('M')
cohort_sizes = data.groupby('registration_month').size()

# Расчет удержания пользователей
retention = data.groupby('registration_month')[activity_columns].mean()

# Преобразование в проценты
retention = retention.multiply(100)

# Создание тепловой карты
plt.figure(figsize=(12, 8))
sns.heatmap(retention, annot=True, fmt=".1f", cmap='YlGnBu', cbar_kws={'label': 'Удержание (%)'})
plt.title('Тепловая карта удержания пользователей')
plt.ylabel('Месяц регистрации')
plt.xlabel('Период активности')
plt.yticks(rotation=0)
plt.xticks(rotation=45)
plt.show()