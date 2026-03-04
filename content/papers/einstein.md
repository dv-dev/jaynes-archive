---
title: "On The Einstein Condensation"
year: 1960
abstract: >
  Exact series expressions for the thermodynamic quantities of an ideal
  Bose gas are found in terms of the theta function of Jacobi. The
  Einstein condensation thus can be treated by rigorous mathematical
  argument. The nature of the "integral approximation" and its
  modification, employed in the usual treatment of the problem, is
  clearly revealed. For finite volume, the exact expansions of pressure
  and density in powers of the activity converge in an entirely
  different way than do the integral approximation expansions. The
  modified integral approximation, however, becomes exact in the limit
  $V \rightarrow \infty$, $N \rightarrow \infty$,
  $V/N \rightarrow \text{const}$.
author: ["E.T. Jaynes", "C.T. Chen-Tsai"]
---
The phenomenon of the Einstein condensation of an ideal boson system is
well known. In the usual procedure of evaluating the thermodynamic
quantities, one uses the "integral approximation", in which the
summations over energy eigenvalues of an individual boson, appearing in
the series expressing the thermodynamic quantities, are replaced by
integrals. This approximation, which gives the correct results in the
region of the homogeneous phase in the case of an infinite system,
requires an artificial modification to account for the condensation
region. The modification is made by treating the terms corresponding to
the ground state of the individual boson separately from the others.[^ref1]
In the present report we show that an exact mathematical treatment of
the Einstein condensation is feasible, and therefore the nature of the
usual "integral approximation" and its modification is revealed.

The fundamental expressions in the Bose-Einstein statistics for N, p and
E, denoting respectively the total number of bosons, the pressure and
the total energy of the system, are:
$$N = \sum_i \frac{g_i}{z^{-1}e^{\beta E_i} - 1} \tag{1}$$
$$p = \sum_i \frac{g_i}{z^{-1}e^{\beta E_i} - 1} \left(-\frac{\partial E_i}{\partial V}\right) \tag{2}$$
$$E = \sum_i \frac{E_i g_i}{z^{-1}e^{\beta E_i} - 1} \tag{3}$$
where
- $\beta = 1/kT$
- $k$ = Boltzmann constant
- $T$ = absolute temperature
- $z = \text{activity} = \exp{(\beta\mu)}$
- $\mu$ = chemical potential
- $E_i$ = the energy of the i-th individual boson state, which is a
  function of the volume V
- $g_i$ = the degeneracy of the i-th individual boson state.

The summation is taken over all boson states.

The expressions (1), (2) and (3), as is well known, can be derived
either from the canonical or grand canonical ensemble method. In the
grand canonical ensemble the independent variables are V, $\beta$ and z,
but in the canonical ensemble the independent variables are V, $\beta$
and N, therefore z changes with V. This familiar fact is important in
the later discussion of the limiting process $V \rightarrow \infty$.

Let us now choose the volume of the system to be a cubic box with side
length $L = V^{1/3}$, and impose periodic boundary conditions upon the
wave functions of the individual boson. The energy $E_i$ then takes the
following form: $$E_i = E_0 (n_x^2 + n_y^2 + n_z^2), \tag{4}$$ where
$$E_0 = h^2 / (2mV^{2/3}), \tag{5}$$ (m = mass of each boson, h = Planck's
constant), and $n_x$, $n_y$ and $n_z$ are
integers, including zero. To each $E_i$ there is generally more than one
set of integers, ($n_x$, $n_y$, $n_z$), satisfying (4), the number of
which is evidently $g_i$ (We assume here that the spin of each boson is
zero. If each boson has a spin S, then the degeneracy of each state will
be 2S + 1 times more).

From (4) and (5) we get immediately
$$-\frac{\partial E_i}{\partial V} = \frac{2}{3} E_i V^{-1}.$$ Hence (2)
and (3) have the following relation $$E = \frac{3}{2} pV, \tag{6}$$ which holds
also for the ideal Boltzmann or Fermi gas.

Since the lowest energy, $E_i$, in (4) is zero, an inspection of (1),
(2) and (3) shows that z must be always smaller than unity, i.e. the
range of z is $0 < z < 1$. Hence we can expand each term of the series
in (1) and (2) (consequently (3) by (6)) in power series in z and
interchange the order of the summation in the resulted repeated series,
which can be shown to be allowable.[^ref2] Thus we have
$$N = \sum_{l=1}^{\infty} z^l \left(\sum_i g_i e^{-l\beta E_i}\right) \tag{7}$$
$$p = \frac{2}{3} V^{-1} \sum_{l=1}^{\infty} z^l \left(\sum_i g_i E_i e^{-l\beta E_i}\right) \tag{8}$$

In the "integral approximation" the two series in the parentheses of
(7) and (8) are approximated by the following replacement:
$$\sum_i g_i (\dots) \rightarrow \int_0^\infty g(E)dE (\dots), \tag{9}$$ where
$$g(E) = 2\pi V \left(\frac{2m}{h^2}\right)^{3/2} E^{1/2}$$

This approximation, in a crude sense, amounts to taking the limit of infinite
volume in each term of the series in z in (7) and (8), while the correct
limiting procedure should sum the series before letting
$V \rightarrow \infty$. This raises a mathematical question about the
interchange of the order of these operations and a physical question
about the correct volume dependence of thermodynamic properties of the
ideal boson system.

We now show that the two series $$I = \sum_i g_i e^{-l\beta E_i},$$ 
$$J = -\frac{\partial I}{\partial l\beta} = \sum_i g_i E_i e^{-l\beta E_i}, \tag{10}$$ 
can be exactly expressed in terms of the theta function, $\theta(x)$,
which is defined by
$$\theta(x) = \sum_{n=-\infty}^{\infty} e^{-\pi n^2 x}, \tag{11}$$ and its
derivative. In fact, by (4) and (5), we have
$$I = \sum_{n_x=-\infty}^{\infty} \sum_{n_y=-\infty}^{\infty} \sum_{n_z=-\infty}^{\infty} e^{-l\beta E_0 (n_x^2 + n_y^2 + n_z^2)} = \left(\sum_{n=-\infty}^{\infty} e^{-l\beta E_0 n^2}\right)^3 = \theta^3\left(\frac{l\beta E_0}{\pi}\right) = \theta^3\left(\frac{l\lambda^2}{V^{2/3}}\right), \tag{12}$$ 
where $$\lambda = h\sqrt{\beta/2\pi m}. \tag{13}$$ The theta function has the
following properties: $\theta(x)$ is a monotonically decreasing function
in $0 < x < \infty$; $\theta(x) \rightarrow 0$, as $x \rightarrow 0$;
$\theta(x) \rightarrow 1$, as $x \rightarrow \infty$. See Fig. 1.
Besides it satisfies the following important functional relation:[^ref3]
$$\theta(x) = \frac{1}{\sqrt{x}}\theta\left(\frac{1}{x}\right). \tag{14}$$ Hence
(12) becomes
$$I = V\lambda^{-3}l^{-3/2}\theta^3\left(\frac{V^{2/3}}{l\lambda^2}\right). \tag{15}$$ 

By (15), (10) then becomes
$$J = \frac{3}{2}V\lambda^{-3}\beta^{-1}l^{-5/2}\Psi\left(\frac{V^{2/3}}{l\lambda^2}\right), \tag{16}$$ 
where $$\Psi(x) \equiv \theta^3(x) + 2x\theta^\prime(x)\theta^2(x). \tag{17}$$ 
The function $\Psi(x)$ has the following properties: $0 < \Psi(x) < 1$
for $0 < x < 1$; $\Psi(x) \rightarrow 1$, as $x \rightarrow \infty$;
$\Psi(x) \approx kx^{-5/2}e^{-\pi/x} \rightarrow 0$, as
$x \rightarrow 0$. See Fig. 1.
Substituting (15) and (16) into (7) and (8) respectively, we obtain the
exact expressions for N and p for any finite V:
$$\frac{N}{V} = \frac{1}{v} = \lambda^{-3} \sum_{l=1}^{\infty} l^{-3/2} \theta^3\left(\frac{V^{2/3}}{l\lambda^2}\right) z^l, \tag{18}$$ 
$$p = \lambda^{-3}\beta^{-1} \sum_{l=1}^{\infty} l^{-5/2} \Psi\left(\frac{V^{2/3}}{l\lambda^2}\right) z^l, \tag{19}$$ 
where v is the specific volume (number of particles per unit
volume)$^{-1}$.
The series (18) and (19) are convergent for $z < 1$ for any finite V,
and as $z \rightarrow 1$, $1/v \rightarrow \text{const}$ but p remains
finite. The p-v curve has no singular point as long as V is finite. See
Fig. 2, curve (a).
From (18) and (19) we notice that in the usual integral approximation
one replaces the functions
$\theta^3\left(\frac{V^{2/3}}{l\lambda^2}\right)$ and
$\Psi\left(\frac{V^{2/3}}{l\lambda^2}\right)$ by unity for all
$l = 1, 2, 3 \dots$. The replacement of
$\theta^3(\frac{V^{2/3}}{l\lambda^2})$ by 1 is a good approximation only
for those $l \ll V^{2/3}/\lambda^2$ since $\theta(x) \approx 1$ for
$x \gg 1$. For $l \gg V^{2/3}/\lambda^2$ we have from (14) that
$\theta\left(\frac{V^{2/3}}{l\lambda^2}\right) \approx \frac{\sqrt{l}\lambda}{V^{1/3}} \gg 1$,
hence it is not justified. In fact for $l \gg V^{2/3}/\lambda^2$, the
series (18) behaves like the series
$$\frac{1}{V} \sum_{l \gg V^{2/3}/\lambda^2} z^l$$ 
which diverges as $z \rightarrow 1$, in contrast to the finiteness of
the corresponding series in the "integral approximation". Thus in
considering the system in a finite volume, the integral approximation is
good only for sufficiently small values of z. Likewise the replacement
of $\Psi\left(\frac{V^{2/3}}{l\lambda^2}\right)$ by 1 is good also for
$l \ll V^{2/3}/\lambda^2$, but not for $l \gg V^{2/3}/\lambda^2$, since
there $\Psi\left(\frac{V^{2/3}}{l\lambda^2}\right) \rightarrow 0$.
However, in this case the exact series (19) converges more rapidly than
the corresponding approximate one, and the numerical error is always
small. We notice that as V becomes larger, the larger is the range of z
in which the integral approximation is applicable.

To show the condensation phenomenon of the ideal boson system, we have
to consider the properties of the system in the limit
$V \rightarrow \infty$. The expressions for $1/v$ and p to be
investigated, from (18) and (19), now are:
$$\frac{1}{v} = \lambda^{-3} \lim_{V\rightarrow\infty} \sum_{l=1}^{\infty} l^{-3/2} \theta^3\left(\frac{V^{2/3}}{l\lambda^2}\right) z^l, \tag{20}$$ 
$$p = \lambda^{-3}\beta^{-1} \lim_{V\rightarrow\infty} \sum_{l=1}^{\infty} l^{-5/2} \Psi\left(\frac{V^{2/3}}{l\lambda^2}\right) z^l. \tag{21}$$ 

A sufficient condition that the "lim" in (20) and (21) can be placed
inside the summation sign is that the series in (20) and (21) be
uniformly convergent with respect to V near $V = \infty$. To test this
condition two cases have to be considered, according to whether (20) and
(21) are originally regarded as derived from the canonical or grand
canonical ensemble method. In the latter case z is an independent
variable,
therefore the only V dependent factors in each term of the series in
(20) and (21) are $\theta^3\left(\frac{V^{2/3}}{l\lambda^2}\right)$ and
$\Psi\left(\frac{V^{2/3}}{l\lambda^2}\right)$ respectively. In the
former case z is a dependent variable, therefore varies with V also.

Let us first consider the case where z is an independent variable, along
with $\beta$ and V. Then it can be easily shown by the Weierstrass'
M-test[^ref4] that both the series in (20) and (21) are uniformly convergent
with respect to V near $V = \infty$ for all z in $0 \le z < 1$. Since
$\lim_{x\rightarrow\infty} \theta(x) = \lim_{x\rightarrow\infty} \Psi(x) = 1$,
we thus from (20) and (21) obtain the limiting expressions for $1/v$ and
p:
$$\frac{1}{v} = \lambda^{-3} \sum_{l=1}^{\infty} l^{-3/2} z^l, \tag{22}$$ 
$$p = \lambda^{-3}\beta^{-1} \sum_{l=1}^{\infty} l^{-5/2} z^l. \tag{23}$$ 

These
expressions are exactly the same as those obtained by "integral
approximation". This means that the "integral approximation" is
justified for calculating the thermodynamic quantities of the ideal
boson system in the limiting case of infinite volume. The p-v curve by
(22) and (23) is shown in Fig. 2, curve (b). Notice that the curve is
regular, extending from $v = \infty$ to the point
$$v = v_c = \lambda^{-3} \sum_{l=1}^{\infty} l^{-3/2} = 2.612 \lambda^{-3}$$
$$p = p_c = \lambda^{-3}\beta^{-1} \sum_{l=1}^{\infty} l^{-5/2} = 1.341 \lambda^{-3}\beta^{-1}.$$ 

There is no extension of the curve to the condensation region $v < v_c$,
which can be expressed analytically in (22) and (23). This is a general
characteristic of the grand canonical ensemble method, which exhibits
only thermodynamic relations of the homogeneous phases in the limit
$V \rightarrow \infty$. That the missing part $v < v_c$ is the
condensation region can be seen only through the graphical observation
that as V becomes larger the curve (a) in Fig. 2 is nearer to the
horizontal dotted line, i.e. p tends to $p_c$ throughout the region
$v < v_c$. But just as the limit is reached, the horizontal part of the
isotherm disappears, for (22) converges to a finite value for
$0 \le z \le 1$.

Next we consider z as depending on V besides v and $\beta$. We then
regard (20) and (21) as being derived from the canonical ensemble
method. To emphasize this we write z as z(V). Because of its absolute
convergence, we can rewrite the series in (20) in the following form:
$$\frac{\lambda^3}{V} \frac{z(V)}{1-z(V)} + \sum_{l=1}^{\infty} l^{-3/2} \phi\left(\frac{V^{2/3}}{l\lambda^2}\right) z^l, \tag{24}$$ 
where $$\phi(x) \equiv \theta^3(x) - x^{-3/2}$$
The function $\phi(x)$ has similar properties to $\Psi(x)$; i.e. $0 < \phi(x) < 1$
for $0 < x < 1$; $\phi(x) \rightarrow 1$, as $x \rightarrow \infty$;
$\phi(x) \approx 6x^{-5/2}e^{-\pi/x} \rightarrow 0$, as
$x \rightarrow 0$.
By these properties of $\phi(x)$ and those of $\Psi(x)$, it is easy to
show, again by the Weierstrass M-test, that the series in (24) and (21)
are
uniformly convergent with respect to V near $V=\infty$. Thus we have
$$\frac{1}{v} = \lim_{V\rightarrow\infty} \frac{1}{V}\frac{z(V)}{1-z(V)} + \lambda^{-3} \sum_{l=1}^{\infty} l^{-3/2} \lim_{V\rightarrow\infty} \phi\left(\frac{V^{2/3}}{l\lambda^2}\right)z^l(V), \tag{25}$$ 
$$p = \lambda^{-3}\beta^{-1} \sum_{l=1}^{\infty} l^{-5/2} \lim_{V\rightarrow\infty} \Psi\left(\frac{V^{2/3}}{l\lambda^2}\right) z^l(V). \tag{26}$$ 

Two regions of v have to be considered separately:

a) For $v > v_c$. In this case we must have
$$z_{00} = \lim_{V\rightarrow\infty} z(V) < 1.$$ 

For otherwise the
series in (25) would become $1/v_c$ as $V \rightarrow \infty$.

Consequently from (25) we get $1/v > 1/v_c$, which is contradictory to
our choice of the region of v. Thus from (25) and (26) we obtain
$$\frac{1}{v} = \lambda^{-3} \sum_{l=1}^{\infty} l^{-3/2} z_{00}^l,$$ 
$$p = \lambda^{-3}\beta^{-1} \sum_{l=1}^{\infty} l^{-5/2} z_{00}^l,$$ 
which are identical to (22) and (23). Thus we have reproduced the p-v
curve shown in Fig. 2, curve (b).

b) For $v < v_c$. z(V) then must tend to 1 as $V \rightarrow \infty$ in
such a way, from (25), that
$$\lim_{V\rightarrow\infty} \frac{1}{V} \frac{z(V)}{1-z(V)} = \frac{1}{v} - \frac{1}{v_c}.$$ 

Hence (26) becomes
$$p = \lambda^{-3}\beta^{-1} \sum_{l=1}^{\infty} l^{-5/2} = p_c,$$ 
which
is independent of v. Thus the region $v < v_c$ has a constant pressure,
characterising the condensation phenomenon.

The p-v curve of the cases (a) and (b) discussed above is shown in Fig.
3. The curve consists of two regular curves which meet at the singular
point $v=v_c$, $p=p_c$. The canonical ensemble method is thus contrasted
with the grand canonical ensemble one by being capable of describing the
condensation analytically.

We note that in the usual method in order to account for the
condensation region one modifies the "integral approximation" by
rewriting the expression for $N/V$ in the form of (24) and approximating
$\phi\left(\frac{V^{2/3}}{l\lambda^2}\right)$ by 1. This "modified
integral approximation" which gives the results we obtained in the
canonical ensemble method by some mathematically less rigorous arguments
may, according to our above discussions, be regarded not as a
modification to the "integral approximation", but as an entirely
different approach to the problem by using a different (i.e. canonical)
ensemble method.

# FIGURE CAPTIONS {#figure-captions .unnumbered}
**Fig. 1:** The functional behaviors of $\theta(x)$, $\Psi(x)$ and
$\phi(x)$.

**Fig. 2:** Curve (a) is the isotherm at finite volume. Curve (b) is the
isotherm at infinite volume obtained from the grand canonical ensemble
method. The dotted line is missing in the process
$V \rightarrow \infty$.

**Fig. 3:** The isotherm at infinite volume obtained from the canonical
ensemble method. The horizontal line shows the region of condensation.
<figure>
<figcaption>The functional behaviors of <span
class="math inline"><em>θ</em>(<em>x</em>)</span>, <span
class="math inline"><em>Ψ</em>(<em>x</em>)</span> and <span
class="math inline"><em>ϕ</em>(<em>x</em>)</span>.</figcaption>
</figure>
<figure>
<figcaption>Curve (a) is the isotherm at finite volume. Curve (b) is the
isotherm at infinite volume obtained from the grand canonical ensemble
method. The dotted line is missing in the process
$V \rightarrow \infty$.</figcaption>
</figure>
<figure>
<figcaption>The isotherm at infinite volume obtained from the canonical
ensemble method. The horizontal line shows the region of
condensation.</figcaption>
</figure>

[^ref1]: For example, A. Munster, Handbook of Physics, Vol. III/2 (Flugge), 1959.
[^ref2]: K. Knopp, Infinite Sequences and Series, Dover, p. 27. Dover, 1956.
[^ref3]: R. Courant and D. Hilbert, Methods of Mathematical Physics, Vol. 1, p. 75, Interscience, 1955.
[^ref4]: E. T. Whittaker and G. H. Watson, Modern Analysis, 4-th ed. Cambridge, 1957.
