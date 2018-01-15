# Citations de San Antonio

Ce petit programme affiche des citations aléatoires de San Antonio, dites par des personnages de dessins animés aléatoires.

Il est tiré du cours *Démarrez votre projet avec Python* de Céline Martinet Sanchez sur OpenClassrooms (https://openclassrooms.com/courses/demarrez-votre-projet-avec-python).

## Installation
Si vous souhaitez mettre à jour les fichiers JSON, il vous sera nécessaire d'installer **scrapy**, par exemple à l'aide de la commande suivante :

    pip install -r requirements.txt

## Maintenance
- La liste des personnages de dessins animés est stockée dans <code>characters.json</code>, qui est donc un fichier au format JSON.
Il est possible de mettre cette liste à jour à l'aide de la commande suivante :

    <code>scraper runspider characters_scrapper.py -o characters.json</code>

**Attention :** ***avant*** d'effectuer la mise à jour, veillez à bien supprimer *préalablement* le fichier <code>characters.json</code>, par exemple à l'aide de la commande suivante :

    rm characters.json
    
- La liste des citations est stockée dans <code>quotes.json</code>, qui est donc un fichier au format JSON.
Il est possible de mettre cette liste à jour à l'aide de la commande suivante :

    <code>scraper runspider quotes_scraper.py -o quotes.json</code>

**Attention :** ***avant*** d'effectuer la mise à jour, veillez à bien supprimer *préalablement* le fichier <code>quotes.json</code>, par exemple à l'aide de la commande suivante :

    rm quotes.json

**NB :** Si vous avez oublié de supprimer le fichier concerné avant de mettre à jour une des listes, ce n'est pas grave *mais le programme ne fonctionnera pas en l'état*. Supprimez le fichier concerné, puis entrez la commande de mise à jour correspondante.

## Langue
**français** uniquement
