![lisa](/static/images/lisa-lexica-3.jfif)

# Lisa - Assistant Personnel d'IA 💁‍♀️🤖

Lisa est votre assistant personnel d'IA conçu pour fournir une interface conversationnelle pour des interactions fluides. Alimentée par le traitement du langage naturel et la gestion des conversations, Lisa comprend vos requêtes et fournit des réponses pertinentes.

## Prérequis 🛠️

Avant d'exécuter le script, assurez-vous d'avoir les dépendances suivantes installées :

- La bibliothèque `langchain`
- La bibliothèque `dotenv`
- La bibliothèque `pyttsx3`
- La bibliothèque `duckduckgo_search`
- La bibliothèque `geocoder`

Vous pouvez installer les dépendances en utilisant la commande suivante :

```
pip install -r requirements.txt
```

## Configuration ⚙️

Suivez ces étapes pour configurer et exécuter Lisa :

1. Clonez le dépôt et accédez au répertoire du projet.
2. Créez un fichier `.env` dans le répertoire du projet et définissez les variables d'environnement suivantes :
   - `OPENAI_API_KEY` : Votre clé d'API OpenAI obtenue sur le site OpenAI.
3. Exécutez l'assistant en utilisant la commande :

   ```
   python assistant.py
   ```

## Utilisation 🚀

Une fois le script en cours d'exécution, vous pouvez interagir avec Lisa via la ligne de commande ou via des commandes vocales, en fonction du mode choisi.

## Options 🎌

Le script prend en charge les options suivantes :

- `-t` ou `--text` : Active l'interaction basée sur le texte.
- `-s` ou `--silent` : Désactive la synthèse vocale pour les réponses.

### Interaction basée sur le texte ✍️

Si vous préférez une interaction basée sur le texte, suivez ces étapes :

1. Lorsque vous êtes invité avec "Que puis-je faire pour vous ?", saisissez votre requête ou commande.
2. Lisa traitera votre saisie et fournira une réponse.

### Interaction vocale 🗣️

Si vous préférez une interaction basée sur la voix, suivez ces étapes :

1. Assurez-vous que votre microphone est configuré et fonctionne.
2. Dites "Hé", "Attention" ou "Lisa" pour réveiller Lisa et attendez le son de confirmation.
3. Prononcez clairement votre requête ou commande.
4. Lisa traitera votre parole et fournira une réponse.

### Confirmation ✅

Après avoir reçu une requête ou une commande, Lisa confirmera ce qu'elle a compris. Si la confirmation est incorrecte, vous pouvez répondre par "non" pour fournir la requête ou la commande correcte.

### Quitter le programme 🚪

Pour arrêter le script et quitter le programme, dites "annuler" ou appuyez sur `CTRL+C`.

## Informations supplémentaires ℹ️

- Lisa utilise le modèle `gpt-3.5-turbo` d'OpenAI pour générer des réponses.
- La bibliothèque Langchain est utilisée pour la gestion des conversations et les tâches de traitement du langage naturel.
- La classe `Agent` de Langchain gère le flux de conversation et génère des réponses.
- La classe `Attention` gère les commandes vocales et réveille Lisa.
- La fonction `speak()` produit des réponses sous forme de voix.
- La fonction `listen()` convertit l'entrée vocale en texte.
- La fonction `make_tools()` initialise les outils utilisés par l'Agent pour différentes tâches.
- La fonction `create_agent()` initialise l'agent Langchain avec le modèle `gpt-3.5-turbo` et les outils de conversation.
- La fonction `ask_lisa()` prend une requête en entrée et génère une réponse en utilisant l'agent Langchain.
- La fonction `lisa_answers()` gère la sortie des réponses de Lisa en fonction de la préférence de l'utilisateur (texte ou voix).
- La fonction `receive_query()` gère les requêtes ou commandes de l'utilisateur en fonction du mode d'entrée (texte ou voix).
- La fonction `start()` sert de point d'entrée du script et gère la boucle principale de conversation.

Veuillez noter que cette implémentation est une version simplifiée et peut ne pas couvrir tous les cas d'utilisation possibles. Vous pouvez l'étendre et la modifier pour répondre à vos besoins spécifiques afin de créer un assistant personnel plus sophistiqué.