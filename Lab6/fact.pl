/* Base case: If X < 2, factorial is 1, and recursion ends */
fact(X, 1) :-
	X<2.

/* Rule for getting factorial Y of number X */
fact(X, Y) :-
/* Recursively get the factorial of X - 1 and multiply with X, ends
 * when X < 2 using base case */
	F is X - 1,
	fact(F, Z),
	Y is Z * X.

