from datetime import datetime
from pathlib import Path
import duckdb

BASE_DIR = Path(__file__).resolve().parent.parent

con = duckdb.connect()

con.execute(f"""
CREATE OR REPLACE VIEW merchants AS
SELECT *
FROM read_parquet('{BASE_DIR}/data/raw/merchants.parquet')
""")

con.execute(f"""
CREATE OR REPLACE VIEW transactions AS
SELECT *
FROM read_parquet('{BASE_DIR}/data/raw/transactions.parquet')
""")

sql_dir = BASE_DIR / "sql"
report = "# SQL Analytics Findings\n\n"

tpv = None
ticket_medio = None

ticket_segmento = None
tpv_city = None
card_brand_analysis = None

for sql_file in sorted(sql_dir.glob("*.sql")):

    query = sql_file.read_text(encoding="utf-8")

    result = con.sql(query).df()

    if sql_file.name == "tpv.sql":
        tpv = result.iloc[0]["tpv"]

    elif sql_file.name == "ticket_medio.sql":
        ticket_medio = result.iloc[0]["ticket_medio"]

    elif sql_file.name == "top_segments.sql":
        ticket_segmento = result

    elif sql_file.name == "top_cities.sql":
        tpv_city = result

    elif sql_file.name == "brand.sql":
        card_brand_analysis = result

tpv_city["tpv"] = (
    tpv_city["tpv"]
    .map(lambda x: f"R$ {x:,.2f}")
)

card_brand_analysis["tpv"] = (
    card_brand_analysis["tpv"]
    .map(lambda x: f"R$ {x:,.2f}")
)

ticket_segmento["tpv"] = (
    ticket_segmento["tpv"]
    .map(lambda x: f"R$ {x:,.2f}")
)

generated_at = datetime.now().strftime(
    "%Y-%m-%d %H:%M:%S"
)

report = f"""
# Analytics Findings

## General Metrics

- Total TPV: R$ {tpv:,.2f}
- Average Ticket: R$ {ticket_medio:,.2f}

## Average Ticket by Segment

{ticket_segmento.to_markdown(index=False)}

## TPV by State

{tpv_city.to_markdown(index=False)}

## Card Brand Analysis

{card_brand_analysis.to_markdown(index=False)}

---

Generated automatically by run_sql_analytics.py

Generated at: {generated_at}
"""

output_file = (
    BASE_DIR
    / "docs"
    / "sql_analytics_findings.md"
)

with open(output_file, "w", encoding="utf-8") as f:
    f.write(report)