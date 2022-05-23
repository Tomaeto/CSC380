/****  FACTS  ****/

/* is_in_class facts:
 defines students in classes */

is_in_class(toby, csc380).
is_in_class(bob, csc480).
is_in_class(toby, csc480).
is_in_class(me, csc312).
is_in_class(me, csc340).

/* is_in_room facts:
 defines classes in rooms */
is_in_room(csc480, wsc100).
is_in_room(csc380, wsc238).
is_in_room(csc312, wsc234).
is_in_room(csc340, wsc234).

/* has_temperature facts:
 defines temperatures of rooms */
has_temperature(wsc100, 65).
has_temperature(wsc238, 92).
has_temperature(wsc234, 70).

/**** RULES ****/
/* Original is_hot rule:
 does not use wildcard variables */
/*
is_hot(Person) :-
	is_in_class(Person, Class),
	is_in_room(Class, Room),
	has_temperature(Room, Temp),
	Temp > 80.
*/

/* Modified is_hot rule:
 uses wildcard variables */

is_hot(Person) :-
	is_in_class(Person, _),
	is_in_room(_, _),
	has_temperature(_, Temp),
	Temp > 80.

