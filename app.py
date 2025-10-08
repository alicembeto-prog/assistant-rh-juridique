import streamlit as st
from transformers import pipeline

# Chargement du modèle
@st.cache_resource
def load_model():
    return pipeline("text-generation", model="dbddv01/gpt2-french-small")

generator = load_model()

# Profils de génération
profils = {
    "Créatif": {"temperature": 0.9, "top_k": 60, "top_p": 0.95},
    "Formel": {"temperature": 0.6, "top_k": 40, "top_p": 0.9},
    "Juridique": {"temperature": 0.5, "top_k": 30, "top_p": 0.85},
    "Synthétique": {"temperature": 0.7, "top_k": 50, "top_p": 0.9}
}

# Configuration de la page
st.set_page_config(page_title="Assistant RH & Juridique", layout="wide", page_icon="🧠")
st.title("🧠 Assistant RH & Juridique")
st.markdown("Crée des fiches de poste, clauses, lettres RH… avec style et précision.")

# Onglets RH et Juridique
tab_rh, tab_juridique = st.tabs(["📋 Génération RH", "⚖️ Génération Juridique"])

with tab_rh:
    st.subheader("📋 Génération RH")
    prompt = st.text_area("Prompt RH", value="Rédige une fiche de poste pour un Responsable RH dans une ONG internationale :")
    longueur = st.slider("Longueur du texte", 50, 500, 250, 10)
    profil = st.selectbox("Style", list(profils.keys()))
    if st.button("Générer RH"):
        params = profils[profil]
        result = generator(prompt, max_new_tokens=longueur, **params)
        texte = result[0]["generated_text"]
        st.text_area("Texte généré", value=texte, height=300)
        st.download_button("📁 Télécharger", data=texte, file_name="fiche_RH.txt")

with tab_juridique:
    st.subheader("⚖️ Génération Juridique")
    prompt_j = st.text_area("Prompt Juridique", value="Rédige une clause de confidentialité pour un contrat de prestation de service.")
    longueur_j = st.slider("Longueur du texte", 50, 500, 250, 10, key="juridique_slider")
    profil_j = st.selectbox("Style", list(profils.keys()), key="juridique_profil")
    if st.button("Générer Juridique"):
        params = profils[profil_j]
        result = generator(prompt_j, max_new_tokens=longueur_j, **params)
        texte_j = result[0]["generated_text"]
        st.text_area("Texte généré", value=texte_j, height=300)
        st.download_button("📁 Télécharger", data=texte_j, file_name="clause_juridique.txt")
