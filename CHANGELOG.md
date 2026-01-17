# Changelog

Tous les changements notables de ce projet seront documentés dans ce fichier.

Le format est basé sur [Keep a Changelog](https://keepachangelog.com/fr/1.0.0/),
et ce projet adhère au [Semantic Versioning](https://semver.org/lang/fr/).

---

## [2.0.0] - 2026-01-17

### 🎉 Nouveau

- **Système de sélection aléatoire** : 20 questions parmi 100 par niveau
- **Rejouabilité infinie** : Bouton "Nouveau tirage" pour obtenir de nouvelles questions
- **Badge v2.0** dans le header pour identifier la version
- **Bannière informative** expliquant le système aléatoire
- **Script de validation Python** (`quiz_manager.py`) pour contrôler la qualité des questions
- **Documentation complète** :
  - `GUIDE-CREATION-QUESTIONS.md` (4000+ mots)
  - `STRUCTURE-100-QUESTIONS.md` (2000+ mots)
  - `CONTRIBUTING.md` pour les contributeurs
- **8 questions supplémentaires Niveau 1** (exemples de qualité)

### ✨ Améliorations

- **Interface UI** : Cartes de niveaux avec statistiques (100 questions / 20 par session)
- **Performance** : Optimisation du code de sélection aléatoire
- **Console logging** : Informations sur les questions sélectionnées
- **Architecture** : Séparation claire base de données / logique de sélection

### 📚 Documentation

- README.md complet pour GitHub
- Guide de contribution détaillé
- Templates d'issues et PR
- CHANGELOG (ce fichier)
- LICENSE MIT

### 🔧 Technique

- Fonction `selectRandomQuestions(pool, count)`
- Algorithme de mélange Fisher-Yates
- Structure JSON standardisée pour les questions
- Validation automatique des questions

---

## [1.0.0] - 2026-01-16

### 🎉 Version Initiale

- **3 niveaux de difficulté** :
  - Niveau 1 : BLS-AED (10 questions)
  - Niveau 2 : First Responder (10 questions)
  - Niveau 3 : Médecine de Catastrophe (10 questions)
- **Quiz interactif** avec feedback immédiat
- **Cas cliniques** au format médical suisse
- **Système de scoring** avec badges (Or, Argent, Bronze)
- **Design responsive** (mobile, tablette, desktop)
- **Sources vérifiables** (IAS, KSBS, OFSP, REGA)
- **Explications pédagogiques** détaillées
- **Compléments d'information** pour les bonnes réponses
- **Timer** en temps réel
- **Barre de progression** visuelle
- **Page de résultats** avec statistiques

---

## [Unreleased]

### 🔜 Version 2.1 (Planifiée)

**Questions** :
- [ ] 100 questions Niveau 1 (actuellement 18/100)
- [ ] 100 questions Niveau 2 (actuellement 10/100)
- [ ] 100 questions Niveau 3 (actuellement 10/100)

**Fonctionnalités** :
- [ ] Mode entraînement (révision des questions ratées)
- [ ] Statistiques détaillées par thématique
- [ ] Export PDF des résultats
- [ ] Historique des sessions
- [ ] Graphiques de progression

**Améliorations** :
- [ ] PWA (Progressive Web App) pour mode offline complet
- [ ] Thème sombre/clair configurable
- [ ] Animations améliorées
- [ ] Accessibilité WCAG 2.1 AA

---

## [Roadmap] - Version 3.0 (Future)

### 🚀 Fonctionnalités Avancées

**Compte Utilisateur** :
- Connexion / Inscription
- Sauvegarde cloud de la progression
- Synchronisation multi-appareils

**Social** :
- Classements (leaderboards)
- Badges avancés et achievements
- Partage de scores sur réseaux sociaux

**Multijoueur** :
- Mode compétition en temps réel
- Salles de quiz privées
- Tournois

**Technique** :
- API REST pour intégration externe
- Webhooks pour notifications
- Dashboard admin
- Analytics avancées

**Mobile** :
- Application iOS native
- Application Android native
- Notifications push

---

## Types de Changements

- `Added` : Nouvelles fonctionnalités
- `Changed` : Modifications de fonctionnalités existantes
- `Deprecated` : Fonctionnalités obsolètes (bientôt retirées)
- `Removed` : Fonctionnalités retirées
- `Fixed` : Corrections de bugs
- `Security` : Corrections de sécurité

---

## Liens

- **Repository** : https://github.com/yourusername/secur-sim
- **Demo** : https://yourusername.github.io/secur-sim/
- **Issues** : https://github.com/yourusername/secur-sim/issues
- **Releases** : https://github.com/yourusername/secur-sim/releases

---

<div align="center">

*Développé avec ❤️ pour sauver des vies*

</div>
