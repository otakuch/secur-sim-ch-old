# 🚀 Configuration GitHub - SECUR-SIM

Guide complet pour mettre en ligne SECUR-SIM sur GitHub.

---

## 📦 Contenu du Repository

Tous les fichiers nécessaires sont prêts :

```
secur-sim/
├── 📄 README.md                  # Page d'accueil GitHub
├── 📄 LICENSE                    # Licence MIT
├── 📄 CONTRIBUTING.md            # Guide de contribution
├── 📄 CHANGELOG.md               # Historique des versions
├── 📄 QUICKSTART.md              # Démarrage rapide
├── 📄 DEPLOYMENT.md              # Guide de déploiement
├── 📄 .gitignore                 # Fichiers à ignorer
├── 📄 _config.yml                # Config GitHub Pages
├── 📄 package.json               # Métadonnées du projet
├──  📁 .github/                   # Templates GitHub
│   ├── pull_request_template.md
│   └── ISSUE_TEMPLATE/
│       ├── bug_report.md
│       ├── feature_request.md
│       └── question_contribution.md
├── 📁 docs/                      # Documentation
│   ├── GUIDE-CREATION-QUESTIONS.md
│   └── STRUCTURE-100-QUESTIONS.md
├── 📁 css/                       # Styles
│   ├── style.css
│   └── responsive.css
├── 📁 js/                        # Scripts
│   ├── app.js
│   ├── quiz-engine.js
│   └── scoring.js
├── 📁 data/                      # Questions (JSON)
│   ├── niveau1.json
│   ├── niveau2.json
│   └── niveau3.json
├── 📁 assets/                    # Ressources
│   └── sources.md
├── 📄 index.html                 # Page d'accueil
├── 📄 quiz.html                  # Interface quiz
├── 📄 resultat.html              # Page résultats
└── 🐍 quiz_manager.py            # Script de validation
```

---

## 🎯 Étapes de Configuration

### 1️⃣ Créer le Repository sur GitHub

#### Option A : Via l'Interface Web

1. Aller sur [github.com](https://github.com)
2. Cliquer sur **+** → **New repository**
3. **Repository name** : `secur-sim`
4. **Description** : `Plateforme interactive de formation au secourisme suisse`
5. **Public** ✓
6. **Ne PAS** initialiser avec README, .gitignore ou license (déjà présents)
7. **Create repository**

#### Option B : Via GitHub CLI

```bash
# Installer GitHub CLI : https://cli.github.com/
gh repo create secur-sim --public --description "Plateforme interactive de formation au secourisme suisse"
```

---

### 2️⃣ Initialiser Git Localement

```bash
# Se placer dans le dossier
cd secur-sim-github

# Initialiser git
git init

# Ajouter tous les fichiers
git add .

# Premier commit
git commit -m "🎉 Initial commit - SECUR-SIM v2.0"
```

---

### 3️⃣ Lier au Repository GitHub

```bash
# Remplacer VOTRE-USERNAME par votre username GitHub
git remote add origin https://github.com/VOTRE-USERNAME/secur-sim.git

# Vérifier
git remote -v
```

---

### 4️⃣ Pousser sur GitHub

```bash
# Renommer la branche principale
git branch -M main

# Pousser
git push -u origin main
```

**✅ Votre code est maintenant sur GitHub !**

---

### 5️⃣ Activer GitHub Pages

1. Aller sur votre repository : `https://github.com/VOTRE-USERNAME/secur-sim`
2. **Settings** → **Pages** (menu de gauche)
3. **Source** : Deploy from a branch
4. **Branch** : `main`
5. **Folder** : `/ (root)`
6. **Save**

**⏱️ Attendez 1-2 minutes...**

Votre site sera accessible à :
```
https://VOTRE-USERNAME.github.io/secur-sim/
```

---

### 6️⃣ Vérifier le Déploiement

1. **Actions** (onglet du repository)
2. Voir le workflow "pages build and deployment"
3. ✅ Quand c'est vert → c'est en ligne !

---

### 7️⃣ Configurer le Repository (Optionnel)

#### Topics (Tags)

Settings → (en haut) → Topics :
```
quiz, secourisme, formation, bls-aed, first-responder, medical-training, 
switzerland, suisse, interactive, education, e-learning
```

#### Description

```
🚑 Plateforme interactive de formation au secourisme suisse avec système de sélection aléatoire de questions
```

#### Website

```
https://VOTRE-USERNAME.github.io/secur-sim/
```

#### Social Preview

Uploader une image (1280x640px) :
- Settings → Social preview → Edit
- Upload `assets/social-preview.png`

---

## 📝 Personnaliser les URLs

### Dans README.md

Remplacer `yourusername` par votre username GitHub :

```bash
# macOS/Linux
sed -i '' 's/yourusername/VOTRE-USERNAME/g' README.md

# Linux
sed -i 's/yourusername/VOTRE-USERNAME/g' README.md

# Windows (PowerShell)
(Get-Content README.md) -replace 'yourusername','VOTRE-USERNAME' | Set-Content README.md
```

### Dans tous les fichiers

```bash
# Trouver toutes les occurrences
grep -r "yourusername" .

# Remplacer dans tous les fichiers Markdown
find . -name "*.md" -exec sed -i '' 's/yourusername/VOTRE-USERNAME/g' {} +
```

---

## 🎨 Ajouter une Image Banner

### Créer le Banner

Dimensions : 1280x640px

Contenu suggéré :
```
- Logo 🚑
- Titre : SECUR-SIM
- Sous-titre : Formation au secourisme suisse
- Badge : v2.0
```

### Upload

```bash
mkdir -p assets/images
# Copier votre banner.png dans assets/images/

git add assets/images/banner.png
git commit -m "📸 Add social preview banner"
git push
```

### Mettre à jour README

```markdown
![SECUR-SIM Banner](assets/images/banner.png)
```

---

## 🏷️ Créer le Premier Release

```bash
# Créer un tag
git tag -a v2.0.0 -m "SECUR-SIM v2.0.0 - Système de sélection aléatoire"

# Pousser le tag
git push origin v2.0.0
```

Sur GitHub :
1. **Releases** → **Draft a new release**
2. **Choose a tag** : v2.0.0
3. **Release title** : `SECUR-SIM v2.0.0 - Sélection Aléatoire`
4. **Description** :

```markdown
## 🎉 SECUR-SIM v2.0.0

### ✨ Nouveautés

- 🎲 Système de sélection aléatoire : 20 questions parmi 100 par niveau
- 🔄 Rejouabilité infinie avec bouton "Nouveau tirage"
- 📚 Documentation complète (GUIDE, CONTRIBUTING, DEPLOYMENT)
- 🐍 Script de validation Python
- 📝 8 nouvelles questions Niveau 1

### 📦 Installation

```bash
git clone https://github.com/VOTRE-USERNAME/secur-sim.git
cd secur-sim
open index.html
```

### 🌐 Démo

[Essayer SECUR-SIM](https://VOTRE-USERNAME.github.io/secur-sim/)

### 📊 Progression

- Niveau 1 : 18/100 questions (18%)
- Niveau 2 : 10/100 questions (10%)
- Niveau 3 : 10/100 questions (10%)
```

5. **Publish release**

---

## 🔒 Configurer les Permissions

### Branch Protection (Recommandé)

Settings → Branches → Add rule :

```
Branch name pattern: main

✓ Require a pull request before merging
  ✓ Require approvals (1)
✓ Require status checks to pass
✓ Require conversation resolution before merging
✓ Include administrators
```

---

## 👥 Ajouter des Collaborateurs

Settings → Collaborators → Add people

Rôles :
- **Admin** : Accès complet
- **Write** : Push, merge PR
- **Read** : Lecture seulement

---

## 📊 GitHub Insights

Activer les insights :

Settings → General → Features :
- ✓ Issues
- ✓ Discussions
- ✓ Projects
- ✓ Wiki (optionnel)

---

## 🎯 Checklist Complète

Avant de rendre le repository public :

- [ ] README.md personnalisé (username, description)
- [ ] LICENSE présent et correct
- [ ] .gitignore configuré
- [ ] Tous les fichiers sensibles exclus
- [ ] Code testé localement
- [ ] Questions validées (`python quiz_manager.py`)
- [ ] Links fonctionnels dans README
- [ ] GitHub Pages activé et testé
- [ ] Topics/tags ajoutés
- [ ] Description du repo configurée
- [ ] Social preview image ajoutée
- [ ] Premier release créé
- [ ] CONTRIBUTING.md clair
- [ ] Issue templates configurés

---

## 📱 Partager

### Liens à Partager

```
🌐 Demo : https://VOTRE-USERNAME.github.io/secur-sim/
📦 Repo : https://github.com/VOTRE-USERNAME/secur-sim
⭐ Star : https://github.com/VOTRE-USERNAME/secur-sim/stargazers
🐛 Issues : https://github.com/VOTRE-USERNAME/secur-sim/issues
```

### Badges README

Ajouter au début de README.md :

```markdown
![GitHub Stars](https://img.shields.io/github/stars/VOTRE-USERNAME/secur-sim?style=social)
![GitHub Forks](https://img.shields.io/github/forks/VOTRE-USERNAME/secur-sim?style=social)
![GitHub Issues](https://img.shields.io/github/issues/VOTRE-USERNAME/secur-sim)
![GitHub License](https://img.shields.io/github/license/VOTRE-USERNAME/secur-sim)
![GitHub Release](https://img.shields.io/github/v/release/VOTRE-USERNAME/secur-sim)
```

---

## 🆘 Troubleshooting

### Push rejeté

```bash
# Récupérer les changements distants
git pull origin main --rebase

# Re-pousser
git push origin main
```

### Fichiers trop gros

```bash
# Voir les gros fichiers
du -sh * | sort -h

# Supprimer de l'historique Git
git filter-branch --tree-filter 'rm -f gros-fichier' HEAD
```

### GitHub Pages 404

```bash
# Vérifier l'URL exacte
https://VOTRE-USERNAME.github.io/secur-sim/

# Attendre 2-3 minutes après activation

# Forcer le redéploiement
git commit --allow-empty -m "Trigger Pages rebuild"
git push
```

---

## ✅ C'est Fait !

Votre projet SECUR-SIM est maintenant :

✅ Sur GitHub  
✅ En ligne via GitHub Pages  
✅ Accessible publiquement  
✅ Prêt pour les contributions  
✅ Documenté professionnellement  

---

## 🚀 Prochaines Étapes

1. **Partager** : Linkedin, Twitter, Reddit
2. **Promouvoir** : Organisations de secourisme suisses
3. **Contribuer** : Ajouter des questions
4. **Améliorer** : Fonctionnalités v2.1
5. **Communauté** : Encourager les contributions

---

**🎉 Félicitations ! Vous avez mis en ligne SECUR-SIM !**

*Des questions ? [Ouvrir une discussion](https://github.com/VOTRE-USERNAME/secur-sim/discussions)*
