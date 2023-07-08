# Ariane's Thread - Cadre de la blockchain

Une plateforme de blockchain basée sur Node.js, Socket.io et Rocket-Store avec prise en charge de contrats intelligents écrits en JavaScript et un protocole de consensus pluggable. La plateforme est livrée avec des fonctionnalités de preuve de travail (Proof of Work) et de permission. Il s'agit toujours d'un travail en cours et il le restera probablement pendant un certain temps, mais n'hésitez pas à me contacter ou à contribuer à ce projet, car j'aimerais le voir utilisé à bon escient.

### Prérequis

- Node.js (dernière version)

## Pour commencer

Vous devez cloner le dépôt dans un dossier

```
git clone https://github.com/gultar/blockchain
cd ./blockchain
```

Ensuite, vous devez installer Node.js, si ce n'est pas déjà fait

```
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

Pour mettre en marche la blockchain, vous devez d'abord obtenir toutes les dépendances

```
npm install
```

### Configuration de la blockchain

Presque toutes les configurations pour la génération de blocs se trouvent dans le fichier ./config/genesis.json.

```
{
  "blockNumber": 0,
  "timestamp": 1554987342039,
  "transactions": {
    "maxCurrency": {
      "fromAddress": "coinbase",
      "toAddress": "coinbase",
      "amount": 1000000000000,
      "data": "Maximum allowed currency in circulation",
      "type": "coinbaseReserve",
      "hash": false,
      "miningFee": 0,
      "timestamp": 1554987342039,
      "nonce": 0,
      "delayToBlock": 0
    }
  },
  "actions": {},
  "previousHash": "",
  "totalDifficulty": "0x1024",
  "difficulty": "0x1024",
  "merkleRoot": "59C9BCB224111E86BC4DEA7ECE299BFAA5B1662E88D69BA898BAC09C16D7AD97",
  "nonce": 0,
  "hash": "09899ef0175512358bcee24d5a1c3db63f816ee5eec03bc977df3dd0cb06f7d0",
  "minedBy": "",
  "challenge": "7ee2825ab3eb2ed69d1e7b6a50ca38ffc08ebed2a60a6894b170c24ad79ae",
  "startMineTime": 1554987342039,
  "endMineTime": 0,
  "coinbaseTransactionHash": "",
  "signatures": {},
  "blockTime": 10,
  "consensus": "Proof of Work",
  "network": "mainnet",
  "maxCoinSupply": 10000000000,
  "faucetActive": true,
  "states": {
    "coinbase": {
      "balance": 1000000000000
    },
    "faucet": {
      "balance": 1e+22
    },
    "Axr7tRA4LQyoNZR8PFBPrGTyEs1bWNPj5H9yHGjvF5OG": {
      "balance": 10000
    },
    "AodXnC/TMkd6rcK1m3DLWRM14G/eMuGXWTEHOcH8qQS6": {
      "balance": 10000
    },
    "A2TecK75dMwMUd9ja9TZlbL5sh3/yVQunDbTlr0imZ0R": {
      "balance": 10000
    },
    "A64j8yr8Yl4inPC21GwONHTXDqBR7gutm57mjJ6oWfqr": {
      "balance": 10000
    }
  }
}
```

Vous pouvez définir les soldes des comptes pour l'ICO. D'autres configurations telles que les temps de bloc, la difficulté initiale/minimale et bien plus encore peuvent être définies dans ce fichier. Les configurations par défaut sont celles du réseau principal.

Vous pouvez ensuite définir les configurations réseau de votre nœud dans le fichier ./config/nodeconfig.json

### Connexion à la blockchain

Ensuite, vous pouvez instancier la classe en utilisant

```
let myNode = new Node({
  host: "123.123.123.123", // Si la découverte des pairs DHT est activée, c'est l'adresse IP publique du réseau
  lanHost: "192.168.1.1", // IP interne, facultatif
  port: "8000", 

// Port du serveur io
  verbose: false, // Affiche plus d'informations comme les transactions envoyées
  httpsEnabled: true, // Active l'API HTTP REST
  exposeHTTP: false, // Rend l'API HTTP REST publique
  enableLocalPeerDiscovery: false, // MSSDNS, sur le réseau local
  enableDHTDiscovery: true, // DHT, sur Internet
  peerDiscoveryPort: "6000",
  network: "mainnet", // Nom du réseau auquel se connecter
  noLocalhost: false, // Active les connexions sur le même environnement
  genesis: genesis, // Obtenus depuis ./modules/tools/getGenesis
  minerWorker: false, // Active le worker sur le même processus Node.js mais dans un worker. Non recommandé, sauf sur un petit réseau privé
  clusterMiner: program.clusterMiner, // Nombre de cœurs à utiliser dans le worker. Par défaut : 1
  keychain: program.keychain // En cas de worker de minage, portefeuille et mot de passe
})


let started = await myNode.startServer()
if (started.error) throw new Error(started.error)

myNode.joinPeers();

```

ou en exécutant blockchainCLI.js pour une interface de type CLI.

```
node blockchainCLI.js start <options>
```

Pour obtenir la liste de toutes les options :
```
$ node blockchainCLI.js --help
Usage: blockchainCLI <value> [-options]


  Possible other commands:

  wallet - Pour gérer les portefeuilles et les états des portefeuilles
  sendTx - Pour envoyer des transactions d'un portefeuille à un autre
  action - Pour créer et envoyer une action à un contrat
  chain  - Pour interroger la blockchain pour obtenir des informations
  config - Pour mettre à jour le fichier de configuration du nœud
  pool   - Pour gérer le pool de transactions


Options:
  -V, --version                     Affiche la version
  -i, --ipaddress <hostname>        Spécifie le nom d'hôte du nœud
  -p, --port <port>                 Spécifie le port du nœud
  -s, --seeds <seeds>               Nœuds seed pour initier les connexions p2p
  -v, --verbose                     Active le mode verbeux pour les transactions et le réseau
  -d, --peerDiscovery [type]        Active la découverte des pairs en utilisant différentes méthodes
  -t, --peerDiscoveryPort <port>    Active la découverte des pairs en utilisant différentes méthodes
  -l, --dhtDisconnectDelay <delay>  Durée après laquelle le nœud se déconnecte du réseau DHT
  -m, --mine                        Démarre un processus enfant de minage de blocs en parallèle du nœud
  -c, --clusterMiner [numbers]      Lance un cluster de mineurs. Par défaut : 1 worker
  -w, --walletName <walletName>     Nom du portefeuille du mineur
  -k, --password <password>         Mot de passe nécessaire pour déverrouiller le portefeuille
  -x, --exposeHTTP                  Expose l'API HTTP pour permettre une interaction externe avec le nœud de la blockchain
  -n, --network <network>           Réseau blockchain auquel se joindre
  -h, --help                        Affiche les informations d'utilisation

Commands:
  start                             Démarre le nœud de la blockchain


```

## Envoi d'une transaction

Pour envoyer une transaction, vous pouvez utiliser l'outil CLI ou envoyer un paquet de données JSON signé à votre nœud de blockchain local. La transaction sera ensuite transmise à tous les pairs connectés pour validation et minage.

La structure de base d'une transaction est la suivante :

```

{ 
  fromAddress: <Clé publique ECDSA OU nom de compte>,
  toAddress: <Clé publique ECDSA OU nom de compte>,
  type: <Type de transaction>,
  data: <Données supplémentaires à envoyer>,
  timestamp: <Horodatage UNIX>,
  amount: <Montant>,
  hash: <Hachage SHA256 de la transaction>,
  miningFee: <Frais de minage suffisants pour équilibrer la taille de la transaction>,
  signature: <Signature ECDSA à partir d'une clé privée> 
}

```

## Interaction avec les contrats intelligents

Il existe deux façons d'utiliser des contrats : les actions et les appels de transaction. Pour les construire, vous pouvez utiliser les outils CLI fournis à cet effet ou envoyer manuellement les données à votre nœud local.
La structure des appels de transaction à l'aide de txCLI.js :
```
node txCLI.js --fromAddress <expéditeur> --toAddress <contrat> --amount <montant> --type call --walletName <portefeuille> --password <mot de passe> --data '{"method":"<nomMéthode>","cpuTime":<tempsEnMS>,"params":{"<nomParamètre>":"<valeur>"}}'
```
Le compte expéditeur doit être un compte, pas une clé publique.
Si un montant doit être envoyé, il doit être spécifié dans l'API du contrat, sinon le montant ne sera pas soustrait du solde.
Le type de transaction doit être défini sur "call" pour que la transaction soit traitée en tant que telle.
La chaîne de données doit être encadrée par des guillemets simples tandis que les guillemets doubles servent à encadrer les noms de propriétés.

### Appels de transaction

En envoyant une transaction de type <call>, vous pouvez interagir avec des contrats intelligents stockés sur la blockchain.
La structure de base de la charge utile des données doit être cohérente afin que la transaction soit
validée par d'autres nœuds. Il est nécessaire de créer un compte pour envoyer des appels sur le réseau. Voici un exemple de la charge utile des données située dans le champ des données de la transaction :

```
{
  'method':'méthodeContrat',
  'cpuTime':0-100,
  'params':{
    'clé':'valeur'
  }
}
```

Voici la structure d'un appel de transaction :

```
{ 
  fromAddress: <Nom du compte émetteur>,
  toAddress: <Nom

du compte du contrat>,
  type: 'call',
  data: {
    'method':<Méthode du contrat>,
    'params':{
      <Paramètres supplémentaires sous forme de paire clé:valeur>
    }
  },
  timestamp: <Horodatage UNIX>,
  amount: <Montant>,
  hash: <Hachage SHA256 de la transaction>,
  miningFee: <Frais de minage suffisants pour équilibrer la taille de la transaction>,
  signature: <Signature ECDSA à partir de votre clé privée> 
}

```

Voici un exemple :

```
 receipt: {
    fromAddress: 'tuor',   // Nom du compte émetteur
    toAddress: 'Tokens',   // Nom du contrat
    type: 'call',         // Type de transaction
    data: { 
      method: 'issue',    // Méthode à appeler à partir du contrat
      params: {
        "symbol":"GOLD",    
        "amount":100,
        "receiver":"turgon"
      } 
    },
    timestamp: 1574788012061,
    hash: '1c853838aca7279141e38613726ed1d26cf97da1a91c1c57cadb59b4e46304bc',
    miningFee: 0.0167,
    signature: 'hkNKNUdT4DnbDVRKaodVg8wYEjkRHSzcMjLyRL/5k1KgDWhcxLolm7vjBEXlnu7A
ckL7qrOkdhXgxSxHVTLHow=='
  }


```

### Actions

Il existe plusieurs types d'actions :
- Création de compte
- Déploiement de contrat
- Destruction de contrat

```
{
    fromAccount: <Nom du compte émetteur>,
    type: <Type d'action>,
    task: <Tâche sélectionnée à effectuer selon le type>,
    data: { // La charge utile des données contient les détails du compte émetteur
      name: <Nom du compte émetteur>,
      ownerKey: <Clé publique ECDSA du portefeuille propriétaire>,
      hash: <Hachage SHA256>,
      ownerSignature: <Signature>,
      type: <>
    },
    timestamp: <Horodatage Unix>,
    contractRef: {},
    fee: <Frais de minage suffisants pour équilibrer la taille de la transaction>,
    hash: <Hachage SHA256 de l'action>,
    signature: <Signature ECDSA du hachage à partir d'une clé privée>

}


```

## Auteur

* **Sacha-Olivier Dulac** - *Travail initial* - [Gultar](https://github.com/gultar)

## Licence

GNU GENERAL PUBLIC LICENSE Version 3, 29 juin 2007

Ce projet est sous licence GNU General Public License v3.0

Vous pouvez copier, distribuer et modifier le logiciel à condition de suivre les modifications/dates dans les fichiers sources. Toutes les modifications ou tout logiciel comprenant (via un compilateur) du code sous licence GPL doivent également être disponibles sous la GPL, ainsi que les instructions de construction et d'installation.

Pour la licence complète : [LICENCE](https://tldrlegal.com/license/gnu-general-public-license-v3-(gpl-3)#fulltext)

Droits d'auteur (C) 2018 Sacha-Olivier Dulac

## Remerciements

* Un grand merci à Simply Explained - Savjee et sa vidéo sur "Creating a blockchain with Javascript", qui a été le point de départ de ce projet. Lien vers sa vidéo ici :  https://www.youtube.com/watch?v=zVqczFZr124

* Un grand merci à Patrik Simek, créateur du module vm2, qui est au cœur même de mon "moteur de contrats intelligents". Cela n'aurait jamais été possible sans votre module, c'est grandement apprécié.