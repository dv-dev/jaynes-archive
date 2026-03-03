---
title: "The Second Law as Physical Fact and as Human Inference"
author: ["E.T. Jaynes"]
year: 1990
abstract: >
  We try to correct some persistent misconceptions which are preventing
  progress in current research. These include failure to take note of
  highly cogent facts and theorems, semantic confusions over
  terminology, and clinging to folklore long after it is obsolete.
---
## Introduction {#introduction .unnumbered}
In spite of the spectacular advances in experimental techniques all
about us, we live in an age of inexplicable decadence where theory is
concerned. A wild variety of different views about entropy and
reversibility, their place in fundamental physics, and the role of
information for science in general, is being expressed. But important
facts that were well understood and clearly explained by Maxwell and
Gibbs over 100 years ago, and which played a crucial role in the work of
Planck and Einstein 80 years ago, have been lost and are no longer
comprehended at all by some who try to work in this area.

Max Planck (1949) complained about this over 40 years ago, and it is
worse today, the advances in understanding of the past 40 years being
equally ignored. As a result, the field seems to have reached an
evolutionary dead end, settled into a limit cycle in which the same
things are rediscovered, and the same old errors are repeated back and
forth, endlessly. We are unable to point to a single new useful result
from this activity.

Yet in the past 40 years we have accumulated a collection of
experimental facts and theorems that, in our view, resolve the paradoxes
about reversibility in a very simple and obvious way, and settle the
questions about the meaning of entropy and its relation to information,
thus determine the role it can play -- and the roles it cannot play --
for science in general.

This recently gained understanding has led to successful new
applications, far beyond equilibrium thermodynamics, in several
different fields. Use of the Maximum Entropy principle -- essentially,
the Gibbs canonical formalism for statistical mechanics -- in many
inverse problems such as spectrum analysis, image reconstruction, and
crystal structure determination, have been described before (Jaynes,
1986).

When more specific prior information is available, an addition to
maximum entropy -- the Bayesian analysis of Bretthorst (1988) -- has led
to a major advance in our ability to extract information from NMR data,
over the fourier transform methods previously used, and to safer methods
of detrending economic time series. Current methods of detrending
introduce spurious artifacts into the data, which can distort the final
conclusions. Bayesian analysis does not seek to remove the trend from
the data, but rather to remove the effect of trend from the final
conclusions, leaving the data intact.

What we believe is the first quantitative application of the second law
in a nonequilibrium biological problem is reported in Jaynes (1989).
There we calculate the maximum theoretical efficiency of muscles from
the energy release $\Delta H = -9.9$ kcal/mol of the chemical reaction
(ATP hydrolysis) which powers them, and the value $T = 273+37 = 310$ K
of body temperature (Jaynes,
1989). The observed efficiency was long thought to be \"too high\", in
violation of the second law; but now a more careful statement of the
second law, which holds in nonequilibrium situations by taking into
account its connection with information, leads to a correct prediction
of that efficiency.

In other words, we ought to be beyond the stage of philosophical
argumentation; where thirty years ago we had only faith, we now have
demonstrated facts and theorems. The difficulty is still the one about
which Max Planck complained; the seeming impossibility of getting
workers in the field to take note of what is already well known. As
Planck put it, a commonly heard statement about the meaning of
thermodynamic reversibility is \"-- an error against which I have fought
untiringly all my life, but which seems impossible to eradicate.\" This
error, discussed below, is still rampant today throughout the
literature; no other area of science seems to have this problem.

In the following, we confine ourselves to citing demonstrable facts
without trying to promote any particular philosophical viewpoint,
because we think that those facts are cogent enough to speak for
themselves.
## The Experimental Facts: Clausius {#the-experimental-facts-clausius .unnumbered}
The general statement of the empirical second law, due to Clausius, is
simply $$S_{\text{initial}} \le S_{\text{final}}$$ in which S stands for
the total entropy of all bodies that take part in a process, and the
entropy for a single system is defined to within an additive constant
for closed systems by $$S_B - S_A = \int_A^B \frac{dQ}{T}$$ but it
requires some discussion to set forth its full meaning. We note five
important facts:
\(I\) This statement is logically equivalent to Carnot's principle (no
heat engine can be more efficient than a reversible one operating
between the same temperatures). That is, it is deducible directly from
Carnot's principle, and it implies Carnot's principle. We have given the
reasoning showing this, reduced to its bare essentials (Jaynes, 1988).
Therefore, although (1) is not proved to be true as a consequence of the
laws of physics, if a physical phenomenon is ever found which violates
(1), then we shall have the means to realize Carnot's perpetual motion
machines of the second kind after all.
\(II\) The integral in (2) is necessarily over a reversible path (i.e.,
a locus of equilibrium states) connecting the macroscopic thermodynamic
states A and B, because the temperature T in (2) is not defined except
in states of thermal equilibrium. Entropy is therefore defined in
classical thermodynamics only for states of thermal equilibrium.
\(III\) Because of (II), statements of the genre $dS/dt \ge 0$ are not
justified (i.e. not deducible from the foundations) in classical
thermodynamics. Of course, one can generalize the notion of entropy to
nonequilibrium, time-dependent conditions; but this can be done in many
different ways and there is no criterion for saying that one is
\"right\" and another \"wrong.\" Rather, some ways may be useful, others
not useful. But the onus is on the one who generalizes to demonstrate
that useful properties actually do exist, which make a difference in
applications.
\(IV\) According to (2) the entropy is to be found from experimental
measurements with calorimeters and thermometers, and so it is by
construction a function $S(V,T,N)$ of the macrostate of a system. It
makes no reference to any such notion as a microstate, much less to any
probability.
\(V\) The entropy defined by (2) is not necessarily extensive; that is,
from (2) one cannot deduce that $S(T, 2V, 2N) = 2S(T,V,N)$. For in (2)
we are varying T and V, while holding N constant.

Therefore (2) tells us only how entropy varies with T and V; it says
nothing about how it depends on N. Indeed, there are systems, such as
spin systems, in which the entropy is not extensive because of
long-range interactions; but for which the Clausius definition (2) is
still valid.

In summary, the second law (1) of Clausius, as a physical fact, is a
proposition of observed macroscopic phenomenology, which makes a
qualitative comparison of two states of thermal equilibrium. The
Clausius entropy is, by definition and construction, a property only of
the macrostate; it makes no reference to microstates, equations of
motion, probability, or nonequilibrium states.
## The Human Inference: Gibbs {#the-human-inference-gibbs .unnumbered}
In noting the position of the pioneers we need to distinguish between
early Planck and late Planck, for he changed his mind in mid-career.
Clausius and early Planck sought to establish the second law (1) as an
absolute law of physics, true of necessity in every case. Late Planck
recognized that this is impossible, and advanced to the viewpoint of
Gibbs. As recounted by Kline (1983), Boltzmann changed his mind many
times.

There are two cogent reasons why one must abandon the view of Clausius
and early Planck. First is the recognition that the entropy to which (1)
and (2) refer is not a "real physical property" of a physical system; it
has also an anthropomorphic quality because it is a property of the
*Thermodynamic system* that you or I create by the measurements we
choose to make on the system. A given physical system (say, a quartz
crystal) corresponds to many different thermodynamic systems, depending
on which macrovariables you or I choose to observe and/or control. They
have different entropy functions, depending on different macrovariables
(Jaynes, 1965). It is therefore meaningless to speak of the \"entropy of
the crystal\" as if it were a physical property like its energy.

This is no more paradoxical than the fact the music produced by a piano
is not an \"objective physical property\" of the piano; it has also an
anthropomorphic quality, because a given piano may produce an unlimited
variety of music, depending on which keys you or I choose to press down.
To see the second cogent reason why the \"absolute physical law\"
position must be abandoned, we turn to the work of Gibbs. The above
statement of the Second Law is still the one traditionally taught to
physicists, although it has severe limitations. It gives us one piece of
information about the general direction in which an irreversible process
will go; but it does not tell us how fast it will go, how far, or along
what specific path. And it refers only to a closed system (no particles
enter or leave).

Gibbs showed how to remove two of those limitations. He generalized the
definition of entropy to open systems, as needed for many applications.
More important for our purposes, he perceived the correct logical status
of (1), which enabled him to extend its application to quantitative
prediction, thus answering the question: \"How far?\".

Instead of Clausius' weak statement that the total entropy of all bodies
involved \"tends\" to increase, Gibbs made the strong prediction that it
*will* increase, up to the maximum value permitted by whatever
constraints (conservation of energy, volume, mole numbers, etc.) are
imposed by the experimental arrangement and the known laws of physics.
Furthermore, the systems for which this is predicted can be more
complicated than those envisaged by Clausius; they may consist of many
different chemical components, free to distribute themselves over many
phases.

Gibbs' variational principle resolved the ambiguity: \"Given the initial
macroscopic data defining a nonequilibrium state, there are millions of
conceivable final equilibrium macrostates to which our system might go,
all permitted by the conservation laws. Which shall we choose as the
most likely to be realized?\"

Although he gave a definite answer to this question, Gibbs noted that
his answer was not found by deductive reasoning. Indeed, the problem had
no deductive solution because it was ill-posed.

There are initial microstates, allowed by the data and the laws of
physics, for which the system will not go to the macrostate of maximum
entropy. There may be additional constraints, unknown to us, which make
it impossible for the system to get to that state; for example new
\"constants of the motion\". So on what grounds could he justify making
that choice in preference to all others?

At this point thermodynamics takes on a fundamentally new character. We
have to recognize the distinction between two different kinds of
reasoning; *deduction* from the laws of physics, and *human inference*
from whatever information you or I happen to have. Instead of asking,
\"What do the laws of physics require the system to do?\", which cannot
be answered without knowledge of the exact microstate, Gibbs asked a
more modest question, which can be answered: \"What is the best guess we
can make, from the partial information that we have?\"

But Gibbs was only recognizing something that is true universally. In
all of science. in or out of thermodynamics, what happens in the real
world depends on physical law and is on the level of ontology. What we
can predict depends on our state of knowledge, and is necessarily on the
level of epistemology. He who confuses reality with his knowledge of
reality generates not solutions, but paradoxes. However, there is still
very little perception of this in the scientific community, and attempts
to point it out can generate bitter controversy.

The conventional attitude is exhibited by those who would object to
Gibbs' answer on the grounds that there may be unknown constraints that
prevent the system from getting to the state of maximum entropy; and so
Gibbs' answer might be wrong. But since the question was ill-posed, the
same kind of objection would apply whatever answer he gave; if such an
objection were sustained, Gibbs would be prohibited from giving any
answer at all. Science does not advance on that kind of timidity; let us
note how much more realistic and constructive is the opposite attitude.
To one who raised that objection, Gibbs might reply as follows:
\"Of course, my answer might be wrong. You seem to think that would be a
calamity that we must avoid; but you are like a chess player who thinks
only one move ahead. If you will think ahead two moves, you will see
that, on the contrary, getting a wrong answer would be even more
valuable than getting a right one. As you note, at present we do not
know whether there may exist unknown constraints that would prevent the
system from getting to the maximum entropy state. But I choose to ignore
that warning, go ahead with my calculation, and then ask an
experimentalist to compare my prediction with observation. What
conclusions will we be able to draw from his verdict?
\"Suppose my prediction turns out to be right. That does not prove that
no unknown constraints exist; but it does prove that there are none
which prevent the system from getting to the macrostate of maximum
entropy. So the calculation has served a useful predictive purpose, and
its success gives us more confidence in future predictions.
\"But suppose my prediction turns out to be wrong; the experiment
repeatedly gives a different result. Then we have learned far more; we
know that there is some new (i.e., previously unknown) constraint
affecting the macroscopic behavior, and the nature of the error gives us
a clue as to what that new constraint is. We would have a start toward
learning a fundamental new physical fact, perhaps a new law of physics.
I do not see this as a calamity; how else can we advance to a new state
of knowledge about physical law, but by having the courage to go ahead
with the best inferences we can make from our present state of
knowledge?\"

The words we have just put into Gibbs' mouth are not fanciful. Gibbs'
classical statistical mechanics did make incorrect predictions of
specific heats. Those were the first clues, indicating the new
constraints of discrete energy levels, pointing to the quantum theory.
Nobody would have realized that specific heats were relevant to the
question, had Gibbs lacked the courage to make an inference because he
might be wrong.

After development of the Schrödinger equation, the Gibbs formalism based
on maximizing
the new quantum expression for entropy has yielded so many thousands of
quantitatively correct equilibrium predictions that there seems to be
almost no chance that it will ever fail in that problem. Whenever it did
seem to fail -- as in the case of ortho and para hydrogen -- it was seen
quickly that it was only performing its second function, revealing an
unexpected constraint.

Today, we are only in the initial stages of extensions to predict the
details of nonequilibrium behavior; these put our entropy expressions to
a more severe test. We can by no means rule out the possibility that
nonequilibrium statistical mechanics may lead to incorrect predictions,
which would then point the way to the next higher level of understanding
of physical law, beyond our present quantum theory. We may be seeing the
incipient beginnings of this in the lore of \"strange attractors\".
We think that this scenario will be repeated many times in the future,
particularly as the method moves into biology. Most maximum entropy
inferences will be correct, serving a useful predictive purpose. But
some of the predictions will be wrong; those instances, far from being
calamities, will open the doors to new basic knowledge.

Another of the curiosities of this field is that, having done so much
with entropy and demonstrated such a deep understanding of the logic
underlying the second law, giving thermodynamics an entirely different
character, Gibbs said almost nothing about what entropy really means. He
showed, far more than anyone else, how much we can accomplish by
maximizing entropy. Yet we cannot learn from Gibbs: \"What are we
actually doing when we maximize entropy?\" For this we must turn to
Boltzmann.
## Fourth Metamorphosis: Boltzmann {#fourth-metamorphosis-boltzmann .unnumbered}
Entropy first appeared, unanticipated and without warning, merely as a
mathematical construct in equation (12). Even after its fundamental
nature and usefulness were recognized and exploited, the question:
\"What is it?\" continued to mystify and confuse. It appears that the
answer was first revealed to Ludwig Boltzmann, when he calculated the
phase volume of an ideal gas of N atoms in volume V, for which the
energy lies in $(E, E + dE)$:
$$W = \int_R d^3x_1 \dots d^3x_N d^3p_1 \dots d^3p_N = CV^N E^{3N/2-1} dE$$
where the region R of integration is those points for which all
coordinates are within a volume V, and the momenta satisfy
$$E < \sum p_i^2/2m < E + dE.$$ The constant C is independent of V and E.

Now from elementary thermodynamics it was known that the entropy of any
system which obeys the equation of state $PV = RT$ with a heat capacity
$C_v = \text{const.}$, has the form
$S(V,T) = C_v \log T + R \log V + \text{const.}$, where the const. is
independent of T and V. But with the heat capacity for Boltzmann's
monoatomic gas, $C_v = (3/2)R$ and the resulting internal energy
function $E = (3/2)RT$, it was evident that $\log W$ has the same volume
and energy dependence as the entropy of that gas, calculated from (12).
That is, to within an additive constant independent of T and V, it was
true that $$S = k \log W.$$ This is such a strikingly simple relation
that one can hardly avoid jumping to the conclusion that it must be true
in general; i.e., the entropy of any macroscopic thermodynamic state A
is a measure of the phase volume $W_A$ occupied by all microstates
compatible with A.

It is convenient verbally to say that S measures the \"number of ways\"
in which the macrostate A can be realized. This is justified in quantum
theory, where we learn that a classical phase
volume W does correspond to a number of global quantum states
$n = W/h^{3N}$. So if we agree, as a convention, that we shall measure
classical phase volume in units of $h^{3N}$, then this manner of
speaking will be appropriate in either classical or quantum theory.
We feel quickly that the conjectured generalization of (17) must be
correct, because of the light that this throws on our problem. Suddenly,
the mysteries evaporate; the meaning of Carnot's principle, the reason
for the second law, and the justification for Gibbs' variational
principle, all become obvious. Let us survey quickly the many things
that we can learn from this remarkable discovery.

Given a \"choice\" between going into two macrostates A and B, if
$S_A < S_B$, a system will appear to show an overwhelmingly strong
preference for B, not because it prefers any particular microstate in B,
but only because there are so many more of them. As noted in Appendix C,
an entropy difference $(S_B - S_A)$ corresponding to one microcalorie at
room temperature indicates a ratio $W_B/W_A > \exp(10^{15})$. Thus
violations are so improbable that Carnot's principle, or the equivalent
Clausius statement (14), appear in the laboratory as absolutely rigid
\"stone wall\" constraints suggesting a law of physics rather than a
matter of probability.

Let us see the light that this casts on Gibbs' method, by examining a
simple application. We have two systems of one degree of freedom (i.e.,
their energy and temperature can vary when in contact with other
systems). Then their entropy functions are
$$S_1(E_1) = k \log W_1(E_1), \quad S_2(E_2) = k \log W_2(E_2),$$ The
systems start out in thermal equilibrium with arbitrary initial energies
$E_{1i}, E_{2i}$. Then they are placed in contact so they can exchange
energy in such a way that the total amount is conserved:
$$E = E_1 + E_2 = \text{const.}, \quad E_1 > 0, \quad E_2 > 0.$$

Required: to predict the final energies $E_{1f}, E_{2f}$ that they will
reach when they come into equilibrium with each other.

This is manifestly an ill-posed problem; for the final energies must
depend on the initial microstates which are unknown; and all values
compatible with (19) are possible without violating any known laws of
physics. We are thus obliged to use inference rather than deduction.
Gibbs' algorithm was: predict that energy distribution that maximizes
the total entropy $S_1 + S_2$ subject to the constraint (19). At first
this seems arbitrary; but now if (17) is correct we can see why this
guess is \"best\". We are maximizing the product
$$M(E_1) = W_1(E_1)W_2(E - E_1)$$ with respect to $E_1$; but that
product is just the multiplicity, or number of ways in which the energy
distribution $(E_1, E_2)$ can be realized. So in the light of (17)
Gibbs' rule now says, merely: \"Predict that energy distribution that
can happen in the greatest number of ways, subject to the information
you have\". An eminently sensible criterion!
Experimentally, one says that equilibrium is reached when the systems
have equal temperature. Differentiating (20), we find that the maximum
is reached when $d \log W_1/dE_1 = d \log W_2/dE_2$. But the general
thermodynamic relation $T^{-1} = dS/dE$ that follows from (12) becomes,
in the light of (17) $$\frac{1}{kT} = \frac{d \log W}{dE}$$ So the
general interpretation of entropy by (17) not only predicts equal
temperature as the condition for equilibrium; it gives a simple
explanation of why this is true.
The above explains why Gibbs' method gives, in a sense, the best guess
one could have made in view of our great ignorance as to the microstate;
but does not explain why it is so uniformly successful. If the
multiplicity (20) had a broad maximum, or many local maxima, one would
not expect Gibbs' rule to be very reliable in practice. This raises the
question: How sharp is the maximum in the multiplicity (20)? Note that
differentiating (21) once more gives the heat capacity:
$$\frac{d^2 \log W}{dE^2} = - \frac{1}{kT^2 C_v}$$ But, as (15) shows
for an ideal gas and is true in general, $C_v$ may be interpreted as
$C_v = nk/2$, where n is the effective number of degrees of freedom of
the system (in quantum theory, the number excited at the temperature T),
of the order of Avogadro's number for a macroscopic system. Therefore,
expanding $\log M(E_1)$ about its peak at $E^\prime$ we have
$$M(E_1) = M(E^\prime) \exp\left \{-\frac{(E_1 - E^\prime)^2}{2\sigma^2}\right \}$$
with the RMS deviation
$$\sigma = kT \left[ \frac{n_1 n_2}{n_1 + n_2} \right]^{1/2},$$ which is
of the order of $kT n^{1/2} = E^\prime/n^{1/2} \approx 10^{-12} E^\prime$.
Therefore, not only is $E^\prime$ the value of $E_1$ that can happen in the
greatest number of ways for given total energy $E$; the vast majority of
all possible microstates with total energy $E$ have $E_1$ very close to
$E^\prime$. Less than 1 in $10^8$ of all possible states have $E_1$ outside
the interval $(E^\prime \pm 6\sigma)$, far too narrow to measure
experimentally. From (17), then, we understand also why Gibbs' method
succeeds.

But there is still more to be learned from Boltzmann's discovery (17).
Imagine $n_2$ to become very large; then we may expand using (21):
$$\log W_2(E-E_1) = \log W_2(E) - \frac{E_1}{kT} + \dots$$ and from (22)
the next term is negligible. But then the fraction of the multiplicity
(23) in the interval $(E_1, E_1+dE_1)$ becomes
$$f(E_1) dE_1 = Z^{-1} W_1(E_1) \exp(-E_1/kT) dE_1$$ which is the
distribution of Gibbs' \"Canonical Ensemble\", the basis of his later
work on Statistical Mechanics. The normalization constant
$$Z(\beta) = \int W_1(E) \exp^{-\beta E_1} dE, \quad \beta=1/kT$$ is

Gibbs' partition function, and if we refine the inference procedure by
taking as our prediction the mean value over the distribution (26)
instead of the peak $E^\prime$, our prediction reduces to
$$\langle E_1 \rangle = -\frac{d \log Z}{d\beta},$$ the basic predictive
rule of statistical mechanics.

All these relations generalize effortlessly to systems with more
macroscopic degrees of freedom (volume, magnetization, angular momentum,
mole numbers, etc.) corresponding to Gibbs' grand canonical ensemble and
its generalizations. So the interpretation (17) of entropy has given us
the key to essentially everything that has happened since in the field
of equilibrium thermodynamics and statistical mechanics. This was
recognized, and exploited in their own fundamental research, by both
Planck and Einstein.

In our opinion, (17) represents by far the greatest of all of
Boltzmann's achievements, just because of its fundamental, timeless
character. One hundred years from now, his transport equation will be a
nearly forgotten detail of the history of science; but a thousand years
from now, the relation $S = k \log W$ will still be the foundation stone
of this subject. A more appropriate inscription for his gravestone can
hardly be imagined.

If we had more information we would seldom do better in prediction of
reproducible phenomena, because those are the same for virtually all
microstates in an enormously large class C; and therefore also in
virtually any subset of C. Indeed, as Gibbs showed, in almost every case
the knowledge supposed above is already sufficient to predict
equilibrium states correctly. Still greater knowledge (such as, perhaps,
that the real system stays in some complicated fractal subset of C)
might be very interesting and important for future purposes; but it
would not have helped for the predictions that Gibbs was making.

Knowledge of the \"data\" E alone would not enable us to choose among
the different values of $E_1$ allowed by (19); the additional
information contained in the entropy functions, nevertheless leads us to
make one definite choice as far more likely than any other, on the
information supposed.
# WHAT DOES 'REVERSIBILITY' MEAN? {#what-does-reversibility-mean .unnumbered}
Thermodynamics is notoriously a field which encourages confusion and
illogic by a terminology which may use a common technical term with
several different meanings, and fails to distinguish between them. We
have noted before (Jaynes, 1980) some of the many different, mutually
inconsistent meanings that have been attached to the word \"entropy\".
An equally serious confusion arises from the fact that the word
\"reversible\" is used with different meanings; and hardly anybody
writing today takes any note of this. The term was introduced by Carnot
in his idea of a reversible heat engine, but Carnot's meaning is only
one of three used interchangeably today.

Let A and B stand for two different macrostates, defined by specifying
(i.e., controlling or observing) a few macroscopic quantities like
temperature, volume, pressure, magnetization, such that the change
$A \to B$ can be carried out, reproducibly, in the laboratory. What do
we mean by saying that it is reversible? In the literature, we find
these quite different meanings:
\(1\) **Mechanical Reversibility.** Reversing all molecular velocities
in B, the equations of motion carry the system back along exactly its
previous path to A. In the end this would restore each individual
molecule to its original position. (But they would be moving in the
reverse direction, so one must reverse all velocities a second time to
restore the original microstate).

But this is manifestly not what Carnot had in mind. In his reversible
engines he is considering instead:
\(2\) **Carnot Reversibility.** The macroscopic physical process can be
made to proceed in the opposite direction $B \to A$, restoring the
original macrostate.

This is an enormously weaker condition than mechanical reversibility.
But it was noted by Clausius, Gibbs, and Planck that thermodynamic
reversibility is a still weaker condition:
\(3\) **Thermodynamic Reversibility.** Even if the backward process
$B \to A$ cannot be made to take place reversibly (for example, because
of supercooling at a phase transition), if by any means such as
$B \to C \to D \to A$ the original macrostate can be recovered without
external change, then all entropies are unchanged and the process
$A \leftarrow B$ is thermodynamically reversible.

From this we see that the common phrase \" -- the paradox of how to
reconcile the irreversibility of the second law with the reversibility
of the equations of motion -- \" does not define any paradox at all; it
is a nonsense utterance, using the term \"reversible\" in the totally
different meanings (1) and (3) in the same sentence. Yet this nonsense
utterance is repeated endlessly in the current literature.

These observations are hardly new. The distinction between mechanical
and thermodynamic reversibility was stressed already by Gibbs (1875) in
his discussion of gas diffusion. Confusion of thermodynamic
reversibility with Carnot reversibility is the error that Planck
complained was 'impossible to eradicate.' Indeed, to this day it has not
been possible to eradicate it.

Despite the efforts of Gibbs and Planck, these distinctions have been
lost today. We have found no recognition of them in current
thermodynamics textbooks, or in the current literature of this field.
Indeed, both Maxwell and Gibbs are still under attack, from authors who
still have not comprehended their messages. See, for example, Atkins
(1986). Recent efforts to \"explain irreversibility\" by tampering with
the equations of motion or the definition of entropy, address themselves
to a non-problem, for reasons that Gibbs explained cogently over 100
years ago.

Indeed, our belief in mechanical reversibility is not based on
experimental fact at all; only on the mathematical fact that our
Lagrangian functions are even functions of the velocities, so that if
the reversed motion were to take place, the equations of motion would be
satisfied. But nobody has ever seen a motion and its exact reversed
version; anyone who imagines that mechanical reversibility is an
experimentally verifiable fact, has never tried to drive backwards along
a winding road with a trailer.

Of course, approximate reversal of a few degrees of freedom is possible,
whose effects persist for a short time; for example in spin echoes and
percolation of water and oil through shale. These cases are valuable
because they stand as counter-examples to glib, unqualified statements
of the second law in the form $dS/dT \ge 0$, and force us to recognize
that the Clausius second law refers only to processes that begin and end
in states of thermal equilibrium.

It should not require a lengthy demonstration to persuade us that one
cannot reverse all molecular velocities -- to infinite accuracy -- with
the technology (pistons, stoves, magnets, etc.) available to
experimenters. By experimental means of macroscopic coarseness one can
generate a class of initial states from which a macroscopic process
$A \to B$ takes place reproducibly; but in general the reversed process
$B \to A$ cannot be achieved reproducibly by macroscopic means. That the
microscopic equations of motion may nevertheless be \"reversible\" in
the mechanical sense, is quite irrelevant to what the experimenter can
actually do.

Yet we can understand at once why irreversibility is observed in real
laboratory experiments, if we recognize the interpretation of entropy
$S = k \log W$ expounded by Boltzmann, Planck, and Einstein. Let $W_A$
be the phase volume occupied by all microstates compatible with the
macrostate A. If in setting up the state A the experimenter's apparatus
is able to put the system only in some uncontrolled point in $W_A$, then
because of Liouville's theorem (conservation of phase volume) the
process $A \to B$ cannot be reproducible unless the phase volume $W_B$
is large enough to hold all the microstates that could evolve out of
$W_A$.

In other words, reproducibility of the process $A \to B$ requires that
$W_B \ge W_A$, or $S_B \ge S_A$. If the inequality holds, then the
reverse process is, as Gibbs noted, not impossible, but only improbable;
i.e., not reproducible. The probability of success is something like
$$p = \frac{W_A}{W_B} = \exp\left(-\frac{S_B - S_A}{k}\right)$$ If the
entropy difference corresponds to about the smallest amount that could
be measured in the laboratory, say one microcalorie at room temperature,
$p < \exp(-10^{15})$. We do not see why any more than this is needed to
understand and explain the observed phenomenological facts about
irreversibility associated with the second law; yet contemporary writers
still try to make a major mystery out of it.

But this simple understanding enables us to generalize the second law
far beyond the equilibrium conditions envisaged in (1). As soon as we
recognize that the fundamental keyword characterizing the second law is
not 'disorder' but 'reproducibility', it is clear that $S = k \log W$
applies equally well to determining which nonequilibrium states can be
reached, reproducibly, from which others and without any restriction
to slow, reversible processes.

This is the principle underlying the above mentioned calculation of
muscle efficiency. Quite generally, biological processes take place so
rapidly that nothing like thermal equilibrium is ever achieved, so
conventional 'free energy' thermodynamics does not apply. Attempts to
apply the second law in biology could not have succeeded until this was
recognized.
## References {#references .unnumbered}
Bretthorst, G. L. (1988), *Bayesian Spectrum Analysis and Parameter
Estimation*, Springer Lecture Notes in Statistics, Vol. 48.

Gibbs, J. Willard (1875-78) \"On the Equilibrium of Heterogeneous
Substances\", Trans. Conn. Acad. Sci. Reprinted in *The Scientific
Papers of J. Willard Gibbs*, Vol. 1; Dover Publications, Inc., N. Y.
(1961).

E. T. Jaynes (1980), \"The Minimum Entropy Production Principle\", in
*Annual Review of Physical Chemistry*, Vol. 31, 579-601 (1980).

Reprinted in *E. T. Jaynes, Papers on Probability, Statistics and
Statistical Physics*, R. Rosenkrantz, Ed., D. Reidel Publishing Co.,
Dordrecht-Holland (1983)

Jaynes, E. T. (1986), "Predictive Statistical Mechanics\", in *Frontiers
of Nonequilibrium Statistical Mechanics*, G. T. Moore & M. O. Scully,
Editors, Plenum Press, New York, pp. 33-56.

Jaynes, E. T. (1988), "The Evolution of Carnot's Principle\", in
*Maximum-Entropy and Bayesian Methods in Science and Engineering*, G. J.
Erickson & C. R. Smith, Editors, Kluwer Academic Publishers,
Dordrecht-Holland; Vol. 1, pp. 267-282.

Jaynes, E. T. (1989), \"Clearing up Mysteries -- The Original Goal\", in
*Maximum Entropy and Bayesian Methods*, J. Skilling, Editor, Kluwer
Academic Publishers, Dordrecht-Holland, pp.1-27.

A. L. Lehninger, *Bioenergetics*, W. A. Benjamin, N. Y. (1965)

A. L. Lehninger, *Biochemistry, the Molecular Basis of Cell Structure
and Function*, Worth Publishers, Inc., 444 Park Ave. South, New York, N.
Y. (1975).

L. Onsager, Phys. Rev. **37**, 405; **38**, 2265 (1931)

Peierls, R. (1979), *Surprises in Theoretical Physics*, Princeton Univ.
Press.

Penrose, R. (1979), \"Foundations of Statistical Mechanics\", Rep. Prog.
Phys. **42**, 1937-2006.

Planck, M. (1949), *Scientific Autobiography*, Philosophical Library, N.
Y., pp. 17-18.
