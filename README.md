# LangGraph Deployment Project

Projet LangGraph pour déploiement sur Render.

## Installation

\\\ash
pip install -e . "langgraph-cli[inmem]"
\\\

## Développement local

\\\ash
langgraph dev
\\\

## Déploiement sur Render

1. Créer les services Postgres et Redis dans Render
2. Configurer les variables d'environnement
3. Déployer avec Docker ou Python runtime
