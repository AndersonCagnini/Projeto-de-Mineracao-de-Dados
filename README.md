# 🔍 Análise de Doença Cardíaca com Mineração de Dados

Este projeto aplica técnicas de **mineração de dados** para prever a presença de **doença cardíaca** com base em características clínicas de pacientes.

## 🧠 Objetivo

Utilizar **classificação supervisionada** com Random Forest e outros modelos para prever a presença de doença cardíaca.

## 📊 Dataset

- **Nome**: Heart Disease UCI
- **Fonte**: [Kaggle - Ronit Fledder](https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset?resource=download)
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
git clone https://github.com/seu-usuario/heart-disease-analysis.git
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

## 📈 Resultados

O modelo Random Forest foi avaliado com diversas métricas:

- **Acurácia**: ~0.87
- **AUC (Curva ROC)**: ~0.94
- **F1-score**: ~0.89

Comparou-se também com outros modelos como Logistic Regression, Decision Tree e KNN.

## 📄 Relatório

O relatório em PDF está localizado no arquivo `relatorio.pdf` e contém:

- Descrição do dataset
- Técnica de mineração utilizada
- Prints dos gráficos:
  - Distribuição da variável alvo
  - Mapa de correlação
  - Matriz de confusão
  - Curva ROC
  - Importância das variáveis
- Comparativo entre modelos

---

Este projeto faz parte da disciplina **Tópicos Especiais em Computação I**.

Para mais informações ou dúvidas, entre em contato com o autor do repositório.
