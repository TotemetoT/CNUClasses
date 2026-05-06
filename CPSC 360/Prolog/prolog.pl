% ---Reverse---
reverse([], []).
reverse([H|T], R) :-
    reverse(T, RevT),
    append(RevT, [H], R).

% ---Palindrome---
palindrome([]).
palindrome(A) :- 
    reverse(A,A).

% ---Left---
left(B, B, N) :-
    N =< 0, !.

left(A, B, N) :-
    N > 0,
    rotate_left(B, B1),
    N1 is N - 1,
    left(A, B1, N1).

rotate_left([], []).
rotate_left([H|T], R) :-
    append(T, [H], R).

% ---Range---
range([], B, C) :-
    B >= C, !.

range([B|Rest], B, C) :-
    B < C,
    B1 is B + 1,
    range(Rest, B1, C).

% ---ModZero---

modzero([], _, []).

modzero([X|Rest], B, [X|Tail]) :-
    0 is B mod X,              % Check divisibility
    modzero(Rest, B, Tail).

modzero(Rest, B, [_|Tail]) :-
    modzero(Rest, B, Tail).

% ---Factors---
factors(A, B) :-
    B > 2,
    B1 is B - 1,
    range(C, 2, B1),
    modzero(A, B, C).

factors([], B) :-
    B =< 2.

% ---Prime---
prime(A) :-
    A =< 1, !, fail.
prime(A) :-
    factors(F, A),
    F == [].


% ---Visit---
all_different([]).
all_different([H|T]) :-
    \+ member(H, T),
    all_different(T).

visit(B, C, D, E, F) :-
    % positions 1–5 for each family
    member(B, [1,2,3,4,5]),
    member(C, [1,2,3,4,5]),
    member(D, [1,2,3,4,5]),
    member(E, [1,2,3,4,5]),
    member(F, [1,2,3,4,5]),

    all_different([B,C,D,E,F]),

    % 1. Belskys first or last
    (B = 1 ; B = 5),

    % 2. Conners 4th
    C = 4,

    % 3. Davies earlier than Conners
    D < C,

    % 4. Estevez two after Flores
    E is F + 2,

    % 5. Flores not 3rd
    F \= 3.