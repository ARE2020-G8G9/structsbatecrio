## Travail effectué  

=> Description hebdomadaire du travail effectué

### Semaine 1
La première semaine de travail effectuée a été consacrée à la récupération de sources, traitement de celles-ci et à préparer une feuille de route pour le projet.
Grace à cela nous avons pu créer notre carnet de bord concernant la recherche documentaire retrouvable à [cette adresse](https://drive.google.com/open?id=1wv8daeGtefYSFS66kO3DNQ1qbyvjoZm-).
Faire ces recherches nous a permis d'obtenir une première idée de la manière dont codé notre projet.

### Semaine 2
Cette seconde semaine a été consacrée à l'initialisation des entiers de base du projet, à savoir ; la boite, la première bactérie, l'antibiotique et au début des interactions entre ces éléments.
Nous avons débuté la programmation par ces éléments afin de pouvoir se faire une idée plus concrète de comment faire fonctionner notre simulation globalement.
Nous avons fait le choix d'utiliser des dictionnaires pour représenter chaque case de la boite ainsi que son état, cela nous permet de stocker plusieurs informations par case, ce qui est pratique pour gérer des paramètres tels que l'âge des bactéries.

### Semaine 3
Lors de la troisième semaine, nous avons pu terminer les interactions avec la boite et son affichage par mathplotlib.
Ces interactions comprennaient les mouvements et naissances de bactérie, l'ajout de nourriture et d'antibiotique.
L'affichage par mathplolib n'était cependant pas satisfaisant car les couleurs se modifaient en fonction du nombre de contenus différents dans la boite, rendant la lisibilité compliquée mais pratique pour vérifier les premiers résultats de simulation.

### Semaine 4
Au cours de cette dernière semaine, nous avons travaillé sur l'affichage des données statistiques dans la boite, l'ajout de la seconde bactérie et son interaction avec la première et surtout une interface graphique via Tkinter.
La création de cette interface à nécessité beaucoup de temps pour la rendre (à peu près) lisible et fonctionnelle. Le regret qu'il reste est que le canvas servant à afficher la boite n'affiche que la dernière étape et non pas chaque étape intermédiaire.
L'ajout de la seconde bactérie n'a pas été un souci majeur car la plupart des fonctions avaient déjà été prévu pour deux bactéries.
De plus nous avons fait le choix de ne pas réaliser certain point de notre feuille de route car ils ne semblaient pas indispensables, par exemple la mutation des bactéries résultant en une résistance aux antibiotiques est tellement rare dans le cas d'une étude dans une boite de pétri que son implémentation relevait plus du gadget que d'une notion utile.

### Semaine 5
Envoie du carnet de bord aux bibliothéquaires (il a été envoyé à la mauvaise personne).
Nous avons pu optimisé un peu le code en regroupant en une seule plusieurs fonctions qui effectuaient des tours de la boite.
L'affichage de la boite est maintenant dynamique, cela pose un problème de vitesse d'exécution pour les grands nombres d'itérations mais l'animation est plus agréable à regarder.
Fin de l'édition du texte du site internet.

<a href="index.html"> Retour à la page principale </a>
