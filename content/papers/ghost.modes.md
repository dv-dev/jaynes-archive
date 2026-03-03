---
title: "Ghost Modes in Imperfect Waveguides"
author: ["E.T. Jaynes"]
year: 1958
abstract: >
  Attention is called to the existence of microwave resonances
  which have the unusual property that they are nonradiating, and thus
  have high Q, in spite of the fact that the fields are not enclosed
  completely by metallic walls. These "ghost modes" represent fields
  which are derived from those of the usual waveguide modes, but are
  "trapped" in the vicinity of imperfections in the waveguide. Their
  resonant frequency is slightly lower than the corresponding cutoff
  frequency. If one attempts to use a waveguide in its lowest mode, over
  a range of frequencies which includes the ghosts of higher modes,
  complicated resonance effects may be observed which can cause trouble
  in some types of microwave circuits. The same phenomenon exists in any
  structure which has pass bands and rejection bands, such as periodic
  structures or crystals.
---
# Introduction
THE phenomenon described herein explains certain curious and troublesome
effects observed in waveguides operating close to the cutoff frequency
of a propagation mode, and it may have applications for waveguide
filters. In addition, it has a certain educational value because of a
mathematical analogy with the phenomenon of localized bound states due
to imperfections in crystals.
# Ghost Modes Due to a Dielectric
To illustrate the simplest case, and one which can be analyzed
completely, consider the structure of Fig. 1. A dielectric disk of
thickness $d$, dielectric constant $\epsilon$, is placed in a
cylindrical waveguide of radius $a$. Let the center of the disk be the
origin of a cylindrical coordinate system $(r, \theta, z)$. A possible
electromagnetic field is one whose transverse structure is that of the
TM$_{01}$ mode, derived from the field component $$E_z = \begin{cases}
    B J_0(k_1 r) \exp [-(k_1^2 - k^2)^{1/2}z], & z > \frac{d}{2} \\\\
    A J_0(k_1 r) \cos [(\epsilon k^2 - k_1^2)^{1/2}z], & |z| < \frac{d}{2} \\\\
    B J_0(k_1 r) \exp [+(k_1^2 - k^2)^{1/2}z], & z < -\frac{d}{2}
\end{cases}$$ In (1),
$$k_1 = \frac{2.405}{a} = \frac{\omega_c}{c}, \quad k = \frac{\omega}{c}$$
where $\omega_c$ and $\omega$ are, respectively, the TM$_{01}$ cutoff
frequency and an operating frequency to be determined presently.

Matching solutions across the dielectric-air interfaces, we obtain the
condition
$$\tan \left( \epsilon k^2 - k_1^2 \right)^{1/2} \frac{d}{2} = \epsilon \left[ \frac{k_1^2 - k^2}{\epsilon k^2 - k_1^2} \right]^{1/2}$$

For any $\epsilon > 1$, (2) has at least one solution for $k$ with
$k < k_1$. If $(\epsilon - 1)^{1/2}k_1d < 2\pi$, only one such solution
exists. We consider, in particular, the case where $\epsilon$ is
appreciably greater than unity and $k_1 d \ll 1$. Then $k$ as determined
from (2) is very close to $k_1$, and it will be a good approximation to
set
$$(\epsilon k^2 - k_1^2)^{1/2}d \approx (\epsilon - 1)^{1/2} k_1 d \ll 1,$$ so that (2) reduces to the following formula for $\omega$:
$$\omega^2 \approx \omega_c^2 \left[ 1 - \frac{\epsilon}{2} \left( \frac{k_1 d}{2} \right)^2 \right].$$ The field derived from (1) thus represents a resonant mode with resonant
frequency slightly below the cutoff frequency of the TM$_{01}$ mode, in
which the fields are localized to the vicinity of the dielectric disk.
The electric field configuration is sketched in Fig. 1. The longitudinal
extension of this ghost mode is described by the "$1/e$ distance"
$$x_0 = \frac{1}{(k_1^2 - k^2)^{1/2}} = \frac{\lambda_c}{2\pi (1 - \omega^2/\omega_c^2)^{1/2}}$$
where $\lambda_c = 2\pi/k_1 = 2.6a$ is the TM$_{01}$ cutoff wavelength.
Numerical values of $(x_0/\lambda_c)$ are indicated in Fig. 2. It is
seen that the ghost is surprisingly well localized; for example, in the
case $\omega = 0.99~\omega_c$, $x_0$ is less than 1.5 pipe diameters. If
the waveguide extends a distance three or four times $x_0$ on either
side of the dielectric disk, this ghost will be essentially nonradiating
and will have a very high Q, limited only by losses in the waveguide
walls and the dielectric.

Suppose this waveguide were being operated in the TE$_{11}$ propagating
mode, at frequencies near the TM$_{01}$ cutoff frequency. This is a
rather common condition in practice, since the TM$_{01}$ cutoff
frequency is only about 30 per cent higher than that of the TE$_{11}$
mode. In a perfect waveguide the fact that we were close to the
TM$_{01}$ propagating range would not cause any trouble. However, the
disk represents an "imperfection" in what would otherwise be a smooth
waveguide. The slightest asymmetry in structure near the disk, or the
slightest inhomogeneity in dielectric constant of the disk, can couple
the ghost to the TE$_{11}$ mode and cause a large absorption of energy
at the frequency given by (3). The field of the ghost can attain a
magnitude several hundred times that of the propagating TE$_{11}$ mode,
so that
<figure>
<figcaption>TM<span class="math inline"><sub>01</sub></span> ghost mode
due to a dielectric disk.</figcaption>
</figure>
<figure>
<figcaption>"(1/e) distance" of ghost modes as a function of
frequency.</figcaption>
</figure>
<figure>
<figcaption>Wall perturbations which create ghost modes.</figcaption>
</figure>
<figure>
<figcaption>Electric field lines of TE and TM ghost modes due to wall
imperfections.</figcaption>
</figure>
in a high-power device a ghost can cause breakdown. It was, in fact, the
persistent failure of ceramic windows in the output waveguides of
high-powered klystrons feeding the Stanford linear electron accelerator
(carrying about 20 megw at 3 kmc), which led to the recognition of ghost
modes. Spurious resonances in certain ferrite devices may also be
traceable to this cause.

What was said for the TM$_{01}$ mode evidently applies in general for
the structure of Fig. 1; every propagation mode of the waveguide is
accompanied by a ghost with the same transverse field pattern, localized
to the vicinity of the disk, with a resonant frequency slightly below
the corresponding cutoff frequency.
# General Ghost Modes
The presence of a dielectric is not necessary for existence of ghosts;
any localized imperfection in a waveguide will cause them to appear.
Consider first a perfect, infinitely long waveguide with zero loss,
excited in one of the propagation mode patterns at exactly its cutoff
frequency. It is thus a large resonant cavity with resonant frequency
$\omega_c$. Let the electric and magnetic fields in the vicinity of any
point P on the waveguide wall be E, H. Now if
$\epsilon_0 E^2 > \mu_0 H^2$, push the wall in slightly at P, while if
$\mu_0 H^2 > \epsilon_0 E^2$, pull out a small "blister" as in Fig. 3.
According to the Slater perturbation formula [1], the resonant
frequency of the cavity is always lowered by this change. But at any
lower frequency than $\omega_c$ the fields will be attenuated
exponentially as we move away from the imperfection; thus a ghost has
been created, trapped to the vicinity of the imperfection, with a
resonant frequency slightly lower than $\omega_c$. Two examples are
given in Fig. 4, in which only the electric field lines are sketched.
The Q of a ghost mode due to a small imperfection as in Fig. 4 is given
to order of magnitude by
$$Q \approx \frac{a}{\delta} = \frac{\text{waveguide radius}}{\text{skin depth}}$$
from which it is seen that values in excess of $10^4$ are easily
attained. For the ghost of any mode other than the lowest one, there
also will be a "loaded Q" involving the strength of coupling to
propagating modes.

Crude estimates of the frequency and longitudinal extension of these
ghosts, obtained from (4) and the Slater perturbation formula, are
$$\omega^2 \approx \omega_c^2 \left[ 1 - \left( \frac{\pi \alpha \delta V}{A \lambda_c} \right)^2 \right],$$
$$x_0 \approx \frac{A \lambda_c^2}{2\pi^2 \alpha \delta V}.$$ 

Here A is the cross-sectional area of the waveguide, $\delta V$ is the
volume added or removed by the imperfection, and $\alpha$ a
dimensionless quantity of the order of magnitude unity, given by
$$\alpha = \frac{|\mu_0 H^2 - \epsilon_0 E^2|}{\langle \mu_0 H^2 + \epsilon_0 E^2 \rangle_{Av}}$$
where the fields in the numerator are values near the imperfection,
while the denominator is an average over a waveguide cross section
passing through the imperfection [2].

From these formulas several general conclusions may be drawn. If the
imperfection is so small that $$\delta V < \frac{A \lambda_c}{100}$$ then one may expect the ghost to be separated from the cutoff frequency
by less than the bandwidth $\omega_c/Q$, so that it does not appear as a
well-resolved resonance, but only a slight broadening of the cutoff
region. If, on the other hand, $$\delta V > \frac{A \lambda_c}{100}$$ the ghost will generally appear as a distinct resonance. The
longitudinal extension $x_0$ of any well-resolved ghost will, from Fig.
2, never be more than a few times $\lambda_c$. The $\delta V$ required
by (10) is so large that the usual mechanical imperfections due to
machining errors, inadvertent hammer blows, etc., do not cause
separation of ghosts from the waveguide modes. However, installation of
almost any kind of apparatus inside a waveguide will cause them to
appear, as may the presence of any twist or bend.
# Periodic Structures
What was said above for waveguides applies equally well to any periodic
structure, such as those used in linear accelerators, traveling-wave
tubes, or, in fact, any lumped-constant filter composed of a cascade of
identical networks. By reasoning exactly like that in the preceding
section, one can show that any localized imperfection in such a
structure will cause a bound resonance to appear, with resonant
frequency just outside the pass band of the structure. In this case, it
may lie either above or below the pass band. Once again, the
imperfection has to be quite large in order to cause separation of a
well-resolved resonance, so that reasonable care in construction is
sufficient to avoid troubles due to these ghosts.

There is an interesting, and pedagogically useful, analogy with certain
well-known features of solid-state theory. Here a crystal represents a
three-dimensional periodic structure, and solutions of the Schrödinger
equation, in one-electron approximation, show an almost perfect
mathematical analogy with those in the corresponding electrical problem
[3]. In particular, the conduction bands of the crystal correspond to
pass bands of the filter, and any localized imperfection in the crystal
(such as a vacancy, interstitial atom, or impurity atom), results in at
least one localized bound state, with an energy just above or just below
the edge of a conduction band. In this way one can understand the
creation of donor or acceptor impurity levels involved in n-type and
p-type conductivity in semiconductors [4].

Further work on ghost modes, by M. Forrer and the writer, is being
prepared for publication. Experimental results, universal curves for
predicting the occurrence of ghosts, and discussion of their possible
use in waveguide filters and mode convertors will be included.
# Bibliography {#bibliography .unnumbered}
::: thebibliography
4 Slater, J. C. *Microwave Electronics*, New York: D. Van Nostrand
Company, Inc., 1950, p. 81. The derivation of (6) and (7) is a bit
tricky, since a small change in $\delta V$ alters the "length" $x_0$
of the cavity. One must apply the Slater formula only to infinitesimal
changes in $\delta V$, and integrate to obtain their cumulative effect.
For this reason the frequency shift involves $(\delta V)^2$ rather than
$(\delta V)$, as one might at first expect. Brillouin, L. *Wave
Propagation in Periodic Structures*, New York: McGraw-Hill Book Company,
Inc., 1946. Kittel, C. *Introduction to Solid-State Physics*. New York: John Wiley & Sons, Inc., 1953, Ch. 14.
:::

[^1]: Microwave Laboratory, Stanford University, Stanford, Calif.
[^2]: Original manuscript received by the IRE, September 6, 1957.