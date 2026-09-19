"""Independent finite checks for worked examples; not proofs of general theorems."""
import itertools
import unittest
from fractions import Fraction as Q


def functions(domain, codomain):
    return [dict(zip(domain, values)) for values in itertools.product(codomain, repeat=len(domain))]


def powerset(xs):
    return [set(c) for n in range(len(xs) + 1) for c in itertools.combinations(xs, n)]


class LogicAndCategoryExamples(unittest.TestCase):
    def test_implication_transitivity_and_invalid_converse(self):
        implies = lambda p, q: not p or q
        for p, q, r in itertools.product((False, True), repeat=3):
            self.assertTrue(implies(implies(p, q) and implies(q, r), implies(p, r)))
        p, q = False, True
        self.assertTrue(implies(p, q) and q)
        self.assertFalse(p)

    def test_quantifier_disjunction_counterexample(self):
        domain = ('a', 'b'); p = lambda x: x == 'a'; q = lambda x: x == 'b'
        self.assertTrue(all(p(x) or q(x) for x in domain))
        self.assertFalse(all(p(x) for x in domain) or all(q(x) for x in domain))

    def test_product_universal_property(self):
        a, b, x = (0, 1), (0, 1, 2), ('s', 't')
        maps = functions(x, tuple(itertools.product(a, b)))
        decomposed = {(tuple(h[t][0] for t in x), tuple(h[t][1] for t in x)) for h in maps}
        choices = {(tuple(f[t] for t in x), tuple(g[t] for t in x)) for f in functions(x, a) for g in functions(x, b)}
        self.assertEqual(decomposed, choices)
        self.assertEqual(len(maps), len(decomposed))
        self.assertEqual(len(maps), 36)

    def test_coproduct_universal_property(self):
        a, b, x = (0, 1), (0, 1, 2), ('s', 't')
        tagged = [('a', i) for i in a] + [('b', j) for j in b]
        restrictions = {(tuple(h['a', i] for i in a), tuple(h['b', j] for j in b)) for h in functions(tagged, x)}
        choices = {(tuple(f[i] for i in a), tuple(g[j] for j in b)) for f in functions(a, x) for g in functions(b, x)}
        self.assertEqual(restrictions, choices)
        self.assertEqual(len(restrictions), 32)

    def test_exponential_adjunction_currying_is_a_bijection(self):
        a, b, x = (0, 1), (0, 1, 2), ('s', 't')
        domain = tuple(itertools.product(x, a))
        hom_product = functions(domain, b)
        exponent = tuple(itertools.product(b, repeat=len(a)))
        curried = {tuple(tuple(h[t, i] for i in a) for t in x) for h in hom_product}
        hom_exponent = {tuple(k[t] for t in x) for k in functions(x, exponent)}
        self.assertEqual(curried, hom_exponent)
        self.assertEqual(len(curried), len(hom_product))
        self.assertEqual(len(curried), 81)
        for h in hom_product:
            k = {t: tuple(h[t, i] for i in a) for t in x}
            self.assertEqual({(t, i): k[t][i] for t, i in domain}, h)

    def test_existential_and_universal_image_adjunctions(self):
        x, y = (0, 1, 2), ('u', 'v', 'w'); f = {0: 'u', 1: 'u', 2: 'v'}
        for a in powerset(x):
            direct = {f[i] for i in a}
            universal = {j for j in y if {i for i in x if f[i] == j} <= a}
            self.assertIn('w', universal)
            for b in powerset(y):
                inverse = {i for i in x if f[i] in b}
                self.assertEqual(direct <= b, a <= inverse)
                self.assertEqual(inverse <= a, b <= universal)

    def test_free_monoid_homomorphism_example(self):
        value = lambda word: sum({'a': 1, 'b': 2}[letter] for letter in word) % 3
        words = [w for length in range(5) for w in itertools.product('ab', repeat=length)]
        self.assertEqual(value('aba'), 1)
        self.assertEqual(value(''), 0)
        for u in words:
            for v in words:
                self.assertEqual(value(u + v), (value(u) + value(v)) % 3)

    def test_finite_yoneda_naturality_and_evaluation(self):
        f0, f1 = ('a', 'b'), ('u',); restriction = {'u': 'a'}
        for represented, expected in [(0, 2), (1, 1)]:
            h0 = ('0-to-' + str(represented),)
            h1 = ('1-to-1',) if represented == 1 else ()
            natural = []
            for alpha0 in functions(h0, f0):
                for alpha1 in functions(h1, f1):
                    if all(restriction[alpha1[t]] == alpha0[h0[0]] for t in h1):
                        natural.append((alpha0, alpha1))
            self.assertEqual(len(natural), expected)
            evaluation = [a0[h0[0]] if represented == 0 else a1[h1[0]] for a0, a1 in natural]
            self.assertEqual(set(evaluation), set(f0 if represented == 0 else f1))
            self.assertEqual(len(evaluation), len(set(evaluation)))

    def test_one_object_functor_preserves_identity_and_composition(self):
        f = lambda n: 2 * n
        self.assertEqual(f(0), 0)
        for m, n in itertools.product(range(20), repeat=2):
            self.assertEqual(f(m + n), f(m) + f(n))


class BranchExamples(unittest.TestCase):
    def test_modular_arithmetic(self):
        self.assertEqual([i for i in range(8) if any(i*j%8 == 1 for j in range(8))], [1,3,5,7])
        self.assertTrue(all(i*i%8 == 1 for i in [1,3,5,7]))
        self.assertEqual(2*3%6, 0)
        self.assertEqual(17*38%43, 1)
        self.assertEqual([i for i in range(10) if 6*i%10 == 4], [4,9])
        self.assertTrue(all(any(i*j%5 == 1 for j in range(5)) for i in range(1,5)))

    def test_rational_circle(self):
        t = Q(1,2); x=(1-t*t)/(1+t*t); y=2*t/(1+t*t)
        self.assertEqual((x,y), (Q(3,5),Q(4,5)))
        self.assertEqual(x*x+y*y, 1)

    def test_hilbert_projection_exact_rational_integrals(self):
        # p=x^2-x+1/6, orthogonal to 1 and x on [0,1].
        coefficients = [Q(1,6), Q(-1), Q(1)]
        self.assertEqual(sum(c/Q(i+1) for i,c in enumerate(coefficients)), 0)
        self.assertEqual(sum(c/Q(i+2) for i,c in enumerate(coefficients)), 0)
        norm=sum(c*d/Q(i+j+1) for i,c in enumerate(coefficients) for j,d in enumerate(coefficients))
        self.assertEqual(norm, Q(1,180))

    def test_binary_strings_and_even_parity(self):
        counts=[]
        for n in range(9):
            strings=[''.join(s) for s in itertools.product('01',repeat=n)]
            counts.append(sum('11' not in s for s in strings))
            if n:self.assertEqual(sum(s.count('1')%2==0 for s in strings), 2**(n-1))
        self.assertEqual(counts[:2],[1,2]);self.assertEqual(counts[5],13)
        for n in range(2,9):self.assertEqual(counts[n],counts[n-1]+counts[n-2])

    def test_coin_moments_and_constrained_minimum(self):
        values=[a+b for a,b in itertools.product((0,1),repeat=2)]
        mean=sum(map(Q,values))/4
        self.assertEqual(mean,1)
        self.assertEqual(sum((x-mean)**2 for x in values)/4,Q(1,2))
        for x in (Q(n,17) for n in range(-40,41)):
            self.assertEqual(x*x+(1-x)**2,Q(1,2)+2*(x-Q(1,2))**2)


if __name__ == '__main__':
    unittest.main()
