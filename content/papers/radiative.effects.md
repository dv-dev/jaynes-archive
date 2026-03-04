---
title: "Radiative Effects in Semiclassical Theory"
author: ["M. D. Crisp", "E.T. Jaynes"]
year: 1969
abstract: >
  Unquantized field calculations are extended to include the effect of
  an atom's field acting back upon the atom. It is shown that, in the
  absence of an applied field, semiclassical theory predicts that an
  atom will decay spontaneously from an excited state with a
  characteristic time equal to the reciprocal of the Einstein A
  coefficient for the transition. The theory also predicts that the
  frequency of the light radiated during a transition will have a small
  time dependence. The corresponding frequency shifts are compared with
  the Lamb shift in hydrogen. The derived equations are used to study
  the response of a many-level atom to an applied, monochromatic field.
  In the case of a three-level system, it is predicted that optical
  nutations are not just limited to the resonant transition, but are
  also present in the fluorescence involving the other level.
---
## Introduction {#introduction .unnumbered}
CALCULATIONS with an unquantized electromagnetic field have proved
adequate to explain such quantum-electronic phenomena as photon
echoes,[^3] self-induced transparency,[^4] and optical nutation.[^5] It
is argued that a quantized field is not necessary for the understanding
of these effects because strong fields consisting of large numbers of
quanta are involved. The present paper investigates the consequences of
retaining a classical field in treating the problem of an atom
interacting with weak electromagnetic radiation. It is shown that the
phenomenon of the spontaneous decay of an atom can be obtained
semiclassically, provided one includes the effects upon the atom of
fields created by the atomic currents. These currents are assumed to be
equal to the probability current of the atomic electrons multiplied by
the electronic charge $e$. This assumption couples the Maxwell and
Schrödinger equations, and this paper is devoted to the solution and
interpretation of this set of simultaneous, nonlinear differential
equations.

Even though it is generally believed that a full quantum-electrodynamic
treatment is necessary in order to obtain all radiative effects
correctly, many calculations involving the interaction of radiation and
matter were first done without quantizing the electromagnetic field.
Thus in the case of the photoelectric effect,[^6] the scattering of
radiation from a free electron (Klein-Nishina formula),[^7] stimulated
emission and absorption of radiation by an atom,[^8] and vacuum
polarization,[^9] the correct predictions were first obtained by
semiclassical methods.

On the other hand, quantum electrodynamics has been applied to a much
wider range of phenomena with great success, in the sense that there is
as yet no clearcut evidence for any discrepancy between its predictions
and experiment. However, in spite of the labors of two generations of
theorists in improving the formulation of the theory and developing more
powerful methods of calculation, present quantum electrodynamics
contains many mathematical and logical difficulties. In almost every
calculation one encounters divergent and/or ambiguous integrals, which
must be disposed of by various devices. Thus, the infinite zero-point
energy is simply subtracted arbitrarily, some divergent expressions are
set equal to zero on grounds of relativistic invariance, others on
grounds of gauge invariance, and the order of some divergences is
reduced by the ad hoc device of regulators. The remaining divergences
are not really removed, but only concealed from view, by the devices of
mass and charge renormalization.

In some cases it is not yet clear whether the difficulty is due to a
defect in the formulation of the theory, or whether it arises merely
from inadequacies in our methods of calculation (i.e., perturbation
expansions in powers of $e^2$ may not \"exist\" in the analytical
sense). However, in some particularly simple cases \[such as the vacuum
expectation value of the current operator, $\langle J_\mu(x) \rangle$,
which is a violently divergent expression set equal to zero on grounds
of Lorentz invariance\], no real \"calculation\" is involved. Another
difficulty that cannot be attributed to inadequate methods of
calculation is the infinite vacuum fluctuations, and consequent infinite
zero-point energy, of the electromagnetic field. Indeed, at first glance
it seems remarkable that any finite results or reproducible effects
could emerge from
a theory based on point interactions to a field with infinite random
fluctuations.

Therefore, even though we have now learned how to manipulate the
divergences of quantum electrodynamics with enough art to extract
meaningful finite results, it seems undeniable that there are
fundamental defects in the basic formulation of the present theory; a
correctly formulated theory should not require additional *ad hoc*
devices in order to obtain physical predictions. Theorists are in quite
general agreement that some very deep modifications will be required in
quantum electrodynamics before we have the elusive \"future correct
theory\" of radiation phenomena. In what specific way, then, should the
present theory be changed? To this question we have as yet no answers,
and few suggestions.

Now semiclassical calculations are conspicuously free from many of the
divergence problems of quantum electrodynamics; the classical
electromagnetic field due to a finite and continuous current
distribution is everywhere finite and well behaved. As the list of
successful semiclassical calculations grows, the question arises whether
the necessary modification of quantum electrodynamics may lie in the
direction of the semiclassical approach. Any such change would, of
course, imply a revision of the physical ideas underlying the present
theory and would probably be as radical as the change which took place
in the interpretation of the Dirac equation in the transition from the
original one-electron Dirac theory to the hole theory.

For these reasons it is of interest to extend the list of semiclassical
calculations as far as possible. To date, it is generally thought that
the phenomena of blackbody radiation, spontaneous emission, and the Lamb
shift actually require the quantizing of the electromagnetic field. It
is the purpose of this paper to examine the possibilities of a
semiclassical theory of the last two, closely related, effects.

In a previous paper[^10] it was shown that, in the dipole approximation,
the expectation of the dipole moment $\langle\mu\rangle$ and the
expectation of the energy $\langle\mathcal{H}\rangle$ of a two-level
atom evolve according to
$$
\frac{d^2}{dt^2}\langle\mu\rangle + \Omega^2\langle\mu\rangle = -\frac{2\mu^2}{\hbar}\langle\mathcal{H}\rangle E(t),
$$
$$
\frac{d\langle\mathcal{H}\rangle}{dt} = E(t)\frac{d\langle\mu\rangle}{dt},
$$
where $E(t)$ is the electric field in the vicinity of the atom. If the
expectation of the dipole moment is interpreted as an actual dipole
moment, its oscillation will create electromagnetic fields and cause
energy to be radiated away from the atom.

In order to understand how the effects of spontaneous decay and
frequency shifts come about in semiclassical theory, consider the
following intuitive argument. It is shown in this paper that the
radiation field which reacts upon the atom consists of two components,
one in phase with the atomic currents and the other $90^\circ$ out of phase
\[see Eq. (9)\]. For a two-level atom in the dipole approximation, this
corresponds to assuming an electric field of the form
$$
E(t) = -K\frac{d^2}{dt^2}\langle\mu\rangle + \frac{2}{3c^3}\frac{d^3}{dt^3}\langle\mu\rangle,
$$
where the constant $K$ depends upon the detailed structure of the atom
and hence cannot be derived rigorously in the dipole limit. The second
term, $(2/3c^3)(d^3/dt^3)\langle\mu\rangle$, is the classical radiation
reaction field[^11] and is independent of the structural details of the
atom.

The field $E(t)$ is weak compared with $\hbar\Omega/\mu$, so that
$$
\frac{d^2}{dt^2}\langle\mu\rangle \approx -\Omega^2\langle\mu\rangle,
$$
and the field acting back upon the atom may be approximated by
$$
E(t) \approx \Omega^2 K \langle\mu\rangle - \frac{2\Omega^2}{3c^3}\frac{d}{dt}\langle\mu\rangle.
$$

Substituting this into the equation of motion of the dipole moment, one
obtains
$$
\frac{d^2}{dt^2}\langle\mu\rangle - \frac{8\mu^2\Omega^2}{3\hbar^2c^3}\langle\mathcal{H}\rangle \frac{d}{dt}\langle\mu\rangle + \Omega^2\left(1+\frac{4\mu^2}{\hbar^2}\langle\mathcal{H}\rangle K\right)\langle\mu\rangle=0.
$$

This equation resembles that of a damped harmonic oscillator with a
damping coefficient
$(-8/3)(\mu^2\Omega^2/\hbar^2c^3)\times\langle\mathcal{H}\rangle$ and a
shifted frequency
$\Omega[1+(4\mu^2/\hbar^2)\langle\mathcal{H}\rangle K]^{1/2}$. If the
atom is excited, $\langle\mathcal{H}\rangle$ is greater than zero and
the dipole moment grows spontaneously until $\langle\mathcal{H}\rangle$
becomes negative, at which time the dipole moment begins its decay to
zero. In this way a dipole's field reacting upon the dipole can give
rise to spontaneous decay and frequency shifts.
## Derivation of Basic Equations {#derivation-of-basic-equations .unnumbered}
Consider a nonrelativistic, spinless atom which is described by the
Hamiltonian 
$$
\mathcal{H} = \mathcal{H}_0 - V,
\tag{1}
$$
 where $\mathcal{H}_0$
is the Hamiltonian of the atomic system in the absence of
electromagnetic fields, and $V$ is the interaction term arising from the
presence of fields. To be specific, set 
$$
\begin{aligned}
\mathcal{H}_0 &= p^2/2m - e^2/r,  \\\\
V &= (e/mc)\mathbf{A}(\mathbf{x}, t) \cdot \mathbf{p}. 
\end{aligned}
\tag{2b}
$$

 The diamagnetic term
$(e^2/2mc^2)\mathbf{A}^2(\mathbf{x}, t)$ in $V$ has been
neglected because the fields treated in this paper are weak. \[The
magnitude of the vector potential $\mathbf{A}(\mathbf{x}, t)$ will be of
the order of $ea^2(mc/\hbar)$.\] Any state of the atomic system may be
expressed as 
$$
\Psi(\mathbf{x}, t) = \sum_j a_j(t) \psi_j(\mathbf{x}),
\tag{3}
$$
where $\psi_j(\mathbf{x})$ are eigenfunctions of $\mathcal{H}_0$, i.e.,
$$
\mathcal{H}_0\psi_j(\mathbf{x}) = E_j\psi_j(\mathbf{x}).
$$

 The
continuum states are not included in Eq. (3) because they are not
significantly excited by radiation of the optical frequencies treated
here.

It is assumed that an atom in the state $\Psi(\mathbf{x}, t)$ contains
charge currents which are given by
$$
\mathbf{J}(\mathbf{x}, t) = (e/m)\text{Re}[\Psi^*(\mathbf{x}, t)\mathbf{p}\Psi(\mathbf{x}, t)].
\tag{4}
$$

Again a higher-order term,
$(e^2/mc)[\mathbf{A}(\mathbf{x}, t)|\Psi(\mathbf{x}, t)|^2]$, has been
neglected because of the smallness of $\mathbf{A}(\mathbf{x}, t)$.
Substituting Eq. (3) in Eq. (4), one obtains
$$
\mathbf{J}(\mathbf{x}, t) = \sum_{\alpha,\beta} \frac{e\hbar}{2mi}[\sigma_{\beta\alpha}\psi_\alpha^*\nabla\psi_\beta - \sigma_{\alpha\beta}\psi_\alpha\nabla\psi_\beta^*],
\tag{5}
$$
where the density matrix elements in the Schrödinger picture,
$\sigma_{\beta\alpha}(t)$, are defined by
$$
\sigma_{\beta\alpha}(t) = a_\beta(t)a_\alpha^*(t),
\tag{6}
$$
 and evolve
according to
$$
i\hbar\dot{\sigma}_{lm} = \sum_j [\mathcal{H}_{lj}\sigma_{jm} - \sigma_{lj}\mathcal{H}_{jm}].
\tag{7}
$$

The atomic currents create a transverse[^12] vector potential which may
be written in the Coulomb gauge as
$$
\mathbf{A}(\mathbf{x}, t) = \frac{1}{c}\int \frac{\mathbf{J}_t(\mathbf{x}^\prime, t-|\mathbf{x}-\mathbf{x}^\prime|/c)}{|\mathbf{x}-\mathbf{x}^\prime|} d^3x^\prime + \mathbf{A}_0(\mathbf{x}, t),
\tag{8}
$$
where $\mathbf{J}_t(\mathbf{x},t)$ is the transverse component of the
current density, and the vector potential $\mathbf{A}_0(\mathbf{x},t)$
represents an externally applied field. In the calculations to follow,
both the source point $\mathbf{x}^\prime$, and the observation point
$\mathbf{x}$ are contained within the atom so that the retardation
$|\mathbf{x}-\mathbf{x}^\prime|/c$ is small compared with the period of
oscillation of $\mathbf{J}_t(\mathbf{x},t)$, and Eq. (8) can be
rewritten as
$$
\begin{aligned}
\mathbf{A}(\mathbf{x}, t) &= \frac{1}{c}\int \frac{\mathbf{J}_t(\mathbf{x}^\prime,t)}{|\mathbf{x}-\mathbf{x}^\prime|}d^3x^\prime \\
&\quad - \frac{1}{c^2}\frac{d}{dt}\int \mathbf{J}_t(\mathbf{x}^\prime,t)d^3x^\prime + \mathbf{A}_0(\mathbf{x},t)
\end{aligned}
\tag{9}
$$
in the vicinity of the atom. The expression of Eq. (5) may be used in
Eq. (9) with the aid of the following identities: 
$$
\begin{aligned}
\frac{1}{|\mathbf{x}-\mathbf{x}^\prime|} &= \frac{1}{2\pi^2}\int_0^\infty dk \int d\Omega\, e^{i\mathbf{k}\cdot(\mathbf{x}-\mathbf{x}^\prime)},  \\\\
\int \mathbf{J}_t(\mathbf{x}^\prime,t) e^{-i\mathbf{k}\cdot\mathbf{x}^\prime}d^3x^\prime &= -\frac{\mathbf{k}}{|\mathbf{k}|} \times \left[ \frac{\mathbf{k}}{|\mathbf{k}|} \times \int \mathbf{J}(\mathbf{x}^\prime,t) e^{-i\mathbf{k}\cdot\mathbf{x}^\prime} d^3x^\prime \right],  \\\\
\int \mathbf{J}_t(\mathbf{x}^\prime,t)d^3x^\prime &= \frac{2}{3} \int \mathbf{J}(\mathbf{x}^\prime,t)d^3x^\prime, 
\end{aligned}
\tag{10}
$$
 where the integral $\int d\Omega$ is over solid angle in
$\mathbf{k}$ space. One obtains 
$$
\begin{aligned}
\mathbf{A}(\mathbf{x}, t) &= \sum_{\alpha,\beta} \sigma_{\beta\alpha}(t) \left\{ \frac{-i e\hbar}{2\pi^2 mc} \int_0^\infty dk \int d\Omega \langle\alpha|e^{i\mathbf{k}\cdot\mathbf{x}}\nabla|\beta\rangle_\perp \right. \\\\
&\left. \qquad\qquad + \frac{2}{3} \frac{\Omega_{\alpha\beta}^2}{c^2} \boldsymbol{\mu}_{\alpha\beta} \right\} + \mathbf{A}_0(\mathbf{x},t)
\end{aligned}
\tag{11}
$$
 for the field which acts upon the atomic currents. The
definition
$$
\langle\alpha|e^{i\mathbf{k}\cdot\mathbf{x}}\nabla|\beta\rangle_\perp = -\frac{\mathbf{k}}{|\mathbf{k}|} \times \left[ \frac{\mathbf{k}}{|\mathbf{k}|} \times \langle\alpha|e^{i\mathbf{k}\cdot\mathbf{x}}\nabla|\beta\rangle \right]
$$
has been made.

The applied field will be assumed to be that of a monochromatic plane
wave of the form
$$
\mathbf{A}_0(\mathbf{x},t) = \frac{c\mathbf{E}_0}{\omega} \cos(\omega t - \mathbf{k}\cdot\mathbf{x}),
\tag{12}
$$
where $\omega$ is an optical frequency. Since at optical frequencies the
phase of $\mathbf{A}_0(\mathbf{x},t)$ does not vary significantly over
the volume of the atom, the dipole approximation is valid and the vector
potential may be evaluated at the center of the atom, i.e.,
$$
\mathbf{A}_0(0,t) = \frac{c\mathbf{E}_0}{\omega} \cos\omega t
\tag{13}
$$
 may be
used in Eq. (11).

Equations (11), (2b), and (1) may be used in Eq. (7) and, if the
nonresonant terms are neglected (the details of this calculation appear
in Appendix A), one obtains 
$$
\begin{aligned}
\dot{\sigma}_{lm} &= -i[\Omega_{lm} - \sum_j (\Gamma_{lj} - \Gamma_{jm})\sigma_{jj}(t)]\sigma_{lm}  \\\\
&\quad - [\sum_j(A_{lj}+A_{mj})\sigma_{jj}(t)]\sigma_{lm}  \\\\
&\quad - \frac{\mathbf{A}_0(0,t)}{\hbar c} \cdot \sum_j [\boldsymbol{\mu}_{lj}\sigma_{jm} - \sigma_{lj}\boldsymbol{\mu}_{jm}]. 
\end{aligned}
\tag{14}
$$
The frequency-shift coefficient is
$$
\begin{aligned}
\Gamma_{lj} &=
-\frac{1}{2\pi^2}\frac{e^2\hbar}{m^2c^2}\,\mathcal{P}\!\int_0^\infty dk \int d\Omega \\
&\quad \times
\left\langle l\middle|e^{i\mathbf{k}\cdot\mathbf{x}}\nabla\middle|j\right\rangle_\perp
\cdot
\left\langle j\middle|e^{-i\mathbf{k}\cdot\mathbf{x}}\nabla\middle|l\right\rangle_\perp \\
&\quad \times \frac{1}{|\mathbf{k}|c-\Omega_{lj}} .
\end{aligned}
\tag{15}
$$
The Einstein $A$ coefficients $A_{lj}$ are defined according to
$$
A_{lj} = \frac{4}{3}\frac{\Omega_{lj}^3}{\hbar c^3}\,\boldsymbol{\mu}_{lj}\cdot\boldsymbol{\mu}_{jl} = -A_{jl}.
\tag{16}
$$
The electric dipole moment matrix element $\boldsymbol{\mu}_{lj}$ and the transition frequencies $\Omega_{lj}$ are defined, respectively, as
$$
\begin{aligned}
\boldsymbol{\mu}_{lj} &= \int \psi_l^*(\mathbf{x})\,e\mathbf{x}\,\psi_j(\mathbf{x})\,d^3x, \\
\hbar\Omega_{lj} &= E_l - E_j.
\end{aligned}
\tag{17a,b}
$$
It is seen from Eq. (14) that the off-diagonal density matrix elements oscillate at frequencies $\Omega_{lm}+\delta\Omega_{lm}(t)$, where the time-dependent frequency shifts $\delta\Omega_{lm}(t)$ are given by
$$
\delta\Omega_{lm}(t) = -\sum_j(\Gamma_{lj}-\Gamma_{jm})\sigma_{jj}(t).
\tag{18}
$$
Now the expectation of the dipole moment of the atom is defined by
$$
\langle\mathbf{u}\rangle = \int \Psi^*(\mathbf{x},t)\,e\mathbf{x}\,\Psi(\mathbf{x},t)\,d^3x
$$
and, using Eq. (3), one can write
$$
\langle\mathbf{u}\rangle = \sum_{\alpha,\beta}\mathbf{u}_{\alpha\beta}\sigma_{\beta\alpha}(t).
$$
Thus the off-diagonal matrix elements are directly related to the expectation of the dipole moment. Since semiclassical theory assumes that the expectation of the dipole moment is responsible for radiation by the atom, Eq. (18) is a prediction of a frequency shift in the radiation emitted or absorbed by an atom. Such a frequency shift is a new phenomenon which has not appeared in other semiclassical calculations.

If a hydrogen atom were prepared in its ground state, $\sigma_{1s1s}$ would be equal to unity and all other $\sigma_{jj}$ would be zero. The quantity $\Gamma_{1s1s}$ is identically zero, so in this case Eq. (18) predicts that the hydrogen atom would respond resonantly to an applied field whose frequency is given by
$$
\omega = \Omega_{2p1s} - \Gamma_{1s2p}.
$$
This 1s-2p frequency shift $\Gamma_{1s2p}$ is calculated in Appendix B to be $0.285\ \mathrm{cm}^{-1}$.

Herzberg[^11] has determined the 1s-2p Lamb shift in deuterium by measuring the 1s-2p absorption line. The reported value is $0.262 \pm 0.038\ \mathrm{cm}^{-1}$. The comparison of other semiclassical frequency shifts with the corresponding Lamb-shift values is given in Table I. The values of $\Gamma_{lm}$ reported in the table have been corrected for the effect of vacuum polarization. The vacuum-polarization calculation, as first done by Uehling,[^7] uses an unquantized electromagnetic field and therefore can be fitted into the framework of this paper.

The agreement between the 1s-2p quantum-electrodynamic Lamb shift and the corresponding semiclassical frequency shift is surprisingly good when it is recalled that the semiclassical calculation corresponds to a two-level, spinless, nonrelativistic hydrogen atom. The other semiclassical frequency shifts agree in sign and order of magnitude with their quantum-electrodynamic counterparts.

| Transition | $\Gamma_{nm}/2\pi$ | $\delta\omega_{\mathrm{expt}}$ | $\delta\omega_{\mathrm{QED}}$ |
| --- | --- | --- | --- |
| 1s-2p | $0.278\ \mathrm{cm}^{-1}$ | $0.262 \pm 0.038\ \mathrm{cm}^{-1}$[^11] | $0.2726\ \mathrm{cm}^{-1}$ |
| 2s-2p | $657.20\ \mathrm{MHz}$ | $1057.77 \pm 0.10\ \mathrm{MHz}$[^21] | $1057.19\ \mathrm{MHz}$ |
| 3s-3p | $0.0027\ \mathrm{cm}^{-1}$ | $0.0083^{+0.002}_{-0.003}\ \mathrm{cm}^{-1}$[^22] | $0.0105\ \mathrm{cm}^{-1}$ |

Table I. Comparison of the semiclassical frequency shifts with the experimentally measured and quantum-electrodynamically calculated Lamb shift. Both the semiclassical and the quantum-electrodynamic calculations include the corrections for vacuum polarization.

![Figure 1. Energy-level diagram for a two-level atom.](/images/papers/radiative.effects_fig_1.png)
## Spontaneous Decay {#spontaneous-decay .unnumbered}
Equation (14) predicts that,[^14] in the absence of an applied field,
the diagonal matrix elements will decay according to
$$
\dot{\sigma}_{ll} = -\sum_j A_{lj} \sigma_{ll} \sigma_{jj}.
\tag{19}
$$

In the
case of a two-level system (see Fig. 1), these equations become
$$
\begin{aligned}
\dot{\sigma}_{22} &= -A_{21}\sigma_{22}\sigma_{11}, \\\\
\dot{\sigma}_{11} &= A_{21}\sigma_{22}\sigma_{11}.
\end{aligned}
\tag{20a}
$$

Adding these equations, one sees that probability is
conserved, i.e., 
$$
\sigma_{11} + \sigma_{22} = 1.
\tag{21}
$$

This constant of
motion allows one to integrate the equations and obtain
$$
\begin{aligned}
\sigma_{22} &= 1/(e^{A_{21}(t-t_0)}+1),  \\\\
\sigma_{11} &= 1/(e^{-A_{21}(t-t_0)}+1). 
\end{aligned}
$$

The constant of integration $t_0$ is determined by the initial state of
the atom. From this solution it follows that the expectation of the
energy evolves in time according to
$$
\langle \mathcal{H}_0 \rangle = \tfrac{1}{2}\Omega_{21}(\sigma_{22}-\sigma_{11}) = -\tfrac{1}{2}\Omega_{21}\tanh[\tfrac{1}{2}A_{21}(t-t_0)].
$$

According to Eq. (14), when $\mathbf{A}_0(0,t)$ is zero, the
off-diagonal matrix element satisfies 
$$
\begin{aligned}
\dot{\sigma}_{21} &= -i\{\Omega_{21}-\Gamma_{12}\tanh[\tfrac{1}{2}A_{21}(t-t_0)]\}\sigma_{21} \\\\
&\quad -\{\tfrac{1}{2}A_{21}\tanh[\tfrac{1}{2}A_{21}(t-t_0)]\}\sigma_{21}.
\end{aligned}
$$

Integrating this, it is seen that the expectation of the
dipole moment varies according to
$$
\begin{aligned}
\langle\boldsymbol{\mu}\rangle &= \boldsymbol{\mu}_{12}(\sigma_{12}+\sigma_{21}) \\
&= \boldsymbol{\mu}_{12} \text{sech}[\tfrac{1}{2}A_{21}(t-t_0)] \times \cos[\Omega_{21}t+\theta(t)],
\end{aligned}
\tag{22}
$$
where $\theta(t)$ is defined by
$$
\theta(t) = \theta_0 - (2\Gamma_{12}/A_{21})\ln\{\cosh[\tfrac{1}{2}A_{21}(t-t_0)]\}
$$
and corresponds to a time-dependent frequency shift given by
$$
\delta\Omega_{21}(t) = d\theta/dt = -\Gamma_{12}\tanh[\tfrac{1}{2}A_{21}(t-t_0)].
$$

Graphs of the expectation of the energy and the envelope of the dipole
moment are shown in Fig. 2.

It should be noted that Eq. (20a) predicts a non-exponential decay for
an atom in its excited state. This corresponds to a fundamental
difference between semiclassical theory and quantum electrodynamics. In
semiclassical theory it is assumed that the expectation of the dipole
moment of the atom is responsible for radiation, and hence an excited
atom radiates slowly until its dipole moment grows to an appreciable
magnitude (see Fig. 2). In quantum electrodynamics, the probability that
a given atom radiates is largest immediately after the atom is excited.
The semiclassical decay does go asymptotically into an exponential decay
as $t-t_0$ becomes large.
![Figure 2. (a) Decay of the expectation of the energy of the two-level atom in absence of applied fields. Time is in units of $A_{21}^{-1}$, where $A_{21}$ is the Einstein A coefficient for the atom. (b) Evolution of the envelope of the expectation of the dipole moment for the two-level atom.](/images/papers/radiative.effects_fig_2.png)

In the case of a three-level system with transitions allowed between
adjacent levels (see Fig. 3), Eq. (19) becomes 
$$
\dot{\sigma}_{33} = -A_{32}\sigma_{33}\sigma_{22},
\tag{24a}
$$

$$
\dot{\sigma}_{22} = A_{32}\sigma_{33}\sigma_{22} - A_{21}\sigma_{22}\sigma_{11},
\tag{24b}
$$

$$
\dot{\sigma}_{11} = A_{21}\sigma_{22}\sigma_{11}.
\tag{24c}
$$

Addition of these equations shows that they are
consistent with conservation of probability, i.e.,
$$
\sigma_{11} + \sigma_{22} + \sigma_{33} = 1.
\tag{25}
$$
![Figure 3. Energy-level diagram for a three-level system. Transitions are allowed between adjacent levels.](/images/papers/radiative.effects_fig_3.png)

Dividing Eq. (24a) by Eq. (24c), it follows that
$$
\dot{\sigma}_{33}/A_{32}\sigma_{33} = -\dot{\sigma}_{11}/A_{21}\sigma_{11}
$$
or 
$$
[\sigma_{33}(t)]^{A_{21}/A_{32}} \sigma_{11}(t) = \alpha_0,
\tag{26}
$$
where
$\alpha_0$ is a constant of integration. The constant of motion of Eq.
(26) is of a new type, not found in conventional theory. It has the
effect of preventing the system from completely decaying to its ground
state. Thus Eq. (26) predicts that the third level should be
\"conditionally metastable\"; i.e., in the absence of external
perturbations it can retain a nonzero amplitude indefinitely. In such a
state, however, the slightest perturbation will cause the decay to
resume.

The constants of motion given in Eqs. (25) and (26) are sufficient to
allow integration of the equations, and one obtains 
$$
\int \frac{d\sigma_{33}}{\sigma_{33}(1-\alpha_0 \sigma_{33}^{-r}-\sigma_{33})} = -A_{32}t + \text{const},
\tag{27a}
$$

$$
\int \frac{d\sigma_{11}}{\sigma_{11}(1-\alpha_0^{1/r}\sigma_{11}^{1-1/r}-\sigma_{11})} = A_{21}t + \text{const},
\tag{27b}
$$

$$
\sigma_{22} = 1 - \sigma_{11} - \sigma_{33},
\tag{27c}
$$
 where the parameter $r$ is defined according to
$$
r = A_{21}/A_{32}.
$$

Equations (27a) and (27b) have been integrated
for the case $r=1$, that is, when the two Einstein A coefficients are
equal. It follows from this solution that the expectation of the energy
of the atom, which is given by
$$
\langle \mathcal{H}_0 \rangle = E_1\sigma_{11}(t) + E_2\sigma_{22}(t) + E_3\sigma_{33}(t),
$$
evolves in time according to
$$
\begin{aligned}
\langle \mathcal{H}_0 \rangle
&= \tfrac{1}{2}(E_1+E_3) \\
&\quad - (1-2\alpha_0)^{1/2}\{
\tfrac{1}{2}\Omega_{32}\tanh[(1-2\alpha_0)^{1/2} A(t-t_3)] \\
&\qquad\qquad + \tfrac{1}{2}\Omega_{21}\tanh[(1-2\alpha_0)^{1/2} A(t-t_1)]
\},
\end{aligned}
$$
where $A$ is the Einstein A coefficient for the system. Further
calculation reveals that the expectation of the dipole moment consists
of two components, one oscillating at the frequency $\Omega_{32}$ and
the other at the frequency $\Omega_{21}$. Both components are modulated
by hyperbolic secant envelopes. Graphs of the energy and the two
components of the dipole moment are shown in Fig. 4.
![Figure 4. (a) Decay of the expectation of the energy of a three-level system. The Einstein A coefficients $A_{21}$ and $A_{32}$ are chosen to be equal. Time is in units of $A^{-1}$, where $A = A_{21} = A_{32}$. (b) Component of the envelope of the expectation of the dipole moment which oscillates at $\Omega_{32}$. (c) Component of the envelope of the expectation of the dipole moment which oscillates at $\Omega_{21}$.](/images/papers/radiative.effects_fig_4.png)

The solutions of Eqs. (24a)-(24c) have been studied on an analog computer[^15]
in the case where $A_{21} \neq A_{32}$. Typical solutions are
illustrated in Figs. 5 and 6. Figure 5 shows the cascading of the atom's
energy down to the ground state, each transition of the atom being
accompanied by the appearance of a dipole moment which oscillates at the
transition frequency. Figure 6 illustrates the case in which the second
level is short lived compared to the third ($A_{21} \gg A_{32}$). It is
seen that the 3-2 dipole moment starts out looking somewhat like a
hyperbolic secant, but then the fast 2-1 transition occurs and causes
the truncation of the 3-2 dipole moment. Physically this \"quenching\"
of the 3-2 dipole moment results in a broadening of the corresponding
spectral line which would be qualitatively similar to the lifetime
broadening which was first predicted quantum-electrodynamically by
Weisskopf and Wigner.[^16]

![Figure 5. (a) Cascading of the expectation of the energy of a three-level atom with $A_{32} = 4A_{21}$. Time is measured in units of $A_{21}^{-1}$. (b) Envelope of the expectation of the component of the dipole moment which oscillates at $\Omega_{32}$. (c) Envelope of the expectation of the component of the dipole moment that oscillates at $\Omega_{21}$.](/images/papers/radiative.effects_fig_5.png)

![Figure 6. (a) Envelope of the 3-2 dipole moment. (b) Envelope of the 2-1 dipole moment.](/images/papers/radiative.effects_fig_6.png)

## Inclusion of an Applied Field {#inclusion-of-an-applied-field .unnumbered}
Now consider the basic Eq. (14), including the applied field given by
Eq. (13). When the applied field is tuned in frequency so that it is in
near resonance with a pair of levels $a$ and $b$, i.e.,
$\omega \approx \Omega_{ab}$, Eq. (14), as shown in Appendix A, becomes
$$
\begin{aligned}
\dot{\sigma}_{lm} &= -i[\Omega_{lm} - \sum_j(\Gamma_{lj}-\Gamma_{jm})\sigma_{jj}(t)]\sigma_{lm} \\\\
&\quad - \tfrac{1}{2}\sum_j(A_{lj}+A_{mj})\sigma_{jj}\sigma_{lm} + \tfrac{1}{2}\epsilon_{ba}\sigma_{am}e^{i\omega t}\delta_{l,b} \\\\
&\quad - \tfrac{1}{2}\epsilon_{ab}\sigma_{bm}e^{-i\omega t}\delta_{l,a} - \tfrac{1}{2}\epsilon_{ba}\sigma_{lb}e^{i\omega t}\delta_{m,a} \\\\
&\quad + \tfrac{1}{2}\epsilon_{ab}\sigma_{la}e^{-i\omega t}\delta_{m,b},
\end{aligned}
\tag{28}
$$
when only resonant terms are retained. Define
$$
\epsilon_{lm} = \frac{\Omega_{lm}}{\omega} \frac{\boldsymbol{\mu}_{lm} \cdot \mathbf{E}_0}{\hbar}
$$
The following change of variables[^17]
$$
\begin{aligned}
x &= \tfrac{1}{2}(e^{i\omega t}\sigma_{ab} + e^{-i\omega t}\sigma_{ba}),  \\\\
z &= \sigma_{aa} - \sigma_{bb}, 
\end{aligned}
$$ 
can be used along with the definitions 
$$
\begin{aligned}
\epsilon_2 &= \epsilon_a + i\epsilon_b = \epsilon_{ab}, \\\\
\Delta &= \Omega_{ab} - \omega.
\end{aligned}
$$

It follows from Eq. (28) that the variables $x$, $y$,
and $z$ evolve according to 
$$
\begin{aligned}
\dot{x} &= \epsilon_2 z -(\Delta - \sum_j (\Gamma_{aj}-\Gamma_{bj})\sigma_{jj})y \\\\
&\quad -\sum_j (\tfrac{1}{2}A_{aj}+\tfrac{1}{2}A_{bj})\sigma_{jj}x,  \\\\
\dot{y} &= -(\Delta - \sum_j (\Gamma_{aj}-\Gamma_{bj})\sigma_{jj})x - \epsilon_1 z  \\\\
&\quad -\sum_j (\tfrac{1}{2}A_{aj}+\tfrac{1}{2}A_{bj})\sigma_{jj}y,  \\\\
\dot{z} &= \epsilon_1 y - \epsilon_2 x - \sum_j (A_{aj}\sigma_{aa}-A_{bj}\sigma_{bb})\sigma_{jj}, 
\end{aligned}
\tag{30}
$$
and when $l$ is not equal to $a$ or $b$,
$$
\dot{\sigma}_{ll} = - \sum_j A_{lj}\sigma_{ll}\sigma_{jj}. 
$$

The variables $x$, $y$, and $z$ satisfy the relation
$$
x^2 + y^2 + z^2 = (1-\sum_{j\neq a,b}\sigma_{jj})^2;
$$
therefore, a
solution of Eqs. (30) is confined to the surface of a sphere whose
time-dependent radius is
$$
R_{ab} = 1 - \sum_{j\neq a,b}\sigma_{jj}(t).
$$

The component of the
dipole moment which oscillates at the frequency
$\omega \approx \Omega_{ab}$ is given by
$$
\mathbf{u}_{ab}(\sigma_a + \sigma_b + \sigma_a) = \mathbf{u}_{ab}(x\cos\omega t - y\sin\omega t).
$$

Thus $\mathbf{u}_{ab}(t)$ should be interpreted as the component of the
dipole moment which oscillates in phase with the applied vector
potential \[see Eq. (13)\], and $-\mathbf{u}_{ab}y(t)$ as the component
which is 90º behind.

For the case of a two-level system, Eqs. (30) may be written,
respectively, as 
$$
\begin{aligned}
\dot{x} &= \epsilon z-[\Delta+\Gamma_{12}z]y+\tfrac{1}{2}A_{21}xz, \\\\
\dot{y} &= [\Delta+\Gamma_{12}z]x+\tfrac{1}{2}A_{21}yz, \\\\
\dot{z} &= -\epsilon x - \tfrac{1}{2}A_{21}(1-z^2).
\end{aligned}
\tag{31}
$$

As indicated above, the wave functions have been chosen
real so that $\epsilon_1$ is zero and $\epsilon_2$ is written as
$\epsilon$. A detailed study of the solutions of these nonlinear
differential equations will be the subject of a future publication.[^18]
In the case of exact resonance $\Delta=0$, there are two distinct types
of solutions of Eqs. (31), depending upon whether the applied field
strength $\epsilon_0$ is greater or less than the critical field $E_c$.
For applied field strengths less than that of the critical field, the
system point attains a stationary point on the unit sphere. Physically
this corresponds to the atom's dipole moment maintaining a constant
phase relation with respect to the applied field and scattering light
coherently. For applied fields greater than the critical field, the
solutions are oscillatory; the system point moves in an orbit on the
sphere. Physically this corresponds to the atom's absorbing and emitting
radiation with a constant phase relation maintained between the applied
field and the dipole moment. The critical field strength is given by
$$
E_c = \hbar/\boldsymbol{\mu}_{12} [(\frac{1}{2}A_{21})^2 + \Gamma_{12}^2]^{1/2}.
$$

It is seen from Table I that the frequency shifts $\Gamma_{ab}$ decrease
rapidly with increasing quantum number. It is of interest, therefore, to
seek solutions of Eqs. (30) when the $\Gamma_{ij}$ are neglected. These
equations would be expected to give a fair description of alkali atoms
such as sodium and potassium.

If one neglects the $\Gamma_{ij}$ and applies the field nearly in
resonance with the upper two levels, Eqs. (30) become 
$$
\begin{aligned}
\dot{x} &= \epsilon z - \Delta y + \tfrac{1}{2}(A_{32}z-A_{21}\sigma_{11})x, \\\\
\dot{y} &= \Delta x + \tfrac{1}{2}(A_{32}z-A_{21}\sigma_{11})y, \\\\
\dot{z} &= -\epsilon x - \tfrac{1}{2}A_{32}[(1-\sigma_{11})^2-z^2] \\\\
&\quad + \tfrac{1}{2}A_{21}\sigma_{11}(1-\sigma_{11}-z),  \\\\
\dot{\sigma}_{11} &= \tfrac{1}{2}A_{21}\sigma_{11}(1-\sigma_{11}-z).
\end{aligned}
\tag{32}
$$

An analytic solution of these equations has been found
in the case of exact resonance $\Delta=0$ and for a strong applied field, $\epsilon \gg A_{21}$ and $A_{32}$.[^19]
The derivation of Eq. (28) outlined in Appendix A tacitly contains the
assumption that $\Omega \gg \epsilon$, where $\Omega$ represents the
smallest optical frequency of the atom. Therefore, the solution below
is valid within the range $A_{21}, A_{32} \ll \epsilon \ll \Omega_{32}, \Omega_{21}$. In this range the variables $y$, $\sigma_{11}$, and $X \equiv (x+iz)e^{i\epsilon t}$ are slowly varying when compared with $e^{i\epsilon t}$, and the result of neglecting the rapidly oscillating terms is the solution
$$
x(t) = \frac{2B \cos(\epsilon t + \theta_0)}{e^{\frac{1}{2}A_{21}(t-t_0)}+1},
\tag{33a}
$$

$$
y(t) = \frac{2y(t_0)}{e^{\frac{1}{2}A_{21}(t-t_0)}+1},
\tag{33b}
$$

$$
z(t) = \frac{-2B \sin(\epsilon t + \theta_0)}{e^{\frac{1}{2}A_{21}(t-t_0)}+1},
\tag{33c}
$$
 where $B, \theta_0$, and $t_0$ are constants determined
by the initial conditions. Geometrically, this solution corresponds to a
system point rotating at angular rate $\epsilon$ about the $y$ axis,
while the radius of the sphere decreases slowly according to
$$
R_{32}(t) = (e^{\frac{1}{2}A_{21}(t-t_0)}+1)^{-1}.
$$

Further
calculation shows that Eqs. (33a) and (33b) are components of a dipole
moment given by 
$$
\begin{aligned}
\langle\boldsymbol{\mu}\rangle &= 2\boldsymbol{\mu}_{32}/[e^{\frac{1}{2}A_{21}(t-t_0)}+1] \\\\
&\quad \times[B \cos(\epsilon t+\theta_0)\cos\Omega_{32}t - y(t_0)\sin\Omega_{32}t] \\\\
&\quad + 2\boldsymbol{\mu}_{21}\text{sech}[\tfrac{1}{2}A_{21}(t-t_0)][C_1 \cos(\tfrac{1}{2}\epsilon t+\theta_1)\cos\Omega_{21}t \\\\
&\quad - C_2 \cos(\tfrac{1}{2}\epsilon t+\theta_2)\sin\Omega_{21}t],
\end{aligned}
$$
 where $C_1, C_2, \theta_1,$ and $\theta_2$ are
constants. It can be seen that the component dipole moment oscillating
at frequency $\Omega_{32}$ is amplitude modulated at frequency
$\epsilon$, while the component oscillating at $\Omega_{21}$ is
amplitude modulated at frequency $\epsilon/2$. A comparison of the 2-1
component of the dipole moment with Eq. (22) shows that the application
of the saturating field to the 3-2 transition causes a narrowing of the
2-1 fluorescence by a factor of $\frac{1}{2}$.
![Figure 7. Response of a three-level atom to a field applied at frequency $\omega = \Omega_{32} - 4A_{21}$ and with a strength of $\epsilon = A_{21}$. Time is in units of $A_{21}^{-1}$.](/images/papers/radiative.effects_fig_7.png)

More complete solutions of Eqs. (32) have been computed on an analog
computer. Figure 7 shows the response of a three-level system in the
case where $\omega\approx\Omega_{32}$, and Fig. 8 shows the response of
the same system to a field with $\omega\approx\Omega_{21}$.
![Figure 8. Response of a three-level atom to a field applied with $\omega = \Omega_{21} - A_{32}$ and of strength $\epsilon = 2A_{32}$. Time is in units of $A_{32}^{-1}$.](/images/papers/radiative.effects_fig_8.png)

## Appendix A {#appendix-a .unnumbered}
The density matrix elements in the interaction picture are defined
according to 
$$
\rho_{lm}(t) = \sigma_{lm}(t) e^{i\Omega_{lm}t},
\tag{A1}
$$
 and
will be used to identify the rapidly oscillating terms. Substituting Eq.
(11) into Eq. (7), one obtains 
$$
\begin{aligned}
\dot{\rho}_{lm} &= -\sum_{\alpha,\beta,j} \sum_j [\tfrac{1}{2}A_{lj}^{\beta\alpha} - i\Gamma_{lj}^{\beta\alpha}]\rho_{\beta\alpha}\rho_{jm} e^{i(\Omega_{lj}+\Omega_{\alpha\beta})t}  \\\\
&\quad - \rho_{lj}\rho_{\beta\alpha}(\tfrac{1}{2}A_{jm}^{\beta\alpha} - i\Gamma_{jm}^{\beta\alpha}) e^{i(\Omega_{lm}+\Omega_{\alpha\beta})t}]  \\\\
&\quad - \frac{\mathbf{A}_0(0,t)}{\hbar c} \cdot \sum_j [\boldsymbol{\mu}_{lj}\rho_{jm}e^{i\Omega_{lj}t} - \rho_{lj}\boldsymbol{\mu}_{jm}e^{i\Omega_{jm}t}],
\end{aligned}
\tag{A2}
$$
where the definitions
$$
A_{lj}^{\beta\alpha} = \frac{4}{3} \frac{\boldsymbol{\mu}_{\alpha\beta}\cdot\boldsymbol{\mu}_{lj}}{\hbar c^3} \Omega_{\alpha\beta}^2\Omega_{lj}
\tag{A3}
$$
and
$$
\begin{aligned}
\Gamma_{lj}^{\beta\alpha} &= \frac{1}{2\pi^2}\frac{e^2\hbar}{m^2c^2} \int_0^\infty dk \int d\Omega_k \\
&\quad \times \frac{\langle\alpha|e^{-i\mathbf{k}\cdot\mathbf{x}}|\beta\rangle_1 \cdot \langle l |e^{i\mathbf{k}\cdot\mathbf{x}}|j\rangle_1}{|k|}
\end{aligned}
\tag{A4}
$$
has been made.

The terms on the right-hand side of Eq. (A2) will be rapidly oscillating
unless the argument of the exponential is zero. For example, in order
for the term containing $\exp[i(\Omega_{lj}+\Omega_{\alpha\beta})t]$ to
contribute significantly to $\dot{\rho}_{lm}$, it is necessary that
$\alpha=j$ and $\beta=l$. The sums over $\alpha$ and $\beta$ can be
eliminated by repeated use of this argument, and with the observation
that 
$$
\rho_{lj}\rho_{jm} = \rho_{lm}\rho_{jj},
$$

Eq. (A2) leads to Eq. (14).[^20]

The applied field term in Eq. (A2) may be written as 
$$
\begin{aligned}
-&\frac{E_0}{\hbar\omega} \sum_j [\Omega_{lj}\boldsymbol{\mu}_{lj}\rho_{jm}e^{i\Omega_{lj}t}(\tfrac{1}{2}(e^{i\omega t}+e^{-i\omega t}))  \\\\
&- \rho_{lj}\Omega_{jm}\boldsymbol{\mu}_{jm}e^{i\Omega_{lm}t}(\tfrac{1}{2}(e^{i\omega t}+e^{-i\omega t}))]
\end{aligned}
\tag{A5}
$$
 when Eq. (13) is used for $\mathbf{A}_0(0,t)$. Under the
assumption that $\omega\approx\Omega_{as}$, it is easy to pick out the
resonant terms of the form $\exp[\pm i(\Omega_{ab}-\omega)t]$ in Eq.
(A5). The non-resonant terms in Eq. (A5) will be neglected. The result,
when substituted into Eq. (A2) and rewritten in the Schrödinger picture,
is given by Eq. (28).
## Appendix B {#appendix-b .unnumbered}
According to Eq. (18) and definition (15), the frequency shift in the
1s-2p absorption line of hydrogen would be
$$
\begin{aligned}
\delta\Omega_{2p01s}
&= \frac{1}{2\pi^2}\frac{e^2\hbar}{m^2c^2}
\int_0^\infty dk \int d\Omega \\
&\quad \times
\langle 2p_0|e^{i\mathbf{k}\cdot\mathbf{x}}\nabla|1s\rangle_\perp
\cdot
\langle 1s|e^{-i\mathbf{k}\cdot\mathbf{x}}\nabla|2p_0\rangle_\perp .
\end{aligned}
\tag{B1}
$$

Using 
$$
\begin{aligned}
\psi_{1s}(\mathbf{x}) &= 1/(\pi a^3)^{1/2} e^{-r/a}, \\\\
\psi_{2p0}(\mathbf{x}) &= 1/(32\pi a^3)^{1/2} (z/a) e^{-r/2a},
\end{aligned}
$$
 it follows that 
$$
\begin{aligned}
\langle 2p_0|e^{i\mathbf{k}\cdot\mathbf{x}}\nabla|1s\rangle_\perp &= -\frac{\mathbf{k}}{|\mathbf{k}|} \times \left[ \frac{\mathbf{k}}{|\mathbf{k}|} \times \langle 2p_0|e^{i\mathbf{k}\cdot\mathbf{x}}\nabla|1s\rangle \right] \\\\
&= \frac{\sqrt{2}(\mathbf{k}/|\mathbf{k}|)\times[(\mathbf{k}/|\mathbf{k}|)\times\hat{e}_z]}{a^5[k^2+(3/2a)^2]^2}
\end{aligned}
$$
 and
$$
\langle 1s|e^{-i\mathbf{k}\cdot\mathbf{x}}\nabla|2p_0\rangle_\perp = -\langle 2p_0|e^{i\mathbf{k}\cdot\mathbf{x}}\nabla|1s\rangle_\perp,
$$
and Eq. (B1) becomes
$$
\begin{aligned}
\delta\Omega_{2p01s}
&= \frac{1}{2\pi^2}\frac{e^2\hbar}{m^2c^2}\frac{2}{a^{10}}
\int_0^\infty \frac{dk}{[k^2+(3/2a)^2]^4} \\
&\quad \times
\int \left[
-\frac{\mathbf{k}}{|\mathbf{k}|}
\times
\left(
\frac{\mathbf{k}}{|\mathbf{k}|}\times\hat{e}_3
\right)
\right]^2 d\Omega .
\end{aligned}
\tag{B2}
$$
where the vector $\hat{e}_3$ is a unit vector along the $k_3$ axis.
Integrating Eq. (B2) gives
$$
\delta\Omega_{2p01s} = -\frac{5\times 2^5}{3^8}\frac{e^2\hbar}{m^2c^2}\frac{1}{a^3} = -\frac{160}{6561}\alpha \left(\frac{mc^2}{\hbar}\right).
$$

It should be noted that for fields stronger than the critical field (50
V/cm in hydrogen), Eq. (18) predicts that $\delta\Omega_{2p01s}$ should
vary with the applied field strength. The fields involved in Herzberg's
experiment were much less than this.

[^1]: This paper is based on a thesis submitted to Washington University
    in partial fulfillment of the requirements for the Ph.D. degree.
[^2]: Work supported in part by the Joint Services Electronics Program
    under Contract No. DA-28-043 AMC-00099(E).

[^3]: N. A. Kurnit, I. D. Abella, and S. R. Hartmann, Phys. Rev. Letters
    **13**, 567 (1964).

[^4]: S. L. McCall and E. L. Hahn, Phys. Rev. Letters **18**, 908
    (1967).

[^5]: G. B. Hocker and C. L. Tang, Phys. Rev. Letters **21**, 591
    (1968).

[^6]: G. Wentzel, Z. Physik **41**, 828 (1927).
[^7]: O. Klein and Y. Nishina, Z. Physik **52**, 853 (1929).
[^8]: O. Klein, Z. Physik **41**, 407 (1927).
[^9]: E. A. Uehling, Phys. Rev. **48**, 55 (1935).
[^10]: E. T. Jaynes and F. W. Cummings, Proc. IEEE **51**, 89 (1963).
[^11]: L. D. Landau and E. M. Lifshitz, *The Classical Theory of Fields*
    (Addison-Wesley Publishing Co., Inc., Reading, Mass., 1962), 2nd
    ed., Eq. (75.4).

[^12]: It is assumed that the atomic electrons do not see their
    longitudinal self-fields.

[^13]: H. A. Bethe, Phys. Rev. **72**, 339 (1947).
[^14]: In the following sections, the atomic eigenfunctions $\psi_j(\mathbf{x})$
    will be chosen to be real. This implies that the dipole moment
    matrix elements $\boldsymbol{\mu}_{ij}$ are real. The frequency
    shifts $\Gamma_{ij}$ have been chosen to be zero in order to result
    in considerable simplification of the equations.

[^15]: These computations were supported by the Washington University
    computing facilities through National Science Foundation Grant No.
    G-22296.

[^16]: V. Weisskopf and E. Wigner, Z. Physik **63**, 73 (1930).
[^17]: R. P. Feynman, F. Vernon, and R. Hellwarth, J. Appl. Phys.
    **28**, 49 (1957).

[^18]: A salient feature of these equations is the existence of the
    \"critical field.\"

[^19]: C. Stroud (private communication).
[^20]: Caution must be exercised in the case where there are more than
    one set of $\alpha$, $\beta$ such that
    $\Omega_{\alpha\beta}=\Omega_{jl}$. For example, the first four
    levels of a spinless hydrogen atom (1s, 2p$\pm$1,
    2p0) exhibit a frequency degeneracy
    $\Omega_{2p+1,1s}=\Omega_{2p0,1s}$. In cases such as this, however,
    $A_{lj}^{\beta\alpha}$ and $\Gamma_{lj}^{\beta\alpha}$ are zero
    unless $\alpha=j$ and $\beta=l$, so that this system is also
    described by Eq. (14).
[^21]: S. Triebwasser, E. S. Dayhoff, and W. E. Lamb, Phys. Rev.
    **89**, 98 (1953).
[^22]: G. W. Series, Proc. Roy. Soc. (London) **A208**, 277 (1951).
