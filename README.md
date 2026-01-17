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

---

## 🚀 Démo

**👉 [Essayer SECUR-SIM](https://yourusername.github.io/secur-sim/)**

---

## 📦 Installation

```bash
# Cloner
git clone https://github.com/yourusername/secur-sim.git
cd secur-sim

# Ouvrir
open index.html  # Ou double-cliquer
```

---

## 🛠️ Technologies

HTML5 • CSS3 • JavaScript (Vanilla) • LocalStorage • Python (validation)

**Zéro dépendance** - Fonctionne offline !

---

## 📂 Structure

```
secur-sim/
├── index.html
├── quiz.html
├── resultat.html
├── css/
├── js/
├── data/             # 100 questions par niveau
├── docs/
└── quiz_manager.py   # Validation
```

---

## 🎓 Utilisation

1. Choisir un niveau (1-3)
2. Répondre aux 20 questions
3. Consulter résultats et badge
4. Cliquer "Nouveau tirage" pour rejouer !

---

## 🤝 Contribution

Voir [CONTRIBUTING.md](CONTRIBUTING.md)

```bash
# Valider les questions
python quiz_manager.py validate 1
```

---

## 📊 Progression

```
Niveau 1 : ████████░░ 18/100 (18%)
Niveau 2 : ████░░░░░░ 10/100 (10%)
Niveau 3 : ████░░░░░░ 10/100 (10%)
Total    : 38/300 (12.7%)
```

**🎯 Objectif : 100 questions/niveau**

---

## 📄 Licence

MIT - Voir [LICENSE](LICENSE)

---

## 🙏 Remerciements

- [IAS](https://www.ivr-ias.ch/) - Interassociation de Sauvetage
- [KSBS](https://www.ksbs.ch/) - Service Sanitaire Coordonné
- [OFSP](https://www.bag.admin.ch/) - Office Fédéral Santé Publique
- [SRC](https://www.resuscitation.ch/) - Swiss Resuscitation Council

---

<div align="center">

**🚑 SECUR-SIM - Formation au secourisme suisse 🇨🇭**

*Développé avec ❤️ pour sauver des vies*

[⭐ Star](https://github.com/yourusername/secur-sim) • [🐛 Bug](https://github.com/yourusername/secur-sim/issues) • [💡 Feature](https://github.com/yourusername/secur-sim/issues)

</div>
