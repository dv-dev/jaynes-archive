---
title: "Irreversible Statistical Mechanics"
year: 1963
abstract: >
  A general formalism for calculation of irreversible processes,
  analogous to the partition sum algorithm of equilibrium theory, is
  presented. Mathematically, it is a generalization of the procedure by
  which Gibbs constructed his canonical and grand canonical ensembles,
  in which the partition function is extended to a partition functional.
  Conceptually, it has a simple interpretation in terms of Information
  Theory. By this means, ensembles can be constructed in which
  macroscopic quantities have any space-time dependence compatible with
  the Hamiltonian of the system. We illustrate its use by developing a
  theory of transport phenomena, in which the following features emerge:
  (1) Dissipative effects are obtained by direct quadratures over the
  new ensembles, with no need for the forward integration and
  coarse-graining operations characteristic of previous treatments. In
  consequence, the theory is not restricted to the quasi-stationary,
  long-wavelength limit; it applies equally well to phenomena such as
  ultrasonic attenuation. (2) The formalism leads to a nonlocal theory,
  and to expressions for linear transport coefficients closely related
  to those of Kubo. Ensembles are exhibited in which Kubo's formulas are
  exact. (3) The statistical analog of the Cauchy initial-value problem
  is included as a special case. In linear approximation it is found to
  be mathematically equivalent to Norbert Wiener's theory of optimal
  prediction of the future of a random function whose past is given. (4)
  The statistical analog of the Dirichlet-Neumann boundary-value
  problem, often a more realistic description of experimental
  conditions, is also included as a special case. It contains a
  "statistical Kirchoff-Huygens principle", according to which use of
  certain information about the macroscopic state can make other kinds
  of information redundant for certain predictions. (5) The theory
  yields a mathematically unambiguous rule for calculation of nonlinear
  effects, such as those due to extremely large temperature or
  concentration gradients, which are not easily described in terms of a
  dynamical perturbation on the system.
author: ["E.T. Jaynes", "D.J. Scalapino"]
categories: ["Statistical Mechanics & Thermodynamics"]
tags: ["irreversible processes", "Gibbs algorithm", "Information Theory", "transport phenomena", "Kubo formulas", "Wiener prediction theory", "dissipative effects"]
---
## 1. INTRODUCTION
In recent years the theory of nonequilibrium statistical mechanics has
made great progress in the sense of successful calculation of several
particular effects. Many workers have speculated on the possibility that
we may eventually learn how to formulate this theory with a generality
comparible to that of the partition sum algorithm of equilibrium theory,
in which a single formal rule applies to all cases. The basic principles
have, however, remained so obscure that one has not seen how to carry
out this generalization, and doubt has even been expressed[^1] as to
whether such a development is possible. It now appears that the missing
formal principle has long been known, and special cases of it have been
used by almost every worker in statistical mechanics; but conceptual
difficulties have prevented us from seeing its generality.

The calculation of an irreversible process usually involves three
distinct stages: (1) Setting up an "ensemble," i.e. choosing a density
matrix $\rho(0)$, or an N-particle distribution function, which is to
describe the initial state of the system of interest; (2) Solving the
dynamical problem; i.e. applying the microscopic equations of motion to
obtain the time-evolution of the system $\rho(t)$; (3) Extracting the
final physical predictions from the time-developed ensemble $\rho(t)$.
Stage (3) has never presented any procedural difficulty; to predict the
quantity F from the ensemble $\rho$, one computes the expectation
value $\langle F \rangle = \text{Tr}(\rho F)$. While the ultimate
justification of this rule has been much discussed (ergodic theory), no
alternative procedure has been widely used.

In this connection, we note the following. Suppose we are to choose a
number f, representing our estimate of the physical quantity F,
based on the ensemble $\rho$. A reasonable criterion for the "best"
estimate is that the expected square of the error,
$\langle (F-f)^2 \rangle$ shall be made a minimum. The solution of this
simple variational problem is: $f = \langle F \rangle$. Thus, if we
regard statistical mechanics as an example of statistical estimation
theory based on the mean square error criterion, the usual procedure is
uniquely determined as the optimal one, independently of ergodic theory.
A justification not depending on ergodic theory is, of course, necessary
as soon as we try to predict time-varying quantities. This point, and the
reason for the reliability of the predictions made by the present
theory, are discussed further in Appendix A.

The dynamical problem of stage (2) is the most difficult to carry out,
but it is also the one in which most recent progress has been booked
(Green's function methods). While the present paper is not primarily
concerned with these techniques, they are available, and needed, in
carrying out the calculations indicated here for all but the simplest
problems.

It is curious that stage (1), which must logically precede all the
others, has received virtually no attention since the pioneering work of
Gibbs, in which the problem of ensemble construction was first
recognized. Most recent discussions of irreversible processes
concentrate all attention on stage (2); some fail to note even the
existence of stage (1). One consequence of this is that the resulting
theories apply unambiguously only to the case of "response functions",
in which the nonequilibrium state is one resulting from a dynamical
perturbation (i.e., an explicitly given term in the Hamiltonian),
starting from thermal equilibrium in the remote past; the initial
density matrix is then given by conventional equilibrium theory.

If, however, the nonequilibrium state is defined (as it usually is from
the experimental standpoint) in terms of temperature or concentration
gradients, rate of heat flow, shearing stress, sound wave amplitudes,
etc., such a procedure does not apply -- at least, not unambiguously. An
extreme example is provided by some problems in astrophysics, in which
it is clear that the system of interest has never, in the age of the
universe, been in a state approximating thermal equilibrium. Such cases,
which have been well recognized[^2][^3] as presenting special
difficulties of principle, are just the ones in which the problem of
stage (1) cannot be evaded.

The main result of the present work is this: recognition of the
existence of the stage (1) problem, and that its general solution is
available, can remove the aforementioned ambiguities and reduce the
labor of stage (2). In the case of the nonequilibrium steady state,
stage (2) can be dispensed with entirely if stage (1) has been properly
treated.

In the following Section we survey previous methods of transport theory
related to our work, and in Sec. 3 the generalization of Gibbs'
algorithm is given. The special case of dynamical perturbations is
discussed briefly in Sec. 4, while Sec. 5 is a mathematical digression
to collect the basic formulas needed for applications. In Sections 6, 7
the general prediction formulas are obtained in linear approximation and
the relation to the Wiener prediction theory established. Sections 8, 9,
10 apply the resulting theory to the problems of diffusion, thermal
conductivity, and ultrasonic attentuation; and in the final Sec. 11
nonlinear problems are discussed. A number of points essential for
understanding of the theory, but not needed for the actual
manipulations, are relegated to Appendices.
## 2. BACKGROUND OF THE PROBLEM
Because of the great diversity of possible nonequilibrium states, a full
microscopic theory seems[^1] at first glance hopelessly complicated; yet
from an experimental standpoint irreversible processes are basically
simple, in the sense that controlling only a few macroscopic quantities
suffices to determine a reproducible outcome. Thus, most of the
microscopic details must be irrelevant for the predictions of interest,
and with proper understanding we should be able to eliminate them
mathematically.

An important clue as to the manner in which one separates relevant and
irrelevant details was provided in the work of Kirkwood,[^4] in which
diffusion coefficients were shown to depend only on the correlation
function of forces acting on a particle. Kirkwood's final formulas are
very similar to those now believed to be exact, but the mathematical
technique used would be difficult to generalize. Furthermore, it made it
appear that a certain time-averaging operation is necessary in order to
obtain dissipative effects, but by this process one loses certain
observable high-frequency effects that clearly must be retained in a
general theory.

A decisive step in the direction of simplicity and generality was made
by Callen and co-workers in a series of articles[^5][^6][^7][^8] in which
the problem was attacked from both the microscopic and macroscopic
standpoints. Generalizing the well-known theorem by Nyquist[^9] on
electrical noise, they showed that linear responses of a system
initially in thermal equilibrium depend on microscopic details only
through the coupled equilibrium fluctuations of the macroscopic
quantities involved. Callen and Welton[^5] conjectured that the theory
of linear irreversible processes in general could be approached via
study of equilibrium fluctuations. Developments in the field since then,
particularly those of Green,[^10] Mori,[^11] Kubo,[^12] and their
co-workers, represent a series of confirmations of this idea. Bernard
and Callen[^13] showed that the case of nonlinear response of a driven
system can also be reduced to the theory of higher moments of
equilibrium fluctuations. The present paper may be regarded as still
another confirmation of Callen and Welton's prediction, in which we
extend the theory to nonequilibrium states whose representative
ensembles are not the result of any dynamical perturbation starting from
equilibrium.

In previous transport theories of the aforementioned types,
dissipative-irreversible effects did not appear in the ensemble
initially set up. For example, a system of N particles of mass m,
distributed with macroscopic density $\rho(x)$, local temperature T(x),
is often described in classical theory by an N-particle distribution
function, or Liouville function, of the form:
$$
W_N(x_1, p_1 \dots x_N, p_N) = \prod_{i=1}^{N} \frac{\rho(x_i)}{Nm} [2 \pi m k T(x_i)]^{-3/2} \exp \left\{ - \frac{p_i^2}{2mkT(x_i)} \right\} \tag{2.1}
$$

But, although this distribution represents nonvanishing density and
temperature gradients $\nabla \rho$, $\nabla T$, the diffusion current
or heat flow computed from (2.1) is zero.

Likewise, in quantum theory such a physical situation has been
described[^11] by the "local equilibrium", or "frozen-state" density
matrix:
$$
\rho_f = \frac{1}{Z} \exp \left\{ -\int d^3x \beta(x) [H(x) - \mu(x)n(x)] \right\} \tag{2.2}
$$
where $H(x)$, $n(x)$ are the Hamiltonian density and number density
operators. Again, although (2.2) describes gradients of temperature,
concentration, and chemical potential, the fluxes computed from (2.2)
are zero.

Mathematically, it was found that dissipative effects appear in the
equations only after one has carried out the following operations: (a)
approximate forward integration of the equations of motion for a short
"induction time", and (b) time smoothing or other coarse-graining of
distribution functions or Heisenberg operators.

Physically, it has always been somewhat of a mystery why either of these
operations is needed; for one can argue that, in most experimentally
realizable cases, dissipative effects (A) are already "in progress" at
the time the experiment is started, and (B) take place slowly, so that
the low-order distribution functions and expectation values of
measurable quantities must already be slowly-varying functions of time
and position; and thus not affected by coarse-graining. In cases where
this is not true, coarse-graining would result in loss of the physical
effects of interest. This point is discussed further in Appendix B.
It appears, therefore, that the real nature of the forward integration
and coarse-graining operations has not yet been explained; in a
correctly formulated theory neither should be required. We are led to
suspect the choice of initial ensemble; i.e. that ensembles such as
(2.1) and (2.2) do not fully describe the conditions under which
irreversible phenomena are observed, and therefore do not represent the
correct solution of the stage (1) problem. [We note that (2.1) and
(2.2) have never been "derived" from anything more fundamental; they
have been written down intuitively, by analogy with the grand canonical
ensemble of equilibrium theory]. The forward integration and
coarse-graining operations would, on this view, be regarded as
corrective measures which in some way compensate for the error in the
initial ensemble.

This conclusion is in agreement with that of Mori, Oppenheim, and
Ross[^14] (hereafter denoted MOR), who have provided a useful review of
this field. These authors never claimed that $\rho_t$ in (2.2) was the
correct density matrix, but supposed that it differed by only a small
amount from another matrix $\rho(t)$, which they designate as the
"actual distribution". They further supposed that after a short
induction time, $\rho_t$ relaxes into $\rho(t)$, which would explain the
need for forward integration. Some such relaxation undoubtedly takes
place in the low-order distribution functions derived from $\rho$, as
was first suggested by Bogoliubov[^15] for the analogous classical
problem. However, this is not possible for the full "global" density
matrix; if $\rho_t$ and $\rho(t)$ differ at t = 0 and undergo the same
unitary transformation in their time development, they cannot be equal
at any other time. Furthermore, $\rho(t)$ was never uniquely defined;
given two different candidates $\rho_1(t)$, $\rho_2(t)$ for this role,
MOR give no criterion by which one could decide which is indeed the
"actual" distribution.

For reasons explained in Appendix A, we believe that such criteria do
not exist; i.e.; that the notion of an "actual distribution" is
illusory, the result of a persistent semantic confusion that has long
plagued statistical mechanics. In the following section we approach the
problem in a different way, which yields a definite procedure for
constructing a density matrix which is to replace $\rho_t$, and will
play approximately the same role in our theory as the $\rho(t)$ of MOR.
## 3. THE GIBBS ALGORITHM
If the above reasoning is correct, a re-examination of the procedures by
which ensembles are set up in statistical mechanics is indicated. If we
can find an algorithm for constructing density matrices which fully
describe nonequilibrium conditions, we should find that transport and
other dissipative effects are obtainable by direct quadratures over the
initial ensemble.

This algorithm, we suggest, was given already by Gibbs.[^16] The great
power and generality of the methods he introduced have not yet been
appreciated; until recently it was scarcely possible to understand the
process by which he constructed his ensembles. This was (*loc. cit.*, p.
143) to assign that probability distribution which, while agreeing with
what is known, "gives the least value of the average index of
probability of phase," or as we would describe it today, *maximizes the
entropy*. This process led Gibbs to his canonical ensemble for
describing closed systems in thermal equilibrium, the grand canonical
ensemble for open systems, and (*loc. cit.*, p. 38), an ensemble to
represent a system rotating at angular velocity $\omega$, in which the
probability density is proportional to
$$
\exp [-\beta(H - \omega \cdot M)] \tag{3.1}
$$
where H, M are the
phase functions representing Hamiltonian and total angular momentum.
A few years later, the Ehrenfests[^17] dismissed these ensembles as mere
"analytical tricks", devoid of any real significance, and stressed the
physical superiority of Boltzmann's methods, thereby initiating a school
of thought in statistical mechanics which persists to this day. The
mathematical superiority of the canonical and grand canonical ensembles
for calculating equilibrium properties has since become firmly
established. Furthermore, although Gibbs gave no applications of the
rotational ensemble (3.1), it has been shown recently[^18] that this
ensemble provides a straightforward method of calculating the
gyromagnetic effects of Barnett and Einstein-de Haas. At the present
time, therefore, the Gibbs methods stand in a position of proven success
in applications, independent of all the conceptual problems regarding
their justification, which are still being debated. As a result,
Statistical Mechanics has taken on a peculiar hybrid character, in which
the practical calculations are always based on the methods of Gibbs,
while the pedagogy has tended to concentrate instead on ergodic
theory.[^19]

The recent development of Information Theory[^20] has made it possible to
see the method of Gibbs as a general procedure for inductive reasoning,
independent of ergodic theory or any other physical hypotheses, and
whose range of validity is therefore not restricted to equilibrium
problems; or indeed to physics. The significance of the principle of
maximum entropy, in the light of Information Theory, has been described
in detail elsewhere[^21][^22] and applications to statistical problems
outside of physics have been sketched.[^23] In the following we show
that this principle is sufficient to construct ensembles representing a
wide variety of non-equilibrium conditions, and that these new ensembles
yield transport coefficients by direct quadratures.

The general rule for constructing ensembles is as follows. The available
information about the state of a system consists of results of various
macroscopic measurements. Let the quantities measured be represented by
the operators $F_1, F_2, \dots, F_m$. The results of the measurements
are, of course, simply a set of numbers: $\{f_1, \dots, f_m\}$ which
makes no reference to any probability distribution. The ensemble is then
a mental construct which we invent in order to describe the range of
possible microscopic states, compatible with the measured values of the
$F_k$.

If we say that a density matrix $\rho$ "contains" certain information,
we mean by this that, if we communicate the density matrix to another
person he must be able, by applying the usual procedure of stage (3)
above, to recover this information from it. Thus we say that the density
matrix "agrees" with the given information if and only if it is
adjusted to yield expectation values equal to the measured numbers:
$$
f_k = \text{Tr}(\rho F_k) = \langle F_k \rangle, \quad k=1, \dots, m \tag{3.2}
$$
and in order to ensure that the density matrix describes the full range
of possible microscopic states compatible with (3.2), and not just some
arbitrary subset of them (in other words, that it describes only the
information given, and contains no hidden arbitrary assumptions about
the microscopic state), we demand that, while satisfying the constraints
(3.2), it shall maximize the quantity
$$
S_I = -\text{Tr}(\rho \log \rho). \tag{3.3}
$$

A great deal of confusion has resulted from the fact that, for three
decades, the single word "entropy" has been used interchangeably to
stand for either the quantity (3.3), or the quantity measured
experimentally (in the case of closed systems) by the integral of dQ/T
over a reversible path. We will try to maintain a clear distinction here
by referring to $S_I$ as the "information entropy" and denoting the
experimentally measured entropy by $S_E$. These quantities are different
in general; in the equilibrium case (which is the only one for which
$S_E$ is defined in conventional thermodynamics) the relation between
them has been shown[^22] to be: for all density matrices $\rho$ which
agree with the macroscopic information that defines the thermodynamic
state,
$$
kS_I \le S_E \tag{3.4}
$$
where k is Boltzmann's constant, with
equality in (3.4) if and only if $S_I$ is computed from the canonical
density matrix[^24]
$$
\rho = \frac{1}{Z(\lambda_1 \dots \lambda_m)} \exp{[\lambda_1 F_1 + \dots + \lambda_m F_m]} \tag{3.5}
$$
where the $\lambda_k$ are unspecified real constants, and for
normalization ($\text{Tr} \, \rho=1$) we have
$$
Z(\lambda_1 \dots \lambda_m) = \text{Tr} \exp{[\lambda_1 F_1 + \dots + \lambda_m F_m]} \tag{3.6}
$$
which quantity will be called the partition function. It remains only to
choose the $\lambda_k$ [which appear as Lagrange multipliers in the
derivation of (3.5) from a variational principle] so that (3.2) is
satisfied. This is the case if
$$
f_k = \langle F_k \rangle = \frac{\partial}{\partial \lambda_k} \log Z, \quad k=1,2,\dots,m \tag{3.7}
$$

These relations are just sufficient to determine all the unknowns
$\lambda_k$ in terms of the given data $\{f_1 \dots f_m\}$; indeed, we
can solve (3.7) explicitly for the $\lambda_k$ as follows. The maximum
attainable value of $S_I$ is, from (3.5), (3.6),
$$
(S_I)_{\max} = \log Z - \sum_{k=1}^m \lambda_k \langle F_k \rangle \tag{3.8}
$$

If this quantity is expressed as a function of the given data,
$S(f_1 \dots f_m)$, it is easily shown[^22][^24] from the above relations
that
$$
\lambda_k = -\frac{\partial S}{\partial f_k} \tag{3.9}
$$

A number of other general formal properties of maximum-entropy distributions are
listed elsewhere[^22] and it has been shown[^22][^25] that the second law
of thermodynamics is a simple consequence of the inequality (3.4) and
the dynamical invariance of $S_I$.

Further mathematical details concerning the process of entropy
maximization have been given by von Neumann,[^26] Wichmann,[^27] and
Wannier.[^28] In Appendix C, we point out an important property of the
maximum entropy ensemble, which is helpful in gaining an intuitive
understanding of this theory. Given any density matrix $\rho$ and any
$\epsilon$ in $0 < \epsilon < 1$, there is defined a "high-probability
manifold" (HPM) of finite dimensionality $W(\epsilon)$, consisting of
all state vectors to which $\rho$ assigns an "array probability" as
defined in Ref. 21b, Sec. 7, greater than a certain amount
$\delta(\epsilon)$, and such that the eigenvectors of $\rho$ spanning
the complementary manifold have total probability less than $\epsilon$.
As $\epsilon$ varies, any density matrix $\rho$ thus defines a nested
sequence of HPM's. For a macroscopic system, the information entropy
$S_I$ may be identified with $\log W(\epsilon)$ in the following sense: if
N is the number of particles in the system, then as $N \to \infty$
with the intensive parameters held constant, $N^{-1}S_I$ and
$N^{-1}\log W(\epsilon)$ approach the same limit independently of
$\epsilon$. This is a form of the asymptotic equipartition theorem[^20]
of Information Theory. The process of entropy maximization therefore
amounts, for all practical purposes, to the same thing as finding the
density matrix which, while agreeing with the available information,
defines the largest possible HPM; this is the basis of the remark
following (3.2). An analogous result holds in classical theory[^25] in
which $W(\epsilon)$ becomes the phase volume of the "high-probability
region" of phase space, as defined by the N-particle distribution
function.

The above procedure is sufficient to construct the density matrix
representing equilibrium conditions, provided the quantities $F_k$ are
chosen to be constants of the motion. The extension to nonequilibrium
cases, and to equilibrium problems in which we wish to incorporate
information about quantities which are not intrinsic constants of the
motion (such as stress or magnetization[^22]) requires mathematical
generalization which we give in two steps.

It is a common experience that the course of a physical process does not
in general depend only on the present values of the observed macroscopic
quantities; it depends also on the past history of the system. The
phenomenon of spin echoes[^29] is a particularly striking example of
this. Correspondingly, we must expect that, if the $F_k$ are not
constants of the motion, an ensemble constructed as above using only the
present values of the $\langle F_k \rangle$ will not in general suffice
to predict either equilibrium or nonequilibrium behavior. As we will see
presently, it is just this fact which causes the error in the "frozen
state" density matrix $\rho_t$ of Eq. (2.2).

In order to describe time variations, we extend the $F_k$ to the
Heisenberg operators
$$
F_k(t) = U^{-1}(t) F_k(0) U(t) \tag{3.10}
$$
in which the time-development matrix $U(t)$ is the solution of the
Schrödinger equation
$$
i\hbar \dot{U}(t) = H(t) U(t) \tag{3.11}
$$
with initial conditions $U(0)=1$, and H(t) is the Hamiltonian. If we are
given values of the $\langle F_k(t_i) \rangle$ at various times $t_i$,
then each of these data must be considered a separate piece of
information, to be given its Lagrange multiplier $\lambda_{ki}$ and
included in the sum of (3.5). In the limit where we imagine information
given over a continuous time interval, $-\tau < t < 0$, the summation
over the time index i becomes an integration and the canonical density
matrix (3.5) becomes
$$
\rho = \frac{1}{Z} \exp \left\{ \sum_{k=1}^m \int_{-\tau}^0 \lambda_k(t) F_k(t) dt \right\} \tag{3.12}
$$
where the partition function has been generalized to a partition
functional
$$
Z[\lambda_1(t)\dots\lambda_m(t)] = \text{Tr} \exp \left\{ \sum_{k=1}^m \int_{-\tau}^0 \lambda_k(t) F_k(t) dt \right\} \tag{3.13}
$$
and the unknown Lagrange multiplier functions $\lambda_k(t)$ are
determined from the condition that the density matrix agree with the
given data $\langle F_k(t) \rangle$ over the "information-gathering"
time interval:
$$
\langle F_k(t) \rangle = \text{Tr}[\rho F_k(t)] = f_k(t), \quad -\tau \le t \le 0. \tag{3.14}
$$

By the perturbation methods developed in Sec. 5 below, we find that
(3.14) reduces to the natural generalization of (3.7):
$$
\langle F_k(t) \rangle = \frac{\delta}{\delta \lambda_k(t)} \log Z, \quad -\tau \le t \le 0. \tag{3.15}
$$
where $\delta$ denotes the functional derivative.

Finally, if the operators $F_k$ depend on position as well as time, as
in (2.2), Eq. (3.10) is changed to
$$
F_k(x,t) = U^{-1}(t) F_k(x,0) U(t) \tag{3.16}
$$
and the values of these
quantities at each point of space and time now constitute the
independent pieces of information, which are coupled into the density
matrix via the Lagrange multiplier function
$\lambda_k(x,t)$. If we are given information about $F_k(x,t)$
throughout a space-time region $R_k$ (which can be different for
different quantities $F_k$), the ensemble which incorporates all this
information, while locating the largest possible HPM, is
$$
\rho = \frac{1}{Z} \exp \left\{ \sum_k \int_{R_k} dt \, d^3x \, \lambda_k(x,t) F_k(x,t) \right\} \tag{3.17}
$$
with the partition functional
$$
Z = \text{Tr} \exp \left\{ \sum_k \int_{R_k} dt \, d^3x \, \lambda_k(x,t) F_k(x,t) \right\} \tag{3.18}
$$
and the $\lambda_k(x,t)$ determined from
$$
\langle F_k(x,t) \rangle = \frac{\delta}{\delta \lambda_k(x,t)} \log Z, \quad (x,t) \text{ in } R_k \tag{3.19}
$$

Prediction of any quantity J(x,t) is then accomplished by calculating
$$
\langle J(x,t) \rangle = \text{Tr}[\rho J(x,t)] \tag{3.20}
$$

In equations (3.17) - (3.20) we have the general algorithm for
calculating irreversible processes. We emphasize that the basic physical
and conceptual formulation of the theory is complete at this point; what
follows represents only the working out of some mathematical
consequences of this algorithm. A simple example of an exactly soluble
problem using these relations, is given in Appendix D.

The form of equations (3.17) - (3.20) makes it appear at first glance
that stages (1) and (2), discussed in the Introduction, are now fused
into a single stage. However, this is only a consequence of our using
the Heisenberg representation. According to the usual conventions, the
Schrödinger and Heisenberg representations coincide at time t = 0; thus
we may regard the steps (3.17) - (3.19) equally well as determining the
density matrix $\rho(0)$ in the Schrödinger representation; i.e. as
solving the stage (1) problem. If, having found this initial ensemble,
we switch to the Schrödinger representation, Eq. (3.20) is then replaced
by
$$
\langle J(x) \rangle_t = \text{Tr}[J(x) \rho(t)] \tag{3.21}
$$
in which the problem of stage (2) now appears explicitly as that of finding
the time-evolution of $\rho(t)$. The form (3.21) will be more convenient
if a number of different quantities $J_1, J_2, \dots$ are to be
predicted.

Evidently, our arguments leading to the rule (3.17), (3.19) for
converting experimental measurements into a density matrix can be
further refined by applying the quantum-mechanical theory of
measurement. We have not done this, for several reasons. In the first
place, the theory of measurement is itself being subjected to renewed
scrutiny,[^30] and fundamental modifications appear likely as a result.
Secondly, the formalism here presented is capable of other
interpretations which give it a meaning independent of the theory of
measurement. Questions concerning predictions made by ensembles which
have maximum phase volume for prescribed expectation values are
mathematically well-posed and physically interesting in their own right.
Finally, it will appear that the above formalism already yields the
results of usual practical interest without these further elaborations.
## 4. DYNAMICAL PERTURBATIONS
If the irreversible process is the result of a dynamical perturbation on
what would otherwise be an equilibrium condition -- in other words,
where it is caused entirely by an explicitly given term V(t) in the
Hamiltonian -- the above equations reduce to a familiar form. If we
remain in the full Heisenberg representation, Eq. (3.20), then if the
available information concerning the state of the system consists solely
of the fact that it was in thermal equilibrium in the remote past, the
density matrix (3.17) remains the equilibrium one for all time. The full
content of the theory then resides in (3.20).

Suppressing the coordinate x for brevity, the Heisenberg operator J(t)
is found by a perturbation expansion of (3.10). If V(t) = Qv(t), where
Q is an operator and v(t) a specified numerical function, the
first-order effect is given by
$$
\langle J(t) \rangle - \langle J(-\infty) \rangle = \int_{-\infty}^t \varphi_{JQ}(t-t^\prime) v(t^\prime) dt^\prime \tag{4.1}
$$
where $\langle J(-\infty) \rangle$ is the thermal equilibrium value, and
$$
\varphi_{JQ}(t-t^\prime) \equiv \frac{1}{i\hbar} \langle [Q^0(t^\prime), J^0(t)] \rangle \tag{4.2}
$$
is the impulse-response function, or "aftereffect function" described
by Kubo,[^12] and by Bernard and Callen,[^13] who also give higher order
nonlinear terms. The superscripts in (4.2) denote time development
according to the unperturbed Hamiltonian $H_0$.

This aspect of the theory, which is adequate to treat such problems as
magnetic resonance line shape and electrical conductivity, has already
been developed by many authors[^31] into an elegant, and undoubtedly
final, form. Among specific calculations based on it, one may note the
treatments of normal metal conductivity by Langer,[^32] and the Meissner
effect by Mattis and Bardeen[^33] and Nambu.[^34]

The case of non-dynamical perturbations, such as temperature or
concentration gradients, or shearing stress of a fluid is, as already
noted, fundamentally different and presents peculiar difficulties both
mathematical and conceptual. In some cases, as Feynman and
Montroll[^35] have shown, one can use physical reasoning to restore the
appearance of a dynamical problem by inventing a fictitious "effective
Hamiltonian" $H_e(t)$ which would, if present, produce a similar
nonequilibrium state starting from equilibrium; or as Luttinger[^3] has
shown, one can find the equilibrium distribution under the action of a
fictitious force field and use "balancing" arguments based on such
relations as the Einstein equation connecting diffusion coefficient and
mobility. However, these are clearly artificial devices, and there seems
to be no general, unique prescription for finding $H_e$ (see, however,
Appendix E, in which we show that under certain conditions a 1:1
correspondence can be set up between statistical problems of the present
theory and a class of fictitious dynamical problems). Most writers on
transport theory have recognized that existing treatments of diffusion,
thermal conductivity, and viscosity are not fully satisfactory for this
reason. This has been stressed particularly in the recent review article
of Chester,[^2] who gives many more details and references, and
concludes that "--- it would be very satisfying to have a quite
different approach to these problems".

The above algorithm evidently provides one such approach; to investigate
its suitability we note that the aforementioned problems all involved
near-equilibrium conditions, and so in treating them by (3.17) - (3.20)
we can make the corresponding approximation. In the following section we
collect the basic perturbation formulas needed for this.
## 5. PERTURBATION THEORY FOR EXPECTATION VALUES
We denote an "unperturbed" density matrix $\rho_0$, by
$$
\rho_0 = \frac{e^A}{Z_0}, \quad Z_0 = \text{Tr}(e^A), \tag{5.1}
$$
 a
"perturbed" one by
$$
\rho = \frac{e^{A+\epsilon B}}{Z}, \quad Z = \text{Tr}(e^{A+\epsilon B}), \tag{5.2}
$$
where A, B are Hermitian. The expectation values of any operator C over
these ensembles are respectively
$$
\langle C \rangle_0 = \text{Tr}(\rho_0 C), \quad \langle C \rangle = \text{Tr}(\rho C) \tag{5.3}
$$

The expansion of $\langle C \rangle$ to all orders in $\epsilon$ has
been derived in Ref. 18, Appendix B. The n'th order contribution is the
covariance, in the unperturbed ensemble, of C with an operator $Q_n$:
$$
\langle C \rangle - \langle C \rangle_0 = \sum_{n=1}^\infty \epsilon^n [\langle Q_n C \rangle_0 - \langle Q_n \rangle_0 \langle C \rangle_0] \tag{5.4}
$$

Here, $Q_n$ is defined by $Q_1 \equiv S_1$, and
$$
Q_n = S_n - \sum_{k=1}^{n-1} \langle Q_k \rangle_0 S_{n-k}, \quad n>1. \tag{5.5}
$$
in which $S_n$ are the operators appearing in the well-known expansion
$$
e^{A+\epsilon B} = e^A \left[1 + \sum_{n=1}^\infty \epsilon^n S_n \right] \tag{5.6}
$$

More explicitly,
$$
S_n = \int_0^1 dx_1 \int_0^{x_1} dx_2 \dots \int_0^{x_{n-1}} dx_n \, B(x_1) \dots B(x_n) \tag{5.7}
$$
where
$$
B(x) \equiv e^{-xA} B e^{xA} \tag{5.8}
$$

The first-order term is
$$
\langle C \rangle - \langle C \rangle_0 = \epsilon \int_0^1 dx [\langle e^{-xA} B e^{xA} C \rangle_0 - \langle B \rangle_0 \langle C \rangle_0] \tag{5.9}
$$
and it will appear below that all relations of linear transport theory
are special cases of (5.9).

For a more condensed notation, define the average of any operator B over
the sequence of similarity transformations as
$$
\bar{B} = \int_0^1 dx \, e^{-xA} B e^{xA} \tag{5.10}
$$
which we will call the Kubo transform of B. Then (5.9) becomes
$$
\langle C \rangle - \langle C \rangle_0 = \epsilon K_{CB} \tag{5.11}
$$
 in
which, for various choices of C, B, the quantities
$$
K_{CB} = \langle \bar{B} C \rangle_0 - \langle \bar{B} \rangle_0 \langle C \rangle_0 \tag{5.12}
$$
are the basic covariance functions of the linear theory.

We list a few useful properties of these quantities; in all cases, the
result is easily proved by writing out the expressions in the
representation where A is diagonal. Let F, G be any two operators; then
$$
\langle \bar{F} \rangle_0 = \langle F \rangle_0 \tag{5.13}
$$
$$
K_{FG} = K_{GF} \tag{5.14}
$$

If F, G, are Hermitian, then 
$$
K_{FG} \text{ is real, } K_{FF} \ge 0 \tag{5.15}
$$

If $\rho_0$ is a projection operator representing a pure state, then
$K_{FG}=0$. If $\rho_0$ is not a pure state density matrix, then with
Hermitian F, G,
$$
K_{FF}K_{GG} - K_{FG}^2 \ge 0 \tag{5.16}
$$
with equality if and only if F = qG, where q is a real number. If G is of the
form
$$
G(u) = e^{-uA} G(0) e^{uA} \tag{5.17}
$$
then
$$
\frac{d}{du} K_{FG} = \langle [F,G] \rangle_0 \tag{5.18}
$$
## 6. APPLICATION TO NEAR-EQUILIBRIUM ENSEMBLES
A closed system in thermal equilibrium is described, as usual, by the
density matrix
$$
\rho_0 = \frac{e^{-\beta H}}{Z_0(\beta)} = \frac{e^{-\beta H}}{\text{Tr}(e^{-\beta H})} \tag{6.1}
$$
which maximizes $S_I$ for prescribed $\langle H \rangle$, and is a very
special case of (3.17). The thermal equilibrium prediction for any
quantity F is, as usual,
$$
\langle F \rangle_0 = \text{Tr}(\rho_0 F) \tag{6.2}
$$

But suppose we are now given the value of $\langle F(t) \rangle$
throughout the "information-gathering" interval $-\tau < t < 0$. The
ensemble which includes this new information in addition to information
about $\langle H \rangle$ as in (6.1) is of the form (3.17), which now
maximizes $S_I$ for prescribed $\langle H \rangle$ and
$\langle F(t) \rangle$ in $-\tau < t < 0$. It corresponds to the
partition functional
$$
Z[\beta, \lambda(t)] = \text{Tr} \exp \left[ -\beta H + \int_{-\tau}^0 \lambda(t)F(t) dt \right] \tag{6.3}
$$
which is a special case of (3.13). If, during the information-gathering
interval, this new information was simply
$\langle F(t) \rangle = \langle F \rangle_0$, it is easily shown from
(3.15) that we have identically (see Appendix D for an explicit example)
$$
\int_{-\tau}^0 \lambda(t) F(t) dt = 0 \tag{6.4}
$$

In words: if the new information is redundant (in the sense that it is
only what we would have predicted from the old information), then it
will drop out of the equations and the ensemble is unchanged. As shown
in Appendix F, this is a general property of the formalism here
presented. In applications this means that there is never any need, when
setting up an ensemble, to ascertain whether the different pieces of
information used are independent; any redundant parts will cancel out
automatically.

If, therefore, we treat the integral in (6.3) as a small perturbation,
we are expanding in powers of the departure from equilibrium. For
validity of the perturbation scheme it is not necessary that
$\lambda(t)F(t)$ be everywhere small; it is sufficient if the integral
is small. First-order effects in the departure from equilibrium, such as
linear diffusion or heat flow, are then predicted using the general
formula (5.9), with the choices $A = -\beta H$, and
$$
B = \int_{-\tau}^0 \lambda(t) F(t) dt \tag{6.5}
$$

With constant H, the
Heisenberg operator F(t) reduces to
$$
F(t) = \exp(iHt/\hbar) F(0) \exp(-iHt/\hbar) \tag{6.6}
$$
and its Kubo
transform (5.10) becomes
$$
\bar{F}(t) = \frac{1}{\beta} \int_0^\beta du \, F(t-i\hbar u), \tag{6.7}
$$
the characteristic quantity of the Kubo[^12] theory.

In the notation of (5.11), the first-order expectation value of any
quantity C(t) will then be given by
$$
\langle C(t) \rangle - \langle C \rangle_0 = \int_{-\tau}^0 K_{CF}(t,t^\prime) \lambda(t^\prime) dt^\prime \tag{6.8}
$$
where $K_{CF}$ is now indicated as a function of the parameters t, t'
contained in the operators:
$$
K_{CF}(t,t^\prime) = \langle \bar{F}(t^\prime) C(t) \rangle_0 - \langle F \rangle_0 \langle C \rangle_0 \tag{6.9}
$$

Remembering that the parameters t,t' are part of the operators C, F, the
general reciprocity law (5.14) now becomes
$$
K_{CF}(t,t^\prime) = K_{FC}(t^\prime,t) \tag{6.10}
$$

When H is constant, it follows also from (6.6) that
$$
K_{CF}(t,t^\prime) = K_{CF}(t-t^\prime) \tag{6.11}
$$

More generally, take the unperturbed ensemble as the grand canonical
distribution (3.1) corresponding to the choice
$$
A = -\beta[H - \mu_1 N_1 - \dots - \mu_r N_r] \tag{6.12}
$$
where
$$
\mathcal{H} = \int d^3x \, H(x) \tag{6.13}
$$
$$
N_i = \int d^3x \, n_i(x) \tag{6.14}
$$
are the total Hamiltonian, and
number operator for the i'th type of particle, and H(x), $n_i(x)$ the
corresponding density operators. If $\sum \mu_i N_i$ commutes with H and
F(t), then (6.7) remains valid; otherwise the Kubo transforms
$\bar{F}(t)$ must be defined by (5.10).

In the unperturbed (equilibrium) ensemble, expectation values are
independent of time, so for any operator J(x,t) we have
$$
\langle J(x,t) \rangle_0 = \langle J(x) \rangle_0 \tag{6.15}
$$

Often, this will be independent of x also. Now suppose we are given additional
information consisting of the expectation values of several functions of
position and time $F_k(x,t)$ [which may include the above operators H(x)
and $N_i(x)$] throughout the space-time regions $R_k$ of (3.17). The new
ensemble is of the form (5.2) with the choice
$$
\epsilon B = \sum_{k=1}^m \int_{R_k} dt \, d^3x \, \lambda_k(x,t) F_k(x,t) \tag{6.16}
$$
which is a small perturbation if the given $\langle F_k(x,t) \rangle$
are not appreciably different from their equilibrium values
$\langle F_k(x) \rangle_0$. In this new ensemble, the predicted value of
any quantity J(x,t) is given by another special case of (5.11):
$$
\langle J(x,t) \rangle - \langle J(x) \rangle_0 = \sum_{k=1}^m \int_{R_k} d^3x^\prime dt^\prime K_{JF_k}(x,t;x^\prime,t^\prime) \lambda_k(x^\prime,t^\prime) \tag{6.17}
$$
with
$$
K_{JF_k}(x,t;x^\prime,t^\prime) = \langle \bar{F}_k(x^\prime,t^\prime) J(x,t) \rangle_0 - \langle F_k(x^\prime) \rangle_0 \langle J(x) \rangle_0 \tag{6.18}
$$

From (6.17) the nonlocal character of the theory is apparent. The
problem of predicting effects of first order in the departure from
equilibrium is now reduced to that of finding the Lagrange multiplier
functions $\lambda_k(x,t)$ from (3.19). This problem is treated, in the
linear approximation, in the following section.
**[TRUNCATED: The original paper and PDF both end at this point. Sections 7 through 11 and Appendices A-F are missing.]**
## REFERENCES
[^1]: N. G. van Kampen, *Physica* 20, 603 (1954).
[^2]: W. Chester, *Reports on Progress in Physics* 26, 411 (1963).
[^3]: J. M. Luttinger, *Phys. Rev.* (to be published).
[^4]: J. G. Kirkwood, *J. Chem. Phys.* 14, 180 (1946).
[^5]: H. B. Callen and T. A. Welton, *Phys. Rev.* 83, 34 (1951).
[^6]: H. B. Callen and R. F. Greene, *Phys. Rev.* 86, 702 (1952).
[^7]: R. F. Greene and H. B. Callen, *Phys. Rev.* 88, 1387 (1952).
[^8]: H. B. Callen, M. L. Barasch, and J. L. Jackson, *Phys. Rev.* 88, 1382 (1952).
[^9]: H. Nyquist, *Phys. Rev.* 32, 110 (1928).
[^10]: M. S. Green, *J. Chem. Phys.* 20, 1281 (1952); 22, 398 (1954).
[^11]: H. Mori, *Phys. Rev.* 112, 1829 (1958).
[^12]: R. Kubo, *J. Phys. Soc. Japan* 12, 570 (1957).
[^13]: W. Bernard and H. B. Callen, *Phys. Rev.* 118, 1466 (1960).
[^14]: H. Mori, I. Oppenheim, and J. Ross, in *Studies in Statistical Mechanics*, Vol. 1, p. 217, J. de Boer and G. E. Uhlenbeck, Editors, North-Holland Publishing Co., Amsterdam (1962).
[^15]: N. Bogoliubov, *Journal of Physics (USSR)* 10, 256, 265 (1946).
[^16]: J. W. Gibbs, *Elementary Principles in Statistical Mechanics*, Yale University Press, New Haven (1902).
[^17]: P. and T. Ehrenfest, *The Conceptual Foundations of the Statistical Approach in Mechanics*, Cornell University Press, Ithaca, N. Y. (1959). (Translation by M. J. Moravcsik of the *Encyk. d. Math. Wiss.* article, 1911).
[^18]: E. T. Jaynes, in *Coherence and Quantum Optics*, L. Mandel and E. Wolf, Editors, Plenum Publishing Corp., New York (1973); pp. 35-81.
[^19]: A. I. Khinchin, *Mathematical Foundations of Statistical Mechanics*, Dover Publications, Inc., New York (1949).
[^20]: C. E. Shannon, *Bell System Tech. J.* 27, 379, 623 (1948).
[^21]: E. T. Jaynes, *Phys. Rev.* 106, 620 (1957); 108, 171 (1957).
[^22]: E. T. Jaynes, in *Statistical Physics*, Brandeis Summer Institute 1962 Lectures, Vol. 3, K. W. Ford, Editor, W. A. Benjamin, Inc., New York (1963).
[^23]: E. T. Jaynes, *Probability Theory in Science and Engineering*, Socony-Mobil Oil Co., Dallas, Texas (1958).
[^24]: E. T. Jaynes, *Information Theory and Statistical Mechanics*, course of lectures delivered at the Brandeis Summer Institute, 1962 (to be published).
[^25]: E. T. Jaynes, *Information Theory and Statistical Mechanics II*, *Phys. Rev.* (submitted).
[^26]: J. von Neumann, *Mathematical Foundations of Quantum Mechanics*, Princeton University Press, Princeton, N. J. (1955).
[^27]: E. H. Wichmann, *J. Math. Phys.* 4, 884 (1963).
[^28]: G. H. Wannier, *Statistical Physics*, John Wiley & Sons, Inc., New York (1966).
[^29]: E. L. Hahn, *Phys. Rev.* 80, 580 (1950).
[^30]: E. P. Wigner, *Am. J. Phys.* 31, 6 (1963).
[^31]: R. Kubo, in *Lectures in Theoretical Physics*, Vol. 1, p. 120, W. E. Brittin and L. G. Dunham, Editors, Interscience Publishers, Inc., New York (1959).
[^32]: J. S. Langer, *Phys. Rev.* 127, 5 (1962).
[^33]: D. C. Mattis and J. Bardeen, *Phys. Rev.* 111, 412 (1958).
[^34]: Y. Nambu, *Phys. Rev.* 117, 648 (1960).
[^35]: R. P. Feynman and E. W. Montroll (unpublished).