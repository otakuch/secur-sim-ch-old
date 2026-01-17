# 📦 SECUR-SIM - Version Web-Only

Cette version de SECUR-SIM est **100% web** - aucune installation requise, aucune dépendance, aucun Python !

---

## ✨ Qu'est-ce que la Version Web-Only ?

Cette version contient **tout** ce dont vous avez besoin pour utiliser SECUR-SIM :

✅ **HTML, CSS, JavaScript** - Code source complet  
✅ **Questions JSON** - 38 questions sur 3 niveaux  
✅ **Documentation** - Guides complets en Markdown  
✅ **Page About** - Disclaimer et sources officielles  
✅ **Templates GitHub** - Issues, PR

❌ **Pas de Python** - Aucun script à installer  
❌ **Pas de dépendances** - Fonctionne immédiatement

---

## 🚀 Démarrage Immédiat

### Méthode 1 : Double-clic

```
1. Télécharger le dossier
2. Double-cliquer sur index.html
3. ✅ Ça marche !
```

### Méthode 2 : Avec Git

```bash
git clone https://github.com/yourusername/secur-sim.git
cd secur-sim
open index.html
```

### Méthode 3 : GitHub Pages

```bash
# Push sur GitHub
git push

# Activer Pages
Settings → Pages → Branch: main → Save

# Accéder
https://yourusername.github.io/secur-sim/
```

---

## 📝 Ajouter des Questions

### Sans Python, Comment Valider ?

Utilisez des **validateurs JSON en ligne** (gratuits) :

#### 1. [JSONLint.com](https://jsonlint.com/) ⭐ Recommandé

```
1. Ouvrir data/niveau1.json
2. Copier tout le contenu
3. Aller sur jsonlint.com
4. Coller le contenu
5. Cliquer "Validate JSON"
6. ✅ Si vert → OK
7. ❌ Si rouge → Erreur à corriger
```

#### 2. [JSONFormatter.org](https://jsonformatter.org/)

Même principe + formate automatiquement le JSON

#### 3. VS Code (Éditeur)

VS Code valide automatiquement le JSON :
- Ouvrir le fichier .json
- Si erreur → soulignement rouge
- Passer la souris → voir l'erreur

---

## 🔧 Structure des Questions

Chaque question doit respecter ce format :

```json
{
  "id": "n1_q050",           ← Unique
  "titre": "Titre",
  "cas_clinique": "...",
  "question": "...",
  "options": [               ← Exactement 4 options
    {
      "id": "a",             ← a, b, c, d
      "texte": "...",
      "correct": false,      ← Exactement 1 true
      "explication": "...",
      "source": "..."
    },
    // ... b, c, d
  ],
  "points": 10,
  "temps_recommande": 60,
  "tags": ["tag1", "tag2"],
  "difficulte": 1
}
```

---

## ✅ Checklist de Validation Manuelle

Avant de committer une nouvelle question :

- [ ] ID unique (vérifier qu'il n'existe pas déjà)
- [ ] Exactement 4 options (a, b, c, d)
- [ ] Exactement 1 option avec `"correct": true`
- [ ] Toutes les options ont `"explication"`
- [ ] Option correcte a `"complement"`
- [ ] Toutes les options ont `"source"`
- [ ] JSON valide (jsonlint.com)
- [ ] Testé dans le navigateur (index.html)

---

## 🎯 Avantages de cette Version

### Simplicité

✅ Aucune installation  
✅ Fonctionne partout  
✅ Compatible tous navigateurs  
✅ Pas de terminal requis

### Accessibilité

✅ Débutants bienvenus  
✅ Pas de connaissances Python  
✅ Documentation claire  
✅ Validation en ligne gratuite

### Performance

✅ Léger (< 500 KB)  
✅ Rapide (pas de serveur)  
✅ Offline après 1er chargement  
✅ Pas de dépendances externes

---

## 📊 Différences avec Version Complète

| Fonctionnalité | Web-Only | Complète |
|----------------|----------|----------|
| Quiz fonctionnel | ✅ | ✅ |
| Questions JSON | ✅ | ✅ |
| Documentation | ✅ | ✅ |
| GitHub ready | ✅ | ✅ |
| Script Python | ❌ | ✅ |
| Validation auto | ❌ | ✅ |
| Stats Python | ❌ | ✅ |

**Pour 99% des utilisateurs, la version Web-Only suffit !**

---

## 🛠️ Outils Recommandés

### Éditeurs de Texte

**Gratuits et faciles** :
- [VS Code](https://code.visualstudio.com/) - Le plus populaire
- [Sublime Text](https://www.sublimetext.com/)
- [Notepad++](https://notepad-plus-plus.org/) (Windows)

**Fonctionnalités utiles** :
- Coloration syntaxique
- Validation JSON automatique
- Indentation automatique

### Navigateurs

**Recommandés** :
- Chrome / Edge (DevTools puissants)
- Firefox (Console claire)
- Safari (bon pour macOS)

**Touches utiles** :
- F12 → DevTools
- Ctrl+Shift+R → Recharger sans cache

### Validateurs JSON

- [jsonlint.com](https://jsonlint.com/)
- [jsonformatter.org](https://jsonformatter.org/)
- [codebeautify.org/jsonviewer](https://codebeautify.org/jsonviewer)

---

## 📚 Documentation

Tout est inclus dans ce dossier :

```
📄 README.md              → Vue d'ensemble
📄 QUICKSTART.md          → Démarrage rapide
📄 CONTRIBUTING.md        → Comment contribuer
📄 DEPLOYMENT.md          → Déployer en ligne
📄 GITHUB-SETUP.md        → Config GitHub
📄 about.html             → Disclaimer et sources

docs/
  📄 GUIDE-CREATION-QUESTIONS.md
  📄 STRUCTURE-100-QUESTIONS.md
```

---

## 🤝 Contribuer

### Workflow Simple

```bash
# 1. Fork le projet sur GitHub

# 2. Clone ton fork
git clone https://github.com/TON-USERNAME/secur-sim.git

# 3. Crée une branche
git checkout -b add-questions

# 4. Ajoute des questions dans data/niveau1.json

# 5. Valide sur jsonlint.com

# 6. Teste dans le navigateur

# 7. Commit et push
git add .
git commit -m "feat: Add 5 new BLS-AED questions"
git push origin add-questions

# 8. Crée une Pull Request sur GitHub
```

---

## 🆘 Aide

### Problèmes Courants

**Q: JSON invalide, où est l'erreur ?**
```
1. Copier le contenu du fichier
2. Aller sur jsonlint.com
3. Coller
4. Lire le message d'erreur
5. Corriger (souvent une virgule ou un guillemet)
```

**Q: Comment savoir si mon ID est unique ?**
```
Ctrl+F dans le fichier JSON
Chercher l'ID (ex: "n1_q050")
S'il apparaît 2 fois → changer le numéro
```

**Q: Mon quiz ne charge pas les questions**
```
1. F12 → Console
2. Regarder les erreurs rouges
3. Souvent : JSON invalide
4. Valider sur jsonlint.com
```

### Support

- 📖 Lire [QUICKSTART.md](QUICKSTART.md)
- 📖 Lire [CONTRIBUTING.md](CONTRIBUTING.md)
- 🐛 [Ouvrir une issue](https://github.com/yourusername/secur-sim/issues)
- 💬 [Poser une question](https://github.com/yourusername/secur-sim/discussions)

---

## ✨ Pourquoi Cette Version ?

### Philosophie

> "Un bon outil doit être simple à utiliser"

SECUR-SIM est conçu pour :
- ✅ Formateurs en secourisme
- ✅ Étudiants
- ✅ Bénévoles

**Pas besoin d'être développeur pour contribuer !**

### Objectif

Permettre à **n'importe qui** de :
1. Utiliser le quiz
2. Ajouter des questions
3. Partager avec d'autres

**Sans barrière technique.**

---

## 🎯 Prochaines Étapes

1. ✅ **Télécharger** cette version
2. 📖 **Lire** QUICKSTART.md
3. 🧪 **Tester** le quiz (index.html)
4. 📝 **Ajouter** 1-2 questions
5. ✅ **Valider** sur jsonlint.com
6. 🚀 **Push** sur GitHub
7. 🌐 **Activer** GitHub Pages

---

<div align="center">

**🚑 SECUR-SIM - Version Web-Only**

*Simple • Rapide • Accessible à tous*

**Aucune installation • Aucune dépendance • 100% fonctionnel**

[📖 Lire le README](README.md) • [🚀 QUICKSTART](QUICKSTART.md) • [🤝 Contribuer](CONTRIBUTING.md)

</div>
