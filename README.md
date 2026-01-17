# 🚑 SECUR-SIM v2.0

**Plateforme interactive de formation au secourisme suisse**

[![Version](https://img.shields.io/badge/version-2.0-blue.svg)](https://github.com/yourusername/secur-sim)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![GitHub Pages](https://img.shields.io/badge/demo-live-success.svg)](https://yourusername.github.io/secur-sim/)

---

## 📖 À propos

**SECUR-SIM** est un quiz interactif pour former et tester les compétences en secourisme selon les normes suisses. Avec un système de **sélection aléatoire** de 20 questions parmi 100 par niveau, chaque session offre une expérience unique.

🎯 **Public** : Secouristes, Samaritains, personnel soignant, pompiers, grand public

---

## ✨ Fonctionnalités

- 🎲 **100 questions par niveau** (300 au total)
- 🔀 **20 questions aléatoires** par session
- 📚 **3 niveaux** : BLS-AED, First Responder, Médecine de Catastrophe
- 💡 **Feedback pédagogique** complet avec sources
- 📊 **Système de scoring** avec badges
- 📱 **Design responsive** (mobile, tablette, desktop)
- 🌐 **100% offline** après chargement
- ⚠️ **Page About** avec disclaimer et sources officielles

---

## 🚀 Démo

**👉 [Essayer SECUR-SIM](https://yourusername.github.io/secur-sim/)**

---

## 📦 Installation

### Méthode Simple (Aucune installation requise)

```bash
# 1. Cloner le repository
git clone https://github.com/yourusername/secur-sim.git
cd secur-sim

# 2. Ouvrir dans le navigateur
open index.html  # macOS
start index.html # Windows
xdg-open index.html # Linux

# Ou double-cliquer sur index.html
```

### Avec Serveur Local (Optionnel)

```bash
# Python 3
python -m http.server 8000

# Node.js avec npx
npx http-server

# PHP
php -S localhost:8000

# Puis ouvrir : http://localhost:8000
```

---

## 🛠️ Technologies

**Frontend** : HTML5, CSS3, JavaScript (Vanilla)

**Design** : Flexbox, Grid, Animations CSS

**Fonts** : Google Fonts (DM Sans, Lexend)

**Storage** : LocalStorage API

**Aucune dépendance** - Fonctionne 100% offline !

---

## 📂 Structure

```
secur-sim/
├── index.html              # Page d'accueil
├── quiz.html               # Interface du quiz
├── resultat.html           # Page de résultats
├── about.html              # About & Disclaimer
├── css/
│   ├── style.css           # Styles principaux
│   └── responsive.css      # Styles responsive
├── js/
│   ├── app.js              # Logique principale
│   ├── quiz-engine.js      # Moteur du quiz
│   └── scoring.js          # Système de scoring
├── data/
│   ├── niveau1.json        # 100 questions BLS-AED
│   ├── niveau2.json        # 100 questions First Responder
│   └── niveau3.json        # 100 questions Catastrophe
├── assets/
│   └── sources.md          # Références officielles
├── docs/
│   ├── GUIDE-CREATION-QUESTIONS.md
│   └── STRUCTURE-100-QUESTIONS.md
├── .github/                # Templates issues/PR
├── LICENSE                 # Licence MIT
└── README.md               # Ce fichier
```

---

## 🎓 Utilisation

1. **Choisir un niveau** (1-3)
2. **Répondre aux 20 questions** sélectionnées aléatoirement
3. **Consulter résultats** et badge
4. **Cliquer "Nouveau tirage"** pour rejouer !

---

## 📝 Ajouter des Questions

### 1. Éditer le fichier JSON

Ouvrir `data/niveau1.json` (ou niveau2, niveau3) dans un éditeur de texte.

### 2. Ajouter une question

```json
{
  "id": "n1_q050",
  "titre": "Titre court",
  "cas_clinique": "Description du cas médical...",
  "question": "Quelle est la priorité ?",
  "options": [
    {
      "id": "a",
      "texte": "Option A",
      "correct": false,
      "explication": "Pourquoi incorrect",
      "source": "Référence"
    },
    {
      "id": "b",
      "texte": "Option B (CORRECTE)",
      "correct": true,
      "explication": "Pourquoi correct",
      "complement": "Info supplémentaire",
      "source": "Guidelines BLS-AED-SRC 2021"
    },
    {
      "id": "c",
      "texte": "Option C",
      "correct": false,
      "explication": "Pourquoi incorrect",
      "source": "Référence"
    },
    {
      "id": "d",
      "texte": "Option D",
      "correct": false,
      "explication": "Pourquoi incorrect",
      "source": "Référence"
    }
  ],
  "points": 10,
  "temps_recommande": 60,
  "tags": ["rcp", "urgence"],
  "difficulte": 1
}
```

### 3. Vérifier le JSON

Utiliser un validateur JSON en ligne :
- [jsonlint.com](https://jsonlint.com/)
- [jsonformatter.org](https://jsonformatter.org/)

### 4. Tester

Ouvrir `index.html` et tester la nouvelle question !

---

## 🤝 Contribution

Voir [CONTRIBUTING.md](CONTRIBUTING.md) pour :
- 📝 Ajouter des questions
- 🐛 Signaler des bugs
- 💡 Proposer des améliorations

---

## 📊 Progression

```
Niveau 1 : ████████░░ 18/100 (18%)
Niveau 2 : ████░░░░░░ 10/100 (10%)
Niveau 3 : ████░░░░░░ 10/100 (10%)
Total    : 38/300 (12.7%)
```

**🎯 Objectif v2.1 : 100 questions/niveau**

---

## 📚 Sources Officielles

Toutes les questions sont basées sur :

- 🇨🇭 **IAS** - Interassociation de Sauvetage
- ❤️ **SRC** - Swiss Resuscitation Council
- 🏥 **KSBS** - Service Sanitaire Coordonné
- 🇪🇺 **ERC** - European Resuscitation Council
- 🏛️ **OFSP** - Office Fédéral de la Santé Publique

➡️ Voir [about.html](about.html) pour la liste complète des sources

---

## ⚠️ Disclaimer

**SECUR-SIM est un outil éducatif uniquement.**

❌ Ne remplace pas une formation officielle  
❌ Ne constitue pas un diagnostic médical  
❌ Ne certifie pas vos compétences  

✅ Complète votre formation  
✅ Permet de réviser  
✅ Basé sur sources officielles  

**En cas d'urgence réelle : appelez le 144 (Suisse)**

➡️ Lire le [disclaimer complet](about.html)

---

## 📄 Licence

MIT - Voir [LICENSE](LICENSE)

Utilisation libre avec conservation de la notice de copyright.

---

## 🙏 Remerciements

- [IAS](https://www.ivr-ias.ch/) - Interassociation de Sauvetage
- [KSBS](https://www.ksbs.ch/) - Service Sanitaire Coordonné
- [SRC](https://www.resuscitation.ch/) - Swiss Resuscitation Council
- [OFSP](https://www.bag.admin.ch/) - Office Fédéral Santé Publique

---

## 🌐 Déploiement GitHub Pages

1. **Fork** ce repository
2. **Settings** → **Pages**
3. **Branch** : `main`
4. **Save**
5. Accéder à : `https://yourusername.github.io/secur-sim/`

---

<div align="center">

**🚑 SECUR-SIM - Formation au secourisme suisse 🇨🇭**

*Développé avec ❤️ pour sauver des vies*

[⭐ Star](https://github.com/yourusername/secur-sim) • [🐛 Bug](https://github.com/yourusername/secur-sim/issues) • [💡 Feature](https://github.com/yourusername/secur-sim/issues)

</div>
