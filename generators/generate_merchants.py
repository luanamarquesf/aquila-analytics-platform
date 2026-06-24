from faker import Faker
import pandas as pd
import random
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

output_file = BASE_DIR / "data" / "raw" / "merchants.parquet"

fake = Faker("pt_BR")

BRAZIL_LOCATIONS = [
    {"city": "São Paulo", "state": "SP"},
    {"city": "Campinas", "state": "SP"},
    {"city": "Santos", "state": "SP"},
    {"city": "São Bernardo do Campo", "state": "SP"},
    {"city": "Rio de Janeiro", "state": "RJ"},
    {"city": "Niterói", "state": "RJ"},
    {"city": "Belo Horizonte", "state": "MG"},
    {"city": "Uberlândia", "state": "MG"},
    {"city": "Curitiba", "state": "PR"},
    {"city": "Porto Alegre", "state": "RS"},
    {"city": "Salvador", "state": "BA"},
    {"city": "Recife", "state": "PE"},
    {"city": "Brasília", "state": "DF"},
]

segments = [
    "Padaria",
    "Restaurante",
    "Mercado",
    "Farmácia",
    "Posto",
    "Loja de Roupa",
    "Academia",
]

merchants = []

TOTAL_MERCHANTS = 100000

for merchant_id in range(1, TOTAL_MERCHANTS + 1):
    # Sorteia a localização combinada (Garante a consistência!)
    location = random.choice(BRAZIL_LOCATIONS)

    merchants.append(
        {
            "merchant_id": merchant_id,
            "name": fake.company(),
            "segment": random.choice(segments),
            "city": location["city"],
            "state": location["state"],
            "created_at": fake.date_between(start_date="-5y", end_date="today"),
        }
    )

df = pd.DataFrame(merchants)
df.to_parquet(
    output_file,
    index=False
)

print("Arquivo salvo com sucesso!")

print(df.head())