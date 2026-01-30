import streamlit as st
import joblib
import re
from nltk.corpus import stopwords
import nltk

# Configuration de la page
st.set_page_config(page_title="Détecteur de SPAM - ISPM", page_icon="🚫")

# 1. Chargement des ressources (Phase B)
@st.cache_resource
def load_resources():
    model = joblib.load('model_spam.pkl')
    vectorizer = joblib.load('vectorizer.pkl')
    nltk.download('stopwords')
    return model, vectorizer

model, vectorizer = load_resources()
stop_words_fr = set(stopwords.words('french'))

# 2. Fonction de nettoyage (Phase A)
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zàâçéèêëîïôûùµv]+', ' ', text)
    tokens = text.split()
    cleaned = [word for word in tokens if word not in stop_words_fr]
    return " ".join(cleaned)

# 3. Interface Utilisateur (Phase C)
st.title("🛡️ Détection de SPAM (SMS)")
st.write("Projet Hackathon - ISPM")

message_input = st.text_area("Saisissez votre message ici :", placeholder="Ex: Félicitations, vous avez gagné...")

if st.button("Analyser le message"):
    if message_input:
        # Prétraitement et Prédiction
        cleaned = clean_text(message_input)
        vectorized = vectorizer.transform([cleaned])
        
        prediction = model.predict(vectorized)[0]
        # Score de confiance (exigence du sujet)
        probabilities = model.predict_proba(vectorized)[0]
        confiance = probabilities[prediction] * 100
        
        # Affichage des résultats
        if prediction == 1:
            st.error(f"Résultat : SPAM (Confiance : {confiance:.2f}%)")
        else:
            st.success(f"Résultat : HAM / Non-Spam (Confiance : {confiance:.2f}%)")
    else:
        st.warning("Veuillez entrer un message.")

# Infos obligatoires pour le README / Pied de page (Phase D)
st.sidebar.markdown("### Équipe & Institut")
st.sidebar.write("ISPM - Madagascar")
st.sidebar.write("[www.ispm-edu.com](https://www.ispm-edu.com)")