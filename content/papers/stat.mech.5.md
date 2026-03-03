---
title: "Gibbs Formalism -- Physical Derivation"
author: ["E.T. Jaynes"]
year: 1965
---
In this Chapter we present physical arguments by which the Gibbs formal-
ism can be derived and justified, deliberately avoiding all use of
probability theory. This will serve to convince us of the *validity* of
Gibbs' formalism for the particular applications given by Gibbs, and
will give us an intuitive physical understanding of the second law, as
well as the physical meaning of the Kelvin temperature.

Later on (Chapter 9) we will present an entirely different derivation in
terms of a general problem of statistical estimation, deliberately
avoiding all use of physical ideas, and show that the identical
mathematical formalism emerges. This will serve to convince us of the
*generality* of the Gibbs meth- ods, and show that their applicability
is in no way restricted to equilibrium problems; or indeed, to physics.
It is interesting to note that most of Gibbs' important results were
found independently and almost simultaneously by Einstein (1902); but it
is to Gibbs that we owe the elegant mathematical formulation of the
theory. In the following we show how, from mechanical considerations
involving the micro- scopic state of a system, the Gibbs rules emerge as
a description of equili- brium macroscopic properties. Having this, we
can then reason backwards, and draw inferences about microscopic
conditions from macroscopic experimental data. We will consider only
classical mechanics here; however, none of this classical theory will
have to be unlearned later, because the Gibbs formalism
lost none of its validity through the development of quantum theory.
Indeed, the full power of Gibbs' methods has been realized only through
their suc- cessful application to quantum theory.
## Review of Classical Mechanics {#review-of-classical-mechanics .unnumbered}
In classical mechanics a complete description of the state of a system
is given by specifying n coordinates $q_1 \dots q_n$, and the
corresponding velocities $\dot{q}_1 \dots \dot{q}_n$. The equations of
motion are then determined by a Lagrangian function which in simple
mechanical problems is 
$$
L(q_i, \dot{q}_i) = T - V
$$
 where T and V are
the kinetic and potential energies. In problems involving coupling of
particles to an electromagnetic field, the Lagrangian function takes a
more general form, as we will see later. In either case, the equa- tions
of motion are
$$
\frac{\partial L}{\partial q_i} - \frac{d}{dt}\frac{\partial L}{\partial \dot{q}_i} = 0.
$$

The advantage of the Lagrangian form (5-2) over the original Newtonian
form (to which it is completely equivalent in simple mechanical
problems) 
$$
m\ddot{x}_i = -\frac{\partial V}{\partial x_i}
$$
 is that
(5-2) holds for arbitrary choices of the coordinates $q_i$; they can in-
clude angles, or any other parameters which serve to locate a particle
in space. The Newtonian equations (5-3), on the other hand, hold only
when the $x_i$ are rectangular (cartesian) coordinates of a particle.
Still more convenient for our purposes is the Hamiltonian form of the
equations of motion. Define the momentum \"canonically conjugate\" to
the co- ordinate $q_i$ by
$$
p_i = \frac{\partial L}{\partial \dot{q}_i}
$$
 and a Hamiltonian
function H by
$$
H(q_1, p_1 \dots q_n, p_n) = \sum_{i=1}^n p_i \dot{q}_i - L(q_1 \dots \dot{q}_n)
$$
the notation indicating that after forming the right-hand side of (5-5)
the velocities $\dot{q}_i$ are eliminated mathematically, so that the
Hamiltonian is ex- pressed as a function of the coordinates and momenta
only.
**Problem (5.1).** A particle of mass m is located by specifying
$(q_1, q_2, q_3) = (r, \theta, z)$ respectively, where r, $\theta$, z
are a cylindrical coordinate system re- lated to the cartesian x, y, z
by $x + iy = r e^{i\theta}$, $z = z$. The particle moves in a potential
$V(q_1, q_2, q_3)$. Show that the Hamiltonian in this coordinate system
is
$$
H(q_i, p_i) = \frac{p_1^2}{2m} + \frac{p_2^2}{2m} + \frac{p_3^2}{2m} + V(q_1, q_2, q_3)
$$
and discuss the physical meaning of $p_1, p_2, p_3$.
**Problem (5.2).** Find the Hamiltonian for the same particle, in the
spherical coordinate system $(q_1, q_2, q_3) = (r, \theta, \phi)$,
related to the cartesian by $x + iy = r \sin\theta e^{i\phi}$,
$z = r \cos\theta$, and again discuss the physical meaning of
$p_1, p_2, p_3$.

In terms of the Hamiltonian, the equations of motion assume a more sym-
metrical form:
$$
\dot{q}_i = \frac{\partial H}{\partial p_i} \qquad \dot{p}_i = -\frac{\partial H}{\partial q_i}
$$
of which the first follows from the definition (5-5), while the second
is equivalent to (5-2).

The above formulation of mechanics holds only when all forces are con-
servative; i.e. derivable from a potential energy function
$V(q_1, \dots, q_n)$, and in this case the Hamiltonian is numerically
equal to the total energy $(T + V)$. Often, in addition to the
conservative forces we have non-conservative ones which depend on the
velocities as well as the coordinates. The Lagrangian and Hamiltonian
form of the equations of motion can be preserved if there exists a new
potential function $M(q_i, \dot{q}_i)$ such that the non-conservative
force acting on coordinate $q_i$ is
$$
F_i = \frac{d}{dt}\frac{\partial M}{\partial \dot{q}_i} - \frac{\partial M}{\partial q_i}
$$

We then define the Lagrangian as $L = T - V - M$.
**Problem (5.3).** Show that the Lagrangian equations of motion (5-2)
are cor- rect with this modified Lagrangian. Find the new momenta and
Hamiltonian. Carry this through explicitly for the case of a charged
particle moving in a time-varying electromagnetic field
$\vec{E}(x,y,z,t)$, $\vec{H}(x,y,z,t)$ for which the non- conservative
force is given by the Lorentz force law,
$$
\vec{F} = e\left[\vec{E} + \frac{1}{c}\vec{v} \times \vec{H}\right]
$$
**Hint**: Express the potential M in terms of the vector and scalar
potentials of the field $\vec{A}, \phi$, defined by
$\vec{B} = \nabla \times \vec{A}$,
$\vec{E} = -\nabla\phi - \frac{1}{c}\frac{\partial\vec{A}}{\partial t}$.
Notice that, since the potentials are not uniquely determined by E, H,
there is no longer any unique connection between momentum and velocity;
or between the Hamiltonian and the energy. Nevertheless, the Lagrangian
and Hamiltonian equations of motion still describe the correct physical
laws.
## Liouville's Theorem {#liouvilles-theorem .unnumbered}
The Hamiltonian form (5-7) is of particular value because of the
following property. Let the coordinates and momenta
$(q_1, p_1 \dots q_n, p_n)$ be regarded as co- ordinates of a single
point in a 2n-dimensional phase space. This point moves, by virtue of
the equations of motion, with a velocity v whose components are
$(\dot{q}_1, \dot{p}_1 \dots \dot{q}_n, \dot{p}_n)$. At each point of
phase space there is specified in this way a particular velocity, and
the equations of motion thus generate a continuous flow pattern in phase
space, much like the flow pattern of a fluid in ordinary space. The
divergence of the velocity of this flow pattern is
$$
\text{div}(v) = \sum_{i=1}^n \left[ \frac{\partial \dot{q}_i}{\partial q_i} + \frac{\partial \dot{p}_i}{\partial p_i} \right] = \sum_{i=1}^n \left[ \frac{\partial^2 H}{\partial q_i \partial p_i} - \frac{\partial^2 H}{\partial p_i \partial q_i} \right] = 0
$$
so that the flow in phase space corresponds to that of an incompressible
fluid.

In an incompressible flow, the volume occupied by any given mass of the
fluid remains constant as time goes on and the mass of fluid is carried
into various regions. An exactly analogous property holds in phase space
by virtue of (5-9). Consider at time t = 0 any 2n-dimensional region
$\Gamma_o$ consisting of some possible range of initial conditions
$q_i(0), p_i(0)$ for a mechanical system, as shown in Fig. (5.1). This
region has a total phase volume
$$
\Omega(0) = \int_{\Gamma_o} dq_1 dp_1 \dots dq_n dp_n.
$$

 In time t,
each point $[q_1(0) \dots p_n(0)]$ of $\Gamma_o$ is carried, by the
equations of motion, into a new point $[q_1(t) \dots p_n(t)]$. The
totality of all points which were originally in $\Gamma_o$ now defines a
new region $\Gamma_t$ with phase volume
$$
\Omega(t) = \int_{\Gamma_t} dq_1 \dots dp_n
$$
 and from (5-9) it can be
shown that 
$$
\Omega(t) = \Omega(0).
$$
**[FIGURE: Volume-conserving flow in phase space.]**
An equivalent statement is that the Jacobian determinant of the
transformation $[q_1(0) \dots p_n(0)] \to [q_1(t) \dots p_n(t)]$ is
identically equal to unity:
$$
\frac{\partial(q_{1t} \dots p_{nt})}{\partial(q_{10} \dots p_{n0})} = 
\begin{vmatrix} 
\frac{\partial q_{1t}}{\partial q_{10}} & \dots & \frac{\partial p_{nt}}{\partial q_{10}} \\\\
\vdots &  & \vdots \\\\
\frac{\partial q_{1t}}{\partial p_{n0}} & \dots & \frac{\partial p_{nt}}{\partial p_{n0}} 
\end{vmatrix}
= 1
$$
**Problem (5.4).** Prove that (5-9), (5-11), and (5-12) are equivalent
statements. (Hint: See A. I. Khinchin, \"Mathematical Foundations of
Statistical Mechan- ics\", Chapter II.)

This result was termed by Gibbs the \"Principle of conservation of
exten- sion-in-phase\", and is usually referred to nowadays as
Liouville's theorem. An important advantage of considering the motion of
a system referred to phase space (coordinates and momenta) instead of
the coordinate-velocity space of the Lagrangian is that in general no
such conservation law holds in the latter space (although they amount to
the same thing in the special case where all
the $q_i$ are cartesian coordinates of particles and all forces are
conservative in the sense of Problem 5.3).
**Problem (5.5).** Liouville's theorem holds only because of the special
form of the Hamiltonian equations of motion, which makes the divergence
(5-9) identi- cally zero. Generalize it to a mechanical system whose
state is defined by a set of variables $(x_1, x_2, \dots, x_n)$ with
equations of motion for $x_i(t)$:
$$
\dot{x}_i(t) = f_i(x_1 \dots x_n), \qquad i = 1, 2, \dots, n
$$

 The
jacobian (5-12) then corresponds to
$$
J[x_1(0) \dots x_n(0); t] = \frac{\partial[x_1(t) \dots x_n(t)]}{\partial[x_1(0) \dots x_n(0)]}
$$

Prove that in place of Liouville's theorem J = 1 = const., we now have
$$
J(t) = J(0) \exp\left[ \int_0^t \sum_{i=1}^n \frac{\partial f_i[x_1(t) \dots x_n(t)]}{\partial x_i(t)} dt \right]
$$
## The Structure Function {#the-structure-function .unnumbered}
One of the essential dynamical properties of a system, which controls
its thermodynamic properties, is the total phase volume compatible with
various experimentally observable conditions. In particular, for a
system in which the Hamiltonian and the energy are the same, the total
phase volume below a certain energy E is
$$
\Omega(E) = \int \Theta[E - H(q_i p_i)] dq_1 \dots dp_n
$$
 (When limits
of integration are unspecified, we understand integration over all
possible values of $q_i, p_i$.) In (5-16), $\theta(x)$ is the unit step
function
$$
\theta(x) = \begin{cases} 1, & x > 0 \\\\ 0, & x < 0 \end{cases}
$$

The differential phase volume, called the structure function, is given
by
$$
\rho(E) = \frac{d\Omega}{dE} = \int \delta[E-H(q_i p_i)] dq_1 \dots dp_n
$$
and it will appear presently that essentially all thermodynamic
properties of the system are known if $\rho(E)$ is known, in its
dependence on such parameters as volume and mole numbers.

Calculation of $\rho(E)$ directly from the definition (5-18) is
generally very difficult. It is much easier to calculate first its
Laplace transform, known as the partition function:
$$
Z(\beta) = \int_0^\infty \rho(E) e^{-\beta E} dE
$$
 where we have
assumed that all possible values of energy are positive; this can always
be accomplished for the systems of interest by appropriately choos- ing
the zero from which we measure energy. In addition, it will develop that
full thermodynamic information is easily extracted directly from the
partition function $Z(\beta)$, so that calculation of the structure
function $\rho(E)$ is unneces- sary for some purposes.

Using (1-18), the partition function can be written as
$$
Z(\beta) = \int e^{-\beta H(q_i p_i)} dq_1 \dots dp_n
$$
 which is the
form most useful for calculation. If the structure function $\rho(E)$ is
needed, it is then found by the usual rule for inverting a Laplace
trans- form:
$$
\rho(E) = \frac{1}{2\pi i} \int_{-i\infty}^{i\infty} Z(\beta) e^{\beta E} d\beta
$$
the path of integration passing to the right of all singularities of
$Z(\beta)$, as in Fig. (5.2).
**[FIGURE: Path of integration in Equation (5-21).]**
To illustrate the above relations, we now compute the partition function
and structure function in two simple examples.
**Example 1. Perfect monatomic gas.** We have N atoms, located by
cartesian co- ordinates $q_1 \dots q_N$, and denote a particular
component (direction in space) by an index $\alpha, \alpha=1, 2, 3$.
Thus, $q_{i\alpha}$ denotes the $\alpha$'th component of the position
vector of the i'th particle. Similarly, the vector momenta of the
particles are denoted by $p_1 \dots p_N$, and the individual components
by $p_{i\alpha}$. The Hamiltonian is then
$$
H_1 = \sum_{i=1}^N \left[ \frac{p_i^2}{2m} + u(q_i) \right]
$$
 where
$$
p_i^2 = \sum_{\alpha=1}^3 p_{i\alpha}^2
$$
 and the potential function
u(q) defines the box of volume V containing the gas:
$$
u(q) = \begin{cases} u_o, & q_i \text{ in } V \\\\ \infty, & \text{otherwise} \end{cases}
$$

The arbitrary additive constant $u_o$, representing the zero from which
we measure our energies, will prove convenient later. The partition
function is then
$$
Z_1(\beta) = \left[ \int e^{-\frac{\beta p_i^2}{2m}} d^3 p_i \int e^{-\beta u(q_i)} d^3 q_i \right]^N
$$
$$
Z_1(\beta) = \left[ \left(\frac{2\pi m}{\beta}\right)^{3/2} V e^{-\beta u_o} \right]^N \tag{5-25}
$$
and the structure function is
$$
\rho_1(E) = \frac{V^N (2\pi m)^{3N/2}}{2\pi i} \int_{-i\infty}^{i\infty} \frac{e^{\beta(E - Nu_o)}}{\beta^{3N/2}} d\beta \tag{5-26}
$$

If N is an even number, the integrand is analytic everywhere in the com-
plex $\beta$-plane, except for the pole of order 3N/2 at the origin. If $E > Nu_o$,
the integrand tends to zero very rapidly as $|\beta| \to \infty$ in the left half-plane
Re$(\beta) \le 0$. The path of integration may then be extended to a closed one by
addition of an infinite semicircle to the left, as in Fig. (5.3), the integral
over the semicircle vanishing. We can then apply the Cauchy residue theorem
$$
\frac{1}{2\pi i} \oint_C \frac{f(z)dz}{(z-a)^{n+1}} = \frac{1}{n!} \frac{d^n}{da^n}f(a) \tag{5-27}
$$
where the closed contour C, illustrated in Fig. (5.4), encloses the point
$z=a$ once in a counter-clockwise direction, and $f(z)$ is analytic everywhere
on and within C.
**[FIGURE: Extensions of integration path in Equation (5-26).]**
**[FIGURE: The Cauchy Residue Theorem.]**
This gives for (5-23),
$$
\rho_1(E) = \frac{V^N (2\pi m)^{K+1}}{K!} \left. \frac{d^K}{d\beta^K} e^{\beta(E-Nu_o)} \right|_{\beta=0} \tag{5-28}
$$
where K = (3N/2) - 1. If $E < Nu_o$, the integrand of (5-26) tends to zero very
rapidly as $|\beta| \to \infty$ in the right half-plane Re$(\beta) \ge 0$, so the path of integra-
tion may be completed by addition of the infinite semicircle to the right,
also illustrated in Fig. (5.3). The integral over the semicircle is again
zero, but the closed path now contains no singularities of the integrand, and
by the Cauchy theorem the integral is now zero. Collecting results, we have
for N even,
$$
\rho_1(E) = 
\begin{cases}
\frac{V^N(2\pi m)^{3N/2}}{\left(\frac{3N}{2} - 1\right)!} (E-Nu_o)^{\frac{3N}{2}-1} & , E > Nu_o \\\\
0 & , E < Nu_o
\end{cases} \tag{5-29}
$$

If N is odd, we have a second-order branch point, instead of a pole, at $\beta = 0$.
We then add a branch cut along the negative real axis as shown in Fig. (5.5).
If $E < Nu_o$, we can still complete the path to the right as in Fig. (5.3), and
the integral is still zero.

If $E > Nu_o$ we cannot complete the path of integration C to the left be-
cause of the branch cut. We can, however, deform it to $C_1$ in Fig. (5.5),
since the integrals over the two infinite quarter-circles C', C'' still vanish.
If we now make the change of variables $s = \beta(E - Nu_o)$, the integral (5-26)
reduces to
$$
\rho_1(E) = V^N(2\pi m)^{3N/2} (E-Nu_o)^{\frac{3N}{2}-1} \frac{1}{2\pi i} \int_{C_1} e^s s^{-3N/2} ds \tag{5-30}
$$

But this is just Hankel's integral representation of the Gamma function
[Whittaker and Watson, (1927); Chap. 12]:
$$
\frac{1}{\Gamma(z)} = \frac{1}{2\pi i} \int_{C_1} e^s s^{-z} ds \tag{5-31}
$$
**[FIGURE: Path of integration for N odd.]**
which holds when z is any complex number. Therefore the previous result
(5-29) actually holds for N even or odd, provided that for N odd we understand
$(\frac{3N}{2}-1)!$ as standing for its analytic generalization, $\Gamma(3N/2)$. The factorial
notation is often more convenient than the $\Gamma$-function notation, and so we
understand that the factorial of any number, real or complex, is defined by
$$
x! \equiv \Gamma(x+1) \tag{5-32}
$$
**Example 2. Assembly of Harmonic Oscillators.** We have N particles of mass m,
and this time we label the cartesian coordinates and corresponding momenta by
$\{q_1 \dots q_n\}$, $\{p_1 \dots p_n\}$, with n = 3N. The potential energy is a positive defi-
nite quadratic form in the $q_i$, so the Hamiltonian is
$$
H_2(q_i p_i) = \sum_{i=1}^n \frac{p_i^2}{2m} + \frac{1}{2}\sum_{i,j=1}^n a_{ij}q_i q_j \ge 0 \tag{5-33}
$$
where, without loss of generality, $a_{ij}$ can be considered a symmetric matrix:
$a_{ij} = a_{ji}$. The partition function is then
$$
\begin{aligned}
Z_2(\beta) &= \left[ \int_{-\infty}^\infty e^{-\frac{\beta p_i^2}{2m}} dp_i \right]^n \left[ \int_{-\infty}^\infty \dots \int_{-\infty}^\infty \exp\left\{-\frac{\beta}{2} \sum_{i,j} a_{ij}q_i q_j\right\} dq_1 \dots dq_n \right] \\\\
&= \left( \frac{2\pi m}{\beta} \right)^{n/2} \frac{(2\pi)^{n/2}}{\sqrt{\beta^n \det(a_{ij})}}
\end{aligned} \tag{5-34}
$$
the formula for the integral over the q's being easily derived from the ele-
mentary integral
$$
\int_{-\infty}^\infty \dots \int_{-\infty}^\infty \exp\left[-\frac{1}{2}\sum_{k=1}^n a_k x_k^2\right] dx_1 \dots dx_n = \prod_{k=1}^n \sqrt{\frac{2\pi}{a_k}} \tag{5-35}
$$
by making the substitutions
$$
x_k = \sum_{j=1}^n M_{kj} q_j, \qquad \sum_{k=1}^n a_k M_{ki} M_{kj} = a_{ij} \tag{5-36}
$$
where M is any matrix with nonvanishing determinant, and using the fact that
the determinant of the product of matrices is the product of the determinants:
$$
\det(a_{ij}) = [\det(M)]^2 \prod_{k=1}^n a_k \tag{5-37}
$$

Better physical understanding of the result (5-34) is achieved by transforma-
tion of the Hamiltonian (5-33) to normal mode coordinates. The matrix $a_{ij}$ is
real and symmetric, and so by a well-known result of matrix theory [Margenau
and Murphy (1943); Chap. 10] there exists an orthogonal matrix N,
$$
\sum_{i=1}^n N_{ij} N_{ik} = \delta_{jk}
$$
which diagonalizes $a_{ij}$:

$$
(\tilde{N} A N)_{kl} = \sum_{i,j=1}^n a_{ij} N_{ik} N_{jl} = \lambda_k \delta_{kl} = m\omega_k^2 \delta_{kl} \tag{5-39}
$$
The last step merely defines a new quantity $\omega_k$. If now we introduce new co-
ordinates $Q_k$, defined by
$$
q_i = \frac{1}{\sqrt{m}} \sum_{k=1}^n N_{ik} Q_k, \tag{5-40}
$$
the potential energy reduces to
$$
V = \frac{1}{2} \sum_{i,j=1}^n a_{ij} q_i q_j = \frac{1}{2} \sum_{k=1}^n \omega_k^2 Q_k^2 \tag{5-41}
$$
The kinetic energy appears in the Lagrangian as
$$
T = \frac{1}{2} m \sum_i \dot{q}_i^2 = \frac{1}{2} \sum_{k=1}^n \dot{Q}_k^2 \tag{5-42}
$$
where we used (5-40) and (5-38). The Lagrangian in terms of the new coordi-
nates thus reduces to
$$
L = \frac{1}{2} \sum_{k=1}^n \left[ \dot{Q}_k^2 - \omega_k^2 Q_k^2 \right] \tag{5-43}
$$
The momentum canonically conjugate to $Q_k$ is therefore
$$
P_k = \frac{\partial L}{\partial \dot{Q}_k} = \dot{Q}_k \tag{5-44}
$$
and the Hamiltonian in the new coordinates is
$$
H_2 = \frac{1}{2} \sum_{k=1}^n \left[ P_k^2 + \omega_k^2 Q_k^2 \right] \tag{5-45}
$$
This yields the equations of motion
$$
\dot{Q}_k = \frac{\partial H}{\partial P_k} = P_k \tag{5-46}
$$
$$
\dot{P}_k = -\frac{\partial H}{\partial Q_k} = -\omega_k^2 Q_k \tag{5-47}
$$
or
$$
\ddot{Q}_k + \omega_k^2 Q_k = 0 \tag{5-48}
$$
and so the $\omega_k$ are the normal mode oscillation frequencies of the system, $Q_k$
is the corresponding normal coordinate. Taking the determinant of (5-39), we
have
$$
\det(a_{ij})[\det(N)]^2 = m^n \prod_{k=1}^n \omega_k^2 \tag{5-49}
$$
but $\det(N) = \pm 1$ from (5-38), and so the partition function (5-34) reduces to
$$
Z_2(\beta) = \left( \frac{2\pi}{\bar{\omega}\beta} \right)^n = \left( \frac{2\pi}{\bar{\omega}\beta} \right)^{3N} \tag{5-50}
$$
where $\bar{\omega}$ is the geometric mean of all the oscillation frequencies, defined by
$$
\bar{\omega}^n = \prod_{k=1}^n \omega_k \tag{5-51}
$$
As a check, note that (5-50) can be derived directly from the transformed
Hamiltonian (5-45) by application of (5-20) and (5-35). This is an example of
the fact that the partition function (5-20) is invariant under any canonical
transformation $(q_i, p_i) \to (Q_k, P_k)$, so that in calculating $Z(\beta)$ we are at liberty
to use any coordinate system that proves to be convenient mathematically.
**Problem (5.6).** In the Debye model of a crystal, lattice vibration modes are
distributed in frequency with a density $\rho(\omega)$ proportional to $\omega^2$; i.e. the
number of modes in a frequency interval $d\omega$ is
$$
\rho(\omega)d\omega = A\omega^2 d\omega
$$
 up to a maximum frequency
$\omega_{max}$, and $\rho(\omega)=0$ for $\omega > \omega_{max}$. Find
the constant A in terms of $\omega_{max}$ and the number N of atoms in
the crystal, and show that the geometrical mean frequency is
$$
\bar{\omega} = \exp(-1/3) \omega_{max} = 0.716 \omega_{max}
$$

The structure function for the assembly of harmonic oscillators is now
found immediately by the method of (5-28):
$$
\rho_2(E) = \left(\frac{2\pi}{\bar{\omega}}\right)^{3N} \frac{1}{2\pi i} \int_{-i\infty}^{i\infty} \frac{e^{\beta E}}{\beta^{3N}} d\beta = \left(\frac{2\pi}{\bar{\omega}}\right)^{3N} \frac{E^{3N-1}}{(3N-1)!} \tag{5-52}
$$

In both examples, the structure function increases as a very high power
of E. This is typical of all macroscopic systems, and it is an essential
part of the reason they exhibit reproducible thermodynamic properties.
The phase volume relations can be visualized by means of semi-realistic
diagrams like Fig. (5.6). The vertical coordinate represents the energy.
Imagine a tapered vase filled with water up to a level equal to the
energy of the system. The total volume of water needed to fill it to
this level cor- responds to the phase volume $\Omega(E)$, the surface
area to the structure function $\rho(E)$. Because $\rho(E)$ increases as
an enormously high power of E, the vase flares at an enormous rate, not
possible to depict in the diagram. It is, in fact so rapid that
practically all of the phase volume up to energy E is ac- tually
contained in a very small range $\delta E$ just under the surface E. For
ex- ample, if $\rho(E) = A E^{n-1}$, then $\Omega(E) = (E/n)\rho(E)$,
and the energy shell $\delta E$ con- tains half the phase volume
$\Omega(E)$ if $\rho(E)\delta E = \frac{1}{2}\Omega(E)$, or
$$
\frac{\delta E}{E} = \frac{1}{2n}
$$
 i.e., the half-volume shell, for a
macroscopic system, has relative thickness of only about one part in
$10^{24}$. If we take the still very small energy shell of thickness
$\delta E = E/\sqrt{n} \approx 10^{-12} E$, we find that
$$
\int_{E-\delta E}^E \rho(E) dE = \Omega(E) - \Omega\left(E-\frac{E}{\sqrt{n}}\right) = \Omega(E)[1-e^{-\sqrt{n}}]
$$
so that only an infinitesimal fraction
**[FIGURE: Representation of phase volume and structure function.]**
$$
e^{-(10^{12})} \approx 10^{-(4.3 \times 10^{11})} \tag{5-54}
$$
of the phase volume $\Omega(E)$ lies below this energy shell. The suggested analogy
to water filling a vase actually holds in a much more important sense,
as we will see presently.
**Problem (5.7).** Calculate the structure function $\rho(E)$ for a
spherical pendulum consisting of a mass m connected to the origin by a
weightless rod of length L, for which the Lagrangian is
$$
L(\theta, \dot{\theta}, \phi, \dot{\phi}) = \frac{1}{2}mL^2\dot{\theta}^2 + \frac{1}{2}mL^2\sin^2\theta \dot{\phi}^2 + mgL\cos\theta,
$$
$\theta$ being the angle the rod makes with the vertical, $\phi$ the
azimuth angle.
## Relation to Thermodynamics {#relation-to-thermodynamics .unnumbered}
Suppose we place two systems with structure functions
$\rho_1(E) = A_1 E^{n_1}$, $\rho_2(E) = A_2 E^{n_2}$ in loose contact so
that they can exchange energy, but not par-
ticles. Together they constitute a larger system with phase volume below
total energy E given by
$$
\Omega(E) = \int_0^E \rho_1(E_1) \Omega_2(E-E_1) dE_1
$$
 or,
differentiating with respect to E, the structure function of the
combined system is 
$$
\rho(E) = \int_0^E \rho_1(E_1)\rho_2(E-E_1) dE_1
$$

Now for macroscopic systems the exponents $n_1, n_2$ are very large as
we have seen. Therefore the integrand of (5-56) has a single enormously
sharp peak, and practically all the contribution to the integral (5-56)
comes from values of $E_1$ in the immediate neighborhood of this peak.
The value of $E_1$ at the peak is found by differentiating:
$$
\frac{d}{dE_1}[\rho_1(E_1)\rho_2(E-E_1)] = \rho_1'(E_1)\rho_2(E-E_1) - \rho_1(E_1)\rho_2'(E-E_1) = 0
$$
or, 
$$
\frac{d\log\rho_1}{dE_1} = \frac{d\log\rho_2}{dE_2}
$$

 Let us
investigate the sharpness of this peak. The logarithm of the integrand
is
$$
L(E_1) = \log[\rho_1(E_1)\rho_2(E-E_1)] = \log(A_1A_2) + n_1\log E_1 + n_2\log(E-E_1)
$$

Expand this in a Taylor series about the value $E_1 = E_{10}$ which
maximizes $L(E)$, noting that $(E-E_{10}) = (n_2/n_1)E_{10}$;
$$
\begin{aligned}
L(E_1) = L_{max} &- \frac{n_1}{2}\left[\frac{1}{n_1} + \frac{1}{n_2}\right]\frac{(E_1-E_{10})^2}{E_{10}^2} + \dots \\\\
&\quad + 2n_1 \left[ 1 - \frac{n_1^2}{n_2^2} \right] \frac{(E_1 - E_{10})^3}{3! E_{10}^3} \\\\
&\quad - 3! n_1 \left[ 1 + \frac{n_1^3}{n_2^3} \right] \frac{(E_1 - E_{10})^4}{4! E_{10}^4} + \dots
\end{aligned}
$$
if the fractional deviation from the maximum is small; i.e. if
$$
|E_1 - E_{10}| \ll E_{10} \frac{n_2}{n_1}
$$
 then all the succeeding
terms are very small compared to the term in $(E_1 - E_{10})^2$, and so
a good approximation is
$$
\rho_1(E_1)\rho_2(E-E_1) = (\rho_1\rho_2)_{max} \exp\left[-n_1 \left(1+\frac{n_1}{n_2}\right) \frac{(E_1 - E_{10})^2}{2 E_{10}^2}\right]
$$
**Problem (5.8).** As a check on the accuracy of the approximation
(5-61), note that it leads to an approximate expression for $\rho(E)$ by
using (5-56): 
$$
\begin{aligned}
\rho(E) &= (\rho_1\rho_2)_{max} \int_{-\infty}^\infty \exp\left[-n_1 \left(1+\frac{n_1}{n_2}\right) \frac{(E_1 - E_{10})^2}{2 E_{10}^2}\right] dE_1 \\\\
&= (\rho_1\rho_2)_{max} \sqrt{\frac{2\pi E_{10}^2 n_2}{n_1(n_1+n_2)}} \notag
\end{aligned}
$$

 Calculate the exact $\rho(E)$ from (5-56) and compare
with (5-62). The following formulas will be useful here: (1) the
Eulerian integral of the first kind, or complete Beta function, is
$$
\int_0^1 x^a (1-x)^b dx = \frac{a!b!}{(a+b+1)!}
$$
\(2\) the Stirling approximation for factorials of large numbers is
$$
\log N! = N \log N - N + \frac{1}{2}\log(2\pi N) + O\left(\frac{1}{N}\right)
$$

The relative contribution of various ranges of $E_1$ to $\rho(E)$ may be
seen from tables of the \"error function\":
$$
\text{erf } x = \frac{2}{\sqrt{\pi}} \int_0^x e^{-t^2} dt
$$

 Some
numerical values of erf x are:
     x                   erf x
  ------- ------------------------------------
    0.0                 0.00000
    0.5                 0.52050
    1.0                 0.84270
    1.5                 0.96611
    2.0                 0.99532
    2.5                 0.99959
    3.0                 0.99998
   $> 3$   $1 - \frac{e^{-x^2}}{x\sqrt{\pi}}$
Suppose, for simplicity, that $n_1=n_2=10^{24}$. Then, letting
$$
x = \sqrt{n_1}\frac{E_1 - E_{10}}{E_{10}} = 10^{12} \frac{E_1-E_{10}}{E_{10}},
$$
we see from the table that over 84 per cent of the integral
$$
\int_0^E \rho_1(E_1)\rho_2(E-E_1)dE_1
$$
 is contributed by values of
$E_1$ in the range
$$
E_{10} \pm \frac{E_{10}}{\sqrt{n_1}} = E_{10}[1 \pm 10^{-12}]
$$

Similarly, 99.998 per cent of the integral is contributed by values of
$E_1$ in a range three times as wide: $E_{10}(1 \pm 3 \times 10^{-12})$.
Values of $E_1$ which deviate from $E_{10}$ by more than one part in a
million contribute one part in
$$
\frac{e^{-x^2}}{x\sqrt{\pi}} \approx \frac{\exp[-10^{12}]}{10^6 \sqrt{\pi}} \approx 10^{-(4.3 \times 10^{11})}
$$
to the structure function of the combined system.

To state this remarkable situation in the most useful way of all for our
purposes, suppose the phase point of a system is known to be in a small
region $\delta\Omega$ of phase space, comprised within the energy shell
of thickness $\delta E$. If $\delta\Omega$ contains as much as one part
in $10^{10^{10}}$ of the total phase volume of this energy shell; i.e.
if $\delta\Omega \ge 10^{-(10^{10})} \rho(E)\delta E$, then 
the fraction of the phase volume $\delta\Omega$ in which $E_1$ differs from $E_{10}$ by as much as one part in $10^6$, is necessarily less than $10^{-(4 \times 10^{11})}$.

 Suppose that these two systems were initially given arbitrary
energies $E_1(0), E_2(0)$ and at time $t=0$ were placed in contact so
that the energies $E_1(t), E_2(t)$ become redistributed. The systems
being otherwise isolated, the total energy $E = E_1(t) + E_2(t)$ will
remain constant. Now on the one hand we know (Liouville's theorem) that
phase volume for the combined system is con- served in the time
development. On the other hand, we have just seen that
the overwhelmingly greatest part of *all* the phase volume accessible to
the system corresponds very accurately to one definite distribution of
energy $E_1$, $E_2$, such that
$$
\frac{\partial\log\rho_1}{\partial E_1} = \frac{\partial\log\rho_2}{\partial E_2}
$$

Thus, if we are asked to predict the final distribution of energy
reached after a long interaction time, it will be a pretty safe bet that
the subsys- tems will divide up the available energy in such a way that
(5-70) is satis- fied.

To illustrate the reasoning here in a case where the numbers are much
more modest, suppose the entire surface of the earth painted red, with
the exception of one particular square centimeter, which is painted
blue. Con- sider now the last nitrogen molecule emitted in the dying
gasp of Julius Caesar. Evidently, we cannot predict very well just where
it is now, but if we are asked to predict only whether it is at this
moment over a red or blue area, it is a pretty safe bet that the answer
is \"red\". Not because we be- lieve that the nitrogen molecule has any
tendency to prefer red regions, but only because there are so many more
of them. Indeed, it would take an *enor- mously* strong tendency to
*avoid* red regions, before there could be any dif- ference in our
conclusions; this is the analog of statement (5-69). The numbers here
are much more modest, however, because the total surface area of the
earth is only about $5 \times 10^{18}$ cm$^2$. If the blue region were
reduced to one square Angstrom, we would be concerned with numbers of
about $5 \times 10^{34}$, still utterly negligible compared to those
involved in (5-69).

As the reader can easily verify, this result holds for any number of
systems in contact, so that they share a common energy; the
*overwhelmingly* greatest part of all the phase volume of the combined
system corresponds very
accurately to a particular distribution of energy among the subsystems
such that
$$
\frac{\partial\log\rho_1}{\partial E_1} = \frac{\partial\log\rho_2}{\partial E_2} = \frac{\partial\log\rho_3}{\partial E_3} = \dots
$$

We can hardly interpret this otherwise than that [equal
$\partial \log\rho/\partial E$ means equal temperature]{.underline}. In
other words, we infer that the quantity
$$
x = \frac{\partial\log\rho(E,V)}{\partial E} = x(T)
$$
 must be some
function of the Kelvin temperature T. To find what function it is, there
is only one criterion. As we saw in Chapter 1, Sec. 1.8, in a closed
system (i.e. no particles enter or leave), $T^{-1}$ is defined as the
in- tegrating factor that converts the infinitesimal heat flow,
$dQ = dE + P dV$, into an exact differential $dS = T^{-1} dQ$ of some
state function $S(E,V)$, where P, V are the pressure and volume of our
system. For convenience, call this integrating factor w:
$$
T^{-1} = w = w(x)
$$
 then we can repeat the argument of Equations
(1-20) -- (1-28): 
$$
dS = w \, dQ = w \, dE + wP \, dV
$$
 so that
$$
w = \left(\frac{\partial S}{\partial E}\right)_V, \qquad wP = \left(\frac{\partial S}{\partial V}\right)_E
$$
and the condition that dS is an exact differential is
$$
\frac{\partial^2 S}{\partial E \partial V} = \frac{\partial^2 S}{\partial V \partial E}
$$
or,
$$
\left(\frac{\partial w}{\partial V}\right)_E = \left(\frac{\partial(wP)}{\partial E}\right)_V
$$

This yields
$$
w^\prime(x)\left(\frac{\partial x}{\partial V}\right)_E = w(x)\left(\frac{\partial P}{\partial E}\right)_V + w^\prime(x)P\left(\frac{\partial x}{\partial E}\right)_V
$$
or, the function w(x) must satisfy
$$
\frac{w^\prime(x)}{w(x)} = \frac{\left(\frac{\partial P}{\partial E}\right)_V}{\left(\frac{\partial x}{\partial V}\right)_E - P\left(\frac{\partial x}{\partial E}\right)_V}
$$

It is clear that this program will fail unless the right-hand side of
(5-77) turns out to be a function of x alone; and we will not have
succeeded in establishing a [universal]{.underline} temperature scale
unless the right-hand side of (5-77) is a [universal]{.underline}
function (i.e., the same function for all systems) of x. These
properties are far from obvious from the form of (5-77).

We cannot solve (5-77) immediately because, although the derivatives in
the denominator are known from (5-72) if $\rho(E,V)$ is known, we do not
yet know how the pressure is related to these quantities. To investigate
this, suppose we increase the volume (for example, by moving a piston).
The system does work, and its energy decreases by
$$
\Delta E = - \int_{V_o}^{V_1} P dV = E_1 - E_o
$$

 The original and
final conditions can be visualized in the semirealistic man- ner of Fig.
(5.6).

The system has an initial energy $E_o$ which we suppose controlled to an
accuracy $\delta E_o$. Thus at the start of the expansion, the system
might be any- where in the phase volume $\rho_o(E_o)\delta E_o$ depicted
at the top of Fig. (5.7a). The
structure function $\rho(E,V)$ will depend on V in a manner
qualitatively like Eq. (5-26); i.e. the expansion of V has the effect of
widening the \"vase\" to the configuration of Fig. (5.7b).

We suppose that on repetitions of this experiment, the change in energy
$\Delta E$ is reproducible. Not because we know of any law of physics
which says that i [must]{.underline} be so, but merely because
thermodynamics is concerned only with reproducible phenomena. If the
work $\Delta E$ varied widely on different repetitions of the
experiment, then no one would think of applying thermodynamics to this
process.

More generally, it is an experimental fact that with an easily
attainable degree of control over experimental conditions, the
observable behavior of most macroscopic systems [is]{.underline}
reproducible. This is a necessary condition for any general theory to be
either useful or possible. Indeed, without this property of
\"macroscopic uniformity\", our measuring instruments would not work
predictably, and neither experimental nor theoretical physics would be
possible.
**[FIGURE: Phase volume relations before and after expansion.]**
We emphasize this because the fact itself is so commonplace to all of us
that we might not notice that, from the standpoint of general dynamics,
as exemplified in the Hamiltonian equations of motion, it is a rather
surprising property. [There is no known property of the Hamiltonian per
se that would lead us to expect this]{.underline}. The fact that
macroscopic experiments are reproduci- ble is thus, from the standpoint
of Hamiltonian mechanics, an entirely \"new\" fact, from which we should
be able to draw new conclusions.

To find such a new conclusion, we might reason as follows. Referring to
Fig. (5.7), if the change $\Delta E$ is reproducible, then it must be
that practically every initial state in the shaded region of volume
$\rho_o(E_o)\delta E_o$ leads to a final energy in the range
$\omega E_1$, of phase volume $\rho_1(E_1)\delta E_1$. But since phase
volume is conserved by the equations of motion, the final volume must be
as least large enough to accommodate all these points. Thus, a
[necessary]{.underline} condition for the process to be reproducible
with the specified tolerances $\delta E_o, \delta E_1$ on initial and
final energies, is 
$$
\rho_1(E_1)\delta E_1 \ge \rho_o(E_o)\delta E_o
$$

But, because of the numerical situation noted above, (5-79) is not the
most appropriate way of stating this condition. For, the exact phase
volume cor- responding to the energy increment $\delta E$ is
$$
\int_{E-\delta E}^E \rho(E) dE = \Omega(E) - \Omega(E-\delta E)
$$
 and
if $\delta E$ is so small that this is well approximated simply by
$\rho(E)\delta E$, then $\delta E$ must be far smaller than the
tolerance with which we could hope to measure the energy experimentally.
Indeed, if $\delta E$ represents any reasonable experi- mental error,
then (5-80) reduces, to enormously great accuracy, simply to
$\Omega(E)$, so that (5-79) ought to be replaced by
$$
\Omega_1(E_1) \ge \Omega_o(E_o)
$$

 Thus, (5-79) is not a realistic
statement of any experimental fact.

In view of this, a weaker condition than (5-79), which exploits the same
idea, will suffice for our purposes. Referring again to Fig. (5.7), it
is surely a well-verified experimental fact that [if]{.underline} the
initial energy $E_o$ leads reproducibly, and within experimental error,
to the final energy $E_1$, then any lower initial energy $E_o^\prime < E_o$
will lead to a lower final energy $E_1' < E_1$. In other words, any
initial state in the phase volume $\rho_o(E_o)$ must lead to a final
state in the phase volume $\rho_1(E_1)$. As before, this is possible
only if the final phase volume is large enough to accommodate all these
states, which leads again to the condition (5-81).

More generally, we see that an immediate consequence of Liouville's
theorem is that in [any]{.underline} reproducible process, the phase
volume compatible with the final macroscopic state cannot be less than
the phase volume which mea- sures the accuracy with which we can
reproduce the initial state: 
$$
\Omega_{final} \ge \Omega_{initial}
$$

Evidently this must hold however we specify the initial and final
states; i.e. instead of energy we may specify the observed pressure,
stress, magnetization, angular momentum, or any other macroscopic
properties. Furthermore, the result (5-82) must hold whether or not the
initial and final states are equi- librium states.

Now suppose we compress the system from volume $V_1$ back to the
original volume $V_o$. It will acquire a final energy $E_2$, and we
shall have to do work $E_2 - E_1$. If this work done is experimentally
reproducible, then exactly the same argument about phase volumes
applies, and it is necessary that 
$$
\Omega_2(E_2) \ge \Omega_1(E_1)
$$

If the expansion and compression are carried out rapidly, it will be
found experimentally that the work required for compression is greater
than that obtained from the expansion, so that $E_2 > E_o$; this is a
particular case of the second law of thermodynamics. But in the limit
where these processes are carried out so slowly that the system is at
all times very close to equili- brium, $E_2$ approaches $E_o$, and we
have a [reversible]{.underline} process. But, if $E_2 = E_o$, comparison
of (5-81) and (5-83) shows that 
$$
\Omega_o(E_o) = \Omega_1(E_1)
$$

 Under
these conditions, the pressure P of (5-78) will be the thermal equili-
brium value which we needed to find in order to solve (5-77).

Thus, the missing relation we need for (5-77) is
$$
P = -\left(\frac{\partial E}{\partial V}\right)_\Omega = -\left(\frac{\partial E}{\partial V}\right)_{\log\Omega}
$$
but let us cast it into a more useful form. For any macroscopic system
we will have a result more or less like (5-29); or
$$
\Omega(E) = AV^n E^m, \qquad \rho(E) = mAV^n E^{m-1}
$$
 where n and m
are of the order of Avogadro's number. But then 
$$
\begin{aligned}
\log\Omega &= n\log V + m \log E + \text{const.} \\\\
\log\rho &= n\log V + (m-1) \log E + \text{const.} \notag
\end{aligned}
$$

 Now the condition ($\log\Omega = \text{const.}$) on
(5-85) imposes a relation between E and V which determines the value of
the derivative. From (5-87) it is clear that the condition
($\log\rho = \text{const.}$) imposes the [same]{.underline} relation, to
an accuracy of something like one part in $10^{24}$. More specifically,
$$
\begin{aligned}
\left(\frac{\partial E}{\partial V}\right)_{\log\Omega} &= -\frac{nE}{mV} \notag \\\\
\left(\frac{\partial E}{\partial V}\right)_{\log\rho} &= -\frac{nE}{(m-1)V}
\end{aligned}
$$
 and so, unless we propose to measure the pressure to
better than 1 part in $10^{24}$ (which as we will see later is about
$10^{12}$ times smaller than the spontaneous fluctuations continually
taking place in P anyway), we can just as well write
$$
P = -\left(\frac{\partial E}{\partial V}\right)_{\log\rho}
$$
 which is
exactly the relation we need to complete the solution of (5-77).
