---
title: "Gibbs vs Boltzmann Entropies"
year: 1965
abstract: >
  The status of the Gibbs and Boltzmann expressions for entropy has been
  a matter of some confusion in the literature. We show that: (1) the
  Gibbs $H$ function yields the correct entropy as defined in
  phenomenological thermodynamics; (2) the Boltzmann $H$ yields an
  "entropy" that is in error by a nonnegligible amount whenever
  interparticle forces affect thermodynamic properties; (3) Boltzmann's
  other interpretation of entropy, $S = k \ \textrm{log} W$, is consistent with
  the Gibbs $H$, and derivable from it; (4) the Boltzmann $H$ theorem
  does not constitute a demonstration of the second law for dilute
  gases; (5) the dynamical invariance of the Gibbs $H$ gives a simple
  proof of the second law for arbitrary interparticle forces; (6) the
  second law is a special case of a general requirement for any
  macroscopic process to be experimentally reproducible. Finally, the
  "anthropomorphic" nature of entropy, on both the statistical and
  phenomenological levels, is stressed.
author:
  ["E.T. Jaynes"]
---
## INTRODUCTION
IN the writer's 1962 Brandeis lectures on statistical mechanics, the
Gibbs and Boltzmann expressions for entropy were compared briefly, and
it was stated that the Gibbs formula gives the correct entropy, as
defined in phenomenological thermodynamics, while the Boltzmann $H$
expression is correct only in the case of an ideal gas. However, there
is a school of thought which holds that the Boltzmann expression is
directly related to the entropy, and the Gibbs' one simply erroneous.
This belief can be traced back to the famous Ehrenfest review
article,[^1] which severely criticized Gibbs' methods.[^2]

While it takes very little thought to see that objections to the Gibbs
$H$ are immediately refuted by the fact that the Gibbs canonical
ensemble does yield correct thermodynamic predictions, discussion with a
number of physicists has disclosed a more subtle, but more widespread,
misconception. The basic inequality of the Gibbs and Boltzmann $H$
functions, to be derived in Sec. II, was accepted as mathematically
correct; but it was thought that, in consequence of the "laws of large
numbers" the difference between them would be practically negligible in
the limit of large systems.

Now it is true that there are many different entropy expressions that go
into substantially the same thing in this limit; several examples were
given by Gibbs. However, the Boltzmann expression is not one of them; as
we prove in Sec. III, the difference is a direct measure of the effect
of interparticle forces on the potential energy and pressure, and
increases proportionally to the size of the system.

Failure to recognize the fundamental role of the Gibbs $H$ function is
closely related to a much deeper confusion about entropy, probability,
and irreversibility in general. For example, the Boltzmann $H$ theorem
is almost universally equated to a demonstration of the second law of
thermodynamics for dilute gases, while ever since the Ehrenfest
criticisms, it has been claimed repeatedly that the Gibbs $H$ cannot be
related to the entropy because it is constant in time.

Closer inspection reveals that the situation is very different. Merely
to exhibit a mathematical quantity which tends to increase is not
relevant to the second law unless one demonstrates that this quantity is
related to the entropy as measured experimentally. But neither the Gibbs
nor the Boltzmann $H$ is so related for any distribution other than the
equilibrium (i.e., canonical) one. Consequently, although Boltzmann's
$H$ theorem does show the tendency of a gas to go into a Maxwellian
velocity distribution, this is not the same thing as the second law,
which is a statement of experimental fact about the direction in which
the observed macroscopic quantities ($P,V,T$) change.

Past attempts to demonstrate the second law for systems other than
dilute gases have generally tried to retain the basic idea of the
Boltzmann $H$ theorem. Since the Gibbs $H$ is dynamically constant, one
has resorted to some kind of coarse-graining operation, resulting in a
new quantity $\mathcal{H}$, which tends to decrease. Such attempts
cannot achieve their purpose, because (a) mathematically, the decrease
in $\mathcal{H}$ is due only to the artificial coarse-graining operation
and it cannot, therefore have any physical significance; (b) as in the
Boltzmann $H$ theorem, the quantity whose increase is demonstrated is
not the same thing as the entropy. For the fine-grained and
coarse-grained probability distributions lead to just the same
predictions for the observed macroscopic quantities, which alone
determine the experimental entropy; the difference between $H$ and
$\mathcal{H}$ is characteristic, not of the macroscopic state, but of
the particular way in which we choose to coarse-grain. Any really
satisfactory demonstration of the second law must therefore be based on
a different approach than coarse-graining.

Actually, a demonstration of the second law, in the rather specialized
situation visualized in the aforementioned attempts, is much simpler
than any $H$ theorem. Once we accept the well-established proposition
that the Gibbs canonical ensemble does yield the correct equilibrium
thermodynamics, then there is logically no room for any assumption about
which quantity represents entropy; it is a question of mathematically
demonstrable fact. But as soon as we have understood the relation
between Gibbs' $H$ and the experimental entropy, Eq. (17) below, it is
immediately obvious that the constancy of Gibbs' $H$, far from creating
difficulties, is precisely the dynamical property we need for the proof.
It is interesting that, although this field has long been regarded as
one of the most puzzling and controversial parts of physics, the
difficulties have not been mathematical. Each of the above assertions is
proved below or in the Brandeis lectures, using only a few lines of
elementary mathematics, all of which was given by Gibbs. It is the
enormous conceptual difficulty of this field which has retarded progress
for so long. Readers not familiar with recent developments may, I hope,
be pleasantly surprised to see how clear and basically simple these
problems have now become, in several respects. However, as we will see,
there are still many complications and unsolved problems.

Inspection of several statistical mechanics textbooks showed that, while
most state the formal relations correctly, their full implications are
never noted. Indeed, while all textbooks give extensive discussions of
Boltzmann's $H$, some recent ones fail to mention even the existence of
the Gibbs $H$.[^3] I was unable to find any explicit mathematical
demonstration of their difference. It appeared, therefore, that the
following note might be pedagogically useful.
## THE BASIC INEQUALITY
We consider, as usual, a monoatomic fluid of $N$ particles. The ensemble
is defined by the $N$-particle distribution function, or Liouville
function, $W_N(x_1, p_1; x_2, p_2; \dots; x_N, p_N; t)$ which gives the
probability density in the full phase space of the system. The Gibbs $H$ is then 
$$
H_G = \int W_N \log W_N d\tau
$$
 and
the corresponding Boltzmann $H$ is
$$
H_B = N \int w_1 \log w_1 d\tau_1,
$$
 where $w_1(x_1, p_1; t)$ is the
single-particle probability density
$$
w_1(x_1, p_1; t) = \int W_N d\tau_{-1}.
$$

 Here and in the following,
we use the notation: $d\tau = d^3x_1 d^3p_1 \dots d^3x_N d^3p_N$,
$d\tau_1=d^3x_1 d^3p_1$, $d\tau_{-1}=d^3x_2 \dots d^3p_N$ to stand for
phase-volume elements in the full phase space, the space of one
particle, and the space of all particles except one, respectively.
Both the Gibbs and Boltzmann $H$ functions are often defined in slightly
different ways, in which one uses distribution functions with different
normalizations. This changes the numerical values by additive constants
which, for fixed $N$, are independent of the thermodynamic state and
therefore not relevant to the present discussion. These additive
constants are important, however, in connection with the "Gibbs paradox"
about entropy of mixing, and the resolution of this paradox by quantum
statistics is well known. The distribution functions used above are
understood to be probability densities; i.e., normalized according to
$\int W_N d\tau = \int w_1 d\tau_1 = 1$.

Using (3) and the fact that $W_N$ is symmetric under permutations of
particle labels, we can write $H_B$ in a more symmetrical form
$$
H_B = N \int W_N \log w_1(x_1, p_1) d\tau = \int W_N \log[w_1(1) \ \cdots w_1(N)] d\tau,
$$
 where we use the abbreviation: $(i) \equiv (x_i, p_i)$. We have, then,
$$
H_B - H_G = \int W_N \log \left[ \frac{w_1(1) \cdots w_1(N)}{W_N(1 \cdots N)} \right] d\tau.
$$

Now on the positive real axis, $\log x \leq (x-1)$, with equality if and
only if $x=1$. Therefore
$$
H_B - H_G \leq \int W_N \left[ \frac{w_1(1) \cdots w_1(N)}{W_N(1 \cdots N)} - 1 \right] d\tau = 0,
$$
 and we have proved
**Theorem 1:** The Gibbs and Boltzmann $H$ functions satisfy the
inequality 
$$
H_B \leq H_G,
$$
 with equality if and only if $W_N$ factors
"almost everywhere" into a product of single-particle functions
$$
W_N(1 \cdots N) = w_1(1) \cdots w_1(N).
$$
## CANONICAL ENSEMBLE
Theorem 1 holds for any symmetrical $W_N$. The magnitude of the
difference $(H_G - H_B)$ depends on the distribution function, and we
are particularly interested in the case of thermal equilibrium,
represented by the canonical distribution $W_N \sim \exp(-\beta H)$, where $\beta = (kT)^{-1}$ and $H$ is the Hamiltonian, taken of the form
$$
H = \sum_{i=1}^N \frac{p_i^2}{2m} + V(x_1 \cdots x_N),
$$
 where the
potential-energy function $V(x_1 \cdots x_N)$ is a symmetrical function
of the particle coordinates, which we suppose for simplicity depends
only the relative coordinates (relaxing this restriction by adding
gravitational potential energy leads to a number of interesting results,
but does not change the conclusions of this section). More explicitly, we have
$$
W_N = \left( \frac{\beta}{2\pi m} \right)^{3N/2} Q^{-1} \times \exp \left \{ -\beta V(x_1 \cdots x_N) - \beta \sum_i \frac{p_i^2}{2m} \right \},
$$
 where 
$$
\begin{split}
Q(\beta, \Omega) &= \int_\Omega \exp(-\beta V) d^3x_1 \cdots d^3x_N \\\\ &= \Omega \int_\Omega \exp(-\beta V) d^3x_2 \cdots d^3x_N
\end{split}
$$
 is the "configuration integral," and in the last
expression we have made use of the fact that $V$ depends only on
relative coordinates, and supposed the range of interparticle forces
negligibly small compared to the size of the container, so that the
final integration supplies only a factor $\Omega$. From (3), the
corresponding single-particle function is then
$$
w_1(x,p) = (\beta/2\pi m)^{3/2} \Omega^{-1} \exp(-\beta p^2/2m).
$$

 We
therefore have
$$
[w_1(1) \cdots w_1(N)] / W_N(1 \cdots N) = Q \Omega^{-N} e^{\beta V},
$$
 and (4) reduces to
$$
H_B - H_G = \log Q - N \log \Omega + \beta \langle V \rangle,
$$
 where
the angular brackets $\langle \ \rangle$ denote the canonical ensemble
average. It is also true that 
$$
\begin{aligned}
\langle V \rangle &= -\partial \log Q / \partial \beta, \\\\ \beta \langle P \rangle &= \partial \log Q / \partial \Omega,
\end{aligned}
$$
 where $P$ is the pressure; Eq. (11) are well-known
identities of the canonical ensemble. From (10), (11), we thus find that
on an infinitesimal change of state,
$$
d(H_B - H_G) = \beta d\langle V \rangle + \beta[\langle P \rangle - P_0] d\Omega,
$$
 where $P_0 = NkT/\Omega$ is the pressure of an ideal gas with the same
temperature and density. Introducing the "entropies" $S_i = -kH_i$ and
integrating (12) over a reversible path (i.e., a locus of equilibrium
states), we see that the difference varies according to
$$
(S_G - S_B)_2 - (S_G - S_B)_1 = \int_1^2 \frac{d\langle V \rangle + [\langle P \rangle - P_0]d\Omega}{T}.
$$

 Now from (9), using $\langle p^2 \rangle = 3mkT$, we find that
$$
S_B = \frac{3}{2}Nk \log(2\pi mkT) + Nk \log \Omega + \frac{3}{2}Nk,
$$
 from which 
$$
\begin{aligned}
\left(\frac{\partial S_B}{\partial T}\right)_\Omega dT &= \frac{3}{2} \frac{NkdT}{T} = \frac{d\langle K \rangle}{T} \\\\ \left(\frac{\partial S_B}{\partial \Omega}\right)_T d\Omega &= \frac{Nk}{\Omega}d\Omega = \frac{P_0 d\Omega}{T},
\end{aligned}
$$
 where $\langle K \rangle = \frac{3}{2}NkT$ is the total
kinetic energy. Over the reversible path (13) the Boltzmann entropy
therefore varies according to
$$
(S_B)_2 - (S_B)_1 = \int_1^2 \frac{d\langle K \rangle + P_0 d\Omega}{T},
$$
 and from (13), (14) we finally have for the Gibbs entropy
$$
(S_G)_2 - (S_G)_1 = \int_1^2 \frac{d\langle K+V \rangle + \langle P \rangle d\Omega}{T} = \int_1^2 \frac{dQ}{T}
$$

Equations (14), (15) are the main results sought. From them it is clear
that (a) the "Boltzmann entropy" is the entropy of a fluid with the same
density and temperature, but without interparticle forces; it completely
neglects both the potential energy and the effect of interparticle
forces on the pressure; (b) the Gibbs entropy is the correct entropy as
defined in phenomenological thermodynamics, which takes into account all
the energy and the total pressure, and is therefore equally valid for
the gas or condensed phases; (c) the difference between them is not
negligible for any system in which interparticle forces have any
observable effect on the thermodynamic properties. If the system
exhibits an equation of state or heat capacity different from those of
an ideal gas, the Boltzmann entropy will be in error by a corresponding
amount.
## THE SECOND LAW
We can now demonstrate the second law very easily, for the specialized
case usually considered. The following argument can be greatly
generalized, although we do not do so here.

It is well known[^4] that the canonical distribution (7) is uniquely
determined by a variational property; over all distributions $W_N$ that
agree with the experimental energy $U$, in the sense that the mean value
of the Hamiltonian is 
$$
\langle H \rangle = \int W_N H d\tau = U,
$$
 the
Gibbs $H$ attains an absolute minimum for the canonical distribution. For this case, we have
just shown that, if the arbitrary additive constant is properly adjusted
at a single point, then the Gibbs entropy $S_G = -kH_G$ will be the same
as the experimental entropy at all points. Therefore, the general
relation between $S_G$ and the experimental entropy $S_e$ is: over all
distributions $W_N$ that agree with the experimental energy in the sense
of (16), we have 
$$
S_G \leq S_e
$$
 with equality if, and only if, $S_G$
is computed from the canonical distribution (7).

At time $t=0$, let our system be in complete thermal equilibrium so that
all its reproducible macroscopic properties are represented by the
canonical distribution; then the equality holds in (17). Now force the
system to carry out an adiabatic change of state (i.e., one involving no
heat flow to or from its environment), by applying some time-dependent
term in the Hamiltonian (such as moving a piston or varying a magnetic
field). It is well known that the $N$-particle distribution function
varies according to the Liouville equation $\dot{W}_N = \{H(t), W_N\}$ where the right-hand side is the Poisson bracket; and in consequence
$H_G$ remains constant.

At a later time $t^\prime$, the system is allowed to come once more, but still
adiabatically, to equilibrium (which means experimentally that
macroscopic quantities such as pressure or magnetization are no longer
varying), so that a new experimental entropy $S_e^\prime$ can be defined. If
the time-developed distribution function $W_N(t^\prime)$ leads to a correct
prediction of the new energy $U^\prime$ in the sense of (16), then the
inequality (17) still holds. The fact that $H_G$ is a constant of the
motion then gives $S_e \leq S_e^\prime$, which is the second law.
## INTUITIVE MEANING OF THE SECOND LAW
The above proof has the merit of being almost unbelievably short, but
partly for that reason, the physical basis of the second law is not made
clear. In the following we are not trying to give a rigorous
mathematical demonstration; that has just been done. We are trying
rather to exhibit the basic intuitive reason for the second law. We
recall Boltzmann's original conception of entropy as measuring the
logarithm of phase volume associated with a macroscopic state. If
Boltzmann's interpretation $S = k \log W$ is to be compatible with
Gibbs' $S = -kH_G$, it must be true that the quantity $W=\exp(-H_G)$
measures, in some sense, the phase volume of "reasonably probable"
microstates.

Such a connection can be established as follows. Define a
"high-probability" region $R$ of phase space, consisting of all points
where $W_N \geq C$, and choose the constant $C$ so that the total
probability of finding the system somewhere in this region is
$(1-\epsilon)$, where $0 < \epsilon < 1$. Call the phase volume of this
region $W(\epsilon)$; in equations, 
$$
\int_R W_N d\tau = 1 - \epsilon,
$$
$$
\int_R d\tau = W(\epsilon).
$$

 Evidently, with a continuously varying
probability density $W_N$, it is not strictly meaningful to speak of the
"phase volume of an ensemble," without qualifications; but the "minimum
phase volume of 50% probability" or the "minimum phase volume of 99%
probability" do have precise meanings.

A remarkable limit theorem first noted by Shannon[^5] shows that for
most purposes the particular probability level $\epsilon$ is
unimportant. We quote the result without proof; it is an adaptation of
the fundamental "asymptotic equipartition property" (AEP) of Information
Theory.[^6] We suppose that the distribution function $W_N$ from which
$H_G$ and $W(\epsilon)$ are computed is either a canonical distribution
or a time-developed version of one resulting from some dynamical
perturbation; and that the system is such that the canonical ensemble
predicts relative fluctuations in energy which tend to zero as
$N^{-1/2}$ in the "thermodynamic limit" as $N \to \infty$ at constant
density. The Gibbs $H$ per particle, $H_G/N$, then approaches a definite
limit, and 
$$
\lim_{N \to \infty} \{ [H_G + \log W(\epsilon)]/N \} = 0
$$
 provided $\epsilon$ is not zero or unity. The principal feature of this
theorem, at first sight astonishing, is that the result is independent
of $\epsilon$. Changing $\epsilon$ does, of course, change
$W(\epsilon)$; and generally by an enormous factor. But the change in
$\log W(\epsilon)$ grows less rapidly than $N$, and in the limit it
makes no difference.

The intuitive meaning of this theorem is that the Gibbs $H$ does measure
the logarithm of phase volume of reasonably probable microstates and, remarkably, for a large system the amount per particle,
$\log W(\epsilon)/N$, becomes independent of just what we mean by
"reasonably probable." We are thus able to retain Boltzmann's original
formula, $S=k \log W$, which is seen to be precisely related to the
Gibbs $H$, not the Boltzmann one.

With this interpretation of entropy, let us reconsider the above
experiment. At time $t=0$, we measure a number of macroscopic parameters
$\{X_1(0), \dots, X_m(0)\}$ adequate to define the thermodynamic state.
The corresponding canonical distribution determines a high-probability
region $R_0$, of phase volume $W_0$. The aforementioned variational
property of the canonical ensemble now implies that, of all ensembles
agreeing with this initial data in the sense of (16), the canonical one
defines the largest high-probability region. The phase volume $W_0$
therefore describes the full range of possible initial microstates; and
not some arbitrary subset of them; this is the basic justification for
using the canonical distribution to describe partial information.
On the "subjective" side, we can therefore say that $W_0$ measures our
degree of ignorance as to the true unknown microstate, when the only
information we have consists of the macroscopic thermodynamic
parameters; a remark first made by Boltzmann.

But, and perhaps more pertinent, we can also say on the "objective"
side, that $W_0$ measures the degree of control of the experimenter over
the microstate, when the only parameters he can manipulate are the usual
macroscopic ones. On successive repetitions of the experiment, the
initial microstate will surely not be repeated; it will vary at random
over the high-probability region $R_0$.

When we carry out an adiabatic change of state, the region $R_0$ is
transformed, by the equations of motion, into a new region $R_1$. From
either the constancy of $H_G$, or directly from Liouville's theorem, the
phase volume remains unchanged; $W_1=W_0$. Each possible initial
microstate in $R_0$ uniquely determines a possible final one in $R_1$, and on successive repetitions of the experiment, the final state varies
over $R_1$ at random.

At the end of this experiment, under the new equilibrium conditions, we
note the new values $\{X_1(t), \dots, X_n(t)\}$ of the thermodynamic
quantities. Now consider the region $R^\prime$, consisting of all microstates
that are compatible with these new $X_i(t)$, whether or not they could
have resulted from the experiment just described; i.e., whether or not
they also lie in $R_1$. By (17) and (18), the final experimental entropy
is $S^\prime=k \log W^\prime$, where $W^\prime$ is the phase volume of $R^\prime$; the
experimental entropy is a measure of all conceivable ways in which the
final macrostate can be realized, and not merely of all ways in which it
could be produced in one particular experiment.

Now it is obvious that, if the observed change of state
$X_i(0) \to X_i(t)$ is to be experimentally reproducible, the region
$R_1$ resulting from the experiment must be totally contained in $R^\prime$.
But this is possible only if the phase volumes satisfy $W_1 \leq W^\prime$,
which is again the second law!

At this point, we finally see the real reason for the second law; since
phase volume is conserved in the dynamical evolution, it is a
fundamental requirement on any reproducible process that the phase
volume $W^\prime$ compatible with the final state cannot be less than the
phase volume $W_0$ which describes our ability to reproduce the initial
state.

But this argument has given us more than the second law; in the past the
notion "experimental entropy" has been defined, in conventional
thermodynamics, only for equilibrium states. It is suddenly clear that
the second law is only a very special case of a general restriction on
the direction of any reproducible process, whether or not the initial
and final states are describable in the language of thermodynamics; the
expression $S=k \log W$ gives a generalized definition of entropy
applicable to arbitrary nonequilibrium states, which still has the
property that it can only increase in a reproducible experiment. This
can be shown directly from Liouville's theorem, without any
consideration of canonical distributions or the asymptotic equipartition
theorem.

Finally, it is clear that this extension of the second law can be
subjected to experimental tests.

Returning to the case of equilibrium thermodynamics, these
considerations (which are easily extended to quantum statistics) lead us
to state the conventional second law in the form: *The experimental
entropy cannot decrease in a reproducible adiabatic process that starts
from a state of complete thermal equilibrium.*
The necessity of the last proviso is clear from a logical standpoint in
our derivation of the second law in Sec. IV; for if the preparation of
the system just before $t=0$ imposes any constraints other than those
implied by the canonical distribution, the manifold of possible initial
states will be reduced below $W_0$, and we shall not have an equality in
Eq. (17) initially. This necessity is also shown strikingly from an
experimental standpoint in the phenomenon of spin echos,[^7]$^,$[^8]
which is a gross violation of any statement of the second law that fails
to specify anything about the past history of the system. This proviso
has not been particularly emphasized before, but it has always been
obvious that some such condition would be needed before we had a really
air-tight statement of the second law, which could not be violated by a
clever experimenter. The future behavior of the system is uniquely
determined, according to the laws of mechanics, only when one has
specified perhaps $10^{24}$ microscopic coordinates and momenta; it
could not possibly be determined merely by the values of the three or
four quantities measured in typical thermodynamic experiments.

Specifying "complete thermal equilibrium" is still not as precise a
statement as we might wish. Experimentally, the only criterion as to
whether it is satisfied seems to be that the system is "aged," i.e.,
that it is quiescent, the macroscopic quantities $X_i$ unchanging, for a
sufficiently long time; and only experience can tell the experimenter
how long is "sufficiently long."

Theoretically, we can understand this requirement as meaning that, for
purposes of prediction, lack of knowledge of the present microstate can
be, in part, compensated by knowledge of the past history of the
macroscopic state. As we observe the system to be quiescent for a longer
and longer time, we become more and more confident that it is not in an
atypical microstate that will lead to "abnormal" behavior in the future.
In Hahn's experiment the spin system, having no observable net
magnetization at time $t=0$, is nevertheless able to develop,
spontaneously and almost magically, a large and reproducible
magnetization at a later time only because it "remembers" some very
atypical things that were done to it before $t=0$.

In this observation lies the clue that shows how to extend the
mathematical methods of Gibbs to a general formalism for predicting
irreversible phenomena; we must learn how to construct ensembles which
describe not only the present values of macroscopic quantities, but also
whatever information we have about their past behavior. The details of
this generalization will be given elsewhere.
## THE "ANTHROPOMORPHIC" NATURE OF ENTROPY
After the above insistence that any demonstration of the second law must
involve the entropy as measured experimentally, it may come as a shock
to realize that, nevertheless, thermodynamics knows of no such notion as
the "entropy of a physical system." Thermodynamics does have the concept
of the entropy of a thermodynamic system; but a given physical system
corresponds to many different thermodynamic systems.

Consider, for example, a crystal of Rochelle salt. For one set of
experiments on it, we work with temperature, pressure, and volume. The
entropy can be expressed as some function $S_v(T,P)$. For another set of
experiments on the same crystal, we work with temperature, the component
$e_{xy}$ of the strain tensor, and the component $P_z$ of electric
polarization; the entropy as found in these experiments is a function
$S_e(T, e_{xy}, P_z)$. It is clearly meaningless to ask, "What is the
entropy of the crystal?" unless we first specify the set of parameters
which define its thermodynamic state.

One might reply that in each of the experiments cited, we have used only
part of the degrees of freedom of the system, and there is a "true"
entropy which is a function of all these parameters simultaneously. 
However, we can always introduce as many new degrees of freedom as we 
please. For example, we might expand each element of the strain tensor 
in a complete orthogonal set of functions $\phi_k(x,y,z)$ 
$$
e_{ij}(x,y,z) = \sum_k A_{ijk} \phi_k(x,y,z)
$$
and by a sufficiently 
complicated system of levels, we could vary each of the first 1000 
expansion coefficients $a_{ijk}$ independently. Our crystal is now a 
thermodynamic system of over 1000 degrees of freedom; but we still 
believe that the laws of thermodynamics would hold. So, the entropy 
must be a function of over 1000 independent variables. There is no end 
to this search for the ultimate "true" entropy until we have reached 
the point where we control the location of each atom independently. But 
just at that point the notion of entropy collapses, and we are no 
longer talking thermodynamics!

From this we see that entropy is an anthropomorphic concept, not only in
the well-known statistical sense that it measures the extent of human
ignorance as to the microstate. *Even at the purely phenomenological
level, entropy is an anthropomorphic concept.* For it is a property, not
of the physical system, but of the particular experiments you or I
choose to perform on it.

This points up still another qualification on the statement of the
second law without which it is, strictly speaking, no law at all. If we
work with a thermodynamic system of $n$ degrees of freedom, the
experimental entropy is a function $S_n(X_1 \cdots X_n)$ of $n$
independent variables. But the physical system has any number of
additional degrees of freedom $X_{n+1}, X_{n+2}$, etc. We have to
understand that these additional degrees of freedom are not to be
tampered with during the experiments on the $n$ degrees of interest; otherwise one could easily produce apparent violations of the second
law.

For example, the engineers have their "steam tables," which give
measured values of the entropy of superheated steam at various
temperatures and pressures. But the H$_2$O molecule has a large electric
dipole moment; and so the entropy of steam depends appreciably on the
electric field strength present. It must always be understood implicitly
(because it is never stated explicitly) that this extra thermodynamic
degree of freedom was not tampered with during the experiments on which
the steam tables are based; which means, in this case, that the electric
field was not inadvertently varied from one measurement to the next.
Recognition that the "entropy of a physical system" is not meaningful
without further qualifications is important in clarifying many questions
concerning irreversibility and the second law. For example, I have been
asked several times whether, in my opinion, a biological system, say a
cat, which converts inanimate food into a highly organized structure and
behavior, represents a violation of the second law. The answer I always
give is that, until we specify the set of parameters which define the
thermodynamic state of the cat, no definite question has been asked!
It seems apparent, in view of complications which we have encountered in
the attempt to give a complete statement of the second law, that much
more work needs to be done in this field. Glib, unqualified statements
to the effect that "entropy measures randomness" are in my opinion
totally meaningless, and present a serious barrier to any real
understanding of these problems. A full resolution of all the questions
that can be raised requires a much more careful analysis than any that
has been attempted thus far. Perhaps the most difficult problem of all
is to learn how to state clearly what is the specific question we are
trying to answer? However, I believe that in the above arguments we have
been able to report some progress in this direction.
## ACKNOWLEDGMENTS
I have profited from discussions of these problems, over many years,
with Professor E. P. Wigner, from whom I first heard the remark,
"Entropy is an anthropomorphic concept." It is a pleasure to thank
Professor Wm. C. Band for reading a preliminary draft of this article,
and suggesting an important clarification of the argument.

[^1]: P. Ehrenfest and T. Ehrenfest, Encykl. Math. Wiss., IV 2, II,
    Issue 6 (1912). Reprinted in Paul Ehrenfest, Collected Scientific
    Papers, edited by M. J. Klein (North-Holland Press, Amsterdam,
    1959). English translation by M. J. Moravcsik, *The Conceptual
    Foundations of the Statistical Approach in Mechanics* (Cornell
    University Press, Ithaca, New York, 1959).

[^2]: Statistical Physics (1962 Brandeis Theoretical Physics Lectures,
    Vol. 3), edited by K. W. Ford (W. A. Benjamin, Inc., New York,
    1963), Chap. 4. Note that typographical errors occur in Eqs. 20, 49,
    74, 78, 94, and the inequality preceding Eq. 90.

[^3]: A notable exception is the monumental work of R. C. Tolman, *The
    Principles of Statistical Mechanics* (Oxford University Press,
    London, 1938). Tolman repeatedly stresses the superiority of Gibbs'
    approach, although he still attempts to base the second law on
    coarse-graining.

[^4]: E. T. Jaynes, Phys. Rev. **108**, 171 (1957).
[^5]: C. E. Shannon, Bell Syst. Tech. J. **27**, 379, 623 (1948);
    reprinted in C. E. Shannon and W. Weaver, *The Mathematical Theory
    of Communication* (University of Illinois Press, Urbana, Illinois,
    1949). See, particularly, Sec. 21.

[^6]: A. Feinstein, *Foundations of Information Theory* (McGraw-Hill
    Book Company, Inc., New York, 1958), Chap. 6.

[^7]: E. L. Hahn, Phys. Rev. **80**, 580 (1950).
[^8]: A. L. Bloom, Phys. Rev. **98**, 1104 (1955).
[^100]: Department of Physics, Washington University, St. Louis, Missouri