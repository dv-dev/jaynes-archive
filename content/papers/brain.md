---
title: "How Does the Brain Do Plausible Reasoning?"
year: 1988
abstract: >
  We start from the observation that the human brain does plausible
  reasoning in a fairly definite way. It is shown that there is only a
  single set of rules for doing this which is consistent and in
  qualitative correspondence with common sense. These rules are simply
  the equations of probability theory, and they can be deduced without
  any reference to frequencies.
  We conclude that the method of maximum-entropy inference and the use
  of Bayes' theorem are statistical techniques fully as valid as any
  based on the frequency interpretation of probability. Their
  introduction enables us to broaden the scope of statistical inference
  so that it includes both communication theory and thermodynamics as
  special cases.
  The program of statistical inference is thus formulated in a new way.
  We regard the general problem of statistical inference as that of
  devising new consistent principles by which we can translate "raw"
  information into numerical values of probabilities, so that the
  Laplace-Bayes model is enabled to operate on more and more different
  kinds of information. That there must exist many such principles, as
  yet undiscovered, is shown by the simple fact that our brains do this
  every day.
author: ["E.T. Jaynes"]
categories: ["Miscellaneous Applications & Commentary"]
tags: ["brain", "plausible reasoning", "probability theory", "maximum entropy", "Bayes' theorem"]
---
# INTRODUCTION
Shannon's theorem 2, in which the formula
$H (p_1 \dots p_n) = - \sum p_i \log p_i$ is deduced,[^1] is a very
remarkable argument. He shows that a qualitative requirement, plus the
condition that the information measure be consistent, already determines
a definite mathematical function. Actually, this is not quite true,
because he chooses the condition of consistency (the composition law) in
a particular way so as to make $H$ additive. Any continuous
differentiable function $f(H)$ for which $f^\prime(H) > 0$ would also satisfy
the qualitative requirements and a different, but equally consistent,
composition law. Thus a qualitative requirement plus the condition of
consistency determines the function $H$ only to within an arbitrary
monotonic function. The content of communication theory would, however,
be exactly the same regardless of which monotonic function was chosen.
Shannon's $H$ thus involves also a convention which leads to simple
rules of combination.

This interesting situation led the writer to ask whether it might be
possible to deduce the entire theory of probability from a qualitative
requirement and the condition that it be consistent. It turns out that
this is indeed possible. In terms of the resulting theory we are enabled
to see that communication theory, thermodynamics, and current practice
in statistical inference, are all special cases of a single principle of
reasoning.

In developing this theory we find ourselves in the fortunate position of
having all the hard work already done for us. The methodology has been
supplied by Shannon, the necessary mathematics has been worked out by
Abel[^2] and Cox[^3], and the qualitative principle was given by
Laplace[^4]. All we have to do is fit them together.

Laplace's qualitative principle is his famous remark[^4] that
\"Probability theory is nothing but common sense reduced to
calculation.\" The main object of this paper is to show that this is not
just a play on words, but a literal statement of fact.

One of the most familiar facts of our experience is this: that there is
such a thing as common sense, which enables us to do plausible reasoning
in a fairly consistent way[^5][^6]. People who have the same background
of experience and the same amount of information about a proposition
come to pretty much the same conclusions as to its plausibility. No jury
has ever reached a verdict on the basis of pure deductive reasoning.
Therefore the human brain must contain some fairly definite mechanism
for plausible reasoning, undoubtedly much more complex than that
required for deductive reasoning. But in order for this to be possible,
there must exist consistent rules for carrying out plausible reasoning,
in terms of operations so definite that they can be programmed on the
computing machine which is the human brain. This is the \"experimental
fact\" on which our theory is based. We know that it must be true,
because we all use it every day. Our direct knowledge about this process
is, however, only qualitative in much the same way as is our direct
experience of temperature. For that reason it is necessary to use the
methodology of Shannon.
# LAPLACE'S MODEL OF COMMON SENSE
We now turn to development of our first mathematical model. We attempt
to associate mental states with real numbers which are to be manipulated
according to definite rules. Now it is clear that our attitude toward
any given proposition may have a very large number of different
\"coordinates\". We form simultaneous judgments as to whether it is
probable, whether it is desirable, whether it is interesting, whether it
is amusing, whether it is important, whether it is beautiful, whether it
is morally right, etc. If we assume that each of these judgments might
be represented by a number, a fully adequate description of a state of
mind would then be represented by a vector in a space of a very large,
and perhaps indefinitely large, number of dimensions.

Not all propositions require this. For example, the proposition, \"The
refractive index of water is 1.3\", generates no emotions; consequently
the state of mind which it produces has very few coordinates. On the
other hand, the proposition, \"Your wife just wrecked your new car,\"
generates a state of mind with an extremely large number of coordinates.
A moment's introspection will show that, quite generally, the situations
of everyday life are those involving the greatest number of coordinates.
It is just for this reason that the most familiar examples of mental
activity are the most difficult ones to reproduce by a model. We might
speculate that this is the reason why natural science and mathematics
are the most successful of human activities; they deal with propositions
which produce the simplest of all mental states. Such states would be
the ones least perturbed by a given amount of imperfection in the human
brain.

The simplest possible model is one-dimensional. We allow ourselves only
a single number to represent a state of mind, and wish to discover how
much of mental activity we can reproduce subject to that limitation. For
the time being we call these numbers *plausibilities*, reserving the
term \"probability\" for a particular quantity to be introduced later.
The way in which states of mind are to be reduced to numbers is at this
stage very indefinite. For the time being we say only that greater
plausibility must always correspond to a greater number, and we assume a
continuity property which can be stated only imprecisely:
infinitesimally greater plausibility should correspond only to an
infinitesimally greater number.

We denote various propositions by letters $A, B, C, \dots$. By the
symbolic product $AB$ we mean the proposition "Both A and B are true."
The expression $(A+B)$ is to be read, "At least one of the propositions
$A, B$ is true." The plausibility of any proposition $A$ will in general
depend on whether we accept some other proposition $B$ as true. We
indicate this by the symbol
$$
(A|B) = \text{conditional plausibility of } A, \text{ given } B.
$$

Thus, for example,
$$
(AB|C) = \text{plausibility of (A and B), given C.}
$$
$$
(A+B|CD) = \text{plausibility that at least one of the propositions } A, B \text{ is true,}
$$
$$
\text{given that both } C \text{ and } D \text{ are true,}
$$
$$
(A|C) > (B|C) \text{ means that, on data } C, A \text{ is more plausible than } B.
$$

In order to find rules for manipulation of these symbols, we are guided
by two requirements:
1.  The rules must correspond qualitatively to common sense. (2-1)
2.  The rules must be consistent. This is used in two ways:
$$
\left \{
\begin{array}{l}
\text{If a result can be arrived at in more than one way,} \\\\
\text{we must obtain the same result for every possible} \\\\
\text{sequence of operations on our symbols.}
\end{array}
\right.
\tag{2-2}
$$
$$
\left \{
\begin{array}{l}
\text{The rules must include deductive logic as a special case.} \\\\
\text{In the limit where propositions become certain} \\\\
\text{or impossible in any way, every equation must reduce} \\\\
\text{to a valid example of deductive reasoning.}
\end{array}
\right.
\tag{2-3}
$$

By a successful model we mean any set of rules satisfying these
conditions. If we find that we have any freedom of choice left after
imposing them, we can exercise that freedom to adopt conventions so as
to make the rules as simple as possible. If we find that these
requirements are so restrictive that there is in effect only one
possible model satisfying them, are we entitled to claim that we have
discovered the mechanism by which the brain does \"one-dimensional\"
plausible reasoning? Except for the proviso that the human mind is
imperfect, it seems that to deny that claim would be to assert that the
human mind operates in a deliberately inconsistent way.

We now seek a consistent rule for obtaining the plausibility of $AB$
from the plausibilities of $A$ and $B$ separately. In particular, let us
find the plausibility $(AB|C)$. Now in order for $AB$ to be true on data
$C$, it is first of all necessary that $B$ be true; thus the
plausibility $(B|C)$ must be involved. If $B$ is true, it is further
necessary that $A$ be true; thus $(A|BC)$ is needed. If, however, $B$ is
false, then $AB$ is false independently of any statement about $A$.
Therefore $(A|C)$ is not needed; it tells us nothing about $AB$ that we
did not already have in $(A|BC)$. Similarly, $(A|B)$ and $(B|A)$ are not
needed; whatever plausibility $A$ or $B$ might have in the absence of
data $C$, could not be relevant to judgments of a case where we know
from the start that $C$ is true.

We could, of course, interchange $A$ and $B$ in the above paragraph, so
that knowledge of $(A|C)$ and $(B|AC)$ would also suffice. The fact that
we must obtain the same value for $(AB|C)$ no matter which procedure we
choose is one of our conditions of consistency.

Thus, we seek some function $F(x, y)$ such that
$$
(AB|C) = F [(A|BC), (B|C)]. \tag{2-4}
$$

It is easy to exhibit special cases which show that no relation of the
form $(AB|C) = F [(A|C), (B|C)]$, or of the form
$(AB|C) = F [(A|C), (A|B), (B|C)]$; could satisfy conditions (2-1),
(2-2), (2-3).

Condition (2-1) imposes the following limitations on the function
$F(x, y)$. An increase in either of the plausibilities $(A|BC)$ or
$(B|C)$ must never produce a decrease in $(AB|C)$. Furthermore,
$F(x, y)$ must be a continuous function, otherwise we could produce a
situation where an arbitrarily small increase in $(A|BC)$ or $(B|C)$
still results in the same large increase in $(AB|C)$. Finally, an
increase in either of the quantities $(A|BC)$ or $(B|C)$ must always
produce *some* increase in $(AB|C)$, unless the other one happened to
represent impossibility. Thus condition (2-1) requires that 
$$
\left \{
\begin{aligned}
& \text{$F(x, y)$ must be a continuous function, with $\left(\frac{\partial F}{\partial x}\right) \ge 0$} \\\\
& \text{and $\left(\frac{\partial F}{\partial y}\right) \ge 0$. The equality sign can apply only when} \\\\
& \text{$(A|BC)$ represents impossibility.}
\end{aligned}
\right. \tag{2-5}
$$

The condition of consistency (2-2) places further limitations on the
possible form of the function $F(x,y)$. For we can calculate $(ABD|C)$
from (2-4) in two different ways. If we first group $AB$ together as a
single proposition, two applications of (2-4) give us
$$
(ABD|C) = F [(AB|DC), (D|C)] = F \{F [(A|BDC), (B|DC)], (D|C)\}.
$$

 But
if we first regard $BD$ as a single proposition, (2-4) leads to
$$
(ABD|C) = F [(A|BDC), (BD|C)] = F [(A|BDC), F [(B|DC), (D|C)]]
$$

 Thus,
if (2-4) is to be consistent, $F(x, y)$ must satisfy the functional
equation 
$$
F [F (x,y), z] = F [x, F (y, z)]. \tag{2-6}
$$

 Conversely, it
is easily shown by induction that if (2-6) is satisfied, then (2-4) is
automatically consistent for all possible ways of finding any number of
joint plausibilities, such as $(ABCDEFG)$. This functional equation
turns out to be one which was studied by N.H. Abel.[^2] Its solution,
given also by Cox,[^3] is 
$$
p[F(x,y)] = p(x) p(y), \tag{2-7}
$$
 where
$p(x)$ is an arbitrary function. By (2-5) it must be a continuous
monotonic function. Therefore our rule necessarily has the form
$$
p[(AB|C)] = p [(A|BC)] p[(B|C)],
$$
which we will also write, for brevity, as[^7]
$$
p(AB|C) = p(A|BC) p(B|C). \tag{2-8}
$$

 The condition (2-3) above places
further restrictions on the function $p(x)$. Assume first that $A$ is
certain, given $C$. Then $(AB|C)=(B|C)$, and $(A|BC) = (A|C) = (A|A)$.
Equation (2-8) then reduces to 
$$
p(B|C) = p(A|A) p(B|C)
$$
 and this must
hold for all $(B|C)$. Therefore,
$$
\text{\textit{Certainty must be represented by $p=1$.}} \tag{2-9}
$$

 If
for some particular degree of plausibility $(A|BC)$, the function
$p(A|BC)$ becomes zero or infinite, then (2-8) says that $(B|C)$ becomes
irrelevant to $(AB|C)$. This contradicts common sense unless $(A|BC)$
corresponds to impossibility. Therefore
$$
\text{\textit{p cannot become zero or infinite}} \tag{2-10}
$$
 *for any
degree of plausibility other than impossibility.*
Now assume that $A$ is impossible, given $C$. Then
$(AB|C) = (A|BC) = (A|C)$, and (2-8) reduces to
$$
p(A|C) = p(A|C) p(B|C)
$$
 which must hold for all $(B|C)$. There are
three choices for $p(A|C)$ which satisfy this; $p(A|C) = 0$, or
$+\infty$, or $-\infty$. But by (2-9) and (2-10) the choice $-\infty$
must be excluded, for any continuous monotonic function which has the
values +1 and $-\infty$ at two given points necessarily passes through
zero at some point between them. Therefore
$$
\text{\textit{Impossibility must be represented by $p=0$, or $p = \infty$.}} \tag{2-11}
$$

Evidently the plausibility that $A$ is false is determined by the
plausibility that $A$ is true in some reciprocal fashion. We denote the
denial of any proposition by the corresponding small letter; i.e.
$$
\begin{aligned}
a &= \text{``A is false''} \\\\
b &= \text{``B is false''}
\end{aligned}
$$

 We could equally well say that $A$ = "a is false," etc.

Clearly, $(A+a)$ is always true, and $Aa$ is always false.

Since we already have some rules for manipulation of the quantities
$p(A|B)$, it will be convenient to work with $p(A|B)$ rather than
$(A|B)$. For brevity in the following derivation we use the notation
$$
[A|B] = p(A|B).
$$

Now there must be some functional relationship of the form
$$
[a|B] = S[A|B] \tag{2-12}
$$
 where by (2-1), $S(x)$ must be a
monotonic, decreasing function. Since the propositions $a$ and $A$ are
reciprocally related, we must have also 
$$
[A|B] = S[a|B]. \tag{2-13}
$$

Therefore the function $S(x)$ must satisfy the functional equation
$$
S[S(x)] = x. \tag{2-14}
$$

To find another condition which $S(x)$ must satisfy, apply (2-8) and
(2-12) alternately as follows:
$$
[AB|C] = [A|BC][B|C] = S[a|BC] [B|C] = S\left \{ \frac{[ab|C]}{[b|C]} \right \} [B|C]. \tag{2-15}
$$

The original expression $[AB|C]$ is symmetric in $A$ and $B$. So also,
therefore, is the final expression; thus
$$
[AB|C] = [A|C] S\left \{ \frac{[bA|C]}{[A|C]} \right \}. \tag{2-16}
$$

The expressions (2-15) and (2-16) must be equal whatever $A, B, C$, may
be. In particular, they must be equal when $b=AD$. But in this case,
$$
\begin{aligned}
    {[bA|C]} &= {[b|C]} = S[B|C], \\\\
    {[ab|C]} &= {[a|C]} = S[A|C].
\end{aligned}
$$

 Substituting these into (2-15) and (2-16), we see that
$S(x)$ must also satisfy the functional equation
$$
x S \left[ \frac{S(y)}{x} \right] = y S \left[ \frac{S(x)}{y} \right]. \tag{2-17}
$$

R. T. Cox[^3] has shown that the only continuous differentiable function
satisfying both (2-14) and (2-17) is 
$$
S(x) = (1-x^m)^{1/m} \tag{2-18}
$$
where $m$ is any non-zero constant. Therefore the reciprocal relation
between $[a|B]$ and $[A|B]$ necessarily has the form
$$
[A|B]^m + [a|B]^m = 1. \tag{2-19}
$$

 Suppose we represent impossibility
by $p=0$. Then, from (2-19), $m$ must be chosen positive. However, use
of different values for $m$ does not represent any freedom of choice
that we did not already have in the arbitrariness of the function
$p(x)$. The only condition on $p(x)$ is that it be a continuous
monotonic function which increases from 0 to 1 as we go from
impossibility to certainty. If the function $p_1(x)$ satisfies this
condition, so also does the function 
$$
p_2(x) = [p_1(x)]^m.
$$

 Therefore
if we write (2-19) in the form 
$$
p(A|B) + p(a|B) = 1 \tag{2-20}
$$
 in
which $p(x)$ is understood to be an arbitrary monotonic function, Eq.
(2-20) is just as general as is (2-19).

Suppose, on the other hand, that we represent impossibility by
$p = \infty$. Then we must choose $m$ negative. Once again, to say that
we can use different values of $m$ does not say anything that is not
already said in the statement that $p(x)$ is an arbitrary monotonic
function which increases from 1 to $\infty$ as we go from certainty to
impossibility. The equation
$$
\frac{1}{p(A|B)} + \frac{1}{p(a|B)} = 1 \tag{2-21}
$$
 is also just as
general as (2-19).

An entire consistent theory of plausible reasoning can be based on
(2-21) as well as on (2-20). They are not, however, different theories,
for if $p_1(x)$ satisfies (2-21), the equally good function
$$
p_2(x) = \frac{1}{p_1(x)}
$$
 satisfies (2-20), and says exactly the
same thing. If we agree to use only functions of type (2-20), we are not
excluding any possibility of representation, but only removing a certain
redundancy in the mathematics.

From (2-20) we can derive the last of our fundamental equations. We seek
an expression for the plausibility of $(A+B)$, the statement that at
least one of the propositions $A, B$ is true. Noting that if $D = A+B$,
then $d=ab$, we can apply (2-20) and (2-8) in alternation to get
$$
\begin{aligned}
p(A+B|C) &= 1 - p(ab|C) = 1 - p(a|bC)p(b|C) \\\\
&= 1 - [1 - p(A|bC)]p(b|C) = p(B|C) + p(Ab|C) \\\\
&= p(B|C) + p(A|C)[1-p(B|AC)]
\end{aligned}
$$
 or, 
$$
p(A+B|C) = p(A|C) + p(B|C) - p(AB|C). \tag{2-22}
$$

Equations (2-8) and (2-22) are the fundamental equations of the theory
of probability. From them all other relations follow.

We have found that the most general consistent rules for plausible
reasoning can be expressed in the form of the product and sum rules
(2-8) and (2-22), in which $p(x)$ is an arbitrary continuous monotonic
function ranging from 0 to 1. It might appear that different choices of
the function $p(x)$ will lead to models with different content, so that
we have found in effect an infinite number of different possible
consistent rules for plausible reasoning. This, however, is not the
case, for regardless of which function $p(x)$ we choose, when we start
to use the theory we find that it is always $p$, not $x$, that has a
definitely ascertainable numerical value. To demonstrate this in the
simplest case, consider $n$ propositions $A_1, A_2, \dots, A_n$ which
are mutually exclusive; i.e., $p(A_i A_j|C) = p(A_i|C)\delta_{ij}$. Then
repeated application of (2-22) gives the usual sum rule
$$
p(A_1 + \dots + A_n|C) = \sum_{k=1}^n p(A_k|C). \tag{2-23}
$$

 If now
the $A_k$ are all equally likely on data $C$ (this means only that data
$C$ gives us no reason to expect that one of them is more valid than the
others), and one of them must be true on data $C$, the $p(A_k|C)$ are
all equal and their sum is unity. Therefore we necessarily have
$$
p(A_k|C) = \frac{1}{n}. \tag{2-24}
$$

 This is Laplace's "Principle of
Insufficient Reason." No matter what function $p(x)$ we choose, there is
no escape from the result (2-24). Therefore, rather than saying that $p$
is an arbitrary monotonic function of $(A|C)$, it is more to the point
to say that $(A|C)$ is an arbitrary monotonic function of $p$, in the
interval $0 \le p \le 1$. It is the connection of the numbers $(A|C)$
with intuitive states of mind that never gets tied down in any definite
way. In changing the function $p(x)$, or better $x(p)$, we are not
changing our model, but just displaying the fact that our intuitive
sensations provide us only with the relation "greater than," not any
definite numbers. Throughout these changes, the numerical values of and
relations between, the quantities $p$ remain unchanged.

All this is in very close analogy with the concept of temperature, which
also originates only as a qualitative sensation. Once it has been
discovered that, out of all the monotonic functions represented by the
readings of different kinds of thermometers, one particular definition
of temperature (the Kelvin definition) renders the equations of
thermodynamics especially simple, the obvious thing to do is to
re-calibrate the scales of the various thermometers so that they agree
with the Kelvin temperature. The Kelvin temperature is no more "correct"
than any other; it is simply more convenient.

Similarly, the obvious thing for us to do at this point is to adopt the
convention $p(x)=x$, so that the distinction between a plausibility and
the quantity $p$ (which we henceforth call the *probability*)
disappears. This means only that we have found a way of calibrating our
"plausibility-meters" so that the consistent rules of reasoning take on
a simple form. The content of the theory would, however, be exactly the
same no matter what function $p(x)$ was chosen. Thus, there is only one
consistent model of common sense.

From now on, we write our fundamental rules of calculation in the form
$$
\begin{aligned}
(AB|C) &= (A|BC)(B|C) = (B|AC)(A|C) \\\\
(A+B|C) &= (A|C)+(B|C) - (AB|C).
\end{aligned} \tag{2-25, 2-26}
$$

Laplace's model of common sense consists of these rules, with numerical
values determined by the principle of insufficient reason.

Out of all the propositions which we encounter in this theory, there is
one which must be discussed separately. The proposition $X$ stands for
all of our past experience. There can be no such thing as an "absolute"
or "correct" probability; all probabilities are conditional on $X$ at
least, and $X$ is not only different for different people, but it is
continually changing for any one person. If $X$ happens to be irrelevant
to a certain question, then this observation is unnecessary but
harmless. We often suppress $X$ for brevity, with the understanding that
even when it does not appear explicitly, it is still "built into" all
bracket expressions: $(A|B)=(A|BX)$. Any probabilities conditional on
$X$ alone are called *a-priori* probabilities. In an a-priori
probability we will always insert $X$ explicitly: $(A|X)$.

It is of the greatest importance to avoid any impression that $X$ is
some sort of hidden major premise representing a universally valid
proposition about nature; it is simply whatever initial information we
have at our disposal for attacking the problem. Alternatively, we can
equally well regard $X$ as a set of hypotheses whose consequences we
wish to investigate, so that all equations may be read, "If $X$ were
true, then ..." It makes no difference in the formal theory.
# DISCUSSION
It is well known that criticism of the theory of Laplace, and pointing
out of its obvious absurdity, has been a favorite indoor sport of
writers on probability and statistics for decades. In view of the fact
that we have just shown it to be the only way of doing plausible
reasoning which is consistent and in agreement with common sense, it
becomes necessary to consider the objections to Laplace's theory and if
possible to answer them.

Broadly speaking, there are three points which have been raised in the
literature. The first is that any quantity which is only subjective,
i.e. which represents a "degree of reasonable belief," in Jeffreys'
terminology,[^8] cannot be measured numerically, and thus cannot be the
object of a mathematical theory. Secondly, there is a widespread
impression that even if this could be accomplished, a quantity which is
different for different observers is not "real," and cannot be relevant
to application.[^9] Thirdly, there is a long history of pathology
associated with this view; it is tempting and easy to misuse it.

The latter is of course not a valid objection to any theory, and we need
only answer the first two. The arguments of Sec. 2 almost answer the
first, but there remains the question of finding numerical values of
probabilities in cases where there
is no apparent way of reducing the situation to one of "equally
possible" cases. We must hasten to point out that the notion of "equally
possible" has, at this stage, nothing whatsoever to do with frequencies.
The notion of frequency has not yet appeared in the theory. Now the
question of how one finds numerical values of probabilities is evidently
an entirely different problem than that of finding a consistent
*definition* of probability, and consistent rules for calculation. In
physics, after the Kelvin temperature is defined, there remains the
difficult problem of devising experiments to establish its numerical
value. Similarly, after our model has been set up, the problem of
reducing "raw" information to a statement of probability numerical
values remains.

Most of the objections to Laplace's theory which one finds in the
literature[^11] consist of applying it to some simple problem, and
pointing out that the result flatly contradicts common sense. However,
study of these examples will show that *in every case where the theory
leads to results which contradict common sense, the person applying the
theory has additional information of some sort, relevant to the question
being asked, but not actually incorporated into the equations.* Then his
common sense utilizes this information unconsciously and of necessity
comes to a different conclusion than that provided by the theory.
Here is one of Polya's examples.[^11] A boy is ten years old today.
According to Laplace's law of succession, he has the probability
$\frac{11}{12}$ of living one more year. His grandfather is 70.

According to the same law, he has the probability $\frac{71}{72}$ of
living one more year. Obviously, the result contradicts common sense.
Laplace's law of succession, however, applies only to the case where we
have absolutely no prior information about the problem.[^13] In this
example it is even more obvious that we *do have a great deal of
additional information* relevant to this question, which our common
sense used but we did not allow Laplace's theory to use.

Laplace's theory gives the result of consistent plausible reasoning on
the basis of the information *which was put into it*. The additional
information is often of a vague nature, but nevertheless highly
relevant, and it is just the difficulty of translating it into numerical
values which causes all the trouble. This shows that the human brain
must have extremely powerful means, the nature of which we have not yet
imagined, for converting raw information into probabilities.

We can see from this why Laplace's theory was incomplete and why it will
always remain incomplete. It is simply that there is no end to the
variety of kinds of partial information with which we might be
confronted, and therefore no end to the problem of finding consistent
ways of translating that information into probability statements. Here
again there is a close analogy with physics. Whenever research involving
temperature extends into some new field, science is dependent on the
ingenuity of experimenters in devising new procedures which will give
the Kelvin temperature in terms of observed quantities. Physicists must
continually invent new kinds of thermometers; and users of probability
theory must continually invent new kinds of "plausimeters." Laplace's
theory is incomplete in the same sense, and for the same reason, that
physics is incomplete; but Laplace's basic model occupies the same
fundamental position in statistics as do the laws of thermodynamics in
physics.

The principle of insufficient reason is only one of many techniques
which one needs in current applications of probability theory, and it
needs to be generalized before it is applicable to a very wide range of
problems.[^14] In the following sections we will show two principles
available for doing this. The first has been made possible by
information theory, and the second comes from a relation between
probabilities and frequencies.

Consider now the second objection, that a probability which is only
subjective and different for different people cannot be relevant to
applications. It seems to the writer that this is the exact opposite of
the truth; *it is only a subjective probability which could possibly be
relevant to applications.* What is the purpose of any application of
probability theory? Simply to help us in forming reasonable judgments in
situations where we do not have complete information. Whether some other
person may have complete information is quite irrelevant to *our*
problem. We must do the best we can with the information we have, and it
is only when this is incomplete that we have any need for probability
theory. The only "objective" probabilities are those which describe
frequencies observed in experiments already completed. Before they can
serve any purpose in applications they must be converted into subjective
judgments about other situations where we do not know the answer.
If a communication engineer says, "The statistical properties of the
message and noise are known," he means only that he has some knowledge
about the *past* behavior of some particular set of messages and some
particular sample of noise. When he infers that some of these properties
will hold also in the future and designs a communication system
accordingly, he is making a subjective judgment of exactly the type
accounted for by Laplace's theory, and *the sole purpose of the
statistical analysis of past events was to obtain that subjective
judgment.*
Two engineers who have different amounts of statistical information
about messages will assign different n-gram probabilities and design
different coding systems. Each represents rational design on the basis
of the available information, and it is quite meaningless to ask which
is "correct." Of course, the man who has more advance knowledge about
what a system is to do will generally be able to utilize that knowledge
to produce a more efficient design, because he does not have to provide
for so many possibilities. This is in no way paradoxical, but just
simple common sense.

Similarly, if a medical researcher says, "This new medicine is effective
in 85 per cent of the cases," he means only that this is the frequency
observed in *past* experiments. If he infers that it will hold
approximately in the future, he is making a subjective judgment which
might be (and often is) entirely erroneous. Nevertheless, it was the
most reasonable judgment he could have made on the basis of the
information available. The judgment, and also its level of significance,
are accounted for by Laplace's theory. Its conclusions are, for all
practical purposes, identical with those provided by the method of
confidence intervals,[^15] and it is our contention that the validity
of the latter method depends on this agreement.
# THE PRINCIPLE OF INSUFFICIENT REASON
Two conditions are necessary before we can assign probabilities by means
of the principle of insufficient reason: 
$$
\left.
\begin{array}{l}
\text{We must be able to analyze the situation into an} \\\\
\text{enumeration of the different possibilities which} \\\\
\text{we recognize as mutually exclusive and exhaustive.}
\end{array}
\right \}
\tag{4-1}
$$
$$
\left.
\begin{array}{l}
\text{Having done this, we must then find that the} \\\\
\text{available information gives us no reason to prefer} \\\\
\text{any possibility to any other.}
\end{array}
\right \}
\tag{4-2}
$$

In practice these conditions are hardly ever met unless there is some
evident element of symmetry in the problem, as is usually the case in
games of chance. Note, however, that there are two different ways in
which condition (4--2) may be satisfied. It may be the consequence of
complete ignorance, or it may be the consequence of positive knowledge.
Suppose a person, known to be very dishonest, is going to toss a die.
Observer A is allowed to examine the die, and he has at his disposal all
the facilities of the National Bureau of Standards. He performs
thousands of experiments with scales, calipers, microscopes,
magnetometers, x-rays, neutron beams, etc., and finally is convinced
that the die is perfectly symmetrical. Observer B is not told this; he
knows only that a die is being tossed by a shady character. He suspects
that it is biased, but has no idea in which direction. Condition (4-2)
is satisfied for both, and they will both assign probability
$\frac{1}{6}$ to each face. The same probability assignment may describe
either knowledge or ignorance. This seems paradoxical: why doesn't A's
extra knowledge make any difference?

Well, it *does* make a difference, and a very important one, but the
difference requires time to "develop." Suppose that the first toss gives
a "3." To observer B this constitutes evidence that the die is biased to
favor 3, and so on the second throw B will assign different
probabilities which take this into account. Observer A, however, will
continue to assign probability $\frac{1}{6}$ to each face, because to
him the evidence of symmetry carries overwhelmingly greater weight than
does the evidence of one throw.

It is now fairly clear what will happen. To observer B, every throw of
the die represents new evidence about its bias, which causes him to
change his probability assignments for the next throw. Under certain
circumstances, his assignments are given by a generalization of
Laplace's law of succession. To observer A, the evidence of symmetry
continues to carry greater weight than does the evidence of the random
experiment, and he persists in assigning probability $\frac{1}{6}$. Each
observer has done consistent plausible reasoning on the basis of the
information available to him, and Laplace's theory accounts for the
behavior of each (Sec. 6).

This difference in behavior is not, however, accounted for by any theory
based on a frequency definition of probability, because when you define
a probability simply as a frequency you deprive yourself of any way of
saying that you *have* evidence
unless it is in the form of an observed frequency. Everything which the
National Bureau of Standards can tell us must be ignored, because it has
no frequency interpretation.
# THE ENTROPY PRINCIPLE
A biased die, colored black with white spots, has been tossed many times
onto a black table, and we have recorded the experiment with a camera,
obtaining a multiple exposure of uniform density. From the blackening of
the film we cannot determine the relative frequencies of the different
faces, but only the *average* number of spots which were on top. This
average is not 3.5, as we might expect from an honest die, but 4.5. On
the basis of this information, what are the probabilities for the
different faces?

Automobiles of make $i$ have weight $W_i$ and length $L_i$. We observe a
cluster of 1000 cars packed bumper to bumper, occupying a total length
of 3 miles. As these cars pass an intersection they go over a machine
which weighs each one and totals the result, not retaining the record of
the individual weights. Therefore we have only the total length and
total weight of the 1000 cars. What can we infer about the number of
cars of each make in the cluster?

During an earthquake, 100 windows were broken into 1000 pieces. What is
the probability for a window to be broken into exactly $m$ pieces?
These are examples of problems where condition (4-1) is satisfied but
not condition (4-2). They can be formulated in a general way as follows.
The quantity $x$ can assume the discrete values $x_1 \dots x_n$. There
are $k$ functions $f_1(x), \dots, f_k(x)$ for which we know the average
values
$$
f_r = \sum_{i=1}^n p_i f_r(x_i), \quad 1 \le r \le k. \tag{5-1}
$$

The problem is to find the $p_i$. If $k < (n-1)$, there are not enough
conditions to determine the $p_i$ in the sense of a mathematical
solution of (5-1) and $\sum p_i = 1$. We cannot use the principle of
insufficient reason because we have too much information; there *are*
reasons for preferring some possibilities to others. There are many
probability assignments which would all agree with the available
information. Which is the most reasonable one to adopt?

Consider the third example above, and restate it as: the average window
is broken into 10 pieces. If we were to conclude that *each* window is
broken into 10 pieces, this would be in complete agreement with all the
available information. However, our common sense tells us that it would
not be a *reasonable* probability assignment; we would be assuming far
more than was given in the statement of the problem. It is more
reasonable to assign probability $p_m = \frac{1}{5}$ for a window to be
broken into $m$ pieces, where $m=8,9,10,11,12$. But this still assumes
more than was warranted by the given information. It says, for example,
that it is impossible for a window to be broken into 13 pieces.

Evidently we regard a broad distribution as more reasonable than a
sharply peaked one, and there is no value of $m$ for which we would be
justified in assigning $p_m=0$.

To make a long story short, we want the probability assignment which
assumes *nothing* beyond what was given in the statement of the problem.
Shannon's theorem 2 tells us that the consistent measure of the 'amount
of uncertainty' in a probability distribution is its entropy and
therefore we must choose the distribution which has maximum entropy
subject to the constraints (5-1). Any other distribution would represent
an arbitrary assumption of some kind of information which was not given
to us. The maximum-entropy distribution is "maximally noncommittal" with
respect to missing information.

The solution follows immediately from the method of Lagrangian
multipliers, by arguments which are very well known in a different
context. The results are expressed compactly if we define the *partition
function*:
$$
Z(\lambda_1 \dots \lambda_k) = \sum_{i=1}^n \exp [-\lambda_1 f_1(x_i) - \dots - \lambda_k f_k(x_i)]. \tag{5-2}
$$

Then the maximum-entropy distribution is
$$
p_i = \exp [-\lambda_0 - \lambda_1 f_1(x_i) - \dots - \lambda_k f_k(x_i)] \tag{5-3}
$$
with the $\lambda_r$ determined by 
$$
\lambda_0 = \log Z, \tag{5-4}
$$
 and
$$
\langle f_r(x) \rangle = -\frac{\partial}{\partial \lambda_r} \log Z, \quad 1 \le r \le k. \tag{5-5}
$$

At first glance it seems idle and trivial that we should have to do all
this in order to learn how to say nothing. The important point, however,
is that we have here found a consistent way of saying nothing in a new
language; the language of probability theory. The triviality fades away
entirely when we notice that the problem of inferring the macroscopic
properties of matter from the laws of atomic physics is of exactly the
type we are considering. *All of thermodynamics, including the
prediction of every experimentally reproducible feature of irreversible
processes, is contained in the above solution.*[^16][^17][^18]

This is so easy to demonstrate that we will sketch the argument here. In
any macroscopic experiment the exact microscopic state of a system is
never under control or observation; there will be perhaps
$$
10^{10^{20}} = \left(10^{10^{10}}\right)^{10^{10}}
$$
 different quantum
states compatible with a given set of experimental conditions. Although
the microscopic state is changing rapidly, the time required for any
reasonably complete "sampling" of so many states is still rather long;
perhaps $10^{10^{10}}$ years. When we repeat the experiment we will
surely not repeat the microscopic state. Therefore, any property which
is experimentally reproducible must be characteristic of *each* of the
great majority of the class $C_e$ of microscopic states allowed
by the experimental conditions. This is not necessarily the same as the
*subjective* class $C_s$ consisting of all reasonably probable states in
the maximum-entropy distribution.[^19] Clearly, the only properties
which we will be able to predict definitely from the maximum-entropy
distribution will be those characteristic of the great majority of the
states in class $C_s$.

Now if it is found that the class $P_s$ of properties predictable by
maximum-entropy inference is identical with the class $P_e$ of
experimentally reproducible properties, the theory is entirely
successful. This would by no means imply that the class $C_s$ is
identical with the class $C_e$. If, however, the class $P_s$ is found to
differ in any way from the class $P_e$, we would be forced to conclude
that $C_s \neq C_e$. But this could be true only if there exist new
physical states, or new constraints on the possible physical states,
which we did not take into account in our initial numeration.

Therefore, strictly speaking, we should not assert that maximum-entropy
inference *must* lead to correct predictions. But we can assert
something even more important: *if the class of predictable properties
is found to differ in any way from the class of experimentally
reproducible properties, that fact would in itself demonstrate the
existence of new laws of physics*. Assuming that this occurs and the new
laws are eventually worked out, then maximum-entropy inference based on
the new laws will again have this property.

From this we see that maximum-entropy inference is precisely the
appropriate tool for reasoning from the microscopic to the macroscopic.
Its characteristic property is that it does not allow us to form any
conclusions which are not indicated by the available evidence. Any other
distribution would permit one to draw conclusions not warranted by the
evidence.

Historically, maximum-entropy inference was discovered, in its
mathematical aspects, by Boltman about 1870, and greatly advanced by
Gibbs around 1900. The result is what the physicist calls statistical
mechanics. However, the *interpretation* of the mathematical rules has
always been a subject of great confusion, because of the illusion that
probabilities must be given a frequency interpretation. This made it
appear that the rules could be justified only by demonstrating a certain
physical property called ergodicity, or in modern terms, metric
transitivity. All attempts to demonstrate this have, however, failed.
Until the discovery of Shannon's theorem 2, it was not possible to
understand just what we were doing in statistical mechanics, or to have
any confidence in it for the prediction of irreversible processes.
However, we can now see that statistical mechanics is a much more
powerful tool than physicists had realized.
# PROBABILITY AND FREQUENCY
Although the word "frequency" has appeared a few times above, we have
not so far made any use of it in developing the basic theory or in
demonstrating its application to thermodynamics. This has been done
deliberately in order to emphasize the fact that the notions of
probability and frequency are entirely distinct. Many of the most
important applications of probability theory can be justified and
carried to completion without ever introducing the notion of frequency.
However, in
cases where a random experiment provides most or all of the available
information, there should exist some relationship between the observed
frequency of the event and the probability which we assign to it.
Similarly, if an event can be regarded as a possible result of a random
experiment, there may in some cases be a relation between the
probability which we assign to it, and the relative frequency with which
we expect it to occur. Such relations must, of course, be deduced from
the theory and not postulated.

To demonstrate the latter relation, we introduce the propositions
$$
A_p = \text{``The probability of A in each case is p.''} \tag{6-1}
$$
$$
N_n = \text{``In N trials, A was (or will be) true n times.''} \tag{6-2}
$$

The probability $(N_n|A_p)$, obtained immediately from
the sum and product rules (2-25), (2-26), is the binomial distribution
$$
(N_n|A_p) = \binom{N}{n} p^n (1-p)^{N-n} \tag{6-3}
$$

 As a function of
$n$, this attains a maximum value when $n$ is within one unit of $Np$,
so that the most probable frequency is substantially equal to the
probability.

Note that the phrase "in each case," in (6-1) is essential. To
demonstrate this, we look more closely at the derivation of (6-3) from
our basic rules. Define the proposition
$$
B_n = \text{``A is true in the n'	ext{-th} trial.''} \tag{6-4}
$$

 Now
according to (2-25) we have 
$$
(B_2 B_1|A_p) = (B_2|B_1 A_p)(B_1|A_p)
$$
which reduces to 
$$
(B_2|A_p)(B_1|A_p) = p^2
$$
 only if
$(B_2|B_1 A_p) = (B_2|A_p)$; i.e. the probability of $A$ at the second
trial which is involved in (6-3) is that based on $A_p$ and knowledge of
the result of the first trial. It is equal to $p$, as assumed in (6-3),
only if knowing the result of the first trial would have given us no
reason to change the assignment. This in spite of the fact that in (6-3)
we are predicting a frequency entirely on the basis of $A_p$, since only
$A_p$ appears to the right of the vertical stroke. Even though we are
not given the results of any trial, the expected frequency still depends
on whether such knowledge would have been relevant.

This again corresponds to common sense. To take the most extreme case,
suppose we are tossing a coin and $A$ stands for "heads." Let it be a
very dishonest coin, and define the proposition 
$$
\begin{aligned}
C_p ={} & \text{``The coin has either two heads or two tails,} \\\\
& \text{and the probability of the former is p.''}
\end{aligned} \tag{6-5}
$$

Now on the basis of this evidence alone, it is still true that the
probability of "heads" in each particular throw is $p$. But no one
expects the relative frequency of heads to be $p$: We now have
$(B_2|B_1 C_p)=1$, so that
$$
(B_2 B_1|C_p) = (B_2|B_1 C_p)(B_1|C_p) = p
$$
 and by repeated
applications of (2-25), we find that the only sequences of $N$ throws
which do not have probability zero, correspond to 
$$
\begin{aligned}
(B_N \dots B_2 B_1|C_p) &= p \\\\
(b_n \dots b_2 b_1|C_p) &= 1-p
\end{aligned}
$$
 so that in place of (6-3) we have
$$
(N_n|C_p) = p \delta(n,N) + (1-p)\delta(n,0), \tag{6-6}
$$
 which is
exactly what our common sense told us without any calculation.

This shows that *before we can infer any definite frequency from a
probability assignment, the evidence on which that probability
assignment is based must be very good evidence indeed*. It corresponds
to that possessed by the man from the Bureau of Standards in the dice
game of Section 3. In order for (6-3) to hold, the evidence on which
$A_p$ is based must carry overwhelmingly more weight than does the
evidence of $N$ throws. For this reason, the probabilities obtained from
maximum-entropy inference have no reasonable frequency interpretation,
and we can see why statistical mechanics was so confusing as long as we
tried to interpret it this way.[^18] Now introduce the proposition,
$$
D_f = \text{``In an infinitely long sequence of trials, the relative frequency of A approaches f.''} \tag{6-7}
$$

In the limit as $N \to \infty$, the binomial distribution becomes
infinitely sharp, and so we obtain the Dirac delta- function[^20]
$$
(D_f|A_p) = \delta(f-p). \tag{6-8}
$$

 Equation (6-8) is loaded with
logical booby-traps, which we must hasten to point out. Note first that
it by no means says that the relative frequency $f=p$ *must* occur. It
says only that, on the basis of the information which led to the
assignment $A_p$, this is the only relative frequency which it is
reasonable to expect; the available evidence gives no support at all to
any other value. The probability (6-8) is still only a subjective
quantity.

Equation (6-8) represents a limiting case which can never be justified
in practice, because in order for (6-3) to continue to hold as
$N \to \infty$, the evidence on which $A_p$ is based must carry
overwhelmingly more weight than do the results of
an infinite number of trials. Not even the Bureau of Standards can
provide us with evidence this good.

But there is still a paradox here. Suppose that the evidence $A_p$ was
perfectly reliable. It would still represent only partial information
about the random experiment. According to (6-8), the probability that
the limiting frequency lies in the interval
$(p-\epsilon) < f < (p+\epsilon)$ is
$$
\int_{p-\epsilon}^{p+\epsilon} (D_f|A_p) df = 1; \tag{6-9}
$$
 i.e., $f$
was *certain*, on data $A_p$, to lie in this interval. How could we have
been certain of *anything* on the basis of only partial information? How
could we have been certain that a limiting frequency even exists?
Well, Eq (6-8) is actually a logical contradiction, but a useful one. We
have asked the theory a foolish question, and it has given us a foolish
answer. Equation (6-8) refers only to an infinite number of trials. If
$N$ is finite, there is no $n$ in $0 \le n \le N$ for which
$(N_n|A_p) = 0$. We are not certain of the result of *any possible*
experiment. It is only when the experiment is *impossible* that we can
be certain of the result! Any attempt to define a probability as the
limit of a frequency is evidently subject to the same logical
difficulty, but in a much more acute form, because there is no way at
all of avoiding it.

In spite of this, (6-8) is useful if we understand how to use it. If $N$
is large and the supporting evidence $A_p$ fairly good, it may be a
perfectly valid approximation to (6-3) for some purposes, and it will
then lead to simpler formulas than would (6-3).

Equation (6-8) can also be used in a different way. If we *had* evidence
about limiting frequencies, that evidence would be equivalent to a
perfectly reliable assignment $A_p$. Thus, if $E$ is any proposition,
and $A_p$ is perfectly reliable so that (6-8) holds, we would have
$$
(E|D_f) = (E|A_p), \quad f=p.
$$

 In particular,
$$
(N_n|D_f) = \binom{N}{n} f^n (1-f)^{N-n} \tag{6-10}
$$
 which is the
form used in the frequency theory.

The inverse problem, of inferring a probability from an observed
frequency, is much more difficult. The quantity which we have here to
evaluate is $(B_{N+1}|N_n X)$, where we denote, as in Sec. 2, the prior
evidence by $X$. It does not seem possible to carry out this calculation
once and for all in the most general case, because the prior evidence
might provide intricate relations between the probabilities at different
trials, in an infinite number of different ways. The order in which "A
true" and $a$ = "A false" occurred would in general be relevant to the
probability of $B_{N+1}$, but the above notation implies that we are not
going to consider that evidence.

The only case which the frequency school of thought can treat is the one
where we ignore completely all the prior evidence; the frequency school
regards a-priori probabilities as nonsense. This simplifies our problem,
because it is only that case that we need to exhibit here in order to
establish the relation between the frequency theory and Laplace's
theory. In other words, the prior evidence $X$ is now to tell us nothing
whatsoever. We have, from (2-25) and (2-26),
$$
(B_{N+1}|N_n) = \int_0^1 (B_{N+1} D_f | N_n) df = \int_0^1 (B_{N+1}|D_f N_n)(D_f|N_n) df. \tag{6-11}
$$

Also, by (2-25),
$$
(D_f|N_n) = (D_f|X) \frac{(N_n|D_f)}{(N_n|X)}. \tag{6-12}
$$

 The
a-priori probabilities $(D_f|X)$ and $(N_n|X)$ must now say nothing
about the values of $f$ or $n$. The consistent way of saying this is,
from the principle of maximum entropy,
$$
(D_f|X)=1; \quad (N_n|X) = \frac{1}{N+1} \quad 0 \le n \le N.
$$

Furthermore, the evidence $D_f$ carries overwhelmingly more weight than
does $N_n$, so that 
$$
(B_{N+1}|D_f N_n) = (B_{N+1}|D_f) = f.
$$

Substituting these results and (6-10) into (6-11), we have
$$
(B_{N+1}|N_n) = (N+1)\binom{N}{n} \int_0^1 f^{n+1}(1-f)^{N-n} df = \frac{n+1}{N+2}, \tag{6-13}
$$
which is Laplace's law of succession. If $N$ is sufficiently large, the
probability which we assign to $A$ at the next trial is substantially
equal to its observed frequency in the previous trials.

From these results we conclude that the general relation between the two
theories is the following. Whenever all of the available evidence
consists of observed frequencies, the conclusions obtained from the
frequency theory approach those given by Laplace's theory asymptotically
as the number of observations increases. If we have additional evidence
not expressible in terms of frequencies, the conclusions of the theories
may differ widely, and it is Laplace's theory which will agree with
common sense.

As a simple example of this, suppose that two observers listen to a
geiger counter, known by both to have an efficiency of 10 per cent.
$O_1$ has no knowledge about the source of the particles being counted.
$O_2$ knows that the source is a radioactive sample of long lifetime, in
a fixed position. He does not know anything about its strength except,
of course, that it is not infinite. During the first minute, 10 counts
are registered. $O_1$ infers, by maximum-likelihood, that about 100
particles actually passed through the counter, and $O_2$ agrees. During
the second minute, 16 counts are registered. $O_1$ infers that about 160
particles were present, and he does
not change his estimate for the first minute. $O_2$, using Bayes'
theorem, concludes that the most probable value is only 137, and he
revises his estimate for the first minute to 123. Each has done
consistent plausible reasoning, but *prior evidence which has no
frequency interpretation can completely change the conclusions which we
draw from random data, and their degree of reliability*.
# \"SUBJECTIVE\" COMMUNICATION THEORY
Laplace's theory is of such wide scope that in principle it includes
every example of plausible reasoning, and thus *a fortiori*,
communication theory. In particular, much of communication theory can be
regarded as an application of maximum-entropy inference. This viewpoint
may or may not lead to new mathematical results unlikely to be found
without it. However, the conditions for validity of some known results
can be extended. Also, it clarifies a constantly recurring question:
what parts of communication theory describe measurable properties of
messages, and what parts describe only the state of knowledge of some
observer?

The current tendency is to state and prove theorems using the frequency
terminology. Mathematical properties needed for the proof must then be
regarded as objective properties of the messages or noise, and this
makes it appear that the theorem is valid only if these properties can
be demonstrated as "true." For example, Shannon's proofs of theorems
often "assume the source to be ergodic so that the strong law of large
numbers can be applied." But how are we to decide whether a source is
"really" ergodic? What measurements could we perform on it? Ergodicity
has a precise frequency interpretation only for behavior over infinite
periods of time. From an operational viewpoint it is therefore
meaningless. How, then, can we ever trust the result of the theorem?
If we look at the problem in Laplace's way this difficulty disappears.
When we say, "The source is ergodic," we are not describing the source,
but rather our state of knowledge about the source. We mean only that
nothing in the available evidence leads us to expect that it has a
sub-class of states in which it can get stuck. *As far as we know*,
there is always a possible route by which it can get from any state to
any other.

Whether or not this is actually true is irrelevant for the use we make
of the theorem. Our job, again, is only to do the best we can with the
information we have, and it would be quite unjustified to assume an
invariant sub-class of states unless we have evidence to support this.
It could, for example, lead to design of a communication system which
turns out to be incapable of handling the actual messages. Ergodicity of
this subjective kind is a consequence only of our being conservative and
avoiding unwarranted assumptions; the resulting probabilities are the
ones which maximize the entropy subject to whatever we *do* know.
Exactly the same argument applies to ergodicity in statistical
mechanics.

Many of the fundamental theorems of communication theory can be
reinterpreted in this way, and we then see that they are valid and
useful in far more general conditions than one would suppose from the
frequency definition of probability.

Consider an observer $O_n$ who knows in advance the n-gram frequencies
which a
source is going to generate, but has no other knowledge about it, what
communication system represents rational design on the basis of this
much knowledge, what is the best way of encoding into binary digits for
the noiseless case, and what channel capacity does $O_n$ require? In
principle, the answer is always the same; we need to find the
probabilities $p(M)$ which $O_n$ assigns to each of the conceivable
messages, and use the method of Fano and Shannon.[^21]

We wish to emphasize that it makes no sense whatever to say that there
exists a "correct" distribution $p(M)$ for this problem; $p(M)$ is an
entirely subjective quantity. This becomes especially clear if we
suppose that only a single message is ever going to be sent over the
communication system, but we wish to transmit it as quickly as possible.
Thus there is no conceivable procedure by which $p(M)$ could be
measured. This would in no way affect the problem of engineering design
which we are considering.

In choosing a distribution $p(M)$, it would by possible to assume a
particular message structure beyond $n$ symbols. But from the standpoint
of $O_n$ this could not be justified, for *as far as he knows*, an
encoding system based on any such structure is as likely to hurt as to
help. From $O_n$'s standpoint, rational conservative design consists in
carefully *avoiding* any such assumption. This means, in short, that
$O_n$ should choose the distribution $p(M)$ by maximum-entropy inference
based on the known n-gram frequencies.[^22] For $O_1$ and $O_2$ the
solution is well known in a different context; the physicist calls them
the linear Ising chain with no interactions, and with nearest-neighbor
interactions respectively.[^23]

Laplace's point of view is helpful also in the problem of detecting a
radar signal in noise. Anyone who studies this problem comes to the
conclusion that there is no way of evading the notion of a-priori
probabilities of different signals. They are an essential part of the
problem, because any prior knowledge we have about the signal is
extremely relevant to the proper engineering design. The question of how
one finds their "true" numerical values then becomes quite embarrassing.
They can be given a frequency interpretation only by devices so
arbitrary and forced that they could have no relevance to the problem.
We can now see the answer to this. In the first place, *no one needs to
apologize for, or do any cautious egg-walking around, the use of Bayes'
theorem and a-priori probabilities*. This is in fact the only consistent
way of handling the problem. We have at present no known procedure for
translating our prior knowledge about signals into numerical values of
probabilities. At least not on paper. But we still have our brains, and
until new principles are discovered, we will have to use them. We must
take into account everything we know about the signal, and then *guess*
the a-priori probabilities.
# CONCLUSION
We have tried to show above how a re-interpretation of the probability
concept can clarify and extend the power of statistical methods for
current applications in science and engineering. Laplace's view of
probability theory as the symbolic logic of plausible reasoning enables
us to follow the process which our brains must be
using, in every case where numerical values of probabilities can be
found. It enables us to do this in far greater detail than is possible
on the frequency theory, and to take into account additional evidence
which cannot even be stated in terms of frequencies.

The analysis of Sec. 2 above is, of course, far from rigorous in the
modern sense of the term. However, I believe that all the necessary
epsilons and deltas can be supplied by anyone sophisticated enough to
feel the need for them. There is always a danger that too much
generality will obscure the important points of an argument. Finally, it
is interesting to note the increasing importance of the theory of
functional equations in this field, shown also by Bellman and
Kalaba.[^24]
# REFERENCES {#references .unnumbered}
[^1]: C.E. Shannon, "A Mathematical Theory of Communication," Bell Syst. Tech. Jour. Vol. 27, pp. 379-423, 623-655; July, October, 1948. Also in C. E. Shannon and W. Weaver, "The Mathematical Theory of Communication," University of Illinois Press, Urbana, 1949.
[^2]: N. H. Abel, *Crelle's Jour.*, Bd. 1 (1826).
[^3]: R. T. Cox, "Probability, Frequency, and Reasonable Expectation," *American Journal of Physics*. Vol. 14, p. 1 (1946). This is a very important, but unfortunately little-known, paper which comes quite close to solving the problem of Sec. 2.
[^4]: "La théorie des probabilités n'est que le ben sens reduit au calcul." This occurs in the Introduction to P.S. Laplace, "Exposition de la théorie des chances at des probabilités," Paris, 1843. The same statement, with slightly different wording, is found in the Truscott-Emory translation of P.S. Laplace, "A Philosophical Essay on Probabilities," Dover Publications, N. Y. (1951), p. 196.
[^5]: G. Polya, "Mathematics and Plausible Reasoning," Volumes I and II, Princeton University Press, 1954.
[^6]: G. Polya, "How to Solve It," Princeton University Press, 1945; Second paper-bound edition by Doubleday Anchor Books, Inc., Garden City, N.Y., 1957.
[^7]: This notation is perhaps confusing. It can be made clearer if we suppose that the symbol for a plausibility is not $(A|B)$, but just $AB$, the parentheses being unnecessary. However, when one writes down more involved equations, the absence of parentheses can cause even greater confusion. The notation adopted here, while not entirely consistent, appears to the writer as the lesser of two evils.
[^8]: H. Jeffreys, "Theory of Probability," Oxford University Press, 1939.
[^9]: This is not a direct quotation from any particular author, but a statement of what is implied by many authors. For example, see Ref. 10, pp. 150-151, or Ref. 12, pp 4-6.
[^10]: H. Cramér, "Mathematical Methods of Statistics," Princeton University Press, 1946.
[^11]: Reference 5, Vol. II, p. 136. For other examples, see Ref. 8, pp. 107-110, and Ref. 12, p. 64.
[^12]: W. Feller, "An Introduction to Probability Theory and its Applications," John Wiley and Sons, Inc., N.Y., 1950. Any reader familiar with this book will see at once that the present paper is largely a reaction against and search for an alternative to, the philosophical views expressed therein. I believe this is necessary if probability theory is to meet all the needs of science and and engineering. But no one can challenge Feller's beautiful mathematical results, the validity of which does not depend on how we choose to interpret them. They are as useful in Laplace's theory as in the frequency theory.
[^13]: This is far from being a precise statement. The derivation of Eq. (6-13) shows in more detail what is required for the law of succession to apply.
[^14]: However, it served Laplace very well indeed. The following procedure led him to some of the most important discoveries in celestial mechanics. Noting a discrepancy between observation and existing theory, he would break down the situation into alternatives which seemed intuitively "equally possible." He would then compare the probability that a discrepancy of this size is due to a systematic effect, with the probability that it is due to errors of observation. Whenever the ratio was sufficiently high, he would decide that this is a problem worth working on, and attack it. He was, in fact, using Wald's decision theory, in exactly the way developed recently by Middleton, van Meter, and others for the detection of signals in noise.
[^15]: Ref. 10, pp. 507-524.
[^16]: E. T. Jaynes, "Information Theory and Statistical Mechanics," *Physical Review*, Vol. 106, pp. 620-630; May 15, 1957. At the time of writing this, I was under the impression that the frequency theory and Laplace's theory are parallel, co-equal theories using the same mathematical rules. However, the arguments of the present paper show that the frequency theory is only a special case of Laplace's theory.
[^17]: E.T. Jaynes, "Information Theory and Statistical Mechanics II," Submitted to the *Physical Review*.
[^18]: E. T. Jaynes, "Poincaré Recurrence Times and Statistical Mechanics," Submitted to the *Physical Review*.
[^19]: This can be stated in a more precise epsilon-delta language, but the reader will anticipate that the conclusions are largely independent of what we mean by "reasonably probable," for the same reason as in Shannon's theorem 4.
[^20]: $(D_f|A_p)$ is a probability density, $(D_f|A_p)df$ being a probability. Since, however, the differentials cancel out of equations and the distinction is already determined by whether the variable is continuous or discrete, there is no need to invent a new notation. On the other hand, it is essential in this theory that we do distinguish in notation between a probability and a frequency.
[^21]: **[REFERENCE MISSING: Method of Fano and Shannon]**
[^22]: **[REFERENCE MISSING: Maximum-entropy inference based on n-gram frequencies]**
[^23]: **[REFERENCE MISSING: Linear Ising chain]**
[^24]: **[REFERENCE MISSING: Theory of functional equations, Bellman and Kalaba]**
[^100]: Present address: Wayman Crow Professor of Physics, Washington University, St. Louis. MO 63130
