---
title: "Some Aspects of Maser Theory"
year: 1958
abstract: >
  As a preliminary to a theoretical study of the ultimate limitations on
  noise figure and frequency stability in molecular-beam masers, we
  examine the relation between quantum electrodynamics and the
  semiclassical theory of radiation. Solutions according to both
  theories are worked out in detail for the case of a single molecule
  interacting with a single cavity oscillation mode. Comparison of the
  results shows several features which make the relation of the two
  theories appear rather different than is usually supposed. For
  example, according to quantum electrodynamics, even in the limit of
  aribrarily large photon occupation numbers, the electromagnetic field
  can be in physical states qualitatively different from any describable
  in classical terms, and a molecule-beam maser excited by molecules all
  in the upper state should produce such a condition.
  The molecular-beam maser provides an interesting example of the
  Einstein-Podolsky-Rosen paradox, arising from correlations in states
  of molecule and field. An attempt is made to find an experimental
  situation in which effects of such correlations are observable, but
  without success.
  It is shown that, contrary to what is often assumed, the semiclassical
  theory of radiation can account for spontaneous emission of radiation.
  It leads to a characteristic time just the same as provided by field
  quantization, when we take into account both the effect of the field
  on the molecule and the effect of the molecule on the field. The
  result is a system of coupled nonlinear equations whose solutions can
  be found in terms of elliptic functions. Even in the case of field
  intensities corresponding to one photon, this solution reproduces
  almost quantitatively the same laws of energy exchange as found in
  quantum electrodynamics. It is concluded that the semiclassical
  theory, as extended here, is a far more reliable means of calculating
  radiation processes than usually supposed.
author: ["E.T. Jaynes"]
categories: ["Electrodynamics & Signal Processing"]
tags: ["maser theory", "quantum electrodynamics", "semiclassical radiation theory", "spontaneous emission", "molecular-beam maser", "Einstein-Podolsky-Rosen paradox", "cavity modes"]
---
## INTRODUCTION
From a theoretical standpoint, maser amplifiers and oscillators offer
some of the most interesting problems in physics. There are few
situations where quantum theory and classical theory are combined so
closely in a single description. Furthermore, relations between the
semiclassical theory of radiation, quantum electrodynamics, and the
statistical mechanics of irreversible processes, are here exhibited in a
very simple model accessible to both calculation and experiment.

The work here reported (which will continue after termination of the
present contract) comprises the first stages of an attempt to treat
maser operation entirely in terms of quantum theory. Although it is
hoped that it will lead to useful results concerning noise figure and
frequency stability, the primary objective is a more complete
understanding of the theoretical relations mentioned above. Some of what
is said below applies to solid-state masers, but we have in mind
specifically the case of molecular-beam devices.

Numerous theoretical treatments of masers now exist, based on several
different types of approximations and assumptions, and new ones appear
almost every month. Broadly speaking, there are two different levels of
approximation used in theories published to date:
(A) The most common type of theory, but also the crudest, is the one
wherein the emission of radiation from molecules is considered to take
place via independent and instantaneous "quantum jumps," whose
probability of occurrence is proportional to the product of time of
interaction and energy density of the radiation at the transition
frequency. This is essentially an application of quantum theory as it
existed 40 years ago. It involves little that was not already given in
Einstein's famous paper of 1917, introducing the A and B coefficients.
Present quantum mechanics tells us that the notion of time-proportional
induced transition probabilities is only an approximation valid when the
correlation time of the radiation is short compared to the time required
to accumulate an appreciable transition probability; in other words, that
the radiation responsible for the transitions must be random, with a
spectrum wide compared to the line width. This condition is satisfied in
most optical experiments, but in an ammonia maser the correlation time of
the radiation may be of the order of $10^3$ to $10^6$ times the flight
time of a molecule through the cavity. Under these conditions, any
attempt to describe maser operation in terms of the standard transition
probability formulas, such as 
$$
W_{1 \to 2} = \frac{2\pi}{\hbar^2} |H_{12}|^2 g(\omega) \tag{1.1}
$$
 may lead to conclusions that are not only
quantitatively, but also qualitatively wrong. Unfortunately, most of the
existing noise figure calculations are based on a treatment of this type.
Of course, use of a poor approximation does not necessarily prevent one
from getting the right answer; but one can never be sure it is right until
the calculation has been checked in other ways.
(B) A second stage of approximation, resulting in a much more
realistic treatment, is represented by the theories of Basov and
Prokhorov, Lamb, and Feynman. This is based on the semiclassical theory
of radiation, in which, instead of using Eq. (1.1), one actually solves
the time-dependent Schrödinger equation for a molecule, as perturbed by
a classically described radiation field. The effect of the molecule on
the field is then assumed to be the same as the effect one would obtain
classically from a dipole whose moment is equal to the expectation value
of moment of the molecule. Such a treatment gives definite predictions
for saturation and frequency-pulling effects, but it is not obvious
whether even this approximation would lead to correct prediction of the
fluctuation effects involved in noise figure and frequency stability.
Theories of this type still involve many approximations, among which
are: (1) the molecules are ascribed independent wave functions, whereas
in principle one should always treat the entire system of molecules as a
single quantum-mechanical system, by a formalism like that of Dicke's
"superradiant gas." (2) In principle, one should also quantize the
radiation field and consider the problem as one of quantum
electrodynamics.

It is generally thought that the semiclassical approach should be quite
adequate for any effects at microwave frequencies, by virtue of the
smallness of the Einstein A coefficients relative to the B coefficients.
However, the relation between semiclassical theory and quantum
electrodynamics is not a simple one. Quantization of the radiation field
introduces many changes in addition to the appearance of A coefficients.
In particular, it leads to the possibility that the electromagnetic
field may be in physical states qualitatively different from any that
can be described in classical terms, even in the limit of arbitrarily
high photon occupation numbers per field normal mode. Such states will
be shown, in the calculations to follow, to be the ones actually
produced in masers under certain idealized conditions.

We approach the theory of maser operation in several stages, starting
with simple special cases for which all details of the mathematics can
be worked out, then adding various features which tend in the direction
of more realistic models. The mathematical form of the theory is quite
similar to what one encounters in the statistical mechanics of
irreversible processes. Of particular interest will be the extent to
which the semiclassical theory is derivable from quantum
electrodynamics, and the effect of different statistical assumptions
concerning the initial states of the molecules.
## FIELD QUANTIZATION
We first develop the formalism of field quantization in a form suitable
for microwave applications. There is, of course, no need for elegant
covariant formulations here; the simple approach to electrodynamics
given by Fermi[^1] is quite adequate for our purposes. Also, the usual
plane wave expansion is not appropriate here, and in its place we need
to use the expansion of electromagnetic fields in terms of resonant
modes of the particular cavity under consideration. We use the cavity
normal mode functions as defined by Slater.[^2]

The cavity is represented by a volume V, bounded by a closed surface S.
Let $\mathbf{E}_a(\mathbf{x})$, $k_a^2 = (\omega_a^2/c^2)$ be the
eigenfunctions and eigenvalues of the boundary-value problem
$$
\nabla \times \nabla \times \mathbf{E} - k_a^2 \mathbf{E} = 0 \quad \text{in V,} \tag{2.1}
$$
$$
\mathbf{n} \times \mathbf{E} = 0 \quad \text{on S,} \tag{2.2}
$$
 where
$\mathbf{n}$ is a unit vector normal to S. The
$\mathbf{E}_a(\mathbf{x})$ are so normalized that
$$
\int_V (\mathbf{E}_a \cdot \mathbf{E}_b) dV = \delta_{ab}. \tag{2.3}
$$

 The
vector functions $\mathbf{H}_a(\mathbf{x})$, related to $\mathbf{E}_a$
by
$$
\nabla \times \mathbf{E}_a = k_a \mathbf{H}_a, \quad \nabla \times \mathbf{H}_a = k_a \mathbf{E}_a, \tag{2.4}
$$
are also orthonormal in V:
$$
\int_V (\mathbf{H}_a \cdot \mathbf{H}_b) dV = \delta_{ab}. \tag{2.5}
$$

 The
electric and magnetic fields can be expanded in the form
$$
\mathbf{E}(\mathbf{x},t) = - \sqrt{4\pi} \sum_a p_a(t) \mathbf{E}_a(\mathbf{x}), \tag{2.6}
$$
$$
\mathbf{H}(\mathbf{x},t) = \sqrt{4\pi} \sum_a \omega_a q_a(t) \mathbf{H}_a(\mathbf{x}). \tag{2.7}
$$

From these relations, we find for the total field energy
$$
\mathcal{H} = \int \frac{E^2 + H^2}{8\pi} dV = \frac{1}{2} \sum_a (p_a^2 + \omega_a^2 q_a^2), \tag{2.8}
$$
and the Maxwell equations,
$$
\nabla \times \mathbf{E} = -\frac{1}{c} \frac{\partial \mathbf{H}}{\partial t}, \tag{2.9}
$$
$$
\nabla \times \mathbf{H} = \frac{1}{c} \frac{\partial \mathbf{E}}{\partial t}, \tag{2.10}
$$
then reduce to the Hamiltonian equations of motion,
$$
\dot{q}_a = \frac{\partial \mathcal{H}}{\partial p_a} = p_a, \tag{2.11}
$$
$$
\dot{p}_a = -\frac{\partial \mathcal{H}}{\partial q_a} = -\omega_a^2 q_a, \tag{2.12}
$$
respectively.

On quantization of the field, the canonically conjugate coordinate and momenta satisfy the commutation rules
$$
[q_a, q_b] = [p_a, p_b] = 0, \quad [q_a, p_b] = i\hbar\delta_{ab}. \tag{2.13}
$$

 The
operators $c_a^*, c_a$ which create or annihilate a photon in the a'th
cavity mode are then
$$
c_a^* = \frac{p_a + i\omega_a q_a}{\sqrt{2\hbar\omega_a}}, \quad c_a = \frac{p_a - i\omega_a q_a}{\sqrt{2\hbar\omega_a}}, \tag{2.14}
$$
with the commutation rule 
$$
[c_a, c_b^*] = \delta_{ab}. \tag{2.15}
$$

 Denote by
$\Phi(n_1, n_2, \dots)$ the state vector of the field for which there
are $n_1$ quanta in mode 1, $n_2$ in mode 2, etc. The $c_a$ operators
have the properties
$$
\begin{aligned}
 c_a \Phi(\dots, n_a, \dots) &= \sqrt{n_a} \Phi(\dots, n_a-1, \dots) \\\\ c_a^* \Phi(\dots, n_a, \dots) &= \sqrt{n_a+1} \Phi(\dots, n_a+1, \dots),
\end{aligned} \tag{2.16}
$$
from which we easily verify (2.15), and obtain the matrix elements in
the $n_a$ representation:
$$
(n_a^\prime|c_a|n_a) = (n_a|c_a^*|n_a^\prime) = \sqrt{n_a+1} \delta(n_a^\prime, n_a+1). \tag{2.17}
$$

The Hamiltonian, with zero-point energy removed, then reduces to
$$
\mathcal{H} = \sum_a \hbar\omega_a c_a^* c_a = \sum_a \hbar\omega_a n_a. \tag{2.18}
$$

Finally we work out, for later purposes, the matrix elements of the
electric field in the case of a cylindrical cavity with only the lowest
TM mode excited. In this mode the only nonvanishing component of
$\mathbf{E}_a$ is $E_{az} = \text{(const.)} \times J_0(k_r r)$,
independent of z and $\theta$. The normalizing constant is obtained
from evaluating the integral (2.3), with the result that on the axis of
the cylinder (along which the molecules travel in an ammonia maser), the
function $E_{az}$ reduces to 
$$
E_{az} = \frac{1}{J_1\sqrt{V}}. \tag{2.19}
$$

Here $J_1 = J_1(u) = 0.5191$, and u=2.405 is the first root of $J_0(u)=0$.
V is the volume of the cavity. The operator $p_a$ involved in the
electric field expansion is, from (2.14),
$$
p_a = \sqrt{\frac{\hbar\omega_a}{2}}(c_a + c_a^*). \tag{2.20}
$$

 Combining
(2.6), (2.19), (2.20), and (2.21), we obtain the matrix element
$$
(n|E|n^\prime) = -\left(\frac{2\pi\hbar\omega}{J_1^2 V}\right)^{1/2} [\sqrt{n} \, \delta_{n,n^\prime+1} + \sqrt{n+1} \, \delta_{n+1,n^\prime}], \tag{2.21}
$$
in which we have dropped the subscript a, it being understood that
(2.21) refers to the case where only the lowest TM mode is taken into
account. For the matrix elements of electric field at points off the
axis of the cylinder, this expression should be multiplied by $J_0(kr)$. 
## INTERACTION WITH A SINGLE MOLECULE
The simplest possible situation is one where we consider a lossless
cavity, which has only a single resonant mode near the natural line
frequency of the molecules, and a uniform field (electric or magnetic,
whichever is the one effective in field-molecule interaction)
along the path of the molecules. Suppose further that only a single
molecule, which has only two possible energy levels, is in the cavity.
With the molecule-field interaction of the usual
$(\mathbf{J} \cdot \mathbf{A})$ form, it appears that even this problem
cannot be solved exactly. However, because of the simplicity of the
model we will be able to treat it more accurately than is usually done
in more difficult problems, where one resorts to an expansion in powers
of $(e^2/\hbar c)$. The stationary states of the system (molecule +
field) can be found to an accuracy of perhaps one part in $10^7$ for
radiation energy densities up to the order of those encountered in
masers, by a calculation which involves nothing worse than solving
quadratic equations. By use of perturbation theory, still better
accuracy would be feasible, but this is not attempted here.

Let the two possible energy levels of the molecule be denoted by $E_m$,
and the corresponding states by $\Psi_m (m=1,2)$. Similarly, the number
of quanta in the field oscillator will be n, and the corresponding
state of the field by $\Phi_n (n=0, 1, 2, \dots)$. The state vectors
$\Psi_m \Phi_n$ then form a basis for the system (molecule + field). In
this representation, the total Hamiltonian is
$$
(mn|H|m^{\prime} n^{\prime}) = (E_m + n\hbar\omega)\delta_{mm^\prime}\delta_{nn^\prime} + (mn|H_{\text{int}}|m^{\prime} n^{\prime}) \tag{3.1}
$$

The interaction Hamiltonian between molecule and field is taken of the
form 
$$
H_{\text{int}} = -\vec{\mu} \cdot \vec{E} \tag{3.2}
$$
 where $\vec{\mu}$
is the electric dipole moment of the molecule, whose component along
$\vec{E}$ shall have matrix elements
$$
(m|\mu_z|m^\prime) = \mu(1 - \delta_{mm^\prime}). \tag{3.3}
$$

 Combining this with
(2.21), we obtain the matrix elements for the interaction energy
$$
(mn|H_{\text{int}}|m^{\prime} n^{\prime}) = \alpha(1-\delta_{mm^\prime})[\sqrt{n} \, \delta_{n,n^\prime+1} + \sqrt{n+1} \, \delta_{n+1,n^\prime}] \tag{3.4}
$$
where
$$
\alpha = \frac{\mu}{J_1}\sqrt{\frac{2\pi\hbar\omega}{V}} \tag{3.5}
$$
 is
the interaction constant. Using the value[^3] $\mu = 1.47 \times 10^{-18}$
esu for ammonia, and a cavity 10 cm long, we find
$(\alpha/\hbar\omega) = 2.08 \times 10^{-10}$, or, in frequency units,
$\alpha/\hbar \approx 5.0$ cps.

The interaction Hamiltonian has matrix elements of two different types:
$H_{\text{int}} = V+W$, where 
$$
\begin{aligned}
 V_n &= (1, n+1|V|2, n) = (2,n|V|1, n+1) = \alpha(n+1)^{1/2} \\\\ W_n &= (1, n|W|2, n+1) = (2, n+1|W|1, n) = \alpha(n+1)^{1/2}
\end{aligned} \tag{3.6}
$$
 all other elements being zero. The term V
cannot be treated as a perturbation, for its matrix elements connect
"unperturbed" states with an energy separation
$(E_2 - E_1 - \hbar\omega)$ which goes through zero as the cavity is
tuned exactly on the natural line frequency. On the other hand, elements
of W connect states with unperturbed energy separation
$(E_2 - E_1 + \hbar\omega) \approx 2\hbar\omega$. Since in typical
operating conditions $(n \approx 10^6)$ we have
$W_n/2\hbar\omega < 10^{-7}$, we may treat W as a small perturbation, or
even neglect it entirely. We thus write the Hamiltonian as
$$
H = H_o + W, \tag{3.7}
$$
 in which the term
$H_o = (H_{\text{molecule}} + H_{\text{field}} + V)$ must be
diagonalized exactly. This is readily done, since $H_o$ has a "block
form" consisting of many (2$\times$2) matrices along the main diagonal.
The eigenvalues and eigenfunctions of $H_o$, defined by $H_o \Phi_n^\pm = E_n^\pm \Phi_n^\pm$,
are the ground state 
$$
E_o = E_1, \quad \Phi_o = \Psi_1 \Phi_o, \tag{3.8}
$$
and, for $n>0$, 
$$
E_n^\pm = \frac{1}{2}[E_1 + E_2 + (2n-1)\hbar\omega] \pm \frac{1}{2}[(E_2-E_1-\hbar\omega)^2 + 4n\alpha^2]^{1/2} \tag{3.9}
$$
$$
\begin{aligned}
\Phi_n^+ &= \Psi_2 \Phi_{n-1} \cos\theta_n + \Psi_1 \Phi_n \sin\theta_n \\\\ \Phi_n^- &= -\Psi_2 \Phi_{n-1} \sin\theta_n + \Psi_1 \Phi_n \cos\theta_n
\end{aligned} \tag{3.10}
$$
 where
$$
\tan 2\theta_n = \frac{2\alpha\sqrt{n}}{\hbar\omega - (E_2-E_1)}. \tag{3.11}
$$

We now require the time-development matrix (in units with $\hbar=1$)
$$
U(t,t^\prime) = U(t-t^\prime) = \exp[-iH(t-t^\prime)], \tag{3.12}
$$
 for which the
perturbation expansion is
$$
U(t) = e^{-iH_o t} - i \int_0^t e^{i(t-t^\prime)H_o} W e^{i t^\prime H_o} dt^\prime + \dots \tag{3.13}
$$

The major term $U_o = \exp(-iH_o t)$ has the matrix elements, for $n>0$,
$$
\begin{aligned}
(2,n-1|U_o|2,n-1) &= a_n = \cos^2\theta_n e^{-i\omega_n^+ t} + \sin^2\theta_n e^{-i\omega_n^- t} \\\\ (2,n-1|U_o|1,n) &= b_n = \sin\theta_n \cos\theta_n (e^{-i\omega_n^+ t} - e^{-i\omega_n^- t}) \\\\ (1,n|U_o|2,n-1) &= b_n \\\\ (1,n|U_o|1,n) &= c_n = \cos^2\theta_n e^{-i\omega_n^- t} + \sin^2\theta_n e^{-i\omega_n^+ t}
\end{aligned} \tag{3.14}
$$
 and, for n=0, 
$$
(1,0|U_o|1,0) = e^{-i\omega_o t}. \tag{3.15}
$$

All other elements vanish. The transition probability for emission or
absorption of one photon during time t is therefore, neglecting terms in
W,
$$
|b_n|^2 = \sin^2 2\theta_n \sin^2(\omega_n^+ - \omega_n^-)\frac{t}{2} = \frac{n\alpha^2 \sin^2\beta_n t}{\hbar^2\beta_n^2} \tag{3.16}
$$
where 
$$
4\hbar^2\beta_n^2 = [\hbar\omega - (E_2-E_1)]^2 + 4n\alpha^2. \tag{3.17}
$$

The above notation has been chosen in such a way that the block form of
$U_o$ consists of the symmetric, (2$\times$2) unitary matrices
$$
\begin{pmatrix} a_n & b_n \\\\ b_n & c_n 
\end{pmatrix}, \quad n=1, 2, \dots
$$
along the main diagonal. The first row and column, however, contain only
the single term (3.15).

We now consider the effect on the field of passing a single molecule
through the cavity, with flight time $\tau$. At the instant (t=0) when
the molecule enters the cavity, let its state be described by the
density matrix $\rho_1(0)$, and the state of the field by the density
matrix $\rho_f(0)$. The initial density matrix of the entire system is
thus the direct product $\rho(0) = \rho_1(0) \times \rho_f(0)$, with
matrix elements 
$$
(mn|\rho(0)|m^{\prime} n^{\prime}) = (m|\rho_1(0)|m^\prime)(n|\rho_f(0)|n^\prime). \tag{3.18}
$$

During the interaction, $\rho$ undergoes a unitary transformation
$$
\rho(t) = U(t,0) \rho(0) U^{-1}(t,0), \tag{3.19}
$$
 and the density matrix
$\rho_f(t)$, which describes the state of the field only, is the
projection[^4] of (3.19) onto the space of the field variables:
$$
(n|\rho_f(t)|n^\prime) = \sum_m (mn|\rho(t)|mn^\prime). \tag{3.20}
$$

 The net change
in the state of the field thus consists of a linear transformation:
$$
(n|\rho_f(\tau)|n^\prime) = \sum_{k,k^\prime} (nn^\prime|G|kk^\prime)(k|\rho_f(0)|k^\prime), \tag{3.21}
$$
or 
$$
\rho_f(\tau) = G \rho_f(0), \tag{3.22}
$$
$$
(nn^\prime|G|kk^\prime) = \sum_{m,m^\prime,m^{\prime\prime}} (m^{\prime\prime}n|U|mk)(m^{\prime} k^{\prime}|U^{-1}|m^{\prime\prime}n^\prime) \sigma_{mm^\prime}, \tag{3.23}
$$
where we have written for brevity 
$$
\sigma_{mm^\prime} = (m|\rho_1(0)|m^\prime). \tag{3.24}
$$

The sums (3.23) are readily evaluated with use of (3.14), with the result
that the only nonvanishing elements of G are 
$$
\begin{aligned}
(nn^\prime|G|nn^\prime) &= a_{n+1}^* a_{n^\prime+1} \sigma_{22} + c_n^* c_{n^\prime} \sigma_{11} \\\\ (nn^\prime|G|n+1,n^\prime) &= b_{n+1}^* a_{n^\prime+1} \sigma_{12} \\\\ (nn^\prime|G|n,n^\prime+1) &= a_{n+1}^* b_{n^\prime+1} \sigma_{21} \\\\ (nn^\prime|G|n,n^\prime-1) &= c_n^* b_{n^\prime} \sigma_{12} \\\\ (nn^\prime|G|n-1,n^\prime) &= b_n^* c_{n^\prime} \sigma_{21} \\\\ (nn^\prime|G|n+1,n^\prime+1) &= b_{n+1}^* b_{n^\prime+1} \sigma_{11} \\\\ (nn^\prime|G|n-1,n^\prime-1) &= b_n^* b_{n^\prime} \sigma_{22}
\end{aligned} \tag{3.25}
$$

 These relations hold for all quantum numbers
n if we understand that $c_o$ is not defined by (3.14), but by
$c_o = \exp(-i\omega_o t)$.

To illustrate the use of this formalism, we discuss a few simple
problems using (3.25). Consider first the case where the field is
initially in its lowest state; $(0|\rho_f(0)|0) = 1$, all other elements
of $\rho_f(0)$ vanish. Then, according to (3.25), after a molecule with
initial density matrix $\sigma$ has passed through, the field density
matrix has elements 
$$
\begin{aligned}
(0|\rho_f(\tau)|0) &= |a_1|^2 \sigma_{22} + \sigma_{11} \\\\ (0|\rho_f(\tau)|1) = (1|\rho_f(\tau)|0)^* &= c_o b_1^* \sigma_{12} \\\\ (1|\rho_f(\tau)|1) &= |b_1|^2 \sigma_{22}.
\end{aligned} \tag{3.26}
$$
all other elements still vanishing. If the molecule was initially in the
lower state $[\sigma_{11}=1, \sigma_{22}=\sigma_{12}=0]$, then nothing
happens, and the field remains in its ground state. If the molecule was
initially in the upper state, $[\sigma_{22}=1, \sigma_{11}=\sigma_{12}=0]$,
we have a simple transition probability of $|b_1|^2$ for the molecule to
emit one photon in passing through. If there was initially no coherence
relation between upper and lower states of the molecule, then
$\sigma_{12}=0$, and $\rho_f$ remains diagonal; no coherence between
states n=0 and n=1 can be set up by the molecule unless there was some
coherence initially between upper and lower states of the molecule.

The expectation value of electric field along the axis of the cavity, as
obtained from (2.21), is
$$
\begin{aligned}
\langle E \rangle &= \text{Tr}(\rho_f E) = -\frac{\alpha}{\mu} \sum_n \sqrt{n+1} [(n|\rho_f|n+1) + (n+1|\rho_f|n)] \\\\ &= -\frac{2\alpha}{\mu} \text{Re} \sum_n \sqrt{n+1} (n|\rho_f|n+1).
\end{aligned} \tag{3.27}
$$

This remains zero as long as there is no coherence between adjacent
levels, even though the energy stored in the field may be large. In the
case (3.26), we obtain for $\langle E \rangle$,
$$
\langle E \rangle = -\frac{2\alpha}{\mu} \text{Re}(c_o b_1^* \sigma_{12}) = \frac{2\alpha^2 \sin \beta_1 t}{\mu \hbar \beta_1} \text{Re}[i \sigma_{12} e^{i(\Omega+\omega)t/2}], \tag{3.28}
$$
where $\beta$ is defined by (3.17) with n=1, and
$\Omega = (E_2-E_1)/\hbar$ is the natural line frequency of the
molecule. If the cavity is so tuned that its resonant frequency $\omega$
is equal to $\Omega$, then $\hbar\beta = \alpha$, and we obtain simply
$$
\langle E \rangle = \frac{2\alpha}{\mu} \sin\left(\frac{\alpha t}{\hbar}\right) \text{Re}[i \sigma_{12} e^{i\omega t}]. \tag{3.29}
$$

Remembering that $\alpha/\hbar \approx 5$ cps, the term
$\sin(\alpha t/\hbar)$ reaches its first maximum in a quarter cycle, or
about 1/20 second. This is the interaction time required for a molecule
to emit a photon, with probability 1, into a lossless cavity initially
in its ground state. This shows the great enhancement of spontaneous
emission probability due to the presence of the resonant cavity, for the
same molecule in empty space would emit with a natural line width (full
width at half-maximum intensity) of
$$
\Delta\omega = \frac{8\omega^3 \mu^2}{3\hbar c^3} \sim 10^{-7} \text{sec}^{-1}, \tag{3.30}
$$
which leads to spontaneous emission times of the order of months at the
frequencies here considered.

If the molecule and field are in arbitrary initial states, the general
transformation of the field caused by passage of the molecule is, from
(3.25), 
$$
\begin{aligned}
(n|\rho_f(\tau)|n^\prime) &= \sigma_{11} [b_{n+1}^* b_{n^\prime+1} (n+1|\rho_f(0)|n^\prime+1) + c_n^* c_{n^\prime} (n|\rho_f(0)|n^\prime)] \\\\ &+ \sigma_{12} [b_{n+1}^* a_{n^\prime+1} (n+1|\rho_f(0)|n^\prime) + c_n^* b_{n^\prime} (n|\rho_f(0)|n^\prime-1)] \\\\ &+ \sigma_{21} [a_{n+1}^* b_{n^\prime+1} (n|\rho_f(0)|n^\prime+1) + b_n^* c_{n^\prime} (n-1|\rho_f(0)|n^\prime)] \\\\ &+ \sigma_{22} [a_{n+1}^* a_{n^\prime+1} (n|\rho_f(0)|n^\prime) + b_n^* b_{n^\prime} (n-1|\rho_f(0)|n^\prime-1)].
\end{aligned} \tag{3.31}
$$
if the field density matrix is initially diagonal,
$$
(n|\rho_f(0)|n^\prime) = p_n \delta_{nn^\prime}, \tag{3.32}
$$
the only nonvanishing
components of $\rho_f(t)$ are
$$
(n|\rho_f(t)|n) = \sigma_{11} [|b_{n+1}|^2 p_{n+1} + |c_n|^2 p_n] + \sigma_{22} [|a_{n+1}|^2 p_n + |b_n|^2 p_{n-1}], \tag{3.33}
$$
$$
(n|\rho_f(t)|n+1) = (n+1|\rho_f(t)|n)^* = \sigma_{12} [b_{n+1}^* a_{n+2} p_{n+1} + c_n^* b_{n+1} p_n], \tag{3.34}
$$
which relations will be used in the next section.

## SUCCESSIVE SINGLE-MOLECULE INTERACTIONS
If several molecules pass through the cavity in succession, the N'th
entering as the (N-1)'th leaves, all with the same initial state, this
generates a Markov chain,
$$
\rho_f(N\tau) = G^N \rho_f(0) = G \rho_f(N\tau-\tau), \tag{4.1}
$$
and
particular interest attaches to the limiting form of $\rho_f$ as
$N \to \infty$.

If the density matrices of field and molecule are initially diagonal,
$$
\sigma_{12} = \sigma_{21} = 0, \quad (n|\rho_f(0)|n^\prime) = p_n \delta_{nn^\prime}, \tag{4.2}
$$
then $\rho_f$ remains diagonal for all time. In this case the entering
molecules can always be described by a temperature, defined by
$$
\sigma_{22} = \sigma_{11} e^{-x} = (e^x+1)^{-1}, \quad x = (E_2 - E_1)/kT = \hbar\Omega/kT, \tag{4.3}
$$
and, using (3.33), Eq. (4.1) reduces to
$$
\rho_n(N\tau) = (e^x+1)^{-1} [ (|a_{n+1}|^2 + |c_n|^2 e^x)\rho_n(N\tau-\tau) + |b_{n+1}|^2 e^x \rho_{n+1}(N\tau-\tau) + |b_n|^2 \rho_{n-1}(N\tau-\tau) ]. \tag{4.4}
$$

From this, the limiting form of $\rho_n$ may be found. Taking note of
the fact that $|a_n|^2 + |b_n|^2 = |b_n|^2 + |c_n|^2 = 1$, we find that
a necessary and sufficient condition for a steady state,
$\rho_n(N\tau) = \rho_n(N\tau-\tau) = \rho_n$, is that the quantities
$$
B_n = |b_n|^2(\rho_{n-1} - e^x \rho_n) \tag{4.5}
$$
 be independent of n. Now
$\sum_n \rho_n = 1$, and so $\rho_n \to 0$ as $n \to \infty$.

Consequently, $B_n \to 0$, since $|b_n|^2 \le 1$. Thus $B_n$ can be
independent of n only if $B_n = 0$, and the only steady-state solution
is the Boltzmann distribution 
$$
\rho_n = e^{-x} \rho_{n-1} \tag{4.6}
$$
 for
all n for which $|b_n|^2 \ne 0$. From (3.16) it is seen that $b_n$ could
vani sh only for certain isolated special values of n.

Note that (4.6) is not a Boltzmann distribution with the same
temperature T as that of the molecules, except in the case where the
cavity is tuned exactly to the natural line frequency. The temperature
of (4.6) is $T_f = \omega T/\Omega$. This difference would never be seen
in practice, for as soon as we detune the cavity appreciably the
transition probability $|b_n|^2$ becomes extremely small, and the
temperature of the radiation would be determined by its interaction with
the walls of the cavity, here neglected. Nevertheless, in principle the
difference is there, and we have an example of an interaction between two
systems which maintains them at different temperatures. The origin of
the phenomenon lies in the fact that for interactions of finite duration
there is no sharp distinction between "real" and "virtual"
transitions, and, perhaps more to the point, our description of the
state of the molecules in terms of a temperature was not entirely
justified, since nothing was said about their kinetic energy of
translational motion. (It is this translational motion, of course, which
supplies or absorbs the excess energy so as to remove the above apparent
violation of energy conservation. When a molecule enters or leaves the
cavity, it passes through a region of inhomogeneous field, and
experiences a net force which very slightly changes its velocity.)
In the "negative temperature" case where the entering molecules are
more likely to be in the upper state, $\sigma_{22} > \sigma_{11}$, and
x < 0. The solution $B_n = \text{const.}$ is still formally the only
stationary one. But it now represents an infinite amount of energy in
the field and could never be reached by any finite number of molecules
passing through the cavity. It is, of course, only our neglect of losses
which leads to such a result, and in practice the operating level
quickly reaches a steady value which can be predicted by adding a
phenomenological damping term to $\dot{\rho}$ in a well-known way.
As long as the density matrix $\sigma$ of the entering molecules is
diagonal, the density matrix of the field alone also remains diagonal;
the expectation value of electric field remains exactly zero in spite of
the fact that the number of photons present may be very large. This
situation raises certain questions regarding the relation between
quantum theory and classical theory. Usually one supposes that the
condition for validity of classical electromagnetic theory is simply
that the number of photons in each field normal mode be large, and that
one may then identify the classical electromagnetic field with the
quantum-mechanical expectation value. However, here is an example where
in spite of the large photon numbers, no such interpretation is
possible, and the semiclassical theory of radiation could not be applied
to describe such states.

In almost every textbook one can find the statement that quantum theory
always goes over into classical theory in the limit of large quantum
numbers (or, what is the same thing, in the limit $h \to 0$). This,
however, may be misleading for the following reason. In the limit of
large quantum numbers, it is possible to construct well-localized wave
packets by coherent superposition of many stationary states, and by a
well-known theorem, the center of gravity of such a packet then follows
classical equations of motion. This means that, with sufficiently large
quantum numbers, classical behavior is contained in quantum theory as a
special case. But for arbitrarily large quantum numbers, it is still
true that quantum theory allows the existence of a great variety of
possible states (such as stationary states, or coherent superpositions
representing very "broad" wave packets) whose properties cannot even
be described, much less accounted for, in classical terms. So the mere
excitation to large quantum numbers is no guarantee that a system will
behave according to the laws of classical physics. One needs also some
kind of restriction as to the type of measurements which are to be made;
for example that we will make only such coarse observations that
individual quantum effects could not have been seen anyway.

If the density matrix $\sigma$ of the entering molecules is not
diagonal, then according to (3.31) the density matrix of the field also
develops off-diagonal elements. Stated intuitively, the definite phase
of the dipole moment of the entering molecules "tells the field what
phase to have," and results in a non-zero expectation value for E. This
situation is an interesting one which could be realized experimentally
(it is, for example, closely related to the "Ramsey technique" for
obtaining sharp resonances). The steady-state distribution resulting
from (3.31) is a difficult but soluble problem. We will not give the
details here because evidence will be presented later which indicates
that in this case the semiclassical theory should provide a fully
reliable and more efficient way of treating the problem.
## RELATION TO SEMICLASSICAL THEORY
One of the main objectives of this work has been to clarify the relation
between the predictions of quantum electrodynamics and the semiclassical
theory of maser operation mentioned in the Introduction. To define more
precisely what is meant by the semiclassical theory, we write the basic
equations of this approach. Here one considers the electric field E(t)
as classically describable (i.e., as a definite, if unknown, function of
time), and introduces a wave function
$$
\Psi(t) = a(t)\psi_1 + b(t)\psi_2 \tag{5.1}
$$
 for the molecule alone,
which develops in time according to the Schrödinger equation
$$
i\hbar\dot{\Psi} = (H_{\text{molecule}} + H_{\text{int}})\Psi, \tag{5.2}
$$
where 
$$
(m|H_{\text{molecule}}|m^\prime) = E_m \delta_{mm^\prime}, \tag{5.3}
$$
$$
(m|H_{\text{int}}|m^\prime) = (m|-\vec{\mu} \cdot \vec{E}(t)|m^\prime) = -\mu(1-\delta_{mm^\prime})E(t). \tag{5.4}
$$

Equation (5.2) then reduces to 
$$
\begin{aligned}
i\hbar\dot{a} &= E_1 a - \mu E(t)b \\\\ i\hbar\dot{b} &= -\mu E(t)a + E_2 b
\end{aligned} \tag{5.5}
$$
 which describes the effect of the field on the
molecule. To find the effect of the molecule on the field, one calculates
the expectation value of dipole moment of the molecule from the solution
of (5.5), 
$$
M(t) = \langle\mu(t)\rangle = \mu(ab^*+a^*b), \tag{5.6}
$$
 and
assumes that the field satisfies the classical equation of motion which
would result from interaction with a dipole of moment M(t). This is
obtained most easily from the Hamiltonian equations of motion by
addition of the interaction energy
$$
-\mathbf{M} \cdot \mathbf{E} = +\sqrt{4\pi} \sum_a p_a E_a(x) \cdot \mathbf{M} \tag{5.7}
$$
to $\mathcal{H}$ in (2.8), where $\mathbf{x}$ denotes the position of the
molecule. The classical equations of motion are now
$$
\begin{aligned}
\dot{p}_a &= -\frac{\partial\mathcal{H}}{\partial q_a} = -\omega_a^2 q_a, \\\\ \dot{q}_a &= \frac{\partial\mathcal{H}}{\partial p_a} = p_a + \sqrt{4\pi}\mathbf{M}\cdot\mathbf{E}_a(\mathbf{x}),
\end{aligned} \tag{5.8}
$$
 or, eliminating $\dot{q}_a$,
$$
\ddot{p}_a + \omega_a^2 p_a = -\sqrt{4\pi}\omega_a^2 \mathbf{M} \cdot \mathbf{E}_a(\mathbf{x}). \tag{5.9}
$$

Finally, assuming that only the single mode (2.19) is excited, the
electric field of this mode satisfies the differential equation
$$
\ddot{E} + \omega^2 E = +\frac{4\pi\omega^2}{J_1^2 V} M_z, \tag{5.10}
$$
 where
we have again dropped the subscript a. If the cavity has a finite Q, due
to wall losses and/or energy coupled out, this is taken into account by
adding a phenomenological term to (5.10), giving us
$$
\ddot{E} + \frac{\omega}{Q} \dot{E} + \omega^2 E = \frac{4\pi\omega^2}{J_1^2 V} M. \tag{5.11}
$$

By the "semiclassical theory" we mean the system of equations (5.5),
(5.6), (5.11). They may be given a slightly neater formal appearance by
eliminating the amplitudes a(t), b(t). The result is the nonlinear
system of coupled equations 
$$
\ddot{M} + \Omega^2 M = -K^2 W E(t), \tag{5.12a}
$$
$$
\dot{W} = E \dot{M}, \tag{5.12b}
$$
$$
\ddot{E} + \frac{\omega}{Q} \dot{E} + \omega^2 E = S \ddot{M}, \tag{5.12c}
$$
 where
$$
K = \frac{2\mu}{\hbar}, \quad S = \frac{4\pi}{J_1^2 V}, \tag{5.13}
$$
and
$$
W = E_1 |a|^2 + E_2 |b|^2 - \frac{1}{2}(E_1+E_2) = \frac{1}{2}\hbar\Omega(|b|^2 - |a|^2) \tag{5.14}
$$
is the expectation value of energy of the molecule, referred to a zero
lying midway between the levels $E_1, E_2$. In the form (5.12a), (5.12b), (5.12c) we have
an apparently classical nonlinear system, all reference to
"quantum-mechanical" quantities having disappeared.

The first two of the equations (5.12a), (5.12b) admit a first integral,
$$
(\dot{M})^2 + \Omega^2 M^2 + K^2 W^2 = \text{const.} = \left(\frac{K\hbar\Omega}{2}\right)^2, \tag{5.15a}
$$
which is readily verified by eliminating E between them. Eq. (5.15a) is
a highly disguised form of the "principle of conservation of
probability," $|a|^2 + |b|^2 = \text{const.} = 1$. Similarly, the last
two of the equations (5.12b), (5.12c) can be combined, in the case $Q=\infty$, to
yield the constant of the motion
$$
(\dot{E})^2 + \omega^2 E^2 + 2S(W-ME) = \text{const.} \tag{5.15b}
$$
 which
expresses the conservation of energy for the system.

Now, what is the relationship between the system of equations (5.12a), (5.12b), (5.12c) and
our earlier ones based on quantum electrodynamics? In order to answer
this, we note that Eqs. (5.12a) and (5.12c) show a strong formal
resemblance to a general operator equation of motion, which is obtained
by differentiating the relation $i\hbar \dot{F} = [F,H]$. The result is
$$
\hbar^2 \ddot{F} + [H, [H,F]] = i\hbar[\dot{H},F] \tag{5.16}
$$
 which is
exact for any operator F.

Returning to the quantum electrodynamics analysis, let us apply this
identity to the electric field operator: F=E. The total Hamiltonian
$H = (H_{\text{mol}} + H_{\text{field}} + H_{\text{int}})$ has no
explicit time dependence, so the righthand side of (5.16) will vanish.
To evaluate the double commutator, we note that $H_{\text{int}}$
commutes with E but not with $[H_f, E]$, while $H_m$ commutes with both.
Therefore 
$$
[H,[H,E]] = [H_f, [H_f, E]] + [H_{\text{int}}, [H_f, E]]. \tag{5.17}
$$

These commutators are readily worked out, with the results
$$
[H_f, [H_f, E]] = \hbar^2 \omega^2 E, \tag{5.18}
$$
$$
[H_{\text{int}}, [H_f, E]] = -\hbar^2 S \mu_{\text{op}}. \tag{5.19}
$$

Therefore, a special case of (5.16) is the operator identity
$$
\ddot{E} + \omega^2 E = S \mu_{\text{op}} \tag{5.20}
$$
 which is to be
compared to (5.12c). If we interpret (5.12c) as the expectation value of
(5.20), they are seen to be identical in the limit $Q \to \infty$,
provided that the expectation value of $\mu_{\text{op}}$ must be defined,
not in terms of a(t) and b(t) by means of (5.6), but as the expectation
value taken over the complete density matrix $(mn|\rho|m^{\prime} n^{\prime})$:
$$
\langle \mu_{\text{op}} \rangle = \text{Tr}(\rho \mu_{\text{op}}) = \sum_{m,m^\prime,n} (mn|\rho|m^{\prime} n)(m^{\prime} n|\mu_{\text{op}}|mn). \tag{5.21}
$$

With this change in interpretation, (5.12c) is seen to be an exact
consequence of quantum electrodynamics.

Next we write out the identity (5.16) for the case $F=\mu_{\text{op}}$.
This time $H_{\text{int}}$ commutes with $\mu_{\text{op}}$, but not with
$[H_m, \mu_{\text{op}}]$, while $H_f$ commutes with both. Therefore,
$$
[H, [H, \mu_{\text{op}}]] = [H_m, [H_m, \mu_{\text{op}}]] + [H_{\text{int}}, [H_m, \mu_{\text{op}}]]. \tag{5.22}
$$

Proceeding as before, a short calculation yields the results
$$
[H_m, [H_m, \mu_{\text{op}}]] = \hbar^2 \Omega^2 \mu_{\text{op}} \tag{5.23}
$$
$$
[H_{\text{int}}, [H_m, \mu_{\text{op}}]] = \hbar^2 K^2 H^\prime E \tag{5.24}
$$
where we have defined an operator
$$
H^\prime \equiv H_{\text{molecule}} - \frac{1}{2}(E_1+E_2) \tag{5.25}
$$
 with
matrix elements
$$
(mn|H^\prime|m^{\prime} n^{\prime}) = \frac{1}{2}\hbar\Omega(-1)^m \delta_{mm^\prime} \delta_{nn^\prime} \tag{5.26}
$$
which is the energy of the molecule, referred to a zero lying midway
between its levels $E_1, E_2$. Combining these relations, we find that
another special case of (5.16) is the operator identity
$$
\ddot{\mu}_\text{op} + \Omega^2 \mu_{\text{op}} = -K^2 H^\prime E \tag{5.27}
$$
which is to be compared to (5.12a). This time, taking the expectation
value of (5.27) does not yield (5.12a) in general, for in the
semiclassical equation the "driving force" term appears as
$\langle H^\prime \rangle \langle E \rangle$, while according to quantum
electrodynamics it should be $\langle H^\prime E \rangle$. The difference
between these quantities arises from the possibility, which exists in
quantum electrodynamics but not in the semiclassical theory, of
"correlated states." When the states of field and molecule are
uncorrelated, the density matrix reduces to a direct product
$\rho = \rho_m \times \rho_f$, or
$$
(mn|\rho|m^{\prime} n^{\prime}) = (m|\rho_m|m^\prime)(n|\rho_f|n^\prime). \tag{5.28}
$$

 When (5.28)
holds, it is easily shown that
$\langle H^\prime E \rangle = \langle H^\prime \rangle \langle E \rangle$. But if
(5.28) does not hold, then in general
$\langle H^\prime E \rangle \ne \langle H^\prime \rangle \langle E \rangle$. Before
exploring the size of this difference, we digress to consider some
general consequences of correlated states.
## CORRELATED STATES
To describe the situation in intuitive terms, the semiclassical theory
may be regarded as based on the assumption that the electric field has, at
any time, "in reality" a definite, if unknown, value. Similarly,
one imagines the molecule as being "in reality" in a definite if
unknown quantum state $\Psi$. However, quantum electrodynamics allows the
possibility of states of the combined system (molecule + field), which do
not admit any such description. The stationary states (3.9) are examples
wherein the system (molecule + field) is in a definite pure state, but
nevertheless one cannot ascribe any definite quantum state to the
molecule alone, or the field alone.

This situation arises in general whenever two different
quantum-mechanical systems interact, and forms the basis of one of
Einstein's objections to quantum theory. The famous
Einstein-Podolsky-Rosen paradox[^5] consists in the fact that when such
correlated states exist, one has the possibility of predicting with
certainty either one of two noncommuting quantities of a system by
making measurements which do not involve any physical interaction with
it. The molecular-beam maser provides a particularly neat example of
this. Suppose the field is initially in its ground state and the molecule
in its upper state. When they start to interact at time t=0, the state of
(molecule + field) then becomes a linear combination
$$
\Psi(t) = \cos\theta_1 \Phi_1^+ e^{-i\omega_1^+ t} + \sin\theta_1 \Phi_1^- e^{-i\omega_1^- t} = a_1(t)\Psi_2\Phi_0 + b_1(t)\Psi_1\Phi_1, \tag{6.1}
$$
where the notation is the same as in Section 3. At time $\tau$, the
molecule leaves the cavity and continues on its way. But although
interaction between molecule and field ceases, there remains a complete
correlation between their states, for at later times than $\tau$,
molecule and field will still be jointly in the pure state
$$
\Psi(t) = g_o(t)\Psi_2\Phi_0 + g_1(t)\Psi_1\Phi_1, \tag{6.2}
$$
 where
$$
g_o(t) = a_1(\tau)\exp\left[\frac{-iE_2(t-\tau)}{\hbar}\right] \tag{6.3}
$$
$$
g_1(t) = b_1(\tau)\exp\left[\frac{-i(E_1+\hbar\omega)(t-\tau)}{\hbar}\right] . \tag{6.4}
$$

Now suppose we measure the energy of the molecule by passing it through
an inhomogeneous field like that in the focuser. If we find the molecule
in the upper state, then according to (6.2) a "reduction of the wave
packet" occurs and the field is left in state $\Phi_0$. If we find the
molecule in the lower state, on the other hand, then we know that the
field must be in state $\Phi_1$. Thus by measuring the energy of the
molecule, we can predict with certainty the result of a measurement of the
energy of the field. We cannot, however, say anything at all about the
phase of the electric field, since this does not commute with $H_f$.
But instead of measuring the energy of the molecule, we could decide to
measure instead its dipole moment $\vec{\mu}$. According to quantum
mechanics, we must obtain one of the eigenvalues $\pm\mu$ of the
operator $\mu_{\text{op}}$. Now the eigenstates of $\mu_{\text{op}}$,
defined by $\mu_{\text{op}}\chi_\pm = \pm\mu\chi_\pm$ are
$$
\chi_\pm = \frac{1}{\sqrt{2}}(\psi_1 \pm \psi_2), \tag{6.5}
$$
 so that
the wave function (6.2) can be written equally well as
$$
\Psi(t) = \chi_+ \left[\frac{g_o(t)\Phi_0 + g_1(t)\Phi_1}{\sqrt{2}}\right] + \chi_- \left[\frac{g_o(t)\Phi_0 - g_1(t)\Phi_1}{\sqrt{2}}\right]. \tag{6.6}
$$

Suppose our measurement at time $t_1$ gives the result ($+\mu$). Then we
know that at this same instant the field must have been in the state
$$
\Phi_+(t_1) = g_o(t_1)\Phi_o + g_1(t_1)\Phi_1, \tag{6.7}
$$
 and therefore,
at any time $t > \tau$, the field is described by the pure state
$$
\Phi_+(t) = g_o(t_1)\Phi_o + g_1(t_1)\Phi_1 e^{-i\omega(t-t_1)}. \tag{6.8}
$$

From this, using the relations of Section 3, we find the expectation
value of electric field to be
$$
\begin{aligned}
\langle E(t) \rangle_+ &= -\frac{2\alpha}{\mu} \text{Re}[g_o(t_1)g_1^*(t_1)e^{i\omega(t-t_1)}] \\\\ &= -\frac{\alpha \sin 2\theta_1}{\mu} \text{Re}\left[\cos 2\theta_1(1-\cos 2\beta\tau)+i\sin 2\beta\tau\right] e^{i(\omega-\Omega)(t_1-\tau)}e^{i\omega(t-t_1)}.
\end{aligned} \tag{6.9}
$$

For simplicity, let the cavity be tuned exactly on the natural line
frequency ($\omega=\Omega$), and choose the time of interaction $\tau$
so that $4\beta\tau = \pi$. Then $\theta_1 = \pi/4$, and (6.9) reduces
to 
$$
\langle E(t) \rangle_+ = -\frac{\alpha}{\mu}\sin\omega(t-t_1). \tag{6.10}
$$

If, on the other hand, measurement of $\mu_{\text{op}}$ at time $t_1$
yields the result ($-\mu$), then we know that the field must, at time
$t_1$, have been in the state
$$
\Phi_-(t_1) = g_o(t_1)\Phi_o - g_1(t_1)\Phi_1, \tag{6.11}
$$
and, repeating the above argument, we obtain instead
$$
\langle E(t) \rangle_- = +\frac{\alpha}{\mu} \sin\omega(t-t_1), \quad t > \tau. \tag{6.12}
$$

The remarkable thing about (6.10) and (6.12) is that they still contain
$t_1$. Merely by choosing the time at which we measure $\mu$, we can
"force" the electric field to have any phase we please, except for an
uncertainty of 180$^{\circ}$! The measurement of $\mu$ can, in principle,
be carried out at a time when the molecule is arbitrarily far from the
cavity, so there can be no question of any physical interaction which
could influence the field in the cavity.
## EQUATIONS OF MOTION
We have seen that the semiclassical theory leads to the following
equation for describing the effect of the field on the state of a
molecule: 
$$
\ddot{M} + \Omega^2 M = -K^2 W E, \tag{5.12a}
$$
 where M, W
are the dipole moment and energy of the molecule, E the electric field, and
$K=2\mu/\hbar$. If the quantities M, W, E are interpreted as
expectation values, this is equivalent to the equation
$$
\frac{\partial^2}{\partial t^2} \langle\mu\rangle + \Omega^2 \langle\mu\rangle = -K^2 \langle H^\prime \rangle \langle E \rangle. \tag{7.1}
$$

In quantum electrodynamics, the operator equation of motion (5.27) leads
instead to
$$
\frac{\partial^2}{\partial t^2} \langle\mu\rangle + \Omega^2 \langle\mu\rangle = -K^2 \langle H^\prime E \rangle. \tag{7.2}
$$

We now write out the right-hand sides of (7.1) and (7.2) in terms of the
density matrix $(mn|\rho|m^{\prime} n^{\prime})$. From the relations of Sections 3 and 5,
we have 
$$
\begin{aligned}
\langle H^\prime \rangle &= \sum_{m,n,m^\prime} \frac{\hbar\Omega}{2} (-)^m \delta_{mm^\prime} (m^{\prime} n|\rho|mn), \\\\ &= \frac{\hbar\Omega}{2} \sum_n [(2n|\rho|2n) - (1n|\rho|1n)];
\end{aligned} \tag{7.3}
$$
$$
\begin{aligned}
\langle E \rangle &= -\sum_{m,m^\prime,n,n^\prime} \frac{\alpha}{\mu} [\sqrt{n} \, \delta_{n,n^\prime+1} + \sqrt{n+1} \, \delta_{n+1,n^\prime}] \delta_{mm^\prime} (m^{\prime} n^{\prime}|\rho|mn), \\\\ &= -\frac{2\alpha}{\mu} \text{Re} \sum_{m,n} \sqrt{n+1} (mn|\rho|m,n+1);
\end{aligned} \tag{7.4}
$$
$$
\begin{aligned}
\langle H^\prime E \rangle &= -\sum_{m,m^\prime,n,n^\prime} \frac{\hbar\Omega\alpha}{2\mu} (-)^m \delta_{mm^\prime} [\sqrt{n} \, \delta_{n,n^\prime+1} + \sqrt{n+1} \, \delta_{n+1,n^\prime}] (m^{\prime} n^{\prime}|\rho|mn), \\\\ &= -\frac{\hbar\Omega\alpha}{\mu} \text{Re} \sum_n \sqrt{n+1} [(2,n|\rho|2,n+1) - (1,n|\rho|1,n+1)].
\end{aligned} \tag{7.5}
$$

 It should be noted that a direct comparison of
(7.1) and (7.2) is not really justified; for the transition from (5.12a) to
(7.1) is not.

In a fully consistent semiclassical theory the variation of M, W, E,
would be determined from solving Eqs. (5.12a), (5.12b), (5.12c) instead of "borrowing"
the solutions of the quantum electrodynamics problem as is implied by
(7.3) and (7.4). Therefore the following arguments cannot claim full
validity. It is apparent from the above equations, however, that in
general the difference between (7.1) and (7.2) could be very great. For
example, only diagonal elements of $\rho$ contribute to
$\langle H^\prime \rangle$, while no diagonal elements contribute to
$\langle H^\prime E \rangle$.

Because of this, it is easy to invent special initial density matrices
(for example, the one representing the field in the ground state and an
entering molecule with $\sigma_{12} \ne 0$) for which the effect of
correlations is decisive. We can have
$\langle H^\prime \rangle \langle E \rangle = 0$, but
$\langle H^\prime E \rangle \ne 0$ throughout the motion. However, these seem
to represent idealized cases which could hardly be set up
experimentally. Realistic situations are those where the magnitude of
the field is well determined on a percentage basis, but with
uncertainties still large compared to effects of a single photon; for
example, where all elements of $(mn|\rho|m^{\prime} n^{\prime})$ corresponding to
$n \approx 10^6 \pm 10^3$ are significantly large, other elements being
small. Under these conditions, however, the major contributions to
$\langle H^\prime \rangle$, $\langle E \rangle$, and $\langle H^\prime E \rangle$ all
come from the same range of quantum numbers, and unless there is some
fine-grained variation of elements of $\rho$ within this range
(which would represent a far more detailed state of information than we
ever have in practice), it turns out that the difference between
$\langle H^\prime \rangle \langle E \rangle$ and $\langle H^\prime E \rangle$ will be
negligible.
## SOLUTIONS OF THE NONLINEAR SEMICLASSICAL EQUATIONS
In this section we look more closely at the system of equations (5.12a), (5.12b), (5.12c)
representing the semiclassical theory. It is convenient to eliminate the
constants K, S by the change of variables
$$
\begin{aligned}
x(t) &= K E(t), \\\\ y(t) &= KS M(t), \\\\ z(t) &= K^2S W(t),
\end{aligned} \tag{8.1}
$$
whereupon the equations of motion reduce to
$$
\ddot{x} + \omega^2 x = \ddot{y}, \tag{8.2a}
$$
$$
\ddot{y} + \Omega^2 y = -zx, \tag{8.2b}
$$
$$
\dot{z} = x\dot{y}, \tag{8.2c}
$$
and the conservation laws (5.15a), (5.15b) become
$$
(\dot{y})^2 + \Omega^2 y^2 + z^2 = \text{const.}, \tag{8.3}
$$
$$
(\dot{x})^2 + \omega^2 x^2 + 2(z - x\dot{y}) = \text{const.} \tag{8.4}
$$

 These
quantities are not dimensionless, but involve only time. Their numerical
values will therefore depend on our unit of time. The constant in (8.3) is
$$
\left( \frac{8\pi \mu^2 \omega^2 \Omega^2}{\hbar^2 J_1^4 V^2} \right) = 3.4 \times 10^{51} \text{ sec}^{-8}. \tag{8.5}
$$

Noting that $(2.76 \times 10^6)^{8} = 3.4 \times 10^{51}$, we see that
if we choose our unit of time as 0.36 microsecond (call it a subsecond),
this constant becomes numerically equal to unity, and (8.3) becomes
$$
(\dot{y})^2 + \Omega^2 y^2 + z^2 = 1 \text{ sub-sec}^{-8}, \tag{8.6}
$$
 i.e.,
the projection of the orbit onto the space of $\dot{y}, \Omega y, z$
always lies on the unit sphere. There is no limitation imposed on
numerical values of the field x, but the amplitudes in typical maser
operation ($n \le 10^6$ quanta) correspond to
$$
|x| \le \frac{2\mu}{\hbar}\sqrt{\frac{2\pi n \hbar\omega}{J_1^2 V}} = 5.3 \times 10^4 \text{ sec}^{-1} = 2 \times 10^{-2} \text{ sub-sec}^{-1} \tag{8.7}
$$

Therefore, since $|\ddot{y}| \le 1$, we see from (8.2c) that z will
always be slowly varying; under the conditions of interest here, any
appreciable change in z can take place only in times of the order of
tens to thousands of subseconds.

We thus have a very convenient time scale for our problem, for the
frequencies $(\omega/2\pi)$, $(\Omega/2\pi)$ are about $10^4$ cycles per
subsecond, and the flight time of a molecule through the cavity is of
the order of 1000 subseconds. On this time scale, the oscillations of
field (x) and dipole moment (y) are still very rapid, while secular
changes due to their interaction are very slow. Because of this clean
separation into fast and slow changes, one might hope to get a fairly
complete understanding of the solutions of (8.2a), (8.2b), (8.2c) in spite of their
nonlinear character.

The simplest approximate solution is the one wherein we ignore the time
variation of z, thereby converting the problem into a linear one,
similar to the case of two coupled pendulums. The two normal modes are
found by assuming that x and y have a common time factor $\exp(ivt)$;
if $z = \text{const.}$, the Eqs. (8.2a), (8.2b) then reduce to
$$
(\omega^2-v^2)(\Omega^2-v^2) + z=0, \tag{8.8}
$$
 or
$$
v^2 = \frac{\omega^2+\Omega^2}{2} \pm \frac{1}{2} \sqrt{(\omega^2-\Omega^2)^2 - 4z}. \tag{8.9}
$$

We see here a new feature, not present in the case of coupled pendulums;
if $z > 0$ and the cavity is tuned so closely to the natural line
frequency that 
$$
|\omega^2 - \Omega^2| < 2\sqrt{z}, \tag{8.10}
$$
 the
square root in (8.9) becomes imaginary; one of the normal modes grows
exponentially, the other decays.

Now an oscillation of growing amplitude represents energy being
transferred from molecule to field, and therefore we see that, contrary
to what is usually supposed, the semiclassical theory does lead to a
prediction of spontaneous emission. Since z is just the energy of the
molecule, in unconventional units, we see that the condition for
existence of unstable growing oscillations is that the molecule's wave
function $\psi = a\psi_1 + b\psi_2$ must contain more of the upper state
than the lower: $|b|^2 > |a|^2$.

We work out some further details for the case that the cavity is tuned
exactly on the natural line frequency: $\omega = \Omega$. Then (8.9)
reduces to 
$$
v^2 = \omega^2 \pm i\sqrt{z}, \tag{8.11}
$$
 or, to an
extremely good approximation,
$$
v = \omega \pm \frac{i\sqrt{z}}{2\omega}. \tag{8.12}
$$

 If we start
with the molecule nearly in the upper state, then
$z \approx 1 \text{ sub-sec}^{-4}$, and the amplitude of the field varies
like
$$
\exp\left[\frac{\sqrt{z}t}{2\omega}\right]e^{i\omega t} = \exp\left(\frac{\alpha t}{\hbar}\right)e^{i\omega t}, \tag{8.13}
$$
where $\alpha$ is the interaction constant defined in Eq. (3.5). This is
to be compared to the result (3.29) describing spontaneous emission
according to quantum electrodynamics. It is seen that although the two
approaches lead to equations of different functional form, they predict
exactly the same characteristic time $(\hbar/\alpha)$ for spontaneous
emission.

This appears to be one of the most important results of the work here
reported, and it shows that the relation between quantum electrodynamics
and the semiclassical theory of radiation is of a quite different type
than is usually assumed. Physically, it means that when the molecule has
any dipole moment different from zero, the fields set up by this dipole
react back on the molecule and change its state in such a way that
energy is delivered to the field, as long as $z>0$. These linear
relations, of course, cannot hold indefinitely. From the conservation
law (8.6) it is clear that when the amplitude of the y oscillation
increases, the magnitude of z must decrease, and this will eventually
put a stop to the emission process.

For a qualitative picture of the secular changes in the case
$\omega = \Omega$, we may consider the orbits in the
($\dot{x}, \omega x$) plane and in the ($\dot{y}, \omega y$) plane, as
in Fig. 1.
**[FIGURE 1: Closed orbits in the phase space of the x and y oscillators. The dots indicate that the x motion is 90° ahead of the y motion in phase.]**
Noting that $x\dot{y}$ is typically about $10^{-6}$ times smaller than
$\dot{z}$, the conservation law (8.4) reduces, in almost all cases, to
$$
(\dot{x})^2 + \omega^2 x^2 + 2z = \text{const.}, \tag{8.14}
$$
 which
shows that when z increases, the orbit in the ($\dot{x}, \omega x$) plane
must shrink, and vice versa. Similarly the conservation law (8.6) shows
that if $|z|$ increases, the y-orbit must shrink, and vice versa. Therefore
the direction of all secular changes is determined by the sign of
$\dot{z}$ and z. In the equation $\dot{z} = x\dot{y}$ we can for all
practical purposes replace $x\dot{y}$ by its average
$\overline{x\dot{y}}$ over one cycle, since we are interested in the
trend of z over time scales of many cycles, rather than small rapid
fluctuations whose effect averages to zero over a cycle. Secular changes
in z thus depend only on the sign of $\overline{x\dot{y}}$.

Now whenever the x motion is advanced in phase over the y motion, we
have $\overline{x\dot{y}} > 0$. In this case, z will slowly increase, and the
x-orbit will shrink. The y-orbit will then grow if $z<0$, shrink
if $z>0$. If the y motion is advanced in phase over the x motion, all
these secular changes are reversed. Thus the situation may be summarized
by the orbit diagrams of Fig. 2. The situations depicted in the column
labelled $z > 0$ are just the growing and shrinking normal modes of Eq.
(8.12).

Whenever the x-orbit is expanding, energy is being delivered from the
molecule to the field, and the necessary and sufficient condition for
this is that the y motion be advanced in phase over the x motion.
**[FIGURE 2: Secular changes in orbits for the four combinations of signs of xy and z.]**
Thus in order to understand the long-time course of events, we must
study the secular changes in relative phase of x and y. To this end,
introduce the slowly varying complex amplitude X, Y, defined by
$$
\dot{x} + i\omega x = X(t) e^{i\omega t}, \tag{8.15}
$$
$$
\dot{y} + i\omega y = Y(t) e^{i\omega t}. \tag{8.16}
$$

If we regard
the above orbit diagrams as complex planes, the quantities depicted are
just the complex numbers (8.15) and (8.16). Noting the properties
$$
(\dot{x})^2 + \omega^2 x^2 = |X|^2, \tag{8.17}
$$
$$
\ddot{x} + \omega^2 x = \dot{X} e^{i\omega t}, \tag{8.18}
$$
and similarly for Y, we can write the equations of motion (8.2a), (8.2b), (8.2c) in the
form: 
$$
2i\omega \dot{X} = \dot{Y} - Y^* e^{-i2\omega t}, \tag{8.19a}
$$
$$
2i\omega \dot{Y} = -z[X-X^* e^{-i2\omega t}], \tag{8.19b}
$$
$$
4i\omega \dot{z} = XY^* - X^*Y + XY e^{i2\omega t} - X^*Y^* e^{-i2\omega t}, \tag{8.19c}
$$
which are exact for the case $\omega = \Omega$. The
conservation laws become simply 
$$
|Y|^2 + z^2 = 1, \tag{8.20}
$$
$$
|X|^2 + 2z = \text{const}. \tag{8.21}
$$

Now the quantities X, Y are
slowly varying functions of time, and again it is their average change
over many cycles, rather than the very small rapid fluctuation at
frequency $2\omega$, which interest us. Therefore the oscillating terms
in (8.19a), (8.19b), (8.19c) may be dropped, since their average over a cycle is negligible
compared to that of the "DC" terms. The system of equations determining
secular changes of both amplitude and phase is therefore 
$$
2i\omega \dot{X} = \dot{Y}, \tag{8.22a}
$$
$$
2i\omega \dot{Y} = -zX, \tag{8.22b}
$$
$$
4i\omega \dot{z} = XY^* - X^*Y. \tag{8.22c}
$$

It is readily verified that the conservation
laws (8.20), (8.21) are exact consequences of (8.22a), (8.22b), (8.22c). Differentiating
(8.22c) once more are making use of the conservation laws, we can
eliminate X and Y, obtaining the equation
$$
4\omega^2 \ddot{z} - 3z\dot{z}^2 + 2az + 1 = 0, \tag{8.23}
$$
 where
$2a = |X|^2+2z$ is the constant of the motion (8.21). A first integral
of (8.23) is obtained immediately:
$$
2\omega^2 (\dot{z})^2 - z^3 + az^2 + z = \text{const.} = c, \tag{8.24}
$$
which has the form of the Hamilton-Jacobi equation for motion of a
particle in a particular potential well. For any motion in which either
of the points $z=\pm 1$ is accessible, we have $c=a$. To see this, note
that if $|z|=1$, we have $Y=0$ from (8.20), and hence $\dot{z}=0$. But
then (8.24) reduces to $a=c$. For any such motion, the cubic polynomial
in (8.24) factors, and the solution is
$$
\frac{t}{\omega\sqrt{2}} = \int_{z(0)}^{z(t)} \frac{dz}{\sqrt{(1+z)(1-z)(a-z)}}. \tag{8.25}
$$

The z-motion is therefore periodic, between turning-points represented
by singularities of the integrand. If $a>1$, these turning-points are at
$z=\pm 1$, while if $a<1$, they are at z=-1 and z=a. Noting that the
condition for the total energy stored in the field to be just
$\hbar\omega$ is that $|X|^2=4$, we see from (8.21) that
$$
\frac{a+1}{2} = n+1 \tag{8.26}
$$
 where n is the number of quanta in the
field when the molecule is in its upper state; therefore (n+1) is the
number when the molecule is in its ground state. There is in this theory
no restriction of n to integer values. The smallest value which a can
attain is represented by zero energy in the field and the molecule in
its ground state, or (n+1)=0. (When n < 0, this of course means that
the total energy is insufficient for the molecule to get into its upper
state, and this is the physical reason why the turning-point of the
z-motion then occurs at z=a).

The integral in (8.25) is one of the standard forms defining elliptic
functions. Using the standard notation sn(u,k), the solution for the
case $n \ge 0$ is
$$
z(t) = -1 + 2 \text{sn}^2\left[\sqrt{n+1} \frac{\alpha t}{\hbar} + Q, \frac{1}{\sqrt{n+1}}\right] , \tag{8.27}
$$
where
$$
Q = \text{sn}^{-1}\left[\sqrt{\frac{z(0)+1}{2}}, \frac{1}{\sqrt{n+1}}\right] \tag{8.28}
$$
is the initial phase of the motion. In the limit of large n, the
elliptic functions approach trigonometric functions, as is seen most
easily directly from (8.25). If $a \gg 1$, then (8.25) reduces to
$$
\frac{t}{\omega\sqrt{2}} \approx \int \frac{dz}{\sqrt{a(1-z^2)}} = \frac{1}{\sqrt{a}} \sin^{-1}z(t) + \text{const.}, \tag{8.29}
$$
or 
$$
z(t) \approx \sin(2\sqrt{n} \frac{\alpha t}{\hbar} + \Theta). \tag{8.30}
$$

The case a=1, n=0 is a special one, for the integrand of (8.25) then
develops a first-order pole at z=1. The solution (8.27) is still valid
but it is no longer a periodic solution, for sn(u,1) is qualitatively
like $\tanh u$; it approaches $\pm 1$ asymptotically as
$u \to \pm \infty$. This represents a case where the energy in the field
exactly disappears just as the molecule gets into its upper state, and
the final stages of the solution (8.27) then represent the "shrinking
normal mode" of (8.12), where X is 90° ahead of Y. (This phase relation
is in fact maintained throughout the part of the motion (8.27) in which
z increases; throughout the decreasing part, X is 90° behind Y).

The point z=1 is a metastable point of the orbit in this case, for if we
start out with exactly the initial conditions z=1, X=Y=0, then nothing
happens; all time derivatives remain zero, and the molecule does not
emit. However, if there is the slightest change in this initial
condition, the growing normal mode of (8.12) will be started up (unless
the phase relation between X and Y happens to be exactly the value for
the pure shrinking mode), and eventually the energy of the molecule
spills out entirely into the field when we reach the lower turning point
z=-1. The molecule then reabsorbs the energy $\hbar\omega$ from the
field, passing back to the metastable point z=1 according to the
solution (8.27), but requiring an infinite time to do so.

The constant of integration c in (8.24) is related to the relative phase
of the X and Y motions, and other values than c=a, as in (8.25), lead
to more general solutions. To show this, note that at z=0, (8.22c) and
(8.24) combined give
$$
4\omega^2(\dot{z})^2 = 2c = |\text{Im}(XY^*)|^2 = |X|^2|Y|^2 \sin^2\Theta(0), \tag{8.31}
$$
where $\Theta(z)$ is the relative phase of the X and Y motions, at a
time when z has the specified value. But in the case z=0, the
conservation laws give $|Y|^2=1$, $|X|^2=2a$, and therefore
$$
c = a \sin^2\Theta(0). \tag{8.32}
$$

 For arbitrary relative phase angle
$\Theta(0)$, the turning points of the z motion are the two lowest roots
of the equation 
$$
z^3-az^2-z+c = (z-z_1)(z-z_2)(z-z_3)=0, \tag{8.33}
$$
 or
$$
(1-z^2)(a-z) = a \cos^2\Theta(0). \tag{8.34}
$$

 Let us order the roots so
that $z_1 \le z_2 \le z_3$. Then, if a > 1 and c < a, we have the relations
$$
-1 \le z_1 \le z \le z_2 < 1 < a < z_3, \tag{8.35}
$$
 and z oscillates
periodically between $z_1$ and $z_2$. The molecule never gets entirely
in the ground state or entirely in the upper state. The solution z(t) is
a generalization of (8.27):
$$
\sqrt{\frac{z-z_1}{z_2-z_1}} = \text{sn}\left[\sqrt{\frac{z_3-z_1}{2}} \frac{\alpha t}{\hbar} + Q, \sqrt{\frac{z_2-z_1}{z_3-z_1}}\right] \tag{8.36}
$$
which again approaches a sinusoidal oscillation in the limit of many
quanta, $a \gg 1$.

For arbitrary values of z, the relative phase of the X and Y motions is
given by combining (8.34) with (8.24) and the conservation laws, with the
result
$$
\sin^2\Theta(z) = \frac{(z-z_1)(z-z_2)(z-z_3)}{(z+1)(z-1)(z-a)}. \tag{8.37}
$$

This reduces to the value $\Theta(z) = \pm 90^\circ$ as previously
noted, in the case c=a.

To summarize the above results, a close analysis of the semiclassical
theory for a simple special case reveals many unexpected and remarkable
features. It is usually supposed that the semiclassical theory of
radiation cannot account for spontaneous emission; indeed this belief
was historically one of the main reasons for introducing field
quantization. However, we see that when we take into account
simultaneously both the effect of the molecule on the field and the
effect of its radiated field reacting back on the molecule, we are led
to a nonlinear system of coupled equations whose solutions are readily
found, and which exhibit almost all the properties usually associated
with field quantization.

In the above analysis the semiclassical theory has been put to a far
more severe test than would be the case in practical maser calculations,
and it has met the test very well. Even in the case of field intensities
corresponding to one or two quanta, the semiclassical theory gives
solutions reproducing almost quantitatively everything that is found in
the quantum electrodynamics analysis. The characteristic times of
interaction processes turn out just the same. The "quantum jumps" are
still with us, but they now appear as perfectly continuous processes,
where an instability develops in the solution of the nonlinear equations
and an amount of energy $\hbar\omega$ is more or less rapidly
transferred between molecule and field.

The semiclassical analysis gives a very interesting description of the
process of spontaneous emission. Consider a large number of molecules, as
nearly as possible in the upper state. In practice, we cannot prepare
them exactly in the upper state, but there will be a certain probability
distribution of initial values of amplitude for the growing normal mode.
A molecule with an initial value $Y_+(0)$ will, at time t, have a Y
amplitude of
$$
Y_+(0) \exp\left(\frac{\alpha t}{\hbar}\right) = Y_+(t). \tag{8.38}
$$

 Let us
agree to say that when this reaches the value K, the molecule is
actively emitting energy. The, no matter what the probability
distribution of initial values, provided only that this distribution is
a continuous function in the neighborhood of the metastable state z=1,
we find that the number of molecules emitting at time t is proportional
to $\exp(-2\alpha t/\hbar)$. Thus, the "law of radioactive decay," or
"time-proportional transition probabilities" appears in this analysis
as a simple consequence of the existence of metastable states. The time
constant of the decay law is independent of the method of preparation of
the molecules, and depends only on the interaction constant with the
electromagnetic field. The situation is exactly like that of a large
number of pencils nearly perfectly balanced on their points. The time
required for any one pencil to fall over depends on how close it was to
vertical at time t=0. If the probability distribution of initial
states is continuous in the neighborhood of this metastable point, then
we have a decay law with a time constant which depends only on the laws
of mechanics, not on the method of preparation of initial states.
## CONCLUSION
The above analysis is evidently no more than a very preliminary survey
of the relations between different theories which might be used in
studying the ultimate limitations imposed by quantum theory on the noise
figure and frequency stability of molecular beam maser amplifiers and
oscillators. The limitation to a single molecule in the cavity is easily
removed in the semiclassical theory, but with more difficulty in the
quantum electrodynamics analysis. For example, the energy levels in the
case of two molecules present involve solution of a general cubic
equation, for three molecules we have a quartic equation, etc. Analyses
of the type given in Section 3, therefore, are quite impractical in the
case of a large number of molecules. However, the following reasoning
shows that there must be some as yet undiscovered way of circumventing
this complication.

Even though a complete theoretical discussion would require in principle
keeping track of perhaps $10^{10^{10}}$ different parameters, the
purpose of the theory is only to predict the values of three or four
quantities which are to be measured. Therefore, it must be that the
overwhelming majority of the microscopic parameters are irrelevant to the
particular predictions we are after. If this were not so, the
experimental measurements could not be reproducible, for when we repeat
an experiment, we surely do not repeat all the details of $10^{10^{10}}$
different parameters. In other words, a form of statistical mechanics
must be applicable, in which we calculate averages over all possible
microscopic conditions which conform to the knowledge we have of the
state of the system. Any quantity which emerges from this treatment with
a very sharply peaked probability distribution must have practically the
same value for each of the possible microscopic states, and this value
can be predicted with confidence without having to go into microscopic
details. Viewed in this way, the maser problem becomes one of the theory
of irreversible statistical mechanics, and this approach is now being
pursued.

The unexpected success of the semiclassical theory, on the other hand,
suggests that it may provide a much more efficient formalism for
handling such problems. The introduction of many molecules, cavity
losses, etc., is easily accomplished in this treatment, and the same
statistical considerations just mentioned apply equally well. There seem
to be excellent grounds for expecting that this extended semiclassical
theory would reproduce every feature of experimental significance which
could be found in the quantum electrodynamics analysis.

The relationships demonstrated here between quantum electrodynamics and
the semiclassical theory of radiation evidently carry implications far
beyond the field of maser theory. Almost any example of the interaction
of matter and radiation would seem to be tractable by these methods.
## REFERENCES
[^1]: E. Fermi, Rev. Mod. Phys. **4**, 131 (1932).
[^2]: J. C. Slater, *Microwave Electronics*, D. van Nostrand Co., Inc., N. Y. (1950), Chapter 4.
[^3]: D. K. Coles, et al., Phys. Rev. **82**, 877 (1951).
[^4]: This formalism is developed in more detail in the following paper: E. T. Jaynes, Phys. Rev. **108**, 171 (1957).
[^5]: A. Einstein, B. Podolsky, and N. Rosen, Phys. Rev. **47**, 777 (1935).
