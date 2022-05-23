fib(1, 0).
fib(2, 1).

fib(N, NFib) :-
   N > 2, 
   NMinus1 is N - 1,
   NMinus2 is N - 2,
   fib(NMinus1, FibMinus1),
   fib(NMinus2, FibMinus2),
   NFib is FibMinus1 + FibMinus2.

