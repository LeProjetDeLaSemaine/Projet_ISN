Projet_ISN
-------------
Ce projet est celui que nous présenterons lors de notre oral d'ISN, pour le baccalauréat général.
Le thème abordé est celui de la compression de données, c'est-à-dire l'obtention de données plus compactes (et donc plus faciles et rapides à transporter), à partir de données non compressées, plus volumineuses.

Clément DOUMERGUE & Ernest FOUSSARD

Actuellement, le projet comporte :
- une implémentation du codage par plages, qui détecte les caractères répétés et les remplace par le nombre de répétitions suivi du caractère.
- une implémentation de la compression selon l'algorithme de Huffman, expliqué (en anglais) dans la vidéo suivante: https://www.youtube.com/watch?v=ZdooBTdW5bM
- une implémentation de la transformée de Burrows-Wheeler, qui prédispose les données à être compressées, en réorganisant le texte. (Le décodage n'est pas encore implémenté)
- une implémentation de l'algorithme Move-To-Front.

