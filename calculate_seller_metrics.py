import pandas as pd

# Загрузка данных из файла
file_path = 'seller_data.csv'  # Укажите путь к вашему файлу
data = pd.read_csv(file_path, sep=',', encoding='utf-8')

# Отладка: вывод уникальных значений в столбцах 'Promotion_Used' и 'Subscription'
print("Уникальные значения в 'Promotion_Used':")
print(data['Promotion_Used'].unique())

print("\nУникальные значения в 'Subscription':")
print(data['Subscription'].unique())

# 1. Средний чек с каждой продажи
total_sales = data['Order_Value'].sum()
total_orders = len(data)
average_order_value = total_sales / total_orders

# 2. Средняя комиссия с каждой продажи
average_commission_rate = data['Commission_Rate'].mean()
average_commission_per_sale = average_order_value * average_commission_rate

# 3. Средний доход с продавца за весь срок взаимодействия
data['Total_Income_Per_Seller'] = (
    data['Promotion_Income'] + data['Subscription_Income'] + (data['Order_Value'] * data['Commission_Rate'])
)
average_income_per_seller = data['Total_Income_Per_Seller'].mean()

# 4. Процент продавцов, использующих платные инструменты продвижения
promotion_users_percentage = (data['Promotion_Used'].sum() / len(data)) * 100

# 5. Процент продавцов, использующих платную подписку
subscription_users_percentage = (data['Subscription'].sum() / len(data)) * 100

# 6. Расчёт процентного соотношения со средним чеком
commission_percentage_of_order = (average_commission_per_sale / average_order_value) * 100
promotion_percentage_of_order = (data['Promotion_Income'].sum() / total_sales) * 100
subscription_percentage_of_order = (data['Subscription_Income'].sum() / total_sales) * 100

# Вывод результатов
print(f"\nСредний чек с каждой продажи: {average_order_value:.2f} руб.")
print(f"Средняя комиссия с каждой продажи: {average_commission_per_sale:.2f} руб.")
print(f"Средний доход продавца: {average_income_per_seller:.2f} руб.")
print(f"Процент продавцов с продвижением: {promotion_users_percentage:.2f}%")
print(f"Процент продавцов с подпиской: {subscription_users_percentage:.2f}%")
print(f"Комиссия (% от чека): {commission_percentage_of_order:.2f}%")
print(f"Продвижение (% от чека): {promotion_percentage_of_order:.2f}%")
print(f"Подписка (% от чека): {subscription_percentage_of_order:.2f}%")
