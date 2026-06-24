import os
import random
from datetime import datetime, timedelta
from pathlib import Path
from faker import Faker
import numpy as np
import pandas as pd
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

from utils.helpers import calculate_installments_options

fake = Faker("pt_BR")

BASE_DIR = Path(__file__).resolve().parent.parent

merchants = pd.read_parquet(BASE_DIR / "data" / "raw" / "merchants.parquet")

SEGMENT_RULES = {
    "Padaria": (5, 50),
    "Restaurante": (20, 250),
    "Mercado": (50, 400),
    "Farmácia": (15, 150),
    "Posto": (100, 500),
    "Loja de Roupa": (80, 600),
    "Academia": (100, 350),
}

card_brands = ["Visa", "Mastercard", "Elo", "Amex"]
installments_options = [1, 2, 3, 6, 12]

NUM_TRANSACTIONS = 1000000
transactions = []

print("Sorteando lojistas em lote para máxima performance...")
sampled_merchants = merchants.sample(
    NUM_TRANSACTIONS, replace=True
).to_dict(orient="records")

print("Gerando transações...")
for transaction_id, merchant in enumerate(sampled_merchants, start=1):
    segment = merchant["segment"]
    min_amt, max_amt = SEGMENT_RULES[segment]

    amount = round(random.uniform(min_amt, max_amt), 2)
    installments = calculate_installments_options(amount)


    merchant_created_at = pd.to_datetime(merchant["created_at"])
    days_since_creation = (datetime.now() - merchant_created_at).days
    if days_since_creation <= 0:
        days_since_creation = 1

    random_days = random.randint(0, days_since_creation)
    transaction_date = merchant_created_at + timedelta(days=random_days)

    transactions.append(
        {
            "transaction_id": transaction_id,
            "merchant_id": merchant["merchant_id"],
            "amount": amount,
            "card_brand": random.choice(card_brands),
            "installments": installments, 
            "transaction_date": transaction_date.strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
        }
    )

print("Convertendo para DataFrame...")
df_transactions = pd.DataFrame(transactions)

output_file = BASE_DIR / "data" / "raw" / "transactions.parquet"
output_file.parent.mkdir(parents=True, exist_ok=True)

df_transactions.to_parquet(output_file, index=False, engine="pyarrow")
print(f"Sucesso! Salvo em: {output_file}")
print(f"Formato dos dados: {df_transactions.shape}")
