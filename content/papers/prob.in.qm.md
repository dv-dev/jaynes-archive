---
title: "Probability in Quantum Theory"
author: ["E.T. Jaynes"]
year: 1990
abstract: >
  For some sixty years it has appeared to many physicists that
  probability plays a fundamentally different role in quantum theory
  than it does in statistical mechanics and analysis of measurement
  errors. It is a commonly heard statement that probabilities calculated
  within a pure state have a different character than the probabilities
  with which different pure states appear in a mixture, or density
  matrix. As Pauli put it, the former represents \"Eine prinzipielle
  Unbestimmtheit, nicht nur Unbekanntheit\". But this viewpoint leads to
  so many paradoxes and mysteries that we explore the consequences of
  the unified view, that all probability signifies only incomplete human
  information. We examine in detail only one of the issues this raises:
  the reality of zero-point energy.
---

## Introduction: How We Look at Things {#introduction-how-we-look-at-things .unnumbered}
In this workshop we are venturing into a smoky area of science where
nobody knows what the real truth is. Such fields are always dominated by
the compensation phenomenon: supreme self-confidence takes the place of
rational arguments. Therefore we shall try to avoid dogmatic assertions,
and only point out some of the ways in which quantum theory would appear
different if we were to adopt a different viewpoint about the meaning
and functional use of probability theory. We think that the original
viewpoint of James Bernoulli and Laplace offers some advantages today in
both conceptual clarity and technical results for currently mysterious
problems.

How we look at a theory affects our judgment as to whether it is
mysterious or irrational on the one hand; or whether it is satisfactory
and reasonable on the other. Thus it affects the direction of our
research efforts; and a fortiori their results. Indeed, whether we
theorists can ever again manage to get ahead of experiment will depend
on how we choose to look at things, because that determines the possible
forms of the future theories that will grow out of our present ones. One
viewpoint may suggest natural extensions of a theory, which cannot even
be stated in terms of another. What seems a paradox on one viewpoint may
become a platitude on another.

For example, 100 years ago it was a much discussed problem how material
objects can move through the aether without resistance. Yet a different
way of looking at it would have made the mystery disappear without any
need to dispense with the aether. One can regard material objects, not
as impediments to the "flow" of aether, but as parts of the aether
(\"knots\" in its structure) which are propagating through it. On this
way of looking at it, there is no mystery to be explained. As a student
at Princeton many years ago, I was fascinated to learn from John Wheeler
how much of physics can be regarded as really only geometry, in this
way.

Today we are beginning to realize how much of all physical science is
really only information, organized in a particular way. But we are far
from unraveling the knotty question: \"To what extent does this
information reside in us, and to what extent is it a property of
Nature?\" Surely, almost every conceivable opinion on this will be
expressed at this workshop.

Is this variability of viewpoint something to be deplored? Well,
eventually we should hope to present a unified picture to the rest of
the world. But for the moment this is neither possible nor desirable. We
are all looking at the same reality and trying to understand what it is.
But we could never understand the structure of a mountain if we looked
at it only from one side. The reality we are studying is far more subtle
than a mountain, and so it is not only desirable, but necessary that it
be examined from many different viewpoints, if we are ever to resolve
the mystery of what it is. Here we present one of those viewpoints,
which we think has not been sufficiently recognized in the recent
literature.

First we note a more immediate example of the effect of how we look at
things, to support by physical arguments what is suggested later from
probability considerations.

## How Do We Look at Gravitation and QED? {#how-do-we-look-at-gravitation-and-qed .unnumbered}
In teaching relativity theory, one may encounter a bright student who
raises this objection: \"Why should such a fundamental thing as the
metric of space and time be determined only by gravitational fields --
the weakest of all interactions? This seems irrational.\" We point out
to him a different way of looking at it, which makes the irrationality
disappear: \"One should not think of the gravitational field as a kind
of preexisting force which 'causes' the metric; rather, the
gravitational field is the main observable consequence of the metric.
The strong interactions have not been ignored, because the field
equations show that the metric is determined by all the energy
present.\" According to the first viewpoint, one might think it a
pressing research problem to clear up the mystery of why the metric
depends only on gravitational forces. On the second viewpoint this
problem does not exist.

But then if the student is very bright, he will be back the next day
with another criticism: \"If the gravitational field is only a kind of
bootstrap effect of the other forces, it raises the question whether the
gravitational field should be quantized separately. Wouldn't we be doing
the same thing twice?\" Thus different ways of looking at what a
gravitational field is, might lead one to pursue quite different lines
of research.

A similar issue arises in electrodynamics, making a thoughtful person
wonder why we quantize the electromagnetic (EM) field. The following
observations were made by Albert Einstein, in two lectures at the
Institute for Advanced Study, which I was privileged to attend in the
late 1940's. Needless to say, very careful transcripts of his words were
made.

He noted that in contemporary quantum theory we first develop the theory
of electrons via the Schrödinger equation, and work out its consequences
for atomic spectra and chemical bonding, with great success. Then we
develop a theory of the free quantized EM field independently, and
discuss it as a separate thing. Only at the end do we, almost as an
afterthought, decide to couple them together by introducing a
phenomenological coupling constant 'e' and call the result 'Quantum
Electrodynamics'.

Einstein told us: \"I feel that it is a delusion to think of the
electrons and the fields as two physically different, independent
entities. Since neither can exist without the other, there is only one
reality to be described, which happens to have two different aspects;
and the theory ought to recognize this from the start instead of doing
things twice.\"

Indeed, the solution of the EM field equations is, in either classical
or quantum theory, $$A_{\mu}(x) = \int D(x - y)J_{\mu}(y)d^4y.\tag{1}$$ In
quantum theory $A_{\mu}(x)$ and $J_{\mu}(y)$ are operators; but since
the propagator $D(x - y)$ is a scalar function, the $A_{\mu}(x)$ in (1)
is not an operator on a "Maxwell Hilbert Space\" of a quantized EM field
-- it is an operator on the same space as $J_{\mu}(y)$, the \"Dirac
Hilbert Space" of the electrons.

Conventionally, one says that (1) represents only the "source field" and
we should add to this the quantized \"free field\" $A_{\mu}^{(0)}(x)$
which operates on the Maxwell Hilbert space. But fundamentally, every EM
field is a source field from somewhere; therefore the free field is
already an operator on the Dirac Hilbert space of distant sources; so
why do we quantize it again, thereby introducing an infinite number of
new degrees of freedom for each of an infinite number of field modes?
The pragmatic distinction between the \"free field" and the \"source
field\" does not lie in whether we think the free field is or is not an
operator; what matters functionally (i.e. what makes a difference in the
results of our calculations) is whether it does or does not commute with
the local matter variables $J_{\mu}(x,t)$ at equal times. At first one
would think, on grounds of the relativity principle, that these
quantities must commute; any theory in which they do not is simply
wrong. However, later we shall see that the situation is not quite that
simple; it depends on some subtle points about the physical meaning of a
propagator, which are not discussed at all in current QED.

One can hardly imagine a better way to generate infinities in physical
predictions than by having a mathematical formalism with $(\infty)^2$
more degrees of freedom than are actually used by Nature. Stated
differently, then, the issue is: should we quantize the matter and
fields separately, and then couple them together afterward; or should we
write down the full classical theory with both matter and field, the
field equations in integrated form; and quantize it in a single step?
The latter procedure (assuming that we could carry it out consistently)
would lead to a smaller Hilbert space.

The viewpoint we are suggesting is very different in spirit, but
nevertheless very similar in its pragmatic consequences, to the
Wheeler-Feynman electrodynamics, in which the EM field is not considered
a \"real\" physical entity in itself, but only a kind of information
storage device invented by us. That is, the present EM field is a
\"sufficient statistic\" which merely summarizes all the information
about past motion of charges that is relevant for predicting their
future motion.

It is not enough to reply: \"The present QED procedure must be right
because it leads to several very accurate predictions: the Lamb shift,
the anomalous moment, etc.\" To sustain that argument, one would have to
show that the act of quantizing the free field actually plays an
essential role in determining those accurate numbers (1058 MHz, etc.),
and that, had we dealt with the free field differently, those numbers
would be different. But their calculation appears to involve only the
Feynman propagators; and mathematically, the propagator $D(x-y)$ in (1)
is equally well a Green's function for the quantized or unquantized
field (albeit with strange boundary conditions).

The conjecture suggests itself, almost irresistibly, that those accurate
experimental numbers come only from the local source fields, which are
coherent with the local state of matter. That is, the experimental
numbers come only from mathematical expressions of the form
$\int \int J_{\mu}(x) D(xy) J_{\mu}(y)dxdy$. Terms such as
$\int J_{\mu}(x)A_{\mu}^{(0)}(x)dx$ involving the quantized free field
in its ground state cancel out because it is uncorrelated with the local
state of matter. This has been confirmed in part by the \"source-field
theory\"[^2] which arose in quantum optics some years ago \[Milonni et al
(1973), Senitzky (1973), Allen & Eberly (1975)\]. It was found that, at
least in lowest nonvanishing order, observable effects such as
spontaneous emission and the Lamb shift, can be regarded as arising from
the source field which we had studied already in classical EM theory,
where we called it the \"radiation reaction field\". Some equations
illustrating this are given below; it is easy to make simple models in
which one can prove from the exact solutions that the analogs of
spontaneous emission and the Lamb shift are determined entirely by the
local source fields.

In these quantum optics calculations it seems that the quantized free
field only tags along, putting an infinite uncertainty into the initial
conditions (that is, a finite uncertainty into each of an infinite
number of field modes) and thus giving us an infinite "zero-point
energy\", but not producing any observable electrodynamic effects. One
wonders, then: If we don't use it, do we really need it?[^3]

## How Do We Look at Basic Quantum Theory? {#how-do-we-look-at-basic-quantum-theory .unnumbered}
Let us back off for a moment for a more general view of these things.
Current thinking about the role of information in science applies to all
areas (and in particular to biology, where perhaps the most valuable
results will be found). But the most tangled area in present physical
science is surely the standard old 1927 vintage quantum theory, where
the conceptual problems of the \"Copenhagen interpretation\" refuse to
go away, but are brought up for renewed discussion by every new
generation of physicists (much to the puzzlement, we suspect, of the
older generation who thought these problems were all solved). Starting
with the debates between Bohr and Einstein over sixty years ago,
different ways of looking at quantum theory persist in making some see
deep mysteries and contradictions in need of resolution, while others
insist that there is no difficulty.

How can scientists of unquestioned competence be in sharp disagreement
about such things? It must be that we have different unstated premises
(hidden assumptions) in the back of our minds. If so, then until we
bring out into the open just what those premises are, there would be no
possibility of resolving the issue.

Defenders of the Copenhagen interpretation have displayed a supreme
self-confidence in the correctness of their position, but this has not
enabled them to give the rest of us any rational explanations of why
there is no difficulty. Richard Feynman, while defending the QM
formalism on grounds of its practical success, at least had the honesty
to admit: \"Nobody knows how it can be that way.\"

While we doubters have not shown so much self-confidence, nevertheless
for all these years it has seemed obvious to me -- for the same reasons
that it did to Einstein and Schrödinger -- that the Copenhagen
interpretation is a mass of contradictions and irrationality and that,
while theoretical physics can of course continue to make progress in the
mathematical details and computational techniques, there is no hope of
any further progress in our basic understanding of Nature until this
conceptual mess is cleared up.

Because this position seems to arouse fierce controversy, let me stress
our motivation: if quantum theory were not successful pragmatically, we
would have no interest in its interpretation. It is precisely because of
the enormous success of the QM mathematical formalism that it becomes
crucially important to learn what that mathematics means. To find a
rational physical interpretation of the QM formalism ought to be
considered the top priority research problem of theoretical physics;
until this is accomplished, all other theoretical results can only be
provisional and temporary.

This conviction has affected the whole course of my career. I had
intended originally to specialize in Quantum Electrodynamics working
with J. R. Oppenheimer; but this proved to be impossible. Whenever I
look at any quantum-mechanical calculation, the basic craziness of what
we are doing rises in my gorge and I have to stop and try to find some
different way of looking at the problem, that makes physical sense.
Gradually I came to see that the resolution cannot be found within the
confines of the traditional thinking of physicists; the foundations of
probability theory and the role of human information have to be brought
in, and so I have spent many years trying to understand them in the
greatest generality.

The failure of quantum theorists to distinguish in calculations between
several quite different meanings of 'probability', between expectation
values and actual values, makes us do things that don't need to be done;
and to fail to do things that do need to be done. We fail to distinguish
in our verbiage between prediction and measurement. For example, the
famous vague phrases: 'It is impossible to specify\...'; or 'It is
impossible to define\...' can be interpreted equally well as statements
about prediction or statements about measurement. Thus the demonstrably
correct statement that the present formalism cannot predict something
becomes perverted into the logically unjustified -- and almost certainly
false -- claim that the experimentalist cannot measure it!

We routinely commit the Mind Projection Fallacy: supposing that
creations of our own imagination are real properties of Nature, or that
our own ignorance signifies some indecision on the part of Nature. It is
then impossible to agree on the proper place of information in physics.
This muddying up of the distinction between reality and our knowledge of
reality is carried to the point where we find some otherwise rational
physicists, on the basis of the Bell inequality experiments, asserting
the objective reality of probabilities, while denying the objective
reality of atoms! These sloppy habits of language have tricked us into
mystical, pre-scientific standards of logic, and leave the meaning of
any QM result ambiguous. Yet from decades of trial-and-error we have
managed to learn how to calculate with enough art and tact so that we
come out with the right numbers!

The main suggestion we wish to make is that how we look at basic
probability theory has deep implications for the Bohr-Einstein
positions. Only since 1988 has it appeared to the writer that we might
be able finally to resolve these matters in the happiest way imaginable:
a reconciliation of the views of Bohr and Einstein in which we can see
that they were both right in the essentials, but just thinking on
different levels.

Einstein's thinking is always on the ontological level traditional in
physics; trying to describe the realities of Nature. Bohr's thinking is
always on the epistemological level, describing not reality but only our
information about reality. The peculiar flavor of his language arises
from the absence of all words with any ontological import. J. C.
Polkinghorne (1989, pp. 78-79) came independently to this same
conclusion about the reason why physicists have such difficulty in
reading Bohr. He quotes Bohr as saying:
> \"There is no quantum world. There is only an abstract quantum
> physical description. It is wrong to think that the task of physics is
> to find out how nature is. Physics concerns what we can say about
> nature.\"

So in Bohr's writings the notion of a \"real physical situation\" was
just not present and he gave evasive answers to questions of the form:
\"What is really happening when \...?\" Eugene Wigner (1974) was acutely
aware of and disturbed by this evasiveness when he remarked:
\"These Copenhagen people are so clever in their use of language that,
even after they have answered your question, you still don't know
whether the answer was 'yes' or 'no'!\"

J. R. Oppenheimer, more friendly to the Copenhagen viewpoint, tried to
explain it in his lectures in Berkeley in the 1946-47 school year. Oppy
anticipated multiple valued logic when he told us: \"Consider an
electron in the ground state of the hydrogen atom. If you ask, 'Is it
moving?' the answer is 'no.' If you ask, 'Is it standing still?' the
answer is 'no'.\"

Bohr would chide both Wigner and Oppenheimer for asking ontological
questions, which he held to be illegitimate. Those who, like Einstein
(and, up till recently, the present writer) tried to read ontological
meaning into Bohr's statements, were quite unable to comprehend his
message. This applies not only to his critics but equally to his
disciples, who undoubtedly embarrassed Bohr considerably by offering
such ontological explanations as \"Instantaneous quantum jumps are real
physical events.\" or \"The variable is created by the act of
measurement.\", or the remark of Pauli quoted above, which might be
rendered loosely as \"Not only are you and I ignorant of x and p; Nature
herself does not know what they are.\"

We disagree strongly with one aspect of Bohr's quoted statement above;
in our view, the existence of a real world that was not created in our
imagination, and which continues to go about its business according to
its own laws, independently of what humans think or do, is the primary
experimental fact of all, without which there would be no point to
physics or any other science. The whole purpose of science is learn what
that reality is and what its laws are.

On the other hand, we can see in Bohr's statement a very important fact,
not sufficiently appreciated by scientists today as a necessary part of
that program to learn about reality. Any theory about reality can have
no consequences testable by us unless it can also describe what humans
can see and know. For example, special relativity theory implies that it
is fundamentally impossible for us to have knowledge of any event that
lies outside our past light cone. Although our ultimate goal is
ontological, the process of achieving that goal necessarily involves the
acquisition and processing of human information. This information
processing aspect of science has not, in our view, been sufficiently
stressed by scientists (including Einstein himself, although we do not
think that he would have rejected the idea).

Although Bohr's whole way of thinking was very different from
Einstein's, it does not follow that either was wrong. In the writer's
present view, all of Einstein's thinking -- in particular the EPR
argument -- remains valid today, when we take into account its
ontological purpose and character. But today, when we are beginning to
consider the role of information for science in general, it may be
useful to note that we are finally taking a step in the epistemological
direction that Bohr was trying to point out sixty years ago.

But our present QM formalism is not purely epistemological; it is a
peculiar mixture describing in part realities of Nature, in part
incomplete human information about Nature -- all scrambled up by
Heisenberg and Bohr into an omelette that nobody has seen how to
unscramble. Yet we think that the unscrambling is a prerequisite for any
further advance in basic physical theory. For, if we cannot separate the
subjective and objective aspects of the formalism, we cannot know what
we are talking about; it is just that simple. So we want to speculate on
the proper tools to do this.

We suggest that the proper tool for incorporating human information into
science is simply probability theory -- not the currently taught
\"random variable" kind, but the original \"logical inference\" kind of
James Bernoulli and Laplace. For historical reasons explained elsewhere
(Jaynes, 1986), this is often called \"Bayesian inference\". When
supplemented by the notion of information entropy, this becomes a
mathematical tool for scientific reasoning of such power and versatility
that we think it will require Centuries to explore all its capabilities.
But the preliminary development of this tool and testing it on simple
problems is now fairly well in hand, as described below.

A job for the immediate future is to see whether, by proper choice of
variables, the QM omelette can be seen as a kind of approximation to it.
In the 1950's, Richard Feynman noted that some of the probabilities in
quantum theory obey different rules (interference of path amplitudes)
than do the classical probabilities. But more recently Jaynes (1989) we
have found that the QM probabilities involved in the EPR scenario are
striking similar to the Bayesian probabilities, often identical; and we
interpret Bohr's reply to EPR as a recognition of this. That is, if we
read it very carefully and sympathetically, Bohr's explanation of the
EPR experiment is seen as a fairly good (albeit awkwardly phrased)
statement of Bayesian inference.

Furthermore, we know that toward the end of his life, Niels Bohr showed
an active interest in Information Theory. Therefore the omelette does
have some discernible structure of the kind that we would need in order
to unscramble it. I do not think this problem is unsolvable in principle
-- in fact, one can now see vaguely how it is going to work out -- only
nobody has yet seen how to handle the specific details.

## Probability Theory as the Logic of Science {#probability-theory-as-the-logic-of-science .unnumbered}
Let us note first an older and simpler field in which basically the same
questions and the same arguments are rampant. For some 200 years a
debate has been underway on the philosophical level, over this issue: Is
probability theory a \"physical\" theory of phenomena governed by
\"chance\" or \"randomness\"; or is it an extension of logic, showing
how to reason in situations of incomplete information? For two
generations the former view has dominated science almost completely.
More specifically, the basic equations of probability theory are the
product and sum rules: denoting by AB the proposition: \"A and B are
both true\"; and by $\bar{A}$ the proposition \"A is false\", these are
$$P(AB|C) = P(A|BC)P(B|C) = P(B|AC)P(A|C)\tag{2a}$$

$$P(A|B) + P(\bar{A}|B) = 1\tag{2b}$$

and the issue is: What do these equations mean? Are they
rules for calculating frequencies of \"random variables\", or rules for
conducting plausible inference (reasoning from incomplete information)?
Does the conditional probability symbol $P(A|B)$ stand for the frequency
with which A is true in some \"random experiment\" defined by B; or for
the degree of plausibility, in a single instance, that A is true, given
that B is true? Do probabilities describe real properties of Nature; or
only human information about Nature?

The original view of James Bernoulli and Laplace was that probability
theory is an extension of logic to the case where, because of incomplete
information, deductive reasoning by the Aristotelian syllogisms is not
available. It was sometimes called \"The calculus of inductive
reasoning.\" Laplace's great contributions to science were made with the
help of probability theory interpreted in this way.

But, starting in the mid-Nineteenth Century, Laplace's viewpoint came
under attack from Leslie Ellis, John Venn, George Boole, R. von Mises,
R. A. Fisher, M. G. Kendall, W. Feller, J. Neyman, and others down to
our own time. Their objection was always to his philosophy; none of
these critics was able to show that Laplace's methods \[application of
Eqs (2a), (2b) as a form of extended logic\] contained any inconsistency
or led to any unsatisfactory results. Whenever they seemed to find such
a case, closer examination always showed that they had only
misunderstood and misapplied Laplace's methods.

Nevertheless, this school of thought was so aggressive that it has
dominated the field almost totally in this Century, so that virtually
all probability textbooks in current use are written from a viewpoint
which rejects Laplace's interpretations and tries to deny us the use of
his methods, ignoring the success he had with them. Almost the only
exceptions are found in the works of
Harold Jeffreys (1939), Arnold Zellner (1971), and G. L. Bretthorst
(1988), which recognize the merit of Laplace's viewpoint and apply it
with the same kind of good results that Laplace found, in more
sophisticated current problems. We have written two short histories of
these matters (Jaynes, 1978, 1986), engaged in a polemical debate on
them (Jaynes, 1976), and are trying to finish a two volume treatise on
the subject, entitled \"Probability Theory -- The Logic of Science\" in
which we demonstrate that these methods are determined uniquely by some
very elementary -- and nearly inescapable -- qualitative desiderata of
consistency and rationality in plausible reasoning. Its validity is a
matter of logic, independent of all physical hypotheses. Today, in our
view, nothing in any physical science has anywhere near the fundamental
theoretical justification that Laplace's methods have.

But their basis is not only theoretical; we have today a mass of
demonstrated pragmatic results obtained from using them, fully
confirming what the theory indicates. Yet denunciations of the
\"subjectivity\" of Laplace, Jeffreys, and the writer for venturing to
use probability to represent human information; and even more of the
\"subjectivity\" of entropy based on such probabilities, often reach
hysterical proportions. It is very hard to understand why so much
emotional fervor should be aroused by these questions, since the means
to resolve them (the theoretical basis and pragmatic results of both
approaches) are already in the literature and available to all. Those
who engage in these attacks are only making a public display of their
own ignorance of recent work in this field.

But the failure of our critics to find inconsistencies or errors does
not in itself prove that our methods have any positive value for
science. Are there any new useful results to be had from using
probability theory as logic? Some are reported in the proceedings
volumes of the Annual (since 1981) MAXENT workshops; particularly the
one in Cambridge, England in August 1988, wherein our present
understanding of entropy leads to a generalized Second Law of
Thermodynamics, applied in what we think is the first quantitative
application of the second law in biology.[^4] But unfortunately, most of
the problems solvable by pencil-and-paper methods were too trivial to
put this issue to a real test; although the results never conflicted
with common sense, neither did they extend it very far beyond what
common sense could see, or what \"random variable\" probability theory
could also derive.

Only recently, thanks to the computer, has it become feasible to solve
real, nontrivial problems of reasoning from incomplete information, in
which we use probability theory as a form of logic in situations where
both intuition and \"random variable\" probability theory would be
helpless. This has brought out the facts in a way that can no longer be
obscured by arguments over philosophy. One can always argue with a
philosophy; it is not so easy to argue with a computer printout, which
says to us: \"Independently of all your philosophy, here are the facts
about what this method actually gives when applied.\"

The \"MEM\" program developed by John Skilling, Steve Gull, and their
colleagues at Cambridge University, England can maximize entropy
numerically in a space of 1,000,000 dimensions, subject to 2,000
simultaneous constraints. The \"Bayesian\" data analysis programs
developed by G. L. Bretthorst (1988) at Washington University, St.
Louis, can eliminate a hundred uninteresting parameters and give the
simultaneous best estimates of twenty interesting ones and their
accuracy; or it can take into account all the parameters in a set of
possible theories or \"models\", and give us the relative probabilities
of the theories in the light of the data. It was interesting, although
to us not surprising, to find that this leads automatically to an
improved, quantitative version of Occam's Razor: prefer the simpler
and/or more plausible theory unless the other gives a significantly
better fit to the data.

Many computer printouts have now been made at Cambridge University, of
image reconstructions in optics and radio astronomy; and at Washington
University in analysis of economic, geophysical, and nuclear magnetic
resonance data. The results were astonishing to all of us; they could
never have been found, or guessed, by hand methods.

In particular, the Bretthorst programs extract far more information from
NMR data (where the ideal sinusoidal signals are corrupted by decay)
than could the previously used fourier transform methods. No longer does
decay broaden the spectrum and obscure the information about oscillation
frequencies; the result can be orders of magnitude better resolution.
Less spectacular numerically, but equally important in principle, they
yield fundamental improvements in extracting information from economic
time series when the data are corrupted by trend and seasonality; no
longer do these obscure the information that we are trying to extract
from the data. Conventional \"random variable\" probability theory lacks
the technical means to eliminate nuisance parameters in this way.

In other words, there is no need to shout; it is now a very well
demonstrated fact that, after all criticisms of its underlying
philosophy, probability theory interpreted and used as the logic of
human inference does rather well in dealing with problems of scientific
reasoning -- just as James Bernoulli and Laplace thought it would, back
in the 18'th Century.

Our probabilities and the entropies based on them are indeed
\"subjective\" in the sense that they represent human information; if
they did not, they could not serve their purpose. But they are
completely \"objective\" in the sense that they are determined by the
information specified, independently of anybody's personality, opinions,
or hopes. It is \"objectivity\" in this sense that we need if
information is ever to be a sound basis for new theoretical developments
in science.

## How Would Quantum Theory Be Different? {#how-would-quantum-theory-be-different .unnumbered}
The aforementioned successful applications of probability theory as
logic were concerned with data processing, while the original maximum
entropy applications were in statistical mechanics, where they
reproduced in a few lines, and then generalized, the results of Gibbs.
In these applications, probability theory represented the process of
reasoning from incomplete information. There is no claim that its
predictions must be \"right\"; only that they are the best that can be
made from the information we have. They do, after all, the most that any
science could ever have pretended to do; yet some complain bitterly when
cherished illusions of \"objectivity\" are replaced by facts.

We would like to see quantum theory in a similar way; since a pure state
$\psi$ does not contain enough information to predict all experimental
results, we would like to see QM as the process of making the best
predictions possible from the information that we have when we know
$\psi$. If we could either succeed in this, or prove that it is
impossible, we would know far more about the basis of our present theory
and about future possibilities than we do today.

Einstein wanted to do something very similar; but he offered only
criticisms rather than constructive suggestions. What undoubtedly
deterred both Einstein and Schrödinger is this: one sees quickly that
the situation is more subtle than merely keeping the old mathematics and
reinterpreting it. That is, we cannot merely proclaim that all the
probabilities calculated within a QM pure state $\psi$, according to the
standard rules of our textbooks are now to be interpreted as expressions
of human ignorance of the true physical state. The results depend on the
representation in a way that makes this naive approach impossible.

For example, if we expand $\psi$ in the energy representation:
$\psi(x,t) = \sum a_n(t)u_n(x)$, the physical situation cannot be
described merely as \"the system may be in state $u_1(x)$ with
probability $p_1 = |a_1|^2$; or it may be in state $u_2(x)$ with
probability $p_2 = |a_2|^2$, and we do not know which of these is the
true state\". This would suffice to give, using classical probability
theory, the QM
predictions of quantities that are diagonal in the $\{u_n\}$
representation; but the relative phases of the amplitudes $a_n$ have a
definite physical meaning that would be lost by that approach.

Even though they have no effect on probabilities $p_n$ in the energy
representation, these phases will have a large effect on probabilities
in some other representation. They affect the predicted values of
quantities that are not diagonal in the $\{u_n\}$ representation, in a
way that is necessary for agreement with experiment. For example, the
relative phases of degenerate energy states of an atom determine the
polarization of its resonance radiation, which is an experimental fact;
so there has to be something physically real in them.[^5]

In other words, we cannot say merely that the atom is \"in\" state $u_1$
or \"in\" state $u_2$ as if they were mutually exclusive possibilities
and it is only we who are ignorant of which is the true one; in some
sense it must be in both simultaneously, or as Pauli would say, the atom
itself does not know what energy state it is in. This is the
conceptually disturbing, but experimentally required, function of the
superposition principle.

We conjecture that this is the circumstance that also deterred Niels
Bohr from making ontological statememts, and forced him to use such
cautious language. He would never say (as some of his unperceptive
disciples did) that $|a_n|^2$ is the probability that an atom is "in"
the n'th state, which would be an unjustified ontological statement;
rather, he would say that $|a_n|^2$ is the probability that, if we
measure its energy, we shall find the value corresponding to the n'th
state.

But notice that there is nothing conceptually disturbing in the
statement that a vibrating bell is in a linear combination of two
vibration modes with a definite relative phase; we just interpret the
mode (amplitudes)$^2$ as energies, not probabilities. So it is the way
we look at quantum theory, trying to interpret $|\psi|^2$ directly as a
probability density, that is causing the difficulty.

If this seems at first to be an obstacle to our purpose, it is also our
real opportunity, because it shows that the probabilities we seek, which
are to express the incompleteness of the information in a pure state in
terms of a set of mutually exclusive possibilities (call it an
"ensemble\" if you like), cannot be the usual things called
\"probability\" in the QM textbooks. The human information must be
represented in a deeper \"hypothesis space\" which contains the phases
as well as the amplitudes.

To realize this is to throw off a whole legacy of supposed difficulties
from the past; the non-classical behavior of QM probabilities pointed
out by Feynman ceases to bother us because the quantities exhibiting
that behavior will not be interpreted as probabilities in the new
hypothesis space. Likewise, the Bell inequality arguments are seen to
have very little relevance to our problem; for he was hung up on the
difficulty of getting the standard QM probabilities out of a causal
theory. But if they are not the basic probabilities after all, the
failure of a causal theory to reproduce them as probabilities might seem
rather a merit than a defect. So the clouds begin to lift, just a bit.

This is not an auspicious time to be making public announcements of
startling, revolutionary new scientific discoveries; so it is rather a
relief that we have none to announce. To exhibit the variables of that
deeper hypothesis space explicitly is a job for the future; but in the
meantime we can do a little job of housecleaning that is in any event a
prerequisite for it. We cannot hope to get our probability connections
right until we get some basic points of logic right.

The first difficulty we encounter upon any suggestion that probabilities
in quantum theory might represent human information, is the barrage of
criticism from those who believe that dispersions
$(\Delta F)^2 = \langle F^2 \rangle - \langle F \rangle^2$ represent
experimentally observable \"quantum fluctuations\" in F. Some who pose
as disciples of Bohr even claim that these fluctuations are real
physical events that take place constantly whether or not any
measurement is being made (although of course that does violence to
Bohr's position, as we have just seen). For example, at the
1966 Rochester Coherence Conference, Roy Glauber assured us that vacuum
fluctuations are \"very real things\" and that any attempts to dispense
with EM field quantization are therefore doomed to failure. It can be
reported that he was widely and enthusiastically believed.

Now in basic probability theory, $\Delta F$ represents fundamentally the
accuracy with which we are able to predict the value of F. This does not
deny that it may be also the variability seen in repeated measurements
of F; but the point is that they need not be the same. To suppose that
they must be the same is to commit an egregious form of the Mind
Projection Fallacy; the fact that our information is able to determine F
only to 5 percent accuracy, is not enough to make it fluctuate by 5
percent! To predict observable fluctuations by a correct application of
probability theory requires an entirely different calculation (Jaynes,
1978, 1983). However, it is almost right to say that, given such
information, any observed fluctuations are unlikely to be greater than 5
percent.

Let us analyze in some depth the single example of EM field
fluctuations, and show that (1) the experimental facts do not require
vacuum fluctuations to be real events after all; (2) Bayesian
probability at this point is not only consistent with the experimental
facts, it offers us some striking advantages in clearing up past
difficulties that have worried generations of physicists.

## Is Zero-Point Energy Real? {#is-zero-point-energy-real .unnumbered}
For many years we have had a strange situation; on the one hand,
\"Official\" QED has never taken the infinite ZP energy problem
seriously, apparently considering it only a formal detail like the
infinite charge density in the original hole theory, which went away
when the charge symmetry of the theory was made manifest in Schwinger's
action principle formulation.

But the ZP problem has not gone away; and on the other hand as we have
noted, there is a widespread belief that ZP fluctuations are real and
necessary to account for all kinds of things, such as spontaneous
emission, the Lamb shift, and the Casimir attraction effect. Steven
Weinberg (1989) accepted the Casimir effect as demonstrating the reality
of ZP energy, and worried about it in connection with cosmology. We know
that Pauli also worried about this and did some calculations, but
apparently never published them.

If one takes the ZP energy literally, one of the disturbing consequences
is the gravitational field it would produce. For example, if there is a
ZP energy density $W_{zp}$ in space, the Kepler ratio for a planet of
mean distance R from the sun would be changed to
$$\frac{R^3}{T^2} = \frac{G}{4\pi^2} \left[ M_{sun} + \frac{4\pi R^3}{3c^2} W_{zp} \right].\tag{3}$$

Numerical analysis of this shows that, in order to avoid conflict with
the observed Kepler ratios of the outer planets, the upper frequency
cutoff for the ZP energy would have to be taken no higher than optical
frequencies.

But attempts to account for the Lamb shift by ZP fluctuations would
require a cutoff thousands of times higher, at the Compton wavelength.
The gravitational field from that energy density would not just perturb
the Kepler ratio; it would completely disrupt the solar system as we
know it.

The difficulty would disappear if one could show that the aforementioned
effects have a different cause, and ZP field energy is not needed to
account for any experimental facts. Let us try first with the simplest
effect, spontaneous emission. The hypothesized zero-point energy density
in a frequency band $\Delta\omega$ is
$$W_{zp} = \rho_{zp}(\omega)\Delta\omega = \left( \frac{1}{2}\hbar\omega \right) \left( \frac{\omega^2}{\pi^2 c^3} \right) \Delta\omega \quad \text{ergs/cm}^3$$

Then an atom decaying at a rate determined by the Einstein A-coefficient
$$A = \frac{4\mu^2\omega_0^3}{3\hbar c^3}\tag{5}$$ where $\mu$ is the dipole
moment matrix element for the transition, sees this over an effective
bandwidth
$$\Delta\omega = \frac{\int I(\omega)d\omega}{I(\omega_0)} = \frac{\pi A}{2}$$
where $I(\omega)$ is the Lorentzian spectral density
$$I(\omega) \propto \frac{1}{(\omega - \omega_0)^2 + (A/2)^2}.$$ The
effective energy density in one field component, say $E_z$, is then
$$(W_{zp})_{eff} = \frac{1}{6}\rho_{zp}(\omega)\Delta\omega = \frac{1}{18\pi} \mu^2 \left(\frac{\omega}{c}\right)^6 \text{ergs/cm}^3\tag{8}$$
and it seems curious that Planck's constant has cancelled out. This
indicates the magnitude of the electric field that a radiating atom sees
according to the ZP theory.

On the other hand, the classical radiation reaction field generated by a
dipole of moment $\mu$:
$$E_{RR} = \frac{2}{3c^3}\frac{d^3\mu}{dt^3} = -\frac{2\omega^3}{3c^3}\mu$$
has energy density
$$W_{RR} = \frac{E_{RR}^2}{8\pi} = \frac{1}{18\pi} \mu^2 \left(\frac{\omega}{c}\right)^6 \text{ergs/cm}^3.\tag{10}$$

But (8) and (10) are identical! A radiating atom is indeed interacting
with an electric field of just the magnitude predicted by the zero-point
calculation; but this is the atom's own radiation reaction field.

Now we can see that this needed field is generated by the radiating
atom, automatically but in a more economical way; only where it is
needed, when it is needed, and in the frequency band needed. Spontaneous
emission does not require an infinite energy density throughout all
space. Surely, this is a potentially far more satisfactory way of
looking at the mechanism of spontaneous emission (if we can clear up
some details about the dynamics of the process).

But then someone will point immediately to the Lamb shift; does this not
prove the reality of the ZP energy? Indeed, Schwinger (1948) and
Weisskopf (1949) stated explicitly that ZP field fluctuations are the
physical cause of the Lamb shift, and Welton (1948) gave an elementary
"classical\" derivation of the effect from this premise.

Even Niels Bohr concurred. To the best of our knowledge, the closest he
ever came to making an ontological statement was uttered while perhaps
thrown momentarily off guard under the influence of Schwinger's famous
8-hour lecture at the 1948 Pocono conference. As recorded in John
Wheeler's notes on that meeting, Bohr says: \"It was a mistake in the
older days to be discontented with field and charge fluctuations. They
are necessary for the physical interpretation.\"

Dyson (1953) also concurred, picturing the quantized field as something
akin to hydrodynamic flow with superposed random turbulence, and he
wrote: \"The Lamb-Retherford experiment is the strongest evidence we
have for believing that our picture of the quantum field is correct in
detail." Then in 1961 Feynman suggested that it should be possible to
calculate the Lamb shift from the
change in total ZP energy in space due to the presence of a hydrogen
atom in the 2s state; and in 1966 E. A. Power gave the calculation
demonstrating this in detail. How can we possibly resist such a weight
of authority and factual evidence?

As it turns out, quite easily. The problem has been that these
calculations have been done heretofore only in a quantum field theory
context. Because of this, people jumped to the conclusion that they were
quantum effects (i.e. effects of field quantization), without taking the
trouble to check whether they were present also in classical theory. As
a result, two generations of physicists have regarded the Lamb shift as
a deep, mysterious quantum effect that ordinary people cannot hope to
understand. So we are facing not so much a weight of authority and facts
as a mass of accumulated folklore.

Since our aim now is only to explain the elementary physics of the
situation rather than to give a full formal calculation, let us show
that this radiative frequency shift effect was present already in
classical theory, and that its cause lies simply in properties of the
source field (1), having nothing to do with field fluctuations. In fact,
by stating the problem in Hamiltonian form we can solve it without
committing ourselves to electromagnetic or acoustical fields. Thus the
vibrations of a plucked guitar string are also damped and shifted by
their coupling to the acoustical radiation field, according to the
following equations.

## The Lamb Shift in Classical Mechanics {#the-lamb-shift-in-classical-mechanics .unnumbered}
Let there be n 'field oscillators' with coordinates and momenta
$\{q_i(t), p_i(t)\}$, and one 'Extra Oscillator' $\{Q(t), P(t)\}$, a
caricature of a decaying atom or plucked string; call it "the EO\". It
is coupled linearly to the field oscillators with coupling constants
$\{\alpha_i\}$, leading to a total Hamiltonian
$$H = \frac{1}{2}\sum_{i=1}^{n} (p_i^2 + \omega_i^2 q_i^2) + \frac{1}{2}(P^2 + \Omega^2 Q^2) - \sum_i \alpha_i q_i Q.\tag{11}$$

The physical effects of coupling the EO to the field variables may be
calculated in two 'complementary' ways: (I) Dynamic: How are the EO
oscillations modified by the field coupling? (II) Static: How is the
distribution of normal mode frequencies changed? The new normal mode
frequencies are the roots $\{\nu_i\}$ of the equation
$\Omega^2 - \nu^2 = K(\nu)$, where $K(\nu)$ is the dispersion function
$$K(\nu) = \sum_i \frac{\alpha_i^2}{\omega_i^2 - \nu^2} = \int_0^\infty K(t)e^{-st}dt, \quad s = i\nu.\tag{12}$$

Let us solve the problem first in the more familiar dynamical way. With
initially quiescent field modes: $q_i(0) = \dot{q}_i(0) = 0$, the decay
of the extra oscillator is found to obey a Volterra equation:
$$\ddot{Q}(t) + \Omega^2 Q(t) = \int_0^t K(t - t^\prime) Q(t^\prime)dt^\prime.\tag{13}$$ Thus
$K(t)$ is a memory function and the integral in (13) is a source field.
For arbitrary initial EO conditions $Q(0), \dot{Q}(0)$ the solution is
$$Q(t) = \dot{Q}(0)G(t) + Q(0)\dot{G}(t)\tag{14}$$ with the Green's function
$$G(t) = \frac{1}{2\pi}\int_{-\infty}^{\infty} \frac{e^{i\nu t}d\nu}{\Omega^2 - \nu^2 - K(\nu)}\tag{15}$$
where the contour goes under the poles on the real axis. This is the
exact decay solution for arbitrary field mode patterns.

In the limit of infinitely many field modes, the solution goes into a
simpler form. There is a mode density function $\rho_0(\omega)$:
$$\sum(\cdot) \rightarrow \int_0^\infty (\cdot) \rho_0(\omega) d\omega$$

Then from (12), $K(\nu)$ goes into a slowly varying function on the path
of integration (15):
$$K(\nu - i\epsilon) \rightarrow \int_0^\infty \frac{\alpha^2(\omega)\rho_0(\omega)d\omega}{\omega^2 - (\nu-i\epsilon)^2} \rightarrow -2\nu[\Delta(\nu) + i\Gamma(\nu)]\tag{16}$$
and neglecting some small terms, the resulting Green's function goes
into
$$G(t) \rightarrow \exp(-\Gamma t) \frac{\sin(\Omega + \Delta)t}{(\Omega + \Delta)}\tag{17}$$
where
$$\Gamma(\Omega) = \frac{\pi \alpha^2(\Omega)\rho_0(\Omega)}{4\Omega^2}\tag{18}$$
$$\Delta(\Omega) = \frac{1}{2\Omega} \mathcal{P} \int_0^\infty \frac{\alpha^2(\omega)\rho_0(\omega)d\omega}{\Omega^2 - \omega^2} = \frac{1}{\pi} \mathcal{P} \int_{-\infty}^\infty \frac{\Gamma(\omega)d\omega}{\omega - \Omega}\tag{19}$$
are the \"spontaneous emission rate\" and \"radiative frequency shift\"
exhibited by the EO due to its coupling to the field modes. We note that
$\Delta(\Omega)$ and $\Gamma(\omega)$ form a Hilbert transform pair, a
Kramers-Kronig type dispersion relation usually considered as expressing
causality.[^6] In this approximation, the general solution (14) becomes the
exponentially damped solution of a linear differential equation with
loss: $\ddot{Q} + 2\Gamma \dot{Q} + (\Omega + \Delta)^2 Q = 0$.

As a check, it is a simple homework problem to compare our damping
factor $\Gamma$, with the well-known Larmor radiation law, by inserting
into the above formulas the free-space mode density function
$\rho_0(\omega) = V\omega^2/\pi^2c^3$, and the coupling coefficients
$\alpha_i$ appropriate to an electric dipole of moment $\mu$
proportional to $Q$. We then find
$$\Gamma(\omega) = \left( \frac{\pi}{4\omega^2} \right) \left( \frac{\mu^2}{Q^2} 4\pi\omega^2 \right) \left( \frac{V\omega^2}{3V\pi^2c^3} \right) = \frac{\mu^2\omega^2}{3Q^2c^3} \sec^{-1}$$
and it is easily seen that for the average energy loss over a cycle this
agrees exactly with the Larmor formula
$$P_{rad} = \frac{2e^2}{3c^3} (\ddot{x})^2$$ for radiation from an
accelerated particle. In turn, the correspondence between the Larmor
radiation rate and the Einstein A-coefficient (5) is well-known textbook
material.

It is clear from this derivation that the spontaneous emission and the
radiative frequency shift do not require field fluctuations, since we
started with the explicit initial condition of a quiescent field:
$q_i = \dot{q}_i = 0$. The damping and shifting exhibited above
are due entirely to the source field reacting back on the source, as
expressed by the integral in (13).

Of course, although the frequency shift formula (19) resembles the
"Bethe logarithm\" expression for the Lamb shift, we cannot compare them
directly because our model is not a hydrogen atom; we have no s-states
and p-states. But if we use values of $\alpha_i$ and $\Omega$ for an
electron oscillating at optical frequencies and a cutoff corresponding
to the size of the hydrogen atom (that is, $\omega_{max} \approx c/a_0$,
where $a_0$ is the Bohr radius), we get shifts of the order of magnitude
of the Lamb shift. A more elaborate calculation will be reported
elsewhere.

But now this seems to raise another mystery; if field fluctuations are
not the cause of the Lamb shift, then why did the aforementioned Welton
and Power calculations succeed by invoking those fluctuations? We face
here a very deep question about the meaning of \"fluctuation-dissipation
theorems\". There is a curious mathematical isomorphism; throughout this
Century, starting with Einstein's relation between diffusion coefficient
and mobility $D = d\langle x^2 \rangle/2t = kT\mu$ and the Nyquist
thermal noise formula for a resistor
$\langle V^2 \rangle = 4kTR\Delta f$, theoreticians have been deriving a
steady stream of relations connecting \"stochastic\" problems with
dynamical problems.

Indeed, for every differential equation with a non-negative Green's
function, there is an obvious stochastic problem which would have the
same mathematical solution even though the problems are quite unrelated
physically; but as Mark Kac (1956) showed, the mathematical
correspondence between stochastic and dynamical problems is much deeper
and more general than that.

Now to get our logic straight: these relations do not prove that the
fluctuations are real; they show only that certain dissipative effects
(i.e. disappearance of the extra oscillator energy into the field modes)
are the same as if fluctuations were present. But then by the Hilbert
transform connection noted, the corresponding reactive effects must also
be the same as if fluctuations were present; the calculation of Welton
(1948) shows how this comes about.

But this still leaves a mystery surrounding the Feynman-Power
calculation, which obtains the Lamb shift from the change in total ZP
energy in the space surrounding the hydrogen atom; let us explain how
that can be.

## Classical Subtraction Physics {#classical-subtraction-physics .unnumbered}
Consider now the second, static method of calculating the effect of
field coupling. One of the effects of the EO is to change the
distribution of normal modes; the above \"free space\" mode density
$\rho_0(\omega)$ is incremented to
$$\rho(\omega) = \rho_0(\omega) + \rho_1(\omega).$$ To calculate the
mode density increment, we need to evaluate the limiting form of the
dispersion function $K(\nu)$ more carefully than in (17). From the
Hamiltonian (11), the normal modes are the roots $\{\nu_i\}$ of the
dispersion equation
$$\Omega^2 - \nu^2 = K(\nu) = \sum_i \frac{\alpha_i^2}{\omega_i^2 - \nu^2}.\tag{23}$$

K($\nu$) resembles a tangent function, having poles at the free field
mode frequencies $\{\omega_i\}$ and zeroes close to midway between them.
Suppose that the unperturbed frequency $\Omega$ of the EO lies in the
cell $(\omega_i < \Omega < \omega_{i+1})$. Then the field modes above
$\Omega$ are raised by amounts $\delta\nu_k = \nu_k - \omega_k$,
$k=i+1,i+2,\dots,n$. The field modes below $\Omega$ are lowered by
$\delta\nu_k = \omega_k - \nu_{k-1}$, $k=1,2,\dots,i$; and one new
normal mode $\nu_i$ appears in the same cell as $\Omega$:
$(\omega_i < \nu_i < \omega_{i+1})$. The separation property (exactly
one new mode $\nu_i$ lies between any two adjacent old modes $\omega_i$)
places a stringent limitation on the magnitude of any static mode shift
$\delta\nu_k$.
Thus the original field modes $\{\omega_i\}$ are, so to speak, pushed
aside by a kind of repulsion from the added frequency $\Omega$, and one
new mode is inserted into the gap thus created. If there are many field
modes, the result is a slight increase $\rho_1(\nu)$ in mode density in
the vicinity of $\Omega$. To calculate it, note that if the field mode
$\omega_i$ is shifted a very small amount to
$\nu_k = \omega_i + \delta\nu$, and $\delta\nu$ varies with $\omega_i$,
then the mode density is changed to
$$\rho(\omega) = \rho_0(\omega) + \rho_1(\omega) = \rho_0(\omega) \left[1 - \frac{d}{d\omega}(\delta\nu) + \dots \right].\tag{24}$$

In the continuum limit, $\rho_0 \rightarrow \infty$ and
$\delta\nu \rightarrow 0$; but the increment $\rho_1(\omega)$ remains
finite and as we shall see, loaded with physical meaning.

We now approximate the dispersion function $K(\nu)$ more carefully. In
(15) where Im$(\nu) < 0$, we could approximate it merely by the
integral, since the local behavior (the infinitely fine-grained
variation in $K(\nu)$ from one pole to the next) cancels out in the
limit at any finite distance from the real axis. But now we need it
exactly on the real axis, and those fine-grained local variations are
essential, because they provide the separation property that limits the
static mode shifts $\delta\nu$.

Consider the case where $\omega_i > \Omega$ and $\nu$ lies in the cell
$(\omega_i < \nu < \omega_{i+1})$. Then the modes are pushed up. If the
old modes near $\nu$ are about uniformly spaced, we have for small $n$,
$\omega_{i+n} \approx \omega_i + n/\rho_0(\omega)$, therefore
$$\omega_{i+n}^2 - \nu^2 \approx \frac{2\nu}{\rho_0}(n - \rho_0\delta\nu),$$
and the sum of terms with poles near $\nu$ goes into
$$\sum_n \frac{\alpha_{i+n}^2}{2\nu(n - \rho_0\delta\nu)} \approx \frac{\pi\alpha^2(\nu)\rho_0(\nu)}{2\nu} \cot[\pi\rho_0(\nu)\delta\nu]$$
where we supposed the $\alpha_i$ slowly varying and recognized the
Mittag-Leffler expansion $\pi\cot\pi x = \sum(x-n)^{-1}$. The
contribution of poles far from $\nu$ can again be represented by an
integral. Thus on the real axis, the dispersion function goes, in the
continuum limit, into
$$K(\nu) \approx -\frac{\pi\alpha^2\rho_0}{2\nu} \cot[\pi\rho_0(\nu)\delta\nu] + \mathcal{P}\int_0^\infty \frac{\alpha^2(\omega)\rho_0(\omega)d\omega}{\omega^2 - \nu^2}.$$

But in this we recognize our expressions (18), (19) for $\Gamma$ and
$\Delta$:
$$K(\nu) \approx -2\Omega[\Delta + \Gamma\cot(\pi\rho_0\delta\nu)].$$ As
a check, note that if we continue $\delta\nu$ below the real axis, the
cotangent goes into $\cot(-ix) \rightarrow +i$, and we recover the
previous result (16). Thus if we again assume a sharp resonance
($\Omega \approx \nu$) and write the dynamically shifted frequency as
$\omega_0 = \Omega + \Delta$, the dispersion relation (23) becomes a
formula for the static mode shift $\delta\nu$:
$$\pi\rho_0(\nu)\delta\nu = \tan^{-1}\left(\frac{\Gamma}{\nu-\omega_0}\right)\tag{29}$$
and (24) then yields for the increment in mode density a Lorentzian
function:
$$\rho_1(\nu)d\nu = \frac{1}{\pi} \frac{\Gamma d\nu}{(\nu - \omega_0)^2 + \Gamma^2}.\tag{30}$$

This is the spectrum of a damped oscillation:
$$\int_{-\infty}^\infty \rho_1(\nu)e^{i\nu t}d\nu = e^{i\omega_0 t}e^{-\Gamma|t|}$$
with the same shift and width as we found in the dynamical calculation
(13).

As a check, note that the increment is normalized,
$\int \rho_1 d\nu = 1$ as it should be, since the \"macroscopic\" effect
of the coupled EO is just to add more new mode to the system. Note also
that the result (29) depended on $K(\nu)$ going locally into a tangent
function. If for any reason (i.e. highly nonuniform mode spacing or
coupling constants, even in the limit) $K(\nu)$ does not go into a
tangent function, we will not get a Lorentzian $\rho_1(\nu)$. This would
signify perturbing objects in the field, or cavity walls that do not
recede to infinity in the limit, so echoes from them remain.

But the connection (30) between the mode density increment and the decay
law is quite general. It does not depend on the Lorentzian form of
$\rho_1(\nu)$, on the particular equation of motion for $Q$, on whether
we have one or many resonances $\Omega$, or indeed on any property of
the perturbing EO other than the linearity of its response.

To see this, imagine that all normal modes are shock excited
simultaneously with arbitrary amplitudes $A(\nu)$. Then the response is
a superposition of all modes:
$$\int A(\nu)[\rho_0(\nu) + \rho_1(\nu)]e^{i\nu t}d\nu.$$ But since the
first integral represents the response of the free field, the second
must represent the \"ringing\" of whatever perturbing objects are
present. If $A(\nu)$ is nearly constant in the small bandwidth occupied
by a narrow peak in $\rho_1(\nu)$, the resonant ringing goes into the
form (30).

Therefore, every detail of the transient decay of the dynamical problem
is, so to speak, \"frozen into\" the static mode density increment
function $\rho_1(\nu)$ and can be extracted by taking the Fourier
transform (30). Thus a bell, excited by a pulse of sound, will ring out
at each of its resonant frequencies, each separate resonance having a
decay rate and radiative frequency shift determined by $\rho_1(\nu)$ in
the vicinity of that resonance.

Then a hydrogen atom in the 2s state, excited by a sharp electromagnetic
pulse, will \"ring out\" at the frequencies of all the absorption or
emission lines that start from the 2s state, and information about all
the rates of decay and all the radiative line shifts, is contained in
the $\rho_1(\nu)$ perturbation that the presence of that atom makes in
the field mode density.

Thus Feynman's conjecture about the relation between the Lamb shift and
the change in ZP energy of the field around that atom, is now seen to
correspond to a perfectly general relation that was present all the time
in classical electromagnetic and acoustical theory, and might easily
have been found by Rayleigh, Helmholtz, Maxwell, Larmor, Lorentz, or
Poincaré in the last Century.

It remains to finish the Power-type calculation and show that, if one
wishes to do so, simple classical calculations can also be done by the
more glamorous quantum mechanical methods that Pauli dismissed as
\"subtraction physics\". Suppose we put the extra oscillator in place
and then turn on its coupling to the field oscillators. Before the
coupling is turned on we have a background mode density $\rho_0(\omega)$
with a single sharp resonance, mode density $\delta(\omega-\Omega)$
superimposed. Turning on the coupling spreads this out into
$\rho_1(\omega)$, superimposed on the same background, and shifts its
center frequency by just the radiative shift $\Delta$. In view of the
normalization of $\rho_1(\omega)$ we can write
$$\Delta = \int_0^\infty \omega\rho_1(\omega)d\omega - \Omega.\tag{32}$$

Suppose, then, that we had asked a different question: \"What is the
total frequency shift in all modes, due to the coupling?\" Before the
coupling is turned on, the sum of all mode frequencies is a badly
divergent expression:
$$(\infty)_1 = \Omega + \int_0^\infty \omega\rho_0(\omega)d\omega$$ and
afterward it is
$$(\infty)_2 = \int_0^\infty \omega[\rho_0(\omega) + \rho_1(\omega)]d\omega$$
which is no better. But then the total change in all mode frequencies
due to the coupling is, from (32): $$(\infty)_2 - (\infty)_1 = \Delta.$$
To do our physics by subtraction of infinities is an awkward way of
asking the line shift question; but it leads to the same result. There
is no longer much mystery about why Power could calculate the radiative
shift in the dynamical problem by the change in total ZP energy;
actually, he calculated the change in total frequency of all modes,
which was equal to the dynamical shift even in classical mechanics.

But some will still hold out and point to the Casimir attraction effect,
where one measures a definite force which is held to arise from the
change in total ZP energy when one changes the separation of two
parallel metal plates. How could we account for this if the ZP energy is
not real? This problem is already discussed in the literature;
Schwinger, de Raad, and Milton (1978) derive it from Schwinger's source
theory, in which there are no operator fields. One sees the effect, like
the van der Waals attraction, as arising from correlations in the state
of electrons in the two plates, through the intermediary of their source
fields (1). It does not require ZP energy to reside throughout all
space, any more than does the van der Waals force. Thus we need not
worry about the effect of ZP energy on the Kepler ratio (3) or the
cosmological constant, after all.

## Conclusion {#conclusion .unnumbered}
We have explored only a small part of the issues that we have raised;
but it is the part that has seemed the greatest obstacle to a unified
treatment of probability in quantum theory. Its resolution was just a
matter of getting our logic straight; we have been fooled by a subtle
mathematical correspondence between stochastic and dynamical phenomena,
into a belief that the \"objective reality\" of vacuum fluctuations and
ZP energy are experimental facts. With the realization that this is not
the case, many puzzling difficulties disappear.

We then see the possibility of a future quantum theory in which the role
of incomplete information is recognized: the dispersion
$(\Delta F)^2 = \langle F^2 \rangle - \langle F \rangle^2$ represents
fundamentally only the accuracy with which the theory is able to predict
the value of F. This may or may not be also the variability in the
measured values.

In particular, when we free ourselves from the delusion that
probabilities are physically real things, then when $\Delta F$ is
infinite, that does not mean that any physical quantity is infinite. It
means only that the theory is completely unable to predict F; the only
thing that is infinite is the uncertainty of the prediction. In our
view, this represents the beginning of a far more rational and
satisfactory way of looking at quantum theory, in which the important
research problems will appear entirely different than they do now.

## References {#references .unnumbered}
L. Allen & J. H. Eberly (1975), *Optical Resonance and Two-Level Atoms*,
J. Wiley & Sons, New York, Chap. 7.

G. L. Bretthorst (1988), *Bayesian Spectrum Analysis and Parameter
Estimation*, Springer Lecture Notes in Statistics, Vol. 48 (1988); G. L.
Bretthorst, C. Hung, D. A. D'Avegnon & J. H. Ackerman, \"Bayesian
Analysis of Time-Domain Magnetic Resonance Signals,\" *J. Mag. Res.*
**79**, pp. 369-376 (1988); G. L. Bretthorst, J. J. Kotyk, J. H.

Ackerman, \" $^{31}$P NMR Bayesian Spectral Analysis of Rat Brain in
Vivo,\" *Mag. Res. in Medicine*, **9**, pp. 282-287 (1989); G. L.
Bretthorst and C. Ray Smith, \"Bayesian Analysis of Signals from
Closely-Spaced Objects,\" *Infrared Systems and Components III*, R. L.
Caswell ed., SPIE Vol. **1050**, pp. 93-104 (1989).

H. G. B. Casimir (1948), Proc. K. Ned. Akad. Wet., **51**, 635 (1948).
F. J. Dyson (1953), \"Field Theory\", in *The Scientific American*,
April; p. 57.

E. T. Jaynes (1976), \"Confidence Intervals vs Bayesian Intervals\", in
*Foundations of Probability Theory, Statistical Inference, and
Statistical Theories of Science*, W. L. Harper and C. A. Hooker,
Editors; D. Reidel Pub. Co., Dordrecht-Holland. Reprinted in part in
Jaynes (1983).
------------------------------------------------------------------------
(1978), \"Where do we Stand on Maximum Entropy?\", in *The Maximum
Entropy Formalism*, R. D. Levine & M. Tribus, Eds, MIT Press, Cambridge
MA. Reprinted in (Jaynes (1983).
------------------------------------------------------------------------
(1983), *Papers on Probability, Statistics, and Statistical Physics*, R.
D. Rosenkrantz, Editor; D. Reidel Publishing Co., Holland (1983).
Reprints of 13 papers dated 1957 -- 1980. Second paperback edition by
Kluwer Academic Publishers, Dordrecht (1989).
------------------------------------------------------------------------
\(1986\) \"Bayesian Methods: General Background\", in *Maximum Entropy
and Bayesian Methods in Applied Statistics*, J. H. Justice, Ed.,
Cambridge University Press, pp 1-25.
------------------------------------------------------------------------
(1989), \"Clearing up Mysteries: The Original Goal\", in *Maximum
Entropy and Bayesian Methods*, J. Skilling, Editor, Kluwer Academic
Publishers, Holland, pp 1-27.

H. Jeffreys (1939), *Probability Theory*, Oxford Univ. Press; Later
editions 1948, 1961, 1966. A wealth of beautiful applications showing in
detail how to use probability theory as logic.

M. Kac (1956), *Some Stochastic Problems in Physics and Mathematics*,
Colloquium Lectures in Pure and Applied Science #2, Magnolia Petroleum
Company, Dallas, Texas.

P. Milonni et al (1973), \"Interpretation of Radiative Corrections in
Spontaneous Emission\", *Phys. Rev. Lett.* **31**, 958.

J. C. Polkinghorne (1989), *The Quantum World*, Princeton University
Press.

E. A. Power (1966), \"Zero-Point Energy and the Lamb Shift\", *Am. Jour.
Phys.* **34**, 516. Note that factors of 2 are missing from Equations
(13), (15).

J. Schwinger (1948), \"Quantum Electrodynamics I, II\" *Phys. Rev.*
**74**, 1439; **75**, 651.

J. Schwinger, L. L. de Raad, and K. A. Milton (1978), \"Casimir Effect
in Dielectrics\", *Ann. Phys.* **115**, 1.

I. R. Senitzky (1973), \"Radiation-Reaction and Vacuum-Field Effects in
Heisenberg-Picture Quantum Electrodynamics\", *Phys. Rev. Lett.* **31**,
955.

S. Weinberg (1989), \"The Cosmological Constant Problem\", *Revs. Mod.
Phys.* **61**, 1-24.

V. F. Weisskopf (1949), \"Recent Developments in the Theory of the
Electron\", *Revs. Mod. Phys.* **21**, 305.

T. A. Welton (1948), \"Some Observable Effects of the Quantum-Mechanical
Fluctuations of the Electromagnetic Field\", *Phys. Rev.* **74**, 1157.

E. P. Wigner (1974), \"Reminiscences on Quantum Theory\", Colloquium
talk at Washington University, St. Louis, March 27, 1974.

A. Zellner (1971), *An Introduction to Bayesian Inference in
Econometrics*, J. Wiley & Sons, Inc. Reprinted by R. Krieger Pub. Co.,
Malabar FLA (1987). The principles of Bayesian inference apply equally
well in all fields, and all scientists can profit from these analytical
solutions to real problems.

[^2]: \* Not to be confused with Schwinger's 'source theory' which is
    quite different in outlook and premises, although of course related
    to, the 'source-field theory' under discussion, in a way not yet
    entirely clear.

[^3]: † Indeed, it has long been standard practice in QED calculations
    that in the Hamiltonian for a field mode,
    $\hbar\omega(a^{\dagger}a + 1/2)$, one starts by throwing away the
    1/2, which represents the ZP energy, on the grounds that it produces
    no dynamical effects because it commutes with all other variables.
[^4]: \* This showed that the observed efficiency of muscles, long
    thought by some to be violations of the second law, are on the
    contrary derivable from the second law once it is properly
    understood.

[^5]: † When these phases are taken into account, the QM formalism has
    the physically necessary property that the polarization follows that
    of the exciting radiation, independently of the direction of our
    axis of quantization.

[^6]: † That interpretation is correct for the present classical
    dynamical problem, in which $K(t-t^\prime)$ clearly represents a physical
    causal influence. But in QED the term 'causal' has become so
    perverted in meaning that the violently anticausal Feynman
    propagator, with response outside the light cone and running
    backward in time, is called a 'causal' propagator! In effect, this
    means that the term 'causal' has become unusable.
