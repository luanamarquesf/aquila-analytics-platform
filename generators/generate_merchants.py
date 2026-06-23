from faker import Faker
import pandas as pd
import random
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

output_file = BASE_DIR / "data" / "raw" / "merchants.parquet"

fake = Faker("pt_BR")

segments = [
    "Padaria",
    "Restaurante",
    "Mercado",
    "Farmácia",
    "Posto",
    "Loja de Roupa",
    "Academia"
]

merchants = []

for merchant_id in range(1, 101):

    merchants.append({
        "merchant_id": merchant_id,
        "name": fake.company(),
        "segment": random.choice(segments),
        "city": fake.city(),
        "state": fake.estado_sigla(),
        "created_at": fake.date_between(
            start_date="-5y",
            end_date="today"
        )
    })

df = pd.DataFrame(merchants)
df.to_parquet(
    output_file,
    index=False
)

print("Arquivo salvo com sucesso!")

print(df.head())