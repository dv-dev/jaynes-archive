---
title: "Resonant Modes in Waveguide Windows"
author: ["M. P. Forrer", "E.T. Jaynes"]
year: 1960
abstract: >
  Analysis and experimental verification of a class of resonant fields, called ghost-modes, occurring in waveguide dielectric windows are presented. Numerical solutions for a simple geometry are given through universal curves. Knowledge about ghost-modes has importance to designers of high-power windows. It also leads to a measuring technique for dielectric constants through a frequency measurement.
---
## Introduction {#introduction .unnumbered}
THE general phenomenon of ghost-modes in imperfect waveguides, special
cases of which have been noted before, was predicted by one of the
authors.[^4] The present paper presents a quantitative analysis and
confirming experiments of a class of ghost-mode resonances occurring in
a particularly simple waveguide window, where exact analysis, using
transmission-line theory, is applicable. A ghost-mode is a resonant
electromagnetic field configuration, existing in the vicinity of certain
waveguide obstacles, such as dielectric windows. Its transverse field
configuration is that of an ordinary waveguide mode and its resonant
frequency lies below the cutoff frequency of the particular mode in the
unperturbed guide. Thus, the ghost-mode fields decay exponentially on
either side of the waveguide obstacle and no energy travels away. Within
the region of the obstacle the z-variation of the fields must have
oscillatory character.
## Analysis {#analysis .unnumbered}
A window configuration simple enough to allow exact analysis is shown in
Fig. 1. The dielectric slab shall be homogeneous and isotropic; the
surrounding waveguide shall be straight and lossless, but its
cross-sectional shape may be arbitrary. Under these assumptions the
window does not introduce modal conversions, and analysis may proceed
using conventional transmission-line theory.
**[FIGURE: Transverse dielectric slab window.]**
wave impedance
$$
Z_{wn} = Z_0 \left\{ \begin{array}{l} k/k_{an} \\\\ k_{an}/k \end{array} \right. ,
$$
where the upper and lower expressions within curly brackets relate to TE
and TM modes, respectively. The quantities $Z_0$ and $k$ are the
free-space impedance and the free-space propagation constant. The
waveguide propagation constant of the nth mode is
$k_{an} = \sqrt{k^2 - k_{cn}^2}$. We shall be interested in frequencies
below waveguide cutoff. Here it is convenient to replace $jk_{an}$ by
the real, positive quantity $k^\prime_{an} = \sqrt{k_{cn}^2 - k^2}$ in all
expressions. The wave impedance, for example, becomes
$$
Z^\prime_{wn} = jZ_0 \left\{ \begin{array}{l} k/k^\prime_{an} \\\\ -k^\prime_{an}/k \end{array} \right.
$$

In the guide completely filled with material of dielectric constant
$\epsilon$, one has
$$
Z_{wn}^{(\epsilon)} = Z_0 \left\{ \begin{array}{l} k/\beta_n \\\\ \beta_n/\epsilon k \end{array} \right.
$$
where $\beta_n = \sqrt{\epsilon k^2 - k_{cn}^2}$ is the propagation
constant of the nth mode in the dielectric filled guide.

The geometrical configuration (Fig. 1) has a symmetry plane $z=0$. Any
resonant fields, therefore, have symmetry properties with respect to
$z=0$, which may be of an even or odd character. Analytically, advantage
is taken of this fact by considering only the region $z>0$ under the
condition of an electric or magnetic short circuit at $z=0$.
### Electric Short at z=0: $Z_{wn}(0)=0$ {#electric-short-at-z0-z_wn00 .unnumbered}
Under this condition, the impedance at the dielectric-air interface
($z=L/2$) is 
$$
Z_{wn}(L/2) = jZ_{wn}^{(\epsilon)} \tan \beta_n L/2.
$$

Continuity of tangential field components at the dielectric-air
interface requires continuity of wave impedance,
$$
Z_{wn}(L/2) = Z^\prime_{wn}.
$$

 Substituting (2)-(4) into (5) yields
$$
\begin{align}
\tan \beta_n L/2 &= -\beta_n/k^\prime_{an} \\\\
\tan \beta_n L/2 &= \epsilon k^\prime_{an}/\beta_n
\end{align}
$$

 Frequencies that satisfy this equation are the ghost-mode
resonant frequencies. The impedance at the dielectric-air interface
becomes 
$$
Z_{wn}(L/2) = jZ_{wn}^{(\epsilon)} \cot \beta_n L/2,
$$
 and the
continuity condition of tangential fields at $z=L/2$ leads to
$$
\begin{align}
\cot \beta_n L/2 &= \beta_n/k^\prime_{an} \\\\
\cot \beta_n L/2 &= -\epsilon k^\prime_{an}/\beta_n
\end{align}
$$

 Eqs. (6b) and (8a) always have at least one real
solution.[^5] A field analysis shows that these solutions are
characterized by *even* symmetry of their longitudinal field component.
They will be called even modes, and the number $N_e$ of such solutions
is determined by
$$
N_e - 1 < \sqrt{\epsilon-1} \frac{k_{cn}L}{2\pi} < N_e.
$$

 On the other
hand, (6a) and (8b) have real solutions only when $\epsilon$ and $L$
exceed certain minimum values. Solutions obtained in such cases exhibit
*odd* symmetry of their longitudinal field component, and will be called
odd modes. In general, there exist $N_o$ odd modes, if
$$
N_o < \sqrt{\epsilon-1} \frac{k_{cn}L}{\pi} < N_o + 1.
$$

 Resonant
field patterns corresponding to the lowest frequency solutions for some
simple waveguide modes are sketched in Fig. 2. The upper-right and
lower-left hand patterns correspond to (6), the others correspond to
(8). Eqs. (6) and (8) may be solved graphically by our plotting both
sides of the equations as functions of frequency, $k/k_{cn}$, and
determining the points of intersection. Such solutions, obtained for
various values of $\epsilon$ and $k_{cn}L$, are shown in Figs. 3 and 4.
Typically, the TE resonant frequencies decrease faster than the TM
resonant frequencies, as $k_{cn}L$ is increased. All curves approach the
value $(k/k_{cn})_{\text{res}} = \epsilon^{-1/2}$ for very large $k_{cn}L$.
This is true for both TE and TM resonant modes and is plausible from the
fact that for very large $k_{cn}L$ practically the entire field is
confined to the inside of the dielectric, and resonances occur, in a
well-known manner, when the dielectric is an integral number of half
wavelengths long.
## Experimental Verification of Ghost-Modes {#experimental-verification-of-ghost-modes .unnumbered}
The ghost-mode resonances derived above are experimentally verified by
an arrangement shown in Fig. 5. A window sample was placed into the
center of a three-inch ID circular waveguide section. Both ends of the
approximately two-foot long section were left open, since the modes of
interest are below waveguide cutoff and have substantially decayed when
reaching the open
ends.
**[FIGURE: Sketch of the lowest TE and TM ghost-mode field patterns of an even and an odd symmetry. (The transverse field variations shown apply to TE$_{1\phi}$ and TM$_{11}$ in rectangular guide or TE$_{11}$ and TM$_{01}$ in circular guide.)]**
**[FIGURE: Ghost-mode experiment.]**
Microwave energy was loosely coupled to the guide through an
electric probe at the guide wall, approximately four inches away from
the dielectric. A similar probe, located on the opposite side of the
dielectric, was connected to a crystal rectifier and an indicator. The
coupling between the probes is small, so that strong indicator
deflections occur only at resonance conditions in the guide. Such
resonances, observed below 3 kmc, were identified as TE$_{11}$ and
TM$_{01}$ ghost-modes, by observing the transverse symmetries of the
residual fields at the open guide ends with a small perturbation rod. To
vary the slab thickness $L$, one or more ceramic discs ($\epsilon=8.79$)
of $\frac{1}{8}$-inch thickness were stacked up. The observed ghost-mode
frequencies are marked on Fig. 6, which also contains the theoretical
curves for the particular arrangement as a comparison.

The approximate Q factors indicated were determined from the half-power
bandwidth of the resonances. The Q factors generally decrease for larger
slab thickness because the resonant fields become more and more confined
to the volume of the relatively lossy dielectric.

The good agreement between theoretical and experimental data in Fig. 6
may be taken as a confirmation of the fact that the dielectric constant
is known to good accuracy. Conversely, one might well make use of the
described experiment to determine unknown dielectric constants of slabs
by measuring a ghost-mode resonant frequency. Error analysis applied to
the lowest TE$_{11}$ ghost-mode in our experiment yields
$$
\frac{\Delta \epsilon}{\epsilon} = -15.5 \left( \frac{\Delta f}{f} \right)_{res}
$$
for a slab of $\frac{1}{8}$-inch thickness (neglecting geometrical
errors). Considering the precision attainable in frequency measurements,
this appears encouraging. If the dielectric constant of the slab is
large, a possible air gap $\delta$ between the dielectric and the
waveguide wall may be-
**[FIGURE: Universal curves showing TE ghost-mode resonant frequencies of a transverse dielectric slab.]**
**[FIGURE: Universal curves showing TM ghost-mode resonant frequencies of a transverse dielectric slab.]**
**[FIGURE: Ghost-mode resonant frequencies of ceramic discs ($\epsilon = 8.79$) of various thickness L. Curves are computed, dots are measured.]**
come troublesome. It may introduce an error of the following order of
magnitude:
$$
\left( \frac{\Delta f}{f} \right)_{res} = \frac{1}{2} \frac{\epsilon(\delta/a)}{1+\epsilon(\delta/a)},
$$
where a is a transverse waveguide dimension, e.g., waveguide radius.
## Conclusion {#conclusion .unnumbered}
The phenomenon of resonant ghost-modes existing in the vicinity of a
dielectric window has been discussed both theoretically and
experimentally for the simplest geometry available. In practice, the
ghost-mode resonances of some higher-order waveguide modes may coincide
with the operating frequency of the dominant waveguide mode. Since these
modes are orthogonal, no coupling would be expected under ideal
conditions. However, imperfections, such as a slight tilt of the window,
uneven thickness, or inhomogeneous dielectric may provide the modal
coupling.

Waveguide discontinuities (irises, couplers, bends, etc.) located in the
vicinity of the window may also provide this function. Since the
ghost-mode resonances have high Q, only a small amount of coupling is
required to produce appreciable resonant fields.

High-power microwave signals are very likely accompanied by harmonics.
These harmonic frequencies may coincide with ghost-mode resonances, and
coupling may be provided by imperfections or discontinuities.

Appreciable excitation of ghost-modes may considerably lower the
breakdown power of a waveguide window. Rather than minimizing the
coupling to these modes by close tolerances, the window designer may
find the information of Figs. 3 and 4 useful to avoid the existence of
ghost-modes within the operating frequency range.

Ghost-mode resonances may exist in dielectric windows of more
complicated geometry than that discussed above. Examples include slanted
dielectric plates and ceramic cones. Analysis of such configurations
becomes complicated. Transmission-line theory is no longer useful, but
the mathematical tool of a normal-mode expansion may be employed and
yields approximate results.[^6] Such windows of increased complexity
generally couple many waveguide modes together. A ghost-mode is,
therefore, no longer a pure waveguide mode in its transverse field
configuration. Moreover, if such a ghost-mode is strongly coupled to the
propagating dominant waveguide mode, its external Q factor may become
rather small, so that the resonance is less pronounced.

The existence of ghost-modes in dielectric obstacles of arbitrary shape
may be made plausible by the following: the insertion of dielectric
material ($\epsilon > 1$) into the guide effects an increase in
\"electrical cross section\" of the guide, so that a wave may have
propagating character (i.e., oscillatory z-variation) within the length
L of the obstacle, while it decays outside. The frequencies at which the
impedance boundary conditions on both sides of the obstacle can be met
are the ghost-mode resonances.

Analysis of ghost-modes for any given window geometry makes it possible
to determine the dielectric constant of the material through a frequency
measurement. Even without analysis, a ghost-mode resonance measurement
may be useful as a uniformity test of dielectric samples.

It is of interest to note the behavior of two windows (of the kind shown
in Fig. 1) placed in the same waveguide. If the distance between them is
such that the ghost-mode fields overlap, there appear two resonant
frequencies, one being slightly higher, the other slightly lower than
the original ghost-mode resonance. The situation is analogous to coupled
resonant tanks. It may be analyzed by use of the same methods as were
employed above. Such analysis and corresponding experiments have been
performed and show good agreement. This experiment is particularly
interesting as it represents one of the rare cases where the coupling
between resonant circuits may be found easily and accurately through
analysis.

Finally, it might be noted that the location of ghost-mode resonances
represents a simple but unusually interesting laboratory experiment by
which several aspects of waveguide theory can be demonstrated in the
teaching of microwave techniques.

[^1]: General Electric Microwave Lab., Palo Alto, Calif.
[^2]: Microwave Lab., W. W. Hansen Labs. of Physics, Stanford
    University, Stanford, Calif.

[^3]: Manuscript received by the PGMTT, August 31, 1959. The research
    reported in this paper was supported jointly by the U. S. Army
    Signal Corps, the U. S. Air Force, and the U. S. Navy (Office of
    Naval Research).

[^4]: E. T. Jaynes, \"Ghost modes in imperfect waveguides,\" PROC. IRE,
    vol. 46, pp. 415-418; February, 1958. (Note that Fig. 2 in this
    reference was incorrectly drawn; the curves should be rotated 180°
    in the plane of the paper, about an axis passing through the center
    of the diagram.)

[^5]: A field analysis shows that these solutions are characterized by
    even symmetry of their longitudinal field component. They will be
    called even modes, and the number $N_e$ of such solutions is
    determined by
[^6]: M. P. Forrer, \"On the Boundary Value Problem of Waveguide
    Windows,\" W. W. Hansen Labs. of Physics, Stanford University,
    Stanford, Calif., Microwave Lab. Rept. No. 575; March, 1959.
