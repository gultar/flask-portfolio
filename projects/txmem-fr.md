# Interface de mémoire de traduction

Il s'agit d'une application React qui sert d'interface utilisateur pour un système de mémoire de traduction. Elle se connecte à une API Python locale qui fournit des segments de traduction et des fichiers associés. L'application permet aux utilisateurs de rechercher des segments de traduction, de visualiser les résultats de recherche et d'accéder à des informations supplémentaires provenant de Linguee.

## Fonctionnalités

L'interface de mémoire de traduction comprend les fonctionnalités suivantes :

- Formulaire de recherche : Les utilisateurs peuvent saisir une requête pour rechercher des segments de traduction.
- Navigation : La barre de navigation offre un moyen pratique de soumettre des requêtes de recherche.
- Résultats de recherche : Affiche les résultats de recherche obtenus à partir de l'API Python.
- Texte actif : Affiche les textes source et cible sélectionnés, avec un segment mis en évidence.
- Intégration de Linguee : Récupère des informations supplémentaires de Linguee liées à la requête de recherche.

## Pour commencer

Pour utiliser l'interface de mémoire de traduction, suivez ces étapes :

1. Assurez-vous d'avoir les dépendances nécessaires installées, y compris Node.js et npm.

2. Clonez le dépôt du projet sur votre machine locale.

3. Installez les dépendances du projet en exécutant la commande suivante :

   ```
   npm install
   ```

4. Lancez le serveur de développement React avec la commande suivante :

   ```
   npm start
   ```

5. Accédez à l'application en ouvrant un navigateur web et en accédant à `http://localhost:3000`.

## Utilisation

1. Saisissez votre requête de recherche dans le formulaire de recherche.

2. Appuyez sur la touche Entrée ou cliquez sur le bouton de recherche pour soumettre la requête.

3. L'application communiquera avec l'API Python locale pour récupérer les résultats de recherche.

4. Une fois les résultats récupérés, ils seront affichés dans le composant des résultats de recherche.

5. Cliquez sur un fichier dans les résultats de recherche pour afficher les textes source et cible correspondants dans le composant du texte actif.

6. Le segment trouvé sera mis en évidence dans le composant du texte actif.

7. Pour faire défiler jusqu'au segment mis en évidence, cliquez sur le bouton "Faire défiler jusqu'au segment".

8. Des informations supplémentaires provenant de Linguee liées à la requête de recherche seront affichées dans le composant Linguee.

## Configuration

L'application est configurée pour communiquer avec l'API Python locale hébergée à l'adresse `http://localhost:5000`. Assurez-vous que l'API est en cours d'exécution et accessible avant d'utiliser l'application. Si votre API est hébergée à une adresse ou un port différent, vous pouvez modifier l'URL de l'API dans les lignes de code suivantes du fichier `App.js` :

```javascript
const response = await fetch(`http://localhost:5000/search?expression=${query}`);
```

```javascript
const response = await fetch(`http://localhost:5000/file?filename=${filename}`);
```

## Dépannage

- Si vous rencontrez des erreurs ou des problèmes lors de l'exécution de l'application, assurez-vous d'avoir suivi correctement les étapes de configuration et que toutes les dépendances sont correctement installées.

- Si l'application échoue à communiquer avec l'API Python, assurez-vous que l'API est en cours d'exécution et accessible. Vérifiez la configuration de l'URL de l'API dans le fichier `App.js`.

- Pour tout autre problème ou question, veuillez vous référer à la documentation ou laisser un problème sur le référentiel git.

## Licence

Ce projet est sous licence [MIT](LICENSE).

## Remerciements

- Cette application a été développée avec React et utilise diverses bibliothèques et composants open-source. Un grand merci à la communauté open-source pour leurs contributions.