---------------------------------------
Indications sur la structure du projet
---------------------------------------

----------
:Subject: Algorithme génétique
:Authors: Descamps Colette, Gréau Pierre, Prause Justine
----------

Dans le dossier Projet, vous trouverez un dossier problems et les fichiers principaux.

La structure est la suivante :
	On utilise les classes IndividualInterface et ProblemInterface comme super classes.
	Une sous classe de IndividualInterface et de ProblemInterface sera proposée pour chaque problème (dans le dossier correspondant).
	Le fichier input_checker.py contient les fonctions permettant d'effectuer les tests et de convertir les arguments saisis en commande.
	Chaque problème contient deux fichiers :
		- un premier nommé problem_classes.py qui contient la définition des sous-classes
		- un second problem_main.py qui peut être appelé pour lancer la résolution du problème.
