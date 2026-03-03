---
title: "Long-Term Solutions in Semiclassical Radiation Theory"
author: ["E.T. Jaynes"]
year: 1970
abstract: >
  An improved form of semiclassical radiation theory is developed which
  includes the effect of the atom's radiation field back on the atom.
  This formalism is applied to the problem of a single "two-level atom"
  interacting with a monochromatic field. The resulting equations are
  solved without resorting to time-dependent perturbation theory, and
  are found to predict the behavior of the system over times long
  compared with the lifetime for spontaneous transitions. Not only
  stimulated emission and absorption, but also spontaneous emission with
  the proper Einstein A coefficient, and a frequency shift which agrees
  at least semiquantitatively with the Lamb shift are described. In
  addition, several nonlinear effects involving the interference between
  spontaneous and stimulated radiation are described, and new
  experiments which might detect such effects are suggested.
---
# INTRODUCTION
The theory of interaction of optical radiation with atoms, beginning
with Einstein's introduction of the A and B coefficients[^2] and refined
by later applications of quantum theory,[^3][^4][^5][^6] has
for many years predicted all aspects of these phenomena on which we have
experimental evidence. However, this evidence, while large in volume, is
limited in scope. Recent advances (lasers, etc.) bring into the area of
feasible experiments a wider range of phenomena, in which our present
theory has received almost no experimental tests thus far. In planning
new significant experiments, a more detailed theoretical treatment of
these phenomena is needed, part of which is given in the present work.
The original optical experiments (from roughly 1880 to 1930) provided
most of the clues on which our present quantum theory is based, but, in
fact, they gave evidence only on what might be called the "kinematic"
and "amplitude" aspects, and not on the "dynamic" or the coherence
aspects, of radiation phenomena. For example, they gave quantitative
verifications of the positions of spectral lines, but not about such
dynamic matters as the shape of the spontaneous emission pulse emitted
by an atom, or about the mutual coherence of radiation from nearby
atoms. Absorption spectrum experiments also gave line positions, but no
evidence about the dynamics by which the absorption develops in time
with sudden illumination. Likewise, one observed the amplitude and
polarization of resonance radiation, but not its degree of phase
coherence with the primary radiation, or the dynamics of its transient
buildup when an atom is suddenly illuminated.

More recent experiments have continued to check the kinematic rather
than the dynamical aspects of radiation theory. Thus, the existing
experiments on the Lamb shift[^7][^8][^9][^10] have measured
only the incident frequency needed to initiate a transition, starting
from a metastable S state. The experimental fact is that upward
transitions are observed to start at a lower frequency, and downward
ones at a higher frequency, than predicted by the elementary solution of
the Dirac equation. This is consistent with the view that the Lamb shift
arises from a raising of the S levels relative to others; but it is
equally consistent with the view that radiative line shifts increase the
frequency of all downward transitions and lower the frequency of upward
ones, whose behavior could not be described in terms of level shifts at
all. Nor do the existing experiments answer the question whether the
radiative line shift remains constant throughout the transition; they
are equally consistent with a theory (which, as we will see, has some
*raison d'être*) in which radiative effects raise the frequency of all
lines during the part of the emission or absorption when the atom is
near the upper level, and lower it when the atom is near the lower
level. Further experiments are thus needed before one could claim that
our present theory of the Lamb shift is established to the exclusion of
thinkable alternatives.

Thus far, dynamical and coherence properties have been observed only as
smeared-out statistical averages, which do not permit inferences about
the underlying elementary processes. Thus, existing experiments on
blackbody radiation measure only its spectral density, and not further
details of the field fluctuations. Such measurements are consistent with
the notion of sudden exchanges of energy $\hbar\omega$ between field and
atom; but they do not require this, since a continuous energy exchange
following any curve of a certain symmetry will lead to just the same
time average for the field energy in any spectral region. Likewise, the
observed exponential decay of fluorescence is consistent with the idea
that each atom emits an exponentially damped wave train, as in the
Wigner-Weisskopf theory[^4]; but it does not require this, since the
total radiation will fall off exponentially, whatever the shape of the
basic spontaneous emission pulse, provided only that the number of
emitting atoms falls off exponentially.

There are other dynamical effects on which we can hardly claim to have
experimental evidence, even in the form of statistical averages. For
example, what interference effects are to be expected when spontaneous
and induced emission proceed simultaneously? What nonlinear effects
result when an atom interacts with a coherent radiation field over long
time intervals? The state of such an atom can always be described by a
density matrix $\rho(t)$. Does $\rho(t)$ settle down to a steady state,
approach a periodic limit cycle, or exhibit some more complicated
long-time behavior? All of the aforementioned dynamical and coherence
effects appear to be in the range where more detailed experimental
evidence could now be obtained.

As far as the theoretical treatment of these phenomena is concerned, the
distinction between "dynamic" and "kinematic" is simply whether
time-dependent perturbation theory is sufficient to describe the
phenomena. To describe "dynamic" phenomena one must develop means of
solving the Schrödinger equation accurately over long time intervals
(e.g., in which an atom undergoes a large change of state), but without
losing phase information. The purpose of this paper is to develop such a
method of solution, and to present several applications, leading to a
number of predictions not yet tested by experiment but on which the
experiments are now feasible.
## QUANTUM ELECTRODYNAMICS AND SEMI-CLASSICAL THEORY
Further study of dynamical and coherence phenomena may prove to have a
greater fundamental importance than would appear at first glance. It is
well known that our present theory of radiation, quantum electrodynamics
(QED), faces serious logical and mathematical difficulties.[^11] The
appearance of divergent integrals in almost every nontrivial problem can
be traced in part to infinite vacuum fluctuations, and in part to the
particular propagators used. The Feynman propagator $S_F(x-x^\prime)$ raises a
difficulty about relativistic causality in that it fails to vanish for
spacelike intervals $(x-x^\prime)^2$. In addition, it has a singularity
$(c^2t^2-r^2)^{-2}$ on the light-cone,[^12] which alone is sufficient to
guarantee divergence of almost any integral of the form
$\int S_F(x-x^\prime)f(x^\prime)dx^\prime$. It is only after using devices such as
regulators and renormalization techniques, or by striking out certain
divergent expressions on grounds of Lorentz or gauge invariance, that
one obtains finite results that can be compared with experiment.

Yet the finite parts of the propagator $S_F$ appear necessary for
agreement with experiment. For example, in the calculation of vacuum
polarization given by Bjorken and Drell,[^13] use of the retarded
propagator, instead of $S_F$, greatly improves the convergence and
removes the difficulty about causality; but it also leads to the
prediction of zero vacuum polarization. It might be thought possible to
separate $S_F$ into its "physical" and "nonphysical" parts; but as
yet no one has seen how to do this.

For these reasons, there has been a growing dissatisfaction with the
present theory, in spite of its experimental successes. Even Dirac,[^14]
the founder of QED, has recently described its present form as "a
stopgap, without any lasting future." It is clear that, at the very
least, there is something seriously wrong in our present formulation of
this theory; but we lack clues telling us in what specific way it should
be modified.

Most recent study of these problems has tended to concentrate on the
high-energy region. However, because of technological limitations,
further high-energy experiments can only continue to give evidence on
"amplitude" aspects of the theory. In view of recent advances, it is
now possible to perform controlled experiments in the optical
region---where duplication in the high energy region would be out of the
question---which test aspects of QED on which we have as yet no direct
evidence. For these reasons, we suggest that the missing clues are as
likely to be found in the optical region as anywhere else, and so it is
important that the optical phenomena be further explored.

In Sec. 3 we develop a method of treating the problem of an atom
interacting with electromagnetic field without resorting to the usual
time-dependent perturbation theory. The solutions will retain their
phase and amplitude accuracy over long periods of time.

In Sec. 4 a number of detailed solutions are presented in which the
effect of spontaneous emission and radiative line shifts on long-time
behavior are exhibited.

In Sec. 5 we show that the method we have developed is quite general and
could be applied just as well to any problem in radiation theory.
Finally, in Sec. 6 we discuss the differences between this method and
the usual formalism. New experiments to test the detailed solutions of
Sec. 4 are proposed.
## EQUATIONS OF MOTION
Consider an atom with energy levels $E_i$ and stationary-state wave
functions $\psi_i$, 
$$
H_0 \psi_i = E_i \psi_i \tag{3.1}
$$

 In what follows
we take into account only two of these levels, between which there is a
dipole-moment matrix element $\mu$. Let $\omega$ be the natural line
frequency of this transition, and choose the zero from which we measure
the energies to be midway between the two "active" levels, so that the
energies are 
$$
E_2 = -E_1 = \frac{1}{2}\hbar\omega. \tag{3.2}
$$

 The state
vector of the atom at an arbitrary time will be some linear combination
of the active levels 
$$
\psi(t) = a(t)\psi_1 + b(t)\psi_2, \tag{3.3}
$$
 and
the Schrödinger equation 
$$
i\hbar\dot{\psi} = [H_0 - \vec{\mu} \cdot \vec{E}(t)]\psi \tag{3.4}
$$
 in
which the dipole moment interacts with an electric field E(t), then
reduces to 
$$
\begin{aligned}
    i\hbar\dot{a}(t) &= E_1a(t) - \vec{\mu} \cdot \vec{E}(t)b(t), \\\\    i\hbar\dot{b}(t) &= E_2b(t) - \vec{\mu} \cdot \vec{E}(t)a(t).
\end{aligned} \tag{3.5}
$$

 This neglect of all other levels is well
justified if we suppose that $\psi_1$ is the ground state, so it cannot
be depopulated by transitions to lower ones; and that the spectrum of the
applied field E(t) contains no appreciable component at any frequency
which could couple $\psi_1$ and $\psi_2$ resonantly to other levels.
Thus, no other levels can attain an appreciable amplitude: Their effect
can be found by perturbation theory,[^15] and amounts, for all practical
purposes, to a small effective level shift, which we suppose to have been
included already in $E_1$ and $E_2$.

We make one further assumption, that the field is linearly polarized
with its polarization parallel to the atomic dipole moment. We will
discuss more general applied fields in Sec. 4, and show that there are
no qualitative changes in our results in that case. This assumption
reduces Eq. (3.5) to scalar equations.

To better understand the physical influence of the field E(t) on the
atom, we introduce a new set of variables:
$$
M(t) = \langle \mu_{\text{op}} \rangle = \mu (a^*b+ab^*), \tag{3.6}
$$
 and
$$
W(t) = \langle H_0 \rangle_{\text{op}} = \frac{1}{2}\hbar\omega(|b|^2-|a|^2). \tag{3.7}
$$

 As a
result of Eqs. (3.5) these new variables satisfy 
$$
\begin{aligned}
    \frac{d^2}{dt^2}M + \omega^2 M &= -K^2WE(t), \\\\    \dot{W} &= \dot{M}E,
\end{aligned} \tag{3.8}
$$
 where 
$$
K = 2\mu/\hbar. \tag{3.9}
$$

 These
equations are exactly equivalent to Eqs. (3.5), but in the form (3.8) we
have a simple physical interpretation. The atomic dipole moment responds
to an applied field E(t) according to a driven harmonic-oscillator
equation, with the unique feature that the coupling constant $K^2W$ is
proportional to the slowly varying energy W of the atom, reversing sign
when W passes through zero. Thus, the dipole responds in opposite phase,
depending on whether the atom is nearer to the upper state or the lower
state. By this means, as we will presently see, the atom automatically
adjusts its phase so as to give maximal induced emission when near the
upper one. Equation (3.8b) is simply a statement of conservation of
energy. These equations were derived previously to describe maser
action.[^16]

There is one further immediate consequence of writing the equations in
this form: We have a first integral. Multiplying (3.8a) by $\dot{M}$ and
substituting (3.8b), we get after integrating
$$
\dot{M}^2 + \omega^2 M^2 + K^2W^2 = \mu^2\omega^2, \tag{3.10}
$$
 where we
determined the constant of integration by substitution of the
definitions of M(t) and W(t), and by use of the normalization
condition 
$$
|a|^2+|b|^2=1. \tag{3.11}
$$

 This first integral is of the
form of the equation of a sphere. We can take advantage of this to define
another convenient set of variables, which are just the Cartesian
coordinates of a point on the unit sphere, defined by 
$$
\begin{aligned}
    \dot{M} + i\omega M &= i\mu\omega e^{i\Omega t}(x+iy), \\\\    W &= \frac{1}{2}\hbar\omega z,
\end{aligned} \tag{3.12}
$$
 where x(t) and y(t) are real, and $\Omega$ is
the frequency of the applied field, which is supposed to be mono-
chromatic. Taking the imaginary part of (3.12a),
$$
M(t) = \mu(x\cos\Omega t - y\sin\Omega t), \tag{3.13}
$$
 we can see the
physical meaning of these Cartesian coordinates. Thus, x(t) is the
component of the dipole moment in phase with the applied field, while
y(t) is the component 90° out of phase with the applied field, if the
applied field is 
$$
E_{\text{app}} = E_0\cos\Omega t. \tag{3.14}
$$

 The
first integral (3.10) can be written in terms of these Cartesian
variables giving 
$$
x^2+y^2+z^2 = 1, \tag{3.15}
$$
 the equation of the
unit sphere. Thus, with these variables the state of the system is
specified by a point on the unit sphere, the azimuth of which determines
the relative phase of the dipole moment with respect to the applied
field, and the colatitude of which determines the energy. The upper and
lower states are mapped onto the north and south poles, respectively.
Conversely, each point on the sphere determines a particular linear
combination of states (3.3) to within a phase factor which has no
meaning. Thus, there is a 1:1 correspondence between points on the sphere
and physical states of the atom.

If we define a resonance parameter 
$$
\alpha = \Omega - \omega, \tag{3.16}
$$
 then
substitution of the ansatz (3.12) into the Eqs. (3.8) results in
$$
\begin{aligned}
    \dot{x} &= \alpha y + (2\mu/\hbar) z(t)E(t) \sin\Omega t, \\\\    \dot{y} &= -\alpha x + (2\mu/\hbar) z(t)E(t) \cos\Omega t, \\\\    \dot{z} &= -(2\mu/\hbar)(x \sin\Omega t + y \cos\Omega t) E(t).
\end{aligned} \tag{3.17}
$$

 This Cartesian form is convenient for use in
obtaining explicit analytic solutions, but for some purposes it is
convenient to express these equations in terms of the azimuth angle
$\phi$ and the colatitude angle $\theta$ on the unit sphere reducing the
system (3.17) to two coupled equations 
$$
\begin{aligned}
    \dot{\theta} &= (2\mu/\hbar) \sin[(\omega + \alpha) t + \phi(t)]E(t), \\\\    \dot{\phi} &= -\alpha + (2\mu/\hbar) \cot\theta \cos[(\omega+\alpha)t + \phi(t)] E(t).
\end{aligned} \tag{3.18}
$$

 Thus far, our results have been exactly
equivalent to the usual semiclassical radiation theory except that we
have not resorted to time-dependent perturbation theory. However, the
present theory differs from conventional treatments in that here we will
include radiation reaction in the driving field, i.e., we will take
$$
E(t) = E_{\text{ext}}(t)+E_{\text{RR}}(t), \tag{3.19}
$$
 where
$E_{\text{ext}}(t)$ is the external applied field, and $E_{\text{RR}}(t)$ is the
radiation reaction field. Many discussions of radiation reaction exist,[^16][^17][^18]
but none of the discussions seems quite appropriate for the present
case, though all arrive at the same final results. We have included in
Appendix B a derivation appropriate to our present problem. The results
of that calculation, in the dipole approximation, are that the effect of
radiation reaction on an oscillating dipole is equivalent to a field
$$
E_{\text{RR}}(t) = \frac{2}{3c^3}\frac{d^3}{dt^3}M(t) - \frac{4K}{3\pi c^3}\frac{d^2}{dt^2}M(t) \tag{3.20}
$$
 acting back on the dipole. This
expression gives the contribution for all frequencies up to the frequency
K. Above that frequency the fields will not be effective since they
correspond to wavelengths smaller than the radius of the charge
distribution. For a charge distribution with dimensions of the order of
the Bohr radius $a_0$, the cutoff is given approximately by
$$
K \approx c/a_0 = 6 \times 10^{18}/\text{sec}. \tag{3.21}
$$

 We will
discuss this point further in Sec. 5, and show how K can be
calculated from the current distribution $J(\mathbf{r}, t)$ within the
atom. Since the dipole moment to a good approximation oscillates
sinusoidally at the natural frequency, Eq. (3.20) can be approximated by
$$
E_{\text{RR}}(t) \approx -\frac{2\omega^2}{3c^3}\dot{M}(t) + \frac{4\omega^2 K}{3\pi c^3}M(t). \tag{3.22}
$$

 Then, if we assume that the
external field is given by
$$
E_{\text{ext}}(t) = E_0\cos\Omega t, \tag{3.23}
$$
 the total field
driving the dipole is
$$
E(t) = E_0 \cos\Omega t - \frac{2\omega^3}{3c^3}\dot{M}(t) + \frac{4\omega^2K}{3\pi c^3}M(t). \tag{3.24}
$$

 Substituting this back into the
differential equations (3.17) and using the ansatz (3.12), we have
$$
\begin{aligned}
\dot{x} ={} & \alpha y + (4\mu^2\omega^3/3\hbar c^3)(x \sin^2\Omega t + y \sin\Omega t \cos\Omega t)z \\\\ & + (8\omega^3 K\mu^2/3\pi\hbar c^3)(x \sin\Omega t \cos\Omega t - y \sin^2\Omega t)z \\\\ & - (2\mu/\hbar)zE_0 \sin\Omega t \cos\Omega t, \end{aligned} \tag{3.25a}
$$
$$
\begin{aligned}
\dot{y} ={} & -\alpha x + (4\mu^2\omega^3/3\hbar c^3)(x \sin\Omega t \cos\Omega t+y \cos^2\Omega t)z \\\\ & + (8\omega^3 K\mu^2/3\pi\hbar c^3)(x \cos^2\Omega t-y \sin\Omega t \cos\Omega t)z \\\\ & + (2\mu/\hbar)E_0 \cos^2\Omega t z, \end{aligned} \tag{3.25b}
$$
$$
\begin{aligned}
\dot{z} ={} & -(4\mu^2\omega^3/3\hbar c^3)(x^2 \sin^2\Omega t + y^2 \cos^2\Omega t \\\\ & + 2xy \sin\Omega t \cos\Omega t) - (8\mu^2 K\omega^3/3\pi\hbar c^3)(x^2 - y^2) \\\\ & \sin\Omega t \cos\Omega t - (2\mu/\hbar) E_0(x \sin\Omega t \cos\Omega t \\\\ & + y \cos^2\Omega t) - (8\mu^2 K\omega^3/3\pi\hbar c^3)xy \cos2\Omega t.
\end{aligned} \tag{3.25c}
$$

 These equations contain two types of terms, those which vary slowly with
time, and those which oscillate rapidly at frequency $2\Omega$. These
rapidly oscillating terms are often encountered in radiation theory; they
are known in magnetic resonance theory as the "counter-rotating"
terms and were discussed by Bloch and Siegert.[^17] There terms
oscillate so rapidly that their effect averages to zero in a half-cycle
of the dipole's oscillation. We will then neglect those terms by
averaging the equations over a time $\pi/\Omega$. The resulting
equations will be called the secular equations and will describe the
slow change of the energy and of the phase of the dipole moment. The
secular equations are 
$$
\begin{aligned}
    \dot{x} &= \alpha y + \beta xz - \gamma yz, \\\\    \dot{y} &= -\alpha x + \beta yz + \gamma xz + \lambda z, \\\\    \dot{z} &= \beta(z^2-1) - \lambda y,
\end{aligned} \tag{3.26}
$$
 where 
$$
    \begin{align}
    \lambda &= \mu E_0/\hbar, \tag{3.27} \\
    \beta &= 2\mu^2\omega^3/3\hbar c^3, \tag{3.28} \\
    \gamma &= 4K\omega^2\mu^2/3\pi\hbar c^3 \tag{3.29}
    \end{align}
$$

 The parameter $\beta$ is exactly one-half the Einstein A
coefficient; it will appear presently that $\gamma$ is related to the
Lamb shift. As a check on the accuracy of this approximation, note that
the first integral (3.15) is still an exact first integral of the secular
equations (3.26). The corresponding secular equations for the azimuth
and the colatitude are
$$
\begin{aligned}
\dot{\phi} &= -\alpha + \lambda \cos\phi \cot\theta + \gamma \cos\theta, \\\\    \dot{\theta} &= \beta\sin\theta + \lambda\sin\phi.
\end{aligned} \tag{3.30}
$$

 This formalism differs from the usual
semiclassical theory in taking the dipole moment of the atom to be an
actual oscillating charge distribution which radiates according to the
classical Maxwell equations. This radiation field then acts back on the
atomic dipole moment to cause radiation reaction. The radiation given off
by the atom undergoing spontaneous or stimulated emission will be
proportional to $\ddot{M}$, as in classical electromagnetic theory.
The predictions of this theory will not always be in exact quantitative
agreement with QED, as we will see in Sec. 4; however, the area of
agreement does seem to be remarkably wide. We will see that the two
theories seem to be in complete agreement in their description of all
experiments which have been carried out heretofore, and that they differ
only in finer details, yet to be tested experimentally. We will be
particularly interested in those cases where the results differ from the
predictions of QED. These results will, at the very least, point out
areas in which this method breaks down as an approximation technique for
QED. The method of calculation has a certain plausibility of its own
however, quite separate from QED, and may be regarded not merely as an
approximation scheme to QED, but as a physical theory in its own right;
one which we suggest as a possible alternative to QED in which the
divergence difficulties are conspicuously missing, yet one which agrees
with existing experiments. The areas in which their predictions differ
thus correspond to new experiments capable of deciding between them.
Of course, one does not expect that this alternative theory can be
correct in every respect; however, we believe it to be useful for
suggesting new experiments. If new experiments show that this
alternative theory contains just one "element of truth" that is not
contained in present QED, then we would have the essential clue telling
us in what direction QED must be modified.
## 4. SOLUTIONS OF SECULAR EQUATIONS
Solutions of the secular equations contain a great amount of detail. In
order to show clearly the nature of these solutions we treat the various
special cases first, gradually generalizing our analysis. By use of this
approach we can see the ways in which the various parameters influence
the solutions.
### A. Strong Fields
The simplest case for which we can obtain nontrivial solutions is the
strong-field case, i.e., the case in which the external applied field is
near resonance and is so strong that radiation reaction is negligible.
This corresponds to neglecting $\alpha$, $\beta$, and $\gamma$ when
compared with $\lambda$. The secular equations are then
$$
\begin{aligned}
    \dot{x} &= 0, \\\\    \dot{y} &= \lambda z, \\\\    \dot{z} &= -\lambda y.
\end{aligned} \tag{4.1}
$$

 Assuming that the atom was in its ground state
at $t=0$, the solutions are
$$
x(t)=0, \quad y(t)=-\sin\lambda t, \quad z(t)=-\cos\lambda t. \tag{4.2}
$$

 Physically this says that the atom alternately absorbs and then reemits
radiation at a rate which is directly proportional to the driving field.
This sort of behavior has been observed in microwave spectroscopy where
spontaneous emission is negligible, and is derivable from conventional
radiation theory.
### B. Pure Spontaneous Emission
The second case which we want to look at in detail is pure spontaneous
emission when the Lamb shift is negligible. In general, the Lamb shift
may be large compared to the natural line width, but in order to better
understand the qualitative effects of spontaneous emission we will
ignore the Lamb shift for the present. The secular equations in this
case are 
$$
\begin{aligned}
    \dot{x} &= \beta xz, \\\\    \dot{y} &= \beta yz, \\\\    \dot{z} &= \beta(z^2-1).
\end{aligned} \tag{4.3}
$$

 The $\dot{z}$ equation can be integrated
immediately and we get the solutions,
$$
\begin{aligned}
    x(t) &= \cos\phi_0 \text{sech}\beta(t-t_0), \\\\    y(t) &= \sin\phi_0 \text{sech}\beta(t-t_0), \\\\    z(t) &= -\tanh\beta(t-t_0).
\end{aligned} \tag{4.4}
$$

 This is spontaneous emission, but in a rather
different form from that found in QED (see Fig. 1). Note that if the atom
is exactly in the excited state, i.e., z=1, then
$\dot{x}=\dot{y}=\dot{z}=0$. The atom will remain forever in the excited
state! This is rather disconcerting until we realize that this is a
point of metastable equilibrium, so that even the very slightest
perturbation would be sufficient to cause the system to decay as given
by (4.4). In any experiment such perturbations will, of course, be
unavoidable. This differs from QED, which predicts that spontaneous
decay will begin immediately. If isolated atoms could be pumped very
close to the excited state, an experimentally observable delay should
occur before spontaneous emission begins, if this theory is correct. This
has not been confirmed or disproved by existing experiments. We will
discuss this further in Sec. 6.
**[FIGURE 1: The time dependence of the energy and of the amplitude of the dipole moment for spontaneous emission.]**
This theory predicts the proper decay constant, the Einstein A
coefficient. For long-term decay,
$$
W(t) = -\frac{1}{2}\hbar\omega\tanh\beta t \xrightarrow{t\to\infty} -\frac{1}{2}\hbar\omega(1-2e^{-At}), \tag{4.5}
$$
 where $A=2\beta$. This is exactly the QED result. These differences
between the present theory and QED are observable only when we can pump
the atom near the upper state. If the atom is excited only slightly
above the ground state, these results are identical to those found in
the conventional theory.

Another comparison can be made with the line shape predicted by the two
theories. The line shape is given by $|M(\omega)|^2$, and
$$
M(\omega) = \frac{\mu}{2\pi} \int_0^\infty e^{i\omega t} \text{sech}\beta t \cos\omega_0 t dt. \tag{4.6}
$$

 If $\Omega \gg \beta$, then
$$
|M(\omega)|^2 = (\pi\mu^2/8\beta^2)[\text{sech}^2(\pi/2\beta)(\Omega+\Omega_0) + \text{sech}^2(\pi/2\beta)(\Omega-\Omega_0)], \tag{4.7}
$$
 so the line shape is given by a hyperbolic secant squared rather than a
Lorentzian. These line-shape differences might be distinguished by a
visibility-curve measurement such as those performed by Michelson,[^18]
if we could eliminate the Doppler broadening and pump the atoms close
enough to the excited state so that the entire decay would be present in
the radiation.[^19]

Having seen this much concerning the phenomena of spontaneous emission
in the formalism, we will go on to investigate the effects of the other
terms in our equations.
### C. Spontaneous Emission with the Lamb Shift
We will now solve the general secular equations with no applied field:
$$
\begin{aligned}
    \dot{x} &= \beta xz - \gamma yz, \\\\    \dot{y} &= \beta yz + \gamma xz, \\\\    \dot{z} &= \beta(z^2-1).
\end{aligned} \tag{4.8}
$$

 The $\dot{z}$ equation is identical with that
for spontaneous emission with no Lamb shift, so we can immediately write
down the result,
$$
z(t) = \tanh\beta(t-t_0). \tag{4.9}
$$

 Rather than solving Eqs.
(4.8) for x(t) and y(t), it is better to return to the angular form
of the secular equations (3.30). Equation (3.30) becomes, in the present
case,
$$
\dot{\phi}(t) = \gamma\cos\theta = \gamma z(t) = -\gamma\tanh\beta(t-t_0). \tag{4.10}
$$

 But since
$$
|\dot{\phi}| \ll \omega, \phi \tag{4.11}
$$
 and
$$
\dot{M}+i\omega M = i\mu\omega\sin\theta e^{i[\omega t + \phi(t)]}, \tag{4.12}
$$
 we see that $\dot{\phi}(t)$ measures a frequency shift in the
oscillations of the dipole moment, and of the emitted radiation. When
the atom is near the upper state, the dipole is oscillating at frequency
$\omega+\gamma$, while it oscillates at frequency $\Omega-\gamma$ near
the lower state, thus the emitted radiation is frequency modulated! This
result again differs with QED, where the frequency of the emitted
radiation is constant.

This result is consistent with the observation that the Lamb shift seems
to raise the S levels, however. In experiments in which the transition
observed has the S level as the lower of the two levels involved, it is
observed that the transition frequency is lowered. Our theory gives that
frequency as $\Omega-\gamma$ near the lower level, which is all that
will be observed in an experiment in which incoherent radiation is
absorbed. In experiments in which the S level is the upper level, the
transition frequency is increased, which again agrees with our result,
since we get $\Omega+\gamma$ in that case. At this point it is not
obvious why we should pick out the frequency near the S level in the
second case, but it is due to many level effects which we will discuss
in Sec. 5.

For comparison with QED, we can again calculate the line shape.

Integrating (4.10), we find
$$
\phi(t) = (\gamma/\beta)\ln\text{sech}\beta(t-t_0), \tag{4.13}
$$
 which we
can substitute into Eq. (3.13) to determine M(t):
$$
M(t) = \mu\text{Re}[(\text{sech}\beta t)^{1+i\gamma/\beta} e^{i\omega_0 t}]. \tag{4.14}
$$

 The Fourier
transform is then obtained by use of the change of variables
$$
\tanh\beta t = 1-2u. \tag{4.15}
$$

 Keeping only the positive frequency
part, we have for the line shape
$$
|M(\omega)|^2 \approx \frac{\mu^2}{\beta\gamma}\sinh\frac{\pi\gamma}{\beta}\left[\cosh\frac{\pi\gamma}{\beta} + \cos\frac{\pi(\omega-\Omega_0)}{\beta}\right]^{-1}. \tag{4.16}
$$

 This line shape is
illustrated in Fig. 2. Again we might be able to test this result with a
Michelson visibility experiment if we could guarantee that the
excitation was such that we got the entire transition.
**[FIGURE 2: The line shape for spontaneous emission including the time-dependent frequency shift.]**
### D. Applied Field, No Lamb Shift
We will now investigate, in detail, the solutions when there is a
monochromatic applied field. We will first neglect the frequency shift.
In this case the secular equations are 
$$
\begin{aligned}
    \dot{x} &= \beta xz + \alpha y, \\\\    \dot{y} &= \beta yz + \lambda z - \alpha x, \\\\    \dot{z} &= \beta(z^2-1) - \lambda y.
\end{aligned} \tag{4.17}
$$

 These equations are linearized by the
following ansatz:
$$
x=f/h, \quad y=g/h, \quad z=-\dot{h}/\beta h. \tag{4.18}
$$

 With this
substitution, Eqs. (4.17) reduce to 
$$
\begin{aligned}
    \dot{f} &= \alpha g, \\\\    \dot{g} &= -(\lambda h/\beta) - \alpha f, \\\\    \ddot{h} &= \beta^2 h + \beta\lambda g.
\end{aligned} \tag{4.19}
$$

 These are linear equations which are easily
solved though the solutions for x(t), y(t), and z(t) are quite
complicated. For example, the solution for z(t) when z(0)=1 is
$$
z(t) = N(t)/D(t), \tag{4.20}
$$
 where 
$$
\begin{aligned}
    N(t) ={} & -(\alpha/\beta)[\beta(a^2+\lambda^2-\beta^2)\cos bt + b(a^2-\beta^2)\sin bt \\\\    & + \beta(\lambda^2-\beta^2-b^2)\cosh at + a(b^2+\beta^2)\sinh at]
\end{aligned} \tag{4.21}
$$
 and 
$$
\begin{aligned}
    D(t) ={} & [a(a^2-\beta^2)\cos bt - (\beta a/b)(a^2+\lambda^2-\beta^2)\sin bt \\\\    & + a(b^2+\beta^2)\cosh at - \beta(b^2+\beta^2-\lambda^2)\sinh at].
\end{aligned} \tag{4.22}
$$

 The oscillation frequency b is
$$
b = \{-\frac{1}{2}(\beta^2-\lambda^2-\alpha^2)+\frac{1}{2}[(\alpha^2+\lambda^2-\beta^2)^2+4\alpha^2\beta^2]^{1/2}\}^{1/2}, \tag{4.23}
$$
 while the damping constant a is
$$
a = \{\frac{1}{2}(\beta^2-\lambda^2-\alpha^2)+\frac{1}{2}[(\alpha^2+\lambda^2-\beta^2)^2+4\alpha^2\beta^2]^{1/2}\}^{1/2}. \tag{4.24}
$$

 The solutions for x(t) and y(t) are of the same form. While it is
impossible to understand the details of this solution by examination, we
can say at least that it is a damped nonsinusoidal oscillation with
oscillation frequency b and damping constant a. In all cases for which
$a \neq 0$ the solution will decay exponentially to a steady-state
asymptotic value. In fact, we can see
$$
\lim_{t\to\infty} z(t) = -\alpha/\beta, \tag{4.25}
$$

 To obtain a better
understanding of these rather complex analytic solutions, we will
further analyze the differential equations themselves and study some
graphical solutions obtained by use of an analog computer. Consider the
dependence of the oscillation frequency b, and the decay constants, on
the parameters $\alpha$ and $\lambda$. The spontaneous emission
parameter is a constant for a given transition. Expanding (4.24), we can
write it in the form 
$$
\lambda^2/(\beta^2-a^2) - \alpha^2/a^2 = 1. \tag{4.26}
$$

 This
is an hyperbola and has solutions only for 
$$
\alpha < \beta, \tag{4.27}
$$
 thus
the transients always die out more slowly than spontaneous emission. We
can treat (4.23) in the same way. The oscillation frequency b then
satisfies 
$$
\lambda^2/b^2 - \beta^2 + \alpha^2/b^2 = 1, \tag{4.28}
$$
 the
equation of an ellipse. These curves are illustrated in Fig. 3. Using
this graph we can read off the oscillation frequency and the damping
constant for any set of the parameters $\alpha$ and $\lambda$.
**[FIGURE 3: The decay constants and oscillation frequencies for transients after sudden turn on of the driving field.]**
Note that we have qualitatively different solutions for the case
$\alpha=0$, exact resonance. At resonance with a field strength
satisfying $\lambda<\beta$, the oscillation frequency is zero. Above the
"critical field," $\lambda > \beta$, there is no damping; the
solutions oscillate forever. This is true only for exact resonance, however.
Any slight value of $\alpha$ will cause the system to decay slowly to a
steady-state value.

We can also use the differential equations to determine the asymptotic
steady-state solutions. We obtain these solutions by requiring
$$
\begin{aligned}
    \dot{x} &= 0 = \beta xz + \alpha y, \\\\    \dot{y} &= 0 = \beta yz + \lambda z - \alpha x, \\\\    \dot{z} &= 0 = \beta(z^2-1) - \lambda y.
\end{aligned} \tag{4.29}
$$

 There are two sets of solutions, one set in the
northern hemisphere and another in the southern hemisphere. We have
already seen in (4.25) that the asymptotic solution is $z = -\alpha/\beta$,
so that the asymptotic solutions are
$$
x = -(\alpha/\lambda)[(\beta/\alpha)-(\alpha/\beta)], \tag{4.30}
$$
$$
y = -(\beta/\lambda)(1-\alpha^2/\beta^2), \tag{4.31}
$$
$$
z = -\alpha/\beta. \tag{4.32}
$$

 The point in the northern hemisphere is a point of unstable equilibrium.
Figures 4-6 show graphs of solutions for x(t), y(t), and z(t) for various
values of the parameters $\alpha$ and $\lambda$. These graphs were
obtained by solving the differential equations (4.17) directly with an
analog computer.
**[FIGURE 4: Solutions of the secular equations for α = γ = 0 and λ = 0.99β.]**
**[FIGURE 5: Solutions of the secular equations for α < 0.01β, λ = 1.01β, and γ = 0.]**
**[FIGURE 6: Solutions of the secular equations for strong applied field off resonance, γ = 0, α = β, and λ = 3β.]**
### E. Strong Field with Lamb Shift
We have already seen that the effect of the Lamb shift is to cause the
frequency of the atomic transition to be raised when the atom is near the
upper state, and lowered when the atom is near the lower state. We would
expect such a frequency shift to cause effects which are evident with
fields so strong that spontaneous emission can be neglected. In this case
the secular equations become 
$$
\begin{aligned}
    \dot{x} &= \gamma y z, \\\\    \dot{y} &= \gamma x z + \lambda z, \\\\    \dot{z} &= -\lambda y,
\end{aligned} \tag{4.33}
$$
 where we have assumed the applied field to be
resonant with the unshifted transition frequency. There is an immediate
first integral by eliminating z between the $\dot{x}$ and $\dot{y}$
equations. If we assume x(0)=y(0)=0, the integral is
$$
(x+\lambda/\gamma)^2+y^2 = (\lambda/\gamma)^2. \tag{4.34}
$$

 This says
that the projection of the system point orbit in the xy plane is a circle
with its center at $x = -\lambda/\gamma$, y=0 and radius of
$\lambda/\gamma$. This orbit lies entirely on the sphere only if
$\lambda<\gamma$. By use of the equation of the sphere (3.15), we can
determine the other two projections of the orbit. The xz projection is
an hyperbola, but the yz projection is a quartic, an ellipse in terms of
y and $z^2$. These projections are shown in Fig. 7 for various values of
the applied field strength. We can actually obtain an analytic solution
for x(t), y(t), and z(t) in this case. Combining the first integral with
the $\dot{z}$ equation (4.33c), we have an equation in the form for
solution in terms of elliptic functions. From the tables[^20] we have
$$
z(t) = -\text{cn}(\lambda t|\gamma/2\lambda), \quad \gamma > \frac{1}{2}\gamma. \tag{4.35}
$$

 By use of the Eqs. (4.33) and the identities for elliptic functions, we
can determine the corresponding solutions for x(t) and y(t):
$$
\begin{aligned}
    x(t) &= -(\gamma/2\lambda)\text{sn}^2(\lambda t|\gamma/2\lambda), \\\\    y(t) &= \text{sn}(\lambda t|\gamma/2\lambda)\text{dn}(\lambda t|\gamma/2\lambda).
\end{aligned} \tag{4.36}
$$

 In the region $\lambda < \frac{1}{2}\gamma$ the
solutions are 
$$
\begin{aligned}
    x(t) &= -(2\lambda/\gamma)\text{sn}^2(\frac{1}{2}\gamma t|2\lambda/\gamma), \\\\    y(t) &= (2\lambda/\gamma)\text{sn}(\frac{1}{2}\gamma t|2\lambda/\gamma)\text{cn}(\frac{1}{2}\gamma t|2\lambda/\gamma), \\\\    z(t) &= -\text{dn}(\frac{1}{2}\gamma t|2\lambda/\gamma).
\end{aligned} \tag{4.37}
$$

 A typical case is illustrated in Fig. 8. In the
limit of a strong field, i.e., $\lambda\gg\gamma$, the solutions reduce
to those given in (4.2) as expected, i.e.,
$$
\lim_{\lambda\to\infty} z(t) = \text{cn}(\lambda t|0) = -\cos\lambda t. \tag{4.38}
$$

 The solution is also simple in the case $\lambda=\frac{1}{2}\gamma$ when
we have
$$
z(t) = -\text{cn}(\frac{1}{2}\gamma t|1) = -\text{sech}\frac{1}{2}\gamma t, \quad \lambda=\frac{1}{2}\gamma. \tag{4.39}
$$

 This last case is the only nonoscillatory solution to Eqs. (4.33); we
must in general include spontaneous emission before we get damping or
steady-state solutions.
**[FIGURE 7: The system-point orbits for α = β = 0, various λ/γ.]**
**[FIGURE 8: Solutions of the secular equations for α = β = 0, and λ < 1/2γ.]**
We can obtain analytic solutions also for the case in which the applied
field is off-resonance. In this case the secular equations are
$$
\begin{aligned}
    \dot{x} &= -\gamma yz + \alpha y, \\\\    \dot{y} &= \gamma xz + \lambda z - \alpha x, \\\\    \dot{z} &= -\lambda y.
\end{aligned} \tag{4.40}
$$

 Again there is a first integral which gives a
projection of the system point orbit
$$
2\lambda x/\gamma + (1+\alpha/\gamma)^2 = (z-\alpha/\gamma)^2; \tag{4.41}
$$
 the
other two projections can be obtained as before. These orbits have been
graphed for various values of $\alpha$, and $\lambda=\frac{1}{2}\gamma$.[^21] There is an
asymmetry between positive and negative values of $\alpha$. This is
because a field with its frequency such that $\alpha = -\gamma$ will be at
resonance with the shifted frequency when the atom is in its ground state,
while a field with its frequency such that $\alpha = \gamma$ will be at
resonance when the atom is in the excited state.

Substituting Eq. (4.41) into the z equation (4.40c), we get a
differential equation which is again in the form for solution by
elliptic functions. The solution is too complicated to be of much value, so
we will rely on the analog solutions, even though we could obtain an
exact analytic solution.
### F. General Solutions
We have thus far been unable to obtain analytic solutions to the secular
equation in the most general case. By use of the analog computer we have
been able to obtain graphical solutions, however; those are shown in
Figs. 9-11. For the case of exact resonance, $\alpha=0$, we are able to
reduce the secular equations to quadrature, though we are unable to
perform the resulting integral.[^22]
**[FIGURE 9: Solutions of the general secular equations at resonance with a weak applied field, α = 0, β = 0.1γ, and λ = 1/2γ.]**
**[FIGURE 10: The system-point orbits for α = 0, β = 0.1γ, and λ = 1/2γ.]**
There are several things we can learn about these general solutions. The
analog plots seem to indicate that for $\alpha=0$, the critical field is
$\lambda_c \approx \frac{1}{2}\gamma$. Above this field, the solutions
are oscillatory and there seems to be no damping. Below this field, the
solutions are damped to their steady-state values in times long compared
with $(\beta)^{-1}$. We can determine the steady-state values. At
resonance the condition for steady-state solutions is 
$$
\begin{aligned}
    0 = \dot{x} &= \beta xz - \gamma yz, \\\\    0 = \dot{y} &= \beta yz + \gamma xz + \lambda z, \\\\    0 = \dot{z} &= \beta(z^2-1) - \lambda y.
\end{aligned} \tag{4.42}
$$

 The solutions are 
$$
\begin{gathered}
    x_\infty = -\gamma\lambda/(\gamma^2+\beta^2), \\\\    y_\infty = -\beta\lambda/(\gamma^2+\beta^2), \\\\    z_\infty = -[1-\lambda^2/(\gamma^2+\beta^2)]^{1/2}.
\end{gathered} \tag{4.43}
$$
**[FIGURE 11: Solutions of the general secular equations with a strong applied field, α = 0, β = 0.1γ, and λ > γ.]**
## 5. GENERAL FORMALISM
The formalism which we have developed and applied in Secs. 3 and 4 uses
an interpretation of quantum mechanics that differs from the Copenhagen
interpretation which is normally used. When the dipole moment of the
atom is taken to be the actual charge distribution which gives off the
atomic radiation, we are using the "Schrödinger interpretation."

Schrödinger proposed in 1926 that the quantities 
$$
\begin{aligned}
    \rho &= e|\Psi(\mathbf{r},t)|^2 \\\\    \text{and } \mathbf{J} &= (e/m)\text{Re}(\Psi^*\mathbf{P}\Psi),
\end{aligned} \tag{5.1}
$$
 where e is the electronic charge, $\psi$ is the
atomic wave function, and P is the momentum operator, be interpreted as
the actual electric charge density and current density associated with
the atom.[^3] By about 1930, this interpretation was superseded by the
present interpretation. The reasons for dropping Schrödinger's
interpretation are not altogether clear, though some are known.

One objection raised against this interpretation is that in the case of
more than one particle, the charge distribution, as defined in Eqs.
(5.1), is not defined in ordinary 3-dimensional space for an N-electron
system, since the wave function for such a system is a function of the
3N components of the coordinates of the N particles. The charge
distribution defined in (5.1) is only for a one-electron system, however,
and is not generalized to a N-electron system by simply replacing
$\Psi(\mathbf{r},t)$ by $\psi(\mathbf{r}_1, \mathbf{r}_2, \dots, \mathbf{r}_N, t)$. Instead the
charge density of the N-particle system is given as the sum of the
charge densities of the individual particles. The charge density due to
electron number 1 in such a system would be
$$
\rho_1(\mathbf{r},t) = e \int |\Psi(\mathbf{r}, \mathbf{r}_2, \mathbf{r}_3, \dots, \mathbf{r}_N, t)|^2 \times d^3r_2 d^3r_3 \cdots d^3r_N, \tag{5.2}
$$
 for electron 2,
$$
\rho_2(\mathbf{r},t) = e \int |\Psi(\mathbf{r}_1, \mathbf{r}, \mathbf{r}_3, \dots, \mathbf{r}_N, t)|^2 \times d^3r_3 d^3r_4 \cdots d^3r_N, d^3r_1 \tag{5.3}
$$
 etc.; and the total charge density for the N-electron system would be
$$
\rho(\mathbf{r},t) = \sum_{i=0}^N \rho_i(\mathbf{r},t). \tag{5.4}
$$

 Likewise, the contribution to the current from the first electron would be
$$
\mathbf{J}_1(\mathbf{r},t) = (e/m)\text{Re} \int \Psi^*(\mathbf{r}, \mathbf{r}_2, \dots, t) \times \mathbf{P}_1 \Psi(\mathbf{r}, \mathbf{r}_2, \dots, t)d^3r_2 \cdots d^3r_N \tag{5.5}
$$
 and similarly for all of the other electrons so that the total current
would be
$$
\mathbf{J}(\mathbf{r},t) = \sum_{i=0}^N \mathbf{J}_i(\mathbf{r},t). \tag{5.6}
$$

 These quantities represent a
generalization of the quantities defined in (5.1) which are defined in
ordinary 3-dimensional space. It is also easily shown that as a result of
the N-particle Schrödinger equation they satisfy the usual continuity
relation,
$$
\nabla\cdot\mathbf{J} + \frac{1}{c}\frac{\partial\rho}{\partial t} = 0. \tag{5.7}
$$

 Another argument often heard is that this and all other semiclassical
theories are incapable of predicting spontaneous emission and the Lamb
shift. We have seen in Secs. 3 and 4 that such is not the case; we have in
fact described just those phenomena as well as other distinctly
"quantum" phenomena.

There is one argument which is not entirely answered at this point. The
usual quantum-mechanical solution for the free-electron problem predicts
a spreading wave packet, thus according to the interpretation (5.1), we
would have a solution for the free electron which is not stable, but
spreads indefinitely over all space. This is not really a correct
description of an electron according to this formalism, however. An
electron is charged and thus has an associated field which reacts back on
the electron. We must solve the problem of the electron interacting with
its own field. It is possible for such a charge distribution to be bound
and nonradiating. Bohm and Weinstein[^23] have described such charge
distributions and have shown that in fact the condition that they be
bound is exactly the condition that they be nonradiating. Clearly, any
description of the free electron must necessarily include spin and thus
use the Dirac equation for the electron. This causes no essential
difficulty since the Eqs. (5.1) are easily generalized for the Dirac
equation. The resulting equations remain to be solved, but the essential
point is that this interpretation cannot be rejected due to this
argument until this problem is solved.

The secular equations (3.26) were derived using this Schrödinger
interpretation, but only in the dipole approximation, for linearly
polarized applied fields, and a "two-level atom." These restrictions
and approximations are not necessary but are made only to simplify the
analysis so that analytic solutions can be obtained. More complicated
cases have been treated. The treatment of applied fields with general
polarization is straightforward and has been carried out.[^24] The result
is that the energy and magnitude of the dipole moment have the same time
dependence as in the linearly polarized case. The problem has also been
treated without the dipole approximation, actually using (5.1) to
describe the oscillating charge distribution.[^24] The result is that the
equations reduce to exactly those we derived in Sec. 3, except that a
definite numerical value is obtained for the constant $\gamma$ of Eq.
(3.29), the Lamb shift. This constant which diverges in the point dipole
approximation converges nicely for the charge distribution (5.1), which
is spread over the entire atom. The numerical value of this constant has
been compared with the Lamb-shift experiments and found to agree within
experimental error.[^24] Finally, the extension to n levels has been
carried out.[^24] The equations in that case are somewhat more complex,
but can be seen to yield the familiar cascade of "photons" as an
electron descends from a higher excited state through successive lower
states to the ground state. When only a few levels are involved in the
transition, the problem is easily solved with an analog computer, as we
did in Sec. 4.

One other case in which we can easily obtain solutions is the case in
which the applied field is not cw but pulsed or amplitude modulated. If
the amplitude of the applied field varies slowly compared with the
spontaneous emission time $(\beta)^{-1}$, then the atom will remain in its
steady state [(4.43) or (4.32)]. The steady state slowly changes according
to the value of $\lambda=\lambda(t)$:
$$
\lambda(t) = \mu E_0(t)/\hbar, \tag{5.8}
$$
 where $E_0(t)$ is the slowly
varying amplitude of the applied field. If the field is very strong, i.e.,
$\lambda \gg \beta$ and $\lambda \gg \gamma$, then yet another solution
can be obtained for an important special case. If the field is of the form
$$
E_{\text{ext}}(t) = E_0\text{sech}(\mu E_0 t/\hbar)\cos\omega t, \tag{5.9}
$$
 then the
secular equations can be written as 
$$
\dot{x}=0, \tag{5.10a}
$$
$$
\begin{aligned}
    \dot{y} &= \lambda(t)z, \\\\    \dot{z} &= -\lambda(t)y, \\\\    \lambda(t) &= \lambda_0\text{sech}\lambda_0 t,
\end{aligned} \tag{5.10b}
$$
 where $\lambda_0 = \mu E_0/\hbar$. These are easily
solved to obtain
$$
z(t) = \pm\tanh\lambda_0 t, \quad y(t) = \mp\text{sech}\lambda_0 t. \tag{5.11}
$$

 This is the hyperbolic secant which was seen experimentally by Hahn and
McCall.[^26] This is the one pulse shape which is preserved on absorption
and reemission.

Other types of coherent excitation are easily described by analog
computation.
## 6. COMPARISON WITH QED EXPERIMENTAL TESTS
We have described a method for doing calculations in quantum radiation
theory. In Sec. 4 we have described rather complex phenomena in a
mathematically simple and intuitively appealing way. In Sec. 5 we have
shown that the method is quite general and capable of treating a wide
range of problems. If we use the Dirac equation for calculating the
current, we can treat relativistic problems by this formalism. A great
many calculations, for example, the Klein-Nishina formula, are normally
calculated semiclassically and thus have already been described by a
variant of this formalism. Even such "far out" phenomena as light-light
scattering can be described semiclassically using the Dirac current.
The method which we have described is not identical with QED. In fact,
the two theories disagree in their predictions of some phenomena. These
disagreements are, however, always in fine details which have not yet
been tested by experiment. Some of these fine details would seem to be
subject to experiment with existing technology. These experiments are
interesting not only as a test of the semiclassical theory but as a test
of QED. Even if this semiclassical formalism does not turn out to be the
ultimate correct theory it might well point out an experiment in which
QED fails. In that case we will have a vital clue as to how QED should be
modified.

There are several possible types of experiments which are suggested by
the calculations of Sec. 4. The most obvious seems to be the line shape
which under certain experimental conditions can differ greatly from the
Lorentzian predicted by the Wigner-Weisskopf theory. Let us go into a
possible experiment of this type in a little detail. Of course, Doppler
broadening and various types of homogeneous broadening in a solid make it
difficult to do any sort of natural line-shape experiment in a gas or
solid. These difficulties could be overcome by using an atomic beam. If a
beam of our "two-level atoms" passed through a region of coherent
illumination at the proper velocity so that they received a $\pi$ pulse
of the radiation in traversing the illuminated region, then the atoms
would emerge with the proper initial conditions so that their subsequent
spontaneous decay pulse should have a line shape like that given in Fig.
2. The width of the line would be twice the Lamb shift of the given
transition unless the Lamb shift happened to be small for the particular
transition, in which case the line width would be just that given by the
usual theory but the line shape would be a hyperbolic secant rather than
the Lorentzian (see Fig. 1). There seems to be no reason in principle why
the experiment could not be carried out this way, the main difficulty
would be obtaining a suitable two-level atom and an accompanying coherent
source which can deliver a $\pi$ pulse.

An interesting point concerning this experiment is that QED does not
predict exactly a Lorentzian line shape for a spontaneous decay; the
Lorentzian line shape is a result of the Wigner-Weisskopf approximation.
We have solved the problem of spontaneous decay using QED without
time-dependent perturbation theory in order to investigate this
problem.[^24] The method used was similar to that given by Kroll.[^25] We
found that, indeed, spontaneous decay is not exponential for long times,
but rather the amplitude of the upper state falls off as $t^{-2}$
eventually. This correction term is extremely small, about one part in
$10^6$, so that for all practical purposes, the decay is over before the
correction is appreciable compared with the exponentially decaying term.
Thus, as far as any feasible experiment is concerned, QED predicts a
Lorentzian line shape.

As we pointed out in Sec. 4, this $\pi$ pulse is extremely important in
any experiment which can hope to find these effects. If the atoms are
excited by an ordinary incoherent source, they will remain near the
ground state and only the exponential tail which agrees with QED will be
observed. If we are able to prepare good enough $\pi$ pulses, another
type of experiment becomes feasible. The formalism predicts a
metastability of the system in the excited state, thus there should be a
delay before the decay takes place if we prepare the system sufficiently
near the excited state. The necessary preparation is quite exacting, however,
as we must get the atom in a state with z(0)>0.94 in order to
double the decay time, and with z(0)>0.9999 in order to get five times
the decay time.

The very detailed solutions presented in Sec. 4 offer all sorts of
additional possibilities for experiments. Their description of the
nonlinear interference which occurs when spontaneous and stimulated
emission occur simultaneously is especially interesting. It suggests that
we might do some experiments observing the interference between an
applied field and the stimulated field which it generates in resonant
scattering. Definite asymptotic phase relations are predicted in Eq.
(4.42) for this problem. The corresponding QED calculations do not seem
to have been carried out at this point.

These few examples illustrate the sort of possibilities which exist. It
is hoped that the detailed solutions of Sec. 4 will suggest other
possibilities perhaps simpler and more direct than those suggested
above.
## ACKNOWLEDGMENTS
Part of this work was carried out while one of us was a National Science
Foundation Graduate Fellow. The analog computations were carried out on
the Washington University Computing facilities supported by NSF Grant
G-222 96. Finally, we would like to thank Centre College, Danville, Ky.,
for the use of their facilities during part of the preparation of this
manuscript for publication.
## APPENDIX A: TYPICAL VALUES OF RADIATION PARAMETERS
The following table gives the values of the radiation parameters for two
special cases: (i) the 1S-2P transition in hydrogen, and (ii) the sodium
D lines. The values are theoretically derived in the case of hydrogen, but
in the case of sodium we are unable to locate reliable theoretical
estimates of these parameters, so that we must rely on experimental
measurements of the lifetime of the P states to determine the
spontaneous emission parameter and thus the dipole moment. The value for
the Lamb shift is based on the known dependence of the Lamb shift on its
parameters. This value of the Lamb shift is only meant as an order of
magnitude estimate. The critical fields $E_\beta$ and $E_\gamma$ are the
fields at which the stimulated processes are able to overcome spontaneous
emission and the radiative shift, respectively. The $P_\gamma$ is just the
power in a plane wave with the electric field $E_\gamma$.
**[TABLE: Typical values of the radiation parameters.]**
## APPENDIX B: RADIATION REACTION
The radiation problem in which we are interested is an oscillating
dipole whose radiation field reacts back on the dipole changing its
motion. We will solve this problem using Green's function. The results
of this calculation are the same as those found elsewhere by other
methods.[^17] It is convenient for this discussion to consider our system
to be contained in a volume V with a closed surface S. We will define a
set of normal field modes by the equations,[^27]
$$
\nabla \times (\nabla \times \mathbf{E}_a) - k_a^2\mathbf{E}_a = 0, \quad \text{in V} \tag{B.1}
$$
 and
$$
\hat{n}\times\mathbf{E}_a=0, \quad \text{on S}, \tag{B.2}
$$
 where $\hat{n}$ is the
inward normal to S. The $\mathbf{E}_a(\mathbf{r})$ are normalized so that
$$
\int_V \mathbf{E}_a \cdot \mathbf{E}_b dV = \delta_{ab}. \tag{B.3}
$$

 A related set of
functions $\mathbf{H}_a(\mathbf{r})$ is defined by
$$
\nabla \times \mathbf{E}_a = k_a \mathbf{H}_a, \quad \nabla \times \mathbf{H}_a = k_a \mathbf{E}_a. \tag{B.4}
$$

 The electric and magnetic fields can be expanded in terms of these
eigenfunctions,
$$
\begin{aligned}
    \mathbf{E}(\mathbf{r},t) &= -2\sqrt{\pi} \sum_a p_a(t)\mathbf{E}_a(\mathbf{r}), \\\\    \mathbf{H}(\mathbf{r},t) &= 2\sqrt{\pi} \sum_a \Omega_a q_a(t)\mathbf{H}_a(\mathbf{r}).
\end{aligned} \tag{B.5}
$$

 Substituting these expansions into Maxwell's
equations, we find 
$$
\dot{p}_a + \Omega_a q_a = J_a(t), \tag{B.6}
$$
 where
$$
J_a(t) = 2c\sqrt{\pi} \int d^3r \mathbf{J}(\mathbf{r},t) \cdot \mathbf{E}_a(\mathbf{r}) \tag{B.7}
$$
 and 
$$
\Omega_a = k_a c. \tag{B.8}
$$

 Combining these Eqs. (B.6), we have
$$
\ddot{p}_a + \Omega_a^2 p_a = \dot{J}_a. \tag{B.9}
$$

Now if our current is due to an oscillating dipole
$$
\mathbf{J}(\mathbf{r},t) = (1/c)\dot{\mathbf{P}}(\mathbf{r},t), \tag{B.10}
$$
 where $\mathbf{P}(\mathbf{r},t)$ is the polarization,
$$
\dot{j}_a(t) = 2\sqrt{\pi c} \int d^3r \dot{\mathbf{P}}(\mathbf{r},t)\cdot\mathbf{E}_a(\mathbf{r}), \tag{B.11}
$$
 which reduces, for a point dipole at the origin, to
$$
\dot{j}_a(t) = 2\sqrt{\pi c} \mathbf{E}_a(0)\cdot\dot{\mathbf{M}}(t). \tag{B.12}
$$

 The amplitude $p_a(t)$ then satisfies
$$
\ddot{p}_a + \Omega_a^2 p_a = 2\sqrt{\pi c} \mathbf{E}_a(0)\cdot\ddot{\mathbf{M}}(t). \tag{B.13}
$$

 The solution for the amplitude can be written down immediately:
$$
p_a(t) = \frac{2\sqrt{\pi c}}{\Omega_a} \int_{-\infty}^t dt^\prime [\mathbf{E}_a(0)\cdot\ddot{\mathbf{M}}(t^\prime)] \sin\Omega_a(t-t^\prime), \tag{B.14}
$$
 where we have dropped the homogeneous solutions which correspond to
external applied fields. The electric field is then given by
$$
\mathbf{E}(\mathbf{r},t) = -4\pi\sum_a \frac{\mathbf{E}_a(\mathbf{r})}{\Omega_a} \int_{-\infty}^t dt^\prime \sin\Omega_a(t-t^\prime) \mathbf{E}_a(0)\cdot\ddot{\mathbf{M}}(t^\prime) = \int_{-\infty}^t \mathbf{G}(\mathbf{r},t;0,t^\prime)\ddot{\mathbf{M}}(t^\prime)dt^\prime. \tag{B.15}
$$

 We need for our purposes only the component of the field which is
parallel to the dipole, and only its value at the position of the
dipole: Thus, we need calculate only
$$
G_{xx}(0,t;0,t^\prime) = -4\pi\sum_a \frac{E_{ax}^2(0)}{\Omega_a}\sin\Omega_a(t-t^\prime). \tag{B.16}
$$

 In order to carry out this sum we go to the continuum limit by letting
the cavity dimensions become very large. In addition, we impose a
high-frequency cutoff which is necessary only because of our dipole
approximation. Our results would be perfectly convergent if we used the
finite charge distribution $\rho=e\psi^*\psi$ rather than our dipole
approximation. In fact, Crisp has carried out that calculation and found
it to give results identical to ours, except that it determines the
value of the cutoff parameter.[^24] In that case
$$
G_{xx}(0,t;0,t^\prime) = -\frac{4V}{c^3\pi} \int_0^K d\Omega \Omega \langle E_{ax}^2(0) \rangle_{\text{av}} \sin\Omega(t-t^\prime), \tag{B.17}
$$
 where K is the cutoff, which will be left unspecified. In our
Schrödinger interpretation, we expect the charge distribution to be
spread over a volume with a radius $a_0$, the Bohr radius. Any radiation
with wavelength shorter than this will not have appreciable effect on the
charge distribution, so we must use a cutoff if we are to use a dipole
approximation. The conventional Lamb shift derivation uses a cutoff at a
wavelength of the Compton radius, and nothing that we do here will be
affected by the value we choose for the cutoff. The value of $\langle E_{ax}^2(0) \rangle_{\text{av}}$, the average taken over the
field modes, is
$$
\langle E_{ax}^2(0) \rangle_{\text{av}} = \frac{1}{3} \langle E_a^2(0) \rangle_{\text{av}} = 1/3V. \tag{B.18}
$$

 Thus, we have
$$
G_{xx}(0,t;0,t^\prime) = -\frac{4}{3\pi c^3} \int_0^K d\Omega \, \Omega \sin\Omega(t-t^\prime) = \frac{4}{3\pi c^3} \frac{\partial}{\partial t} \left(\frac{\sin K(t-t^\prime )}{t-t^\prime}\right), \tag{B.19}
$$
 which gives, for $E_x(0,t)$,
$$
E_x(0,t) = \frac{4K}{3\pi c^3} \int_{-\infty}^t dt^\prime \ddot{M}(t^\prime) \frac{\partial}{\partial t}\left(\frac{\sin K(t-t^\prime)}{(t-t^\prime)^2}\right). \tag{B.20}
$$

 Writing the derivative in terms of t' we can carry out an integration
by parts
$$
E_x(0,t) = -\frac{4K}{3\pi c^3} \ddot{M}(t) + \frac{4}{3\pi c^3} \int_{-\infty}^t dt^\prime \frac{\sin K(t-t^\prime)}{t-t^\prime} \frac{d^3}{dt'^3} M(t^\prime). \tag{B.21}
$$

 Now if we change to a new variable defined by y=K(t-t') the integral
becomes
$$
\int_0^\infty dy M(t-y/K) \frac{\sin y}{y} \frac{d^3}{dy^3} \to \frac{\pi}{2} \frac{d^3}{dt^3} M(t), \quad \text{as } K\to\infty. \tag{B.22}
$$

 Thus, the reaction field acting on the dipole is
$$
E_x(0,t) = \frac{2}{3c^3}\frac{d^3}{dt^3}M(t) - \frac{4K}{3\pi c^3}\frac{d^2}{dt^2}M(t). \tag{B.23}
$$

 This is exactly the expression we use in Eq. (3.20).
## FOOTNOTES
[^1]: Based in part on a thesis submitted in partial fulfillment of the requirements for the degree of Doctor of Philosophy at Washington University.
[^2]: A. Einstein, Z. Physik **18**, 121 (1917).
[^3]: E. Schrödinger, Ann. Physik **80**, 437 (1926).
[^4]: P. A. M. Dirac, Proc. Roy. Soc. (London) **A114**, 243 (1927).
[^5]: V. F. Weisskopf and E. Wigner Z. Physik **63**, 54 (1930).
[^6]: W. E. Lamb, Jr., Phys. Rev. **85**, 259 (1952).
[^7]: W. E. Lamb, Jr., and R. C. Retherford, Phys. Rev. **79**, 549 (1950); **81**, 222 (1951).
[^8]: M. Skinner and W. E. Lamb, Jr., Phys. Rev. **75**, 1325 (1949); **78**, 539 (1950).
[^9]: L. R. Wilcox and W. E. Lamb, Jr., Phys. Rev. **119**, 1915 (1960).
[^10]: R. T. Robiscoe and B. L. Cosens, Phys. Rev. Letters **17**, 69 (1960).
[^11]: A. S. Wightman, 1964 Cargese Lectures in Theoretical Physics, edited by M. Levy (Gordon and Breach, Science Publishers, Inc., New York, 1968).
[^12]: N. N. Bogoliubov and D. V. Shirkov, Introduction to the Theory of Quantized Fields (Wiley-Interscience, Inc., New York, 1959), Appendix I.
[^13]: J. D. Bjorken and S. D. Drell, Relativistic Quantum Mechanics (McGraw-Hill Book Co., New York,), pp. 153-161.
[^14]: P. A. M. Dirac, Lectures on Quantum Field Theory (Belfer Graduate School of Science, Yeshiva University, New York, 1966), p. v.
[^15]: C. Bates, thesis, Washington University, St. Louis, 1967 (unpublished).
[^16]: E. T. Jaynes and F. W. Cummings, Proc. IEEE **51**, 89 (1963).
[^17]: F. Bloch and A. Siegert, Phys. Rev. **57**, 552 (1940).
[^18]: A. Michelson, Phil. Mag. **V34**, 280 (1892).
[^19]: This hyperbolic secant line shape has been derived previously in other related cases. See R. H. Dicke, Phys. Rev. **93**, 104 (1954); S. L. McCall and E. L. Hahn, Phys. Rev. Letters **18**, 908 (1967).
[^20]: P. F. Byrd and M. D. Friedman, Handbook of Elliptic Integrals for Engineers and Physicists (Springer-Verlag, Berlin, 1954).
[^21]: These graphs, as well as several others giving solutions of the secular equations for various special cases, are given in C. Stroud, thesis, Washington University, St. Louis, 1969 (unpublished). Copies are available through University Microfilms, Ann Arbor, Mich.
[^22]: C. Stroud, thesis, Washington University, St. Louis, 1969 (unpublished), Eq. (3.48).
[^23]: D. Bohm and M. Weinstein, Phys. Rev. **74**, 1789 (1948).
[^24]: M. Crisp and E. T. Jaynes, Phys. Rev. **179**, 1253 (1969).
[^25]: N. Kroll, Quantum Optics and Electronics, edited by C. DeWitt and C. Cohen-Tannoudji (Gordon and Breach, Science Publishers, Inc., New York, 1965).
[^26]: S. L. McCall and E. L. Hahn, Phys. Rev. Letters **18**, 902, (1967).
[^27]: This field expansion was introduced by J. C. Slater, Microwave Electronics (D. Van Nostrand, Inc., New York, 1950).