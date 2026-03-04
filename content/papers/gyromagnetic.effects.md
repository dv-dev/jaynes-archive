---
title: "Theory of Gyromagnetic Effects and Some Related Magnetic Phenomena"
year: 1962
abstract: >
  In this paper we present a unified theory of these gyromagnetic effects
  and ordinary magnetic polarization. In addition, we consider the
  analogous nuclear gyromagnetic phenomena and polarization of nuclei by a
  magnetic field. This results in a unified treatment of several effects,
  such as the Knight shift, the Lamb diamagnetic shielding, the Ramsey
  chemical shift, and pseudodipolar coupling. Of these phenomena, only the
  nuclear gyromagnetic effects have not as yet been observed
  experimentally, although their existence has been suggested. Our
  treatment of electronic effects does not include ferromagnetism.
author: ["S.P. Heims[^1]", "E.T. Jaynes[^2]"]
---
## INTRODUCTION
THE experiment of rotating a magnet to polarize it and the converse
experiment of applying a magnetic field to a freely suspended magnet in
order to induce its rotation are called gyromagnetic experiments. Their
history goes back as far as Maxwell,[^3] who suggested and tried these
types of experiments as a means of determining whether electricity is
carried by a material substance. The first successful
magnetization-by-rotation experiments were performed by Barnett[^4] and
the first successful rotation-by-magnetization experiments were carried
out by Einstein and de Haas.[^5] These experiments provided early
measurements of the gyromagnetic ratio of electrons. The experimental
work on these effects has continued[^6] and very high accuracy is 
attained in the recent experiments, particularly those of Scott.[^6]

The physical fact underlying all the gyromagnetic effects is that the
nuclear spin and the electronic spin, as well as their orbital angular
momenta, generate a magnetic moment parallel to the angular momentum
with a magnitude fixed through a characteristic constant of
proportionality, known as the gyromagnetic ratio. This fact, together
with Newton's second law of motion or the Schrödinger equation,
transformed to a rotating-coordinate system, leads to Larmor's
theorem---that the effect of a uniform magnetic field on a system of
spins or particles can be transformed away by going to a rotating
coordinate system, provided the angular momentum of the system in the
field direction is a constant of motion.

In Sec. 2, the quantum-mechanical Larmor theorem is derived. It is given
in a generalized form including spin and orbital motion, systems of
spins with differing gyromagnetic ratios, and some time-dependent
magnetic fields. According to the Larmor theorem, the magnetic field
produces only a periodic effect, although in fact it is well known that
magnetic fields tend to produce polarization in the field direction, not
just periodic Larmor precession. To analyze how polarization can take
place, the behavior in a magnetic field of two spins coupled by the
interaction between their magnetic dipoles is followed by an exact
solution of the Schrödinger equation. The coupling is essential so as to
allow the exchange of angular momentum required to produce polarization.
It is shown that, if no field acts on these two spins but instead the
whole system is physically caused to rotate, this rotation can cause a
polarization of just the magnitude produced by a field which produces a
Larmor frequency equal to the rotation frequency. Polarization does not
occur for any arbitrary initial conditions, but it does occur, for
example, if the initial density matrix corresponds to thermal
equilibrium. This example helps reconcile in a qualitative way the exact
Schrödinger-equation solution with the approximate statistical theories
of magnetization or magnetic-relaxation phenomena.[^7]

In Sec. 3a, the density matrix for a uniformly rotating system in
thermal equilibrium is derived on the basis of maximum-entropy
inference. Since one rarely sees equilibrium distributions involving the
angular momentum in a role parallel to that of the energy (although they
were given by Gibbs), it is of some interest to make predictions for
observations on the basis of this density matrix. The application to
physical systems is made by use of a perturbation theory for expectation
values. The perturbation theory is derived in general terms and its
properties are investigated in detail in Sec. 3b.

In Sec. 3c we obtain the magnetic moment of a piece of magnetically
dilute material with a magnetic field acting on it and with the material
rotating. Similarly, the electronic angular momentum is studied subject
to a field and a rotation. The cross-coupling coefficients, i.e., the
magnetic moment due to rotation alone or the angular momentum due to the
field alone, represent the Barnett and the Einstein-deHaas effects,
respectively. A summary of the comparison of experimental data with the
theory of these effects is given. The present form of the theory is in
agreement with some previous calculations for particular cases in the
literature.[^8]

In Sec. 3d, the polarization of a nuclear spin in a rotating crystal
acted upon by a constant magnetic field is studied and its magnitude
calculated. The corrections to the polarization due to the internal
crystal field are obtained from the perturbation theory for expectation
values. Many line-shift phenomena, well known from nuclear magnetic
resonance experiments, are shown to result from such a treatment. These
effects are usually derived separately; in some cases, the unified
method given here may provide a simpler means of evaluating the effects
because the energy denominators of second-order perturbation theory can 
be avoided and also because the formulas are in a form independent of 
the representation used.

In Sec. 4, the time-dependent behavior of nuclear spins in a rotating
crystal is described. We attempt there to show the relation of solutions
to the Schrödinger equation for the rotating crystal to those for the
case of a rotating magnetic field acting on the crystal. A statistical
treatment of the spin system on a rotating crystal is given, using the
formalism and the approximations of the Wangsness-Bloch theory of
nuclear magnetic relaxation.

In all of the theory of rotation phenomena and induced angular momenta,
it is apparent that the information to be gained from their study is of
a nature similar to, but not usually identical with, that obtained from
studying magnetic phenomena and magnetic moments. Thus, the measurements
of gyromagnetic coefficients give as much useful information as the
determination of magnetic susceptibilities, nuclear or electronic. Yet,
the magnetic phenomena have been studied far more fully than the
gyromagnetic ones; small wonder, in view of the greater difficulty of
performing experiments of the latter type.
## DYNAMICS OF SPIN SYSTEMS
### Larmor's Theorem in Quantum Mechanics
According to both classical theory and quantum mechanics, the effect of
a uniform magnetic field on a system of charged particles may be shown
to be equivalent to a rotation of the coordinate system. In quantum
mechanics, the system is described by the wave function $\psi(x,t)$, a
solution to the Schrödinger equation
$$
i\hbar \frac{\partial\psi}{\partial t} = \mathcal{H}\psi,
$$
 where
$\mathcal{H}$ is the Hamiltonian operator, $x$ represents all the space
and spin coordinates of the system of particles, and $t$ is the time.
The transformation of the wave function to a rotating coordinate system
is achieved by means of a unitary operator $R(t)$. The rotated wave
function is $\psi_r=R(t)\psi(x,t)$. The vector operators appearing in
quantum mechanics (momentum, position, angular momentum) are rotated by
the same transformation. If $Q$ is such a vector operator, then
$Q_r = R(t)QR(-t)$ gives the operator in the rotating system.

Explicitly, 
$$
R(t) = \exp[(i/\hbar)J \cdot \omega t],
$$
 where $J$ is the
total angular momentum of the system and $\omega$ the angular velocity
of the coordinate system. Equation (2) follows from the requirements
that $R$ be unitary, that it satisfy the relation
$R(t_1)R(t_2) = R(t_1+t_2)$, and the well-known connection between
infinitesimal rotations and angular-momentum operators,[^7] expressed by
$$
J \cdot \omega = i\hbar \lim_{t\to 0} [R(t)-1]/t.
$$

 The Hamiltonian
$\mathcal{H}$ of the system considered is assumed to be time-independent
and to consist of a part $\mathcal{H}_0$ independent of the magnetic
field and an additional part $\mathcal{H}_1$ due to a constant magnetic
field. Without the field, the time development of the wave function is
$$
\psi(x,t) = \exp[-(i/\hbar)\mathcal{H}_0 t]\psi(x,0);
$$
 with the
magnetic field, it is
$$
\psi = \exp[-(i/\hbar)(\mathcal{H}_1+\mathcal{H}_0)t]\psi(x,0).
$$

Applying the rotation operator $R(t)$ corresponding to a uniform rate of
rotation to (3), gives
$$
\psi_r = \exp[(i/\hbar)J\cdot\omega t] \exp[-(i/\hbar)\mathcal{H}_0 t] \psi(x,0).
$$

Restricting consideration to a Hamiltonian $\mathcal{H}_0$ which is
invariant to rotation around the direction of $\omega$, so that
$[J\cdot\omega, \mathcal{H}_0]=0$, permits rewriting (5) in the form
$$
\psi_r = \exp[-(i/\hbar)(-\omega\cdot J+\mathcal{H}_0)t]\psi(x,0).
$$

To obtain a Larmor theorem,[^8] we compare Eqs. (4) and (6) for some
particular types of systems:

For a system of spins all having the same gyromagnetic ratio $\gamma$,
in a uniform magnetic field $H$, $\mathcal{H}_1 = -\gamma S \cdot H$;
then by inspection $\psi_r$ and $\psi_t$ are identical if the field is
equal to $H = (1/\gamma)\omega$.

For a system of spins with differing gyromagnetic ratios and a field
$H_k$ acting on the $k$th spin,
$\mathcal{H}_1 = -\sum_k \gamma_k S_k \cdot H_k$. For a given angular
velocity $\omega$, $\psi_t$ and $\psi_r$ are equal only if the fields
$H_k$ have the values 
$$
 H_k = (1/\gamma_k)\omega; 
\tag{7a}
$$
 or if a uniform field $H_0=H$ is given, the theorem may be
stated as requiring a different rotation frequency for each particle, so
that in Eq. (6), $\omega \cdot J$ becomes $\sum_k \omega_k S_k$ with
$$
\omega_k = \gamma_k H.
\tag{7b}
$$

 The theorem is exact for a pure spin system. Consider however
the magnetic part of the Hamiltonian for the motion of an electron in a
uniform magnetic field $H$,
$$
\mathcal{H}_1 = (e/2mc)H\cdot(L+2S)+(e^2/8mc^2)H^2 r^2 \sin^2\theta,
$$
where $\theta$ is the angle between the position vector $r$ and the
magnetic field. In this case, it is necessary to assume that the
quadratic term in $\mathcal{H}$ is small compared to the linear term.
Then the Larmor theorem applies, the space function and spin functions
being rotated with angular velocities
$$
\omega_1 = -\frac{e}{2mc}H, \quad \text{and} \quad \omega_s = 2\omega_1,
$$
 respectively. For ordinary laboratory fields, the quadratic term in (8)
is indeed very small compared to a linear term and (9) is a very good
approximation. The error can be estimated by expanding (4) to first
order in the neglected term to obtain
$$
\psi(x,t) = e^{i\epsilon}(1+A)\psi(x,0),
$$
 where 
$$
\begin{aligned}
A &= -\frac{it}{\hbar} \left[\mathcal{H}_0 - \frac{eH\cdot(L+2S)}{2mc}\right] \nonumber \\\\
& \quad -\frac{it e^2 H^2}{\hbar 8mc^2} \int d\tau e^{i\epsilon} (r^2 \sin^2\theta) e^{-i\epsilon}.
\end{aligned}
$$

 Thus, (9) is valid when $|\epsilon| \ll 1$. The
assumption made in deriving (6), namely, that
$[J\cdot\omega, \mathcal{H}_0]=0$ is fulfilled for any system on which
no external torque is acting other than the constant magnetic field
considered.

The Larmor theorem, Eqs. (7) and (9), may be generalized to
time-dependent fields, giving a description of the wave function as the
field builds up. Suppose the magnetic field varies linearly with the
time[^9] 
$$
 H(t) = at+H_0,
$$
 but is uniform throughout space. The vectors
$H_0$ and $a$ may point in arbitrary directions, so that the direction
of the field $H(t)$ may be a function of time. To satisfy the Maxwell
equation $\mathrm{curl} E = (-1/c)\partial H/\partial t$ an electric
field must accompany the growing magnetic field: $E=-a \times r/2c$. The
other Maxwell equations for a source-free region are then also
satisfied. By introducing the potentials $A=H(t) \times r/2$ and
$\phi=0$, it is readily shown that the Hamiltonian of systems of spins
and particles will differ from that of a system in a constant magnetic
field only in that $H(t)$ everywhere will replace $H$. The
time-dependent Larmor theorem is then proved by considering small
rotations 
$$
 R_n = 1+(i/\hbar)\sum_k I_k \cdot \omega_k(t_n)\Delta t,
$$
 and the limit of the product
$$
 R(t) = \lim_{N\to\infty} \prod_{n=1}^N R_n = \exp \left[-\frac{i}{\hbar}\sum_k I_k \int_0^t \omega_k(t^\prime)dt^\prime\right].
$$

 In (13), the convention must be observed that in every product of
$I\omega_x(t_n)$ and $I\omega_x(t_m)$ that occurs, the order of writing
the factors is taken to be the order of the natural time sequence.
Comparing (13) to the part of the time-evolution operator involving the
magnetic field and requiring that $[J\cdot\omega(t), \mathcal{H}_0]=0$,
gives the time-dependent Larmor theorem which differs from (7) and (9)
only in that $H$ and $\omega$ are time-dependent. For example, (7b)
becomes 
$$
\omega_k(t) = \gamma_k H(t) \text{ for all } t.
$$

 For magnetic
fields which vary nonlinearly with the time, the accompanying electric
field is only approximately given by $E = \dot{H} \times r/2c$. The
approximation consists of neglecting displacement current. When that
approximation applies, the theorem (14) and the other time-dependent
expressions corresponding to (7a) and (9) can be derived.
### A Simple Example of Polarization
The discussion of Larmor's theorem has shown that the effect of a
constant magnetic field is transformed away by going to a rotating
coordinate system. However, in the following sections, we are primarily
concerned with the polarization of systems in the field direction, a
phenomenon which is not transformed away by going to a rotating system.
To help clarify how polarization can occur in spite of Larmor's theorem,
a very simple example is treated in Appendix A by an exact integration
of the Schrödinger equation. The system considered is a pair of nuclear
spins, each of magnitude $\frac{1}{2}\hbar$, coupled to each other by
dipole-dipole coupling. Some polarization of the spins can be brought
about either by applying a magnetic field in a direction perpendicular
to the line connecting the positions of the two nuclei, or by a rigid
rotation of the whole system about such a direction.[^10] To show that
the latter problem can be reduced to the magnetic-field problem, we note
that the expression for the interaction of two dipoles, if the relative
position vector $R$ is rotating, is 
$$
\begin{aligned}
G(t) &= -\frac{\gamma_1\gamma_2\hbar^2}{2R^3} \left[ S_1 \cdot S_2 - \frac{3[S_1 \cdot R(t)][S_2 \cdot R(t)]}{R^2} \right] \nonumber \\\\ &= \exp\left(\frac{i}{\hbar}\omega\cdot S t\right) \frac{-\gamma_1\gamma_2\hbar^2}{2R^3} \nonumber \\\\ & \quad \times \left[ S_1 \cdot S_2 - \frac{3[S_1 \cdot R(0)][S_2 \cdot R(0)]}{R^2} \right] \exp\left(-\frac{i}{\hbar}\omega\cdot S t\right),
\end{aligned}
$$
where $\omega$ is the angular velocity of rotation and $S_1$ and $S_2$
the spins of the two dipoles in units of $\hbar$ and $\gamma_1$,
$\gamma_2$, their gyromagnetic ratios. Transforming the Schrödinger
equation $i\hbar \dot{\psi} = G(t)\psi$ by the unitary transformation
$\psi^\prime = \exp[(i/\hbar)\omega\cdot St]\psi$ gives the equation
$$
i\hbar \frac{d\psi^\prime}{dt} = [G(0)-\hbar\omega\cdot S]\psi^\prime, \quad S=S_1+S_2.
$$

The Schrödinger equation for the pair of coupled spins with identical
gyromagnetic ratios $\gamma$ is
$i\hbar d\psi/dt = [G(0)-\gamma\hbar H\cdot S]\psi$, which is identical
with (15) except in that the Larmor frequency $\omega_L=\gamma H$
replaces $\omega$. We expand the solution in eigenfunctions $\phi$ of
$S^2$ [eigenvalues $s(s+1)$, $|S_1-S_2| \leq s \leq S_1+S_2$] and
$S_z$ [eigenvalues $m_s$, $-s \leq m_s \leq s$]:
$$
\psi(t) = \sum_k b_k(t)\phi_k(m_s, s),
$$
 where $k=1$ stands for
$(m_s,s)=(1,1)$; $k=2$ for $(m_s,s)=(0,1)$; $k=3$ for $(m_s,s)=(-1,1)$;
and $k=4$ for $(m_s,s)=(0,0)$. We take the direction of $\omega$ or $H$
as the $x$ direction, but the nuclei on a line parallel to the $z$
direction. Assuming the field turned on at $t=0$, and averaging over
oscillations, we find the following results for the expectation value of
the total spin after the field (or rotation) has been on a long time:
$$
\langle S_x \rangle = \frac{3\hbar\omega E_0}{\epsilon^2} [|b_1(0)+b_3(0)|^2 - 2|b_2(0)|^2] + \frac{4(\hbar\omega)^2}{\epsilon^2} \langle S_x(0) \rangle,
$$
 $\langle S_y \rangle = \langle S_z \rangle = 0$, with
$E_0=(\hbar\gamma)^2/2R^3$,
$\epsilon^2=[(3E_0)^2+(2\hbar\omega)^2]^{1/2}$. The polarization (16)
clearly depends on initial conditions and may be in either direction. If
the initial density matrix $b_k b_l^*$ is a multiple of the unit matrix,
the system cannot polarize because the density matrix will of necessity
commute with the Hamiltonian and so will not change with time. If we
have a large number of identical pairs of spins, and if initially before
the field is turned on each pair is in contact with a heat reservoir at
a temperature $T_0$, and then at $t=0$ the reservoir is removed, we find
from (16) for one such pair on the average
$$
\langle\langle S_x \rangle\rangle = -\frac{\hbar\omega}{kT_0} \frac{(3E_0)^2}{2\epsilon^2}.
$$

 The second $\langle\langle \cdot \rangle\rangle$ indicates the average
over the initial states. The polarization (17) is a maximum when
$2\hbar\omega=3E_0$, and it falls off for $2\hbar\omega \gg 3E_0$. This
is to be expected, because the polarization process requires
simultaneous exchange of energy $\hbar\omega$ and angular momentum
between the Zeeman part of the Hamiltonian and the dipole-dipole
coupling. However, the latter can absorb no more than an amount of
energy of the order of $3E_0$, so that when $2\hbar\omega \gg 3E_0$, the
two spins are effectively uncoupled and no polarization can occur. If we
had included more degrees of freedom in the example, then it is expected
more polarization would be possible. The spins can be polarized in this
example in spite of Larmor's theorem, since the Hamiltonian $G$ does not
commute with $S\cdot\omega$; the angular momentum lost or gained by the
spin is transferred to the nuclear-orbital motion via the interaction
$G$. Thus, the dipole-dipole coupling provides a mechanism for spin
polarization through the exchange of angular momentum with the
nuclear-position coordinates.
## EQUILIBRIUM THEORY
### Density-Matrix Description of Rotating-Material System
The foregoing example illustrates that Larmor's theorem (or in fact the
Schrödinger equation) is not incompatible with the tendency of systems
to move towards thermal equilibrium. In this section, we assume that
thermodynamic equilibrium of the system is obtained, and study the
equilibrium properties of general systems. Consider a macroscopic system
which has a total energy $E=\langle\mathcal{H}\rangle$ and whose total,
angular-momentum components are $M_i=\langle J_i \rangle$. The
$\langle \cdot \rangle$ indicate the taking of an expectation value of
an operator, i.e., the trace of the product of the operator with the
density matrix describing the system. The density matrix which describes
the aforementioned information is obtained by maximizing the entropy,
subject to the constraints imposed by knowledge of the expectation value
of energy and angular momentum.[^11] The resulting density matrix is
$$
\rho = \exp(-\beta\mathcal{H} - \lambda_i J_i - \lambda_0 1),
$$
 where
$\beta$, $\lambda_i$, and $\lambda_0$ are introduced in the derivation
as Lagrange multipliers whose physical significance is determined
next.[^12] The summation convention is used for the index $i$, which
runs from 1 to 3. Normalization of $\rho$ such that $\mathrm{Tr}\rho=1$,
requires that $\lambda_0=\ln Z$, where
$Z=\mathrm{Tr}\exp(-\beta\mathcal{H}-\lambda_i J_i)$ is the partition
function. The afore-mentioned expectation values are given in terms
of $\rho$ and $Z$ by 
$$
\begin{aligned}
\langle \mathcal{H} \rangle &= \mathrm{Tr}(\rho\mathcal{H}) = -\partial \ln Z / \partial\beta; \nonumber \\\\ 
\langle J_i \rangle &= \mathrm{Tr}(\rho J_i) = -\partial \ln Z / \partial\lambda_i.
\end{aligned}
$$

 The entropy corresponding to the density matrix (18) is, in
conventional units,
$$
\begin{aligned}
S &= -k \mathrm{Tr}(\rho\ln\rho) \nonumber \\\\ &= k[\beta\langle\mathcal{H}\rangle+\lambda_i\langle J_i \rangle + \lambda_0],
\end{aligned}
$$
 where $k$ is the Boltzmann constant. Differentiating
(20) and noting from (19) that
$-d\lambda_0=\langle\mathcal{H}\rangle d\beta + \langle J_i \rangle d\lambda_i$,
gives
$$
dS = k[\beta d\langle\mathcal{H}\rangle + \lambda_i d\langle J_i \rangle].
$$

We now consider a macroscopic system characterized by a uniform and
constant temperature $T_0$, rotating with constant and uniform angular
velocity $\omega$. The system is in thermal and rotational equilibrium,
and can be described by the laws of thermodynamics. The increment of
total energy is $dE=dQ+\omega_i dM_i$, from which the differential of
entropy is 
$$
 dS = dQ/T = (1/T)dE - (\omega_i/T)dM_i.
$$

 Comparison of
(21) and (22) yields the physical meaning of the Lagrange multipliers,
$$
\beta=1/kT, \quad \lambda_i = -\omega_i/kT.
$$

 The density matrix (18)
may thus be written as
$\rho=Z^{-1} \exp{-\beta(\mathcal{H}-\omega_i J_i)}$. From Eq. (6), the
quantity $\mathcal{H}-\omega_i J_i$ appearing in the exponent has the
physical significance of the effective Hamiltonian in the
rotating-coordinate system, if $\omega_i J_i$ is a constant of the
motion. In this case, the density matrix remains given by (18) for all
time.

If $\omega_i J_i$ is not a constant of the motion, Eq. (18) gives the
density matrix only at the initial time $t=0$, for which the information
$\langle\mathcal{H}\rangle, \langle J_i \rangle$ is given. The time
dependence of any density matrix is given by
$i\hbar \dot{\rho} = [\mathcal{H}, \rho]$. The equilibrium-density
matrix for a rotating system need not commute with the Hamiltonian and
thus may have a time dependence. By "equilibrium" we mean that
expectation values of observable quantities are constant in a frame of
reference rotating with the system. The vector operator $v$ is
represented in the rotating system, for example, by the operator
$v_r = R(t)vR(-t)$, where $R(t)$ is given by the expression (2). Its
equation of motion is 
$$
\begin{aligned}
\left\langle \frac{dv_r}{dt} \right\rangle &= \left\langle \frac{\partial v_r}{\partial t} \right\rangle + \frac{1}{i\hbar} \langle [\mathcal{H}] \rangle \nonumber \\\\ &= (1/i\hbar) \langle [v_r, \mathcal{H}-\omega_i J_i] \rangle \nonumber \\\\ &= (1/i\hbar) \mathrm{Tr}(v_r, [\rho, \mathcal{H}-\omega_i J_i]),
\end{aligned}
$$

 The commutator, and hence $\langle dv_r/dt \rangle$,
vanishes for the equilibrium-density matrix (18). Also, it is easily
seen that the density matrix in the rotating frame is constant:

$\dot{\rho}_r=(d/dt)[R(t)\rho R(-t)]=0$. In practice, one may be
interested only in some small part of the macroscopic rotating system,
such as the expected value of the spin angular momentum in a crystal
with many other degrees of freedom. Then, in taking the trace of $\rho$,
one can first sum over all the quantum numbers of the other degrees of
freedom; what remains is a density matrix with a smaller number of rows
and columns, describing only the small subsystem being studied. If the
interaction energy between the subsystem and the remaining system is
neglected, the only role of the larger system will be to provide an
environment with a definite temperature and angular velocity. We focus
attention on the expectation value of the magnetic moment of a single
atom or nucleus, but assume that it is representative of a large number
of identical spins in the macroscopic sample. If spin-spin interactions,
either direct or indirect (through the lattice) are negligible, the
condition that expected moments for a single spin correspond to a
reliable prediction of total moment of $N$ spins is
$N\gg(\beta\hbar\gamma H^*)^{-1}$, where
$H^*=|\mathbf{H}-\omega/\gamma|$ is the effective magnetic field. As
spin-spin interactions become stronger, the requirements become more
stringent, and when conditions for a ferromagnetic or antiferromagnetic
phase change are reached, the connection between expected moment of a
single spin and total moment of $N$ spins breaks down completely. As is
shown elsewhere, this breakdown of correspondence between the Boltzmann
"molecular" treatment and the Gibbs "global" treatment is
characteristic of any phase transition. In this paper, we limit
ourselves to the case of sufficiently weak interactions so that
cooperative phenomena do not appear. Before proceeding to calculate
specific gyromagnetic effects with the density matrix (18), the
perturbation method to be employed is developed.
### Perturbation Expansion[^13] for Expectation Values
The expectation value of an arbitrary operator $C$, pertaining to a
system described by a density matrix of the form (18), is
$\langle C \rangle = \mathrm{Tr}(\rho C)$. If part of the exponent in
(18) is small, but complicated, it may be treated as a perturbation.
Since the quantity $\langle C \rangle$ is the trace of an operator, its
value is independent of the representation; this invariance property is
to be retained in the perturbation scheme. Not only is it convenient to
work directly with the expansion for the expectation value of the
observable of interest rather than an expansion for the partition 
function, but also, because of the normalizing denominator, the 
convergence of the expansion is bound to be better. Consider a quite 
general system described by a density matrix
$$
\rho = e^{\epsilon A+B}[\mathrm{Tr}(e^{\epsilon A+B})]^{-1},
$$
 where
$A$ and $B$ are arbitrary operators. A second, simpler, density matrix,
is $\rho_0=e^A[\mathrm{Tr}e^A]^{-1}$. We assume that expectation values
over $\rho_0$ can be evaluated directly, and express the expectation
value over $\rho$ in terms of those over $\rho_0$. The expectation value
of an arbitrary operator $C$,
$\langle C \rangle_\epsilon = \mathrm{Tr}Ce^{\epsilon A+B} / \mathrm{Tr}e^{\epsilon A+B}$,
is a function of the number $\epsilon$. When $\epsilon=0$, then
$\langle C \rangle_\epsilon = \langle C \rangle_0 = \mathrm{Tr}(\rho_0 C)$.
When $\epsilon=1$, then
$\langle C \rangle_\epsilon = \langle C \rangle = \mathrm{Tr}\rho C$.
Expanding $\langle C \rangle_\epsilon$ in a Taylor series about
$\epsilon=0$,
$$
\langle C \rangle_\epsilon = \sum_{n=0}^\infty \frac{\epsilon^n}{n!} \frac{d^n \langle C \rangle_\epsilon}{d\epsilon^n} \bigg|_{\epsilon=0}.
$$

 To evaluate the leading terms in (26), we make use of the well-known
mathematical identity[^14]
$$
e^{A+B} = e^A\left[1+\epsilon \int_0^1 e^{-Ax}Be^{A(x+\epsilon B)}dx \right]
$$
 to obtain, by iteration,
$$
e^{\epsilon A+B} = e^A[1+\epsilon S_1 + \epsilon^2 S_2 + O(\epsilon^3)]
$$
$$
\begin{aligned}
S_1 &= \int_0^1 dx e^{-Ax}Be^{Ax} \nonumber \\\\ S_2 &= \int_0^1 xdx \int_0^1 dx^\prime e^{-Ax}Be^{Ax(1-x^\prime)}Be^{Axx^\prime},
\end{aligned}
$$
 and, thus, 
$$
\begin{aligned}
\frac{de^{\epsilon A+B}}{d\epsilon}\bigg|_{\epsilon=0} &= e^A S_1; \nonumber \\\\ \frac{d^2e^{\epsilon A+B}}{d\epsilon^2}\bigg|_{\epsilon=0} &= 2e^A S_2.
\end{aligned}
$$

 The derivatives for $\langle C \rangle_\epsilon$ are
then obtained by application of (29) and the definition (26) for
$\langle C \rangle$. The result is up to $n=2$ for $\epsilon=1$, if we
define $\Gamma=C-\langle C \rangle_0\cdot 1$,
$$
\langle\Gamma\rangle = \langle S_1 \Gamma \rangle_0 + (\langle S_2 \Gamma \rangle_0 - \langle S_1 \rangle_0 \langle B\Gamma \rangle_0).
$$

 The subscript 0 means the average is taken over density matrix $\rho_0$. The higher-order terms to arbitrary order are derived in Appendix B. In the special case that $A$ and $B$ commute, the calculation becomes relatively simple because $S_1=B$ and $S_2=\frac{1}{2}B^2$. A somewhat more complicated case is the one where $A$ and $B$ do not commute, but $A$ and $C$ are commuting operators. In that case, (30) becomes
$$
\langle\Gamma\rangle = \langle B\Gamma \rangle_0 + \langle(S_2 - \langle B \rangle_0 B)\Gamma \rangle_0 = \langle B\Gamma \rangle_0 + \frac{1}{2}\langle(B-\langle B \rangle_0)^2 \Gamma \rangle_0 + Q,
$$
 where
$$
Q = \int_0^1 xdx \int_0^1 dx^\prime \langle e^{-A\Gamma}[Be^{A\Gamma(1-x^\prime)}]Be^{A\Gamma x^\prime} \rangle_0.
$$

 It is seen that if the operator $A \to 0$, the commutator in $Q$
vanishes, since every operator commutes with the unit operator. For
small $A$, the operator $Q$ is of order $(AB^2)$, and is, therefore, small
compared to the other terms in (31) which are of the order
$\langle B^2 \rangle$. So, for sufficiently small $A$, the operator $Q$
may be neglected. To make this condition more precise, we introduce an
explicit representation. In general, one can split $A$ into a part $a$
which fails to commute with $B$ and a part $a^\prime$ which commutes with $a$
and $B$, both $a$ and $a^\prime$ commuting with $\Gamma$. Then, in a
representation where $a$ and $\Gamma$ are diagonal, the complete
quadratic term in (27),
$\langle(S_2 - \langle B\rangle_0 B)\Gamma\rangle_0$, can be shown to be
equal to $\langle \theta \Gamma \rangle_0$ with 
$$
\begin{aligned}
\theta_{kl} &= \delta_{kl} \left[ \sum_n |B_{kn}|^2 f(a_n-a_k) - \langle B \rangle_0 B_{kk} \right], \nonumber \\\\ f(x) &= \sum_{N=0}^\infty \frac{x^{N-2} - x - 1}{N!}
\end{aligned}
$$

 Putting $Q=0$ corresponds to replacing $f(a_n-a_k)$ by
$1/2$, its limiting value for vanishing $a_n-a_k$. A sufficient
condition for neglecting $Q$ is that for all states $n$ and $k$ for
which $|B_{nk}|^2$ is finite, $|a_n-a_k|$ be much less than unity. A
particular case of (31) and (33) is the one in which $B$ is a sum of
terms, $B=\sum_k b^{(k)}$. Then, 
$$
\begin{aligned}
\langle \Gamma \rangle = \sum_k \langle b^{(k)}\Gamma \rangle_0 &+ \sum_k \sum_\lambda \langle (b^{(k)}b^{(\lambda)} - 2\langle b^{(k)} \rangle_0 \langle b^{(\lambda)} \rangle_0) \Gamma \rangle_0 + Q,
\end{aligned}
$$
 and
$\theta_{kn} = \delta_{kn} \sum_k \sum_\lambda [\sum_m b_{km}^{(k)} b_{mn}^{(\lambda)} f(a_n-a_m) - \langle b^{(k)} \rangle_0 b_{nn}^{(\lambda)}]$.
The rapid convergence of the expansion (26) or (30) for
$\langle C \rangle$ does not necessarily require that the eigenvalues of
the operator $B$ be small, even though it is an expansion in powers of
$B$. The convergence is in part due to the effective cancellation of
terms in the numerator and the denominator of
$\mathrm{Tr}(Ce^{A+B})/\mathrm{Tr}(e^{A+B})$. For example, if $B$ is a
multiple of the unit operator, cancellation is complete and
$\langle C \rangle = \langle C \rangle_0$; if $B$ is a multiple of the
unit operator plus a small operator, one expects convergence to be rapid
because the part proportional to the unit operator has no effect. The
linear term in the expansion (30) has the property that if the roles of
$B$ and $C$ are interchanged, it remains unchanged, even if none of the
operators $A, B,$ or $C$ commute with either of the other operators:
$$
\int_0^1 dx \langle e^{-Ax}B e^{Ax} C \rangle_0 - \int_0^1 dx \langle e^{-Ax} C e^{Ax} B \rangle_0 = 0;
$$
 for, in a representation in which $A$ is diagonal,
$$
(Z^{-1})\sum_n \sum_m \langle n|B|m \rangle \langle m|C|n \rangle \times \int_0^1 dx \{ \exp[A_n x(1-x)+A_m x] - \exp[A_m(1-x)+A_n x] \} = 0,
$$
 because the integral vanishes identically. The other linear term
$\langle S_1 \Gamma \rangle_0 \langle C \rangle_0 = \langle B \rangle_0 \langle C \rangle_0$
is obviously also unchanged by an interchange of $B$ and $C$. This
symmetry property is shown to imply a class of reciprocity laws for
measurable magnetic and gyromagnetic constants. We illustrate some
properties of the expansion (30) and at the same time obtain some
formulas which are required later on by applying the perturbation scheme
to some simple examples of nonrotating systems.
#### Magnetic Susceptibility of Free Atoms or Ions
The electrons of an atom or an ion in the presence of a static magnetic
field $H$, may be described by a Hamiltonian of the form
$$
\begin{aligned}
\mathcal{H} &= \mathcal{H}^{(0)} + \mathcal{H}^{(1)}H + \mathcal{H}^{(2)}H^2, \nonumber \\\\ \mathcal{H}^{(1)} &= -(\frac{e}{2mc})(L_z+2S_z), \nonumber \\\\ \mathcal{H}^{(2)} &= (\frac{e^2}{8mc^2})\sum_k (x_k^2+y_k^2),
\end{aligned}
$$
 and $\mathcal{H}^{(0)}$ is an operator not involving the
magnetic field; $L$ and $S$ are orbital and spin angular momentum. The
magnetic-moment operator is defined by
$M_z = -\partial\mathcal{H}/\partial H$, which in view of (36), becomes
$M_z = -\mathcal{H}^{(1)} - 2H\mathcal{H}^{(2)}$. Taking the expectation
value gives the exact expression for the magnetic moment; assuming an
equilibrium density matrix with no rotation,
$$
\langle M_z \rangle = \frac{-\mathrm{Tr}(\partial\mathcal{H}/\partial H)\exp(-\beta\mathcal{H})}{\mathrm{Tr}\exp(-\beta\mathcal{H})} = -\langle\mathcal{H}^{(1)}\rangle_0 - 2H\langle\mathcal{H}^{(2)}\rangle_0.
$$

 We restrict attention to the part of the magnetic moment linear in the
field strength. Let $A=-\beta\mathcal{H}^{(0)}$,
$B=-\beta(H\mathcal{H}^{(1)}+H^2\mathcal{H}^{(2)})$, and assume that $B$
is small, or numerically that $\beta\mu_B H=6.4\times 10^{-5}H/T \ll 1$,
if $H$ is measured in gauss and $T$ in degrees Kelvin. Expanding (37) by
means of Eq. (30) and assuming zero spontaneous polarization
$\langle\mathcal{H}^{(1)}\rangle_0=0$, we obtain for the term linear in
$H$,
$$
\langle M_z \rangle = H\beta \int_0^1 dx \langle e^{-A}x \mathcal{H}^{(1)} e^{Ax} \mathcal{H}^{(1)} \rangle_0 - 2H\langle\mathcal{H}^{(2)}\rangle_0.
$$

 The susceptibility, defined by $\chi=d\langle M_z \rangle / dH$, is then
$$
\chi = \beta \int_0^1 dx \langle e^{-Ax}\mathcal{H}^{(1)}e^{Ax}\mathcal{H}^{(1)}\rangle_0 - 2\langle\mathcal{H}^{(2)}\rangle_0.
$$

 The diamagnetic (negative definite) part has the usual form,
$$
\chi_d = -2\langle\mathcal{H}^{(2)}\rangle_0 = -\frac{e^2}{4mc^2}\langle\sum_k(x_k^2+y_k^2)\rangle_0 = -\frac{e^2}{6mc^2}\langle\sum_k r_k^2\rangle_0,
$$
 where the last step is permissible if in the absence of the field no
direction is singled out in the atom, i.e., if its environment has cubic
or isotropic symmetry. We obtain the Van Vleck expression[^15] for
paramagnetic susceptibility from the first part of (38) by introducing a
representation in which $\mathcal{H}^{(0)}$ is diagonal with eigenvalues
$E_n$, and then integrating:
$$
\chi_p = \beta \int_0^1 dx \langle e^{-Ax} \mathcal{H}^{(1)} e^{Ax} \mathcal{H}^{(1)} \rangle_0
$$
$$
\begin{aligned}
&= \beta \int_0^1 dx \frac{\sum_m \sum_n \langle m|e^{A(1-x)}|m \rangle \langle m|\mathcal{H}^{(1)}|n \rangle \langle n|e^{Ax}|n \rangle \langle n|\mathcal{H}^{(1)}|m \rangle}{\sum_n \langle n|e^A|n \rangle} \qquad (39a) \\\\ &= \frac{2\sum_{n,m, E_n \neq E_m} \frac{\exp(-E_m\beta)}{E_n-E_m} |\langle m|\mathcal{H}^{(1)}|n \rangle|^2}{\sum_n \exp(-E_n\beta)} + \frac{\beta \sum_n \exp(-E_n\beta) |\langle n|\mathcal{H}^{(1)}|n \rangle|^2}{\sum_n \exp(-E_n\beta)}. \qquad (39b)
\end{aligned}
$$

 An approximation to (39) suggests itself if we write
$$
\chi_p = \beta \langle (\mathcal{H}^{(1)})^2 \rangle_0 + \beta \int_0^1 dx \langle [e^{-Ax},\mathcal{H}^{(1)}] e^{Ax}\mathcal{H}^{(1)}\rangle_0
$$
 and neglect the commutator to obtain
$$
\chi_p = \beta\mu_B^2/\hbar^2 \langle(L_z+2S_z)^2\rangle_0.
$$

 The
neglect of the commutator is permissible if that part of $A$ which fails
to commute with $\mathcal{H}^{(1)}$ is sufficiently small. In an atom or
ion, this is usually a single term of the form
$(\zeta/\hbar^2)L\cdot S$, so that if $|\betaζ| \ll 1$, the
commutator may be neglected.

From this derivation of susceptibilities, three points about the
perturbation theory are noted. (1) Whereas the result (39) is obtained
by using only the first term in the expansion (30), the usual
derivation[^18] of (39) by means of a perturbation theory for the energy
levels requires a second-order perturbation calculation. Generally, the
two different perturbation schemes need not run parallel, since their
expansion parameters are in fact different. (2) The result (40) would
not be obtained at all in the energy-level perturbation scheme. There
the first-order term involves only the diagonal elements of
$(L_z+2S_z)$, whereas (40) includes both diagonal and off-diagonal
elements. Thus, somewhat different approximations are suggested by the
two different schemes. (3) If the energy denominator in (39b) creates a
problem, an alternative method of evaluating (39) is to take the trace
[e.g., carry out the sums in (39a)] before doing the integral.
#### Polarization of Nuclei with Hyperfine Coupling
The second example for consideration is the polarization of nuclei which
are coupled to electrons via the hyperfine interaction. The system is
described by the Hamiltonian
$$
\mathcal{H} = \mathcal{H}_e - \gamma_e S\cdot H - \gamma_n I\cdot H - \gamma_n \sum_k a_k S_k \cdot I,
$$
 where $\mathcal{H}_e$ does not involve the nuclear-spin coordinates, $I$
is the nuclear-spin vector, $S=\sum_k S_k$ is the total electronic spin, and
$\gamma_e$ and $\gamma_n$ are the electronic and nuclear
gyromagnetic ratios, respectively ($\hbar\gamma_e=2\mu_B$ and
$\hbar\gamma_n=g\mu_N$ in terms of the Bohr and nuclear magneton). The
$a_k$ are the hyperfine-coupling constants,[^16]

$a_k=(8\pi/3)\gamma_e\hbar |\psi_k(0)|^2$ where $|\psi_k(0)|^2$ is the
probability that the $k$th electron is found at the nucleus. This
probability is finite for the S-state electrons in free atoms as well as
for the free electrons in metals. The second and third terms of (41)
give the coupling of the external field with the electronic and nuclear
dipoles, respectively, and the last term is the interaction of the
nuclear dipole with the electronic ones. Let us call the direction of
the magnetic field the $z$ direction, and let 
$$
\begin{aligned}
A &= \beta(\gamma_n I_z H + \gamma_e S_z H - \mathcal{H}_e), \nonumber \\\\ B &= \beta\gamma_n \sum_k a_k S_{kz} I_z, \nonumber \\\\ C &= I_z.
\end{aligned}
$$

 Since $[A,C]=0$, we have to first order in $B$ from Eq.
(31)
$$
\langle I_z \rangle = \langle I_z \rangle_0 + \beta\gamma_n \sum_k a_k \langle S_k \cdot I (I_z - \langle I_z \rangle_0) \rangle_0.
$$

 Evaluating the sums over the nuclear-spin states gives for
$\beta\gamma_n H \ll 1$,
$$
\langle I_z \rangle = \beta\gamma_n \hbar I(I+1)[H+\sum_k (a_k \langle S_{kz} \rangle_0)].
$$

 The only requirement for the expression (42) to be valid is that
$\beta\mu_N g \sum_k a_k \ll 1$. The physical interpretation of (43) is
simple. Clearly, the magnetic susceptibility for the free nucleus is
$$
\chi_n = \beta(\gamma_n \hbar)^2 I(I+1),
$$
 and the effect of the
hyperfine coupling is to provide an internal magnetic field of magnitude
$H^\prime=\sum_k(a_k\langle S_z \rangle_k)_0$. For the free electrons in a
metal, $\sum_k(a_k\langle S_z \rangle_k)_0$ is evaluated[^20] with the
help of the definition of the $a_k$ and the Pauli theory of
paramagnetism in metals, to yield $H^\prime=H_z(8\pi\mu_B^2/E_F)n(0)$, where
$E_F$ is the Fermi energy of the metal at absolute zero, and
$n(0)=\langle\sum_k |\psi_k(0)|^2\rangle_0$. These internal fields give
arise to the Knight shift[^21] in the nuclear magnetic resonance in
metals. The internal field here gives a small correction to the applied
field, so that the problem could as well be treated by a perturbation
theory for the energy levels. On the other hand, in a hydrogen-like
atom, if the electron is in its ground state, one easily finds[^20]
$$
H^\prime=(a\langle S_z \rangle_0) = (\beta H \mu_B)(8/3)\mu_B Z^3/a_0^3,
$$
 where
$a_0$ is the Bohr radius and $Z$ the atomic number of the nucleus. These
fields give rise to a method of polarizing nuclei suggested by
Rose and Gorter.[^22] At temperatures of the order of 1$^\circ$K, such
internal fields may be $10^5$ or $10^6$ times as large as the external
field. Still, the present perturbation theory would be applicable and
second-order terms negligible, although it would not be appropriate to
use the usual perturbation theory for energy levels. As these examples
indicate, the method employed here can provide a unified derivation of
some phenomena which are usually treated by diverse methods.
### Electronic Gyromagnetic Effects
The results of the preceding sections are now applied to the analysis of
electronic gyromagnetic effects. We wish to evaluate the combined effect
of a macroscopic rotation of a substance and of an external magnetic
field on the angular momentum of the electrons and on the
atomic-magnetic moment. Only the effects linear in the magnetic field
and the rotation are considered, practically limiting the theory to
magnetically dilute systems.

Let $\mathcal{H}_0$ be the Hamiltonian of a stationary crystal in the
absence of any external field. The crystal is rotating about a fixed
direction with angular velocity $\omega$ and has an external magnetic
field $H$ acting on it. We introduce coordinates fixed with respect to
the crystal, and distinguish all operators expressed in the rotating 
coordinates by an asterisk. More explicitly, by a vector operator $A^*$ 
we mean one whose components $A_i^*$ are found by computing the components 
$A_i$ in the laboratory frame and projecting onto rotating axes. In view 
of (18) and (23), the density matrix of the system may be written in the 
form (25) with 
$$
\begin{aligned}
A &= -\beta\mathcal{H}_0^*, \nonumber \\\\ B &= \beta\left[\frac{e}{2mc}(L+2S)^*\cdot H^*(t) \right. \nonumber \\\\ & \quad \left. - \frac{e^2}{8mc^2} \sum_k r_k^* \times H_k^*(t) \cdot r_k^* + J\cdot\omega \right].
\end{aligned}
$$

 The time dependence of $H^*(t)$ arises because a field
which is fixed in space will be seen as a rotating field in the
rotating-coordinate system. While $\mathcal{H}_0$ would be expected to
have an implicit time dependence due to the rotation, the Hamiltonian
$\mathcal{H}_0^*$ referred to body-fixed axes keeps the
relative-position vector of particles approximately independent of the
rotation, and no implicit time dependence is expected. We calculate the
magnetic moment $\langle M^* \rangle$ and the angular momentum
$\langle J^* \rangle$; these vectors, like $H^*(t)$, are related to the
laboratory frame, if the axis of rotation is the 3 direction, by the
relation
$$
\begin{pmatrix} v_1^* \\\\ v_2^* \\\\ v_3^* \end{pmatrix} = \begin{pmatrix} \cos{\omega t} & \sin{\omega t} & 0 \\\\ -\sin{\omega t} & \cos{\omega t} & 0 \\\\ 0 & 0 & 1 \end{pmatrix} \begin{pmatrix} v_1 \\\\ v_2 \\\\ v_3 \end{pmatrix}.
$$

 If the $\cos{\omega t}$ and $\sin{\omega t}$ are treated as C numbers,
the commutation rules for vectors in the rotating system are the same as
that in the fixed system; the transformation (45) is then, in fact,
equivalent to the unitary transformation (2) for vector operators,
although not for classical quantities such as the magnetic field. If the
$\cos{\omega t}$ and $\sin{\omega t}$ are regarded as the components of
a vector giving the relative orientation of physical particles (or a
quasi-particle such as the center of mass of the system), they do not
commute with $J$. In that case, the angular-momentum, commutation rules
become in the rotating system[^17] $[J_x^*, J_y^*] = -iJ_z^*$, etc.,
instead of the usual $[J_x, J_y]=iJ_z$, etc. Note the minus sign.
Applying the perturbation expansion (30) to (44), considering only the
term linear in $B$, yields for the expectation value of $J_i^*$ and
$M_i^* = -\partial\mathcal{H}/\partial H_i$: 
$$
\begin{aligned}
\langle M_i^* \rangle &= -\frac{e}{2mc}\langle L_i^*+2S_i^* \rangle_0 = \sum_{j=1}^3 \chi_{ij}H_j^*(t)+\theta_{i3}\omega, \nonumber \\\\ \langle J_i^* \rangle - \langle J_i^* \rangle_0 &= \sum_{j=1}^3 \theta_{ij}^\prime H_j^*(t)+\eta_{i3}\omega,
\end{aligned}
$$
 where 
$$
\begin{aligned}
\chi_{ij} &= \beta \left(\frac{e}{2mc}\right)^2 \int_0^1 dx \langle e^{-A^*} (L_i^*+2S_i^*) e^{A^*} (L_j^*+2S_j^*) \rangle_0 \nonumber \\\\ & \quad -\beta(e/2mc)^2\langle(L_i^*+2S_i^*)\rangle_0 \langle(L_j^*+2S_j^*)\rangle_0 \nonumber \\\\ & \quad + (e^2/4mc^2)\sum_k \langle x_i^* x_j^* - \delta_{ij} (r^*)^2 \rangle_0, \nonumber \\\\ \theta_{i3} &= \beta\frac{e}{2mc}\int_0^1 dx \langle e^{-A^*} J_3^* e^{A^*} (L_i^*+2S_i^*) \rangle_0 \nonumber \\\\ & \quad -\beta\frac{e}{2mc} \langle J_3^* \rangle_0 \langle L_i^*+2S_i^* \rangle_0, \nonumber \\\\ \theta^\prime_{ij} &= \beta\frac{e}{2mc}\int_0^1 dx \langle e^{-A^*} (L_i^*+2S_i^*) e^{A^*} J_j^* \rangle_0 \nonumber \\\\ & \quad -\beta\frac{e}{2mc} \langle L_i^*+2S_i^* \rangle_0 \langle J_j^* \rangle_0, \nonumber \\\\ \eta_{i3} &= \beta \int_0^1 dx \langle e^{-A^*} J_3^* e^{A^*} J_i^* \rangle_0 - \beta\langle J_3^* \rangle_0 \langle J_i^* \rangle_0.
\end{aligned}
$$

 From the identity (35), it follows that these
coefficients have certain symmetry properties:
$$
\theta_{ij} = \theta^\prime_{ji}; \quad \chi_{ij}=\chi_{ji}; \quad \eta_{ij}=\eta_{ji}.
$$

 In deriving (46) and (47), it was assumed that the system is in
thermodynamic equilibrium; but, the system is generally in the presence
of a time-dependent field $H^*(t)$ so that the assumption is not
generally justified. The time-dependent behavior is discussed in Sec. 4.
However, the equilibrium treatment is applicable in several important
cases.
1.  The field is parallel to the axis of rotation (only the transverse
    components have a time dependence).
2.  The transverse components are made to rotate with the crystal, so
    that again there is no time dependence.
3.  The rotation is so slow that the longest relaxation time of the
    system is very small compared to the period of rotation. Then the
    system continues in a time-varying equilibrium.
4.  The rotation is so rapid that the shortest relaxation time of the
    system is very large compared to the period of rotation. In this
    case, the spins and particles do not have time to respond to the
    rapidly changing, transverse field, and only the field in the
    3-direction should be considered in Eq. (46).

The usual Einstein-deHaas and Barnett effects[^4] are already included in
the case of a field parallel to the axis of rotation. For analysis of
these effects, we require further that the system have sufficient
symmetry (e.g., reflection symmetry across a plane passing through the 3
axis is sufficient), so that the off-diagonal elements of the tensors 
(47) all vanish. In addition, it is assumed that the unperturbed crystal
is unpolarized. Finally, diamagnetism is neglected.

The Eqs. (46) become, with these simplifications, 
$$
\begin{aligned}
\langle M_3 \rangle = \chi_{33} H_3 + \theta_{33}\omega, \nonumber \\\\ \langle J_3 \rangle = \theta^\prime_{33} H_3 + \eta_{33}\omega,
\end{aligned}
$$
 with 
$$
\begin{aligned}
\chi_{33} &= \beta\left(\frac{e}{2mc}\right)^2 \int_0^1 dx \langle e^{-A*}(L_3+2S_3)e^{A*}(L_3+2S_3)\rangle_0, \nonumber \\\\ \theta_{33} &= \theta^\prime_{33} = \beta\frac{e}{2mc} \int_0^1 dx \langle e^{-A*}(L_3+2S_3)e^{A*}J_3\rangle_0, \nonumber \\\\ \eta_{33} &= \beta \int_0^1 dx \langle e^{-A*}J_3 e^{A*}J_3\rangle_0.
\end{aligned}
$$

 In the usual Einstein-deHaas type of experiment, a
magnetic field $H_3$ induces a magnetic moment $\langle M_3 \rangle$ in
a solid which is measured, and it also induces an electronic angular
momentum $\langle J_3 \rangle$. This internal angular momentum must be
balanced[^24] by a macroscopic rotation
$Q\omega_E = -\langle J_3 \rangle$, with $Q$ the moment of inertia about
the 3 axis. Measurements then yield the $g^\prime$ factor
$$
(e/2mc)g^\prime_E = \langle M_3 \rangle / Q\omega_E = \langle M_3 \rangle / \langle J_3 \rangle = \chi_{33}/\theta_{33}.
$$

In the Barnett experiments, the angular velocity $\omega_B$ is
impressed, and a resulting polarization observed. The angular velocity
is compared to an equivalent field $H_B$ which produces the same
polarization. The Barnett coefficient
$$
(e/2mc)g^\prime_B = \omega_B/H_B = \frac{\langle M_3 \rangle/\theta_{33}}{\langle M_3 \rangle/\chi_{33}} = \frac{\chi_{33}}{\theta_{33}}.
$$

The equality $g^\prime_B=g^\prime_E=g^\prime$ arises from the equality of $\theta_{33}$
and $\theta^\prime_{33}$, which is a direct consequence of the relation (35). In
the present (linear) approximation, $g^\prime_E$ and $g^\prime_B$ are independent
of the field strength or angular velocity, but may have a temperature
dependence. Numerical evaluation of $g^\prime$ has been carried out by Van
Vleck and Frank,[^25] by Arajs et al.[^26] for rare-earth salts, and by
Gorter and Kahn[^27] particularly for salts containing ions of the iron
group. Van Vleck, Frank, and Arajs assume that $J_z$ commutes with
$\mathcal{H}^{(0)}$, so that
$$
\theta = (e/2mc)\beta\langle(L_z+S_z)(L_z+2S_z)\rangle_0.
$$

 This is a
good assumption for the rare-earth salts, since the $4f$ electrons
responsible for the magnetism are well inside the atoms and only very
weakly coupled to other atoms with which they could exchange angular
momentum; in addition, these authors assume Russell-Saunders coupling
for the atom.[^28] With only these assumptions, $g^\prime$ has been evaluated
for Eu$^{3+}$ and Sm$^{3+}$ by Frank for various temperatures. Theory and
experiment[^28] are in agreement insofar as experimental data are
available. For the other rare-earth ions, the calculation for room
temperatures is simplified, because the multiplet splitting (same $L$
and $S$, different $J$) is large compared to $kT$. If, further, the
off-diagonal elements of $(L_z+2S_z)$ are neglected in a representation
where $\mathcal{H}_0$ is diagonal, it is found from (39) and (51) that
$g^\prime=g$, the usual Lande splitting factor associated with the ground
state of the ion:
$$
g = \frac{3}{2} + \frac{S(S+1)-L(L+1)}{2J(J+1)}.
$$

 This
simple formula agrees with the experimental results quite well for all
the rare-earth salts, except those involving Eu$^{3+}$ or Sm$^{3+}$. To
illustrate the situation, we take the case of Nd$^{3+}$ where $g=0.73$; the
evaluation of $g^\prime$ without assuming large multiplet splitting or
negligible off-diagonal elements gives $g^\prime=0.76$; the experiments of
Sucksmith on Nd$_2$O$_3$ give values of $g^\prime$ ranging from 0.74 to 0.83, the
mean value for the experimental results being 0.77, in good
agreement with Van Vleck theory. Arajs and co-workers have extended the
calculations of Frank for Eu$^{3+}$ and Sm$^{3+}$ to higher temperatures, up
to 2000$^°$K. They also have evaluated the $g^\prime$ for the other
tri-positive rare-earth ions in the temperature range from 10$^°$K
to 2000$^°$K. They find that Eu$^{3+}$ (six $4f$ electrons) has by far
the largest $g^\prime$ value at room temperature, but it falls off with
increasing temperatures; the $g^\prime$ for Sm$^{3+}$ (five $4f$ electrons)
increases with temperature, reaches a maximum at about 1000$^°$K,
and then decreases. The $g^\prime$ values for the tripositive, rare-earth ions
having from one to four $4f$ electrons increase monotonically with
temperature, whereas those for ions with more than six $4f$ electrons
are practically independent of temperature. No high-temperature
experimental measurements of $g^\prime$ for these tripositive ions are
available.

Gorter and Kahn have worked out a procedure for calculating $\theta$,
without the simplification (53); $J_3$ and $\mathcal{H}_0$ need not
commute. However, they assume, in analogy to the Van Vleck theory for
susceptibilities, that one has Russell-Saunders coupling and that
multiplet splitting is either large compared to $kT$ or small compared
to $kT$. In evaluating $g^\prime$ for salts of the iron group, it is assumed
that the crystalline-field splitting is much larger than the $L\cdot S$
splitting; the former is in lowest approximation assumed to quench
completely the magnetism due to orbital motion; then the $L\cdot S$
coupling is treated as a perturbation. The perturbation parameter
$\alpha$ is a measure of the relative strength of spin-orbit coupling to
the crystal field. In terms of this parameter, the magnetic
susceptibility obtained is $\chi=(e/2mc)^2\beta S(S+1)(2+\alpha)^2$, and
the $g^\prime$ value is $g^\prime=(2+\alpha)/(1+\alpha)$. The values of $\alpha$
obtained from susceptibility measurements are then employed to predict
$g^\prime$ values. Agreement is satisfactory[^27] for Cr$^{3+}$, Mn$^{2+}$, Fe$^{2+}$,
and Co$^{2+}$, although for Co$^{2+}$ the application of perturbation theory
is questionable, and $\alpha$ is rather large, around 0.5. The $g^\prime$ for
Ni$^{2+}$ and Cu$^{2+}$ were evaluated by these authors, but no measurements
are available.

Although the theory presented here is primarily for paramagnetic
materials, for completeness we summarize the status of the theory of the
gyromagnetic ratio for ferromagnetic and other materials. For
ferromagnetic materials, it has been shown first by Kittel[^30] and
proved quite generally by Van Vleck[^31] that the magnetomechanical
factor $g^\prime$ is related to the spectroscopic-splitting factor $g$ which
occurs in the theory of ferromagnetic-resonance experiments by the
relation $g^\prime=g/(g-1)$, or approximately $g-2 \approx 2-g^\prime$. This is
proved by assuming again that the orbital angular momentum is nearly
quenched. It is irrelevant whether quenching is due to exchange coupling
or due to the crystal field. If $M_z=(e/2mc)(L_z+2S_z)$, i.e., if
diamagnetism may be neglected, and $J_z=L_z+S_z$, then one has
$g^\prime=(2mc/e)\langle M_z \rangle / \langle J_z \rangle = (2+\alpha)/(1+\alpha)$, where
$\alpha=\langle L_z \rangle / \langle S_z \rangle \ll 1$. In
microwave spectroscopy, one observes energy levels $E=E_0+\mu_B gMH$,
where $M$ is an integer eigenvalue of the component of the total spin in
the direction of the field. The splitting factor $g$ is equal to 2 in
the case of no orbital contribution. In Van Vleck's calculation, the
spin-orbit coupling and the effect of the external field on the orbital
angular momentum are treated as a perturbation. Using second-order
perturbation theory, he finds $g=2+\alpha$. The result is valid even
when exchange interactions, dipole interactions between spins, and any
other interactions which commute with $S$ are included. The available
experimental data are summarized in Table I.

| Material | Magnetic-resonance measurements $g$ | $g/(g-1)$ | Gyromagnetic-effect measurements $g^\prime$ |
| :--- | :--- | :--- | :--- |
| Fe | 2.11 | 1.90 | 1.92 |
| Co | 2.20 | 1.83 | 1.85 |
| Ni | 2.21 | 1.83 | 1.84 |
| Permalloy | 2.11 | 1.90 | 1.91 |
| Supermalloy | 2.10 | 1.91 | 1.91 |
| Heusler Alloy | 2.01 | 1.99 | 1.99 |
| Magnetite | 2.20 | 1.83 | 1.93 |
| Mn Sb | 2.10 | 1.91 | 1.98 |

**Table I:** Comparison of experimental g values and g' values.[^32]

The data indicate satisfactory agreement with the relation $g/(g-1)=g^\prime$,
for Fe, Ni, Co, and the alloys. A few years ago it appeared that
discrepancies existed for these metals and alloys. However, the recent
precision measurements of the Einstein-deHaas effect seem to have
removed the discrepancies. For the chemical compounds Fe$_3$O$_4$ and
MnSb, the experiments indicate that $g/(g-1) \neq g^\prime$. Possible origins
of deviations from this relation have been discussed by Van Vleck[^31]
and by Kittel and Mitchell,[^33] although not specifically in connection
with these compounds. Further theoretical study is needed to understand
quantitatively and qualitatively the relation between $g$ and $g^\prime$ for
them.

For diamagnetic ionic crystals, one expects no gyromagnetic phenomena
because the $\theta_{ij}$ and $\theta^\prime_{ij}$ of Eq. (47) contain no
diamagnetic contribution as the susceptibilities do. Gyromagnetism due
to conduction electrons has been discussed by Broer,[^34] although it is
too small to be observable in ordinary metals by present techniques.
However gyromagnetic experiments have been performed[^35] on
superconducting lead; these experiments give $g^\prime=1.0$ for the conduction 
electrons in magnetic fields below the threshold value at which the 
resistivity of lead has a measurable magnitude.

Magnetomechanical effects are not necessarily restricted to solids, but
would also be expected in liquids and gases, in which the atoms or
molecules have a magnetic moment. Gorter and Kahn point out that
molecules in a gas can exchange angular momentum through collisions with
the walls of the vessel in which the gas is contained, so that we should
be able to detect gyromagnetic effects in paramagnetic gases such as
oxygen and nitric oxide. In the Einstein-deHaas effect, we would observe
a rotation $\omega_E$ of the vessel.
### Polarization of Nuclear Spins in a Crystal
Since most nuclei, like electrons, posses both a spin angular momentum
and a parallel magnetic moment in their ground state, and since angular
momentum can be exchanged between nuclear spins and lattice motion, we
expect at least in principle that polarization of nuclei by the rotation
of a macroscopic sample, the nuclear analog of the Barnett effect, is
possible. The polarization of nuclei by a magnetic field requires a
means for balancing the angular momentum acquired by the nuclei. One
such means is the rotation of the whole lattice. This occurrence is the
nuclear analog of the Einstein-deHaas effect. We discuss in the
following the polarization of nuclei due to the simultaneous action of
an external field and a rotation, thus including both effects. The
coupling of the nuclear spins with the crystal environment is treated as
a perturbation, whereas the action of the field and the rotation on the
uncoupled nucleus are treated exactly. In evaluating the polarization of
the nuclear spins, the simplifying assumption is made that in the
stationary crystal the nuclei have no orbital angular momentum.

Consider a single-spin operator $I$ expressed in units of $\hbar$ with
moment $\mu g I$ and in an external field $H$ contained in a rotating
crystal which is at temperature $\beta$. If the coupling between the
spin and the surroundings is neglected, the density matrix, in view of
(18) and (23) is
$$
\rho_I = (1/Z)\exp(\beta\mu g I\cdot K), \quad \text{where } K_i = H_i+\omega_i/\gamma,
$$
 the $K_i$ are the components of the effective magnetic field due to the
combined action of the external field and the angular velocity $\omega$
of the crystal. We leave off the subscript $n$ from $\gamma_n$ in the
rest of this paper. The expectation value for the component $I_{||}$
along the direction $K$ is
$$
\langle I_{||} \rangle = (I+\tfrac{1}{2})\coth[a(I+\tfrac{1}{2})] - \tfrac{1}{2}\coth(a/2) \approx \tfrac{1}{3}aI(I+1), \quad \text{if } Ka = \beta\mu g K \ll 1.
$$

 The expectation value $\langle I_{||} \rangle$ is time-independent; the
perpendicular component has zero expectation value. $I$ is the spin of
the nucleus in its ground state. The effects of rotation and magnetic
field are additive according to (55) if $a \ll 1$, and for any value of
$a$ are correctly described by a total effective field $K$. The moment
of inertia $\eta_V$, defined by $\langle I \rangle=f_V\omega$, and the
nuclear susceptibility are related:
$$
\chi_\nu = \gamma\eta_\nu = \beta(\mu g)^2 I(I+1).
$$

 To include the
interaction of a single nuclear spin with the internal fields due to all
the rest of the crystal, we treat the uncoupled system "spin plus
remainder of crystal" as the zeroth approximation, and regard the
coupling between the spin and the crystalline fields as a perturbation,
which must be small compared to $kT$. The calculation is carried out in
the laboratory coordinate system in which the effective, external
magnetic field $K$ is constant. The perturbation Hamiltonian
$\mathcal{H}_{12}$ will in general have an implicit time dependence,
which is discussed further on. In applying the perturbation expansion
(30), we choose 
$$
\begin{aligned}
A &= -\beta(\mathcal{H}_0-H\cdot M - \omega\cdot J - \mu g K\cdot I), \nonumber \\\\ B &= -\beta\mathcal{H}_{12}, \nonumber \\\\ \Gamma &= I - \langle I \rangle_0.
\end{aligned}
$$

 Here, $\mathcal{H}_0$ is the uncoupled Hamiltonian of
the crystal in the absence of the magnetic field and the rotation.
$\langle I_z \rangle_0$ is given by (55) and
$\langle I_\pm \rangle_0=0$. $M$ and $J$ are the magnetic-moment and
angular-momentum operators for the crystal excluding the particular
nuclear spin of interest. To calculate $\langle\Gamma_z\rangle$, Eq.
(31) is applied, neglecting $Q$; to obtain $\langle I_\pm \rangle$, the
corresponding approximation is made in Eq. (30). Thus one obtains,
$$
\langle\Gamma_z\rangle = \beta\langle\mathcal{H}_{12}I_z\rangle_0 + \beta^2(\langle\mathcal{H}_{12}^2 I_z\rangle_0 - 2\langle\Gamma_z\mathcal{H}_{12}\rangle_0\langle H_{12}\rangle_0),
$$
$$
\langle I_\pm \rangle = -\beta(1\pm\sigma)\langle\mathcal{H}_{12}I_\pm\rangle_0 + \beta^2\langle[\Gamma I_{12}(\sigma/a)] \times (\mathcal{H}_{12} I_\pm)_0 - [\Gamma I_0]\langle\mathcal{H}_{12}I_\pm\rangle_0\langle\mathcal{H}_{12}\rangle_0\rangle,
$$
 where $a=\beta\mu gK$; $\sigma=(1-e^{-a})/a-1 \approx -\frac{1}{2}a$;
and $I_\pm = I_x \pm i I_y$. The $z$ direction is chosen parallel to
$K$. To derive (58), we use the commutation relations
$$
[e^{cI_z}, I_\pm] = \pm(e^c-1)I_\pm e^{cI_z},
$$
 where $c$ is any
complex number. These relations are easily verified in any explicit
representation of the $I_z$ and $I_\pm$. The Hamiltonian
$\mathcal{H}_{12}$ is a sum of interactions. In the linear
approximation, only those terms can make a contribution which have a
dependence on the components of $I$. These terms are:
1.  the magnetic-dipole coupling between nuclei
$$
    \mathcal{H}^{(1)} = - \mu^2 g^2 \sum_\alpha \left[ \frac{I \cdot I_\alpha}{R_\alpha^3} - 3 \frac{(R_\alpha \cdot I)(R_\alpha \cdot I_\alpha)}{R_\alpha^5} \right];
$$
2.  the coupling with electron spins of unpaired electrons
$$
    \begin{aligned}
    \mathcal{H}^{(2)} &= -(8\pi/3)g_e\mu_B\gamma_e \sum_m \delta(r_m)I\cdot S_m - g_e\mu_B\gamma_e \sum_{m} \left[ \frac{I\cdot S_m}{r_m^3} - \frac{3(I\cdot r_m)(S_m\cdot r_m)}{r_m^5} \right];
    \end{aligned}
$$
3.  the interaction due to the electric-quadrupole moment of the
    nucleus[^36]
$$
    \mathcal{H}^{(3)} = -\frac{1}{6} \sum_{i,k} Q_{ik} \frac{\partial^2\phi}{\partial x_i \partial x_k}, \quad Q_{ik} = C[I_iI_k+I_kI_i - \delta_{ik}I^2]
$$
 with the constant $C=eQ/I(2I-1)$; and
4.  the interaction between the nuclear magnetic moment and the orbital
    motion of the electrons[^37]
    in the presence of the external field,
$$
    \mathcal{H}^{(4)} = -\mu g \frac{e}{mc} \sum_m \frac{r_m \times p_m}{r_m^3}\cdot I - \frac{e}{2c}H\cdot r_m - (\mu g) \frac{e^2}{8mc^2} \sum_m \left[I\times\frac{H\times r_m}{r_m^3} \right].
$$

 The notation used is the conventional one. In the first term of (61),
the sum is over $S$ electrons and $\delta(r_m)$, the Dirac delta
function which vanishes unless the electron is at the nucleus; the
second sum in $\mathcal{H}^{(2)}$ is over electrons other than $S$
electrons. In (62), $x_i$ and $x_k$ are the Cartesian coordinates of the
nuclear charge of the nucleus of interest, $Q_{ik}$ is an operator,
$\phi$ is the electrostatic potential, and $Q$ is the quadrupole moment
of the nucleus. $\mathcal{H}^{(4)}$ is obtained if it is assumed the
$m$th electron is in the combined external and nuclear field
$H_m=H+\mu g \mathrm{grad}(I\cdot\nabla 1/r_m)$, and the vector
potential is taken to be
$A_m=\frac{1}{2}H\times r_m - \mu g I \times \nabla(1/r_m)$. The $r_m$
is the position vector of the $m$th electron relative to the nucleus to
which it is bound.

Unlike the calculation of the electronic gyromagnetic effects, we have
here expressed the Hamiltonian in the stationary frame. The rotation
means that the nuclear position coordinates will in fact rotate in
space; if the rotation is sufficiently slow and the external field
produces an effect on the electron motion which is small compared to the
electrostatic crystal fields, the electron coordinates will also rotate
with the same frequency $\omega$. The nuclear-spin orientation $I$ in
effective, external, magnetic fields of a magnitude customary in nuclear
magnetic resonance experiments is primarily determined by the effective
external field and is little influenced by the changing, internal,
magnetic fields. The orientation of unpaired electronic spins is again
primarily determined by the effective, external-field direction rather
than the relatively weak, internal, magnetic fields.[^38] The fact that
the spin of interest is subject to an internal magnetic field which
varies systematically with time indicates that the assumption of
thermodynamic equilibrium can be expected to hold only in some cases, such
as any of the following:
1.  The internal magnetic field has cylindrical symmetry about the axis
    of rotation.
2.  The longest relaxation time is much shorter than the period of
    rotation. The equilibrium polarization will in that case vary slowly
    with time, as in the corresponding electronic case. The dominant
    part of $\langle I \rangle$, namely, $\langle I_z \rangle$, will
    remain constant.
3.  The shortest relaxation time is much longer than the period of
    rotation. The internal fields perpendicular to $\omega$ are
    effectively replaced by their average value in this case.

With these reservations, the first order to $\langle I_z \rangle$, in
view of (57) and (60) to (63), are found to be
$$
\langle I_z \rangle - \langle I_z \rangle_0 = -\beta\mu g(H^I+H^S+H^{S^\prime}+H^P+H^D)\times\langle I_z^2\Gamma \rangle_0 - \beta(D_1+D_2)\langle I_z^2\Gamma \rangle_0,
$$
 with the following expressions for the quantities in (64) (see Appendix
C): 
$$
\begin{aligned}
\langle I_z^2 \rangle_0 &= I(I+1)/3; \\\\ \langle I_z^2\Gamma \rangle_0 &= [aI(I+1)/45][4I(I+1)-3].
\end{aligned}
$$
 $H^I$ is the average field in the $z$ direction due to
other polarized nuclear spins,
$$
H^I = \mu g \sum_\alpha \left\langle \frac{\langle I_\alpha \rangle_z}{R_\alpha^3} - \frac{3Z_\alpha(R_\alpha \cdot I_\alpha)}{R_\alpha^5} \right\rangle_0
\tag{65a}
$$

 If all the nuclei are similar to the one of interest, and
the external field is large compared to internal magnetic fields, this
may be written in terms of the angle $\theta_\alpha$ which the
relative-position vector $R_\alpha$ makes with the $z$ axis:
$$
H^I \approx I(I+1)\beta\mu g H \sum_\alpha \langle(1-3\cos^2\theta_\alpha)/R_\alpha^3\rangle_0. 
\tag{65b}
$$

 The internal field $H^S$ due to nearby unpaired electron
spins for all but s electrons is
$$
H^S = -\gamma_e \sum_{\substack{\text{electrons} \\\\ r_i \neq 0}} \left\langle \frac{\langle S_i \rangle_z}{r_i^3} - \frac{3z_i(r_i \cdot S_i)}{r_i^5} \right\rangle_0,
$$
 and the internal field due to the s electrons,
$$
H^{S^\prime} = (8\pi/3)\gamma_e \sum_s \langle \delta(r_i)S_{iz} \rangle_0.
$$

 This
field $H^{S^\prime}$ is the hyperfine field already discussed and shown
to be responsible for the Knight shift in metals, and the Rose-Gorter
polarization in paramagnetic ions. In the presence of the rotation as
well as the external field, the expressions given there for this
internal field must be generalized to
$H^{S^\prime} \approx 8\pi\mu_B |\psi_k(0)|^2 \times (\mu_e H_z + \hbar\omega_z)/E_F$
for free electrons in a metal, and
$H^{S^\prime} \approx (8/3)\beta(\mu_e Z^3/a_0^3)(\mu_e H_z + \hbar\omega_z)$
for a hydrogen-like atom or ion. The magnetic moment due to orbital
angular momenta $L^\prime$ of the individual electrons gives rise through
$\mathcal{H}^{(4)}$ to the internal field
$$
H^P = \frac{\mu_B}{\hbar} \sum_i \left\langle \frac{L^\prime_{iz}}{r_i^3} \right\rangle_0,
$$
 where, in evaluating the expectation value, it must be remembered that
the electrons are in an effective external field
$(H+\hbar\omega/\mu_e)$. Also, from $\mathcal{H}^{(4)}$, there arises
the field
$$
H^D = -\frac{e^2}{2mc^2}\sum_i \left\langle H\left[\frac{y_i^2}{r_i^3} - \frac{y_i^2}{r_i^3}\right] - H_z \frac{x_i^2+y_i^2}{r_i^3} + H\left[\frac{x_i^2+y_i^2}{r_i^3}\right]\right\rangle_0.
$$

 For the spin of a nucleus in an atom with a spherically symmetric charge
distribution, only the last term in (70) will contribute. The direction
of the internal field is in this case opposite to that of $K$. For
$I > \frac{1}{2}$, the $D_1$ and $D_2$ terms can contribute. $D_1$
depends on the nuclear quadrupole moment:
$$
D_1 = -\frac{eQ}{2I(2I-1)} \left\langle \frac{\partial^2\phi}{\partial x^2} + \frac{\partial^2\phi}{\partial y^2} - 2\frac{\partial^2\phi}{\partial z^2} \right\rangle_0 = -\frac{3eQ}{2I(2I-1)} \left\langle \frac{\partial^2\phi}{\partial z^2} \right\rangle_0.
$$

 The last expression is legitimate because the s electrons do not
contribute to the quadrupole interaction, and the charge density at the
nucleus due to p or d electrons $\nabla^2\phi$ is negligibly small. The
quantity $D_2$ has the value
$$
D_2 = -(\mu g)\sum_{\text{elec}} \frac{e}{16mc^2} \left\langle \frac{1-3\cos^2\theta_i}{r_i^3} \right\rangle_0.
$$

 It is a small interaction of the nonspherical part of the electron cloud
with the nuclear-magnetic moment. Each of the terms in (64) is related
to previously known effects, many of which have been observed and
evaluated theoretically in detail. The field $H^I$ is known[^39] to cause
splitting of magnetic-resonance lines in unsymmetrical configurations.
If the crystal is rotating, the vector $R_\alpha$ also rotates, so that
the splittings depending on the components of $R_\alpha$ perpendicular
to the axis of rotation will be washed out.[^40] The term $H^S$ produces
an anisotropic line shift, which is however zero in crystals with cubic
symmetry. The field $H^S$ must also include the effect of the
second-order, pseudodipolar coupling, which has, for example, been
studied by Bloembergen and Rowland.[^41] This is shown by treating the
contact interaction between the electron spin $S$ and nuclear spin $I_a$
as a perturbation in the exponent of the density matrix $\rho_0$ in
evaluating the expectation values (66), and by then calculating the
linear term in the perturbation according to (30). In this way, we find
for an electron of spin $S$ coupled with a nuclear spin $I$ other than
the spin of interest:
$$
\left\langle \frac{S_z}{r^3} - \frac{3z(r\cdot S)}{r^5} \right\rangle_{00} - \left\langle \frac{S_z}{r_a^3} - \frac{3z_a(r_a \cdot S)}{r_a^5} \right\rangle_{00} - (4\pi/3)\mu_e\mu_g\beta\langle I_a^z \rangle_{00} \left\langle \frac{1-3\cos\theta_{0a}}{R_{0a}^3} \right\rangle_{00} + \dots
\tag{73}
$$

 Here, the 00 means that the expectation value is taken over
the density matrix $\rho_{00}$ unperturbed by the $I_a \cdot S$
coupling. Comparison of the second term in (73) with (65b) shows its
resemblance to a direct, nuclear, dipole-dipole interaction. Integrals
over commutators of the form $[\rho_{00}, (r-R_a)S \cdot I_a]$ are
neglected in deriving (73). For the Knight shift $H^{S^\prime}$, much detailed
knowledge is available for nonrotating crystals, and values of
$H^{S^\prime}/H$ are in the literature[^42] for a large number of metals. In
many cases, the magnitude of $H^{S^\prime}/H$ is of the order of $1/100$. If
the crystal is rotating, the correction is unchanged, except that $H$ is
replaced by $H_z+(\hbar\omega_z/\mu_e)$. If $H^{S^\prime}$ is evaluated in
just the same way as $H^S$ in Eq. (73), with
$\beta\mu_g(8\pi\gamma_e/3)\delta(r_a-R_a)I\cdot S_a$ treated as a
perturbation, one finds,
$$
\begin{aligned}
\langle H^{S^\prime}I_z\Gamma\rangle_{00} &= (8\pi\gamma_e/3)\sum_a\langle\delta(r_a)S_a^z\rangle_{00} \langle I_z\Gamma \rangle_{00} \nonumber \\\\
& \quad + (8\pi\gamma_e/3)^2\mu_e\beta_e\langle\alpha I_z\Gamma \rangle_{00}\sum_a \langle[\delta(r_a-R_a)S_z]_{00}
\nonumber \\\\
& \quad \times [\langle\delta(r_a-R_a)S_z\rangle_{00}\langle S_z\rangle_{00} - \langle S_z S_z\delta(r_a)\delta(r_a-R_a)\rangle_{00}] \rangle.
\end{aligned}
$$

 The second term in (74) is, in effect, like an exchange
interaction between nuclear spins $I$ and $I_a$. Here $r_a$ is the 
position vector of electron $k$, the nucleus of interest being taken as
the origin. In a metal, if an electron has a finite probability of being
at nucleus $a$ as well as at the nucleus of interest, the effective-exchange
term can give a contribution for $i=k$. This kind of pseudo-exchange effect
has been derived by Rudermann and Kittel.[^43] It is possible to obtain a
contribution if $i \neq k$, provided the two electrons are strongly coupled
to each other, as for example by an electron-exchange interaction.[^44] 
Without any correlation between the electrons, the effective-exchange term
is zero. If the electron, nuclear, dipole-dipole interaction were treated
as the perturbation in evaluating $H^{S^\prime}$, we should again obtain a
pseudo-dipolar term something like (73).

The field $H^P$ [Eq. (69)] is seen from (69) to have the simple, physical
significance of the field due to polarization of the magnetic moments
due to the orbital motion of the electrons. It is closely related to the
shielding effect obtained by Ramsey,[^45] which is known as the chemical
shift. This relation is shown by writing
$$
\rho_0 = \exp[-(\mathcal{H}_{00}-\mu_B L\cdot H^\prime)]/z_0,
$$
 where
$H^\prime = H+1/\mu_B \hbar\omega$, and $z_0$ is the partition function, and
then treating $\beta\mu_B L\cdot H^\prime$ as a perturbation. If
$\rho_{00}=\exp(-\beta\mathcal{H}_{00})/z_{00}$, application of (30) to
(69) yields in a representation in which $\mathcal{H}_{00}$ is diagonal
and has eigenvalues $E_n$ for the term linear in
$\beta\gamma_n L\cdot H^\prime$, 
$$
\begin{aligned}
H^P &= -\frac{\gamma_e\hbar}{2}\mathrm{Re}\sum_n\sum_m (\rho_{00})_{nn} \frac{\sum_k (L_{k,nm}H^\prime_{nm})(L_{k,mn}^\prime/r_{mn}^3)}{E_n-E_m} \nonumber \\\\ & \quad + \mu_e\beta \sum_n (\rho_{00})_{nn} \sum_k [(L_{k,nn}^\prime H^\prime_{nn})L_{k,nn}^\prime/r_{nn}^3];
\end{aligned}
$$
 Re means "real part of." As Ramsey points out, the
calculation of this effect is very similar to that of the Van Vleck
theory of paramagnetism. Ramsey's shielding correction corresponds to
the double sum in (75). In obtaining (75), it is assumed that
$\sum_k(L_{k,i}/r_i^3)_{n0}=0$, or complete quenching of the orbital
angular momenta in the absence of the field. The rotation manifests
itself in that $H^\prime$ rather than $H$ appears, and in that energy levels
may be modified by the rotation. Experimentally, without rotation,
shifts of resonance lines due to chemical surroundings have been found
for example to be $H^P/H\sim 6\times 10^{-4}$ for fluorine atoms.
Measurements of chemical shifts have been made by a number of
investigators.[^46]
The field $H^D$ [Eq. (70)] becomes in the limit of no rotation the
diamagnetic-shielding field found by Lamb[^46]: $H^D=\sigma H$, where
$$
\sigma = \frac{e^2}{2mc^2}\left\langle \sum_i \frac{x_i^2+y_i^2}{r_i^3} \right\rangle_0.
$$
 The term proportional to $D_1$ gives the polarization through the
electric-quadrupole moment of the nucleus.[^47] In the evaluation of the
field gradient $(\partial^2\phi/\partial z^2)$, the field gradient of
the electrons of the ion containing the nuclear spin of interest must be
added to the field gradient due to other ions. The contribution to the
quadrupole interaction arising from the distortion of the field of the
ion in which the nucleus of interest sits, due to the other ions is
included in the expectation value
$\langle\partial^2\phi/\partial z^2\rangle_0$, since the interaction
energy between the electrons of the ion with the crystal field is
contained in the exponent of $\rho_0$. This interaction may be treated
as a linear perturbation using (30). Finally, the term proportional to
$D_2$ has been discussed by Ramsey[^48] in connection with the
magnetic-resonance spectrum of molecules, and the line shift evaluated
for deuterium molecules. It gives rise to an apparent quadrupole moment,
since it produces the same line-splitting as the nuclear-quadrupole term
$D_1$.
In evaluating the correction to $\langle I_z \rangle_0$, which is linear
in the direct coupling of the spin to the surroundings
$\mathcal{H}_{12}$, we have found actually two types of corrections: one
which is really of first order, such as the Knight shift and the Lamb
shielding---these line shifts would appear as a first-order perturbation
of energy levels in usual quantum-mechanical, perturbation theory; the
other type involves not only the coordinates $q_2$ coupled directly to
the spin $I$ of interest, through $\mathcal{H}_{12}$, but also
coordinates $q_3$ coupled to $I$ only indirectly through terms in the
total Hamiltonian which contain both $q_2$ and $q_3$. These corrections
are of the form
$\sim \beta\langle\mathcal{H}_{12}\mathcal{H}_{23}I\rangle_{00}$ and are
exemplified by the Ramsey shielding and the effective-nuclear-exchange
term; the corresponding corrections to the energy levels would appear in
second-order perturbation theory.
Of course, we might have employed a perturbation
$\mathcal{H}^\prime_{12}=\mathcal{H}_{12}+\mathcal{H}_{23}$ in the first
place, and then the terms proportional to
$\langle \mathcal{H}_{12}\mathcal{H}_{23} \rangle$ would appear in the
second-order part of the expansion. However, the physical significance
of individual terms is more clearly brought out in the present way of
doing it; besides, we are assured that the
$\beta\langle\mathcal{H}_{12}\rangle$ effect is small, whereas this may
not be the case for $\beta^2\langle\mathcal{H}^\prime_{12}\rangle^2$.
In Eq. (64), seven linear corrections were distinguished; we would
obtain 28 types of terms from them in evaluating
$\langle \mathcal{H}_{12}^2 \rangle$. While all of these quadratic
corrections are expected to be small, some of them are expected to be
well within the range of observation of experiment.[^49] Here, only the five 
quadratic terms involving the hyperfine coupling and the "internal 
magnetic fields" occurring in (64) are evaluated; they are corrections 
either to the nuclear polarization in a paramagnetic ion or to the 
Knight shift. At this point, it must be mentioned that the "internal 
fields" $H^I, H^S$, etc., are statistical averages of fields arising 
from particular internal interactions. It does not necessarily follow 
from this that the NMR frequency will be shifted by the Larmor 
frequency corresponding to the internal fields; however, (64) states 
that the polarization of the spin acts as if the levels were shifted by 
just that amount. In some cases, as for example in the lowest-order 
Knight shift or the Lamb shielding, it is in fact so.
We write the part of $\mathcal{H}_{12}$ giving rise to
$H^I, H^S, H^{S^\prime}, H^P,$ and $H^D$ in the form
$\mathcal{H}^I+\mathcal{H}^S+\mathcal{H}^{S^\prime}+\mathcal{H}^P$, where
$\mathcal{H}^I$ gives $H^I$, etc. The coupling of hyperfine interaction
$\mathcal{H}^{S^\prime}$ with $\mathcal{H}^S$ gives in second order,
$$
(g\mu_B)^2[(3H_{x,y}^S H_{x,y}^{S'} - H_z^S H_z^{S'}) \langle I_z^2\Gamma \rangle_0 - 4H_{x,y}^S H_{x,y}^{S'} \langle (I_x^2)_0 \rangle \langle I_z\Gamma \rangle_0],
$$
 where $H_{x,y}$ are obtained from (65) by replacing $z$ by $x$ and $y$, respectively; similarly, $H_{x,y}^{S^\prime}$ are obtained from (67). To obtain (76), the simplifying assumption is made that the coordinates and spins of the electrons responsible for the contact interaction are not correlated to the spins of the nuclei, other than the one of interest.
The quadratic term coupling $\mathcal{H}^S$ and $\mathcal{H}^{S^\prime}$ is of
the same form, if it is assumed that the coordinates of different
electrons are uncorrelated and that a particular electron either has the
$\mathcal{H}^S$ type or the $\mathcal{H}^{S^\prime}$ type of interaction, but
not both:
$$
(g\mu_B)^2[(3H_x^S H_x^{S'} - H_z^S H_z^{S'}) \langle I_z^2\Gamma \rangle_0 - 4H_x^S H_x^{S'} \langle (I_x^2)_0 \rangle \langle I_z\Gamma \rangle_0].
$$
 If the correlation between electrons is to be included, the coefficient
of $\langle I_z^2\Gamma \rangle_0$ in (77) is replaced by
$$
(8\pi/3)(g\mu_B\beta)^2 \left\langle \sum_{n,n'} \left( \delta(r_n) \frac{3S_{nz'}}{r_{n'}^3} - \frac{3z_{n'}(S_{n'}\cdot r_{n'})}{r_{n'}^5} \right)_0 \left( \delta(r_{n'}) \frac{3S_{n'z}}{r_n^3} - \frac{3z_n(S_n \cdot r_n)}{r_n^5} \right)_0 \right\rangle.
$$
 The quadratic correction depending on $(\mathcal{H}^S)^2$ is
$$
\begin{aligned}
[(8\pi/3)g\mu_n(\mu_B/\hbar)\beta]^2 \langle I_z^2\Gamma \rangle_0 \left\langle \sum_{n,n'} \langle [S_n^z S_{n'}^{z'} - (S_n^x S_{n'}^x + S_n^y S_{n'}^y)] \right. \nonumber \\ \left. \times \delta(r_n)\delta(r_{n'}) \rangle - (g\mu H'\beta)^2 \langle(I_z)_0\rangle \langle I_z\Gamma \rangle_0 \right\rangle.
\end{aligned}
$$
 If $n \neq n^\prime$, the first term of (79) clearly vanishes; it can make a contribution only if at least two electrons have a finite probability of being at the nucleus. Even then, it can be shown to vanish, if the electron-spin space and coordinate space may be separated. For the quadratic terms coupling $\mathcal{H}^{S^\prime}$ and
$\mathcal{H}^P$, one assumes that the electrons with finite probability
of being at the nucleus are in s states, to obtain 
$$
\begin{aligned}
(8\pi/3)(g\mu_B\beta)^2 \langle I_z^2\Gamma \rangle_0 \left\langle \sum_{n,n'} \delta(r_n) \frac{1}{r_{n'}^2} (3L_{z,n'}S_{n,z'}-L\cdot S')_0 \right\rangle \nonumber \\ - 2(g\mu_B)^2 H_z^P H_z^{S'} \langle (I_x)_0 \rangle \langle I_z\Gamma \rangle_0.
\end{aligned}
$$
 The terms arising from products of $\mathcal{H}^{S^\prime}$ and
$\mathcal{H}^D$ give rise to the quadratic correction
$$
\begin{aligned}
(4\pi/3)(g\mu_B)(e^2/mc^2)\mu_e \langle I_z^2\Gamma \rangle_0 \left\langle \sum_n \delta(r_n)(3S_{nz}f_z - S_n \cdot f) \right\rangle_0 \nonumber \\ + 2(g\mu_B)^2 H_z^D H_z^{S'} \langle (I_x)_0 \rangle \langle I_z\Gamma \rangle_0,
\end{aligned}
$$
 where $f_z$ is the sum over electron coordinates:
$$
f_z = \sum_e [y_e z_e H_y - x_e z_e H_x - (x_e^2+y_e^2)H_z]/r_e^2,
$$
 and $f_x$ and $f_y$ are obtained by cyclic permutation of $x, y,$ and
$z$. We recall that, when the crystal is not rotating, $H_x=H_y=0$. This
completes the list of quadratic effects calculated here. In Eqs. (76) to
(81), all of the coefficients of $\langle I_z^2\Gamma \rangle_0$ produce
an effect on the expectation value of the $z$ component of the nuclear
spin proportional to that produced by a nuclear-quadrupole moment. For
$I=1/2$, these effects are not present, since
$\langle I_z^2\Gamma \rangle_0=0$. Ramsey[^48] has discussed the
pseudoquadrupolar effect contained in our Eq. (77) in connection with
the deuterium molecule. He also points out that no pseudoquadrupolar
contribution can come from $(\mathcal{H}^{S^\prime})^2$, because the dot
product $I\cdot S$ is isotropic. In solids in thermal equilibrium, a
small contribution could come from this term, the first term in our Eq.
(79), through the anisotropic terms in the exponent of the density
matrix.
Finally, a comment on the magnitude of the nuclear gyromagnetic effects.
According to Eqs. (54) and (55), the polarization produced by a crystal
rotation of $\omega/2\pi$ rev/sec is equal to that produced by a
magnetic field of $H$ gauss if $\omega/2\pi=\mu_N g/\hbar=762 gH$. For a
nuclear $g$ factor of order unity, a rotation frequency of order of 1000
rev/sec is equivalent to a gauss; rotation frequencies up to $10^5$
rev/sec have been achieved.[^49] By the techniques of nuclear induction,
one might observe not only the total polarization due to rotation, but
also details of the associated relaxation phenomena. The easiest, but
least interesting, observable effect of rotation would be the shift of
the resonance line. The nuclear counterpart of the Einstein-deHaas
effect, rotation by polarization, would, for a sample of $N$-saturated,
nuclear spins which are allowed to come to thermal equilibrium, lead
to a rotation frequency of the crystal $\omega_E = NI(I+1)\beta g\mu_N H/3B$,
where $B$ is the moment of inertia of the sample. For a field of $10^4$
gauss, $T=1^°$K, and a cylindrical sample with radius of gyration
$10^{-2}$ cm, we have $\omega_E=0.0023[I(I+1)g/A \sec]^{-1}$, where
$A$ is the average atomic weight of the sample.
## TIME-DEPENDENT BEHAVIOR OF NUCLEAR SPINS IN ROTATING CRYSTALS
### Solution of Schrödinger Equation
To generalize the example of the rotating pair of spins coupled by
dipole-dipole interaction of Sec. 2b, we consider a general system of
spins in a rotating crystal, acted upon by an external magnetic field
$H$. The interaction between spins is assumed to consist of a part $A$
which is unaffected by the fact that the crystal is rotating, and a part
$G(0)$, which if the crystal is rotating becomes
$$
G(t)=U(t)G(0)U(-t); \quad U(t)=\exp(i\omega\cdot S t),
$$
 where $S$ is
the total-spin vector for the system. The term $A$ includes, for
example, the contact interaction between nuclear spins and S electrons; the
$G(0)$ includes, in particular, the interaction between
non-overlapping dipoles. The Hamiltonian for the spins is, thus,
$$
\mathcal{H}_{CS} = -\sum_k \gamma_k H \cdot S_k + G(t) + A,
$$
 where
$S_k$ may be a nuclear or electronic spin. If the operator $A$ is
unchanged by the transformation $U$, we can put the time dependence into
the Zeeman term by the transformation $\psi^\prime = U\psi$ to give
$i\hbar\dot{\psi}^\prime = \mathcal{H}\_{CS}^\prime\psi^\prime$ with
$$
\mathcal{H}_{CS}' = \sum_k S_k \cdot [H'(t)\gamma_k+\omega] + G(0) + A,
$$
 where 
$$
\begin{aligned}
H'_x &= H_x \cos\omega t - H_y \sin\omega t, \nonumber \\ H'_y &= H_x \sin\omega t + H_y \cos\omega t, \nonumber \\ H'_z &= H_z,
\end{aligned}
$$
 if the axis of rotation is taken as the $z$ axis. The
Hamiltonian (84) is, however, just the Hamiltonian for the spin system
in a stationary crystal acted on by the rotating field
$H_\perp=(H^\prime_x, H^\prime_y, 0)$ plus a static field
$H_k=(0,0,H_z+\omega/\gamma_k)$ acting on the $k$th spin. Thus, the
rotating-crystal problem can be reduced to the much-studied,
rotating-field problem;[^50] of course, the solution to
$i\hbar\dot{\psi}^\prime=\mathcal{H}\_{CS}^\prime\psi^\prime$ must finally be transformed
back to the laboratory frame through $\psi=U^{-1}\psi^\prime$.
In the particular case that the field is parallel to $\omega$, the
equivalent problem is just the stationary field $H$ acting on the spins,
but with the effective gyromagnetic ratio
$\gamma_k^\prime = (\gamma_k+\omega/H)$. In this case, the effect of the
rotation on the wave function and eigenvalues is found by considering
the eigenvalues $E^\prime_{g,\omega}$ and eigenfunctions $\psi^\prime_{g,\omega}$,
of $\mathcal{H}\_{CS}^\prime$. Assume the $\psi^\prime_{g,\omega}$ forms a complete
nondegenerate set, and the $g$ symbolizes the quantum numbers of a
complete set of commuting, dynamical variables. In particular, if the
magnetic-quantum number $m_g$, eigenvalue of $S\cdot\omega/\omega$, is a
good quantum number, it too is included in the symbol $g$. In general,
we transform the $\psi^\prime_{g,\omega}$ to a representation in which
$S\cdot\omega$ is diagonal by means of transformation coefficients
$(g|m_\omega f)$, where $f$ represents any quantum numbers besides
$m_\omega$ required to label the complete set of functions
$U_{m_\omega f}$. Then, 
$$
\begin{aligned}
\psi &= \exp(-iS\cdot\omega t)\psi' = \exp(-iS\cdot\omega t)\sum_g \exp(-i/\hbar E'_g t)\psi'_g \nonumber \\ &= \exp(-iS\cdot\omega t)\sum_g \exp(-i/\hbar E'_g t)\sum_{m_\omega,f}(g|m_\omega f)U_{m_\omega f} \nonumber \\ &= \sum_g \sum_{m_\omega} \exp[-i/\hbar(E'_g + m_\omega\omega)t] \sum_f (g|m_\omega f) U_{m_\omega f}.
\end{aligned}
$$
 So that, in the laboratory system, the characteristic
energies are $E_g(\omega)=E^\prime_g(\omega)+m_\omega\omega$. If $m_\omega$ is
a good quantum number, then it follows from (84) that
$E^\prime_g(\omega) = E^\prime_g(0)-m_\omega\omega$. Thus,
$$
E_g(\omega) = E'_g(0).
$$
 The wave function is then in the laboratory
frame
$$
\psi=\sum_g \exp(-i/\hbar E_g t)\psi'_g(\Omega_k), \quad \Omega_k=\gamma_k H+\omega,
$$
 where the $E_g$ are independent of the frequency of rotation and are
given by (86); the $\psi^\prime_g(\Omega_k)$ are simultaneous eigenfunctions
of $\mathcal{H}^\prime_{CS}$ and $S\cdot\omega$. The effect of the rotation is
only to change the argument of the $\psi^\prime_g$ from $\gamma_k H$ to
$\Omega_k$. The condition that $m_\omega$ is a good quantum number is
satisfied if the effective external field $H+\omega/\gamma_k$ is large
compared to the transverse part of the internal field due to the other
dipoles acting on spin k.
The effect of the rotation on the lattice motion can be seen by
transforming the Hamiltonian to body-fixed axes. Presumably the rotation
is slow enough so that in the rotating coordinate system the crystal
electric fields are the same as those in a stationary crystal. The
Hamiltonian referred to the rotating axes is, if spin-orbit coupling and
external fields are neglected,[^51]
$$
\mathcal{H}_L = \sum_i P_i^2/2m_i - \omega\cdot L + V.
$$
 Here, $L$ is
the orbital angular momentum in the rotating system. The $\omega\cdot L$
term is due to the rotation; it indicates that a particular
lattice-vibration frequency may be split into frequencies differing from
it by an amount of the order of the frequency of rotation of the
crystal. If $L\cdot\omega/\omega$ commutes with the Hamiltonian, its
integer eigenvalues are good quantum numbers, and the frequency
splitting is by integer multiples of $\omega$.
### Statistical Treatments; Approach to Equilibrium
The approach to thermal equilibrium of nuclear spins in a rotating
crystal may be studied by means of the Wangsness and Bloch[^52] theory of
nuclear magnetic relaxation. Consider the case of a crystal rotating
with angular velocity $\omega$; in addition, the crystal is in a
constant magnetic field $H_0$. Let $I_1$ be the spin operator of system
one, the system of interest, and $I_2$ the total-spin operator of system
two, the environment. The combined system is described by a Hamiltonian
of the form 
$$
\mathcal{H} = \mathcal{H}_1 + \mathcal{H}_2 + G(t),
$$
 where
$\mathcal{H}\_1$ and $\mathcal{H}\_2$ are the Hamiltonian operators
for systems one and two separately, and $G(t)$ is the coupling between
them. $\mathcal{H}\_2$ and $I_2$ are assumed to be independent of the
time while $G(t)$ will be assumed to have the time-dependence
characteristic of the dipole-dipole interaction in a rotating crystal:
$$
G(t) = U^{-1}G(0)U, \quad U=\exp[i(I_1+I_2)\cdot\omega t].
$$
 The
calculations are most easily carried out in the interaction
representation, obtained by a unitary transformation $S$ from the
laboratory system. Let $\rho$ be the density matrix in the laboratory
system and $\rho^\prime$ in the interaction representation, then,
$$
\rho' = S\rho S^{-1}, \quad S = \exp[i/\hbar(\mathcal{H}_1+\mathcal{H}_2)t],
$$
 and 
$$
\dot{\rho}' = (1/i\hbar)[G', \rho'], \quad G' = SG(t)S^{-1}.
$$
 Applying perturbation theory to (91), keeping terms up to second order
in $G^\prime$, and then summing over the quantum numbers of the environment,
gives in the usual way[^52]
$$
\dot{\sigma}' + i \mathrm{Tr}_2[G'(t), \rho'(0)] = - \mathrm{Tr}_2 \int_0^t [G'(t), [G'(t'), \rho'(0)]]dt',
$$
 where $\mathrm{Tr}\_2$ means the diagonal sum over the quantum numbers of
the environment, and $\sigma^\prime = \mathrm{Tr}\_2\rho^\prime$. The eigenvalues of
$\mathcal{H}\_2-\omega\cdot I_2$ will be labeled $g$ and are assumed to
be nondegenerate; one can suppose some very small perturbations to have
removed all degeneracies. Now, we restrict system one to a single
nuclear spin, with $(I_1)\_z=m\hbar$. The matrix elements of $\sigma^\prime$ are
$$
(m|\sigma'|m') = \sum_g (mg|\rho'|m'g).
$$
 Choose the $z$ axis
along the external field $H_0$ and choose the $y$ axis such that
$\omega$ lies in the $x-z$ plane at some angle $\theta$ with the $z$
axis. Then, 
$$
\begin{aligned}
U(t) &= \exp(i I_y \theta t) \exp(i I_z \omega t) \nonumber \\ &= \exp(iI_y\theta t) \exp[-i\theta(I_1)_y] \exp[-i\omega t(I_1)_z] \times \exp[i\theta(I_1)_y] \nonumber \\ \langle mg|U(t)|m'g'\rangle &= \langle g|\exp(iI_2\cdot\omega t)|g'\rangle \sum_{m''} \langle m|\exp(-i\omega t m'') \rangle \nonumber \\ & \quad \times d_{m m''}^{(I_1)}(\theta)d_{m'' m'}^{(I_1)}(-\theta),
\end{aligned}
$$
 where the $d_{mm^\prime}^{(I)}(\theta)$ are the well-known, explicit matrix elements[^53]
$\langle m|\exp[-i\theta(I_1)\_y]|m^\prime\rangle$. The interaction
$G^\prime(t)=SU^{-1}G(0)US^{-1}$ is in this representation 
$$
\sum_{m''m'''m''''m'''''} \exp[-i\omega t(m''-m''')] \times \langle m''''g|G(0)|m'''''g'\rangle A(\theta)_{m''m'''}^{m''''m'''''} 
$$
 with $A=d(\theta)d(-\theta)d(-\theta)d(-\theta)$. In
particular, we consider $\omega$ and $H_0$ parallel, $\theta=0$. Since
$d_{mm^\prime}^{(I)}(0)=\delta_{mm^\prime}$, (94) becomes for this case
$$
\langle mg|G'(t)|m'g'\rangle = e^{i(m-m')\Omega t} \langle mg|G(0)|m'g'\rangle,
$$
 where $\Omega=\gamma H_0+\omega$. The heat bath is assumed to remain in
thermal equilibrium
$$
\sum_m \langle gm|\rho'|g'm \rangle = (e^{-\beta g}/\sum_{g''} e^{-\beta g''})\delta_{gg'};
$$
 further, the interaction of the spin of interest is assumed to be linear
in the spin components, so that one may expand
$$
G(0) = \sum_n F_n K_n,
$$
 with
$\langle gm|K_n|g^\prime m^\prime\rangle=\langle m|K_n|m+n\rangle \delta_{gg^\prime}\delta_{m, m^\prime+n}$
and $F_n$ is dependent only on the state of system two. The heat-bath
action is characterized by the quantum-mechanical spectral density
defined by
$$
\langle F_n(\epsilon)F_{-n}(-\epsilon) \rangle = \sum_g \langle g|F_n|g+n\Omega+\epsilon\rangle\langle g+n\Omega+\epsilon|F_{-n}|g\rangle \times (e^{\beta g}/\sum_{g'} e^{\beta g'}).
$$
 We insert (95), (96), and (97) into Eq. (92), and averaging over
oscillation in the usual manner[^52] to obtain in the laboratory system
$$
\dot{\sigma}+i[\gamma H_0 I_z + \Delta E + \Gamma, \sigma]\_z = \pi\sum_n \langle F_n(0)F_{-n}(0)\rangle (2e^{-\beta\hbar n\Omega}\sigma K_n K_{-n} - \sigma K_n K_{-n} - K_n K_{-n}\sigma),
$$
 with $\Delta E$ defined by its matrix elements
$$
\langle m|\Delta E|m'\rangle = [\hbar/(\sum_{g'}e^{-\beta g'})]\sum_g e^{\beta g}\langle mg|G(0)|mg\rangle,
$$
 and
$$
\Gamma = \sum_n P \int (d\epsilon/\epsilon)(F_n(-\epsilon)F_{-n}(\epsilon))K_n K_{-n},
$$
 where $P$ means the "principal part of the integral." The left-hand
side of (99) describes the periodic precession of the spin. In first
approximation, the precession frequency is just $\gamma H_0$,
independent of the rotation of the crystal. The terms in $\Delta E$ and
$\Gamma$ are corrections, respectively, linear and quadratic in the
coupling $G$; these correspond to the linear and quadratic perturbations
on the energy levels, which were studied in Sec. 3d in connection with
the equilibrium-density matrix. The right-hand side of (99) describes
the rate of relaxation towards equilibrium. Inspection shows that it
depends on the quantity $\Omega=\gamma H_0+\omega$, but does not depend
on $\gamma H_0$ and $\omega$ separately, except for the dependence of
the heat-bath levels $g$ on $H_0$ and $\omega$ separately. Generally,
$g$ will depend on the combination $\Omega_k=\gamma_k H_0+\omega$ where
$\gamma_k$ is the gyromagnetic ratio of spins interacting with the spin
of interest. In the case of pure rotation ($H_0=0$), all the
$\Omega_k=\Omega$; this allows transitions involving two spins of
differing gyromagnetic ratio without exchanging energy with the lattice.
For this reason, one should expect an enhanced cross relaxation if the
total effective field $H_e=H_0+\omega/\gamma$ is partly due to rotation,
rather than wholly due to a static field. If we multiply (99) by the
spin vector $I$ for $I=\frac{1}{2}$, we obtain in the usual manner[^52]
the Bloch phenomenological equations with the asymptotic value
$$
\langle I_z \rangle_0 = \tfrac{1}{2}\tanh \tfrac{1}{2}\beta\hbar\Omega, \quad \langle I_x \rangle_0 = \langle I_y \rangle_0=0; \tag{100a}
$$
 the precession frequency 
$$
\begin{aligned}
\omega' &= \gamma(H_0+h'+h''), \nonumber \\ \gamma h' &= (1/\sum_g e^{\beta g})\sum_g e^{\beta g} \langle g|F(0)|g \rangle, \tag{100b} \\ \gamma h'' &= -P \int \frac{d\epsilon}{\epsilon}[1+e^{\beta\hbar(\Omega+\epsilon)}]\langle F^1(\epsilon)F^{-1}(-\epsilon)\rangle;
\end{aligned}
$$
 and relaxation times 
$$
\begin{aligned}
1/T_2 &= 2\pi(1+e^{-\beta\hbar\Omega})\langle F^1(0)F^{-1}(0)\rangle, \nonumber \\ 1/T_1 &= 1/2T_2+\pi\langle F^0(0)F^0(0)\rangle. \tag{100c}
\end{aligned}
$$
 It may be of interest to note explicitly that
$\gamma h^{\prime\prime}$, if the exponent is expanded, contains a term linear in
$\beta\Omega$. It follows from (99) that, when the diagonal elements of
$\sigma$ are stationary, then,
$$
\langle m|\sigma|m\rangle / \langle m+n|\sigma|m+n\rangle = e^{\beta\hbar n\Omega},
$$
 provided that for every value $m$ there exist at least one value of $n$
so that
$$
\langle F^n(0)F^{-n}(0)\rangle\langle m|K_n K_{-n}|m\rangle \neq 0.
$$
 The foregoing discussion based on the Wangsness-Bloch is limited in a
number of ways.
1.  We have assumed that $\omega$ and $H_0$ are parallel. This
simplified the analysis, permitting the use of the expression (95)
instead of (94). However, the extension to the case of $\omega$ and
$H_0$ being in different directions can be carried through; in fact,
the closely related problem of the rotating magnetic field has been
treated[^54] by several authors.
2.  It has been assumed that the interaction $G$ is a perturbation on
the dominant energy term which has a magnitude $\hbar\Omega$, so
that $m$ is a good quantum number. In other words, we require
$\hbar\Omega \gg 1/T_2$. For CaF$_2$, the $1/T_2 \sim 10^5$
sec$^{-1}$. These are rather high frequencies for a pure rotation.
3.  The most serious shortcoming is that the system of interest is taken
to be a single spin, and the other nuclear spins are regarded as
part of the heat bath, which is not described in detail. Thus, the
correlations between neighboring spins is completely ignored. In
principle, one should consider all of the spins and their dipole
interaction as the system of interest. However, the solution of the
coupled-spin systems in a solid lattice is prohibitively difficult.
One can, however, assume that the spin system as a whole is
described by a spin temperature[^55] different from the lattice
temperature; then, the problem becomes soluble. In many crystals
indeed, $T_2 \ll T_{1s}$, so that the assumption of a spin
temperature can at least be regarded as physically plausible.
Dreitlein and Kessemeier,[^49] have studied the line shape for the
magnetic resonance absorption of a rotating crystal. The study is
restricted to high magnetic fields and assumes a rigid lattice. The
physical features obtained include (1) the narrowing of the
magnetic-resonance lines which results from the time dependence of the
dipole-dipole coupling $G(t)$ if the crystal rotates, and (2) the
characteristic frequencies of satellite lines which appear in the
presence of rotation. These phenomena occur when the rotation axis makes
a finite angle with the magnetic field.
## ACKNOWLEDGMENTS
We should like to thank G. G. Scott and S. Arajs for correspondence
concerning their results, some of which had not been published at the
time. We should also like to acknowledge some interesting discussions
relevant to the present study with Professor. N. Bloembergen and Dr. W.
Janos, Dr. B. S. Tanenbaum, and Dr. L. Wilcox.
## SYSTEM OF TWO COUPLED SPINS
Consider two spins, $S_1$ and $S_2$ attached to two nuclei located on
the $Z$ axis a distance $R$ apart; the coupling between the associated
dipoles is
$$
\mathcal{H}_{12} = 2E_0[S_1\cdot S_2 - 3S_{1z}S_{2z}], \quad \text{where } E_0=\hbar^2\gamma_1\gamma_2/2R^3. \tag{A1}
$$
 In a representation in which $S^2=(S_1+S_2)^2$ and $S_z=(S_{1z}+S_{2z})$
are diagonal with eigenvalues $S(S+1)$ and $m$, respectively, a complete
set of orthonormal eigenfunctions are $\phi_k(m,S)$:
$$
\phi_1(11) = \begin{pmatrix} 1 \\ 0 \\ 0 \\ 0 \end{pmatrix}, \quad \phi_2(01) = \begin{pmatrix} 0 \\ 1 \\ 0 \\ 0 \end{pmatrix}, \quad \phi_3(-11) = \begin{pmatrix} 0 \\ 0 \\ 1 \\ 0 \end{pmatrix}, \quad \phi_4(00) = \begin{pmatrix} 0 \\ 0 \\ 0 \\ 1 \end{pmatrix}
$$
 The single index $k$ replaces the two quantum numbers $m$ and $S$. The
equations for the coefficients in the expansion
$\psi(t)=\sum_k b_k(t)\phi_k(m,S)$ of the Schrödinger wave function are
$$
i\hbar\dot{b}_k + \sum_m b_m K_{mk} = 0, \quad \text{where } K_{mk} = \langle\phi_m|\mathcal{H}|\phi_k\rangle. \tag{A2}
$$
 If the two spins are acted upon by a magnetic field $H=(H_x,0,H_z)$ and
are coupled through $\mathcal{H}\_{12}$ of Eq. (A1), the symmetric matrix
$K$ has elements 
$$
\begin{aligned}
K_{11} &= -E_0 - \bar{\gamma}H_z; \quad K_{22}=2E_0; \quad K_{33}=-E_0+\bar{\gamma}H_z; \nonumber \\ K_{44} &= 0, \nonumber \\ K_{12} &= K_{32} = -H_x\bar{\gamma}/\sqrt{2}; \quad K_{14} = -H_x\Delta/2; \nonumber \\ K_{24} &= -H_z\Delta, \tag{A3}
\end{aligned}
$$
 with $\bar{\gamma}=\frac{1}{2}(\gamma_1+\gamma_2)$ and
$\Delta=\frac{1}{2}(\gamma_1-\gamma_2)$. If a rotating pair of spins is
being treated, replace $H$ by $\omega$ expressed in energy units and put
$\Delta=0$. When $\Delta=0$, no transitions between the triplet ($S=1$)
and singlet ($S=0$) state are possible. We treat only this case. The
eigenvalues of $K$ are most easily expressed in terms of the angle
$\phi$ where
$$
\cos\phi = \frac{E_0(E_0^2+\frac{1}{2}\omega_x^2-\omega_z^2)}{(E_0^2+\frac{1}{4}\omega_x^2)^{3/2}}, \quad 0 \le \phi < \pi.
$$
 They are 
$$
\begin{aligned}
\lambda_1 &= (E_0^2+\frac{1}{4}\omega_x^2)^{1/2}[\sqrt{3}\sin\phi/3+\cos\phi/3], \nonumber \\ \lambda_2 &= (E_0^2+\frac{1}{4}\omega_x^2)^{1/2}[-\sqrt{3}\sin\phi/3-\cos\phi/3], \nonumber \\ \lambda_3 &= 2(E_0^2+\frac{1}{4}\omega_x^2)^{1/2}\cos\phi/3, \nonumber \\ \lambda_4 &= 0. \tag{A4}
\end{aligned}
$$
 Since the trace of $K$ vanishes,
$\lambda_1+\lambda_2+\lambda_3+\lambda_4=0$ even when $\Delta\neq0$. In
the limiting case of $|ω/E_0|\gg 1$, the eigenvalues (A4) go into
the usual Zeeman splitting $(\omega_z, -\omega_z, 0, 0)$, whereas in the
$|ω/E_0|\ll 1$ limit, they become the eigenvalues of
$\mathcal{H}\_{12}$, $(-E_0, -E_0, 2E_0, 0)$. Assume the field is
practically in the $x$ direction, but has a very small component in the
$z$ direction, which will eventually be put equal to zero. Then,
$$
\begin{aligned}
\lambda_1 &= \tfrac{1}{2}(E_0-\epsilon)-\Delta_1, \nonumber \\ \lambda_2 &= -E_0+\Delta_2, \nonumber \\ \lambda_3 &= -\tfrac{1}{2}(E_0+\epsilon)+\Delta_3, \nonumber \\ \lambda_4 &= 0. \tag{A5}
\end{aligned}
$$
with 
$$
\begin{aligned}
\Delta_1 &= 6E_0\omega_z^2/(\epsilon^2-3E_0\epsilon), \nonumber \\ \Delta_2 &= 3E_0(\omega_z/\omega_x)^2, \nonumber \\ \Delta_3 &= 6E_0\omega_z^2/(\epsilon^2+3E_0\epsilon), \nonumber \\ \epsilon &= (9E_0^2+4\omega_x^2)^{1/2}.
\end{aligned}
$$
 The solution to (A2) reduces to
$$
b_k(t) = \sum_{l=1}^3 B_k^l e^{i\lambda_l t/\hbar}, \quad k=1,2,3, \tag{A6}
$$
 where the constant $B_k^l$ can be expressed in terms of the initial
state $b_k(0)$ by substituting (A6) into (A2) and solving the resulting
linear, algebraic equations together with
$$
b_4(0) = \sum_{l=1}^3 B_4^l.
$$
 The result is 
$$
\begin{aligned}
B_1^1 &= B_3^1 = \tfrac{1}{2}[b_1(0)-b_3(0)], \nonumber \\ B_1^2 &= B_3^2 = -\frac{\omega_x}{\sqrt{2}\epsilon}b_2(0)+[b_1(0)+b_3(0)]\frac{\epsilon-3E_0}{4\epsilon}, \nonumber \\ B_1^3 &= B_3^3 = \frac{\omega_x}{\sqrt{2}\epsilon}b_2(0)+[b_1(0)+b_3(0)]\frac{\epsilon+3E_0}{4\epsilon}, \nonumber \\ B_2^1 &= 0, \nonumber \\ B_2^2 &= \frac{\epsilon+3E_0}{2\epsilon}b_2(0)-[b_1(0)+b_3(0)]\frac{\omega_x}{\sqrt{2}\epsilon}, \nonumber \\ B_2^3 &= \frac{\epsilon-3E_0}{2\epsilon}b_2(0)+[b_1(0)+b_3(0)]\frac{\omega_x}{\sqrt{2}\epsilon}. \tag{A7}
\end{aligned}
$$
 The expectation value of $S_x$ in the representation
chosen is
$$
\langle S_x \rangle = \psi^*(t)S_x\psi(t) = (1/\sqrt{2}\epsilon)[b_1^*b_2+b_1b_2^*+b_2^*b_3+b_2b_3^*].
$$
 Substituting (A6) for the $b_k$ and averaging over all periodic terms,
gives a time-independent value, which is, with the help of (A7),
$$
\begin{aligned}
\langle S_x \rangle_{\mathrm{av}} &= (3\omega E_0/\epsilon^2)[|b_1(0)+b_3(0)|^2-2|b_2(0)|^2] \nonumber \\ & \quad + (4\omega_x^2/\epsilon^2)[b_1(0)b_2^*(0)+b_2(0)b_1^*(0)+b_3(0)b_2^*(0)+b_2(0)b_3^*(0)]. \tag{A8}
\end{aligned}
$$
 Similarly, one obtains
$\langle S_y \rangle_{\mathrm{av}} = \langle S_z \rangle_{\mathrm{av}} = 0$.
The av indicates the time average. If the initial density matrix
$b_k(0)b_l^*(0)$ is diagonal and is normalized so that
$$
\sum_{k=1}^4 |b_k(0)|^2 = 3/4,
$$
 Equation (A8) becomes
$$
\langle S_x \rangle_{\mathrm{av}} = (9\omega E_0/4\epsilon^2)(1-4|b_2(0)|^2).
$$
 If the initial states are distributed in a Boltzmann distribution at
temperature $T_0$, an average over initial states gives the result
quoted in the text:
$$
\langle\langle S_x \rangle\rangle_{\mathrm{av}} \approx (\omega/kT_0)(3E_0/2\epsilon)^2.
$$
 The same assumption gives for the squared components 
$$
\begin{aligned}
\langle\langle S_x^2 \rangle\rangle_{\mathrm{av}} &= \frac{1}{2} - \frac{E_0}{8k T_0} \nonumber \\ \langle\langle S_y^2 \rangle\rangle_{\mathrm{av}} &= \frac{1}{2} + \frac{1}{\epsilon^2} \frac{9E_0^2-2\omega_x^2}{8k T_0}E_0 \nonumber \\ \langle\langle S_z^2 \rangle\rangle_{\mathrm{av}} &= \frac{1}{2} - \frac{1}{\epsilon^2} \frac{9E_0^2+\omega_x^2}{4k T_0}E_0 \tag{A9}
\end{aligned}
$$
 In the limit of no coupling between spins ($E_0 \to 0$),
$\langle\langle S_x^2 \rangle\rangle_{\mathrm{av}}=1/2$. A geometrical
picture of the motion of the tip of the averaged spin vector is, according
to (A9), more complicated than a circular precession around the
field direction, for otherwise one would have equal values for
$\langle\langle S_y^2 \rangle\rangle_{\mathrm{av}}$ and
$\langle\langle S_z^2 \rangle\rangle_{\mathrm{av}}$.
## PERTURBATION THEORY TO ALL ORDERS
The perturbation expansion (30) may be extended to all orders of $B$, by
calculating the derivatives indicated in (26). We generalize the
definitions (28) to 
$$
\begin{aligned}
S_0 &= 1 \nonumber \\ S_n &= \int_0^1 dx' \int_0^1 dx'' \dots \nonumber \\ & \quad \times \int_0^1 dx^{(n)} e^{-A x'} B e^{A x'} e^{-A x''}(Bx'')e^{A x''} \dots \nonumber \\ & \quad \times e^{-A x^{(n)}}(Bx'x''\dots x^{(n)}) \nonumber \\ & \quad \times e^{A x'x''\dots x^{(n)}}, \quad n \ge 1. \tag{B1}
\end{aligned}
$$
 The general expansion of $\langle\Gamma\rangle$ then
gives
$$
\langle\Gamma\rangle = \sum_{n=1}^\infty \langle Q_n\Gamma \rangle_0, \tag{B2}
$$
 with 
$$
Q_n = S_n - \sum_{k=1}^{n-1}\langle Q_k \rangle_0 S_{n-k}.
$$
 To
prove (B2) one can write (27) in the form
$$
e^{\epsilon A+B} = e^A \sum_{n=0}^\infty \epsilon^n S_n, \tag{B3}
$$
 where the $S_n$ are defined by (B1). Consequently, 
$$
\begin{aligned}
u(\epsilon) &= \mathrm{Tr}Ce^{\epsilon A+B} = \sum_{n=0}^\infty \epsilon^n \mathrm{Tr}Ce^A S_n \\ v(\epsilon) &= \mathrm{Tr}e^{\epsilon A+B} = \sum_{n=0}^\infty \epsilon^n \mathrm{Tr}e^A S_n
\end{aligned}
$$
 and the $n$th derivatives with respect to $\epsilon$ evaluated at $\epsilon=0$ are
$$
u^{(n)}(0)/v(0)=n!\langle S_n C \rangle_0, \quad v^{(n)}(0)/v(0)=n!\langle S_n \rangle_0. \tag{B4}
$$
 We need the derivatives of $1/v$; these may be expanded in terms of the
derivatives of $v$, to obtain by use of the second of the Eqs. (B4),
$$
v(0)(v^{-1})^{(n)}(0) = -n!\langle Q_n \rangle_0. \tag{B5}
$$
 Equations
(B4) and (B5) show that the $\langle Q_n \rangle_0$ and
$\langle S_n \rangle_0$ are related to the derivatives of the partition
function $v$. The derivatives required in (26) are
$$
\frac{1}{n!}\frac{d^n\langle C \rangle_\epsilon}{d\epsilon^n} = \frac{1}{n!}\frac{d^n(uv^{-1})}{d\epsilon^n} = \sum_{k=0}^n \frac{u^{(k)}(v^{-1})^{(n-k)}}{k!(n-k)!}
$$
 as follows from the elementary rule for differentiating a product. At
$\epsilon=0$, the derivatives are, with the help of (B4) and (B5),
$$
\frac{1}{n!}\frac{d^n\langle C \rangle_\epsilon}{d\epsilon^n} = \sum_{k=1}^n \langle Q_k \rangle_0 \langle S_{n-k}C \rangle_0 + \langle S_n C \rangle_0 = \langle Q_n \Gamma \rangle_0. \tag{B6}
$$
 Inserting the expression (B6) into (26), finally gives the theorem (B2).
## SOME SIMPLE EXPECTATION VALUES
Below are given the expectation values of frequently occurring, spin
operators taken over the density matrix
$$
\rho_0 = \frac{\exp(aI_z)}{\mathrm{Tr}[\exp(aI_z)]}.
$$
The abbreviation $\Gamma=I_z^2-I\cdot I-\langle I_z^2 \rangle_0$ is
used, and $I$ is the angular momentum in units of $\hbar$.
1.  $\langle I_x \rangle_0 = \langle I_y \rangle_0 = 0$
2.  $\langle I_z \rangle_0 = (I+\tfrac{1}{2})\coth[a(I+\tfrac{1}{2})] - \tfrac{1}{2}\coth a/2 = (a/3)I(I+1)+O(a^3)$
3.  $\langle I_xI_y \rangle_0 = \langle I_z I_x \rangle_0 = 0$
4.  $\langle I_x^2 \rangle_0 = I(I+1)+\tfrac{1}{2}\coth^2 a/2 - (I+\tfrac{1}{2})\coth(a/2)\coth[a(I+\tfrac{1}{2})] = \tfrac{1}{2}I(I+1)+O(a^2)$
5.  $\langle I_z\Gamma \rangle_0 = \partial\langle I_z \rangle_0/\partial a = \tfrac{1}{3}I(I+1)+O(a^2)$
6.  $\langle I_z^2\Gamma \rangle_0 = \frac{\partial\langle I_z^2 \rangle_0}{\partial a} = \frac{aI(I+1)}{45}[4I(I+1)-3]+O(a^3)$
7.  $\langle I_x^2\Gamma \rangle_0 = \frac{1}{2}\frac{\partial\langle I_x^2 \rangle_0}{\partial a} = \frac{aI(I+1)}{90}[4I(I+1)-3]+O(a^3)$
8.  $\langle I_x I_y \Gamma \rangle_0 = \langle I_z I_x \Gamma \rangle_0 = 0$
9.  $\langle I_x I_y \Gamma \rangle_0 = -\langle I_y I_x \Gamma \rangle_0 = \tfrac{1}{2}i\hbar\langle I_z\Gamma \rangle_0$

[^1]: Brandeis University, Waltham, Massachusetts. Part of the material in this paper is based on a Ph.D. dissertation submitted to Stanford University in 1960. Some of the work was carried out while this author was associated with Raytheon Company, Wayland, Massachusetts. Work at Brandeis University supported by the U. S. Air Force.
[^2]: Washington University, St. Louis, Missouri. Work at Stanford University supported by the U. S. Air Force during 1959 and 1960.
[^3]: J. Clerk Maxwell, *Electricity and Magnetism* (Oxford University Press, London, 1892), pp. 574 and 575.
[^4]: S. J. Barnett, Phys. Rev. 6, 239 (1915); 10, 7 (1917); 17, 404 (1921); 20, 90 (1922). S. J. Barnett and J. H. Barnett, Proc. Am. Acad. Arts Sci. 60, 125 (1925).
[^5]: A. Einstein and W. J. de Haas, Verhandl. deut. physik Ges. 17, 152 (1915). A. Einstein, *ibid*. 17, 203 (1915); 18, 17 (1916). W. J. de Haas, Proc. Acad. Sci., Amsterdam 18, 1280 (1916).
[^6]: The earlier experiments are reviewed by S. J. Barnett, Revs. Modern Phys. 7, 136 (1935) and by L. F. Bates, *Modern Magnetism* (Cambridge University Press, New York, 1951), Chap. 7. Of particular importance are the experiments on paramagnetic materials performed by W. Sucksmith, Proc. Roy. Soc. (London) A128, 276 (1930); A133, 179 (1931); A135, 276 (1932). Measurements reported in the literature since 1951 are S. J. Barnett and G. S. Kenney, Phys. Rev. 87, 723 (1952). A. J. P. Meyer, Compt. rend. 246, 1294 (1958). A. J. P. Meyer and S. Brown, J. phys. radium 18, 161 (1957). A. J. P. Meyer, G. Asch, and S. Brown, "Colloque National de Magnetisme," (Strasbourg 1957), p. 305. G. Asch, Compt. rend. 246, 1294 (1958). G. G. Scott, Phys. Rev. 82, 542 (1951); 99, 1241 (1955); 99, 1824 (1955); 103, 561 (1956); Rev. Sci. Instr. 28, 270 (1957); Phys. Rev. 119, 84 (1960); 120, 331 (1960). For a recent review of experiments see G. G. Scott, Revs. Modern Phys. 34, 102 (1962).
[^7]: P. A. M. Dirac, *Quantum Mechanics* (Oxford University Press, New York, 1947), 3rd ed., p. 35.
[^8]: For the case of a pure spin system, I. Rabi, N. F. Ramsey, and J. Schwinger [Revs. Modern Phys. 26, 167 (1954)] give a different proof of Larmor's theorem. They consider the operator $J$ and its equation of motion in the Heisenberg picture. Their proof can be readily generalized to differing $\gamma$'s and to include orbital motion. However, the restriction $[J\cdot\omega, \mathcal{H}\_0]=0$ is also necessary. Transformation to a rotating coordinate system as a means of transforming away static fields is well known in the theory of magnetic resonance. See, for example, R. V. Wangsness and F. Bloch, Phys. Rev. 89, 728 (1953).
[^9]: Exact solutions of the Schrödinger equation for particles with spin, but without orbital motion, in a time-dependent, magnetic field have been studied by E. Majorana, Nuovo cimento 9, 43 (1932), and by F. Bloch and I. Rabi, Revs. Modern Phys. 17, 237 (1945). One may treat the case including orbital motion by means of the adiabatic approximation: If the field does not change direction, then, in the lowest approximation of a slowly varying field, the eigenvalue equation $[Α\mathcal{H}\_0-e\hbar H(t)]=E_N(t)\psi_N(t)$, is solved, yielding the Zeeman splitting but no transitions between states. The next approximation yields transition probabilities proportional to $(dH/dt)^2$.
[^10]: Not to be confused with the rotation of the coordinate system in Larmor's theorem. We are now talking about an actual, physical rotation.
[^11]: This procedure has been formulated by E. T. Jaynes, Phys. Rev. 106, 620 (1957); 108, 171 (1957), in a general way from considerations based on information theory.
[^12]: One may also wish to incorporate into $\rho$ knowledge of the accuracy with which the energy and angular momentum are known. This can be done most easily by including $\mathcal{H}^2$ and $J_i^2$ in the set of operators whose expectation values are given, which would add the terms $-\beta_2 \mathcal{H}^2-\lambda_{ij}J_i J_j$ to the exponent in (18). In principle, whenever such information is available it should be incorporated into $\rho$. However, as was pointed out in the classical case already by Gibbs, the state-density function for any system which exhibits reproducible thermodynamic properties is such a rapidly varying function of the parameters $\mathcal{H}$, $J_i$ that the variance $\langle \mathcal{H}^2 \rangle - \langle \mathcal{H} \rangle^2$ or $\langle J_i^2 \rangle - \langle J_i \rangle^2$ obtained from (18) is already very small compared to any reasonable mean-square, experimental error. Consequently, although the extra terms would represent a considerable redistribution of probabilities, they would not lead to any difference in prediction of reproducible phenomena. This is the basic reason for the success of the Gibbs canonical ensemble, and it is interesting to note that Gibbs also used an ensemble canonical in angular momenta, as in (18), to describe a rotating system.
[^13]: An early quantum-statistical perturbation theory, expressed in terms of perturbations on the energy levels, was given by R. Peierls, Z. Physik 80, 763 (1933); S. Nakajima, Advances in Physics 4, 363 (1955), has used operator techniques to obtain an expansion for the partition function. Application of similar techniques to statistical-mechanics problems has been given among others by R. Kubo and K. Tomita, J. Phys. Soc. Japan 9, 888 (1954); D. Thouless, Ann. Phys. 10, 553 (1960); W. Kohn and J. Luttinger, Phys. Rev. 118, 41 (1960). The present approach was briefly reported at the April 15, 1961, meeting of the New England Section of The American Physical Society.
[^14]: R. Karplus and J. Schwinger, Phys. Rev. 73, 1020 (1948); R. P. Feynman, ibid. 84, 108 (1951); R. Kubo and K. Tomita, J. Phys. Soc. Japan 9, 888 (1954).
[^15]: J. H. Van Vleck, *The Theory of Electric and Magnetic Susceptibilities* (Oxford University Press, New York, 1932).
[^16]: E. Fermi, Z. Physik 60, 320 (1930).
[^17]: J. H. Van Vleck, Revs. Modern Phys. 23, 213 (1951).
[^18]: See, for example, J. H. Van Vleck, *The Theory of Electric and Magnetic Susceptibilities* (Oxford University Press, New York, 1932), Chap. VII.
[^19]: J. H. Van Vleck, *The Theory of Electric and Magnetic Susceptibilities* (Oxford University Press, New York, 1932), p. 235.
[^20]: C. H. Townes, C. Herring, and W. D. Knight, Phys. Rev. 77, 852 (1950).
[^21]: W. D. Knight, Phys. Rev. 76, 1259 (1949).
[^22]: M. E. Rose, Phys. Rev. 75, 213 (1949); C. J. Gorter, Physica 14, 504 (1948).
[^23]: S. R. De Groot, *Thermodynamics of Irreversible Processes* (North-Holland Publishing Company, Amsterdam, 1951), Chap. 2.
[^24]: The assumption that the spin system and crystal lattice rotate together as a rigid body is valid if the period of rotation is long compared to the relaxation time $T_1$ for transfer of angular momentum between spins and lattice. This is always satisfied in the usual experimental arrangements.
[^25]: A. Frank, Phys. Rev. 39, 119 (1932); see also reference 15, p. 254.
[^26]: S. Arajs, R. V. Colvin, and H. Chessin, J. Appl. Phys. 33, 1353S (1962).
[^27]: C. J. Gorter and B. Kahn, Physica 16, 753 (1940); C. J. Gorter, *Paramagnetic Relaxation* (Elsevier Publishing Company, Inc., Amsterdam, 1947), p. 116.
[^28]: For Eu$^{3+}$ and Sm$^{3+}$, the lowest multiplet levels are close enough so that the states cannot be characterized by a single $J$ value. However, the matrix elements of $\beta(L+2S)$ can be calculated in the $(S,L,J,M_J)$ representation.
[^29]: See, for example, L. Pauling and S. Goudsmit, *The Structure of Line Spectra* (McGraw-Hill Book Company, Inc., New York, 1930), p. 165.
[^30]: C. Kittel, Phys. Rev. 76, 743 (1949).
[^31]: J. H. Van Vleck, Phys. Rev. 78, 266 (1950); see also reference 33.
[^32]: The values of $g$ and $g^\prime$ are taken from the review article by C. Kittel, J. phys. radium 12, 291 (1951), except for the value of $g$ for Co and the values of $g^\prime$ for MnSb and Fe$_3$O$_4$ which are from Scott's review article, reference 6.
[^33]: C. Kittel and A. H. Mitchell, Phys. Rev. 101, 1611 (1956).
[^34]: L. J. F. Broer, Physica 13, 473 (1947).
[^35]: I. K. Kikoin and S. W. Goobar, J. Phys. (U.S.S.R.) 3, 333 (1940); R. H. Pry, A. L. Lathrop, and W. V. Houston, Phys. Rev. 86, 905 (1952).
[^36]: N. F. Ramsey, *Molecular Beams* (Oxford University Press, New York, 1956), p. 60.
[^37]: N. F. Ramsey, *Molecular Beams* (Oxford University Press, New York, 1956), p. 163.
[^38]: The exception to this is the case of ferromagnets and antiferromagnets, which are not considered here.
[^39]: G. E. Pake, J. Chem. Phys. 16, 327 (1948).
[^40]: E. R. Andrew, *Nuclear Magnetic Resonance* (Cambridge University Press, New York, 1955), pp. 166-171.
[^41]: N. Bloembergen and T. J. Rowland, Phys. Rev. 97, 1679 (1955).
[^42]: W. D. Knight, in *Solid State Physics*, edited by F. Seitz and D. Turnbull (Academic Press Inc., New York, 1956), Vol. 2, p. 93.
[^43]: M. A. Rudermann and C. Kittel, Phys. Rev. 96, 99 (1954).
[^44]: N. F. Ramsey and E. M. Purcell, Phys. Rev. 85, 143 (1952).
[^45]: N. F. Ramsey, Phys. Rev. 78, 699 (1950).
[^46]: See, for example, the review by H. S. Gutowsky in *Annual Review of Physical Chemistry* (Annual Reviews, Inc., Stanford, California, 1954), Vol. 5, p. 333.
[^47]: W. E. Lamb, Phys. Rev. 60, 817 (1941).
[^48]: N. F. Ramsey, Phys. Rev. 89, 525 (1953).
[^49]: J. Dreitlein and H. Kessemeier, Phys. Rev. 123, 835 (1961).
[^50]: I. I. Rabi, N. F. Ramsey, and J. Schwinger, Revs. Modern Phys. 26, 167 (1954).
[^51]: See for example, H. Goldstein, *Classical Mechanics* (Addison-Wesley Publishing Company, Inc., Reading, Massachusetts, 1950), Chap. 10.
[^52]: R. K. Wangsness and F. Bloch, Phys. Rev. 89, 728 (1953).
[^53]: E. P. Wigner, *Group Theory* (Academic Press Inc., New York, 1959), p. 167.
[^54]: H. C. Torrey, Phys. Rev. 76, 1059 (1949); see also reference 50.
[^55]: A. G. Redfield, Phys. Rev. 98, 1787 (1955).
