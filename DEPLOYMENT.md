# 🚀 Guide de Déploiement - SECUR-SIM

Ce guide explique comment déployer SECUR-SIM sur différentes plateformes.

---

## 📊 Table des Matières

- [GitHub Pages (Recommandé)](#github-pages)
- [Netlify](#netlify)
- [Vercel](#vercel)
- [Serveur Personnel](#serveur-personnel)
- [Docker](#docker)

---

## 🌐 GitHub Pages

### ✅ Avantages

- ✨ **Gratuit** pour les projets publics
- 🚀 **Déploiement automatique** à chaque push
- 🔒 **HTTPS** inclus
- 🌍 **CDN global** rapide
- 📊 **GitHub Actions** intégré

### 📝 Instructions

#### 1. Créer le Repository

```bash
# Initialiser git (si pas déjà fait)
git init
git add .
git commit -m "Initial commit - SECUR-SIM v2.0"

# Créer le repo sur GitHub
# Aller sur github.com → New repository
# Nom : secur-sim
# Public

# Ajouter le remote
git remote add origin https://github.com/VOTRE-USERNAME/secur-sim.git
git branch -M main
git push -u origin main
```

#### 2. Activer GitHub Pages

1. Aller sur votre repository GitHub
2. **Settings** → **Pages**
3. **Source** : Deploy from a branch
4. **Branch** : `main`
5. **Folder** : `/` (root)
6. **Save**

#### 3. Attendre le Déploiement

- GitHub Pages déploie automatiquement en 1-2 minutes
- URL : `https://VOTRE-USERNAME.github.io/secur-sim/`
- Vérifier dans **Actions** pour voir le statut

#### 4. Domaine Personnalisé (Optionnel)

```
Settings → Pages → Custom domain
Entrer : secursim.example.com
```

Configurer DNS :
```
Type: CNAME
Name: secursim
Value: VOTRE-USERNAME.github.io
```

---

## 🎯 Netlify

### ✅ Avantages

- 🚀 **Déploiement ultra-rapide**
- 🔄 **CI/CD automatique**
- 🌍 **CDN global** instantané
- 📊 **Analytics** inclus
- 🔒 **SSL automatique**

### 📝 Instructions

#### Méthode 1 : Drag & Drop

1. Aller sur [netlify.com](https://netlify.com)
2. S'inscrire / Se connecter
3. **Sites** → **Add new site** → **Deploy manually**
4. Glisser-déposer le dossier `secur-sim/`
5. ✨ **C'est en ligne !**

URL générée : `https://random-name-123.netlify.app`

#### Méthode 2 : GitHub Integration

1. **Add new site** → **Import an existing project**
2. **Connect to GitHub**
3. Sélectionner le repository `secur-sim`
4. **Deploy settings** :
   - Build command : (laisser vide)
   - Publish directory : `/`
5. **Deploy site**

### 🔧 Configuration

Créer `netlify.toml` :

```toml
[build]
  publish = "."
  
[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200
  
[[headers]]
  for = "/*"
  [headers.values]
    Cache-Control = "public, max-age=3600"
```

---

## ⚡ Vercel

### ✅ Avantages

- 🚀 **Performance optimale**
- 🔄 **Preview deployments** pour chaque PR
- 🌍 **Edge Network** global
- 📊 **Analytics** intégrés

### 📝 Instructions

#### Via CLI

```bash
# Installer Vercel CLI
npm install -g vercel

# Déployer
cd secur-sim
vercel

# Production
vercel --prod
```

#### Via GitHub

1. Aller sur [vercel.com](https://vercel.com)
2. **Add New Project**
3. **Import Git Repository**
4. Sélectionner `secur-sim`
5. **Deploy**

---

## 🖥️ Serveur Personnel

### Apache

```apache
<VirtualHost *:80>
    ServerName secursim.example.com
    DocumentRoot /var/www/secur-sim
    
    <Directory /var/www/secur-sim>
        Options Indexes FollowSymLinks
        AllowOverride All
        Require all granted
    </Directory>
    
    ErrorLog ${APACHE_LOG_DIR}/secursim_error.log
    CustomLog ${APACHE_LOG_DIR}/secursim_access.log combined
</VirtualHost>
```

### Nginx

```nginx
server {
    listen 80;
    server_name secursim.example.com;
    root /var/www/secur-sim;
    index index.html;
    
    location / {
        try_files $uri $uri/ /index.html;
    }
    
    # Cache static assets
    location ~* \.(js|css|png|jpg|jpeg|gif|ico|svg)$ {
        expires 1y;
        add_header Cache-Control "public, immutable";
    }
}
```

---

## 🐳 Docker

### Dockerfile

```dockerfile
FROM nginx:alpine

# Copier les fichiers
COPY . /usr/share/nginx/html

# Configuration nginx
RUN echo 'server { \
    listen 80; \
    location / { \
        root /usr/share/nginx/html; \
        index index.html; \
        try_files $uri $uri/ /index.html; \
    } \
}' > /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
```

### docker-compose.yml

```yaml
version: '3.8'

services:
  secursim:
    build: .
    ports:
      - "80:80"
    restart: unless-stopped
```

### Commandes

```bash
# Build
docker build -t secur-sim .

# Run
docker run -d -p 8080:80 secur-sim

# Avec docker-compose
docker-compose up -d
```

---

## 🔒 HTTPS / SSL

### Let's Encrypt (Certbot)

```bash
# Installer certbot
sudo apt install certbot python3-certbot-nginx

# Obtenir certificat
sudo certbot --nginx -d secursim.example.com

# Renouvellement automatique
sudo certbot renew --dry-run
```

---

## 📊 Monitoring

### Google Analytics

Ajouter dans `index.html` avant `</head>` :

```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

### Plausible Analytics (Privacy-friendly)

```html
<script defer data-domain="secursim.example.com" src="https://plausible.io/js/script.js"></script>
```

---

## 🔄 CI/CD

### GitHub Actions (Automatique)

GitHub Pages déploie automatiquement. Pour personnaliser :

`.github/workflows/deploy.yml` :

```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Validate Questions
        run: python quiz_manager.py
      
      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./
```

---

## ✅ Checklist de Déploiement

Avant de déployer en production :

- [ ] Toutes les questions validées avec `quiz_manager.py`
- [ ] Tests sur plusieurs navigateurs (Chrome, Firefox, Safari)
- [ ] Tests sur mobile (iOS, Android)
- [ ] Pas d'erreurs dans la console
- [ ] Performances vérifiées (Lighthouse)
- [ ] HTTPS activé
- [ ] Analytics configuré
- [ ] `README.md` à jour
- [ ] `CHANGELOG.md` à jour
- [ ] Git tags créés pour la version

---

## 🆘 Troubleshooting

### GitHub Pages ne se déploie pas

```bash
# Vérifier le statut
# Repository → Actions → Voir les logs

# Forcer le redéploiement
git commit --allow-empty -m "Trigger deployment"
git push
```

### 404 sur GitHub Pages

- Vérifier que `index.html` est à la racine
- Attendre 2-3 minutes après activation
- Vider le cache : Ctrl+Shift+R

### Styles ne chargent pas

```html
<!-- Vérifier les chemins relatifs -->
<link href="./css/style.css">  ❌
<link href="css/style.css">    ✅
```

---

## 📞 Support

Besoin d'aide ?

- 📖 [Documentation complète](README.md)
- 🐛 [Signaler un problème](https://github.com/yourusername/secur-sim/issues)
- 💬 [Discussions](https://github.com/yourusername/secur-sim/discussions)

---

**🎉 Félicitations pour votre déploiement !**
