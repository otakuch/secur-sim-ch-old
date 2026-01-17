# 🚑 SECUR-SIM - Version Standalone

## ✨ Version 100% HTML - Un Seul Fichier !

Cette version est **ultra-simple** : tout est dans un seul fichier HTML.

---

## 📦 Fichier Principal

### **secur-sim-standalone.html** (240 KB)

**Contient** :
- ✅ HTML complet
- ✅ CSS intégré
- ✅ JavaScript intégré
- ✅ **60 questions** intégrées (20 par niveau)
- ✅ Système de quiz complet
- ✅ Résultats avec badges
- ✅ Design responsive

**Aucun fichier externe nécessaire !**

---

## 🚀 Utilisation

### Méthode 1 : Double-clic

```
1. Ouvrir le dossier
2. Double-cliquer sur "secur-sim-standalone.html"
3. ✅ Le quiz s'ouvre dans votre navigateur !
```

### Méthode 2 : Glisser-déposer

```
1. Glisser "secur-sim-standalone.html" dans un navigateur
2. ✅ Ça fonctionne immédiatement !
```

---

## 📝 Contenu

### 20 Questions par Niveau

#### Niveau 1 - BLS-AED (20 questions)
- Arrêt cardiaque et RCP
- Fréquence et profondeur des compressions
- Position des mains
- Ratio compressions/insufflations
- Utilisation du DEA
- Hémorragie externe
- Position latérale de sécurité
- Obstruction voies aériennes
- Brûlures
- Malaise vagal
- Choc anaphylactique
- Traumatisme crânien
- Fractures
- Crise d'épilepsie
- Hypoglycémie
- Saignement de nez
- Piqûre de guêpe
- Hypothermie
- Appel d'urgence 144

#### Niveau 2 - First Responder (10 questions)
- Évaluation ABCDE
- Oxygénothérapie
- Choc hémorragique
- Trauma thoracique
- Trauma rachidien
- Glasgow Coma Scale
- Œdème pulmonaire aigu
- AVC (test FAST)
- Infarctus du myocarde
- Transmission au 144

#### Niveau 3 - Catastrophe (10 questions)
- Triage START
- Catégories T1, T2, T3, T4
- Temps de remplissage capillaire
- Chaîne de commandement
- Point de rassemblement
- Événement CBRN
- Zonage catastrophe
- Ressources limitées
- Communication POLYCOM
- Noria ambulancière

---

## 🎯 Fonctionnalités

### Quiz Interactif

- ✅ Sélection du niveau (1, 2 ou 3)
- ✅ 20 questions par niveau
- ✅ Feedback immédiat après chaque réponse
- ✅ Explications détaillées
- ✅ Sources citées
- ✅ Score en temps réel

### Résultats

- ✅ Score final en pourcentage
- ✅ Badges (Or ≥80%, Argent ≥60%, Bronze <60%)
- ✅ Possibilité de recommencer
- ✅ Retour au menu

### Design

- ✅ Interface moderne et propre
- ✅ Responsive (mobile, tablette, desktop)
- ✅ Couleurs par niveau (bleu, violet, rouge)
- ✅ Animations fluides

---

## 📱 Responsive

Fonctionne parfaitement sur :

- ✅ Mobile (< 600px)
- ✅ Tablette (600-1024px)
- ✅ Desktop (> 1024px)

---

## 🔧 Avantages

### Par rapport à la version complète :

✅ **Un seul fichier** - Pas de dossiers, pas de structure
✅ **Aucune dépendance** - Pas de JSON, pas de JS externes
✅ **Fonctionne offline** - 100% autonome
✅ **Facile à partager** - Envoyer par email, USB, etc.
✅ **Pas de serveur nécessaire** - Double-clic et ça marche
✅ **Pas de problèmes de chemins** - Tout est dans un fichier

---

## 📊 Comparaison

| Fonctionnalité | Standalone | Version Complète |
|----------------|------------|------------------|
| **Fichiers** | 1 fichier | 30+ fichiers |
| **Taille** | 240 KB | 500+ KB |
| **Questions** | 60 (20/niveau) | 38 questions |
| **Installation** | Double-clic | Structure à respecter |
| **Modification questions** | Éditer HTML | Éditer JSON |
| **Déploiement** | Copier 1 fichier | Copier dossier |
| **Hors ligne** | ✅ | ✅ |
| **Responsive** | ✅ | ✅ |

---

## 🎓 Cas d'Usage

### Quand utiliser la version Standalone ?

✅ **Partage rapide** : Envoyer le quiz par email
✅ **Présentation** : Ouvrir sur n'importe quel PC
✅ **Formation** : Utiliser en cours sans internet
✅ **USB** : Mettre sur clé USB pour distribution
✅ **Simplicité** : Pas de connaissances techniques requises
✅ **Démo** : Montrer rapidement le quiz

### Quand utiliser la version Complète ?

✅ **GitHub Pages** : Héberger en ligne
✅ **Personnalisation** : Modifier facilement les questions
✅ **Évolutivité** : Ajouter des fonctionnalités
✅ **Collaboration** : Plusieurs personnes modifient
✅ **Documentation** : Guides complets inclus

---

## 📝 Modifier les Questions

### 1. Ouvrir le fichier

```
Ouvrir "secur-sim-standalone.html" avec un éditeur de texte :
- VS Code
- Sublime Text
- Notepad++
- Bloc-notes (Windows)
```

### 2. Trouver la base de données

```javascript
// Chercher (Ctrl+F) :
const questionsDB = {
```

### 3. Modifier une question

```javascript
{
    titre: "Mon titre",
    cas: "Description du cas...",
    question: "Ma question ?",
    options: [
        { 
            text: "Option A", 
            correct: false, 
            explication: "Pourquoi incorrect", 
            source: "Source" 
        },
        { 
            text: "Option B (correcte)", 
            correct: true, 
            explication: "Pourquoi correct", 
            complement: "Info supplémentaire",
            source: "Source" 
        }
        // ... 2 autres options
    ]
}
```

### 4. Sauvegarder et tester

```
1. Sauvegarder le fichier
2. Ouvrir dans le navigateur
3. Tester la question modifiée
```

---

## 🧪 Test

### Vérifications

- [ ] Ouvrir le fichier → fonctionne
- [ ] Sélectionner niveau 1 → 20 questions
- [ ] Répondre à une question → feedback correct
- [ ] Finir le quiz → résultats affichés
- [ ] Cliquer "Recommencer" → fonctionne
- [ ] Tester sur mobile → responsive OK
- [ ] Tester offline → fonctionne

---

## 🆘 Problèmes Courants

### Le fichier ne s'ouvre pas

**Solution** :
```
1. Clic droit → Ouvrir avec
2. Choisir un navigateur (Chrome, Firefox, Edge)
```

### Les questions ne s'affichent pas

**Solution** :
```
1. F12 → Console
2. Vérifier les erreurs JavaScript
3. Vérifier que le navigateur supporte ES6
```

### Modifications non prises en compte

**Solution** :
```
1. Vider le cache : Ctrl+Shift+R
2. Ou ouvrir en navigation privée
```

---

## 💡 Astuces

### Partage

**Par email** :
```
Attacher "secur-sim-standalone.html"
Taille : 240 KB (passe sans problème)
```

**Par USB** :
```
Copier le fichier sur la clé
Utiliser sur n'importe quel PC
```

**Par QR Code** :
```
Héberger sur un serveur
Générer QR code vers l'URL
Scanner pour accéder
```

### Impression

```
1. Ouvrir le quiz
2. Ctrl+P (Imprimer)
3. Les questions s'impriment proprement
```

---

## 🌟 Points Forts

### Simplicité Extrême

✅ Un seul fichier
✅ Double-clic et ça marche
✅ Aucune configuration
✅ Fonctionne partout

### Autonomie Totale

✅ Pas d'internet requis
✅ Pas de serveur
✅ Pas de dépendances
✅ 100% autonome

### Facilité de Partage

✅ Email (240 KB)
✅ USB
✅ Cloud (Dropbox, Drive)
✅ QR Code

---

## 📈 Évolution

### Version actuelle : 1.0

- 60 questions (20 par niveau)
- 3 niveaux
- Quiz complet fonctionnel
- Responsive
- Badges

### Prochaines versions potentielles

- [ ] Plus de questions (100 par niveau)
- [ ] Timer par question
- [ ] Sauvegarde score
- [ ] Mode examen
- [ ] Export résultats PDF
- [ ] Statistiques détaillées

---

## 📞 Support

### Questions ?

Si le fichier standalone ne fonctionne pas :

1. **Vérifier** que JavaScript est activé dans le navigateur
2. **Tester** avec un autre navigateur (Chrome, Firefox)
3. **Vider** le cache (Ctrl+Shift+R)
4. **Consulter** la console (F12) pour les erreurs

---

<div align="center">

**🚑 SECUR-SIM Standalone v1.0**

*Un fichier • 60 questions • 100% fonctionnel*

**Simplicité maximale • Efficacité garantie**

**Télécharge, double-clique, joue ! 🎯**

</div>
