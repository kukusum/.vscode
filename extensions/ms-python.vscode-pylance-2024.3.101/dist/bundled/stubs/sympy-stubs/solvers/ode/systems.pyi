from typing import Any
from sympy.core.relational import Eq, Ne, Relational
from sympy.matrices import Matrix
from sympy.solvers.solveset import NonlinearError

class ODEOrderError(ValueError):
    ...


class ODENonlinearError(NonlinearError):
    ...


def simpsol(sol, wrt1, wrt2, doit=...) -> list[Eq | Any | Relational | Ne]:
    ...

def linodesolve_type(A, t, b=...) -> dict[Any, Any]:
    ...

def linear_ode_to_matrix(eqs, funcs, t, order) -> tuple[list[Any], Any | Matrix]:
    ...

def matrix_exp(A, t):
    ...

def matrix_exp_jordan_form(A, t) -> tuple[Matrix, Any]:
    ...

def linodesolve(A, t, b=..., B=..., type=..., doit=..., tau=...) -> list[Any]:
    ...

def canonical_odes(eqs, funcs, t) -> list[Any]:
    ...

def dsolve_system(eqs, funcs=..., t=..., ics=..., doit=..., simplify=...) -> list[Any]:
    ...
