# Tundra OS ❄️🖥️

Un environnement de bureau alimenté par Electron conçu pour offrir une expérience utilisateur fluide.

## Prérequis 🛠️

Pour utiliser Tundra OS, assurez-vous d'avoir Node.js et NPM (Node Package Manager) installés. Il est recommandé d'utiliser un système Linux ou Windows Subsystem for Linux (WSL), bien que l'environnement soit également compatible avec Windows, avec quelques limitations potentielles.

Pour installer Node.js, exécutez les commandes suivantes :

```
curl -fsSL https://deb.nodesource.com/setup_14.x | sudo -E bash -
```

Ensuite, installez le package Node.js en exécutant :

```
sudo apt-get install -y nodejs
```

Alternativement, vous pouvez visiter le [site Web de Node.js](https://nodejs.org/en/) et suivre les étapes fournies.

## Installation 🚀

Pour commencer avec Tundra OS, suivez ces étapes :

1. Clonez le dépôt en exécutant la commande :

   ```
   git clone https://github.com/gultar/workspace
   ```

2. Installez toutes les dépendances nécessaires en exécutant :

   ```
   npm install
   ```

## Exécution 🏃

Si vous utilisez Tundra OS sur Windows, il est recommandé d'entrer dans le Windows Subsystem for Linux (WSL) car le projet a été principalement conçu pour Linux.

Pour lancer l'application avec un système de fichiers intégré à la racine du répertoire du projet, exécutez la commande suivante :

```
npm run electron
```

Alternativement, si vous souhaitez avoir accès à l'ensemble du système de fichiers Linux, utilisez la commande suivante :

```
npm run electron-full
```

## API 📚

Tundra OS propose les outils d'API suivants :

- **ApplicationWindow** : Une instance d'ApplicationWindow sert d'enveloppe pour la bibliothèque WinBox, permettant la création de fenêtres flexibles, élégantes et personnalisables. Elle permet de sauvegarder et de charger des états de fenêtres, ce qui est pratique pour les développeurs pour recharger les modifications apportées à la partie frontale de leurs applications sans les rouvrir.

- **Editor** : L'outil Editor lance un éditeur de code simple et cool alimenté par Ace, avec des fonctionnalités de gestion de fichiers. Initialisez-le avec le chemin souhaité vers un fichier.

- **Exec Command and Directory Pointers** : Pour interagir avec le système de fichiers virtuel, utilisez des identifiants de pointeurs de répertoire uniques et incluez-les dans les commandes du système de fichiers. Les "pointeurs" de répertoire référencent les répertoires via des références circulaires vers leur répertoire parent. La création d'une fonction d'encapsulation peut aider à simplifier le processus. N'oubliez pas de détruire le pointeur lorsque vous avez terminé.

## Développé par ✨

Sacha-Olivier Dulac

Profitez de l'utilisation de Tundra OS et explorez l'environnement de bureau fluide alimenté par Electron qu'il offre ! ❄️🖥️