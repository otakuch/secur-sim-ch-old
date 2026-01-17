# 🚀 Guide de Démarrage Rapide - SECUR-SIM

## ⚡ En 30 Secondes

```bash
# 1. Cloner
git clone https://github.com/yourusername/secur-sim.git
cd secur-sim

# 2. Ouvrir
open index.html  # macOS
# OU double-cliquer sur index.html

# 3. Jouer !
# Choisir un niveau et commencer le quiz
```

---

## 🎯 Premiers Pas

### 1. Choisir un Niveau

**Niveau 1 - BLS-AED** (Débutant)
- Réanimation cardio-pulmonaire
- Défibrillateur automatique
- Premiers secours de base

**Niveau 2 - First Responder** (Intermédiaire)
- Évaluation ABCDE
- Traumatologie
- Urgences médicales

**Niveau 3 - Médecine de Catastrophe** (Avancé)
- Triage START
- Gestion CBRN
- Afflux massif de victimes

### 2. Répondre aux Questions

- 📝 **20 questions** sélectionnées aléatoirement
- ⏱️ **Timer** pour suivre votre temps
- 📊 **Progression** affichée en temps réel

### 3. Obtenir le Feedback

Après chaque réponse :
- ✅ / ❌ Indication correcte/incorrecte
- 💡 **Explication** détaillée
- ➕ **Complément** d'information (si bonne réponse)
- 📚 **Source** vérifiable

### 4. Consulter les Résultats

À la fin du quiz :
- 🎯 **Score** en pourcentage
- 🏅 **Badge** (Or/Argent/Bronze)
- 📈 **Statistiques** (temps moyen, taux de réussite)
- 💬 **Recommandations** personnalisées

### 5. Rejouer

Cliquez sur **"🎲 Nouveau tirage"** pour obtenir 20 nouvelles questions !

---

## 🛠️ Développement Local

### Avec Serveur HTTP

```bash
# Python 3
python -m http.server 8000
# Ouvrir : http://localhost:8000

# Node.js
npx http-server
# Ouvrir : http://localhost:8080

# PHP
php -S localhost:8000
```

### Sans Serveur

Double-cliquer sur `index.html` fonctionne parfaitement !

---

## 📝 Ajouter des Questions

### 1. Éditer le Fichier JSON

```bash
# Ouvrir le fichier du niveau souhaité
vim data/niveau1.json  # ou niveau2.json, niveau3.json
```

### 2. Ajouter une Question

```json
{
  "id": "n1_q050",
  "titre": "Titre court",
  "cas_clinique": "Description du cas...",
  "question": "Votre question ?",
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
    // options c et d...
  ],
  "points": 10,
  "temps_recommande": 60,
  "tags": ["tag1", "tag2"],
  "difficulte": 1
}
```

### 3. Valider

```bash
python quiz_manager.py validate 1  # ou 2, 3
```

### 4. Tester

Ouvrir `index.html` et tester la nouvelle question !

---

## 🎨 Personnalisation

### Modifier les Couleurs

Éditer `css/style.css` :

```css
:root {
  --primary: #3B82F6;        /* Couleur principale */
  --primary-dark: #2563EB;   /* Couleur foncée */
  --success: #10B981;        /* Succès (vert) */
  --danger: #DC2626;         /* Erreur (rouge) */
}
```

### Modifier le Logo

Remplacer dans `index.html` :

```html
<div class="logo-icon">🚑</div>  <!-- Changer l'emoji -->
```

### Modifier le Nombre de Questions

Par défaut : 20 questions par session

Éditer `js/quiz-engine.js` ligne ~35 :

```javascript
// Changer 20 par le nombre souhaité
questions = shuffled.slice(0, 20);  // ← Modifier ici
```

---

## 🚀 Déploiement

### GitHub Pages (Gratuit)

1. Fork le repository
2. **Settings** → **Pages**
3. **Source** : Deploy from `main`
4. **Save**
5. Accéder à : `https://yourusername.github.io/secur-sim/`

### Netlify (Gratuit)

1. Aller sur [netlify.com](https://netlify.com)
2. Drag & drop le dossier `secur-sim`
3. C'est en ligne ! ✨

### Vercel (Gratuit)

```bash
npm install -g vercel
cd secur-sim
vercel
```

---

## 📚 Documentation Complète

- **[README.md](README.md)** - Vue d'ensemble
- **[CONTRIBUTING.md](CONTRIBUTING.md)** - Guide de contribution
- **[docs/GUIDE-CREATION-QUESTIONS.md](docs/GUIDE-CREATION-QUESTIONS.md)** - Créer des questions
- **[docs/STRUCTURE-100-QUESTIONS.md](docs/STRUCTURE-100-QUESTIONS.md)** - Architecture du système

---

## 🆘 Aide

### Problèmes Courants

**Q: Les questions ne se chargent pas**
```bash
# Vérifier que le fichier JSON est valide
python -m json.tool data/niveau1.json
```

**Q: Le timer ne fonctionne pas**
- Vérifier la console (F12) pour les erreurs
- S'assurer que JavaScript est activé

**Q: Les styles ne s'affichent pas**
- Vérifier que `css/style.css` existe
- Forcer le rechargement : Ctrl+Shift+R

### Support

- **Issues** : [GitHub Issues](https://github.com/yourusername/secur-sim/issues)
- **Discussions** : [GitHub Discussions](https://github.com/yourusername/secur-sim/discussions)

---

## ✅ Checklist Premier Lancement

- [ ] Repository cloné
- [ ] `index.html` ouvert dans le navigateur
- [ ] Aucune erreur dans la console (F12)
- [ ] Niveau 1 testé
- [ ] Questions aléatoires vérifiées (rejouer 2 fois)
- [ ] Page de résultats consultée
- [ ] Documentation parcourue

---

**🎉 Félicitations ! Vous êtes prêt à utiliser SECUR-SIM !**

*Des questions ? [Ouvrir une issue](https://github.com/yourusername/secur-sim/issues)*
