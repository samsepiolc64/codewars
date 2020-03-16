
def frobenius_number(*a):
    """
    Return the first number past which all numbers divisible by
    the gcd of the numbers can be made from non-negative multiples
    of positive integers in `a`; also report the gcd of the numbers.

    >>> frobenius_number(6,9,20)
    (43, 1)

    Any number larger than 43 can be created from combinations
    of 6, 9 and 20.

    >>> frobenius_number(20, 44)
    (159, 4)

    Starting at 160, all multiples of 4 can be made from
    combinations of 20 and 44.
    """

    from sympy import igcd

    # modified Bocker-Liptak implementation from https://brg.a2hosted.com/?page_id=563

    def __residue_table(a):
        from collections import defaultdict
        n = defaultdict(None)
        n[0] = 0
        for i in range(1, len(a)):
            d = igcd(a[0], a[i])
            for r in range(d):
                try:
                    nn = min(n.get(q) for q in range(r, a[0], d) if q in n)
                except ValueError:
                    continue  # e.g. a = 2,4,5 or 4,6,7
                for _ in range(a[0] // d):
                    nn += a[i]
                    p = nn % a[0]
                    if n.get(p) is not None:
                        nn = min(nn, n[p])
                    n[p] = nn
        return n

    a = [i for i in a if i]
    if len(a) == 0 or any(i < 0 for i in a):
        raise ValueError
    if len(a) == 1:
        return -(a[0] - 1)
    g = igcd(*a)
    if g != 1:
        n = frobenius_number(*[i // g for i in a])[0]
        return g * (n + 1) - 1, g
    a = sorted(a)
    return max(__residue_table(a).values()) - a[0], 1

frobenius_number(6,9,20)