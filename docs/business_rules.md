# 📘 Glossário e Dicionário de Negócios (Adquirença)

Este documento centraliza as principais siglas, conceitos e indicadores do mercado de meios de pagamento e adquirença utilizados na regra de negócio da plataforma **Aquila**.

---

### 📊 Indicadores de Volume e Receita

* **TPV (Total Processed Volume - Volume Total Processado):** É a métrica rainha da adquirente. Representa a soma de todo o dinheiro bruto que passou pelas maquininhas ou gateways de pagamento em um determinado período. Se 10 clientes compram R$ 100, o TPV é R$ 1.000.
  
* **MDR (Merchant Discount Rate - Taxa de Desconto do Lojista):** É a taxa percentual que a adquirente cobra do lojista para processar uma venda (ex: 2% no débito, 4% no crédito). Se o MDR é 3% e o cliente compra R$ 100, o lojista recebe R$ 97 e a adquirente retém R$ 3.
  
* **MSC (Merchant Service Charge):** Termo sinônimo de **MDR**. É a nomenclatura mais utilizada internacionalmente para se referir à taxa cobrada do estabelecimento comercial.

* **Net Revenue (Receita Líquida da Adquirente):** É o lucro real que sobra para a adquirente após a divisão do bolo. A conta básica é: 
  $$\text{Net Revenue} = \text{MDR} - \text{Intercâmbio} - \text{Assessment}$$

---

### 🏛️ Custos de Interconexão (Bandeiras e Bancos)

* **Interchange Fee (Taxa de Intercâmbio):** É a fatia do MDR que a adquirente é obrigada a pagar para o **Banco Emissor** (o banco que emitiu o cartão do cliente). Serve para remunerar o banco pelo risco de crédito e inadimplência. Quem dita essa taxa é a bandeira.
  
* **Assessment Fee (Taxa da Bandeira):** É uma mini-taxa fixa cobrada pela **Bandeira** (Visa, Mastercard, Elo) por cada transação processada utilizando a sua rede de arranjo de pagamento. Também é deduzida do MDR cobrado do lojista.

---

### 💸 Fluxo Financeiro e Crédito

* **Settlement (Liquidação):** O ato físico e financeiro de pagar o lojista. É o agendamento e o depósito do dinheiro da venda (já descontado o MDR) na conta bancária do estabelecimento comercial, respeitando os prazos acordados (ex: D+1 para débito, D+30 para crédito).
  
* **Anticipation (Antecipação de Recebíveis):** Um serviço de crédito onde o lojista escolhe receber hoje o valor de vendas que só seriam pagas no futuro (como as parcelas de uma venda em 12x). A adquirente cobra uma taxa de juros (taxa de antecipação) por esse adiantamento.

---

### ⚠️ Risco e Operações

* **Chargeback (Contestação de Venda):** Ocorre quando o portador do cartão entra em contato com o banco emissor dizendo que não reconhece a compra ou que sofreu uma fraude. O dinheiro é estornado para o cliente e retirado do lojista. É o principal indicador de risco e fraude em adquirença.
  
* **Capture Rate (Taxa de Captura):** A porcentagem de transações iniciadas que foram concluídas com sucesso absoluto. É uma métrica técnica que ajuda a monitorar a estabilidade das maquininhas e gateways.

---

### 💻 Infraestrutura de Mercado

* **Gateway de Pagamentos:** A tecnologia que faz a ponte de comunicação entre um e-commerce (loja virtual) e as adquirentes. É a "maquininha de cartão" do mundo digital.
  
* **Subadquirente:** Empresas que intermediam pagamentos entre pequenos lojistas e as grandes adquirentes (ex: plataformas de e-commerce ou carteiras digitais no início de suas operações). Elas facilitam o credenciamento do lojista, mas rodam sob a infraestrutura técnica de uma adquirente principal.