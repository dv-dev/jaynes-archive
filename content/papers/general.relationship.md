---
title: "General Relationships Between Ultrasonic Attenuation and Dispersion"
year: 1978
abstract: >
  General relationships between the ultrasonic attenuation and dispersion
  are presented. The validity of these nonlocal relationships hinges only
  on the properties of causality and linearity, and does not depend upon
  details of the mechanism responsible for the attenuation and dispersion.
  Approximate, nearly local relationships are presented and are
  demonstrated to predict accurately the ultrasonic dispersion in
  solutions of hemoglobin from the results of attenuation measurements.
author: ["M. O'Donnell[^100]", "E.T. Jaynes", "J.G. Miller[^100]"]
---
PACS numbers: 43.80.Cs, 43.35.Bf

The purposes of this letter are twofold: (1) to explore the implications
of the existence of general relationships between the ultrasonic
attenuation and the frequency dependence of the ultrasonic phase
velocity (i.e., dispersion) for identifying specific mechanisms
responsible for the propagation of ultrasound in some media, and (2) to
present nearly local forms of these general relationships. We illustrate
the use of these nearly local relationships for cases of ultrasonic
propagation in media of biomedical interest, an area in which the
mechanisms governing the propagation remain obscure.

Relationships between attenuation and dispersion, sometimes called
Kramers--Kronig or generalized dispersion relationships, have proved
useful in several areas of physics.[^1][^2] Expressed in a form
appropriate to ultrasonic studies, these relationships take the form
$$
K_I(\omega) = C_0 - \frac{2}{\pi} \int_0^\infty \frac{\omega^\prime \alpha(\omega^\prime)}{(\omega^\prime)^2 - \omega^2} d\omega^\prime  ,
\tag{1}
$$
$$
K_R(\omega) = \frac{2\omega^2}{\pi} \int_0^\infty \frac{\alpha(\omega^\prime)}{\omega^\prime((\omega^\prime)^2 - \omega^2)} d\omega^\prime  ,
\tag{2}
$$
where $K_I(\omega)$ and $K_R(\omega)$ are the real and imaginary parts,
respectively, of the dynamic compressibility (inverse of the bulk
modulus). If the ultrasonic wave vector is written as
$k=\omega/C(\omega)+i\alpha(\omega)$, then $C(\omega)$ is the phase
velocity and $\alpha(\omega)$ is the attenuation coefficient for the
incident wave, as observed in transmission (i.e., direct "straight-line"
propagation) measurements.

The following considerations involve only this total attenuation
coefficient, and do not depend on details of the ultimate physical
mechanism (i.e., absorption, scattering, or a mixture of both). That is,
the effect on the incident wave of removing energy from it is the same
whether that removed energy is converted immediately into heat, or
whether it goes first into scattered waves which subsequently decay into
heat. Indeed, there is no sharp distinction between these mechanisms; a
local absorption of energy can always be thought of as the limit of a
scattered wave which propagates only a short distance. In either case,
the effect on the incident wave can be represented by a phenomenological
compressibility $K(\omega)$ obeying Eqs. (1) and (2), which can be used
to derive the relationship between the attenuation and dispersion. In
the limit $\alpha(\omega)C(\omega)/\omega \ll 1$ (i.e., if the real part
of the wave vector is much larger than its imaginary part), the real and
imaginary parts of the compressibility can be directly related to the
attenuation coefficient and phase velocity such that
$$
C(\omega) = [\rho_0 K_R(\omega)]^{-1/2},
\tag{3}
$$
$$
\alpha(\omega) = \frac{1}{2}\rho_0 C(\omega) K_I(\omega).
\tag{4}
$$

Using Eqs. (1) and (3) the dispersion at a specified frequency can be
computed from a knowledge of the attenuation at all frequencies.

Conversely, if the dispersion is known at all frequencies, the
attenuation at any specified frequency can be computed from Eqs. (2) and
(4).

The validity of the general form of the Kramers--Kronig relationships
[Eqs. (1) and (2)] hinges only on the properties of causality (that an
effect does not precede its cause) and linearity (that a response is
approximately proportional to the stimulus). We make the usual physical
assumption that a spatially local compressibility exists, relating
pressure and density, in a region large compared to atomic dimensions,
but small compared to a wavelength.

For present purposes the significant feature of these relationships is
that they do not depend upon details of the specific mechanism
responsible for the attenuation and dispersion. As illustrated below,
the existence of these completely general relationships renders invalid
attempts to compare the attenuation and dispersion as a means of
validating any specific model proposed to account for the propagation of
ultrasound in some medium, as some authors appear to have
attempted.[^5][^6]

In the form given by Eqs. (1) and (2) the Kramers--Kronig relationships
are limited in usefulness because of their nonlocal character; i.e., a
knowledge of either the attenuation or the dispersion for all
frequencies is required. More useful, approximate attenuation-dispersion
relationships in a nearly local form can be obtained from the nonlocal
form using an approach analogous to that used by Bode in the study of
the relationship between the gain and phase shift of an amplifier.[^7]
The nearly local forms of the attenuation-dispersion relationships are
obtained from the exact nonlocal forms given in Eqs. (1) and (2) under
the assumptions that the attenuation and dispersion are sufficiently
small and do not change rapidly over the frequency range of interest. A
review of the derivation of Eqs. (1) and (2) and a discussion of the
range of validity of the approximate relationships presented below will
be presented in a subsequent publication.[^8] The nearly local
relationships are
$$
\alpha(\omega) \simeq (\pi\omega^2 / 2C_0^2) dC(\omega)/d\omega,
\tag{5}
$$
$$
\Delta C(\omega) = C(\omega) - C_0 \simeq \frac{2C_0^2}{\pi} \int_{\omega_0}^{\omega} \frac{\alpha(\omega^\prime)}{(\omega^\prime)^2}d\omega^\prime  ,
\tag{6}
$$
where $\omega_0$ is some convenient reference frequency and
$C_0=C(\omega_0)$ is the phase velocity at this reference frequency.
Although strictly appropriate only under rather restrictive conditions,
Eqs. (5) and (6) appear to be excellent approximations for cases
encountered in the study of soft tissue. In Table I we indicate the
frequency dependences observed for classical viscous losses and for the
attenuation in most soft tissues. The corresponding frequency
dependences for the dispersion are predicted using Eq. (6). From Table
I, if the attenuation varies linearly with frequency, the dispersion
should vary logarithmically with frequency, regardless of the details of
the specific mechanism responsible for the linear frequency dependence
of the attenuation.

| Description | Frequency dependence of attenuation $\alpha(\omega)$ | Frequency dependence of $\Delta C(\omega)$ |
| :--- | :--- | :--- |
| Classical Viscous | $\omega^2$ | $\omega$ |
| "Soft Tissue" | $\omega$ | $\ln \omega$ |

**Table I:** Observed frequency dependences of attenuation coefficient $\alpha$ for classical viscous losses and for the case of soft tissue, and corresponding frequency dependences of $\Delta C$ predicted from Eq. (6).

To illustrate the use of the nearly local attenuation-dispersion relationships, we present in Fig. 1(a) the attenuation measured as a function of frequency by Carstensen and Schwan[^5] in two solutions of hemoglobin. In Fig. 1(b) we compare the dispersion measured by Carstensen and Schwan to the dispersion predicted on the basis of the measured attenuation and Eq. (6), where $C_0$ was taken to be the phase velocity at 1 MHz.

Agreement between the measured and predicted dispersion is excellent. Further, if the dispersion data are plotted on a logarithmic frequency scale, the data lie approximately on a straight line, in agreement with the prediction of Table I for the case of a nearly linear dependence of attenuation on frequency.

**[FIGURE: (a) The attenuation coefficient measured by Carstensen and Schwan is plotted as a function of frequency for hemoglobin solutions of two concentrations. (b) The change $\Delta C$ in the velocity of sound from its value $C_0$ at 1 MHz is displayed as a function of frequency for the same two solutions. The data points correspond to measurements made by Carstensen and Schwan, and the dashed curves were computed using Eq. (6) and the attenuation data of Fig. 1(a).]**

These results demonstrate the need for determining which features of
ultrasonic propagation are determined by general laws of physics, as
opposed to those features which are specific to the particular mechanism
of propagation. An appreciation of the distinction should prove useful
in establishing the mechanisms responsible for the propagation of
ultrasound in biologically interesting specimens. The same lesson was
learned many years ago by workers in ferromagnetism and
ferroelectricity, with the emergence of a general rule that only
experiments at the molecular level can distinguish reliably between
different molecular models.
## ACKNOWLEDGMENT
Supported in part by grants NIH HL19537, NSF APR7709776, and NASA NSG 1392.
## References
[^1]: R. Kronig, "On the Theory of Dispersion of X-rays," J. Opt. Soc. Am. **12**, 547 (1926).
[^2]: R. Kronig and H. A. Kramers, "Absorption and Dispersion in X-Ray Spectra," Zeits f. Phys. **48**, 174 (1928).
[^3]: L. D. Landau and E. M. Lifshitz, *Statistical Physics* (Addison-Wesley, Reading, MA 1958), pp. 392--398.
[^4]: V. Mangulis, "Kramers-Kronig or dispersion relations in acoustics," J. Acoust. Soc. Am. **36**, 211 (1964).
[^5]: E. L. Carstensen and H. P. Schwan, "Acoustic Properties of Hemoglobin Solutions," J. Acoust. Soc. Am. **31**, 305 (1959).
[^6]: P. N. T. Wells, "Absorption and Dispersion of Ultrasound in Biological Tissue," Ultrasound Med. Biol. **1**, 369 (1975).
[^7]: H. W. Bode, "Relations Between Attenuation and Phase in Feedback Amplifier Design," Bell Syst. Tech. J. **19**, 421 (1940).
[^8]: M. O'Donnell, E. T. Jaynes, and J. G. Miller (unpublished).
[^100]: Laboratory for Ultrasonics, Department of Physics, Washington University, St. Louis, Missouri 63130.
