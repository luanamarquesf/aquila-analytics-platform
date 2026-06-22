# Aquila Analytics Platform

## Visão Geral

Aquila Analytics Platform é uma plataforma de inteligência financeira inspirada em adquirentes, fintechs e processadoras de pagamentos. O projeto simula uma operação completa de pagamentos utilizando dados sintéticos, permitindo a construção de um ecossistema de dados ponta a ponta.

O objetivo é desenvolver conhecimentos práticos em Engenharia de Dados, Ciência de Dados, Analytics e IA Generativa através da implementação de pipelines, modelos analíticos e produtos orientados por dados.

---

# FASE 1 — Fundamentos e Geração de Dados

## Objetivo

Construir a base do projeto, gerar dados sintéticos realistas e definir a modelagem inicial.

## Conhecimentos

* Python para dados
* Pandas
* NumPy
* Faker
* SQL básico e intermediário
* Modelagem de dados
* Conceitos de Data Warehouse

## Entregáveis

### Estrutura do Projeto

Criar a organização inicial:

* backend/
* data-generator/
* notebooks/
* docs/
* infrastructure/

### Geração de Clientes

Criar uma base sintética contendo:

* 100 mil lojistas
* Dados cadastrais
* Segmentos de atuação
* Localização
* Data de adesão

### Geração de Transações

Criar aproximadamente:

* 5 milhões de transações
* Bandeiras de cartão
* Parcelamentos
* Horários
* Valores
* Cidades

### Modelagem Inicial

Definir entidades:

* Merchant
* Transaction
* Settlement
* Anticipation
* Device

---

# FASE 2 — Engenharia de Dados

## Objetivo

Construir pipelines de ingestão e processamento de eventos.

## Conhecimentos

* Docker
* Docker Compose
* Kafka
* PostgreSQL
* Airflow
* Conceitos de streaming

## Entregáveis

### Infraestrutura Local

Subir via Docker:

* Kafka
* PostgreSQL
* Airflow

### Publicação de Eventos

Simular eventos:

* Venda realizada
* Estorno
* Antecipação
* Cadastro de cliente

### Consumo de Eventos

Criar consumidores responsáveis por:

* Ler eventos
* Validar dados
* Persistir dados

### Pipeline Automatizado

Fluxo:

Kafka → PostgreSQL → Data Lake

---

# FASE 3 — Data Warehouse

## Objetivo

Construir a camada analítica da plataforma.

## Conhecimentos

* Data Warehouse
* Star Schema
* dbt
* Analytics Engineering

## Entregáveis

### Dimensões

Criar:

* dim_merchant
* dim_date
* dim_city
* dim_segment
* dim_card_brand

### Fatos

Criar:

* fact_transactions
* fact_anticipations

### KPIs

Calcular:

* TPV
* Ticket Médio
* Receita
* Volume de Transações
* Crescimento Mensal

---

# FASE 4 — Dashboard Executivo

## Objetivo

Disponibilizar indicadores para análise de negócio.

## Conhecimentos

* Metabase
* BI
* Visualização de Dados

## Entregáveis

### Dashboard Operacional

Visualizações:

* Volume de transações
* Receita diária
* Ticket médio

### Dashboard Executivo

Indicadores:

* TPV
* Receita
* Crescimento
* Retenção
* Churn

### Dashboard por Segmento

Comparação entre:

* Restaurantes
* Mercados
* Farmácias
* Vestuário

---

# FASE 5 — Benchmark Inteligente

## Objetivo

Permitir comparação entre lojistas semelhantes.

## Conhecimentos

* Machine Learning
* Clustering
* PCA
* Segmentação

## Entregáveis

### Agrupamento de Clientes

Criar clusters considerando:

* Segmento
* Região
* Faturamento
* Frequência de vendas

### Benchmark

Comparar cada lojista com seus pares.

Exemplos:

* Crescimento
* Ticket médio
* Receita
* Frequência

### Insights

Gerar análises como:

"Seu faturamento está 15% abaixo da média de empresas semelhantes."

---

# FASE 6 — Predição de Churn

## Objetivo

Identificar clientes com risco de cancelamento.

## Conhecimentos

* Feature Engineering
* Classificação
* XGBoost
* Avaliação de Modelos

## Entregáveis

### Definição de Churn

Exemplo:

Cliente sem transações por 60 dias.

### Construção de Features

Criar variáveis como:

* TPV mensal
* Ticket médio
* Frequência
* Crescimento
* Uso de antecipação

### Treinamento

Treinar modelos:

* Logistic Regression
* Random Forest
* XGBoost

### API de Score

Disponibilizar endpoint:

/churn-score

Retornando:

* Probabilidade de churn
* Classificação de risco

---

# FASE 7 — Forecast de Fluxo de Caixa

## Objetivo

Prever comportamento financeiro futuro.

## Conhecimentos

* Séries Temporais
* Forecasting
* Prophet
* XGBoost para séries temporais

## Entregáveis

### Preparação dos Dados

Criar séries contendo:

* Receita diária
* Receita semanal
* Receita mensal

### Modelagem

Treinar previsões para:

* 30 dias
* 60 dias
* 90 dias

### Visualização

Exibir:

* Histórico
* Tendência
* Faixa de confiança

---

# FASE 8 — Detecção de Fraude

## Objetivo

Identificar transações anômalas.

## Conhecimentos

* Anomaly Detection
* Isolation Forest
* Machine Learning Não Supervisionado

## Entregáveis

### Simulação de Fraudes

Gerar eventos sintéticos:

* Valores fora do padrão
* Mudanças bruscas de localização
* Horários suspeitos

### Construção do Modelo

Treinar:

* Isolation Forest

Opcional:

* Autoencoders

### Sistema de Alertas

Classificar:

* Baixo risco
* Médio risco
* Alto risco

---

# FASE 9 — IA Generativa e Copiloto Financeiro

## Objetivo

Transformar dados em linguagem natural.

## Conhecimentos

* LLMs
* OpenAI API
* Prompt Engineering
* RAG

## Entregáveis

### Camada de Insights

Transformar métricas em explicações.

Exemplo:

* Queda de vendas
* Crescimento
* Mudança de comportamento

### Assistente Financeiro

Perguntas:

* Por que minhas vendas caíram?
* Como estou em relação ao mercado?
* Qual meu risco de churn?

### Recomendações

Gerar sugestões automáticas:

* Antecipação
* Campanhas
* Retenção
* Crescimento

### Copiloto Financeiro

Consolidar todos os módulos em uma interface conversacional baseada em IA.

---

# Resultado Final

Ao término do projeto, a plataforma deverá conter:

* Geração de dados sintéticos
* Streaming de eventos
* Data Lake
* Data Warehouse
* Dashboards executivos
* Benchmark inteligente
* Predição de churn
* Forecast financeiro
* Detecção de fraude
* Assistente financeiro com IA Generativa

O projeto demonstrará competências práticas em:

* Engenharia de Dados
* Analytics Engineering
* Ciência de Dados
* Machine Learning
* IA Generativa
* Arquitetura de Dados
* Engenharia de Software
