import pandas as pd

# Загрузка данных из файла
file_path = 'seller_data.csv'
df = pd.read_csv(file_path)

# Данные о затратах
marketing_expenses = 3000000  # в рублях
avg_buyers_per_month = 2000
avg_sellers_per_month = 500
operational_expenses = 1500000  # в рублях
seller_service_cost = 1000  # на каждого продавца
retention_buyers = 0.20  # 20% удержание покупателей
retention_sellers = 0.40  # 40% удержание продавцов
avg_months_interaction_buyers = 24  # Средняя продолжительность взаимодействия с покупателями (в месяцах)
avg_months_interaction_sellers = 18  # Средняя продолжительность взаимодействия с продавцами (в месяцах)


# Расчет CAC для покупателей
CAC = marketing_expenses / avg_buyers_per_month
print(f"CAC (Стоимость привлечения покупателя): {CAC:.2f} рублей")

CAC_sellers = marketing_expenses / avg_sellers_per_month
print(f"CAC (Стоимость привлечения продавцов): {CAC_sellers:.2f} рублей")



# Расчет среднего дохода с одного покупателя
df['Average_Income_per_Buyer'] = df['Order_Value'] * df['Commission_Rate']
average_income_per_buyer = df['Average_Income_per_Buyer'].mean()

#average_income_per_buyer = df['Order_Value'].sum()
# Расчет LTV для покупателей
LTV_buyers = average_income_per_buyer * avg_months_interaction_buyers * retention_buyers
print(f"LTV покупателя: {LTV_buyers:.2f} рублей")

# Расчет среднего дохода с одного продавца
df['Average_Income_per_Seller'] = (
    df['Promotion_Income'] + df['Subscription_Income'] + (df['Order_Value'] * df['Commission_Rate'])
)
average_income_per_seller = df['Average_Income_per_Seller'].mean()

# Расчет LTV для продавцов
LTV_sellers = (average_income_per_seller - seller_service_cost) * avg_months_interaction_sellers * retention_sellers
print(f"LTV продавца: {LTV_sellers:.2f} рублей")



# Расчет ROI для покупателей и продавцов

ROI_buyers = (LTV_buyers-CAC)/CAC;
ROI_sellers = (LTV_sellers-CAC_sellers)/CAC_sellers;

# Расчет ROI

print(f"ROI продавцов: {ROI_buyers:.2f}")
print(f"ROI_покупателейellers: {ROI_sellers:.2f}")

# Вывод проблемных зон и оптимизаций
if CAC > LTV_buyers:
    print("Проблема: Стоимость привлечения покупателя (CAC) выше его LTV. Необходимо оптимизировать маркетинг.")
#if total_revenue < total_expenses:
#    print("Проблема: Общие доходы ниже расходов. Необходимо увеличить LTV или снизить затраты.")

# Оптимизация CAC и увеличение LTV:
# Возможные направления:
# 1. Повышение удержания клиентов
# 2. Оптимизация маркетинговых расходов
# 3. Увеличение доходности от подписки или комиссий
