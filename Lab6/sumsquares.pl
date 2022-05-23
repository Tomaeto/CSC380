/* Base case: If X = 1, square is 1 and recursion ends */
sumsquares(X, 1) :-
	X = 1.

/* Rule for recursively finding sum Y of squares b/w 1 and X. */
sumsquares(X, Y) :-
/*Recursively get square of X - 1 and add to square of X, ends when S = 1
 * due to base case */
	S is X - 1,
	sumsquares(S, Z),
	Y is X*X + Z.
