size([],0).
size([H|T],N) :- size(T,N1), N is N1+1.

sumlist([],0).
sumlist([H|T],N) :- sumlist(T,N1), N is N1+H.

reverse([], Reversed, Reversed).
reverse([Head|Tail], SoFar, Reversed) :-
          reverse(Tail, [Head|SoFar], Reversed).
