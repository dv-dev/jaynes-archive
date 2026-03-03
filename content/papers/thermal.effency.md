---
title: "Note on Thermal Heating Efficiency"
author: ["E.T. Jaynes"]
year: 1981
abstract: >
  Kelvin showed the maximum efficiency with which heat can be converted
  into work; but there is a dual theorem about the maximum efficiency
  with which heat at one temperature can be converted into heat at
  another temperature. It has some surprising implications, in
  particular that the efficiency with which we heat our buildings could
  in principle be improved by a large factor. This long known but
  still little known --- fact is of current pedagogical interest and
  practical importance.
---
## Introduction
For over 200 years the University of Glasgow, Scotland, has played a
uniquely important role in the development of thermodynamics. There the
distinction between temperature as a measure of *intensity* of
something; and heat as a *quantity* of something, was first seen clearly
by Joseph Black, about 1760. This knowledge contributed to the work of
his colleague, James Watt, in the first practical means of converting
heat into work. Then Carnot and others tried to find the maximum
theoretical efficiency of this conversion, but the one who finally
succeeded was Wm. Thomson (later Lord Kelvin) at the University of
Glasgow.

Recent an addition to this was made, which is not only of theoretical
interest as representing in a sense the completion of the logical
structure of classical thermodynamics; it has immediate practical
implications. Yet the principle is hardly new; it is such a simple and
immediate consequence of Thomson's work that it must have been known
to Thomson in 1870. Today it cannot be really unknown to anyone familiar
with the theory of heat pumps. But to the best of our knowledge it has
not yet appeared in any physics textbook, stated in a form where it is
seen as logically independent of Carnot engines, and forming the natural
dual theorem to the one on efficiency of Carnot engines. It seems
appropriate that this way of looking at the result was finally pointed
out by Robert S. Silver (1981), the James Watt Professor (now emeritus)
of the University of Glasgow.

In Section 2 we give the almost trivial derivation, and in Section 3 we
point out its practical implications by numerical examples. Since a
large part of the world's energy resources are actually used for heating
rather than production of work, these implications are not trivial.
Section 4 points out another surprising application, and in the final
Section 5 we speculate on possible nonequilibrium generalizations.
## Theoretical Derivation
We have a source of heat $Q_2$ which is available at Kelvin temperature
$T_2$. By this we mean, as was stressed long ago by J. Willard Gibbs
(1886), that the source is capable of delivering that heat to a heat
reservoir which is at temperature $T_2$; and $T_2$ is the highest
temperature to which it can deliver that heat. If there is available a
cold reservoir at temperature $T_1 < T_2$, then according to classical
thermodynamics we may exploit this temperature difference to obtain work
$W$. Applying the first and second laws: $W = Q_2 - Q_1$,
$Q_1/T_1 \ge Q_2/T_2$ and solving these for $W$ and $Q_1$ we have
$$W \le Q_2 \left(1 - \frac{T_1}{T_2}\right), \quad Q_1 \ge Q_2 \frac{T_1}{T_2}$$
with equality if and only if the engine is reversible. In the latter
case the \"wasted energy\" $$Q_1(\text{Carnot}) = Q_2 \frac{T_1}{T_2}$$
is delivered as heat to the reservoir at temperature $T_1$. This is the
standard result.

But now suppose that our objective is not to produce work, but to
deliver the maximum possible heat to that lower temperature reservoir.
This is the conversion problem faced in every home, where one has heat
from a gas, oil, wood, or coal flame but wants heat at room temperature.
At present, we simply allow the primary heat $Q_2$ to degrade itself
directly to the lower temperature $T_1$ by passing through ducts,
radiators, etc. Thus we obtain, at best (i.e., neglecting heat loss
through chimneys), the amount of heat $Q_1(\text{direct}) = Q_2$. But
this is an irreversible process, since there is a net entropy increase
$\Delta S = Q_2/T_1 - Q_2/T_2 > 0$ indicating that something has been
wasted, and we can do better. The first and second laws imply that, not
only in conversion of heat to work, but also in conversion of heat to
heat, the maximum efficiency will be attained if we can carry out the
process reversibly.

Suppose we have an ambient heat reservoir (the outside world) at
temperature $T_0 < T_1$ and we use a perfect Carnot engine to obtain the
heat $Q_1(\text{Carnot})$. Then we still have the work $W$ available,
which we can use to drive a heat pump between $T_0$ and $T_1$, yielding
the additional heat $$Q_1(\text{pump}) = \frac{T_1 W}{T_1- T_0}.$$
Combining (2) and (3), we have now obtained the total heat
$$Q_1 = Q_1(\text{Carnot}) + Q_1(\text{pump}) = Q_2 \frac{T_1}{T_2} \frac{T_2 - T_0}{T_1 - T_0}$$
and there is always a net gain, since $Q_1$ is always greater than $Q_2$
whenever $T_0 < T_1 < T_2$. But while we know that a reversible Carnot
engine delivers the maximum attainable work, this argument does not make
it obvious whether (4) is the maximum attainable heat.

Now from a theoretical standpoint it is more general and more elegant to
apply the first and second laws directly to this process, as we did in
(1). Since some heat $Q_0$ is removed from the outside reservoir, we
must have
$$Q_1 = Q_0 + Q_2, \quad \frac{Q_1}{T_1} \le \frac{Q_0}{T_0} + \frac{Q_2}{T_2}.$$

Solving these equations for $Q_1$ and $Q_0$, we have
$$Q_1 \le Q_2 \frac{T_1}{T_2} \frac{T_2 - T_0}{T_1 - T_0}, \quad Q_0 \le Q_2 \frac{T_0}{T_2} \frac{T_2 - T_1}{T_1 - T_0}$$
with equality if and only if the process is reversible. Thus we obtain
automatically the same result (4), plus the statement that it is the
*maximum attainable heating*, without invoking Carnot engines at all. It
is in this simple argument that the main theoretical and pedagogical
interest of this discussion lies.
## Practical Implications
Consider heating from a primary temperature $T_2 = 1000$K to room
temperature, $T_1 = 25^\circ\text{C} =$ $298$K, with an outside
temperature $T_0 = 0^\circ\text{C} = 273$K. Comparing our ideal $Q_1$
with the present maximum $Q_2$, we have from (7), the gain factor
$$G = \frac{Q_1}{Q_2} = \frac{1-.273}{1-.916} = 8.66$$ This seems at
first glance quite startling; if we take into account that we are at
present far from getting even $Q_2$ because of heat loss up chimneys,
the conclusion is that it is in principle possible to heat our homes
with an order of magnitude less fuel than we are now consuming.
A better idea of the numerical improvement allowed by the second law is
given in Fig. 1, where we give contours of constant gain $G=Q_1/Q_2$ in
the $(T_0, T_2)$ plane for $T_1 = 25^\circ\text{C}$, room temperature.
Even in cold climates, average gains of the order of 5 are indicated.
**[FIGURE: Contours of Constant Gain in the ($T_0, T_2$) Plane, for $T_1 = 25^\circ\text{C}$.]**
The reason for this high efficiency is that $T_0$ and $T_1$ are not very
different on the Kelvin scale. With the values of inside and outside
temperature assumed in (7), one Joule of work will pump
$$T_0/(T_1 - T_0) = 10.9$$ Joules of heat from the outside world, and
deliver 11.9 joules to the inside. Unfortunately, presently available
heat pumps are far from realizing this theoretical efficiency. Silver
(1981) notes that if present engines realize only half of the
theoretical efficiency, then the heat pump component of $Q_1$ will be
only a quarter of our calculated value.

Evidently, the development of heat pumps that approach the theoretical
efficiency for small temperature differences would be of very great
economic importance, and no physical law stands in the way of realizing
them. It is only a matter of the ingenuity of inventors; and the one who
succeeds will be one of the world's great benefactors. We suspect that
the successful technology will avoid the crude mechanical pumps of our
present realizations, perhaps depending on thermoelectric or
electrochemical means that avoid all mechanical moving parts, although
perhaps with circulating fluids.
## Free Ovens for Eskimos
Note that the derivation of (6) is general in that it holds for any
exchange of heat between three reservoirs whatever the relative
temperatures and the signs of the $Q_i$, although the arrangement of
Carnot engines envisaged in our derivation of (4) would no longer apply.
But this seems to contradict one common statement of the second law,
attributed to Kelvin, that \"It is impossible for heat to flow of itself
from a cold reservoir to a hotter one\". The statement actually made by
Kelvin is that it is impossible to do this *without leaving changes in
external bodies*. Eq. (6) demonstrates the need for this qualification;
for it is quite possible for heat to flow spontaneously from room
temperature $T_1$ to a higher temperature $T_2$, if there is at the same
time a compensating flow to a lower temperature $T_0$.

Suppose then that we want to heat an oven at the standard cooking
temperature of $T_2 =$ $400\text{F} = 204\text{C} = 477$K, using heat
extracted from the air of a kitchen at room temperature
$T_1 = 25\text{C} = 298$K. Our equations use the sign convention that
$Q_1$ is heat *delivered* to the reservoir at $T_1$, while $Q_0$ and
$Q_2$ represent heat *extracted* from those at $T_0, T_2$. Therefore
$Q_0, Q_1, Q_2$ are now all negative, so $(-Q_1)$ is the heat extracted
from the room and $(-Q_2)$ is the resulting heat delivered to the oven;
but Eqs. (6) still hold. Writing the first as
$$(-Q_2) \le (-Q_1) \frac{1-T_0/T_1}{1-T_0/T_2},$$ we see that the
maximum heat that can be delivered to the oven is less than that
extracted from the room, but if the outside temperature $T_0$ is low
enough, the efficiency can be quite high; unlike room heating, oven
heating becomes *more* efficient as the outside temperature is lowered.
Indeed, we have only to run a Carnot engine between $T_1$ and $T_0$
extracting the work $W =$ $(-Q_1) (1- T_0/T_1)$, then use that to run a
heat pump between $T_0$ and $T_2$, which delivers the heat
$(-Q_2) = W/(1-T_0/T_2)$, in agreement with (9). If the outside
temperature $T_0$ is $-40\text{F} = -40\text{C} =$ $233$K then according
to (9), 1000 calories of heat removed from the room can deliver 426
calories to the oven. If this leaks back eventually to re-heat the room,
it might appear that the \"cost\" of running the oven was not the 1000
calories removed from the room, but only the 574 calories lost to the
outside.
But this leaking back is again an irreversible process in which
something is wasted, and we can do better. If the oven is well
insulated, then when we are done with it the heat $(-Q_2)$ is still in
it, so we have only to run those Carnot engines backwards, obtaining the
work $W = 426(1 - T_0/T_2)$ from which the heat pump can return the heat
$W/(1-T_0/T_1) = 1000$ calories to the room, completely restoring the
*status quo*. The second law allows us to operate an oven, at whatever
temperature we please, at zero cost, the outside reservoir $T_0$ serving
only as a temporary repository for the entropy that must be disposed of
in heating the oven.
Unfortunately, the second law will not allow us to supply our cooling
needs as easily; it offers free (that is, zero operating cost) ovens to
Eskimos, but not free air-conditioning to hottentots because they have
no lower temperature reservoir to take up that entropy.
## Speculations
How much generality and finality do the above results have? As we
stressed before (Jaynes, 1965), in classical thermodynamics the notions
of temperature and entropy are defined only for states of thermal
equilibrium; therefore the conventional second law that we considered
above refers only to the net result of processes that begin and end in
states of thermal equilibrium.
Then classical thermodynamics does not in itself prohibit still more
efficient engines, if they operate in *nonequilibrium conditions*; it is
simply silent on that question. Indeed, the surprisingly high observed
efficiency of animal muscles, which operate in a nonequilibrium
environment, has been thought by some to be such a realized violation of
the second law.
Many have speculated about the possibility of non-biological engines
that violate the second law. The more careful writers have refrained
from claiming that they are absolutely impossible in principle. The
Maxwell Demon, which is able to operate on a system directly at the
microscopic level, is the most familiar example; but Max Planck (1917)
also noted that we expect \"to make a most serviceable application\" of
any phenomenon that is found to deviate from the second law, and
considered it a good policy to remain alert, on the lookout for such
things.
Presumably, if fundamental limitations on conversion efficiency in
nonequilibrium conditions exist, they will come instead from statistical
mechanics; but in our opinion all existing attempts to show this contain
logical loopholes, and no absolutely convincing arguments of this nature
have been produced. We feel, as did Maxwell and Planck, that from the
standpoint of logical demonstration this is still an open question;
dogmatic pronouncements on either side are premature.
However, a nonequilibrium generalization of the second law, that in
essence goes back to Boltzmann, does place definite restrictions on what
can be accomplished *reproducibly* when our technology, unlike the
Maxwell Demon, is without knowledge of the microstate and is able to
operate only at the macroscopic level. Any macrostate M, equilibrium or
nonequilibrium, represents a certain phase volume $W(M)$ occupied by all
microstates compatible with M. A reproducible process must work for all
of those microstates; so it is a direct consequence of Liouville's
theorem that the entropy $S = k \log W$ cannot decrease in a
reproducible macroscopic process $(M_1 \to M_2)$ that takes place
between such states. The maximum efficiency of a reproducible
macroprocess is attained when the phase volume of those degrees of
freedom that actually take part in the interactions is the same for the
initial and final macrostates: $W(M_1) = W(M_2)$.
Using this fact, we have shown (Jaynes, 1989) that the high efficiency
of animal muscles may be predicted from two data: the heat of reaction
0.43 ev of hydrolysis of the ATP molecule and the value 37$^\circ$C of body
temperature. Presumably, similar efficiencies are realizable *in vitro*,
using systems that are never in thermal equilibrium. However, these
phenomena do not really violate the principles explained by Maxwell,
Gibbs, Planck, and Einstein long ago; they represent only the
recognition that reversible operation need not be slow. In a
nonequilibrium environment, maximum efficiency may require the
reversible entropy-preserving process to be fast on the molecular time
scale, so that the useful work is done before the inevitable final
thermalization can take place. This, we suggest, is the secret of the
high efficiency of muscles. The field now seems wide open for new and
important advances.
## References {#references .unnumbered}
Gibbs, J. W. (1886), "Electrochemical Thermodynamics\", Report Brit.
Assoc. Adv. Sci. 388; reprinted in *The Scientific Papers of J. Willard
Gibbs*, Longmans, Green & Co., (1906) and by Dover Publications, Inc.,
New York (1961); pp 406-412.
Jaynes, E. T. (1965), "Gibbs vs. Boltzmann Entropies\", Am. Jour. Phys.
**33**, 391.
Jaynes, E. T. (1989), \"Clearing up Mysteries --- the Original Goal\",
in *Maximum Entropy and Bayesian Methods*, J. Skilling, Editor, Kluwer
Publishing Co., Holland, pp. 1-27.
Planck, Max (1917), *Treatise on Thermodynamics*, 5th Edition,
Longmans, Green, & Co., London; undated reprint by Dover Publications,
Inc., New York; Part III, Chapter II.
Silver, R. S. (1981), \"Reflexions sur la puissance chaleurique du
feu\", Heat Recovery Systems, **1**, 205-207.
