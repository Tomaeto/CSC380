/*** FACTS ***/
hassize(bluebird, small).
hascovering(bird, feathers).
hascolor(bluebird, blue).
hasproperty(bird, flies).
isa(bluebird, bird).
isa(bird, vertebrate).

/*** RULE ***/

isbird(Animal) :-
/* If Animal is a bird and has any color and size, it is a bird. */
	(isa(Animal, bird),
	hascolor(Animal, _),
	hassize(Animal, _));

/* Or, if Animal is a vertebrate with feathers and can fly, it is a bird. */
	(isa(Animal, vertebrate),
	hascovering(Animal, feathers),
	hasproperty(Animal, flies)).
