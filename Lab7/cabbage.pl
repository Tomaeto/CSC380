% Basic stack manipulation
% and solution to the farmer/cabbage/wolf/goat puzzle
% Stacks in Prolog are maintained as lists

empty_stack([]).

% Push, pop, and peek are all available in the one fact:
stack(Top,Stack,[Top|Stack]).

%  Some things added in class to look at Prolog!
valat([First|Rest],0,First).
valat([First|Rest], N, Val) :- N > 0, Nminus1 is N - 1, valat(Rest,Nminus1,Val).
commastack(Top,Stack,[Top,Stack]).

%  Just use the list member function to see if something is in a stack
member_stack(Element,Stack) :- member(Element,Stack).
%member(Element,[Element|List]).
%member(Element,[Y|List]):-member(Element,List).

add_list_to_stack(List,Stack,Result) :- append(List,Stack,Result).

reverse_print_stack(S) :- empty_stack(S).
reverse_print_stack(S) :-
   stack(E,Rest,S),
   reverse_print_stack(Rest),
   write(E),
   nl.

writelist([]):-nl.
writelist([H|T]):- write(H), tab(1),writelist(T).

%  A state gives the location of the farmer, wolf, goat, and cabbage, 
%  in that order.

unsafe(state(X,Y,Y,_)) :- opp(X,Y).
unsafe(state(X,_,Y,Y)) :- opp(X,Y).
opp(e,w).
opp(w,e).

%  Try moving the wolf:
move(state(X,X,G,C),state(Y,Y,G,C)) :- 
      opp(X,Y),
      \+(unsafe(state(Y,Y,G,C))),
      writelist(['try farmer takes wolf: ',Y,Y,G,C]).

%  Try moving the goat
move(state(X,W,X,C),state(Y,W,Y,C)):-
   opp(X,Y),
   \+(unsafe(state(Y,W,Y,C))),
   writelist(['try farmer takes goat: ', Y,W,Y,C]).

%  Try moving the cabbage
move(state(X,W,G,X),state(Y,W,G,Y)):-
   opp(X,Y),
   \+(unsafe(state(Y,W,G,Y))),
   writelist(['try farmer takes cabbage: ',Y,W,G,Y]).

%  Try moving just the farmer
move(state(X,W,G,C),state(Y,W,G,C)):-
   opp(X,Y),
   \+(unsafe(state(Y,W,G,C))),
   writelist(['try farmer takes self: ',Y,W,G,C]).

%  If this is our choice for move, we've come down a 
%  bad path and need to backtrack by failing.
move(state(F,W,G,C),state(F,W,G,C)) :-
   writelist(['backtrack from:', F,W,G,C]),
   fail.

%  The degenerate case of looking for a path is going from Goal to Goal
path(Goal,Goal,Been_stack) :-
   write('Solution path is:'),
   nl,
   reverse_print_stack(Been_stack).

%  Otherwise, we have to try moving.
path(State,Goal,Been_stack) :-
   move(State,Next_state),
   \+(member_stack(Next_state, Been_stack)),
   stack(Next_state, Been_stack, New_been_stack),
   path(Next_state, Goal, New_been_stack).
   %!.

go(Start,Goal) :-
   empty_stack(Empty_been_state),
   stack(Start, Empty_been_state, Been_stack),
   path(Start,Goal,Been_stack).

test:-go(state(w,w,w,w),state(e,e,e,e)).


