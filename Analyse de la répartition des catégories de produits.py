import pandas as pd
import matplotlib.pyplot as plt

# Chargement des données
data = pd.read_csv('cleaned_openfoodfacts.csv', delimiter='\t', dtype={'code': str})

# Identification des catégories de produits du top 2 au top 11
categorie_counts = data['categories_en'].value_counts()  # Calculer le compte total pour chaque catégorie
top_categories = categorie_counts[1:11]  # Sélectionner du top 2 au top 11

# Création du graphique
plt.figure(figsize=(12, 8))
top_categories.plot(kind='bar')
plt.title('Top 1 à Top 10 des catégories de produits les plus représentées')
plt.xlabel('Catégorie')
plt.ylabel('Nombre de Produits')
plt.xticks(rotation=45, ha='right')  # Ajustement de l'alignement des étiquettes pour une meilleure lisibilité
plt.tight_layout()  # Ajuste automatiquement les paramètres de subplot pour que le graphique tienne bien dans la zone d'affichage
plt.show()
