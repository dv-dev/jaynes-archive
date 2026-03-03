---
title: "Violation of Boltzmann's H Theorem in Real Gases"
author: ["E.T. Jaynes"]
year: 1971
abstract: >
  The well-known variational (maximum-entropy) property of the
  Maxwellian velocity distribution is used to shed some light on the
  range of validity of the Boltzmann transport equation. It permits a
  characterization of the initial states for which the Boltzmann H
  theorem is violated. In particular, it is shown that: (a) Any
  monatomic system for which the equilibrium potential energy exceeds
  the minimum possible value possesses a continuum of initial states for
  which the approach to equilibrium takes place through an increase,
  rather than a decrease, in Boltzmann's H. (b) If the initial
  distribution of particles is spatially homogeneous and Maxwellian, the
  approach to equilibrium will take place through an increase (decrease)
  in the Boltzmann H, according as the initial potential energy is less
  (greater) than the equilibrium value. (c) A necessary condition for
  the H-theorem-violating phenomenon is that the approach to equilibrium
  takes place through a conversion of kinetic energy into potential
  energy; a sufficient condition requires also that the initial velocity
  distribution be sufficiently close to Maxwellian. (d) These
  H-theorem-violating conditions are readily attained experimentally;
  for example, the free expansion of oxygen gas at 160$^\circ$K and
  45-atm pressure produces an experimentally realizable violation of the
  Boltzmann H theorem.
---
## Introduction
Ever since the famous *Umkehreinwand* and *Wiederkehreinwand* of Zermelo
and Loschmidt, it has been clear that the Boltzmann H theorem, and
therefore the Boltzmann transport equation, cannot be of universal
validity, even for a dilute gas. Any system possesses certain initial
states for which the H theorem is violated. In one sense, these
H-theorem-violating states can be characterized at once, as those in
which the particle positions and velocities are so correlated that
*Stosszahlansatz* fails to hold. However, this is very abstract, and
gives no hint as to how, or whether, such states could be produced
experimentally.

It is often supposed that these H-theorem-violating states are in some
way exceptional, so that they may be disregarded in practice. While this
conclusion is undoubtedly correct in many cases, we show below that when
the system has an appreciable potential energy, there is a class of
initial conditions for which interparticle forces automatically produce
and maintain H-theorem-violating states, with the result that $\dot{H}$
remains positive, on the average, throughout the approach to
equilibrium. These conditions are, moreover, in no way exceptional; they
can be (and undoubtedly have been) produced experimentally.

The existence of this H-theorem-violating phenomenon was pointed out
briefly at the end of the writer's Brandeis lectures[^2] on statistical
mechanics; however, the class of states for which it occurs was
described incompletely, in terms of the average force acting on a
particle. We obtain below a simpler description, in terms of the kinetic
and potential energy of the system.
## Derivations
Consider a monatomic fluid consisting of $N$ particles of mass $m$,
confined to a box of volume $V$,
interacting through a potential energy
$U(\mathbf{x}_1 \cdots \mathbf{x}_N)$ which is a symmetric function of
the coordinates $\mathbf{x}_i$. All integrations over the coordinates
and velocities, $d^3x_i, d^3v_i$, are understood to be over the volume
$V$, and all of velocity space, respectively. The Boltzmann distribution
function $f(\mathbf{x}, \mathbf{v}, t)$ is normalized so that the number
of particles, total kinetic energy, and Boltzmann H are given,
respectively, by
$$
N = \int \int f(\mathbf{x}, \mathbf{v}, t) d^3x d^3v,
$$
$$
K = \int \frac{1}{2} m v^2 f(\mathbf{x}, \mathbf{v}, t) d^3x d^3v,
$$
$$
H = \int \int f \ln f d^3x d^3v.
$$

 The basic variational property is
$$
H \ge N \left[ \ln\left(\frac{N}{V}\right) - \frac{3}{2} + \frac{3}{2} \ln\left(\frac{3Nm}{4\pi K}\right) \right],
$$
 or more briefly, 
$$
H \ge A - B \ln K,
$$
 where, for fixed $N, V$, the constants $A$ and $B$ are
independent of the microstate. The equality applies in (2.4) if and only
if $f(\mathbf{x}, \mathbf{v}, t)$ is equal \"almost everywhere\" to the
Maxwellian distribution
$$
f_M(\mathbf{x}, \mathbf{v}, t) = (N/V)(\lambda/\pi)^{3/2} e^{-\lambda v^2}
$$
with 
$$
\lambda = 3Nm/4K.
$$
 *Proof*. On the positive real axis,
$\ln z \le (z-1)$, with equality if and only if $z=1$. Therefore,
$$
\int \int f \ln(f_M/f) d^3x d^3v \le \int \int [(f_M/f) - 1] d^3x d^3v = 0,
$$
with equality if and only if $f=f_M$ almost everywhere. The inequality
(2.7) is equivalent to 
$$
H \ge \int \int f \ln f_M d^3x d^3v,
$$
 and on
evaluating the right-hand side of (2.8), we have the result (2.4).
**[FIGURE: Possible states in the K-H plane, allowed by Eq. (2.4).]**
The above assertions now follow from the graphical interpretation of
(2.4). Figure 1 represents the plane whose coordinates are the Boltzmann
H and the total kinetic energy $K$. Any microstate determines a point on
this plane; a given point corresponds, of course, to many different
microstates. According to (2.4), the possible microstates are all mapped
onto the shaded region lying above the curve $H = A - B \ln K$, which
represents the locus of all spatially homogeneous Maxwellian velocity
distributions; the Maxwellian states thus form the boundary between
allowed and forbidden regions of the plane.

Starting from any initial state, represented by a point $P$, the
approach to equilibrium is represented by some trajectory in this plane.
We assume that, for an isolated system with a fixed total energy $E$,
there is a unique final equilibrium point $P_{eq}$ which (i) depends
only on $E$, and not on the particular initial state, and (ii) lies on
the Maxwellian boundary.[^3]

If the system is a nearly ideal gas, so that the potential energy is
negligible, then the kinetic energy is a constant of the motion, and
this trajectory can only be a vertical line terminating at the
Maxwellian boundary, in agreement with the Boltzmann H theorem. If there
is an appreciable potential energy of interaction, the image point may
move laterally, representing an interconversion of kinetic and potential
energy.

In Fig. 2, we show the locus of possible initial states corresponding to
a given total energy $E$. The potential energy is assumed to have a
unique minimum possible value $U_{min}$, and so the kinetic energy must
be bounded by $0 \le K \le K_{max}$, where $K_{max} = E - U_{min}$. If
the equilibrium kinetic energy
**[FIGURE: Location of H-theorem-violating states.]**
is less than $K_{max}$, there is a triangular region of
H-theorem-violating states, from which the approach to the equilibrium
point necessarily requires an average increase, rather than a decrease
in H.

It is seen that a necessary condition for the H-theorem-violating
phenomenon is that the initial kinetic energy be greater than $K_{eq}$,
so that kinetic energy is converted into potential energy in going to
equilibrium. The other statements (a)-(c) made in the abstract are
equally evident from inspection of Fig. 2. It is interesting that the
Maxwellian initial velocity distribution represents a \"maximally
H-theorem-violating\" condition, in the sense that for a given amount of
kinetic-potential-energy conversion, one obtains the maximum possible
increase in H.
## Discussion
In spite of implications to the contrary sometimes found in the
literature, the Boltzmann H theorem is not a demonstration of the second
law of thermodynamics.[^4] The H-theorem-violating phenomenon therefore
in no way represents a violation of the second law. As we have shown
elsewhere,[^5] in systems with an appreciable potential energy the
entropy is not determined by the Boltzmann H, but by the Gibbs H, which
is appreciably different and does not increase. These points are perhaps
emphasized most strongly by citing definite experiments in which, if we
attempted to define the entropy in terms of the Boltzmann H, we would be
forced to conclude that the second law had been violated.

In order to realize the H-theorem-violating phenomenon experimentally,
one must produce an initial nonequilibrium state in which the kinetic
energy is greater than its final equilibrium value. This might be
accomplished by suddenly adding kinetic energy to a system; thus in the
initial stages of an explosion, particles acquire a high kinetic energy,
and the subsequent hydrodynamic motion separates them against attractive
forces; in some cases it might be possible to produce the
H-theorem-violating condition in this way.

An easier method is to remove suddenly a volume constraint (for example,
by opening a valve), thus allowing a gas to expand freely into a vacuum.
From (2.4) and the relation $K = \frac{3}{2}NkT$, the Boltzmann H for a
system in thermal equilibrium at temperature $T$ may be written as
$$
H = C - N \ln V - \frac{3}{2} N \ln T,
$$
 where $C$ is independent of
the thermodynamic state. If the gas is allowed to expand freely from
volume $V$ to an infinitesimally greater one $V+\delta V$, the condition
that H will increase in going to the new equilibrium state is thus
$$
\left( \frac{\partial T}{\partial V} \right)_E < -\frac{2T}{3V},
$$
from which it appears that the substances commonly used as refrigerants
would be the best candidates; however, this condition is readily
attained with almost any gas, as the following argument shows.

Using well-known thermodynamic identities, the condition (3.2) may be
written in terms of the equation of state as
$$
T \left( \frac{\partial P}{\partial T} \right)_V - P > \frac{2 C_v T}{3V},
$$
where $P$ is the pressure, and $C_v$ the specific heat at constant
volume. For a gas obeying the van der Waals equation of state
$(P+aV^{-2})(V-b) = NkT$, (3.3) reduces to $2C_vTV < 3a$, which can
always be satisfied above the critical temperature by sufficiently high
pressure.

In terms of the enthalpy, $h=E+PV$, (3.3) becomes
$$
\left( \frac{\partial h}{\partial T} \right)_P - \frac{PV}{T} > \frac{2}{3}C_v,
$$
in which form the left-hand side can be read off from the published
Mollier charts for various substances.[^6] From the Mollier chart of
oxygen we find that for 1 mole at $T=160\ ^\circ$K, $P=45$ atm,
$(\partial h / \partial T)_P = 12$ cal deg$^{-1}$, and $V = 200$ cm$^3$,
from which $PV/T \approx 1.3$ cal deg$^{-1}$, making the left-hand side
of (3.4) equal to 10.7 cal deg$^{-1}$. Since
$\frac{2}{3} C_v = \frac{2}{3} \cdot \frac{5}{2} Nk \approx 5.0$ cal
deg$^{-1}$, the right-hand side of (3.4) is 8.3 cal deg$^{-1}$. The
inequality is thus well satisfied, and we conclude that free expansion
of oxygen gas at 160 $^\circ$K and 45 atm would produce a violation of
the Boltzmann H theorem. (Although in Sec. II we had in mind the case of
a monatomic gas, the analysis is valid for polyatomic ones, provided we
interpret $K$ as representing only the translational kinetic energy.)
It has, of course, been recognized from the start that the original
derivation of the Boltzmann transport equation, from which the H theorem
follows, is valid only for a dilute gas. This in itself does not prove
that the transport equation is necessarily incorrect in other cases; and
indeed it has been used extensively in treatments of transport phenomena
in imperfect gases, liquids, plasmas, and solids, while many attempts
have been made to derive it under less restrictive assumptions than used
by Boltzmann. To the best of the writer's knowledge, these analyses have
not led previously to the discovery of specific experimental situations
in which the Boltzmann equation can be shown to give a qualitatively
incorrect result. In the case of oxygen at 160 $^\circ$K and 45 atm, the
mean free path estimated from the kinetic theory cross sections is
still about 15 Å; so one might have expected Boltzmann's assumptions to
be more nearly justified than in many applications to plasmas and
solids. Our results suggest that, instead of seeking to characterize the
physical systems for which the Boltzmann transport equation is valid, it
may be more appropriate to seek, for a given physical system, to
characterize the *initial states* for which it is valid. The analysis
given here, of course, is very far from answering this question.

[^1]: Work supported by the Air Force Office of Scientific Research,
    Contract No. F44620-60-C-0121.

[^2]: E. T. Jaynes, in *Statistical Physics*, edited by K. W. Ford
    (Benjamin, New York, 1963), Vol. 3, Chap. 4.

[^3]: This assumption appears to be one of the \"fundamental\"
    propositions of statistical mechanics; i.e., one which has never
    been proved or doubted; and we do neither here. We have, of course,
    the well-known fact that the Maxwellian distribution with a
    particular partitioning of total energy between kinetic and
    potential, corresponds to an overwhelmingly greater phase volume
    than any other disposition of the energy; this makes it highly
    plausible, but does not prove, that a physical system will go to
    this equilibrium condition. In addition, we have excellent
    experimental evidence that the assumption is correct for all
    systems; otherwise it is very hard to see how the propositions of
    elementary thermodynamics (existence of a definite, reproducible
    equation of state, heat capacity, etc.) could be valid.

[^4]: For a particularly clear explanation of this point, see T. L.
    Hill, *Statistical Mechanics* (McGraw-Hill, New York, 1956), pp.
    91-96.

[^5]: E. T. Jaynes, Am. J. Phys. **33**, 391 (1965).
[^6]: R. B. Scott, *Cryogenic Engineering* (van Nostrand, Princeton, N.
    J., 1959).
