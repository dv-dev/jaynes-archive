---
title: "Use of Jacobians in Thermodynamics"
author: ["E.T. Jaynes"]
year: 1965
---
Many students find that thermodynamics, although mathematically almost
trivial, is nevertheless one of the most difficult subjects in their
program. A large part of the blame for this lies in the extremely
cumbersome partial derivative notation. In this chapter we develop a
different mathematical scheme, with which thermodynamic derivations can
be carried out more easily, and which gives a better physical insight
into the meaning of thermodynamic relations.
## Statement of the Problem {#statement-of-the-problem .unnumbered}
In fields other than thermodynamics, one usually starts out by stating
explicitly what variables shall be considered the independent ones, and
then uses partial derivatives without subscripts, the understanding
being that all independent variables other than the ones explicitly
present are held constant in the differentiation. This convention is
used in most of mathematics and physics without serious
misunderstandings. But in thermodynamics, one never seems to be able to
maintain a fixed set of independent variables throughout a derivation,
and it becomes necessary to add one or more subscripts to every
derivative to indicate what is being held constant. The often-needed
transformation from one constant quantity to another involves the
relation
$$
\left(\frac{\partial A}{\partial B}\right)_C = \left(\frac{\partial A}{\partial B}\right)_D + \left(\frac{\partial A}{\partial D}\right)_B \left(\frac{\partial D}{\partial B}\right)_C
$$
which, although it expresses a fact that is mathematically trivial,
assumes such a complicated form in the usual notation that few people
can remember it long enough to write it down after the book is closed.
As a further comment on notation, we note that in thermodynamics as well
as in mechanics and electrodynamics, our equations are made cumbersome
if we are forced to refer at all times to some particular coordinate
system (i.e., set of independent variables). In the latter subjects this
needless complication has long since been removed by the use of vector
notation, which enables us to describe physical relationships without
reference to any particular coordinate system. A similar house-cleaning
can be effected for thermodynamics by use of jacobians, which enable us
to express physical relationships without committing ourselves to any
particular set of independent variables.

We have here an interesting example of retrograde progress in science:
for the historical fact is that use of jacobians was the original
mathematical method of thermodynamics. They were used extensively by the
founder of modern thermodynamics, Rudolph Clausius, in his work dating
from about 1850. He used the notation
$$
D_{xy} = \frac{\partial^2 Q}{\partial x \partial y} - \frac{\partial^2 Q}{\partial y \partial x}
$$
where Q stands, as always, for heat, and x, y are any two thermodynamic
quantities. Since dQ is not an exact differential, $D_{xy}$ is not
identically zero. It is understandable that this notation, used in his
published works, involved Clausius in many controversies, which in
retrospect appear highly amusing. An account of some of them may be
found in his book (Clausius, 1875). On the other hand, it is unfortunate
that this occurred, because it is probably for this reason that the
quantities $D_{xy}$ went out of general use for many years, with only
few exceptions (See comments at the end of this chapter). In a footnote in Chapter II of Planck's famous treatise (Planck, 1897), he
explains that he avoids using dQ to represent an infinitesimal quantity
of heat, because that would imply that it is the differential of some
quantity Q. This in turn leads to the possibility of many fallacious
arguments, all of which amount to setting $D_{xy} = 0$. However, a
reading of Clausius' works makes it clear that the quantities $D_{xy}$,
when properly used, form the natural medium for discussion of
thermodynamics. They enabled him to carry out certain derivations with a
facility and directness which is conspicuously missing in most recent
expositions. We leave it as an exercise for the reader to prove that
$D_{xy}$ is a jacobian (Problem 2.1).

We now develop a condensed notation in which the algebra of jacobians
may be surveyed as a whole, in a form easy to remember since the
abstract relations are just the ones with which we are familiar in
connection with the properties of commutators in quantum mechanics.
## Formal Properties of Jacobians {#formal-properties-of-jacobians .unnumbered}
Consider first a system with only two degrees of freedom. We define
$$
[A,B] = \frac{\partial(A,B)}{\partial(x,y)} =
\begin{vmatrix}
\frac{\partial A}{\partial x} & \frac{\partial A}{\partial y} \\\\
\frac{\partial B}{\partial x} & \frac{\partial B}{\partial y}
\end{vmatrix}
$$
 where x, y are any variables adequate to determine the
state of the system. Since for a change of variables, $x, y \to x^\prime, y^\prime$
we have
$$
\frac{\partial(A,B)}{\partial(x^\prime,y^\prime)} = \frac{\partial(A,B)}{\partial(x,y)}\frac{\partial(x,y)}{\partial(x^\prime,y^\prime)}
$$
or, in an easily understandable condensed notation,
$$
[A,B]' = [A,B][x,y]'
$$

It follows that any equations that are homogeneous in the jacobians are
invariant in form under \"coordinate transformations\", so that we can
suppress the independent variables x, y and carry out derivations
without committing ourselves to any particular set.

The algebra of these symbols is characterized by the following
identities (the comma may be omitted if A, B are single letters). The
properties of antisymmetry, linearity, and composition have the familiar
form 
$$
\begin{gathered}
[AB] = -[BA], \qquad [AA] = 0 \\\\
[A \pm B, C] = [AC] \pm [BC] \\\\
[AB, C] = [AC]B + A[BC]
\end{gathered}
$$

In addition we have three cyclic identities, easily proved:
$$
\begin{gathered}
[AB] dC + [BC] dA + [CA] dB = 0 \\\\
[A,[BC]] + [B,[CA]] + [C,[AB]] = 0 \\\\
[AB][CX] + [BC][AX] + [CA][BX] = 0
\end{gathered}
$$

The final fundamental property is the \"theorem\"
$$
\text{Let} \qquad dA = b\ dB + c\ dC.
$$

 Then, for all X,
$$
[AX] = b[BX] + c[CX].
$$

These relations are not all independent; for example, (2-11) follows
from (2-9) and (2-13).

Putting $dC = 0$ in (2-9), we obtain the rule
$$
\left(\frac{\partial A}{\partial B}\right)_C = \frac{[AC]}{[BC]} = \frac{[CA]}{[CB]}
$$
by means of which equations are translated from one language to the
other.

From it one sees that the transformation law (2-1) now appears as a
special case of the identity (2-11). Writing for the enthalpy, free
energy, and Gibbs function respectively, 
$$
\begin{gathered}
H = U + PV \\\\
F = U - TS \\\\
G = U - TS + PV
\end{gathered}
$$
 where U is the internal energy with the property
$dU = TdS - P dV$, we have as consequences of (2-13) the relations
$$
\begin{aligned}
\relax [UX] &= T[SX] - P[VX] \\\\
\relax [HX] &= T[SX] + V[PX] \\\\
\relax [FX] &= -S[TX] - P[VX] \\\\
\relax [GX] &= -S[TX] + V[PX]
\end{aligned}
$$

The advantages of this notation is shown particularly when we consider
the four Maxwell equations 
$$
\begin{aligned}
\left(\frac{\partial T}{\partial V}\right)_S &= - \left(\frac{\partial P}{\partial S}\right)_V \\\\
\left(\frac{\partial T}{\partial P}\right)_S &= \left(\frac{\partial V}{\partial S}\right)_P \\\\
\left(\frac{\partial P}{\partial T}\right)_V &= \left(\frac{\partial S}{\partial V}\right)_T \\\\
\left(\frac{\partial V}{\partial T}\right)_P &= - \left(\frac{\partial S}{\partial P}\right)_T
\end{aligned}
$$

 Applying (2-14), we see that each reduces to the single
identity 
$$
[TS] = [PV]
$$

Thus, all of the Maxwell equations are expressions in different
\"coordinate systems\" of the same basic fact (2-18), which will receive
a physical interpretation in Sec. 2.4. In a derivation, such as that of
Eq. (1-49), everything that can be gained by using any of the equations
(2-17) is already accomplished by application of the single relation
(2-18).

Jacobians which involve the entropy in combinations other than $[TS]$
are related to various specific heats. The heat capacity at constant X
is 
$$
C_X = T \left( \frac{\partial S}{\partial T} \right)_X
$$
 and, using
(2-14) we obtain the identity 
$$
[SX] = \frac{C_X}{T}[TX]
$$

In the simplest derivations, application of (2-18) or (2-20) is the
essential step.

In his well-known textbook, Zemansky (1943) shows that many of the
elementary derivations in thermodynamics may be reduced to application
of the \"T dS equations\"
$$
T dS = C_V dT + T \left( \frac{\partial P}{\partial T} \right)_V dV
$$
$$
T dS = C_p dT - T \left( \frac{\partial V}{\partial T} \right)_P dP
$$
and the \"energy equation\",
$$
\left( \frac{\partial U}{\partial V} \right)_T = T \left( \frac{\partial P}{\partial T} \right)_V - P
$$

In the above notation these equations are far from obvious and not easy
to remember. Note, however, that the T dS equations are special cases of
the cyclic identity (2-9) for the sets of variables $\{TVS\}$,
$\{TPS\}$, respectively, while the energy equation is a consequence of
(2-13) and the Maxwell relation:
$$
[UT] = T[ST] - P[VT] = T[PV] - P[VT]
$$

 From (2-14) we see that this is
the energy equation in jacobian notation.
## Elementary Examples {#elementary-examples .unnumbered}
In a large class of problems, the objective is to express some quantity
of interest, or some condition of interest, in terms of experimentally
measurable quantities. Therefore, the \"sense of direction\" in
derivations is provided by the principle that we want to get rid of any
explicit appearance of the entropy and the various energies U, H, F, G.
Thus, if the entropy appears in the combination $[TS]$, we use the
Maxwell relation to replace it with $[PV]$. If it appears in some other
combination $[SX]$, we can use the identity (2-20).

Similarly, if combinations such as $[HX]$ or $[UX]$ appear, we can use
(2-16) and replace them with 
$$
\begin{aligned}
[HX] &= T[SX] + V[PX] = C_X[TX] + V[PX] \\\\
[UX] &= C_X[TX] - P[VX]
\end{aligned}
$$

If the entropy appears outside a jacobian, as in
$[GX] = -S[TX] + V[PX]$, it cannot be eliminated in this way. However,
since in phenomenological thermodynamics the absolute value of the
entropy has no meaning, this situation cannot arise in any expression
representing a definite physical quantity.

For problems of this simplest type, the jacobian formalism works like a
well-oiled machine, as the following examples show. We denote the
isothermal compressibility, thermal expansion coefficient, and ratio of
specific heats by K, $\beta$, $\gamma$, respectively:
$$
K = -\frac{1}{V}\left(\frac{\partial V}{\partial P}\right)_T = \frac{[TV]}{V[PT]}
$$
$$
\beta = \frac{1}{V}\left(\frac{\partial V}{\partial T}\right)_P = \frac{[PV]}{V[PT]}
$$
$$
\gamma = \frac{C_p}{C_V}
$$
 and note that from (2-27) and (2-28) we
have
$$
\frac{K}{\beta} = \frac{[TV]}{[PV]} = \left(\frac{\partial T}{\partial P}\right)_V
$$

Several derivatives, chosen at random, are now evaluated in terms of
these quantities: 
$$
\begin{aligned}
\left(\frac{\partial U}{\partial P}\right)_S &= \frac{[US]}{[PS]} = \frac{T[SS]-P[VS]}{[PS]} = -P\frac{C_V}{C_p}\frac{[TV]}{[TP]} = -\frac{PVK}{\gamma} \\\\
\left(\frac{\partial U}{\partial T}\right)_S &= \frac{[US]}{[TS]} = \frac{T[SS]-P[VS]}{[PV]} = P\frac{C_V}{T}\frac{[TV]}{[PV]} = \frac{PC_V K}{T\beta} \\\\
\left(\frac{\partial T}{\partial S}\right)_U &= \frac{[TU]}{[SU]} = \frac{T[ST]-P[VT]}{T[SS]-P[VS]} = \frac{T[VP]-P[VT]}{P\ C_V[TV]} = \frac{T}{C_V}\left[1-\frac{T\beta}{PK}\right] \\\\
\left(\frac{\partial H}{\partial V}\right)_P &= \frac{[HP]}{[VP]} = \frac{T[SP]+V[PP]}{[VP]} = C_p \frac{[TP]}{[VP]} = \frac{C_p}{\beta V} \\\\
\left(\frac{\partial T}{\partial P}\right)_H &= \frac{[TH]}{[PH]} = \frac{T[ST]+V[PT]}{T[SP]+V[PP]} = \frac{T[VP]+V[PT]}{C_p[TP]} = \frac{V}{C_p}(\beta T - 1) \\\\
\left(\frac{\partial F}{\partial S}\right)_T &= \frac{[FT]}{[ST]} = \frac{-S[TT]-P[VT]}{[VT]} = -\frac{PK}{\beta} \\\\
\left(\frac{\partial G}{\partial V}\right)_T &= \frac{[GT]}{[VT]} = \frac{-S[TT]+V[PT]}{[VT]} = -\frac{1}{K}
\end{aligned}
$$

A more difficult type of problem is the following: We have given a
number of quantities and wish to find the general relation, if any,
connecting them. In one sense, the question whether relations exist can
be answered
immediately; for any two quantities A, B a necessary and sufficient
condition for the existence of a functional relation A = f(B) in a
region R is: $\{[AB] = 0 \text{ in } R\}$. In a system of two degrees of
freedom it is clear that between any three quantities A, B, C there is
necessarily at least one functional relation f(A,B,C) = 0, as is implied
by the identity (2-9) \[Problem 2.2\]. An example is the equation of
state f(PVT) = 0. This, however, is not the type of relation one usually
has in mind. For each choice of A, B, C and each particular system of
two degrees of freedom, some functional relationship must exist, but in
general it will depend on the physical nature of the system and can be
obtained only when one has sufficient information, obtained from
measurement or theory, about the system.

The problem is rather to find those relations between various quantities
which hold *generally*, regardless of the nature of the particular
system. Mathematically, all such relations are trivial in the sense that
they must be special cases of the basic identities already given. Their
physical meaning may, however, be far from trivial and they may be
difficult to find. Note, for example, that the derivative computed in
(2-35) is just the Joule-Thomson coefficient $\mu$. Suppose the problem
had been stated as: \"Given the five quantities
$\{\mu, V, C_p, \beta, T\}$, determine whether there is a general
relation between them and if so find it.\" Now, although a repetition of
the argument of (2-35) would be successful in this case, this success
must be viewed as a lucky accident from the standpoint of the problem
just formulated. It is not a general rule for attacking this type of
problem because there is no way of ensuring that the answer will come
out in terms of the desired quantities.

To illustrate a general rule of procedure, consider the problem of
finding a relationship, if any, between $\{C_p, C_V, V, T, \beta, K\}$.
First we write these quantities in terms of jacobians.
$$
C_p = T \frac{[SP]}{[TP]}, \qquad C_V = T \frac{[SV]}{[TV]}
$$
$$
\beta = \frac{[VP]}{V[TP]}, \qquad K = \frac{[TV]}{V[PT]}
$$

 At this
point we make a definite choice of some coordinate system. Since $[TP]$
occurs more often than any other jacobian, we adopt x = T, y = P as the
independent variables; thus $[TP] = 1$. We can now solve for the
remaining jacobians: 
$$
[SP] = \frac{C_p}{T}, \qquad [VP] = \beta V
$$
$$
[VS] = \frac{C_V KV}{T}, \qquad [VT] = KV
$$

 The variables in jacobians
are P, V, T, S, for which (2-11) gives
$$
[PV][TS] + [VT][PS] + [TP][VS] = 0
$$
 or, in this case
$$
[PV]^2 + [VT][PS] + [VS] = 0.
$$

 Substituting the expressions (2-39)
into this we obtain
$$
\beta^2 V^2 - KV \frac{C_p}{T} + \frac{C_V KV}{T} = 0
$$
 or,
rearranging, we have the well-known law
$$
C_p - C_V = \frac{TV\beta^2}{K}
$$
 which is now seen as a special case
of (2-11).

There are several points to notice in this derivation: (1) no use has
been made of the fact that the quantities T, V were given explicitly;
the
argument supplied them automatically. (2) The solution depends in no way
on the particular coordinate system adopted; if we had chosen $[TV]=1$,
the algebra would have been very slightly longer, with the same result.
(3) The particular arrangement of (PVTS) in (2-40) has no influence on
the result; after an arbitrary permutation of (PVTS), Eq. (2-40) still
says exactly the same thing. (4) It was essential to the method that all
the quantities be expressible in terms of jacobians of exactly four
variables, but any four in place of PVTS would have served just as well.
In solid-state physics, $C_V$ is most easily calculated from theory,
while $C_p$ is most easily measured in the laboratory. Equation (2-42)
is therefore much used (often in approximate forms known as the
Eucken-Grüneisen relation, or the Nernst-Lindemann equation) for the
correction of experimental specific heat data before comparison with
theory. For further details, see Zemansky (1943), Chap. 13; or Callen
(1960), Appendix E.

As a second example, consider again the problem of the Joule-Thomson
coefficient; find a relation between $\{\mu, \beta, C_p\}$ and any other
quantities that may be needed. Proceeding as before, we have
$$
\mu = \frac{[HT]}{[HP]} = \frac{T[ST]+V[PT]}{T[SP]}
$$
$$
\beta = \frac{[VP]}{V[TP]}, \qquad C_p = T\frac{[SP]}{[TP]}
$$

 Choosing
the coordinate system $[SP]=1$, and solving for the remaining jacobians,
we have 
$$
[TP] = \frac{T}{C_p}
$$
$$
[VP] = \frac{\beta VT}{C_p}
$$
but at this stage we see already that the jacobians $[TP]$, $[VP]$ are
the only ones appearing in $\mu$, so we have immediately the result
(2-35):
$$
\mu = [VP] + \frac{V}{T}[PT] = \frac{\beta VT}{C_p} - \frac{V}{T}\frac{T}{C_p} = \frac{V}{C_p}(\beta T-1)
$$
and the identity (2-11) was not needed.

As a third example consider the problem of finding a relation between
$\beta, K, C_p$, and the quantity
$\alpha \equiv (\partial U / \partial T)_S$. The calculation goes
through exactly as in the first example, with the result
$$
\alpha = P \left[ \frac{K C_p}{T} - \beta V \right].
$$

We have already found a simpler formula for $\alpha$ in (2-32). By use
of (2-42) one shows that (2-44) and (2-32) are indeed equivalent. If we
had chosen the variables $\{\alpha, \beta, K, C_V\}$ we would once again
have found a \"shortcut\" that takes us directly to (2-32) without use
of (2-11).

In the first type of problem, illustrated by equations (2-30) through
(2-37), we are content to find the quantity or condition of interest in
terms of *any* experimentally measurable quantities. After finding any
such relationship, one can apply the basic identities and transform it
into various other forms. In the second type of problem we demand that
the result must come out in terms of certain *specified* quantities, for
example the ones which we have measured. The second method of procedure
leads us directly to this relation if it exists.

As a final example, suppose we have measured $C_p$ and the thermal
expansion coefficient $\beta$ at various temperatures and volumes. Are
these data sufficient to determine the quantity
$\delta \equiv (\partial T/\partial P)_U$? If not, what additional
measurements must we make? In the coordinate system $[SP]=1$, we find
the relations
$$
[TP] = \frac{T}{C_p}, \qquad [VP] = \frac{\beta V T}{C_p}
$$
$$
[VT] = \left[\frac{\beta V T}{C_p} - \delta \right]
$$
 and substituting
into (2-40) we have
$$
[SV] = \frac{\beta^2 V^2 T}{C_p^2} + \frac{C_p}{P} - \frac{\beta V T}{P}.
$$

We do not yet have the desired result because there is nothing which
determines the jacobian $[SV]$. This means that $\beta$ and $C_p$ are
not enough to determine $\delta$; but we can determine the missing
quantity as follows. The extra jacobian (2-45) is, from (2-20),
$$
[SV] = \frac{C_V}{T}[TV] = \frac{C_V}{P}\left[\delta - \frac{\beta V T}{C_p}\right]
$$

Thus, it would be sufficient to measure also $C_V$. Equating (2-45) and
(2-46) and solving for $\delta$,
$$
\delta = \frac{\beta V T}{C_p}\left[1 - \frac{\beta V T}{C_p - C_V}\right]
$$
which, using (2-42), may also be written as
$$
\delta = \frac{V}{C_p}(\beta T - KP).
$$
 so that a measurement of the
compressibility K would also suffice.

It is impossible to appreciate the ease with which these derivations
have been carried out here unless one also tries to derive them without
making any use of jacobians; the reader is urged to do this for himself
\[Problem 2.3\].
## Physical Meaning of Jacobians {#physical-meaning-of-jacobians .unnumbered}
The preceding discussion, while demonstrating the power and usefulness
of jacobians in thermodynamics, has raised more questions than it has
answered. What do the jacobians mean? Why do these methods work so well?
Can we find a point of view which makes it clear from the start that
jacobians rather than partial derivatives are the \"natural\" quantities
of thermodynamics? And a much deeper question: Why is it that in so many
different branches of physics, the introduction of antisymmetric bracket
symbols, all with the same abstract algebraic properties, leads to the
most succinct and powerful methods of calculation?

As a start toward answering these questions we observe that, in spite of
first appearances, jacobians are actually simpler quantities than are
partial derivatives. Because of the fact that the particular coordinate
system x, y is unimportant, we can regard a jacobian as expressing a
mutual property of two variables, while a partial derivative represents
a joint property of three variables. One interpretation of this mutual
property follows from the familiar use of jacobians in transforming an
element of volume in multiple integrals. Thus, consider a quantity
Z(x,y) which is a function of state of the system, and a certain range
of states represented by the area r in the (x-y) plane. In terms of a
different set of variables A, B this same set of states is mapped onto a
corresponding region R in the (A-B) plane. Then the integral of Z over
this region is given by
$$
\int_R Z\ dA\ dB = \int_r Z \frac{\partial(A,B)}{\partial(x,y)}\ dx\ dy
$$

Thus elements of volume corresponding to the same range of states
transform according to 
$$
dR = \frac{\partial(A,B)}{\partial(x,y)}\ dr
$$
or, the jacobian is the [local magnification factor]{.underline} in the
mapping of the (x-y) plane onto the (A-B) plane.

These remarks are illustrated in Fig. 2.1, in which we see an
infinitesimal Carnot cycle as viewed in the six different planes which
can be formed from the coordinates P, V, T, S. Adopting the convention
that the rectangle in the T-S plane encloses unit area, the jacobian
$[AB]$ is then equal to the area enclosed by the mapping of this Carnot
cycle onto the A-B plane, with a positive sign if it is described in a
counterclockwise direction, negative if clockwise. The Maxwell equation
(2-17a) is often described as expressing the fact that $(T\ dS - P\ dV)$
is an exact differential; an equivalent statement which has perhaps more
intuitive appeal is that [the mapping of the T-S plane onto the P-V
plane always preserves areas]{.underline}. This is just the statement
that the work done in a closed reversible cycle can be found equally
well from the T-S diagram as the P-V diagram:

$\oint T\ dS = \oint P\ dV$.

The content of the identity (2-11):
$$
[PV][TS] + [VT][PS] + [TP][VS] = 0
$$
 is that, given the ratios
$[TS]:[PS]:[VS]$ of the areas of the top three diagrams, one linear
combination of the areas $[PV]$, $[VT]$, $[TP]$ is determined. A study
of Fig. 2.1 discloses the geometrical reason for this and shows that a
stronger statement can be made: Given the top three diagrams, all the
others may be constructed by projections as shown.

The interpretation of a jacobian $[AB]$ as giving the area and direction
of travel for an infinitesimal reversible cycle, as seen in the A-B
plane, is probably the most convenient one. However, another way of
looking at it is to draw in the x-y plane the contours A(x,y) = const.,
B(x,y) = const., as in Fig. 2.2. If we imagine a z-axis at right angles
to the paper, we see that the jacobian can be written as a vector
cross-product
**[FIGURE: An infinitesimal Carnot cycle as seen in several coordinate planes.]**
1 $\to$ 2 adiabatic expansion\
2 $\to$ 3 isothermal compression\
3 $\to$ 4 adiabatic compression\
4 $\to$ 1 isothermal expansion
**[FIGURE: Lines of constant A and constant B in the x-y plane. The jacobian [A,B] is equal to the area of the parallelogram.]**
$$
\frac{\partial(A,B)}{\partial(x,y)} = \frac{\partial A}{\partial x}\frac{\partial B}{\partial y} - \frac{\partial A}{\partial y}\frac{\partial B}{\partial x} = (\nabla A \times \nabla B)_z
$$
of the gradients $\nabla A, \nabla B$. Its numerical value is therefore
equal to the area of the parallelogram whose sides are
$\vec{\nabla A}, \vec{\nabla B}$. At any point where $[A,B]=0$, the
lines B = const., A = const., are tangent to each other. At such a
point, any infinitesimal change of state which holds A constant also
holds B constant; thus, the condition for the inversion point of the
Joule-Thompson effect is 
$$
0 = [HT] = T[ST] + V[PT] = T[VP] + V[PT]
$$

This appears as a singular point in the mapping of the P-V plane onto
the H-T plane.
