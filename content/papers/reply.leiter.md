---
title: "Comment on the Characteristic Time of Spontaneous Decay in Jaynes's Semiclassical Radiation Theory"
author: ["Darryl Leiter", "E.T. Jaynes"]
year: 1970
abstract: >
  We examine the implication in the fact that, in a semiclassical theory
  of atomic structure proposed by Jaynes and Crisp, the initial state of
  an atom plays a critical role in determining its average lifetime in
  an excited state.
---
In a recent publication,[^2] Jaynes and Crisp have studied the behavior of atoms
within the framework of a semiclassical theory, which includes the effects upon
the atom of the fields created by the atomic currents. They state that, in the
absence of an applied field, an atom will spontaneously decay from an excited
state with a characteristic time which is equal to the reciprocal of the
Einstein A coefficient for the transition. The purpose of this note is to point
out that statement is not entirely precise.

To see this we note that the solution to the nonlinear density-matrix equation,
for the diagonal matrix elements in a two-level decay, in a spontaneous
transition with no applied fields can be written
$$
\tag{1}
\rho_{11}(t) = 1/[\exp(-A_{21}(t-t_m))+1],
$$
$$
\tag{2}
\rho_{22}(t) = [\exp(A_{21}(t-t_m))+1]^{-1},
$$
 where
$\rho_{11}(t) + \rho_{22}(t) = 1$
$$
\tag{3}
\text{and } t_m = A_{21}^{-1}[\ln(\rho_{22}(0)/\rho_{11}(0))]
$$
 is
related to the initial state of the atom at $t=0$. If we temporarily
neglect that part of the self-field which yields only a small frequency
shift, the solution for the off-diagonal elements are given by
$$
\tag{4}
\rho_{12}(t) = \rho_{21}^{*}(t)
= \frac{\rho_{12}(0)}{\rho_{22}(0)} \frac{\exp(-i\omega_{21}t+A_{21}t/2)}{\exp(A_{21}(t-t_m))+1},
$$
where $\rho_{nn}(0) = C_n^*(0)C_n(0)$ and $C_n(0)$ are the initial values of the
coefficients ($n=1,2$) in the wave-function of the atom which describes the
transition process. We first note, that the value of $t_m$ determines the point
at which the maximum atomic-dipole moment occurs [the effective-dipole moment
of the transition is proportional to $(\rho_{12}+\rho_{21})$].

In Jaynes's semiclassical theory, it is assumed that the expectation value of
the dipole moment of the atom is responsible for the radiation process. Hence,
an excited atom radiates slowly until its dipole moment grows to an appreciable
value, and then begins to radiate its energy away very rapidly. While this
characteristic behavior was duly noted by Jaynes and Crisp in their article,
the role that the value of $t_m$ (the point in time where the maximum dipole
radiation occurs) plays in determining the average lifetime of the atom was not
clarified. While it is certainly true that Eqs. (1), (2), and (4) imply that
most of the transition energy is radiated during a time interval which is
proportional to the reciprocal of the associated Einstein A coefficient
$A_{21}$, this \"characteristic energy transfer time\" is not equal to the
average lifetime of the atom.

In particular, if we define the average lifetime of the atom as that time
required for $\rho_{22}(0) = 1$, at $t=0$, to decay to $1/e$th of its initial
value, we find from Eq. (2) that
$$
\tau_2 \approx (A_{21})^{-1} \ln[(1.718)\rho_{22}(0)/\rho_{11}(0)](\text{sec}).
$$

Hence, we see that the initial values of $\rho_{22}(0)$ and $\rho_{11}(0)$
[where $\rho_{11}(0) + \rho_{22}(0) = 1$] play a critical role in determining
the atoms average lifetime, while the \"characteristic energy transfer time\"
(occurring in some interval of time $\Delta t$ about $t_m$) is essentially
independent of the atoms initial condition at $t=0$. The implication here is
that there is a need to include an additional element into the theory, one
which can account for the experimental fact that the average lifetime of an
atom is essentially independent of its preparation. One possibility is that the
presence of a \"semiclassically described\" vacuum state[^3] might produce the
required behavior when properly included in the associated nonlinear
density-matrix equations of the theory.[^4]
## Reply to Leiter's Comment {#reply-to-leiters-comment .unnumbered}
E. T. Jaynes\
*Arthur Holly Compton Laboratory of Physics, Washington University, St.
Louis, Missouri 63130*\
(Received 1 January 1970)

Leiter[^5] raises an important point which illustrates the need for more
refined experiments before we could claim to understand the dynamics of
spontaneous emission and other radiation processes. The same point was
raised by Schawlow at the 1966 Rochester Coherence Conference, and
answered in the ensuing discussion. We welcome the opportunity to
clarify matters to a wider audience.

The semiclassical or \"neoclassical\" theory (NCT) in question was
developed by the writer and his
colleagues[^6][^7][^8][^9][^10][^11] with the following
motivation. Our present quantum electrodynamics (QED) has not achieved
any satisfactory final form; it contains many important \"elements of
truth,\" but is mixed up with clear \"elements of nonsense.\" The
divergence and other difficulties indicate, that at least one of its
underlying principles must be modified; but for forty years we have
lacked experimental clues suggesting where and how this should be done,
and nobody has seen how to disentangle the truth from the nonsense.
A possible way out of this impasse is to try to construct alternative
theories in which various objectionable features of QED are eliminated
by fiat, and see whether they suggest new experiments capable of
deciding among them. If some alternative theory could be shown to
contain just one grain of truth that is not contained in present QED,
then we would have the missing clue showing how QED must be modified.
NCT automatically removes all divergences arising from field
quantization and infinite vacuum fluctuations, but retains the
conventional Schrödinger equation to describe the behavior of matter.
Although energy exchanges between field and matter then take place
continuously, there is a strong tendency for this to occur in units of
$\hbar\omega$, explained by NCT in a completely mechanistic and causal
manner as a consequence of the equations of motion for matter -- just as
Planck and Schrödinger always believed must be true.

To the best of our knowledge, NCT agrees with existing experiments in
every case where accurate calculations have been completed.[^12] But the
predictions always differ from those of QED in finer details on which we
have as yet no experimental evidence. The case of spontaneous emission
discussed by Leiter is one example of this. Considering for simplicity
only two levels, when an atom is excited (for example, by electron
impact) we have to expect that, in general, it will not be left in exactly the excited state $\phi_2$ at the moment of excitation $t=0$, but
in some linear combination $\psi(0) = a_1\phi_1 + a_2\phi_2$, where
$\phi_1$ is the ground state. In QED, we interpret $|a_2|^2$ as the
probability that the atom is excited to the upper state, and each
excited atom proceeds to radiate a spontaneous emission pulse with field
amplitude at a given point of the form
$$
\tag{1}
Ce^{-At/2} \cos(\omega t + \theta),
$$
 where $\hbar\omega = E_2 - E_1$,
and A is the Einstein A coefficient for the transition. The total energy
radiated in the pulse is $\hbar\omega$.

In NCT, the predicted spontaneous emission pulse is of the form
$$
\tag{2}
C^\prime \text{sech}[A(t-t_m)] \cos[\omega(t-t_m) + \theta],
$$
 where
$(C^\prime)^2 \propto C^2$, and $t_m$ is determined by the initial state through
Leiter's Eq. (3) with $\rho_{22}(0) = |a_2|^2$, etc. The observed pulse,
of course, consists only of the portion of this function for $t > 0$;
and so NCT predicts a spontaneous emission pulse with a truncated
hyperbolic secant envelope rather than an exponential one. Furthermore,
the total energy radiated during the pulse is
$\hbar\omega |a_2|^2 < \hbar\omega$. As Leiter notes, if $|a_2|^2$ is
near unity, there is an appreciable delay time $t_m$ before maximum
emission is reached. For example, if $|a_2|^2 = [0.9; 0.99; 0.999]$, we
find $At_m \approx [4.4; 9.2; 13.8]$, respectively. This behavior
contradicts what we have all been taught in courses on quantum theory.
The relevant question is: Does it contradict experiment?

The common methods of excitation -- whether by collision or by
absorption of radiation -- are highly inefficient, i.e., the upper state
attains an amplitude $|a_2| \ll 1$. But then $t_m$ in Eq. (2) is
negative, the cases $|a_2|^2 = [0.4; 0.1; 0.01]$ yielding
$At_m \approx [-0.81; -4.4; -9.2]$, respectively. The emitted radiation,
according to NCT, thus, consists only of the exponential tail of the
hyperbolic secant pulse, in Eq. (2); since
$\text{sech } x \approx 2e^{-x}$ for $x \gg 1$, this is of the same form
as the QED pulse, in Eq. (1) except for a smaller amplitude.

Experiments on radiation from excited atoms have, for intensity reasons,
necessarily observed only the net radiation from many atoms
simultaneously. As long as the excitation mechanism is inefficient,
$|a_2|^2 \ll 1$, these two theories would describe such experiments as
follows. QED: A very small fraction of the atoms is excited by
collision, and each one emits the full exponential pulse as in Eq. (1);
NCT: Each atom, on collision, emits an exponential pulse of the shape
given by Eq. (1), but with an amplitude proportional to the particular
value of $|a_2|$ produced in the collision.

On either theory, the total radiation emitted and its spectral
distribution are identical. QED predicts greater instantaneous intensity
fluctuations; but statistical calculations by Dr. Charles Owen and the
author show that it would not be feasible to detect this difference by
photoelectric counting experiments. Because of the much larger Doppler
broadening, even the exponential shape of the pulses is not verified in
existing experiments known to us. In principle, this could be done by
observing the fringe visibility curve of radiation emitted normal to a
well-collimated atomic beam; but even this will not distinguish among
the theories as long as the excitation is inefficient.

As Leiter suggests, we do observe that when the excitation is removed,
the net radiation from many atoms decays exponentially according to Eq.
(1). But this is just what NCT predicts for inefficient excitation; and
a more detailed analysis of the net radiation, for a given distribution
of initial states, shows that NCT predicts net exponential decay with
the proper time constant even for efficient excitation, if the
distribution of $|a_2|$ is not sharply peaked.

Evidently, experiments capable of distinguishing between these theories
would be possible if we could achieve high and accurately reproducible
excitation. For example, suppose that by a laser pulse of controlled
amplitude and duration we could pump in such a way that most of the
atoms had $|a_2|^2 \approx 0.9$. QED predicts no change in the character
of the emitted radiation, except for a greater intensity due to the
greater pumping efficiency. NCT predicts (a) a time delay before the
maximum emission is reached, which in the case of the sodium D-lines
would be of the order of 100 nsec; (b) a change in the fringe visibility
curve as we see more and more of the hyperbolic secant envelope. Such
experiments appear feasible with presently available technology.

In summary, existing optical experiments do not permit one to decide
between QED and NCT; but several new experiments capable of doing this
are now feasible, two of which were just mentioned. In any event, this
situation makes it clear that present experimental evidence does not
establish the validity of QED, to the exclusion of alternative theories,
even in the optical region.

[^1]: Present address: Physics Department, University of Windsor,
    Windsor, 11, Ontario.

[^2]: E. T. Jaynes and M. D. Crisp, Phys. Rev. **179**, 1253 (1969).
[^3]: E. A. Uehling, Phys. Rev. **48**, 55 (1935).
[^4]: Since the maximum-dipole moment occurs at $t=t_m$ in Eq. (4), the
    \"time halfwidth\" of the associated dipole radiation pulse about
    the maximum is given by
$$
\Delta t \sim 2A_{21}^{-1} \ln\left(\frac{2+\sqrt{3}}{2-\sqrt{3}}\right).
$$

    Hence the associated frequency halfwidth is
    $\Delta\omega \sim (\Delta t)^{-1} \ll A_{21}$, which is smaller
    than that predicted quantum electrodynamics.

[^5]: D. Leiter, previous paper, Phys. Rev. A **2**, 259 (1970).
[^6]: E. T. Jaynes and F. Cummings, Proc. IEEE **51**, 89 (1963).
[^7]: M. Duggan, thesis, Stanford University, 1961 (unpublished).
[^8]: J. H. Eberly, thesis, Stanford University, 1962 (unpublished).
[^9]: C. W. Bates, Jr., thesis, Washington University, 1968
    (unpublished).

[^10]: M. D. Crisp, thesis, Washington University, 1968 (unpublished);
    M. D. Crisp and E. T. Jaynes, Phys. Rev. **179**, 1253 (1969);
    **185**, 2046 (E) (1969).

[^11]: C. R. Stroud, thesis, Washington University, 1969 (unpublished);
    C. R. Stroud and E. T. Jaynes, Phys. Rev. A **1**, 106 (1970).
[^12]: The preliminary treatment of the Lamb shift in Ref. 6 is still
    based on a two-level approximation, neglecting the effect of other
    levels weakly excited during a transition. The result agreed with
    experiment in the one case (Lyman-$\alpha$ line), where this
    approximation would be expected to be good. Better calculations for
    other lines are underway.
