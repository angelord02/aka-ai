# Guide de Développement : Blockchain d'IA Industrielle

Ce guide détaille les étapes techniques pour développer et étendre l'écosystème AKA.

## Étape 1 : Initialisation de la Blockchain
La blockchain sert de registre de confiance. Pour ajouter des données :
1. Utilisez `blockchain/mock_chain.py`.
2. Appelez `blockchain.add_block(data)` avec un dictionnaire contenant les métadonnées de l'APK ou de la donnée.

## Étape 2 : Collecte de Données via APK (Ex: Sport)
L'APK Sport est hébergée sur Firebase. Pour lier une nouvelle APK :
1. Créez un agent dans `data_agents/` (ex: `sport_agent.py`).
2. Configurez la méthode `fetch_raw_data()` pour pointer vers l'API de l'APK ou de Firebase.
3. Utilisez le `DataFilter` de `data_processing/classifier.py` pour valider la pertinence industrielle.

## Étape 3 : Analyse et Classification Big Data
Le système utilise `data_processing/classifier.py` pour filtrer les données massives :
- Ajoutez des mots-clés dans `DataFilter.keywords` pour de nouvelles industries.
- Le score de pertinence détermine si la donnée est utilisée pour l'entraînement global.

## Étape 4 : Entraînement des Modules d'IA (Niches)
Chaque industrie (Mines, Sport, Finance) a son propre module dans `ai_modules/` :
- Les modules utilisent une architecture **MoE (Mixture of Experts)** pour réduire les coûts.
- L'entraînement est déclenché via la méthode `train()`.

## Étape 5 : Interaction via Chatbot
Intégrez le chatbot dans votre APK :
1. Importez `ai_modules/chatbot_nn.py`.
2. Initialisez `ChatbotNeuralNetwork()`.
3. Utilisez `process_query(input)` pour obtenir des réponses basées sur les données filtrées.

## Étape 6 : Suivi via le Dashboard
Pour visualiser l'état du système :
1. Lancez le serveur : `python3 dashboard/server.py`.
2. Ouvrez votre navigateur sur `http://localhost:8000`.
3. Vous y verrez les derniers blocs minés et l'état des agents.

---
**Note sur la Sécurité** : Toutes les données sont hachées en SHA-256 avant d'être inscrites sur la blockchain pour garantir la provenance et l'intégrité.
