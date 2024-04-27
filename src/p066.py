from math import floor, sqrt


def continued_fraction(d):
    '''
        Returns the continued fraction of sqrt(d), if d is not a square.
        The return value will be a list of the form
            [a_0, a_1, ..., a_r}]
        such that 
            sqrt(d) = [a_0; (a_1, a_2, ..., a_r)^*] (same notation as SageMath)
        i.e. the periodic part will be (a_1, ..., a_r)
    '''
    a0 = floor(sqrt(d))
    a = a0
    c = (d - a * a)
    partials = [a0, (a + a0) // c]
    while c != 1:
        a = partials[-1] * c - a
        c = (d - a * a) // c
        partials.append((a + a0) // c)
    return partials


def convergent(coefficients, n):
    '''
        Returns the n-th convergent of the given quadratic continued fraction
    '''
    p_prev, p_new = 1, coefficients[0]
    q_prev, q_new = 0, 1
    period = len(coefficients) - 1
    for i in range(0, n):
        ai = coefficients[1 + (i % period)]
        p_prev, p_new = p_new, ai * p_new + p_prev
        q_prev, q_new = q_new, ai * q_new + q_prev
    return p_new, q_new


def problem(b):
    '''
        Returns the smallest D <= b such that the associated pell equation
            x^2 - dy^2 = 1
        is maximal in x.

        This is a fun one: first note that there are clearly no solutions
        if D is a perfect square. On the other hand if D is not a perfect square
        then this has a solution if and only if Z[sqrt(D)] contains a nontrivial
        unit. By Dirichlet's unit theorem such an unit exists and in fact this induces
        the minimal solution. It therefore remains to compute this unit.

        In this case, this is rather easy.
        We first compute the continued fraction of sqrt(D), [a_0, (a_1, ..., a_r)^*].
        If p_{r - 1} / q_{r - 1} denotes the (r-1)-th convergent of sqrt(D). Then

                    p_{r-1}^2 - D * q_{r-1}^2 = (-1)^{r-1}.

        Hence if r is odd, then this is a solution to our equation. In fact, by some
        algebraic number theory it is the minimal solution [1, Thm 3.3.4]. If on the other hand
        r is even, then take p_{2r - 1} / q_{2r - 1} to conclude the same.

        Code below can still be optimized. For example, one could only consider
        the squarefree numbers D since for any D' that is not squarefree, there
        exists some k such that D' = k^2 D with D squarefree and thus any solution

                    x^2 - D (k^2 y) = 1

        has the same minimal solution in x.

        [1] Quadratic Diophantine Equations by Titu Andreescu and Dorin Andrica,
            2015.
    '''
    curr_max = (0, 0)
    for d in range(2, b):
        if int(sqrt(d)) == sqrt(d):
            continue
        cont_frac = continued_fraction(d)
        period = len(cont_frac) - 1
        if period % 2 == 0:
            x, _ = convergent(cont_frac, period - 1)
        else:
            x, _ = convergent(cont_frac, 2 * period - 1)
        if x > curr_max[0]:
            curr_max = (x, d)
    return curr_max[1]


if __name__ == "__main__":
    print(problem(7))
