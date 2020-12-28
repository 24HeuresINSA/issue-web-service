# User stories Assomaker

## BOOOONSOIR :smile: 

Merci de passer donner un coup de main pour éditer les USERS Stories du (futur) nouveau assomaker :tada:

**C'est quoi une USER Storie ?**

C'est une description sous forme de carte d'une fonctionnalité d'un logiciel en développement. On va s'en servir de fil rouge pour le nouveau Assomaker. Elles ont pour but de coller au maximum au besoin et à ce que verra l'utilisateur quand il va utiliser le logiciel.

**Qui les écrit ?**

Toi+moi+tout ceux qui le veulent. Les utilisateur de l'ancien assomaker en fait ! Et c'est pas compliqué, il suffit de lire les petites règles qui sont en dessous :arrow_down: 

## Les règles de contributeur (aka comment écrire une carte)

Pour écrire une carte il y a quelque règles à respecter : 
 - **3 phrases max** pour la description sinon c'est qu'il faut séparer en plusieur cartes. Simple. Basique.
 - :warning: Faites attention à bien respecter le **template** ci-dessous :arrow_down: :warning: Ca nous permettra d'automatiser :gear: le traitement de toutes les cartes :card_index:.
 - Ces cartes vont être **relues** et **validées** donc pas de pression :wink: ! Si vous pensez à une fonctionnalité (même un truc très précis, pointus,..) mettez la ! Au moins on aura une trace de l'idée.
 - Hésitez pas a vous inspirer de celles qui sont déjà faites pour bien comprendre.
 - En anglais :flag-gb: parce que tout le monde comprend.
 - Pas de caractere spéciaux :angry: Sinon c'est comme Assomaker ca va plus marcher
 - Si tu peux pas éditer il faut cliquer sur ![](https://i.imgur.com/1ZPc3tF.png) en haut a gauche :wink: 


## Liste des utilisateur possibles

 - GUEST : Un utilisateur qui n'est pas connecté à aucun compte
 - USER : Tous les gens qui ont un compte
 - SOFT : Un soft
 - CONFIANCE : Un confiance
 - HARD : Un hard
 - LOG : Un orga log
 - HUMAIN : Un humain
 - ADMIN : Un admin Assomaker
 - BUREAU : Un membre du bureau
 - SECU : Un orga sécu
 - SG : Le secretaire général

Si vous avez des suggestions sur le template, des questions en tout type, faites les dans le channel `#la-comsi-comca` sur le discord. 

**Bonne chance**

## Liste des USER STORIES a écrire

On est gentils ~~et organisés~~ donc on a fait une liste de toute celles qui n'éxistent pas encore

### Sign up
 - Les admins peuvent créer un formulaire d'inscription avec un message personnalisé.
 - Formulaire d'inscription avec des pages séparées pour soft, hard, teckos.
 - Un utilisateur enregistré peut choisir une liste de pote deja dans la db. 
 - Les admins voient les inscriptions en attente de validation sur une page séparée.
 - Les admins peuvent assigner un libellé a quelqu'un
 - Les admins/humains peuvent rajouter des libelles aux comptes
 - Les admins peuvent modifier les profils
 - Les admins peuvent valider les inscriptions
 - (En débat)Champs avec le numero de secu social non obligatoire 
 - Un admin peut activer/désactiver les inscriptions.
 - Possibilité d'envoyer des notifications basé sur des événements.
 - Un user peut indiquer la catégorie du compte (soft, tekos).
 - les hards ont un lien separe pour s'inscrire.
 - ajouter le contact (envoyer une notif depuis cette ecran aux HUMANs avec un miniformulaire) des HUMANS dans le calendrier de disps

### Dispo
 - Les HUMAINS peuvent créer un creaneau de disponibilité
 - Les HUMAINS peuvent créer des groupes de créneaux(separation automatique en tranche de X heures)
 - Les HUMAINS peuvent modifier les créneaux
 - Les USERS peuvent voir leur charisme
 - Un USER peut voir le minimum de charisme pour etre pris
 - Un HUMAIN peut modifier le minimum de charisme
 - 
### Anim = Activites -->  HARD only
 - On peut voir les Activites deja crees
 - On peut creer une Activites
     - titre
     - description
     - equipe
     - resp (par def celui qui crée la tache)
     - date debut/fin de l'activite
    - date debut/fin de l'anim ouvert au public si elle publié sur le site
     - lieux
     - matos
     - type
     - presta
         -  Nom
         -  Tel
         -  email
         -  nb de repas
 - Possibilité de publier les annimations directement sur le site dans animations
 - ADMIN peuvent desactiver l'affichage d'un champ 
 - demander a la LOG d'ajouter un matos
 - les HARDs lors de la creation de FA peuvent les mettre de cote en mode redaction (draft)

#### Cycle de vie d'une FA
 ![](https://cdn.discordapp.com/attachments/772888531101941770/792810948347297832/20201227_184602.jpg)
![](https://cdn.discordapp.com/attachments/772888531101941770/792811331689381919/unknown.png) 

 - pour la log ->Validation par matos et non validation global (ex que les orga barieres peuvent valider le nb de bariere nessaire)


### Logistique
 - Creation de matos 
 - edition de matos (LOG / BUREAU /ADMIN)
 - affichage de matos (HARD+)
 - confirmer le matos ajouter
 - Il faut pouvoir valider la fiche que a condition que le matos soit disponible
 - Il faut compter le matos utiliser pour creer des alerte en cas de trop large utilisation et/ou afficher que la quantité dispo
 - Affiche tous les activités lié au matos
 - Validatoin par matos et pas par activite


## Template 

Copier coller le template avec les ` ``` ` au dessus et en dessous

```json
{
    "title": "The card title",
    "author": "Your name in case we need to ask you questions",
    "priority": "", //LEAVE AS IT IS
    "users" : [
        "GUEST",
        "ADMIN"
    ], // FILL THE LIST
    "description": "What you can do",
    "tests":[
        "test 1",
        "test 2"
    ], // FILL THE LIST
    "commments": "Explain your pain" // NOT MANDATORY
}
```

<!-- OLD TEMPLATE - DO NOT USE
```
UserStoryTitle
Author: Your name in case we need to ask you questions
Priority: p3(LOW),p2(MEDIUM),p1(HIGH) ---- LEAVE EMPTY
---
As a USER # pick one or more from the list separated by comma
I can 
---
Acceptance tests:
- [ ] test 1
- [ ] test 2
---
Comments:
Espace commentaire on peut se lacher
```
-->

## List
<!-- start  DO NOT DELETE THIS COMMENT -->
```json
{
    "title": "Account creation",
    "author": "comSA",
    "priority": "p1", //LEAVE AS IT IS
    "users" : [
        "GUEST"
    ], // FILL THE LIST
    "description": "create an account",
    "tests":[
        "There is account creation form.",
        "The account creation is secure.",
        "The database is filled.",
        "Form have ALL the options described in the specifications."
    ], // FILL THE LIST
    "commments": "Do we accept all the new users? Or do you need an access link ?"
}
```


```json
{
    "title": "Account logging in",
    "author": "comSA",
    "priority": "p1",
    "users" : [
        "USER"
    ],
    "description": "log in to my account",
    "tests":[
        "There is an account logging page",
        "The connection is secure",
        "The session is stored in cookies"
    ]
}
```


```json
{
    "title": "Editing Labels",
    "author": "comSA",
    "priority": "p1", //LEAVE AS IT IS
    "users" : [
        "HUMAIN",
        "ADMIN",
        "BUREAU"
    ], // FILL THE LIST
    "description": "create/delete/edit colored labels",
    "tests":[
        "There is a label creation option on ADMINS interface",
        "There is a label deletion option on ADMINS interface",
        "There is a label modification option on ADMINS interface",
        "Labels are stored in database"
    ]
}
```


```json
{
    "title": "Using Labels",
    "author": "comSA",
    "priority": "p1",
    "users" : [
        "USER"
    ],
    "description": "I can use labels",
    "tests":[
        "Edit option appear on users list page for ADMINS",
        "USERS can inspect their labels",
        "USERS can see other USERS labels",
        "USERS can sort Users List with Labels",
        "USERS can filter Users List with Labels"
    ]
}
```


```json
{
    "title": "Account creation",
    "author": "comSA",
    "priority": "p1", //LEAVE AS IT IS
    "users" : [
        "GUEST"
    ], // FILL THE LIST
    "description": "create an account",
    "tests":[
        "There is account creation form.",
        "The account creation is secure.",
        "The database is filled.",
        "Form have ALL the options described in the specifications."
    ], // FILL THE LIST
    "commments": "Do we accept all the new users? Or do you need an access link ?"
}
```


```json
{
    "title": "Editing dispos categories",
    "author": "comSA",
    "priority": "p2", //LEAVE AS IT IS
    "users" : [
        "HUMAIN",
        "ADMIN",
        "BUREAU"
    ], // FILL THE LIST
    "description": "create/delete/edit dispos categories",
    "tests":[
        "There is a dispos categories creation option for concerned users",
        "There is a dispos categories deletion option for concerned users",
        "There is a dispos categories edition option for concerned users",
        "Dispos categories are stored in database"
    ]
}
```


```json
{
    "title": "Editing dispos",
    "author": "comSA",
    "priority": "p2", //LEAVE AS IT IS
    "users" : [
        "HUMAIN",
        "ADMIN",
        "BUREAU"
    ], // FILL THE LIST
    "description": "create/delete/edit dispos inside",
    "tests":[
        "There is a dispos creation option for concerned users",
        "There is a dispos deletion option for concerned users",
        "There is a dispos edition option for concerned users",
        "Dispos are stored in database"
    ]
}
```

```json
{
    "title": "Using dispos",
    "author": "comSA",
    "priority": "p2", //LEAVE AS IT IS
    "users" : [
        "USER"
    ], // FILL THE LIST
    "description": "fill my personnal dispos and validate it FOREVER",
    "tests":[
        "Dispos of the User are stored in database FOREVER.",
        "User friendly filling interface."
    ], // FILL THE LIST
    "commments": ""
}
```


```json
{
    "title": "Editing Friends",
    "author": "Stophe and Ginny",
    "priority": "", //LEAVE AS IT IS
    "users" : [
        "USER"
    ], // FILL THE LIST
    "description": "manage who are my friends",
    "tests":[
        "There is a friend creation option on my personal account",
        "There is a friend deletion option on my personal account",
        "User’s Friends  are stored in database as USERS.",
        "Number of friends  are under the limit number of friends.",
        "Friends are stored in database."
    ], // FILL THE LIST
    "commments": "On ne peut ajouter que des gens qui sont déjà inscrit (ça oblige à motiver ses potes) et à choisir avec qui tu voudrais vraiment être. Sinon bonjour le BDE qui met 500 personnes en pote…"
}
```

```json
{
    "title": "Using Friends",
    "author": "Stophe and Ginny",
    "priority": "", //LEAVE AS IT IS
    "users" : [
        "HUMAIN",
        "ADMIN",
        "BUREAU"
    ], // FILL THE LIST
    "description": "use USER’s list of friend.",
    "tests":[
        "USERS can inspect their friends",
        "ADMIN, BUREAU, HUMAIN can see other USERS friends"
    ], // FILL THE LIST
    "commments": "La liste des amis est une donnée à caractère sensible, du coup géré par la partie donnée sensible"
}
```

```json
{
    "title": "Using no critical Personal data",
    "author": "Stopghe and Ginny",
    "priority": "", //LEAVE AS IT IS
    "users" : [
        "USER"
    ], // FILL THE LIST
    "description": "use no critical personal data (name, first name, telephone number, …)",
    "tests":[
        "USERS can inspect their no critical data",
        "USERS can see other USERS no critical data"
    ], // FILL THE LIST
    "commments": ""
}
```

```json
{
    "title": "Using critical Personal data",
    "author": "Stophe and Ginny",
    "priority": "p1", //LEAVE AS IT IS
    "users" : [
        "ADMIN",
        "HUMAIN",
        "BUREAU"
    ], // FILL THE LIST
    "description": "Use critical personal data (Date of birth, driver’s license, Friends...)",
    "tests": [
        "USERS can inspect their critical data",
        "ADMIN, HUMAIN, BUREAU can see other USERS critical data",
        "ADMIN, HUMAIN, BUREAU can sort Users List with Labels",
        "ADMIN, HUMAIN, BUREAU can filter Users List with Labels"
    ], // FILL THE LIST
    "commments": ""
}
```