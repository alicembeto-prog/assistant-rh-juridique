# 🧠 Assistant RH & Juridique

Ce projet Streamlit propose un assistant intelligent pour générer des contenus RH et juridiques en français, à partir de prompts personnalisés.

## ✨ Fonctionnalités

- Génération de fiches de poste, clauses, lettres RH…
- Onglets RH et Juridique
- Choix de styles : Créatif, Formel, Juridique, Synthétique
- Export du texte généré en `.txt`
- Interface harmonisée avec thème personnalisé

## 🚀 Utilisation sur Hugging Face Spaces

Ce projet est conçu pour être déployé facilement sur [Hugging Face Spaces](https://huggingface.co/spaces) avec Streamlit.

### Lancer en local

```bash
pip install -r requirements.txt
streamlit run app.py
```

### Déploiement sur Spaces

1. Créez un Space avec le SDK **Streamlit**.
2. Importez ce dépôt ou uploadez les fichiers `app.py`, `requirements.txt` et `README.md`.
3. Le lancement est automatique. Si besoin, ajoutez des variables d’environnement dans les paramètres du Space.

## 📚 Modèle utilisé

Modèle francophone : [`dbddv01/gpt2-french-small`](https://huggingface.co/dbddv01/gpt2-french-small) via Hugging Face Transformers.

## 📁 Arborescence minimale

```
assistant-rh-juridique/
├── app.py
├── requirements.txt
└── README.md
```

## 📖 Exemple d'utilisation

- Sélectionnez un type de document RH ou juridique
- Choisissez un style (créatif, juridique…)
- Entrez un prompt personnalisé
- Obtenez un texte généré et téléchargez-le si besoin

## 🛠️ Dépendances principales

- streamlit
- transformers
- torch

_Voir `requirements.txt` pour la liste complète._

## 🙏 Remerciements

Merci à la communauté Hugging Face et aux contributeurs aux modèles open-source.

---

*Projet réalisé par Moise / alicembeto-prog.*
