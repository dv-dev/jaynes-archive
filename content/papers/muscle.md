---
title: "The Muscle as an Engine"
year: 1983
abstract: >
  Jaynes speculates on the principles governing energy conversion efficiency,
  arguing that muscles achieve higher efficiency than conventional
  interpretations of the Second Law of Thermodynamics (Kelvin's formula)
  suggest. He proposes that by reinterpreting Kelvin's formula in terms of
  energy per degree of freedom rather than temperature, the formula becomes
  general enough to include heat engines, muscles, and pure mechanisms. This
  perspective suggests that capture of primary chemical energy before it
  degrades into heat can lead to man-made engines with efficiencies far
  exceeding those of traditional Carnot engines.
author: ["E.T. Jaynes"]
categories: ["Quantum Mechanics & Advanced Physics"]
tags: ["muscle efficiency", "Carnot engine", "second law of thermodynamics", "energy conversion", "statistical mechanics", "molecular biology", "Gibbs", "Kelvin formula"]
---
## INTRODUCTION
We sometimes encounter statements of the genre: "Kelvin's formula for
the efficiency of a reversible Carnot engine

$$e = 1 - T/T^\prime \tag{1}$$

shows that the efficiency of every type of energy converter has a
theoretical upper limit that cannot be exceeded." We wish to point out
that Kelvin's result applies, not to every type of energy converter, but
only to heat engines -- i.e., engines which operate by extracting heat
from one reservoir which is at thermal equilibrium at some temperature
$T^\prime$ and delivering heat to a similar reservoir at a lower temperature T.
But there is no reason why (1) should apply to engines that deliver work
by a different mode of operation. Indeed, the world's most universally
available source of work -- the animal muscle -- presents us with a
seemingly flagrant violation of that formula.

Our muscles deliver useful work when there is no cold reservoir at hand
(on a hot day the ambient temperature is at or above body temperature)
and a naive application of (1) would lead us to predict zero, or even
negative efficiency. But according to Lehninger (1965), under these
conditions they still deliver an efficiency of about 20%.

According to Alberts, *et al.* (1983), under favorable conditions the
efficiency of a muscle can be as high as 70%, although a Carnot engine
would require an upper temperature $T^\prime$ of about 1000 K to achieve this.
The answer, of course, is that a muscle is not a heat engine. It draws
its energy, not from any heat reservoir, but from the activated
molecules produced by a chemical reaction. That is why we should always
stress the word "heat" when discussing Carnot engines.

Only when we first allow that primary energy to degrade itself into heat
at temperature $T^\prime$ -- and then extract only that heat for our engine --
does the Kelvin efficiency formula (1) apply. If we can learn how to
capture that primary energy before it has a chance to degrade, as our
muscles have already learned how to do, then we should be able to
achieve higher efficiency than one would suppose from (1) in a man-made
engine. Of course, this would not be a violation of the second law;
rather, to achieve it will require a very clear understanding of what
the second law really is.

## THE ANTI-CARNOT EFFICIENCY
What efficiency might one hope for in such an anti-Carnot engine? There
is no reason to doubt that, with proper understanding, the performance
of our muscles could be at least equalled *in vitro*. Now, whatever the
theoretical maximum efficiency, it can always be written in the form (1)
if we wish to do so; the question then becomes: "What are the effective
upper and lower temperatures?"

As a partial answer we imagine that our engine will, like our muscles,
eventually discharge some heat to the outside world; then let us take
T as the ambient temperature -- which is, for our muscles, body
temperature. What is the effective upper temperature $T^\prime$? It appears to
us that this was answered in a penetrating remark made by J. Willard
Gibbs in a letter to Sir Oliver Lodge, in 1887; it is the highest
temperature to which the activated molecules could deliver heat.

If the molecules with activation energy Q can deliver a fraction fQ
of that energy to a heat reservoir at temperature $T^{\prime\prime}$, then we could
in turn use it to run a conventional Carnot engine with upper
temperature $T^{\prime\prime}$. Thus the theoretical maximum efficiency must be at
least as high as the maximum attainable value of
$$f(1 - T/T^{\prime\prime}) \tag{2}$$

This little hint from Gibbs is all we need to understand the efficiency
of a large class of energy convertors.

If in the Kelvin formula (1) we replace temperature by what it amounts
to -- energy per degree of freedom $W = (1/2)kT$, we see before us an
explanation and generalization of (1):

$$e = 1 - W/W^\prime \tag{3}$$

which does not
look very different at first; but now we have removed the limitation of
thermal equilibrium on our energy source and sink. For "temperature" 
is defined only for a system in thermal equilibrium, while "energy per
degree of freedom" is meaningful not only in thermal equilibrium, but
for any small part of a system -- such as those activated molecules --
which might be far from thermal equilibrium.

One might then question whether such a nonequilibrium generalization of
(1) is valid. We may, however, reason as follows. Although conventional
thermodynamics defines temperature and entropy only in equilibrium
situations, it cannot matter to an engine whether all parts of its
energy source are in equilibrium with each other. Only those degrees of
freedom with which the engine interacts can be involved in its
efficiency; the engine has no way of knowing whether the others are or
are not excited to the same average energy. The same applies to the low
temperature heat sink.

Therefore, since (3) is unquestionably valid when both reservoirs are in
thermal equilibrium, it must be correct more generally, if we take W
and $W^\prime$ to be the average energy in those degrees of freedom with which
the engine actually interacts. But then (3) has a simple intuitive
meaning.

To see this, note that at room temperature T the average thermal
energy per degree of freedom $W = (1/2)kT$ is about 1/80 ev. A chemical
reaction might leave a product molecule in an excited state with perhaps
E = 0.5 ev of excitation energy. If this is concentrated in, say,
N = 2 vibrational degrees of freedom, it thus represents a tiny "hot
spot" with energy E/N per degree of freedom. The activated molecules
would have, as a class, an effective temperature $T^\ast = 2W/Nk$, of the
order of 20 times room temperature.

This, we conjecture, is the $T^\prime$ that we should use in Kelvin's formula
(1) for the maximum theoretical efficiency of a muscle. It is not a real
temperature, but only the effective temperature of those degrees of
freedom that are supplying the energy. In effect, we are using the
activated molecules themselves as the heat reservoir of (2), so f = 1
and $T^\prime = T^{\prime\prime} = T^\ast$, and we recover just Gibbs' statement.
If $T^\prime/T = 20$ and we convert the little bubble of concentrated energy
from a single molecule into useful work before it has a chance to
thermalize by spreading out over 20 vibrational degrees of freedom, we
should in principle be able to realize something like 95% conversion
efficiency. Thus the values actually achieved by our muscles cease to be
puzzling.

From this viewpoint, the basic reason for the "second law" limitation
on efficiency is that we are trying to recapture energy that has spread
in an uncontrolled way over many degrees of freedom, and concentrate it
back into a single degree of freedom, the motion of a piston or tendon.
But the engine must be able to do this reproducibly; i.e., whatever the
details of excitation of all those molecular degrees of freedom.

It is then Liouville's theorem -- conservation of microscopic phase
volume -- that places the limitation (3) on how much concentration of
energy into a small phase volume is possible. As we have noted before
(Jaynes, 1965), if we interpret entropy as $S=k\log V$, where V is the
phase volume compatible with any macrostate, equilibrium or
nonequilibrium, then the second law
$$S(\text{final}) \ge S(\text{initial})$$
follows immediately from
Liouville's theorem, as a necessary condition for any process to be
reproducible. But in a fast process, that happens in a time so short
that thermal equilibrium of the whole system is never reached, only the
phase volume of those degrees of freedom actually involved in the
interactions needs to be considered.

Indeed, if the primary energy is concentrated in a single degree of
freedom and we can extract it before it spreads at all, then our engine
is in effect a "pure mechanism" like a lever and $W^\prime$ is the work
delivered to it. The generalized efficiency (3) then reduces to
$1 - kT/2W^\prime$, or
$$(\text{Work out}) = (\text{Work in}) - (1/2) kT \tag{4}$$

The work we
can expect to get out of a lever is not quite all that we had put in!
It may seem strange to see a pure mechanical formula thus amended by
thermodynamics. But a little further thought makes it clear that (4) is
indeed correct; the last term is just the mean thermal energy of the
lever itself, which cannot be extracted reproducibly. At least, if
anyone should succeed in doing this, then he would need only to wait a
short time until the lever has absorbed another (1/2)kT from its
surroundings, extract that, and repeat -- and we would have the
perpetual motion machine that the Second Law holds to be impossible.
The simple generalization (3) of Kelvin's formula thus appears to have a
rather wide range of application.

## TENTATIVE CONCLUSIONS
What do the known facts of biology tell us about these questions? The
currently popular myosin bridge mechanism for striated muscle
contraction (Alberts, *et al.*, 1983) fits in quite nicely with these
speculations; the bending of that bridge is a degree of freedom that
seems well adapted to transferring its energy, while resisting rapid
thermalization.

Of course, we are not pretending to make any new contribution to biology
by these remarks; rather we are speculating about the possibility of
advancing the technology of energy convertors by taking hints from how
Nature has managed it in biology.

Having seen this biological mechanism, it is easy to believe that many
other kinds of macromolecules could be "designed" to do similar
things, perhaps more easily. In time the design of useful anti-Carnot
molecular engines (artificial muscles) might become about as systematic
and well understood as the design of dyes, drugs, and antibiotics is
now. However, a prerequisite to this is a clear understanding of the
physical principles that must govern energy conversion in any system,
biological or otherwise.

In the attempts of L. A. Blumenfeld (1983) to relate efficiency of
biological energy conversion to physical principles, he states that (A)
high efficiency requires the energy conversion process to be reversible; 
and (B) reversible behavior is fundamentally impossible in a system of
molecular size, because of the uncertainty principle. In some similar
remarks (C), Elsasser (1966) invokes the uncertainty principle to place
fundamental limits on mechanistic analysis in biology. Our thinking has
led us to just the opposite conclusions:

(A) The Carnot principle and low "second law" efficiency of present
engines are only consequences of the thermalization process (the primary
chemical energy is allowed to degrade into heat before being used). If
we can avoid the thermalization, Carnot engine lore must be modified as
noted above. It is satisfying that the same formula holds, only
reinterpreted.

(B) For efficient conversion of chemical energy into mechanical energy
the conversion must proceed directly and quickly. Far from being
impossible in systems of molecular size, this almost requires that the
moving parts receiving the primary energy be of molecular size, because
the useful output energy must be delivered to a single degree of
freedom. We speculate that this is just the reason why biological
systems have accomplished it, and human engineers have not.

(C) Instead of present quantum theory placing limits on the
possibilities of mechanistic analysis in biology, the continued success
of mechanistic analysis in biology may some day show us the limits of
validity of quantum theory.

Thus it appears to us that the second law and the uncertainty principle
place virtually no limitations on what can be done in conversion of
chemical energy to mechanical work; the field is wide open for clever
inventors, who may at any time do what we have all been taught is
impossible.

## REFERENCES
B. Alberts et al., (1983), *Molecular Biology of the Cell*, Garland
Publishing Co., New York; pp. 550-609.

L. A. Blumenfeld (1983), *Physics of Bioenergetic processes*,
Springer-Verlag.

W. M. Elsasser (1966), *Atom and Organism, a New Approach to Theoretical
Biology*, Princeton University Press, Princeton, New Jersey.

J. Willard Gibbs (1887), in *Scientific Papers*, Vol 1, Dover
Publications, Inc. (1961); pp. 406-412.

E. T. Jaynes (1965), "Gibbs vs Boltzmann Entropies", *Am. J. Phys.*
**33**, 391-398.

A. L. Lehninger (1965), *Bioenergetics*, W. A. Benjamin, N. Y. See also
A. L. Lehninger (1975), *Biochemistry, The Molecular Basis of Cell
Structure and Function*, Worth Publishers, Inc., 444 Park Ave. South,
New York.
