---
title: "The Maser as a Parametric Amplifier"
year: 1960
abstract: >
  Jaynes explores the mathematical analogy between masers and classical
  parametric amplifiers. He demonstrates that the Schrödinger equation
  describing a quantum-mechanical system (like a molecule in a maser)
  interacting with an electromagnetic field can be recast in the form of
  classical Hamiltonian equations for an assemblage of harmonic oscillators.
  This analogy shows that the conservation of probability in quantum theory
  corresponds to the conservation of action in classical parametric systems,
  suggesting that many maser-like functions can be achieved through purely
  classical parametric mechanisms.
author: ["E.T. Jaynes"]
categories: ["Electrodynamics & Signal Processing"]
tags: ["maser", "parametric amplifier", "Schrödinger equation", "Hamiltonian mechanics", "adiabatic theorem", "Manley-Rowe equations", "quantum-classical analogy"]
---
## THE MASER AS A PARAMETRIC AMPLIFIER
MANY PEOPLE have noted an amusing similarity between the maser and the
parametric amplifier, whose behavior is also governed by
"pseudo-quantum" laws, such as the Manley-Rowe equations, reminiscent of
$E = \hbar\omega$. Relations giving a proportionality between energy and
frequency have a long history in physics, and are characteristic of many
purely classical systems. The best-known example is the adiabatic
theorem, which played an important role in the early development of
quantum theory. One finds that in any classical periodic system, the
action integral over one period is an approximate invariant under slowly
varying perturbations. The derivation of this law is particularly simple
in the case of a harmonic oscillator with slowly varying spring
constant. Here the oscillator coordinate satisfies the equation of
motion $\ddot{x} + \omega^2 x = 0$. If now we allow $\omega$ to be a
slowly varying function of time, the BWK approximation to the solution
is

$$x(t) = \frac{1}{\sqrt{\omega}} \exp\left[i \int \omega(t) dt\right] \tag{1}$$

and so the energy is

$$E = \frac{1}{2} m \dot{x}^2 + \frac{1}{2} m \omega^2 x^2 = (\text{const.}) (\omega). \tag{2}$$

This adiabatic theorem has recently found several applications, ranging
from a simple derivation of the Slater perturbation formula in microwave
theory to the calculation of orbits in particle accelerators.

Now consider a quantum-mechanical system such as a molecule in a maser,
interacting with an electromagnetic field. We wish to show that the
Schrödinger equation describing the time-evolution of this system has a
close mathematical analogy to classical parametric systems, and in fact
discloses a particular form of classical Hamiltonian for which the action
conservation law becomes rigorous, independently of the magnitude or rate
of change of the perturbations. Let the stationary state vectors of the
quantum-mechanical system be $u_n$ for the energy levels $E_n = \hbar\omega_n$,
and expand the time-dependent wave function in the usual way,

$$\psi(t) = \sum_n a_n(t) u_n. \tag{3}$$

The equations of motion are then

$$i\hbar\dot{a}_m = \sum_n H_{mn} a_n = E_m a_m + \sum_n V_{mn}(t) a_n \tag{4}$$

where $V_{mn}(t)$ are the matrix elements of the interaction with
fields, for example the product of dipole moment operator with electric
field E(t). By introducing the quadratic form which represents the
expectation value of the energy,

$$H = \sum_{mn} H_{mn} a_m^* a_n \tag{5}$$

we
can write the equations of motion in a form resembling the classical
Hamiltonian equations:

$$\begin{aligned}
 i\hbar\dot{a}_m &= \frac{\partial H}{\partial a_m^*} \\\\
 i\hbar\dot{a}_m^* &= -\frac{\partial H}{\partial a_m}.
\end{aligned} \tag{6}$$

To increase the resemblance, we introduce the real
quantities $p_n(t), q_n(t)$ defined by

$$a_n = \frac{p_n - i\omega_n q_n}{(2\hbar\omega_n)^{1/2}}. \tag{7}$$

In terms
of them, the quantity (5) becomes

$$H(q,p) = \frac{1}{2}\sum_n (p_n^2 + \omega_n^2 q_n^2) + \frac{1}{2}\sum_{mn} [a_{mn}(p_m p_n + \omega_m \omega_n q_m q_n) + 2b_{mn}\omega_m q_m p_n] \tag{8}$$

where $a_{mn}(t), b_{mn}(t)$ are proportional to the real and
imaginary parts of $V_{mn}$, and the Equations of motion (4) and (6)
reduce to

$$\dot{q}_m = \frac{\partial H}{\partial p_m}, \quad \dot{p}_m = -\frac{\partial H}{\partial q_m}. \tag{9}$$

Equations (8) and (9) are, of course, nothing but the Schrödinger
equation, in unconventional notation.

In consequence of the fact that $H_{mn}$ is Hermitian, the Equation of
motion (4) has a rigorous constant of the motion

$$\sum_m |a_m|^2 = \text{constant} \tag{10}$$

which in quantum theory we
interpret as "conservation of probability." Using Equation (7), we find
that in terms of $p_n, q_n$ this conservation law becomes

$$\sum_n \frac{p_n^2 + \omega_n^2 q_n^2}{2\omega_n} = \sum_n \frac{W_n}{\omega_n} = \text{constant} \tag{11}$$

where $W_n$ is the energy stored in the n'th mode. Equation (11) is also
easily verified directly from Equations (8) and (9).

If we had been shown only the final Equations (8), (9), and (11), and
not the argument which I have used to derive them here, a very different
interpretation would seem natural. In Equations (8) and (9) we have an
assemblage of classical harmonic oscillators perturbed by some external
environment in a manner described by the matrices $a_{mn}(t), b_{mn}(t)$.
Since the Hamiltonian (8) is quadratic in the $p_n, q_n$, for any
particular values of the $a_{mn}, b_{mn}$ we could find a new set of
normal modes; the effect of the environment is to vary the spring
constants. The set of harmonic oscillators is not coupled directly to its
environment, but parametrically. Thus to every kind of level scheme which
one might use in a maser, there corresponds a purely classical parametric
system which would behave in just the same manner and what is most
important, would react back on the perturbing environment in the same way
as does the atom or molecule.

As a consequence of this analogy, the decision whether a maser or a
parametric amplifier is best for any given application might involve the
following reasoning. For many jobs which a maser can do, we can in
principle find a classical parametric system which would do the same job.
So it must be the practical considerations, such as availability of
materials with certain relaxation times, stability of parameters,
efficient parametric circuit elements, etc., which lead us to prefer one
kind of device to another. Many years ago, W. W. Hansen proposed a
theorem which may or may not apply to this case; given two different ways
of accomplishing something, both of which will work in principle, that
one will be best which receives the greatest number of man-hours of
development work.

## DISCUSSION

**I. R. SENITZKY:** I would like to make two comments.

1.  The spontaneous emission properties of the molecule have not been
    completely considered, since the field has not been quantized. Thus,
    a molecule may be regarded as a classical parametric system only if
    some of the quantum-mechanical properties are neglected.
2.  It seems that the essential difference between a maser and a
    parametric amplifier (ignoring now the quantum-mechanical aspects
    mentioned above) is that a maser is a collection of many
    loosely-coupled systems, while a parametric amplifier is a single
    system. Thus, there is negligible correlation between the idler
    oscillations of the many molecules of the maser, while the
    parametric amplifier has a single idler oscillation. Any effects,
    therefore, which are due to idler oscillation (such as the ones
    mentioned in my talk yesterday) will be entirely different in a
    maser than in a parametric amplifier.

**E. T. JAYNES:**

1.  Surely. When we write E(t), we are implying
semiclassical radiation theory. However, as I showed in a report last
year, this theory does give spontaneous emission, with the correct
Einstein A-coefficients, if we take the expectation value of dipole
moment as the source for a classical electromagnetic field. Field
quantization is not necessary for spontaneous emission.

2.  The "idler oscillations" involve the absolute phase of the wave
    function $\psi(t)$, which is not observable. In the classical
    Hamiltonian, [Equation (8)], this corresponds to the fact that the
    interaction term involves coordinates and momenta in a form which
    contains only the difference frequencies $\omega_m - \omega_n$, not the
    sums $\omega_m + \omega_n$.

**M. WEISS:** In addition to deriving the Manley-Rowe relations by means
of conservation of the number of quanta, it is also possible to derive
the Tien phase relations for a traveling wave parametric amplifier by
requiring the conservation of momentum. Thus,

$$\left( \frac{h\nu}{v\phi} \right)_{\text{pump}} \approx \left( \frac{h\nu}{v\phi} \right)_{\text{signal}} + \left( \frac{h\nu}{v\phi} \right)_{\text{idler}}$$

results in

$$\beta_{\text{signal}} + \beta_{\text{idler}} = \beta_{\text{pump}}.$$

It is to be noted that for momentum in a dispersive medium one must use
the phase velocity. This quantum analog is particularly useful in the
derivation of the phase relations of more than three frequency traveling
wave parametric amplifiers.

**G. GOULD:** Professor Townes has mentioned an early electron maser,
the triode. The Barkhauser-Kurz oscillator is more easily understood.
Electrons oscillate approximately harmonically in a one-dimensional
potential well between plate and cathode. The electrons are injected into
a band of levels whose vibrational quantum numbers are
$n \approx [E/h\nu] - \frac{1}{2} \sim 10^8$. An oscillating electric
field induces transitions to empty lower and higher levels, depending on
phase. Those which absorb power are removed, leaving a net induced
emission of photons to the e.m. field.

Similarly, in the magnetron type of maser, stimulated emission of
radiation takes place as the electrons undergo transitions to states of
lower angular momentum quantum number.

**M. W. P. STRANDBERG:** An analytic definition which seems to make
physical sense has been given by Strandberg.[^strandberg_1958] A solid state maser or paramagnetic
amplifier by this definition is one in which the pumping field interacts
with a system which has such a short phase memory that only the diagonal
elements of the density matrix are affected, for example, a system with
$T_2 \ll T_1$. A parametric amplifier is one such that the pumping field
is able to impose phase coherence on the system, so that both diagonal
and off-diagonal elements of the density matrix are affected.

[^strandberg_1958]: Phys. Rev. (1958), "Spin-Lattice Relaxation".
