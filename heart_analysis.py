import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay,
    roc_curve,
    auc
)

# 1. Carregar o dataset
df = pd.read_csv("heart.csv")
print("Primeiras linhas do dataset:")
print(df.head())

# 2. Análise inicial
print("\nVerificação de dados ausentes:")
print(df.isnull().sum())

# 3. Gráfico da distribuição da variável alvo
sns.countplot(x='target', data=df)
plt.title("Distribuição da Variável Alvo (0 = Sem doença, 1 = Com doença)")
plt.savefig("imagens/target-distribuicao.png")
plt.show()

# 4. Mapa de correlação
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title("Mapa de Correlação entre Variáveis")
plt.savefig("imagens/correlacao.png")
plt.show()

# 5. Separar features e target
X = df.drop("target", axis=1)
y = df["target"]

# 6. Separar treino e teste
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# 7. Modelo principal: Random Forest
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# 8. Avaliação
print("\nMatriz de Confusão:")
print(confusion_matrix(y_test, y_pred))

print("\nRelatório de Classificação:")
print(classification_report(y_test, y_pred))

# 9. Matriz de Confusão (gráfico)
ConfusionMatrixDisplay.from_estimator(model, X_test, y_test, cmap="Blues")
plt.title("Matriz de Confusão - Random Forest")
plt.savefig("imagens/matriz-confusao.png")
plt.show()

# 10. Importância das variáveis
importances = model.feature_importances_
features = X.columns
indices = np.argsort(importances)[::-1]

plt.figure(figsize=(10, 6))
sns.barplot(x=importances[indices], y=features[indices])
plt.title("Importância das Variáveis - Random Forest")
plt.savefig("imagens/importancia-variaveis.png")
plt.show()

# 11. Curva ROC
y_prob = model.predict_proba(X_test)[:, 1]
fpr, tpr, thresholds = roc_curve(y_test, y_prob)
roc_auc = auc(fpr, tpr)

plt.figure()
plt.plot(fpr, tpr, label=f"Curva ROC (AUC = {roc_auc:.2f})")
plt.plot([0, 1], [0, 1], 'k--')
plt.xlabel("Taxa de Falsos Positivos")
plt.ylabel("Taxa de Verdadeiros Positivos")
plt.title("Curva ROC - Random Forest")
plt.legend(loc="lower right")
plt.savefig("imagens/roc.png")
plt.show()

# 12. Comparação com outros modelos
print("\n🔍 Comparação entre modelos:")

modelos = {
    "Random Forest": RandomForestClassifier(random_state=42),
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Decision Tree": DecisionTreeClassifier(),
    "KNN": KNeighborsClassifier()
}

for nome, modelo in modelos.items():
    modelo.fit(X_train, y_train)
    score = modelo.score(X_test, y_test)
    print(f"{nome}: Acurácia = {score:.2f}")
