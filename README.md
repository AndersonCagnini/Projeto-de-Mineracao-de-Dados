# 🔍 Análise de Doença Cardíaca com Mineração de Dados

Este projeto aplica técnicas de **mineração de dados** para prever a presença de **doença cardíaca** com base em características clínicas de pacientes.

## 🧠 Objetivo

Aplicar modelos de classificação supervisionada em um conjunto de dados clínicos para prever a presença de doenças cardíacas, com foco no uso do algoritmo **Random Forest**.

## 📌 Resumo Executivo

Neste projeto, foram aplicadas técnicas de mineração de dados para prever a presença de doenças cardíacas em pacientes. O modelo **Random Forest** apresentou os melhores resultados, com acurácia de **98%** e **AUC de 0.94**. Variáveis clínicas como **tipo de dor no peito (cp)** e **frequência cardíaca máxima (thalach)** foram as mais relevantes para o diagnóstico. A análise reforça como algoritmos de aprendizado supervisionado podem apoiar a medicina na tomada de decisão clínica.

## 📊 Dataset

- **Nome**: Heart Disease UCI  
- **Fonte**: [Kaggle - Ronit Fledder](https://www.kaggle.com/datasets/ronitf/heart-disease-uci)  
- **Registros**: 303  
- **Colunas**: 14  

## 📁 Estrutura do Projeto

```
heart-disease-analysis/
│
├── heart.csv                   # Dataset
├── heart_analysis.py          # Código Python principal
├── README.md                  # Este arquivo
├── relatorio.pdf              # Relatório final em PDF
└── imagens/                   # Gráficos gerados pelo código
```

## ✅ Tecnologias Utilizadas

- Python 3.x  
- pandas  
- matplotlib  
- seaborn  
- scikit-learn  

## 🚀 Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/AndersonCagnini/Projeto-de-Mineracao-de-Dados.git
```

2. Instale as dependências:

```bash
pip install pandas matplotlib seaborn scikit-learn
```

3. Execute o script principal:

```bash
python heart_analysis.py
```

Os gráficos serão salvos na pasta `imagens/`.

## 🧪 Metodologia

1. **Análise Exploratória**: gráficos de distribuição, correlação e estatísticas descritivas.  
2. **Pré-processamento**: tratamento de dados e divisão em treino/teste.  
3. **Modelagem**: aplicação dos seguintes algoritmos:
   - Random Forest
   - Regressão Logística
   - Árvore de Decisão
   - KNN  
4. **Validação**: validação cruzada k-fold para maior confiabilidade.

## 📈 Resultados

### 📊 Métricas do modelo Random Forest:

- **Acurácia**: 0.98  
- **F1-score**: 0.89  
- **AUC (Curva ROC)**: 0.94  

### 📋 Comparação com outros modelos:

| Modelo               | Acurácia |
|----------------------|----------|
| Random Forest        | 0.98     |
| Logistic Regression  | 0.81     |
| Decision Tree        | 0.97     |
| KNN                  | 0.71     |

## 💬 Discussão

Os modelos Random Forest e Decision Tree apresentaram desempenho superior, destacando-se pela capacidade de lidar com variáveis categóricas e outliers. As variáveis `cp` (tipo de dor no peito) e `thalach` (frequência cardíaca máxima) foram as mais relevantes. Os resultados reforçam como a ciência de dados pode contribuir significativamente para a medicina preventiva.

## 📄 Relatório

O relatório completo está disponível em `relatorio.pdf` e contém:

- Descrição do dataset  
- Metodologia aplicada  
- Gráficos gerados  
- Tabela comparativa de modelos  
- Discussão e conclusão  

## 🔗 Link do Projeto

Repositório no GitHub: [https://github.com/AndersonCagnini/Projeto-de-Mineracao-de-Dados](https://github.com/AndersonCagnini/Projeto-de-Mineracao-de-Dados)

---

Este projeto faz parte da disciplina **Tópicos Especiais em Computação I** do curso de Ciência da Computação.
