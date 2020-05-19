# Générateur de table de vérité
Ce code python génère automatiquement une table de vérité d'une expression logique (LE), telle que (p v (p ^ q)) ^! P -> r.

# Opérations prises en charge

Mon code prend en charge 5 opérateurs:
- NON: noté '!' ou '-' .
- ET: noté '^' ou '.' .
- OU: noté «v» ou «+».
- Implication matérielle: notée «->» ou «>».
- équivalence: notée '<->' ou '~'.

** Ordre des opérations **: PAS> ET = OU> Implication matérielle = Équivalence
- Les opérateurs NOT calculent en premier (priorité la plus élevée).
- Ensuite, les opérateurs ET et OU.
- Enfin, l'implication matérielle et l'équivalence (priorité la plus basse).
- Il calculera de gauche à droite si 2 opérateurs ont le même ordre.
# Comment utiliser
- voire le fichier file.txt vous pouviez dans ce dernier poser votre expresion dans la 5 eme ligne a la place de s'elle trouver la-bas 
Vous pouvez utiliser une lettre miniscule pour représenter les variables, mais n'utilisez pas 'v' comme variable, car il s'agit d'un opérateur dans mon code. 
Par conséquent, vous pouvez utiliser au maximum 25 variables. Mais ma complexité temporelle est d'environ O (2 ^ n) avec une tonne de constantes, donc vous ne devriez pas utiliser trop de variables, moins de 15 variables est correct.

-[TruthTableGenerator.py] (TruthTableGenerator.py) et exécutez-le par la commande `python TruthTableGenerator.py`, 

# Example
Ma epression is: (p v (p ^ q)) ^ !p -> r.

Et voila sa serais sa table de verite:
```
  p  |  q  |  r  |  (p v (p ^ q)) ^ !p -> r
  0  |  0  |  0  |  1
  0  |  0  |  1  |  1
  0  |  1  |  0  |  1
  0  |  1  |  1  |  1
  1  |  0  |  0  |  1
  1  |  0  |  1  |  1
  1  |  1  |  0  |  1
  1  |  1  |  1  |  1
```
