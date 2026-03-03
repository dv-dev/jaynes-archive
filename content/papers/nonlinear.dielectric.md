---
title: "Nonlinear Dielectric Materials"
year: 1955
abstract: >
  The following is a brief description of nonlinear
  dielectrics from the standpoint of the fundamental physics involved.
  Specific available materials and technical applications are considered
  only by way of illustration of general properties. It is shown that,
  although dielectric nonlinearity and ferroelectricity are quite
  different phenomena, the fact that ferroelectrics have high dielectric
  constants makes them the most likely materials to exhibit a high
  degree of nonlinearity at electric field strengths safely below the
  breakdown values.
author: ["E.T. Jaynes"]
categories: ["Electrodynamics & Signal Processing"]
tags: ["nonlinear dielectrics", "ferroelectricity", "dielectric constant", "barium titanate", "Rochelle salt", "Curie point", "polarization"]
---
## INTRODUCTION
The macroscopic electromagnetic properties of matter are commonly
described by specifying the current density J, electric displacement
D, and magnetic induction B as functions of the electric and
magnetic "intensities" E and H. In the majority of substances
these relations are found to be linear, leading to the definitions of
the conductivity, dielectric constant, and permeability tensors. The
meaning of the word "linear" must be made more precise as soon as we
consider time-varying fields; in particular, we must be careful to
distinguish between nonlinearity and dispersion. The simple statement
that D(t) is proportional to E(t) will not do; by common usage it is
understood that linearity is concerned with such a proportionality in
the frequency domain rather than in the time domain. Thus, consider a
Fourier integral representation of the fields: 
$$
\begin{aligned}
E(t) &= \int_{-\infty}^{\infty} E(\omega) e^{i\omega t} d\omega \\\\
D(t) &= \int_{-\infty}^{\infty} D(\omega) e^{i\omega t} d\omega
\end{aligned} \tag{1}
$$

 By linearity we mean that the material is characterized
by some unique function $\epsilon(\omega)$ such that
$$
D(\omega) = \epsilon(\omega) E(\omega). \tag{2}
$$

 This corresponds in general
to no simple relation between D(t) and E(t). Thus, a linear
dielectric material is characterized intuitively by the following
conditions:
1.  No frequencies are present in D(t) which not are present in
    E(t).
2.  If $E_1(t)$ produces $D_1(t)$, which we write compactly as
    $E_1 \rightarrow D_1$ and $E_2 \rightarrow D_2$, then
    $(a_1 E_1 + a_2 E_2) \rightarrow (a_1 D_1 + a_2 D_2)$, with similar
    definitions for linear conductors and magnetic media.

It is possible to have one but not both of these conditions satisfied:
for example, consider the corresponding magnetic properties of water
placed in a strong but inhomogeneous magnetic field. For applied
frequencies within the range of the proton Larmor frequencies, condition
1 is satisfied but not the superposition condition 2.[^3]

Strictly speaking, all such linear laws may be regarded as
approximations for several different reasons. In the first place, they
would presumably fail in any material substance at sufficiently high
field strengths; i.e., breakdown or saturation effects would occur.
Secondly, there really are no unique relations between the above vectors
since in the work of the highest accuracy one would always expect to
find that, for example, the electric displacement does not depend only
on the electric field, but also on every other physical condition of the
material such as temperature, state of stress and strain, degree of
illumination, and even the entire past history of the specimen. Thus,
even if it should be found that D is exactly proportional to E at
constant temperature, the fact that the dielectric constant so defined
is a function of temperature gives rise to electrocaloric effects, in
which a sudden change in electric field produces a change in
temperature. Thus, the linearity or nonlinearity of a substance could
depend on its degree of thermal contact with its surroundings; i.e., on
whether it is operated under isothermal or adiabatic conditions.

Similarly, if a dielectric is linear under conditions of constant
stress, it might not be so under conditions of constant strain. In
practice, however, these are usually extremely small effects.

Finally there are more esoteric examples provided by modern physical
theories, according to which even a perfect vacuum should have nonlinear
properties. In quantum electrodynamics one finds that the phenomenon of
scattering of light by light (a violation of condition 2) should occur
due to the formation and subsequent annihilation of electron-positron
pairs;[^4] the cross-section for this process is, however, so small that
experimental confirmation is not to be thought of. Another effect is
predicted by General Relativity; an electromagnetic field contains
energy and therefore mass. This produces a gravitational field which can
in turn deflect a light beam, again in violation of condition 2. Once
again, we do not expect any experimental confirmation in the laboratory!
In order to be extremely cautious about the experimental situation,
however, we note that electrical measurements of the highest accuracy
are never performed with intense fields; if appreciable deviations from
Maxwell's equations did occur in free space at field strengths in excess
of $10^5$ v/cm or $10^5$ oersted, they would almost certainly have
escaped experimental detection thus far.[^5]

In spite of the above considerations, the vast majority of substances is
found to be linear to a high degree of accuracy at all field strengths
commonly attained, hence we denote as "nonlinear" only those
substances in which there are substantial and easily demonstrable
effects arising from violation of conditions 1 or 2 above, occurring at
easily produced field strengths. Each such substance is potentially
capable of important technical applications, since by violation of
condition 1 we generate harmonics and beat frequencies, while violation
of condition 2 enables one to modulate one signal by the presence of
another.

In the case of conductivity and permeability, substances which are
nonlinear in the above sense have long been known; thyrite and, to a
certain extent, electrolytic cells and various solid-state devices, such
as rectifiers, may be regarded as media with nonlinear conductivity
(more correctly as circuit elements with nonlinear conductance), while
the hysteresis and saturation effects in ferromagnetic materials
represent great nonlinearity. By contrast, nonlinear dielectric
materials, although not entirely unknown in the past, have not until
recently been available in forms of interest to electrical engineers.
Probably the earliest known example of dielectric nonlinearity was the
discovery, over 80 years ago, of the Kerr electro-optical effect.[^6]
Glass and many liquids, in particular nitrobenzene, develop optical
birefringence in fairly strong electric fields; thus the dielectric
constant at optical frequencies varies with a low-frequency electric
field in violation of the superposition condition. An example of a
nonlinear capacitance at microwave frequencies is provided by crystal
rectifiers, particularly the germanium welded-contact variety,[^7] in
which the barrier capacitance varies strongly with bias voltage. By far
the most important nonlinear dielectrics, however, are the ferroelectric
crystals or ceramics.
## FERROELECTRICS
From a phenomenological point of view, ferroelectricity may be defined
as the electric analog of ferromagnetism, and the fundamental criterion
of ferroelectricity is the existence, at certain temperatures, of
hysteresis between D and E. The static electric displacement then
depends not only on the applied electric field but also on the past
history, in such a way that with sufficiently slow periodic variation of
E we obtain a D-E hysteresis loop exactly like the familiar B-H
curves of ferromagnetic materials. Above a certain temperature $T_c$,
called the Curie point, this hysteresis disappears, but the relation
between D and E may remain appreciably nonlinear up to temperatures
far above $T_c$. Since oscillograms illustrating these effects have been
published recently in this journal,[^8] they will not be repeated here.
In the neighborhood of the Curie point more complicated phenomena are
sometimes found.[^9]

Several distinct classes of ferroelectrics, with widely different
chemical composition and crystal structure, are now known. The first to
be discovered was Rochelle salt (sodium potassium tartrate
tetrahydrate), widely used for its piezoelectric properties.[^10] This
substance appears to be unique in that it possesses two Curie
temperatures ($-18^\circ$C and $+23^\circ$C) and is ferroelectric
between them. Other ferroelectric tartrates[^11][^12] show only a
single Curie point. Mueller[^13] has shown that the electrical,
mechanical, and thermal properties of Rochelle salt can be correlated
very satisfactorily by a single thermodynamic free-energy function valid
on both sides of the Curie points. This is important not only from the
standpoint of economy of description, but it indicates that the
ferroelectric-"paraelectric" phase transition at the Curie points is
probably not a very drastic rearrangement from a molecular point of view
as is the case in many phase transitions, for example, that between
diamond and graphite.[^14] This conclusion seems well established also
for the other classes[^15] of ferroelectrics.

Another class of ferroelectrics is represented by the salt potassium
dihydrogen phosphate, KH$_2$PO$_4$ and other substances of similar
chemical composition and crystal structure (i.e., the alkali and
ammonium phosphates and arsenates).[^16] Although they have found
applications based on their electro-optical properties, the fact that
their Curie points are at liquid-air temperatures limits their
usefulness as nonlinear dielectrics in the purely electrical sense.
KH$_2$PO$_4$ is at present unique in that the molecular mechanism of its
properties (different arrangements of hydrogen bonds) is probably
understood with greater certainty than for any other
ferroelectric.[^15][^17][^18]

The third class of ferroelectrics,[^19] represented by the cubic form of
barium titanate, BaTiO$_3$ and several similar substances, is at the
present time the most interesting from a theoretical standpoint and the
most useful in terms of applications. The Curie point of BaTiO$_3$ is at
120$^\circ$C, and at room temperature the most nearly perfect crystals
grown to date exhibit hysteresis loops with coercive force as low as 600
v/cm and a spontaneous polarization of about 26 microcoulombs/cm$^2$,
very much higher than in the first two classes of ferroelectrics. The
dielectric properties of BaTiO$_3$ single crystals above the Curie point
have been measured by Drougard, Landauer, and Young,[^20] with results
that may be summarized as follows. For crystals that are free to distort
in accordance with their electrostrictive properties (i.e., under
conditions of zero stress), the behavior is given within experimental
error by the free-energy function
$$
F(P, T) = F_0(T) + A(T) P^2 + B(T)P^4, \tag{3}
$$
 where P is the
dielectric polarization, $F_0$ the free energy at zero polarization
(which is irrelevant for dielectric properties, although it largely
determines the specific heat of the material), and A, B are linear
functions of temperature, given by the empirical equations 
$$
\begin{aligned}
A &= 3.8 \times 10^{-5} (T - 105) \\\\
B &= 4.5 \times 10^{-15} (T - 175),
\end{aligned} \tag{4}
$$
 which are in cgs units, with the temperature in degrees
centigrade. The electric field is, from thermodynamics,
$$
E = \partial F/\partial P = 2AP + 4BP^3. \tag{5}
$$

 Therefore, the incremental
(small signal) dielectric constant is
$$
\epsilon = 1 + 4\pi(\partial P/\partial E) = 1 + 4\pi/(2A + 12BP^2) \approx 4\pi A^2/(2A^3 + 3BE^2), \tag{6}
$$
 the approximation being valid at field strengths for which the cubic
term in (5) is small compared to the linear one. Since B is negative
in the temperature range where these experiments were performed
(119$^\circ$C to 150$^\circ$C), we have the rather surprising result
that application of a biasing field increases the dielectric constant of
the crystal. This phenomenon is seen clearly in the oscillograms of
Merz, and may be shown by thermodynamic arguments[^21] to be connected
with the fact that the crystals exhibit a first-order transition at the
Curie point; i.e., as the temperature is lowered, the spontaneous
polarization jumps discontinuously from zero to a finite value (about 18
microcoulombs/cm$^2$). Some of the first crystals grown, which were less
perfect, exhibited a second-order transition and, as required by
thermodynamics, a positive sign of B.[^22] It must be remembered,
however, that this increase due to bias occurs only under conditions of
zero stress, and therefore can be seen only at sufficiently low
frequencies, below all of the mechanical vibration modes of the crystal.
Measurements made at Stanford University by Mr. V. Varenhorst at
frequencies of 20, 40, and 120 mcs showed in all cases a decrease in
dielectric constant with bias voltage. The results were complicated by
temperature hysteresis effects which persist above the Curie point and
are not understood, but in a typical case at 40 mcs and 130$^\circ$C,
application of a biasing field of 1700 v/cm lowered the dielectric
constant from 6,700 to 6,000.

Growth of good single crystals of BaTiO$_3$ is still a difficult and
costly art, and most of its applications to date have involved the
ceramic material, often with various added impurities. The ceramic also
exhibits dielectric nonlinearity, a typical result being a decrease of
dielectric constant with biasing field such that a field of 10 kv/cm
lowers $\epsilon$ from 1,400 to 1,100, while a field of 30 kv/cm lowers
it to 700. Similar results have been found at Stanford University, with
an interesting additional qualitative observation that the loss tangent
of a ceramic at radio frequencies may be lowered substantially by
application of a biasing field of a few kv/cm. Further data on
properties of ceramics have been given by von Hippel.[^23]

Many details concerning the physical properties of BaTiO$_3$ have been
omitted here; in particular the phenomena of domain formation and motion
which are essential to an understanding of the properties of single
crystals below the Curie point. These have been described by
Forsbergh,[^24] Merz,[^25] and Little.[^26] A recent discussion of the
theory of ferroelectrics has been given by Devonshire.[^27]
## THEORY OF DIELECTRICS
It might be supposed that with modern knowledge of the properties of
atoms and molecules, it would be a straightforward matter to calculate
the dielectric constant of any material of known composition from first
principles. Unfortunately, this turns out to be an extremely complicated
problem on which little progress has been made; only in the case of
gases where the dielectric constant is very close to unity and the
similar case of dilute solutions of polar molecules in nonpolar liquids
can one claim quantitative success. Although it is easy to describe in
words the mathematical procedure that would give a rigorous treatment,
in practice one must make from the start drastic simplifications which
make it difficult to interpret whatever agreement or disagreement with
experiment is found. The basic reason for this is that the properties of
a crystal are not merely the properties of a single molecule, multiplied
by the number of molecules present, but the interactions between them
are an essential part of the picture, and these are never taken into
account in a correct way. From the point of view of quantum mechanics,
we would have to say that it is not meaningful in any precise way to
speak of the states and behavior of individual molecules or atoms, but
the only really correct attitude is the global one in which we enumerate
the possible quantum states (wave functions) of the crystal as a whole.
Almost without exception, however, theoretical treatments of dielectric
properties of solids have been based on the concepts developed by
Clausius and Mosotti about 100 years ago. Here one regards a solid as
composed of a large number of polarizable objects (in various cases the
mechanism of polarization may be thought of as distortion of electronic
distributions of atoms or ions, motion of ions, or rotation of molecular
aggregates having a permanent dipole moment) each with polarizability
$\alpha$, so that each object, in an electric field F, develops a dipole
moment 
$$
M = \alpha F. \tag{7}
$$

 The field F is not, however, the same
as the macroscopic applied field E; because of the interaction of the
polarizable objects with each other, there is an additional term
commonly taken as proportional to the net polarization, with a
proportionality constant $\beta$, known as the Lorentz factor.
$$
F = E + \beta P. \tag{8}
$$

 Lorentz showed that if the polarizable objects are
arranged in a cubic or random array, and each maintains the same
constant dipole moment (no thermal agitation effects), $\beta$ would
have the value $4\pi/3$. If there are N of these polarizable objects
per unit volume, the polarization is
$$
P = N \alpha F = N \alpha (E + \beta P), \tag{9}
$$
 so that the dielectric
susceptibility becomes 
$$
\chi = P/E = N\alpha / (1 - N\alpha\beta). \tag{10}
$$

 Introducing the dielectric constant
$$
\epsilon = 1 + 4\pi\chi, \tag{11}
$$
 and assuming the Lorentz value $\beta=4\pi/3$, we arrive at the well-known
Clausius-Mosotti formula
$$
\frac{\epsilon-1}{\epsilon+2} = \frac{4\pi N\alpha}{3}, \tag{12}
$$
 which is
presented in some textbooks as if it were a rigorous relation. Many
refinements of this treatment have been made, and a very complete
account of them may be found in the recent book of Böttcher.[^28] They
have led to some improvement in agreement with experiment but not to any
appreciably deeper understanding, because the basic concepts remain the
local polarizability and local field F, which in modern theory no
longer have a precise meaning. Nevertheless, this classical treatment
contains enough of the truth to be very useful in giving a qualitative
understanding of dielectrics, provided certain precautions are observed.
In the first place, (12) cannot be used when the polarizability is due
to freely rotating permanent dipoles (i.e., polar molecules) except in
the case of high dilution when it reduces to
$$
\epsilon - 1 = 4\pi N\alpha \ll 1. \tag{13}
$$

 From statistical mechanics, one
can calculate the polarizability of a rotating dipole of moment M,
with the result $\alpha = M^2/3kT$, with k Boltzmann's constant and
T the temperature in degrees Kelvin. Eq. (12) predicts an infinite
dielectric constant, i.e., ferroelectricity, when $N\alpha\beta>1$, so
that this should occur at sufficiently low temperatures for any
substance with rotating dipoles. However, if we insert the numerical
values, we find that many polar substances should be ferroelectric at
temperatures far above their boiling points! This is the famous
"4$\pi$/3 catastrophe," which was resolved by Onsager[^29] with the
observation that strong correlations between the motions of nearby
dipoles reduce the effective Lorentz factor; the results of his
approximate treatment are obtained if we formally replace $\beta$ in the
above equations by $4\pi/(2\epsilon+1)$; the opposite conclusion is then
obtained that ferroelectricity does not occur unless the polarizability
becomes infinite.

The fact that ferroelectricity is so easy to "explain" when one uses
poor mathematical approximations has long plagued theoreticians and has
delayed any reliable understanding of the true cause of
ferroelectricity. For example, Rochelle salt was for many years treated
as an assembly of rotating dipoles exhibiting the catastrophe of (12).
Another example of a model which predicts ferroelectricity as a result
of poor approximation is an array of harmonic oscillators interacting
with each other. Such an oscillator with a particle of charge e, mass
m, and resonant frequency $\omega$ has a temperature-independent
polarizability of $e^2/m\omega^2$, and therefore according to the above
equations one can always produce a ferroelectric array by making the
resonant frequency sufficiently small. However, this model is so simple
that it can be treated rigorously; an orthogonal transformation of
coordinates enables one to find the states of the array as a whole, and
it is found when the problem is treated correctly that ferroelectricity
cannot occur unless the polarizability of a single oscillator becomes
infinite. We also note that Slater's theory of KH$_2$PO$_4$, already
mentioned as probably the best available theory of a ferroelectric, does
not make use of electrostatic interactions but rather ones of a more
direct mechanical nature. In spite of these and other
considerations,[^30] many people believe that in barium titanate we have
the realization of the classical polarization catastrophe; in the present
writer's opinion it is doubtful whether any existing theory is free of the
effects of poor approximations of the above type, and interactions other
than electrostatic may well be the essential ones.

If, disregarding these precautions, we assume that a classical type of
theory should have at least a qualitative usefulness, what can be said
about the expected occurrence of dielectric nonlinearity? According to
the above equations, this would require that either the polarizability
or the Lorentz factor be field-dependent. We consider separately the
three cases that the polarization is due to: (a) rotating permanent
dipoles; (b) translational motion of ions; or (c) electronic distortion
of atoms or ions.
(a) *Rotating Dipoles*. The polarizability $\alpha = M^2/3kT$ given
above is an approximation valid only at field strengths F such that
$MF \ll kT$. The exact expression, first calculated by Langevin in 1905,
is 
$$
\alpha = (M/F)L(a) = M^2/3kT - M^4F^2/45k^3T^3 + \dots, \tag{14}
$$
 where
$L(a) = \coth a - a^{-1}$ is the Langevin function and $a=MF/kT$. From
this we find that at a=1 the polarizability is lowered by about 6 per
cent, and for a>5, L(a) is essentially equal to unity, so that
$\alpha$ varies inversely as the internal field F. Since molecular
dipole moments are of the order of $10^{-18}$ esu, we find that at room
temperature an appreciable nonlinearity could be expected only for F
greater than about $4 \times 10^4$ esu, or $1.2 \times 10^7$ v/cm. Since
we must remember to use the Onsager field for F, the applied field E
would have to be of the same order of magnitude; thus a measurable
nonlinearity due to saturation of rotating dipoles could be expected
only at very low temperatures and intense field strengths.
(b) *Translational Motion of Ions*. Here the prospects are
considerably brighter. In many types of crystals the size of the lattice
is determined by the larger ions that have to fit into it, and if small
ions are also present, they may be free to move in the interstices,
through distances of an appreciable fraction of an Angstrom, but cannot
move further due to contact with the larger ions. It is seen without any
calculation that this results in a contribution to the polarization of
the crystal which saturates rather abruptly at a certain value.

KH$_2$PO$_4$ is undoubtedly of this type, with movable hydrogens; other
crystals of similar structure, even though not ferroelectric, might be
expected to show nonlinearity. However, materials with high dielectric
constants should provide the most favorable possibilities, since
according to the above equations we then obtain an internal field F
which is considerably "amplified" above the applied field E. If
appreciable motion occurs, the Lorentz factors might also vary.
(c) *Electronic Distortion*. As a simple example, consider an atom
which has a ground state $\psi_0$ with energy $E_0$, and an excited
state $\psi_1$ with energy $E_1$, such that the matrix element of the
dipole moment operator between them,
$$
M_{01} = e \int \psi_0^* z \psi_1 dV \tag{15}
$$
 does not vanish.[^31]

Using quantum mechanics and statistical mechanics,[^32] the following
formula for polarizability may be obtained:
$$
\alpha = \frac{|M_{01}|^2 \tanh a}{k T a} \tag{16}
$$
 where
$$
a = \frac{[4(E_1-E_0)^2 + |M_{01}|^2 F^2]^{1/2}}{kT} \tag{17}
$$

 It is seen
that appreciable nonlinearity requires that a be of order unity or
greater and that the term in $F^2$ must contribute substantially to a.
Therefore, since $M_{01}$ will typically be of the order of magnitude
$10^{-18}$ esu, if the two energy levels are sufficiently close together
the situation is about the same as in the case of rotating dipoles. If a
high dielectric constant leads to great internal field strengths, these
conditions might be met, although it appears that the case of movable
ions remains the most favorable to development of strong nonlinearity.
Reprinted from the PROCEEDINGS OF THE I.R.E.

VOL. 43, NO. 12, DECEMBER, 1955
PRINTED IN THE U.S.A.
## FOOTNOTES
[^1]: Microwave Laboratory, Stanford University, Stanford, Calif.
[^2]: Original manuscript received by the IRE, October 14, 1955.
[^3]: F. Bloch, *Phys. Rev.*, vol. 70, p. 460; 1946. A. Bloom, *Phys. Rev.*, vol. 98, p. 1105; 1955.
[^4]: O. Halpern, *Phys. Rev.*, vol. 44, p. 855; 1934. H. Euler and B. Kockel, *Naturwiss.*, vol. 23, p. 246; 1935.
[^5]: There is, of course, indirect evidence associated with atomic theory suggesting that the laws of electrostatics hold at field strengths far beyond this limit; for example, the fact that the wavelengths of the spectral lines of hydrogen can be calculated to great accuracy on the assumption that the electric field of the nucleus is a coulomb field. However, this could hardly be called an electrical measurement.
[^6]: M. Born, "Optik," p. 365, J. Springer, Berlin; 1933.
[^7]: H. C. Torrey and C. A. Whitmer, "Crystal Rectifiers," Chap. 13, M.I.T. Radiation Laboratory series No. 15; McGraw-Hill Book Co., Inc., New York; 1948.
[^8]: W. P. Mason and R. F. Wick, "Ferroelectrics and the dielectric amplifier," PROC. IRE, vol. 42, pp. 1606-1620; November, 1954.
[^9]: W. J. Merz, *Phys. Rev.*, vol. 91, p. 513; 1953.
[^10]: W. G. Cady, "Piezoelectricity," McGraw-Hill Book Co., Inc., New York, 1946.
[^11]: W. J. Merz, *Phys. Rev.*, vol. 82, p. 562; 1950, vol. 83, pp. 226, 656; 1951.
[^12]: B. T. Matthias and J. K. Hulm, *Phys. Rev.*, vol. 82, pp. 108; 1951.
[^13]: H. Mueller, *Phys. Rev.*, vol. 47, p. 175; 1935, vol. 57, pp. 829-842; 1940, vol. 58, pp. 565-805; 1941, *Zeit. Krist.*, vol. 99, p. 122, 1938, *Ann. N. Y. Acad. Sci.*, vol. 40, p. 321; 1940.
[^14]: R. Smoluchowski, et al., "Phase Transformations in Solids," John Wiley & Sons, New York; 1951.
[^15]: H. R. Danner and R. Pepinsky, *Phys. Rev.*, vol. 99, p. 1215; 1955.
[^16]: G. Busch and P. Scherrer, *Naturwiss.*, vol. 23, p. 737; 1935. G. Busch, *Helv. Phys. Acta.*, vol. 11, p. 269, 1938. C. C. Stephenson and J. G. Hooley, *Phys. Rev.*, vol. 56, p. 121; 1939. W. Bantle and P. Scherrer, *Nature*, vol. 143, p. 980; 1939. J. and K. Mendelssohn, *Nature*, vol. 144, p. 595, 1939.
[^17]: J. C. Slater, *Jour. Chem. Phys.*, vol. 9, p. 16; 1941.
[^18]: C. C. Stephenson and J. G. Hooley, *Jour. Am. Chem. Soc.*, vol. 66, p. 1937; 1944.
[^19]: von Hippel, Breckenridge, Chesley, and Tisza, *Jour. Ind. Eng. Chem.*, vol. 38, p. 1097; 1946.
[^20]: M. E. Drougard, R. Landauer, and D. R. Young, *Phys. Rev.*, vol. 98, p. 1010; 1955.
[^21]: E. T. Jaynes, "Ferroelectricity," Princeton University Press, Princeton, N. J., Chap. 3; 1953.
[^22]: W. J. Merz, *Phys. Rev.*, vol. 76, p. 1221; 1949.
[^23]: A. von Hippel, "Dielectric Materials and Applications," John Wiley & Sons, New York; 1954.
[^24]: P. W. Forsbergh, Jr., *Phys. Rev.*, vol. 76, p. 1187; 1949.
[^25]: W. J. Merz, *Phys. Rev.*, vol. 88, p. 421, 1952; vol. 95, p. 690; 1954.
[^26]: E. A. Little, *Phys. Rev.*, vol. 98, p. 978; 1955.
[^27]: A. F. Devonshire, *Phil. Mag. Suppl.*, vol. 3, p. 85; 1954.
[^28]: C. J. F. Böttcher, "Theory of Electric Polarisation," Elsevier Press, Amsterdam; 1952.
[^29]: L. Onsager, *Jour. Am. Chem. Soc.*, vol. 58, p. 1486; 1936.
[^30]: J. M. Luttinger and L. Tisza, *Phys. Rev.*, vol. 70, p. 954, 1946; vol. 72, p. 257; 1947.
[^31]: L. I. Schiff, "Quantum Mechanics," McGraw-Hill Book Co., Inc., New York, sec 25; 1949.
[^32]: See ref. 21 (pp. 58-60) for a similar calculation.
