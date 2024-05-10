def problem():
    '''
        Return the number of all reduced proper fractions whose denominator
        is less than d.

        Note that there are phi(d) number of reduced proper fractions whose denominator
        is d, hence the answer to this question is simply:

            sum_{k=2}^d phi(k).

        So the question is theoretically easy, but we may have trouble calculating the actual answer.
        Let Phi(d) denote the sum above. Instead of finding it directly, note that there are
        d(d + 1) / 2 tuples (n, m) with 1 <= n <= m <= d. As such

            Phi(d) = d * (d + 1) / 2 - sum_{k=2}^d Phi(floor(d / k)).

        Since floor(d / k) is small for quite a lot of k, we can instead sum over floor(d / k) and count
        the multiples:
                Phi(d) = d * (d + 1) / 2 - sum_{k=2}^sqrt(d) Phi(floor(d / k))
                                         - sum_{k=1}^{sqrt(d) - 1} (floor(d / k) - floor(d / (k + 1))) Phi(k)

        Here we basically grouped together floor(d / k) for all k >= sqrt(d).

    '''
