![albanil](/static/images/albanil-lexica.jfif)

# Albañil - Un générateur d'applications basé sur des spécifications

Albañil est un constructeur d'applications personnel qui vous aide à créer des applications en fonction d'un ensemble de spécifications fournies par l'utilisateur. Il génère la structure de fichiers et le code de l'application en fonction des spécifications données.

## Prérequis

Avant d'utiliser Albañil, assurez-vous d'avoir ce qui suit :

- Python 3.x installé sur votre système.
- Les packages Python requis installés. Vous pouvez les installer en exécutant la commande suivante :

  ```shell
  pip install -r requirements.txt
  ```

## Pour commencer

1. Clonez le dépôt :

   ```shell
   git clone https://github.com/gultar/albanil.git
   cd albanil
   ```

2. Installez les dépendances :

   ```shell
   pip install -r requirements.txt
   ```

3. Configurez les variables d'environnement :

   Créez un fichier `.env` dans le répertoire du projet et fournissez les variables suivantes :

   ```
   OPENAI_API_KEY=votre_clé_api_openai
   ```

   Remplacez `votre_clé_api_openai` par votre clé d'API OpenAI.

4. Lancez l'application :

   ```shell
   python albanil.py [-f FILE] [-y]
   ```

   Les arguments facultatifs sont les suivants :

   - `-f FILE` ou `--file FILE` : Spécifiez un fichier `.md` à utiliser comme valeur de la variable `spec`.
   - `-y` ou `--yes` : Acceptez automatiquement tous les fichiers créés sans confirmation de l'utilisateur.

   Si l'option `-f` n'est pas fournie, l'application vous demandera de fournir les détails de l'application que vous souhaitez créer.

## Utilisation

1. Lancez l'application en utilisant la commande mentionnée dans la section "Pour commencer".

2. L'application affichera les spécifications de l'application et vous demandera de fournir les chemins d'accès aux fichiers et leurs descriptions au format paire clé/valeur JSON.

3. Entrez les données JSON contenant les chemins d'accès aux fichiers et les descriptions. L'application créera la structure de fichiers de l'application dans le dossier `./generated`.

4. Pour chaque fichier de la structure de fichiers, l'application vous demandera d'écrire le code du fichier. Seul le code doit être fourni, sans aucune explication, reconnaissance, commentaire ou style Markdown.

5. Après avoir écrit le code d'un fichier, l'application créera le fichier et y enregistrera le contenu du code.

6. Si l'option `-y` est fournie, l'application procédera automatiquement avec chaque fichier sans demander de confirmation à l'utilisateur. Sinon, on vous demandera de confirmer si vous souhaitez continuer avec chaque fichier.

7. Une fois que tous les fichiers ont été créés, l'application affichera un message indiquant la fin du processus de création des fichiers.

## Licence

Ce projet est sous licence [MIT](LICENSE).