# hackatonVANILAA
Application Web de detection de SPAM SMS (ML/NLP) 

#  Système de Détection de SPAM (NLP) - ISPM 2026

Ce projet a été développé dans le cadre du Hackathon de Machine Learning. Il propose une solution complète de classification de SMS en français, utilisant un modèle de traitement automatique du langage naturel (NLP).

##  Informations Institutionnelles
* Institut : Institut Supérieur Polytechnique de Madagascar (ISPM)
* Site Web : [www.ispm-edu.com](https://www.ispm-edu.com)

##  Application Web 
* Accédez à l'application ici : https://hackatonvanilaa-wuwsamuylwshaj4gfqsziy.streamlit.app/

---

##  Équipe & Rôles
* POPP Dietmar Ndremarolahy : Responsable donneés et annotation
* DIMBINIERANA Tolojanahary Nisandratampifaliana : Pretraiment NLP
* RANJASON Sitrakaniana Brundy Joel : Modelisation machine Learning
* ANDRIANASOLO Hasina Tovonambinintsoa : Application Web et deploiement
* RAKOTOMANALINARIVO Andy Nantenaina : Gestion du projet et github
* RAFALIMANANA Minosoa Mampionona : Documentantion et rapport
* RAKOTOFARA Nianantsalama : Teste et demonstration

---

##  Stack Technologique 
* Backend : Python 3.11
* ML Framework : Scikit-Learn pour la vectorisation TF-IDF et l'algorithme de classification.
* NLP Pipeline : NLTK (Natural Language Toolkit) pour le filtrage linguistique.
* Web Interface : Streamlit pour l'expérience utilisateur et la saisie en temps réel.
* DevOps : GitHub pour le versioning et Streamlit Cloud pour le déploiement public.

---

1. Le Modèle : Régression Logistique
Pour ce projet, nous avons implémenté un algorithme de Régression Logistique.

Pourquoi ce choix ? Contrairement à une simple liste de mots interdits, ce modèle probabiliste apprend l'importance relative de chaque mot. Il est particulièrement performant pour la classification binaire (Spam vs Ham) car il est robuste, rapide et offre une interprétation mathématique claire via les coefficients des mots.

Fonction de décision : Le modèle utilise une fonction sigmoïde pour transformer le score textuel en une probabilité entre 0 et 1.

2. Le Processus Technique (Pipeline NLP)
Le traitement des données suit un flux de travail rigoureux pour transformer un texte brut en une décision binaire :

A. Prétraitement (Cleaning)
Avant l'analyse, le texte est "nettoyé" pour ne garder que l'essentiel :

Normalisation : Conversion en minuscules pour uniformiser le vocabulaire.

Nettoyage Regex : Suppression des caractères spéciaux, emojis et chiffres.

Stop-Words : Retrait des mots de liaison français (ex: "ce", "dans", "votre") via la bibliothèque NLTK, car ils n'aident pas à distinguer un spam d'un message normal.

B. Vectorisation TF-IDF
Comme les modèles de Machine Learning ne comprennent que les nombres, nous utilisons la technique TF-IDF (Term Frequency-Inverse Document Frequency) :

TF : Mesure la fréquence d'un mot dans le message.

IDF : Attribue un poids plus fort aux mots rares et discriminants (ex: "félicitations", "gain", "cliquez") et diminue l'importance des mots communs.

C. Inférence en Temps Réel (Application Web)
Dans l'interface Streamlit, le processus est le suivant :

Saisie : L'utilisateur entre un message suspect.

Transformation : Le message subit le même nettoyage et la même vectorisation que le dataset d'entraînement.

Prédiction : Le modèle chargé via joblib calcule la probabilité.

Affichage : Le résultat est renvoyé avec un score de confiance (ex: "Probabilité de Spam : 98%").

Évaluation du Modèle
Le modèle a été évalué sur un jeu de test (données jamais vues lors de l'entraînement) avec les métriques suivantes :

Accuracy : Capacité globale à bien classer les messages.

F1-Score : Moyenne harmonique de la précision et du rappel, essentielle ici pour s'assurer que nous ne classons pas par erreur un message important (Ham) en Spam.


---  


## Installation locale
```bash
git clone [https://github.com/PoppDIDI/hackatonVANILAA.git](https://github.com/PoppDIDI/hackatonVANILAA.git)
pip install -r requirements.txt
streamlit run app.py
