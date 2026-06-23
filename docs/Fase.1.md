Sua Fase 1 deveria ser praticamente uma mistura de:

Modelagem de negócio
Modelagem de dados
SQL
Geração de dados sintéticos

Objetivo da Fase 1

Entendendo o Negócio: o que é uma adquirente?

Fluxo simplificado:

Cliente
↓
Cartão
↓
Maquininha
↓
Adquirente
↓
Bandeira
↓
Banco Emissor

Exemplo:

Cliente compra R$100

Visa aprova

Adquirente processa

Lojista recebe
Quais entidades existem?

Você vai modelar:

Merchant

O lojista

Exemplo:

{
  "merchant_id": 1,
  "name": "Padaria Central",
  "segment": "Padaria",
  "city": "Campinas"
}
Transaction

A venda

{
  "transaction_id": 1,
  "merchant_id": 1,
  "amount": 120.50
}
Settlement

Liquidação

{
  "settlement_id": 1,
  "transaction_id": 1,
  "amount_paid": 117.30
}
Anticipation

Antecipação de recebíveis

{
  "merchant_id": 1,
  "amount": 10000
}
Semana 1 — Modelagem Conceitual

Desenhe:

Merchant
│
├── Transactions
│
├── Settlements
│
└── Anticipations

Depois defina atributos.

Exemplo:

Merchant
id
name
segment
city
state
created_at
Transaction
id
merchant_id
amount
card_brand
installments
created_at

Entrega:

Um diagrama ER.

Semana 2 — Estrutura do Projeto

Criar repositório.

finsight-analytics-platform

Estrutura:

finsight/
│
├── docs/
│
├── data/
│
│   ├── raw/
│   ├── processed/
│
├── generators/
│
├── notebooks/
│
├── sql/
│
├── tests/
│
└── README.md

Instalar:

pip install pandas faker numpy pyarrow

Aprender:

Pandas
DataFrame
merge
groupby
pivot
Semana 3 — Gerador de Lojistas

Objetivo:

Gerar:

100.000 merchants

Campos:

merchant_id
name
segment
city
state
created_at

Segmentos:

Padaria
Restaurante
Mercado
Farmácia
Posto
Loja de Roupa
Academia

Salvar:

data/raw/merchants.parquet

Aprendizado:

Faker
Pandas
Parquet
Semana 4 — Gerador de Transações

Agora vem a parte importante.

Cada merchant gera vendas.

Exemplo:

merchant_id=1

2025-01-01
R$50

2025-01-01
R$120

2025-01-02
R$90

Criar:

1 milhão de transações

Inicialmente.

Depois aumentar.

Campos:

transaction_id
merchant_id
amount
card_brand
installments
transaction_date

Bandeiras:

Visa
Mastercard
Elo
Amex

Parcelas:

1x
2x
3x
6x
12x

Salvar:

transactions.parquet
Semana 5 — Regras de Negócio

Aqui o projeto começa a parecer real.

Exemplo:

Nem todos os segmentos vendem igual.

Restaurante

mais vendas à noite

Farmácia

mais vendas manhã

Academia

mais vendas início do mês

Mercado

mais vendas finais de semana

Você vai criar comportamento sintético.

Isso é extremamente importante para os modelos de ML depois.

Semana 6 — Construção do Data Mart Inicial

Criar consultas SQL.

Perguntas:

TPV
SELECT SUM(amount)
Ticket Médio
AVG(amount)
Top Segmentos
GROUP BY segment
Top Cidades
GROUP BY city

Objetivo:

Começar a pensar como analista de dados.

Entrega Final da Fase 1

Você deve ter:

Dados
merchants.parquet

transactions.parquet
Documentação
Arquitetura

Modelo ER

Regras de negócio
SQL

Consultas analíticas

Conhecimento adquirido

Você terá praticado:

✅ Python

✅ Pandas

✅ SQL

✅ Modelagem de Dados

✅ Conceitos de DW

✅ Dados sintéticos

✅ Regras de negócio financeiras

✅ Parquet

✅ Analytics básico

E o mais importante: terá criado a matéria-prima que será usada em todas as próximas fases (Kafka, Spark, Churn, Forecast, Fraude e IA). Se eu estivesse te mentorando, eu não deixaria você avançar para a Fase 2 antes de conseguir responder com segurança perguntas como "qual é o TPV por segmento?", "qual o ticket médio por cidade?" e "como os dados estão modelados?". Isso é a fundação de todo o restante.