# Croissance bactériologique et structure de colonisation du milieu
 
L'objectif de ce projet est de visualiser les structures visibles lors de la colonisation d'une boite de pétri par une ou deux bactéries et de voir comment certains paramètres peuvent modifier ces structures.
Pour ce faire nous avons réaliser une simulation par Python et un affichage par Tkinter afin d'observer les structures tout en modifiant certain paramètres via une interface pratique.
Pour donner un exemple de résultat ainsi que de condition d'expérience dès maintenant, nous pouvons déceler une durée de vie minimale (en itertations) en fonction du taux de croissance effectif d'une souche afin que cette dernière ne s'éteigne pas au début de la simulation. 
Comme le modèle de croissance primaire choisi est exponentiel (chaque bactérie en donne deux nouvelle à chaque division), le format de fonction choisi pour modéliser ce phénomène est lui aussi exponentiel.
Le graphique représentant cela se trouve à [cette adresse](https://drive.google.com/open?id=1N1cfhPkAyh5dQDhtxmFP0bSHg0fmaaeX).
Le taux de corélation obtenu (à savoir 0.95) étant proche de 1, on peut en conclure que la modélisation est satisfaisante, sans être parfaite.
Ceci nous permet de fixer une condition minimale sur le taux de croissance à laquelle s'ajouteront de nouvelles conditions expliquées plus bas.

## English version: Bacteriological growth and environmental colonization structure

The goal of this project is to visualize the structures visible during the colonization of a petri box by one or two bacteria and to see how certain parameters can modify these structures.
To do this, we performed a simulation by Python and a display by Tkinter in order to observe the structures while modifying certain parameters via a practical interface.
As a exemple of result and of necessary condition for the experiment, we can find a minimal lifespan (in iterations) as a function of the effective growth rate of a bacterial strain so that it does not persih right at the start of the simulation.
Because we choosed an exponential growth model (each bacteria give birth to two new ones we she divides), we choosed to use an exponential function to represent this phenomenon.
The graph that depicts this is at [this adress](https://drive.google.com/open?id=1JAA5CgLlx63kgONDmUsMR0yLsrOApJfW)
The correlation rate (which is 0.95) is close enought to 1 so that we can consider the model as acceptable, not perfect thought.
With this we can fixe a minimal requirement on the growth rate, there are few more requirements (on the temperature and the pH) which are explained bellow (but in French, this is just a small presentation sorry).

## Présentation de l'équipe

|(´・ω・｀)| ( ͡° ͜ʖ ͡°) | ಠ_ಠ | ᕕ( ᐛ )ᕗ |
|-----|-----|-----|-----|
| Kurdyk Louis| Martin Amaury | Rosenthal Massyl ? (il l'enlèvera comme preuve qu'il a au moins travaillé une minute) | Corlue Florian |


## Description synthétique du projet

**Problématique :** Comment vont s'organiser une ou plusieurs bactéries afin de coloniser un milieu ?

**Hypothèse principale :** Les bactéries cherchent à coloniser et dominer la totalité de leur milieu tant qu’elles y trouvent de la nourriture.

**Hypothèses secondaires :** 
La position de départ d'une bactérie va grandement influer sur ses chances de survies et sa rapidité à s'étendre, le centre de la boite étant le mieux.
Une bactérie plus adapté au milieux se trouvera dans une position de domination par rapport à une autre ce qui lui permettra de coloniser plus d'espace.

**Objectifs :** Déterminer la vitesse de colonisation du milieu par une bactérie en fonction de plusieurs critères (ph, température, vitesse de division, taux de mutations...).

**Critère(s) d'évaluation :** Nombres d'individus, de vides, de cases de nourriture dans la boîte.

## Présentation structurée des résultats

Nous avons décidé de choisir le modèle exponentielle afin d'étudier la structure de colonisation d'une boîte de pétri par une ou des bactérie(s):
ce modèle induit que chaque bactérie mère se sépare en deux nouvelles bactéries filles lors de sa reproduction.

Pour revenir sur les conditions minimales et leur mise en place, la température pour que le taux de croissance ne soit pas nul est limitée à ± 20 degrés Celsius de la température optimale et le pH est lui limité à ± 3 unité de pH du pH optimal.
En effet si la bactérie se trouve dans un milieu dont la température ou le pH se trouve trop loin de la valeur optimale, la bactérie ne se plait pas dans le milieu et est donc incapable de s'y développer.
Ceci présente donc une nouvelle contrainte (en plus de la durée de vie minimale) sur les conditions de l'exprérience afin qu'elle puisse être menée dans des conditions intéressantes.

On donne aussi ce tableau récapitulatif de la durée de vie minimale (en itérations) par rapport au taux de croissance :
| Taux de croissance | Durée de vie minimale (en itérations) |
| ------------------ | ------------------------------------- |
| 0.1 | 11 |
| 0.2 | 10 | 
| 0.3 | 9 |
| 0.4 | 8 |
| 0.5 | 7 |
| 0.6 | 6 |
| 0.7 | 5 |
| 0.8 | 3 |
| 0.9 | 3 |
| 1 | 3 |

Pour modéliser la croissance de nos bactéries nous avons opté pour une représentation graphique en couleur de l'état de la boite de pétri à laquelle nous avons ajouté des courbes avec le même code couleur.
En ce qui concerne la boite nous avons utilisé un canvas de tkinter afin de pouvoir l'actualiser à chaque tour de boucle. 
Il nous permet de dessiner des rectangles (qui sont des carrés en l'occurence) de couleur différente pour chaque entité possible dans la boîte (blanc pour un vide, rouge pour la bactérie 1, orange pour la bactérie 2, vert pour la nourriture, bleu pour l'antibiotique).
Pour l'affichage des courbes de résultats, nous utilisons matplotlib car nous avions déjà de l'expérience avec cette bibliothèque après le TP sur Schelling.
De plus, cette bibliothèque a pour avantage de permettre à l'utilisateur quelques manipulations sur la fenêtre des courbes afin par exemple de pourvoir zoomer sur une partie qui l'intéresserait plus.

La boite étant grande (100 * 100 donc 10 000 cases au total) il est difficile pour une bactérie seule de coloniser tout le milieu en peu de temps et cela est presque impossible sans ajout de nourriture régulier (sauf si la bactérie possède une longue durée de vie sans se nourrir).
On remarque de plus une diminution de la vitesse d'expension lorsque la courbe du nombre d'individu (qui est croissant) coupe celle de la nourriture (qui décroit).
En général, lorsque deux bactéries sont présentes la bactérie la plus proche du centre au niveau de sa position de départ (qui sont aléatoires).
Lorsqu'il n'y a qu'une seule bactérie, si elle apparait vers le centre, elle se développera plus vite que si elle apparait dans un coin de la boîte.

Nous avons décidé de retirer certaines fonctionnalité qui était prévu car trop rare dans des conditions d'expériences réelles ; ceci comprend la mutation des bactéries résultant en une résistance aux antibiotiques ainsi que la symbiose entre bactéries de types différents.


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
