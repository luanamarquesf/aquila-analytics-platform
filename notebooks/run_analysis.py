import pandas as pd
from pathlib import Path

print("\n=== [1/4] Carregando dados de forma otimizada ===")

BASE_DIR = Path(__file__).resolve().parent.parent

merchants = pd.read_parquet(BASE_DIR / "data" / "raw" / "merchants.parquet",  columns=["merchant_id", "segment", "state"])
transactions = pd.read_parquet(
    BASE_DIR / "data" / "raw" / "transactions.parquet", 
    columns=["merchant_id", "amount", "card_brand"]
)

print(f"-> Transações carregadas: {transactions.shape[0]:,}")
print(f"-> Lojistas carregados: {merchants.shape[0]:,}")

print("\n=== [2/4] Cruzando as tabelas (Merge) ===")
df = transactions.merge(merchants, on="merchant_id", how="left")

print("\n=== [3/4] Calculando Métricas Gerais ===")
tpv_total = df["amount"].sum()
ticket_medio = df["amount"].mean()

print(f"   TPV Total: R$ {tpv_total:,.2f}")
print(f"   Ticket Médio Geral: R$ {ticket_medio:,.2f}")

print("\n=== [4/4] Agrupamentos (Resultados) ===")

print("\n--- TICKET MÉDIO POR SEGMENTO ---")
ticket_segmento = df.groupby("segment")["amount"].mean().reset_index().rename(columns={"amount": "ticket_medio"})
print(ticket_segmento.to_string(index=False))

print("\n--- TPV POR ESTADO ---")
tpv_estado = df.groupby("state")["amount"].sum().reset_index().rename(columns={"amount": "tpv"}).sort_values(by="tpv", ascending=False)
print(tpv_estado.to_string(index=False))

print("\n--- VOLUMETRIA POR BANDEIRA ---")
analise_bandeira = df.groupby("card_brand")["amount"].agg(qtd_transacoes="count", tpv_total="sum").reset_index()
print(analise_bandeira.to_string(index=False))

print("\n=== Análise concluída com sucesso! ===\n")

report = f"""
# Analytics Findings

## General Metrics

- Total TPV: R$ {tpv_total:,.2f}
- Average Ticket: R$ {ticket_medio:,.2f}

## Average Ticket by Segment

{ticket_segmento.to_markdown(index=False)}

## TPV by State

{tpv_estado.to_markdown(index=False)}

## Card Brand Analysis

{analise_bandeira.to_markdown(index=False)}

---
Generated automatically by run_analysis.py
"""

output_file = BASE_DIR / "docs" / "analytics_findings.md"

with open(output_file, "w", encoding="utf-8") as f:
    f.write(report)

print(f"Relatório salvo em: {output_file}")