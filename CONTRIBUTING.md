# 🤝 Guide de Contribution - SECUR-SIM

Merci de contribuer à SECUR-SIM ! Ce guide vous aidera à participer au projet.

---

## 📋 Table des Matières

- [Code de Conduite](#code-de-conduite)
- [Comment Contribuer](#comment-contribuer)
- [Ajouter des Questions](#ajouter-des-questions)
- [Signaler un Bug](#signaler-un-bug)
- [Proposer une Fonctionnalité](#proposer-une-fonctionnalité)
- [Process de Pull Request](#process-de-pull-request)
- [Style de Code](#style-de-code)

---

## 📜 Code de Conduite

En participant à ce projet, vous acceptez de respecter notre code de conduite :

- 🤝 Être respectueux et inclusif
- 💬 Communiquer de manière constructive
- 🎯 Rester focalisé sur l'objectif : améliorer la formation au secourisme
- 🚫 Ne pas tolérer le harcèlement ou les comportements inappropriés

---

## 🛠️ Comment Contribuer

### 1. Fork & Clone

```bash
# Fork le projet sur GitHub (bouton "Fork")

# Clone ton fork
git clone https://github.com/ton-username/secur-sim.git
cd secur-sim

# Ajouter l'upstream
git remote add upstream https://github.com/original-owner/secur-sim.git
```

### 2. Créer une Branche

```bash
# Créer une branche depuis main
git checkout -b feature/ma-nouvelle-fonctionnalite

# Types de branches recommandées :
# feature/nom-fonctionnalite
# fix/nom-bug
# docs/nom-documentation
# refactor/nom-refactoring
```

### 3. Faire les Modifications

Faites vos changements en suivant les guidelines ci-dessous.

### 4. Tester

```bash
# Ouvrir dans le navigateur et tester
open index.html

# Si ajout de questions : valider
Valider le JSON sur jsonlint.com 1  # ou 2, 3
```

### 5. Commit & Push

```bash
# Ajouter les fichiers
git add .

# Commit avec message clair
git commit -m "feat: Ajout de 10 nouvelles questions RCP niveau 1"

# Format des commits :
# feat: Nouvelle fonctionnalité
# fix: Correction de bug
# docs: Documentation
# refactor: Refactoring
# test: Tests
# chore: Maintenance

# Push vers ton fork
git push origin feature/ma-nouvelle-fonctionnalite
```

### 6. Créer une Pull Request

- Aller sur GitHub
- Cliquer "New Pull Request"
- Remplir le template (titre + description)
- Attendre la review !

---

## 📝 Ajouter des Questions

### Format JSON

```json
{
  "id": "n1_q050",
  "titre": "Titre court et descriptif",
  "cas_clinique": "Description détaillée du cas (200-400 caractères recommandés)",
  "question": "Question claire et précise ?",
  "options": [
    {
      "id": "a",
      "texte": "Première option",
      "correct": false,
      "explication": "Pourquoi c'est incorrect",
      "source": "Référence officielle"
    },
    {
      "id": "b",
      "texte": "Deuxième option (CORRECTE)",
      "correct": true,
      "explication": "Pourquoi c'est correct",
      "complement": "Information supplémentaire utile",
      "source": "Référence officielle avec page si possible"
    },
    {
      "id": "c",
      "texte": "Troisième option",
      "correct": false,
      "explication": "Pourquoi c'est incorrect",
      "source": "Référence"
    },
    {
      "id": "d",
      "texte": "Quatrième option",
      "correct": false,
      "explication": "Pourquoi c'est incorrect",
      "source": "Référence"
    }
  ],
  "points": 10,
  "temps_recommande": 90,
  "tags": ["tag1", "tag2", "tag3"],
  "difficulte": 2
}
```

### Checklist Qualité

Avant de soumettre une question, vérifier :

- [ ] ID unique (n[niveau]_q[numero])
- [ ] Cas clinique réaliste (200-400 caractères)
- [ ] Exactement 4 options (a, b, c, d)
- [ ] Exactement 1 réponse correcte
- [ ] Toutes les options ont une explication
- [ ] La réponse correcte a un complément
- [ ] Sources vérifiables citées
- [ ] Au moins 1 tag pertinent
- [ ] Difficulté définie (1-3)
- [ ] Validation réussie : `Valider le JSON sur jsonlint.com [niveau]`
- [ ] Testé dans le quiz web

### Sources Acceptées

**Niveau 1** :
- Guidelines BLS-AED-SRC 2021
- Référentiel Samaritains FSS
- ERC Guidelines 2021

**Niveau 2** :
- Référentiel First Responder IAS 2023
- PHTLS 9th Edition
- Protocoles cantonaux 144

**Niveau 3** :
- Référentiel IAS MedCat 2023
- Guide KSBS 2022
- Directive fédérale CBRN 2021
- WHO Emergency Response Framework

---

## 🐛 Signaler un Bug

### Template

```markdown
**Description**
Description claire du bug

**Reproduction**
1. Aller sur '...'
2. Cliquer sur '...'
3. Observer '...'

**Comportement Attendu**
Ce qui devrait se passer

**Screenshots**
Si applicable

**Environnement**
- Navigateur: [Chrome 120]
- OS: [macOS 14]
- Version: [2.0]
```

**Labels** : `bug`, `high-priority`, `documentation`, etc.

---

## 💡 Proposer une Fonctionnalité

### Template

```markdown
**Problème**
Quel problème cette fonctionnalité résout ?

**Solution Proposée**
Description de la solution

**Alternatives Considérées**
Autres approches envisagées

**Contexte Additionnel**
Informations supplémentaires
```

**Labels** : `enhancement`, `feature`, `discussion`

---

## 🔄 Process de Pull Request

### Avant de Soumettre

- [ ] Code testé localement
- [ ] Questions validées avec validateur JSON en ligne
- [ ] Pas de conflits avec `main`
- [ ] Commits clairs et atomiques
- [ ] Documentation mise à jour si nécessaire

### Template PR

```markdown
## Description
Brève description des changements

## Type de Changement
- [ ] 🐛 Bug fix
- [ ] ✨ Nouvelle fonctionnalité
- [ ] 📝 Documentation
- [ ] 🔧 Refactoring

## Checklist
- [ ] Tests passés
- [ ] Code review auto-effectuée
- [ ] Documentation mise à jour
- [ ] Pas de warnings console
```

### Review Process

1. **Soumission** → PR créée
2. **Review** → Au moins 1 approbation requise
3. **CI/CD** → Tests automatiques (si configurés)
4. **Merge** → Par un mainteneur

---

## 🎨 Style de Code

### HTML

```html
<!-- Indentation : 2 espaces -->
<!-- Attributs : double quotes -->
<div class="container">
  <h1>Titre</h1>
</div>
```

### CSS

```css
/* Indentation : 2 espaces */
/* Ordre : alphabétique */
.container {
  background: white;
  border-radius: 12px;
  padding: 24px;
}
```

### JavaScript

```javascript
// Indentation : 2 espaces
// camelCase pour variables/fonctions
// PascalCase pour classes
// Const par défaut, let si mutation

const myVariable = 'value';

function myFunction() {
  // Code
}
```

### JSON

```json
{
  "id": "n1_q001",
  "indentation": "2 espaces",
  "ordre": "alphabétique des clés si pertinent"
}
```

---

## 📚 Ressources

- **Documentation** : `/docs/`
- **Guide Questions** : `GUIDE-CREATION-QUESTIONS.md`
- **Structure** : `STRUCTURE-100-QUESTIONS.md`
- **Sources** : `assets/sources.md`

---

## 🎯 Priorités Actuelles

**v2.1 - Questions**
- [ ] Compléter Niveau 1 à 100 questions
- [ ] Compléter Niveau 2 à 100 questions
- [ ] Compléter Niveau 3 à 100 questions

**v2.1 - Features**
- [ ] Mode entraînement
- [ ] Export PDF résultats
- [ ] Statistiques par thématique

**v3.0 - Future**
- [ ] Compte utilisateur
- [ ] Mode multijoueur
- [ ] API

---

## 💬 Questions ?

- **GitHub Discussions** : [Poser une question](https://github.com/yourusername/secur-sim/discussions)
- **Issues** : [Ouvrir une issue](https://github.com/yourusername/secur-sim/issues)

---

## 🙏 Merci !

Chaque contribution compte, qu'elle soit grande ou petite. Merci de nous aider à améliorer la formation au secourisme ! 🚑

---

<div align="center">

**Développé avec ❤️ pour sauver des vies**

</div>
