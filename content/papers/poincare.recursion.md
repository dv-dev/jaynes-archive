---
title: "Poincaré Recurrence Times and Statistical Mechanics"
year: 1957
abstract: >
  The theory of almost-periodic functions is applied to the problem of
  the relation, conjectured by the Ehrenfests, between Poincaré
  recurrence times and the time over which averages of phase functions
  must be taken in order to approximate their limiting values for
  infinite time. It is concluded that the necessary averaging times
  might be very much longer than the Poincaré periods. Equality of
  ensemble averages and time averages would then carry no implications
  about equality of ensemble averages and experimental values. Two
  possible ways of understanding the success of statistical mechanics
  without recourse to ergodicity are then discussed. One of these
  interpretations has implications for the theory of irreversible
  processes and the problem of condensation, which are capable of being
  tested independently.
author: ["E.T. Jaynes"]
categories: ["Quantum Mechanics & Advanced Physics"]
tags: ["Poincaré recurrence", "statistical mechanics", "ergodic theory", "almost-periodic functions", "thermodynamics", "irreversible processes", "quantum theory"]
---

## INTRODUCTION
One of the most serious objections[^1][^2][^3] to the ergodic approach in
statistical mechanics is the fact that, even if the equality of time
averages and ensemble averages were demonstrated rigorously and
universally, this result would be established only for averages over the
times which would be required for the phase point to "explore" all the
accessible regions of phase space. This time is presumably related to
the Poincaré recurrence times,[^4][^5] which are enormous compared to
the age of the universe for macroscopic systems. Recently, the
suggestion has been made[^6][^7] that this objection may be answered by
considering permutations of identical particles. The Poincaré periods
should then be divided by N! in order to obtain recurrence times for
observable quantities. This raises the question whether these "generic
recurrence times" are sufficiently short to be comparable with the
times involved in experiments, and whether averages over these times
will approximate their limiting values for infinite time.

These questions are difficult to discuss in terms of classical theory,
since phase space is not a metric space and there seems to be no
canonically invariant way of defining "closeness of approach."

Boltzmann's estimate of these times[^5] ($>10^{10^{19}}$ years) was made
by considering distances in coordinate space and momentum space
separately. Poincaré's theorem,[^4] on the other hand, involves only the
invariant element of phase volume. Since the factor N! is in a sense a
quantum effect, it appears more satisfactory to discuss these problems
in terms of quantum theory. Here the norm $|\Psi_1 - \Psi_2|$ provides
an invariant meaning to the "degree of closeness" of two states.

The classical problem concerned a completely isolated system, restricted
to a finite volume and a finite energy, therefore a finite phase volume.
The phase point of such a system must ultimately return to a
neighborhood, of arbitrarily small phase volume $\delta \Omega$, of the
initial point. We take as the corresponding quantum theory model an
isolated system of finite size, for which all elements of the density
matrix referring to energies greater than E_max are zero. The
analog of recurrence in phase space will be taken as a recurrence of the
expectation values of all observables. The problem then reduces to a
transcription of known results in the theory of almost-periodic
functions.[^8]

## ALMOST-PERIODIC FUNCTIONS
A set of real numbers $\{\tau_i\}$ is called relatively dense if there
exists a number $T$ such that every interval $t < \tau < t + T$ of length
$T$ contains at least one number of the set. A continuous function $f(t)$
is called almost periodic if for any $\epsilon > 0$ there exists a
relatively dense set of numbers $\{\tau_i\}$ such that
$|f(t + \tau_i) - f(t)| \le \epsilon$ for $-\infty < t < \infty$. The
$\tau_i$ are called translation numbers of $f(t)$ corresponding to
$\epsilon$. We denote by $T_0(\epsilon)$ an interval such that every
interval of length $T_0(\epsilon)$ contains at least one translation
number corresponding to $\epsilon$.

It may be shown[^8] that the class of almost-periodic functions is
identical with the class of functions consisting of all finite sums

$$f_N(t) = \sum_{n=1}^{N} a_n e^{i\omega_n t} \tag{2.1}$$

when "closed" by the
addition of all functions f(t) which can be uniformly approximated by
the f_N: $|f(t) - f_N(t)| \le \epsilon$ for all $t$. In (2.1) the
$a_n$ are arbitrary complex numbers and the $\omega_n$ are arbitrary
real numbers.

In our physical problem, the density matrix at time t is given by

$$\rho_{nm}(t) = \rho_{nm}(0) e^{i\omega_{mn} t} \tag{2.2}$$

where the
stationary states are defined by $H\Psi_n = E_n\Psi_n$ and
$\hbar \omega_{mn} = E_m - E_n$. Only a finite number of the $\rho_{nm}$
are different from zero, and therefore any expectation value

$$f(t) = \langle F \rangle = \text{Tr}(\rho F) = \sum_{m,n} F_{mn} \rho_{nm}(0) e^{i\omega_{mn} t} \tag{2.3}$$

is an almost-periodic function of t. Recurrence times then correspond
to the simultaneous translation numbers of all functions of the form
(2.3).

## TIME AVERAGES
In classical theory, the statement that recurrence times are related to
the period over which time averages must be taken in order to
approximate their limiting values (henceforth called the averaging
times), seems to be only a reasonable conjecture. In quantum theory,
however, this becomes a theorem with surprising content. For every
almost-periodic function, not only does there exist a mean value

$$Mf(t) = \lim_{T\to\infty} \frac{1}{T} \int_{\alpha}^{\alpha+T} f(t) dt \tag{3.1}$$

independent of $\alpha$, but it is also true[^8] that for any
$\epsilon > 0$ we have

$$\left| Mf(t) - \frac{1}{T} \int_{0}^{T} f(t) dt \right| \le \epsilon \tag{3.2}$$

whenever

$$T \ge \frac{4}{3\epsilon} T_0(\epsilon/2) f_{\text{max}} \tag{3.3}$$

where $f_{\text{max}}$ is an upper bound of $|f(t)|$ in
$-\infty < t < \infty$. This result is surprisingly weak, since one
might expect intuitively a much stronger statement, that the average
over a translation number corresponding to $\epsilon$ would already
approximate $Mf(t)$ to the order $\epsilon$. Note, however, that
$T_0(\epsilon)$ might be very much greater than the first[^9]
translation number $\tau_1(\epsilon)$ corresponding to $\epsilon$, so
that the behavior of $f(t)$ in $0 \le t \le \tau_1$ would not provide a
"representative sample" of its behavior in all regions.[^10]

This result applies also to the classical case, if we interpret the
Poincaré recurrence theorem as implying that every phase function
F(p_i, q_i) is, by virtue of the equations of motion, an
almost-periodic function of time.

One then sees that the averaging time for F might in fact be very much
longer than the Poincaré periods. There is no guarantee that behavior
during one recurrence time with given closeness of return provides a
representative sample of behavior for all time. We conclude that no
simple relation exists between averaging times and generic recurrence
times, and consequently the averaging times should be studied on their
own merits, without reference to Poincaré periods.

For any macroscopic system the averaging time for the quantities (2.3)
will still be large. To take the simplest possible example, consider a
"system" consisting of a single hydrogen atom moving in a cubic box of
side 1 cm, and known to be in one of the two lowest energy states. The
averaging time for this case, of the order of $h/(E_2 - E_1)$, turns out
to be about 15 minutes. Every new particle added to the system, and
every new energy level taken into account, will increase this by a large
factor. When we have reached any realistic model, the averaging time
will again be enormous compared to the age of the universe. It seems
hardly worthwhile to work out a typical numerical value.

## PHYSICAL INTERPRETATION
The times involved in experiments are shorter, by perhaps 10^10
orders of magnitude, than the times required for a full exploration of
the accessible classical phase space or quantum function space. Thus
there can be no possibility of explaining the laws of thermodynamics on
the grounds that every possible microscopic condition is approximated in
succession during the time of observation. In spite of this, the
experimental fact which has to be explained is not that the average
behavior over an ensemble of similar systems follows the laws of
thermodynamics, but rather that each individual system obeys these laws.
We conclude that any explanation of the fact that ensemble averages
correspond to experimental values, must be based on other properties
than ergodicity.

It should be noted that justification of the methods of statistical
mechanics, and explanation of their success, are entirely different
problems. The former is very easy if we regard statistical mechanics as
a form of statistical inference, and show[^11] that its methods make
full use of all the available information. Whether the theory is
successful or not, one cannot do better than this. However, until we
have also explained the reasons for its success, we cannot claim to have
any real understanding of statistical mechanics.

Any attempt to do this without making use of ergodicity leads one
immediately into the deepest questions of interpretation. There are two
directions in which one can proceed, depending on whether we accept the
following assumption of realism: *Every system is, at every time, in a
single, definite microscopic state*. In classical theory one would never
question this, but in quantum theory the Einstein-Podolsky-Rosen
paradox[^12][^13] shows that it is not to be dismissed as obvious. If we
deny this assumption, we imply the possibility that an individual system
may be, in some sense which is different from that of the principle of
superposition,[^14] simultaneously in many different microscopic
states. The statement that a system has a given temperature because it
is "in a Boltzmann distribution" might then have a definite
operational meaning for a single system at a single time. If we admit
this possibility, the problem is solved in a very simple way; we assume
that interaction with a heat-bath eventually produces this condition.
There are good reasons[^15][^16] for believing this can be justified
quite generally. If all states of the system are in some sense present
simultaneously with Boltzmann weighting factors, the identification of
ensemble averages with experimental values is immediate, independently
of ergodicity or, in fact, of any property relating to evolution in
time.

It is to be emphasized that this interpretation, bizarre as it may seem,
probably cannot be refuted by logic. Furthermore, a study of the
Einstein-Podolsky-Rosen paradox will lead one to conclude that it is
quite consistent with, if not indeed required by, the present
interpretation of quantum theory. For example, the present theory allows
the possibility that the system of interest O_1 and a heat-bath O_2
which have been in interaction in the past, but are now completely
isolated from each other and from the rest of the universe, may be
jointly in a pure state 

$$\psi(1,2) = \sum_{n,m} a_{nm} u_n(1) v_m(2) \tag{4.1}$$

where u_n(1) and v_m(2) are possible state vectors of systems O_1
and O_2 respectively. This implies that system 1 is in some sense in
each of the states u_n(1), with a density matrix

$$\rho_{nk}(1) = \sum_m a_{nm} a_{km}^{*} \tag{4.2}$$

There is clearly no possibility of interpreting this density matrix as giving the relative
frequencies with which system O_1 occupies the various states
*successively*; because of coherence properties implied by (4.1) which
are in principle observable (by measurement of some joint property of
the two systems), we must conclude that there is some objective sense in
which system O_1 is in all these states *simultaneously*. Thus the
statement that an individual system is "in a Boltzmann distribution"
at a given time does not contradict the mode of description provided by
quantum theory.

In spite of this, and a certain attractiveness because of the simple way
in which this disposes of difficult problems, we prefer to retain the
assumption of realism, and to try to understand statistical mechanics on
that basis. The remainder of this paper is based on the assumption of
realism and represents what appears to the writer as the only possible
way of understanding the success of statistical mechanics which is
compatible with that assumption, and which does not make use of
ergodicity. We do not, however, attempt to answer the question whether
"microscopic state" is to be interpreted as a pure state of quantum
theory.

## MACROSCOPIC UNIFORMITY
Consider any experiment performed on a macroscopic system. It might be
anything from a nuclear induction measurement to throwing a baseball.
The initial conditions of the experiment never restrict the system to a
particular microscopic state; it could be in any one of billions of
possible states. Clearly, when we repeat the experiment we do not repeat
the initial microscopic state. If, in spite of this, the result is
reproducible, we must conclude that the *same* result would have been
obtained for *each* of the great majority of the possible initial
states. This is the *principle of macroscopic uniformity*. The
properties for which it holds true are precisely those for which
reproducible macroscopic experiments are possible.

Given the principle of macroscopic uniformity, it follows that, whether
a process in reversible or irreversible, in order to calculate any
reproducible feature of it we could choose at random any one of the
possible initial states and solve the equations of motion (for example,
the time-dependent Schrödinger equation) for it. We would get the same
results for any such state, unless we were unfortunate enough to choose,
out of all the billions of possibilities, one particular state of the
small minority for which the answer is different. *The only thing which
the use of a probability distribution over initial states accomplishes
for us is that it protects us from that danger*; in calculating the
average over many possible states, we *suppress this small minority*.
"*Almost any*" probability assignment for initial states, which gives
the correct average values for the controlled or observed parameters,
would lead to the same macroscopic predictions. The Boltzmann
distribution, besides being mathematically convenient, is the broadest
one (i.e., it has maximum entropy) for a given value of
$\langle E \rangle$; therefore it is the one which affords maximum
protection against minority states.

Because of the principle of macroscopic uniformity, the validity of
statistical mechanics as a method for predicting experimental results in
no way depends on the "correctness" of the Boltzmann distribution. It
is rather the other way around; the Boltzmann distribution or a
generalization thereof *derives its validity* as a tool for prediction
from the fact that it is consistent with the measured values of
temperature and other parameters, and it assumes nothing beyond
that.[^11] This remark carries many implications. In particular, if we
adopt the view just expressed, it becomes necessary to discuss anew the
meaning of experimentally measured temperature and entropy.

## EXPERIMENTAL TEMPERATURE AND ENTROPY
In a thermodynamic experiment, a few degrees of freedom of a system are
fixed by the experimental conditions, and a few others are observed,
while the vast majority are neither controlled nor observed. Energy
exchanged via controlled degrees of freedom is called work; energy
exchanged via uncontrolled ones is called heat. Two systems are said to
be at the same temperature if, when placed in weak interaction with each
other, the net amount of energy which they exchange over long periods of
time is small, of the order of the interaction energy. Numerical values
of temperature are defined by the relative amounts of energy which two
heat baths interchange with a third system operating in a Carnot cycle
between them. *Since these are the only criteria used in experiments to
measure temperature and heat, they must, according to the operational
view of physics, be the only ones involved in the corresponding
concepts.*

We may say that the temperature of a system is known if we can predict
correctly which one of a set of thermometers, showing different
readings, will not exchange appreciable energy with it if brought into
weak interaction. If the system is in a known microscopic state, we must
surely be in the best possible position to make this prediction. Thus,
an *operationally defined* temperature has a definite meaning *even, or
rather especially, in the case of a system in a known microscopic
state*. This is in sharp contrast to the often expressed view that the
concept of temperature requires some degree of ignorance or
"randomness." To say that a system has a given temperature because it
is "in a Boltzmann distribution," or to say, "the system has random
phases," is devoid of any meaning if we adopt the assumption of
realism.

Conventional modes of expression often suggest that experimentally
measured entropy represents the logarithm of the volume of phase space
"occupied" by a system, or its degree of "disorder." From the
present point of view, such statements also become meaningless. The
experimental entropy is constructed from observed quantities, and would
be exactly the same for any microscopic conditions which would lead to
the observed values. Thus it is not required that the system actually
"avail itself" of this full volume of phase space; very severe
constraints on the possible states could exist without in any way
affecting macroscopic observations. Suppose we have found the
experimental entropy $S(\alpha_1, \alpha_2, \ldots)$ as a function of
certain measured parameters $\alpha_i$. This entropy measures the volume
of phase space which is *compatible with the $\alpha_i$, and thus it
measures our degree of ignorance as to the true state in the case where
$\alpha_i$ provide the only available information about that state*.

There is in principle no reason why we could not obtain additional
information, on a microscopic level. Such additional information would,
of course, not alter the experimental entropy if we continue to define
it as $(S_{\text{exp}})_1 = \oint dQ/T$. It would, however, enable us to
define a new experimental entropy $(S_{\text{exp}})_2$, which embodies
this information. A method of doing this is described in reference 11.
In principle, the additional information would always make possible more
reliable predictions of the behavior of the system than are obtainable
from the equations of thermodynamics. In practice, however, it would be
found to be of very little value unless we wished to predict microscopic
details of that behavior, or unless it showed us that the system was in
a "minority state." The reason for this is to be found, again, in the
principle of macroscopic uniformity, which shows that the additional
information is usually irrelevant for macroscopic predictions. If this
were not the case, macroscopic information would not suffice for
predicting macroscopic behavior, and there could be no science of
thermodynamics.

## CONCLUSION
Although the assumption of realism implies that the principle of
macroscopic uniformity must be true, the converse does not hold. Indeed,
the principle of macroscopic uniformity, in a somewhat weaker form, has
long been recognized. If we accept it, we can relax considerably the
requirements for the possible interpretation discussed in Sec. 4. There
is no longer any need for the system to be exactly "in a Boltzmann
distribution." Any reasonable approximation to it will still lead to the
same macroscopic predictions.

The interpretation of statistical mechanics based on the assumption of
realism carries many implications for current unsolved problems in
statistical mechanics.[^17] In the following we point out two examples
of the manner in which these problems change if we now interpret
"microscopic state" as meaning a pure state of quantum theory.

### A. Irreversible Processes.
One of the fundamental problems of the theory of irreversible processes
is how to find the ensemble which correctly represents a system in a
nonequilibrium state. With our interpretation, however, there is no such
thing as a "correct" ensemble; the notion is quite meaningless.

Nevertheless, because of the principle of macroscopic uniformity, we
conclude that the methods of maximum-entropy inference,[^11] when
generalized to the density matrix formalism, must provide a correct
prediction of every feature of irreversible processes which is
experimentally reproducible. The reason for this is that every property
which is characteristic of the great majority of the possible states
will emerge from this treatment with a sharp probability distribution.
Thus the prescription for a general theory of irreversible processes
becomes: For the initial time t = 0, find the density matrix which
maximizes the entropy $S = -\operatorname{Tr}(\rho \log \rho)$ subject to all
the constraints represented by the available information. The solution
of $i\hbar \dot{p} = [H,\rho]$ with this initial condition must
contain the description of the irreversible process. In finding this
solution, any approximation which does not alter the expectation values
$\langle F \rangle = \operatorname{Tr}(\rho F)$ of the quantities which we wish to predict,
are permissible regardless of what they do to $\operatorname{Tr}(\rho \log \rho)$. Thus, the adoption of a "coarse-grained
density" is not something required by philosophical principles[^7]
concerning the accuracy of measurements; it represents simply the
process of discarding, voluntarily, irrelevant information.

### B. Condensation.
In attempts to understand condensation since the time of van der Waals,
the underlying idea has been that the phenomenon is basically a
statistical one, which would be understood if only one could do a
rigorous job of evaluating partition functions and passing to the limit
$N \to \infty$. However, since condensation is an experimentally
reproducible property, we are forced to conclude that it must be found,
not only in some ensemble average, but it must be characteristic of
*each* of the great majority of the pure states compatible with the
conditions of the experiment. But if this is so, then condensation must
be predictable already from a study of the properties of typical pure
states, *independently of any statistical consideration*. As we lower
the energy of a gas, we must reach a point where practically all of the
possible stationary states correspond to a greater density of matter
along the bottom portion of the container. Thus the problem of
condensation becomes primarily one of physics rather than statistics.

We see that if we abandon the attempt to utilize ergodicity, and at the
same time retain the assumption of realism, the fact that statistical
mechanics is successful carries far-reaching implications which are
capable of being tested independently. Conversely, if it can be shown
that any of these implications, such as (A) or (B) above, is false, then
it would appear that we must either abandon the association
"microscopic state = pure state," or else return to the interpretation
of Sec. 4.

## REFERENCES
[^1]: P. and T. Ehrenfest, *Encykl. Math. Wiss.* **4**, No. 32 (1911).
[^2]: R. H. Fowler, *Statistical Mechanics* (Cambridge, 1936), 1.4.
[^3]: R. C. Tolman, *The Principles of Statistical Mechanics* (Oxford University Press, 1938), 25.
[^4]: H. Poincaré, *Acta Math.* **13**, 67 (1890).
[^5]: L. Boltzmann, *Wien. Ber.* **106**, 12 (1897).
[^6]: D. ter Haar, *Elements of Statistical Mechanics* (Rinehart and Company, New York, 1954), Appendix I.
[^7]: D. ter Haar, *Rev. Mod. Phys.* **27**, 289 (1955).
[^8]: H. Bohr, *Almost Periodic Functions* (Chelsea Publishing Company, New York, 1947).
[^9]: By this is meant the first nontrivial translation number, i.e., we do not count the translation numbers which occupy a neighborhood of zero. That the latter are formally translation numbers depends only on the continuity, not the almost-periodicity, of f(t).
[^10]: As a simple example showing why the stronger statement could not be true in general, consider the function $f(t) = e^{i\omega_1 t} + e^{i\omega_2 t} + e^{i\omega_3 t}$, where the frequencies are all incommensurable and $\omega_1 \ll \omega_2$, $\omega_1 \ll \omega_3$. Then if $m, n$ are the smallest integers for which $|m(\omega_2/\omega_3) - n| \le \epsilon/4\pi$ and $\omega_1$ is sufficiently small so that $n(\omega_1/\omega_3) \le \epsilon/4\pi$, the interval $\tau_1 = (2\pi n/\omega_3)$ is a translation number corresponding to $\epsilon$. Clearly, however, in order to obtain a representative sample of $f(t)$, one must observe it for at least a time interval $T$ so long that all three terms have completed nearly an integral number of cycles. This time is of the order of $T \approx (2\pi/\omega_1) \ge 4\pi \tau_1/\epsilon$. As a second example, consider the case where $\omega_1$ is very close to $\omega_2$.
[^11]: E. T. Jaynes, *Phys. Rev.* **106**, 620 (1957).
[^12]: A. Einstein, B. Podolsky, and N. Rosen, *Phys. Rev.* **47**, 777 (1935).
[^13]: N. Bohr, *Phys. Rev.* **46**, 696 (1935).
[^14]: P. A. M. Dirac, *The Principles of Quantum Mechanics* (Second Edition, Oxford, 1935); Chapter I.
[^15]: R. K. Wangsness and F. Bloch, *Phys. Rev.* **89**, 728 (1953).
[^16]: F. Bloch, *Phys. Rev.* **102**, 104 (1956); **105**, 1206 (1957).
[^17]: L. van Hove, *Rev. Mod. Phys.* **29**, 200 (1957).
