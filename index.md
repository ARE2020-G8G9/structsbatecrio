# Croissance bactériologique et structure de colonisation du milieu
 
L'objectif de ce projet est de visualiser les structures visibles lors de la colonisation d'une boite de pétri par une ou deux bactéries et de voir comment certains paramètres peuvent modifier ces structures.
Pour ce faire nous avons réaliser une simulation par Python et un affichage par Tkinter afin d'observer les structures tout en modifiant certain paramètres via une interface pratique.

Pour donner un exemple de résultat ainsi que de conditions d'expérience dès maintenant, nous pouvons déceler une durée de vie minimale (en itérations) en fonction du taux de croissance effectif d'une souche afin que cette dernière ne s'éteigne pas au début de la simulation. 
Comme le modèle de croissance primaire choisi est exponentiel (chaque bactérie en donne deux nouvelle à chaque division), le format de fonction choisi pour modéliser ce phénomène est lui aussi exponentiel.

Le graphique représentant cela se trouve à [cette adresse](https://drive.google.com/open?id=1N1cfhPkAyh5dQDhtxmFP0bSHg0fmaaeX).

Le taux de corélation obtenu (à savoir 0.95) étant proche de 1, on peut en conclure que la modélisation est satisfaisante, sans être parfaite.
Ceci nous permet de fixer une condition minimale sur le taux de croissance à laquelle s'ajouteront de nouvelles conditions expliquées plus bas.

## English version: Bacteriological growth and environmental colonization structure

The goal of this project is to visualize the structures visible during the colonization of a petri box by one or two bacterias and to see how certain parameters can modify these structures.
To do this, we performed a simulation by Python and a display by Tkinter in order to observe the structures while modifying some parameters via a practical interface.

As an example of result and of necessary condition for the experiment, we can find a minimal lifespan (in iterations) as a function of the effective growth rate of a bacterial strain so that it does not perish right at the start of the simulation.
Because we choosed an exponential growth model (each bacteria give birth to two new ones we she divides), we've chosen to use an exponential function to represent this phenomenon.

The graph that depicts this is at [this adress](https://drive.google.com/open?id=1JAA5CgLlx63kgONDmUsMR0yLsrOApJfW).

The correlation rate (which is 0.95) is close enought to 1 so that we can consider the model as acceptable, not perfect thought.
With this we can set a minimal requirement on the growth rate, they are few more requirements (on the temperature and the pH) which are explained below (but in French, this is just a small presentation sorry).

## Présentation de l'équipe

|(´・ω・｀)  | ( ͡° ͜ʖ ͡°) | ಠ_ಠ | ᕕ( ᐛ )ᕗ |
|:-----:|:-----:|:-----:|:-----:|
| Kurdyk Louis| Martin Amaury | Rosenthal Massyl | Corlue Florian |


## Description synthétique du projet

**Problématique :** Comment vont s'organiser une ou plusieurs bactéries afin de coloniser un milieu ?

**Hypothèse principale :** Les bactéries cherchent à coloniser et dominer la totalité de leur milieu tant qu’elles y trouvent de la nourriture.

**Hypothèses secondaires :** 
La position de départ d'une bactérie va grandement influer sur ses chances de survies et sa rapidité à s'étendre, le centre de la boite étant le mieux.
Une bactérie plus adapté au milieux se trouvera dans une position de domination par rapport à une autre ce qui lui permettra de coloniser plus d'espace.

**Objectifs :** Etudier les structures récurrentes mises en place dans la colonisation d'une boite de pétri ainsi que les conditions nécessaires à la réalisation de celle-ci (ph, température, vitesse de division, taux de mutations...).

**Critère(s) d'évaluation :** Nombres d'individus, de vides, de cases de nourriture dans la boîte.

## Présentation structurée des résultats

Nous avons décidé de choisir le modèle exponentiel afin d'étudier la structure de colonisation d'une boîte de pétri par une ou bien deux bactérie(s):
ce modèle induit que chaque bactérie mère se sépare en deux nouvelles bactéries filles lors de sa reproduction.

Pour revenir sur les conditions minimales et leur mise en place, la température pour que le taux de croissance ne soit pas nul est limitée à ± 20 degrés Celsius de la température optimale et le pH est lui limité à ± 3 unité de pH du pH optimal.
En effet si la bactérie se trouve dans un milieu dont la température ou le pH se trouve trop loin de la valeur optimale, la bactérie ne se plait pas dans le milieu et est donc incapable de s'y développer.
Ceci présente donc une nouvelle contrainte (en plus de la durée de vie minimale) sur les conditions de l'exprérience afin qu'elle puisse être menée dans des conditions intéressantes.

On donne aussi ce tableau récapitulatif de la durée de vie minimale (en itérations) par rapport au taux de croissance :

| Taux de croissance         | Durée de vie minimale (en itérations)        | 
| :-------------: |:-------------:| 
| 0.1     | 11 | 
| 0.2      | 10      |  
| 0.3 | 9      | 
| 0.4 | 8 |
| 0.5 | 7 |
| 0.6 | 6 |
| 0.7 | 5 |
| 0.8 | 3 |
| 0.9 | 3 |
| 1 | 3 |




Pour modéliser la croissance de nos bactéries nous avons opté pour une représentation graphique en couleur de l'état de la boîte de pétri à laquelle nous avons ajouté des courbes avec le même code couleur.
En ce qui concerne la boîte, nous avons utilisé un canvas de tkinter afin de pouvoir l'actualiser à chaque tour de boucle. 
Il nous permet de dessiner des rectangles (qui sont des carrés en l'occurence) de couleurs différentes pour chaque entité possible dans la boîte (blanc pour un vide, rouge pour la bactérie 1, orange pour la bactérie 2, vert pour la nourriture, bleu pour l'antibiotique).
Pour l'affichage des courbes de résultats, nous utilisons matplotlib car nous avions déjà de l'expérience avec cette bibliothèque après le TP sur Schelling.
De plus, cette bibliothèque a pour avantage de permettre à l'utilisateur quelques manipulations sur la fenêtre des courbes afin par exemple de pourvoir zoomer sur une partie qui l'intéresserait plus.

La boîte étant grande (100 * 100 donc 10 000 cases au total) il est difficile pour une bactérie seule de coloniser tout le milieu en peu de temps et cela est presque impossible sans ajout de nourriture régulier (sauf si la bactérie possède une longue durée de vie sans se nourrir).
On remarque de plus une diminution de la vitesse d'expension lorsque la courbe du nombre d'individu (qui est croissant) coupe celle de la nourriture (qui décroît).
En général, lorsque deux bactéries sont présentes, la bactérie la plus proche du centre au niveau de sa position de départ (qui sont aléatoires) va prédominer sur la seconde à condition que leur capacité à s'étendre soit à peu près similaire, cela s'explique par le fait que le centre laisse beaucoup plus d'option pour chercher de la nourriture qu'un bord (dans le graphe ci-dessous, où les deux bactéries ont été initialisées avec exactement les mêmes spécificités -celles par défaut dans le programme-, nous pouvons voir que la bactérie 2, qui dans la simulation commençait au milieu, s'est développée plus aisément que la souche 1).

![this adress](https://github.com/ARE2020-G8G9/structsbatecrio/blob/master/Exemples/Courbe_batc2_milieu.PNG)

Lorsqu'il n'y a qu'une seule bactérie, si elle apparaît vers le centre, elle se développera plus vite que si elle apparaît dans un coin de la boîte.
En effet, le premier graphique ci-dessous a été obtenu à l'issue d'une simulation où la bactérie seule commence sa colonisation sur un côté de la boîte, et le 2e graphique est une autre simulation, où cette fois-ci la bactérie seule commence au milieu.
On remarque bien une différence dans la vitesse de développement sur 50 itérations.

![this adress](https://github.com/ARE2020-G8G9/structsbatecrio/blob/master/Exemples/Souche1_seule_cote.PNG)

![this adress](https://github.com/ARE2020-G8G9/structsbatecrio/blob/master/Exemples/Souche1_seule_milieu.PNG)

On peut donc estimer que l'hypothèse secondaire selon laquelle la position de départ au milieu donne un avantage dans le développement d'une bactérie est validée.

En ce qui concerne la seconde hypothèse secondaire, la bactérie la plus adaptée au milieu se retrouve en effet dans une position largement favorable par rapport à une autre moins adaptée.
De fait, lorsque deux bactéries interagissent, une des deux bactéries va mourir en laissant un vide. Les bactéries ayant les mêmes chances de victoire, au final le nombre impacte fortement sur le choix de la bactérie qui va dominer le milieu. 
Ainsi, c'est bien la bactérie qui se développera le plus vite qui pourra remporter la course à la domination dans la boîte en surnombrant l'autre souche.

A chaque simulation, les bactéries présentes s’agglutinent sur la nourriture disponible adjacente à leur position, et les colonies suivent la nourriture qui s’éloigne au fur et à mesure. 
Lorsque de la nourriture apparaît à un endroit éloigné des bactéries, celles-ci ne réagissent pas. Mais si des bactéries sont présentes encore à cet endroit, alors elles se reproduisent tant que la nourriture est disponible et meurent lorsque celle-ci est consumée.
Cependant, si les bactéries trop éloignées de la nourriture semblent ne pas réagir, c'est parce que le programme ne leur permet pas de détecter la présence de nourriture si celle-ci n'est pas adjacente à leur position.
Elles ne peuvent donc pas se déplacer en conséquence. Nous avons tout de même la confirmation qu’elles colonisent le milieu tant que de la nourriture est accessible de façon immédiate.
Cela signifie donc que les bactéries colonisent le milieu et se divisent tant que de la nourriture est disponible, et migrent vers des milieux propices en même temps que ces derniers se modifient.
Nous pouvons ainsi valider notre hypothèse principale malgré la faille dans la capacité de nos bactéries à voir au-delà de leur environnement proche, en ajoutant que les milieux déjà colonisés ne sont pas voués à le rester, si la nourriture venait à manquer, puisque les bactéries meurent.


Nous avons décidé de retirer certaines fonctionnalités qui étaient initialement prévues car trop rares dans des conditions d'expériences réelles ; ceci comprend la mutation des bactéries résultant en une résistance aux antibiotiques ainsi que la symbiose entre bactéries de souches différentes.


## Lien vers page de blog : <a href="blog.html"> C'est ici ! </a>

## Bibliographie :

**Carte mentale présentant nos différentes idées** : <a href="https://cdn.discordapp.com/attachments/690215408917282943/694206338603155466/Mindmap.jpg"> Mindmap </a> 

Liste de l'ensemble des ressources bibliographiques utilisées pour vos travaux. **<= Indiquez le canal utilisé pour les trouver (Google Scholar, sources wikipedia, ressources en ligne SU, ...)**


[1] D.Nielsen, “Comment les bactéries intestinales rivalisent entre elles pour leur survie.”,www.biokplus.com, 12 octobre 2018.Disponible ici : <a href="https://www.biokplus.com/blog/fr_CA/les-bacteries-vous/comment-bacteries-intestinales-rivalisent-entre-elles-pour-leur-survie"> lien de la ressource[1] </a>

[2] S.Sonea, “Les symbioses dynamiques, mode de vie bactérien”, medecine/sciences vol.4,n°6, p.378-381, juin 1988, republié sur www.ipubli.inserm.fr,<a href="http://www.ipubli.inserm.fr/bitstream/handle/10608/3836/MS_1988_6_378.pdf?sequence=1"> lien de la ressource[2] </a>

[3] E. Sender, “Antibiotiques : faites tourner pour vaincre la résistance.”, 12 mais 2015. Sciences et Avenir [en ligne]. Disponible à l’adresse :<a href="https://www.sciencesetavenir.fr/sante/antibiotiques-faites-tourner-pour-vaincre-la-resistance_28043"> lien de l'article[3] </a>. Pour combattre la résistance aux antibiotiques, des chercheurs proposent un programme de rotation des médicaments, selon un modèle mathématique.

[4] Cornu, Marie, et Philippe Rosset. « Appréciation quantitative de la croissance bactérienne potentielle à partir de profils temps-température - Exemples d’application pour la croissance de Salmonella Typhimurium dans un steak haché ». Bulletin de l’Académie Vétérinaire de France, vol. 157, no 1, 2004, p. 93‑100.

[5] CRETENET, Marina, et al. « Etude des interactions entre staphylococcus aureus et lactococcus lactis en matrice fromagère ». SYMPOSTAPH, 2010, p. np. HAL ArchivesOuvertes, <a href="https://hal.archives-ouvertes.fr/hal-01454348."> lien de l'archive[5] </a>

[6] Krasovec, Marc. Estimation of mutation rates : implications for diversification and evolution of eukaryotic phytoplankton. Université Pierre et Marie Curie - Paris VI, octobre 2016. HAL Archives Ouvertes, <a href="https://tel.archives-ouvertes.fr/tel-01647210."> lien de l'archive[6] </a>

[7] « Spontaneous Mutation Rate in the Smallest Photosynthetic Eukaryotes ». Molecular Biology and Evolution, vol. 34, no 7, 2017, p. 1770‑79. HAL Archives Ouvertes,doi:10.1093/molbev/msx119.

[8] [Auteurs inconnus] « Résistance aux antibiotiques ». Institut Pasteur, 24 avril 2017,dernière mise à jour : septembre 2019,<a href="https://www.pasteur.fr/fr/centre-medical/fiches-maladies/resistance-aux-antibiotiques."> lien de la ressource[8] </a>

[9] Rosset, Philippe, et al. « Intégration des profils temps-température et appréciation de la croissance bactérienne ». Revue Générale du Froid, no 1038, novembre 2003, p. 27‑34.

[10] Trivedi, Mahendra Kumar, et al. « Characterization of Antimicrobial Susceptibility Profile of Biofield Treated Multidrug-resistant Klebsiella oxytoca ». Applied Microbiology: OpenAccess, vol. 1, no 1, octobre 2015, p. 1000101.

[11] CHONG, Yong, SHIMODA, Shinji, YAKUSHIJI, Hiroko, ITO, Yoshikiyo, MIYAMOTO,Toshihiro, KAMIMURA, Tomohiko, SHIMONO, Nobuyuki et AKASHI, Koichi, 2013.Antibiotic Rotation for Febrile Neutropenic Patients with Hematological Malignancies:Clinical Significance of Antibiotic Heterogeneity. PLOS ONE. 23 janvier 2013. Vol. 8, n° 1,pp. e54190. DOI 10.1371/journal.pone.0054190.
