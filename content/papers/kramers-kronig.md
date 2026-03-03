---
title: "Kramers-Kronig relationship between ultrasonic attenuation and phase velocity"
year: 1980
abstract: >
  Kramers-Kronig relations linking the attenuation and dispersion are
  presented for a linear acoustic system. These expressions are used as
  a starting point to derive approximate, nearly local expressions
  relating the ultrasonic attenuation at a specific frequency to the
  local frequency derivative of the phase velocity (i.e., dispersion).
  The validity of these approximate relationships is demonstrated in
  several acoustic systems exhibiting substantially different physical
  properties.
author: ["M. O'Donnell", "E.T. Jaynes", "J.G. Miller"]
categories: ["Electrodynamics & Signal Processing"]
tags: ["Kramers-Kronig", "ultrasonic attenuation", "phase velocity", "dispersion", "linear response theory", "causality"]
---
PACS numbers: 43.35.Bf, 43.80.Cs, 43.20.Hq, 43.35.Fj
## INTRODUCTION
Quantitative relationships between attenuation and the frequency
dependence of the phase velocity (dispersion), the validity of which
depend only upon the properties of linearity and causality of the system
under investigation, have proven useful in a number of settings.

Examples include the Kramers-Kronig relationships[^1][^2][^3][^4] connecting the
in-phase and out-of-phase components of the appropriate susceptibility
in electromagnetic and acoustic phenomena and the Bode relationships[^5]
connecting the gain and phase shift in amplifier circuits. In a previous
short report we discussed quantitative relationships between the
attenuation and dispersion for a linear acoustic system.[^6] The present
study presents a derivation of the generalized relationship between the
ultrasonic attenuation and dispersion based on linear response theory.
In addition, useful approximate forms for these relations are derived
under the conditions that the attenuation and the dispersion do not vary
rapidly as functions of frequency. The use of these approximate
relationships for a wide range of acoustic systems is illustrated and
the implications of the existence of these relations concerning
investigation of the physical mechanisms responsible for the observed
attenuation are examined.

In Sec. I formulas are derived for predicting the ultrasonic attenuation
as a function of frequency from measurements of the frequency dependence
of the dispersion and vice versa. In Sec. II we illustrate the use of
the approximate relations, including a theoretical analysis of a simple
relaxation. In this section we also compare the results of experiments
with predictions based on the theory of Sec. I in a number of different
acoustic systems. Section III is devoted to a discussion of the
implications of the existence of these generalized relationships as
regards the study of mechanisms describing the propagation of ultrasound
in materials. Specifically, the formulas developed can be used to
predict ultrasonic properties not yet measured and to set limits on
properties which may lie beyond the range of currently available
measurement techniques. In addition, the existence of these completely
general relationships renders invalid attempts to compare the
attenuation and dispersion as a means of validating some specific model
proposed to explain the attenuation. As noted in the previous short
report, a demonstration of agreement between the dispersion and
attenuation predicted from a specific model and the measured dispersion
and attenuation serves only to establish that the specific mechanism and
the system as measured satisfy the conditions of causality (i.e., that
effects do not precede their causes) and linearity (i.e., that to some
approximation the response of the system is linearly proportional to the
stimulus).[^6]
## I. THEORY
We consider an isotropic acoustic medium described by a generalized form
of Hooke's law, and analyze the response of this medium to an incident
acoustic wave in terms of linear response theory. Utilizing the
formalism of linear response theory, we review the derivation of the
Kramers-Kronig equations which relate the in-phase and out-of-phase
components of the response of the acoustic system. We then use this
result in conjunction with the dispersion relation for the propagation
of sound in the medium to obtain general expressions which relate the
frequency dependence of the attenuation coefficient to the frequency
dependence of the phase velocity. Finally, we examine these expressions
for the case in which the phase velocity and the attenuation coefficient
do not vary rapidly with frequency. Under these conditions, the general
relations are cast into a more useful expression which relates the
attenuation coefficient to the dispersion over a limited frequency
range.

In the Hooke's law limit, the ultrasonic equation of motion describes a
linear system whose response can be represented by
$$
s(t) = \int_{-\infty}^{t} K(t-t^\prime)p(t^\prime) dt^\prime, \tag{1}
$$
 where $s$ is the
condensation, $p$ is the pressure, and $K$ is the adiabatic
compressibility. In Eq. (1), $K(t-t^\prime)$ plays the role of generalized
susceptibility relating the response $s(t)$ to the stimulus $p(t^\prime)$. The
central theme of this paper is that the principle of causality places
restrictions on the behavior of $K(t-t^\prime)$. Specifically, the response
$s(t)$ can depend upon past but not upon future values of the stimulus
$p(t^\prime)$. The restrictions imposed by causality on the generalized
susceptibility are conveniently expressed in terms of the real and
imaginary parts of the Fourier transform of the compressibility. If the
Fourier transform exists for $s$, $K$, and $p$, where the Fourier
transform for $K(t)$ is defined as
$$
K(t) = \int_{-\infty}^{\infty} \frac{d\omega}{2\pi} K(\omega)e^{-i\omega t}, \tag{2}
$$
then the response of the system in the frequency domain becomes
$$
S(\omega) = K(\omega)P(\omega), \tag{3}
$$
 where $K(\omega)$ is the
frequency domain compressibility. In general, $K(\omega)$ is a complex
function, $K(\omega) = K_1(\omega) + iK_2(\omega)$, where $K_1(\omega)$
is the real part and $K_2(\omega)$ is the imaginary part of the
compressibility.

To determine the relationship between the ultrasonic attenuation
coefficient and the dispersion, we begin by investigating the frequency
domain response of an acoustic system to a pressure fluctuation applied
as an impulse, i.e., a delta function. Under the action of this delta
function, the condensation becomes
$$
s(t) = K(t) = \int_{-\infty}^{\infty} \frac{d\omega^\prime   }{2\pi} e^{-i\omega^\prime t}K(\omega^\prime). \tag{4}
$$

The Kramers-Kronig relations can be obtained from Eq. (4) by applying
two conditions. First, the compressibility, $K(t)$, is physically
measurable and thus must be a real function. For this condition to be
satisfied, $K(-\omega)$ must equal $K^{*}(+\omega)$. That is, the real
part of the transform of the compressibility must be a symmetric
function and the imaginary part an antisymmetric function of frequency.
Applying this constraint to Eq. (4), the condensation reduces to
$$
s(t) = \frac{1}{\pi} \int_0^\infty d\omega^\prime    K_1(\omega^\prime) \cos\omega^\prime t + \frac{1}{\pi} \int_0^\infty d\omega^\prime    K_2(\omega^\prime) \sin\omega^\prime t. \tag{5}
$$

The second requirement on $K(t)$ is that of causality, which states that
the present condensation should not depend on the future pressure.
Consequently, $s(t)$ is zero for $t<0$, which from Eq. (5) requires that
$$
\int_0^\infty d\omega^\prime    K_1(\omega^\prime) \cos\omega^\prime t + \int_0^\infty d\omega^\prime    K_2(\omega^\prime) \sin\omega^\prime t=0, \quad t<0, \tag{6}
$$
or for $t>0$
$$
\int_0^\infty d\omega^\prime    K_1(\omega^\prime) \cos\omega^\prime t - \int_0^\infty d\omega^\prime    K_2(\omega^\prime) \sin\omega^\prime t=0, \quad t>0. \tag{7}
$$

To cast this result into a more useful form, we multiply (7) by
$\exp(-\lambda t)$, where $\lambda$ equals $\epsilon+i\omega$, and
integrate over positive times to obtain
$$
\int_0^\infty \frac{\omega^\prime K_1(\omega^\prime) - \lambda K_2(\omega^\prime)}{(\omega^\prime)^2 + \lambda^2} d\omega^\prime    = 0, \quad \epsilon>0. \tag{8}
$$

We now consider the limit as $\epsilon$ approaches 0, that is as
$\lambda$ approaches $i\omega$. Focusing on the denominator of Eq. (8)
we observe that
$$
((\omega^\prime)^2 + \lambda^2)^{-1} = P((\omega^\prime)^2 - \omega^2)^{-1} - \frac{i\pi}{2\omega}[\delta(\omega^\prime - \omega) + \delta(\omega^\prime + \omega)], \tag{9}
$$
where $P$ stands for the principal part in a subsequent
integration.[^7][^8] Using Eq. (9), the real and imaginary parts of (8)
then go into
$$
K_1(\omega) = \frac{2}{\pi} P \int_0^\infty \frac{\omega^\prime K_2(\omega^\prime)}{(\omega^\prime)^2 - \omega^2} d\omega^\prime   , \tag{10}
$$
$$
K_2(\omega) = -\frac{2\omega}{\pi} P \int_0^\infty \frac{K_1(\omega^\prime)}{(\omega^\prime)^2 - \omega^2} d\omega^\prime   . \tag{11}
$$

Equations (10) and (11) are the Kramers-Kronig relations for
longitudinal waves. In a real acoustic system, inertia will ensure that
the response and hence the generalized susceptibility to which the
response is proportional falls off rapidly enough at high frequencies so
that the integrals converge. In the original Kramers-Kronig application
(electric susceptibility), allowance was also made for an instantaneous
component of response $K_\infty \delta(t)$, where $K_\infty$ is the
value of the generalized susceptibility at arbitrarily high
("infinite") frequency. The causality condition was applied to the
remainder of the total response $[K(t) - K_\infty\delta(t)]$. A similar
approximation is useful in the acoustic problem, in which case
$K_1(\omega^\prime)$ in the above is to be replaced by
$[K_1(\omega^\prime)-K_\infty]$.

These equations can be used to relate the attenuation coefficient and
phase velocity because the frequency dependent compressibility also must
satisfy the dispersion relation for acoustic wave propagation
$$
k^2 = \omega^2 \rho_0 K(\omega), \tag{12}
$$
 where $k$ is the wavenumber
of the ultrasonic wave and $\rho_0$ is the density of the medium. To
satisfy Eq. (12), $k$ must be complex. We make the identification that
the wavenumber $k$ equals $\omega/C(\omega)+i\alpha(\omega)$, where
$C(\omega)$ is the phase velocity and $\alpha(\omega)$ is the
attenuation coefficient. Thus, for example, a plane wave traveling in
the $+x$ direction propagates as
$e^{i(kx-\omega t)} = e^{-\alpha x}e^{i[\omega x/C(\omega) - \omega t]}$.
The compressibility can be related to the attenuation coefficient and
phase velocity such that
$$
\frac{\omega^2}{C^2(\omega)} - \alpha^2(\omega) + \frac{2i\omega\alpha(\omega)}{C(\omega)} = \omega^2 \rho_0 [K_1(\omega) + iK_2(\omega)], \tag{13}
$$
or 
$$
\begin{aligned}
\frac{\omega^2}{C^2(\omega)} - \alpha^2(\omega) &= \omega^2 \rho_0 K_1(\omega), \\
\frac{2\alpha(\omega)}{C(\omega)} &= \omega \rho_0 K_2(\omega).
\end{aligned} \tag{14}
$$

In the usual case in which the magnitude of the
imaginary part of the wavenumber is much less than the magnitude of the
real part [i.e., $\alpha(\omega)C(\omega)/\omega \ll 1$] for all
frequencies, the set of equations [Eq. (14)] decouples and the phase
velocity and attenuation coefficient are determined by 
$$
\begin{aligned}
C(\omega) &= 1/[\rho_0 K_1(\omega)]^{1/2}, \\
\alpha(\omega) &= [\rho_0 C(\omega)/2] \omega K_2(\omega).
\end{aligned} \tag{15}
$$

Equations (10), (11), and (15) represent a
complete description of the frequency domain response of the acoustic
system in terms of the phase velocity and the attenuation coefficient.
Using these equations, the phase velocity can be computed exactly at all
frequencies if the attenuation coefficient is known at all frequencies.
Similarly, a knowledge of the phase velocity at all frequencies can be
used to compute the attenuation at all frequencies with Eqs. (10), (11),
and (15). The full Kramers-Kronig relations have proved useful in a
number of settings where the dominant contribution to the infinite
integrals is highly localized in frequency. For example, the exact
relations are widely applied in the field of magnetic resonance, where
the resonance constitutes the dominant contribution to the integral.
However, these expressions appear to be of limited usefulness in
settings where the integrals are not highly localized since the
computation of one variable appears to necessitate a knowledge of the
complementary variable for all frequencies; i.e., Eqs. (10) and (11) are
nonlocal.

We now utilize the analogy between the acoustic Kramers-Kronig relation
and the relationship between the frequency dependence of the gain and
phase shift of an electrical amplifier to obtain a more useful
expression relating the frequency dependence of the attenuation to the
dispersion over a limited frequency range in nonresonant systems.
Starting with the Kramers-Kronig relation connecting the gain and phase
shift of an electrical amplifier, Bode demonstrated that at any
frequency the phase shift is approximately related to the local rate of
change of the gain with frequency.[^5] The approximation is quite
accurate if both the gain and phase shift are sufficiently well behaved
(e.g., exhibit no resonances) over a limited frequency range centered at
the frequency of interest. A similar relation between the attenuation
coefficient and the phase velocity can be derived starting with Eq. (11)
and using a change of variable to evaluate the integral. We define the
variable $x = \ln(\omega^\prime/\omega)$ and consider the integral of Eq.
(11). The imaginary part of the compressibility becomes
$$
K_2(\omega) = -\frac{2}{\pi} \int_{-\infty}^{\infty} \frac{G(x) - G(\infty)}{e^x - e^{-x}} dx, \tag{16}
$$
where $G(x) = K_1(\omega^\prime)$ and $K_1(\infty) = G(\infty)$ since x is
infinite for $\omega^\prime$ equal to infinity. Integrating Eq. (16) by parts,
we find that $K_2(\omega)$ reduces to
$$
K_2(\omega) = -\frac{1}{\pi} \int_{-\infty}^\infty \frac{dG(x)}{dx} \ln \coth \left(\frac{|x|}{2}\right) dx. \tag{17}
$$

The integral in Eq. (17) can be cast into an approximate local form due
to the character of the function $\ln \coth(|x|/2)$, which is
illustrated in Fig. 1. As is evident from this figure, the function has
a sharp singularity at $x=0$, and thus the magnitude of the integral in
Eq. (17) is dominated by the value of the integrand at $x=0$.

Consequently, if the integral is rewritten in the form
$$
K_2(\omega) = -\frac{1}{\pi} \int_{-\infty}^\infty F(x) \ln \coth \left(\frac{|x|}{2}\right) dx, \tag{18}
$$
where $F(x)$ equals $dG(x)/dx$, then $F(x)$ can be expanded about $x=0$
to find an approximation to the integral. Expanding $F(x)$ about $x=0$,
and noting that the integral over odd powers of x in the expansion
vanishes since $\ln\coth(|x|/2)$ is an even function of x, Eq. (18)
becomes
$$
K_2(\omega) = -2 \sum_{n=0}^\infty \frac{F^{(2n)}(0)}{(2n)!} \int_0^\infty x^{2n} \ln \coth \frac{|x|}{2} dx. \tag{19}
$$
**[FIGURE 1: Function ln[coth(|x|/2)] in the neighborhood of x equals zero.]**
In Eq. (19) the term $F^{(2n)}(0)$ corresponds to the 2nth derivative of
$F(x)$ evaluated at $x=0$. Expanding $\ln \coth(|x|/2)$ in powers of
$e^x$, the integral of Eq. (19) can be evaluated:
$$
K_2(\omega) = -\frac{4}{\pi} \left( \sum_{n=0}^\infty F^{(2n)}(0) \sum_{m=0}^\infty \frac{1}{(2m+1)^{2n+2}} \right). \tag{20}
$$

Equation (20) indicates that $K_2(\omega)$ is related to the sum of the
even derivatives of $F(x)$ evaluated at $x=0$. If both the phase
velocity and attenuation coefficient are slowly varying functions of
frequency, then this sum can be approximated by the first few terms.
Under these conditions,
$$
K_2(\omega) = -\frac{\pi}{2} \left( F(0) + \frac{\pi^2}{96} F^{\prime\prime}(0) + \dots \right), \tag{21}
$$
or substituting for $F(x)$,
$$
K_2(\omega) = -\frac{\pi}{2} \left. \frac{dG(x)}{dx} \right|_{x=0} - \frac{\pi^3}{24} \left. \frac{d^3G(x)}{dx^3} \right|_{x=0} + \dots \tag{22}
$$

As is demonstrated below, $dG(x)/dx$ is related to the dispersion,
$dC(\omega)/d\omega$. Correspondingly, all higher derivatives of $G(x)$
are related to higher derivatives of the phase velocity with respect to
frequency. Consequently, if the change in dispersion is small over a
limited frequency range (e.g., no sharp resonances are present over the
frequency range of interest) then the higher order derivatives can be
neglected in the expansion presented in Eq. (22). The leading term in
Eq. (22) can be rewritten as
$$
\left. \frac{dG}{dx} \right|_{x=0} = \left. \frac{dK_1(\omega)}{d\omega} \frac{d\omega}{dx} \right|_{x=0} = \omega \frac{dK_1(\omega)}{d\omega}, \tag{23}
$$
and $K_2(\omega)$ becomes
$$
K_2(\omega) = -\frac{\pi}{2} \omega \frac{dK_1(\omega)}{d\omega}. \tag{24}
$$

Equation (24) relates the imaginary part of the compressibility at a
frequency $\omega$ to the local rate of change of the real part of the
compressibility at the same frequency. Using Eq. (15) to relate the real
part of the compressibility to the phase velocity, the derivative of
$K_1(\omega)$ with respect to frequency becomes
$$
\frac{dK_1(\omega)}{d\omega} = -\frac{2}{\rho_0 C^3(\omega)} \frac{dC(\omega)}{d\omega}. \tag{25}
$$

The dispersion and the attenuation coefficient can now be related by
combining Eqs. (15b), (24), and (25) with the result that
$dC(\omega)/d\omega$ becomes
$$
\frac{dC(\omega)}{d\omega} = 2C^2(\omega) \alpha(\omega)/\pi\omega^2, \tag{26}
$$
and $\alpha(\omega)$ becomes
$$
\alpha(\omega) = \frac{\pi\omega^2}{2C^2(\omega)} \frac{dC(\omega)}{d\omega}. \tag{27}
$$

If we rewrite Eq. (26) as
$$
\frac{dC(\omega)}{C^2(\omega)} = \frac{2\alpha(\omega)}{\pi\omega^2} d\omega, \tag{28}
$$
and integrate both sides from some reference frequency $\omega_0$ to
$\omega$, then the phase velocity is related to the attenuation
coefficient according to
$$
\frac{1}{C_0} - \frac{1}{C(\omega)} = \frac{2}{\pi} \int_{\omega_0}^\omega \frac{\alpha(\omega^\prime)}{(\omega^\prime)^2} d\omega^\prime, \tag{29}
$$
where $C_0$ is the sound velocity at $\omega_0$. Equations (27) and (29)
represent nearly local generalized ultrasonic attenuation-dispersion
relations. The magnitude of the dispersion is usually small, so that
these expressions can be further simplified to 
$$
\begin{aligned}
\alpha(\omega) &= \frac{\pi\omega^2}{2C_0^2} \frac{dC(\omega)}{d\omega}, \\
\Delta C = C(\omega) - C_0 &= \frac{2C_0^2}{\pi} \int_0^\omega \frac{\alpha(\omega^\prime)}{(\omega^\prime)^2} d\omega^\prime,
\end{aligned} \tag{30}
$$
where $C(\omega)$ is written as $C_0+\Delta C(\omega)$ with $\Delta C(\omega) \ll C_0$, and only terms of order
$\Delta C(\omega)$ are retained. In the next section, the validity of
Eq. (30) in several different acoustic systems is discussed.
## II. VERIFICATION OF THE NEARLY LOCAL RELATIONSHIPS
In the previous section we derived approximate forms for the
Kramers-Kronig relations linking the attenuation coefficient at a
frequency $\omega$ to the local rate of change of the phase velocity
with frequency. These nearly local forms should represent an accurate
description of the relationship between the attenuation and the
dispersion in the absence of rapid variations with frequency such as
those associated with a sharp resonance. In this section we explore the
validity of these expressions in several physical systems.

Relaxational phenomena represent an important class of loss mechanisms.
Although arising from many different physical sources, the class of loss
mechanisms associated with relaxation results in frequency dependent
attenuation of the form
$$
\alpha(\omega)/\omega = R_0 [(\omega/\omega_0)/(1+\omega^2/\omega_0^2)]. \tag{31}
$$

In Eq. (31), $\alpha(\omega)/\omega$ is the attenuation per cycle, $R_0$
is a frequency independent constant, and $\omega_0$ is the relaxation
frequency. The attenuation per cycle for a single
**[FIGURE 2: Attenuation per cycle for a single relaxation and dispersion from approximate vs exact Kramers-Kronig relations.]**
relaxation normalized to its value at the relaxation frequency is
illustrated as a function of frequency in Fig. 2(a). Using the form of
the attenuation per cycle [Eq. (31)] illustrated in Fig. 2(a), we have
computed the dispersion according to the exact, nonlocal Kramers-Kronig
relationship [Eqs. (10) and (15)] and according to the approximate,
nearly local relationship [Eq. (29)]. In Fig. 2(b) we compare the
dispersion computed from the nearly local approximate form to the
dispersion obtained from the exact Kramers-Kronig relation. This figure
clearly indicates that both the character and the numerical magnitude of
the dispersion associated with a single relaxation is accurately
described by the approximate nearly local relation derived in the
previous section.

To further test the validity of the approximate relations in describing
the relationship between attenuation and dispersion in materials
exhibiting relaxation, we investigate the properties of a system
consisting of a solution of CoSO$_4$ in water. The attenuation
coefficient and dispersion were measured in this system over the range
of approximately 1 to 10 MHz by Carstensen.[^10] In the top panel of Fig.
3 we present the product of the attenuation coefficient times the
wavelength measured in a 1 molar solution of CoSO$_4$ in water over the
frequency range of 500 kHz to 10 MHz. For small values of the
dispersion, the attenuation per cycle is simply proportional to
$\alpha\lambda$. From the top panel of Fig. 3 it appears that for
frequencies less than 3 MHz, the attenuation per cycle is accurately
described by a simple relaxation, whereas above 5 MHz, the data can be
fit to a straight line [i.e., $\alpha(\omega)$ proportional to
$\omega^2$]. In the lower panel of Fig. 3 we compare the change in the
sound velocity from its value at 1 MHz as measured by Carstensen to that
predicted by Eq. (30) using the attenuation data of the top panel. Both
the qualitative character and numerical value of the dispersion measured
in solutions of CoSO$_4$ in water are accurately predicted by the
approximate relations derived in the previous section.
**[FIGURE 3: Attenuation times wavelength in CoSO₄ solution and predicted vs measured dispersion.]**
We also investigated the validity of the approximate forms of the
Kramers-Kronig relations by comparing the attenuation and dispersion
measured from 1 to 10 MHz in polyethylene. We chose polyethylene for
this investigation because it represents a system that exhibits acoustic
properties very different from those of the systems described above.
Specifically, polyethylene is a solid and exhibits losses which are
relatively large in magnitude over the low MHz range ($\alpha\lambda$
equals 0.13 at 5 MHz). We measured the attenuation coefficient and the
velocity of sound using standard techniques.[^11][^12] Errors in the
attenuation coefficient determination were estimated to be less than 5%
and errors in the velocity determination less than 1 part in $10^4$. The
attenuation coefficient measured in a polyethylene plate is plotted as a
function of frequency over the range 1 to 10 MHz in the top panel of
Fig. 4. As illustrated in this figure, the attenuation coefficient is
nearly a linear function of frequency over this frequency range.

Consequently, according to Eq. (30), $\Delta C$ should be a nearly
logarithmic function of frequency over the same frequency range. In the
bottom panel of Fig. 4, $\Delta C$ as determined experimentally is
compared with that obtained from Eq. (30) (dashed curve) using the
attenuation data of the upper panel. The frequency
**[FIGURE 4: Attenuation in polyethylene plate and predicted vs measured dispersion.]**
corresponding to $C_0$ was taken to be 1 MHz. Not only is $\Delta C$ a
nearly logarithmic function of frequency in polyethylene, as predicted,
but over a decade in frequency the numerical magnitude of $\Delta C$
predicted by Eq. (30) is nearly identical to that measured. These
results clearly indicate that the approximate nearly local relations are
also valid in polyethylene over the range 1 to 10 MHz.
## III. DISCUSSION
In this study we considered acoustic propagation in a system which
satisfies Hooke's law in the context of linear response theory, where
the compressibility is identified as the generalized susceptibility of
the linear acoustic system. Because an acoustic medium represents a
causal system, the real and imaginary parts of the frequency dependent
compressibility are related by the Kramers-Kronig relations. Using the
dispersion relation for acoustic propagation, we have shown that the
real part of the compressibility is related to the phase velocity and
the imaginary part of the compressibility is related to the attenuation
coefficient. Consequently, the Kramers-Kronig relations can be used in
conjunction with the dispersion relation to obtain expressions linking
the phase velocity to the attenuation coefficient. These nonlocal
expressions are exact, and are independent of the particular mechanism
responsible for the attenuation. In Sec. I we demonstrated that the
exact, nonlocal Kramers-Kronig relations could be approximated by nearly
local relations linking the attenuation and the dispersion in systems
which do not exhibit rapid frequency variations. The validity of the
**[FIGURE 5: Attenuation in normal dog myocardium and predicted dispersion.]**
nearly local, approximate relations was tested in a number of acoustic
systems possessing a range of loss mechanisms. The results of
theoretical analysis and experiments presented in Figs. 2, 3, and 4
clearly show that the approximate relations represent an accurate
description of acoustic propagation in several systems which do not
exhibit rapid variations with frequency over the range of interest.
The approximate expressions presented in Eq. (30) can be used to predict
the ultrasonic properties of materials which may be difficult to obtain
using currently available measurement techniques. For example, the
ultrasonic dispersion is difficult to measure accurately in soft tissue
specimens. However, the dispersion in soft tissue can be estimated from
a knowledge of the measured attenuation coefficient. In Fig. 5 we
predict the dispersion in normal dog myocardium from measurements of the
attenuation coefficient obtained in our laboratory. The top panel of
Fig. 5 illustrates the attenuation coefficient as a function of
frequency over the range 1-10 MHz. In the lower panel of Fig. 5 we
present the dispersion predicted by Eq. (30). According to Eq. (30), the
nearly linear dependence of the attenuation coefficient on frequency for
normal dog myocardium gives rise to the prediction of nearly logarithmic
frequency dependence for the dispersion. The numerical value of the
change in phase velocity from 1 to 10 MHz is less than 2 parts in $10^3$
of the velocity. Consequently, the dispersion anticipated in normal dog
myocardium, and most soft tissues, is very small. Therefore dispersive
effects, such as distortion in the ultrasonic pulse shape, are
correspondingly negligible.

Finally, as noted above, the relationship between the attenuation and
dispersion is independent of the specific mechanism responsible for the
attenuation. Several authors have stated that the existence of
dispersion in a material is a strong indication that relaxational
processes are responsible for the attenuation in that material.[^13][^14]
As we noted in a previous publication,[^6] and have clearly demonstrated
in the present study, the existence of dispersion is in no way
indicative of a particular mechanism of propagation, but rather merely
establishes that a system which exhibits attenuation must exhibit
dispersion if it satisfies the conditions of linearity and causality. An
appreciation of which features of ultrasonic propagation are determined
by general laws of physics as opposed to those features which are
specific to the particular mechanism should prove useful in establishing
the mechanisms responsible for the propagation of ultrasound in a
material.
## ACKNOWLEDGMENTS
Pranoat Suntharothok-Priesmeyer was responsible for the production of
the text and illustrations. This research was supported in part by NASA
grant NSG 1601 and by NIH grant HL-17646.
## REFERENCES
[^1]: R. Kronig, "On the Theory of Dispersion of X-Rays," J. Opt. Soc. Am. **12**, 547 (1926).
[^2]: R. Kronig and H. A. Kramers, "Absorption and Dispersion in X-Ray Spectra," Zeits f. Phys. **48**, 174 (1928).
[^3]: L. D. Landau and E. M. Lifshitz, *Statistical Physics* (Addison--Wesley, Reading, MA, 1958), p. 392--398.
[^4]: V. Mangulis, "Kramers-Kronig or Dispersion Relations in Acoustics," J. Acoust. Soc. Am. **36**, 221 (1964).
[^5]: H. W. Bode, "Relations Between Attenuation and Phase in Feedback Amplifier Design," Bell Syst. Tech. J. **19**, 421 (1940).
[^6]: M. O'Donnell, E. T. Jaynes, and J. G. Miller, "General Relationships Between Ultrasonic Attenuation and Dispersion," J. Acoust. Soc. Am. **63**, 1935 (1978).
[^7]: P. M. Morse and H. Feshback, *Methods of Theoretical Physics* (McGraw-Hill, New York, 1953). The principal value integral is discussed on p. 368.
[^8]: R. N. Bracewell, *The Fourier Transform and Its Applications* (McGraw-Hill, New York, 1978). Methods for dealing with impulse functions are treated in Chap. 5. The result used to obtain Eq. (9) is presented on p. 95 in problem number 3.
[^9]: Equation (15b) is incorrectly printed in Ref. 6. Equation (4) of Ref. 6 is missing a factor of $\omega$ on the right side of the equation.
[^10]: Edwin L. Carstensen, "Relaxation Processes in Aqueous Solutions of MnSO₄ and CoSO₄," J. Acoust. Soc. Am. **26**, 862 (1954).
[^11]: H. P. Schwan and E. L. Carstensen, "Ultrasonics Aids Diathermy Experiments," Electronics, **25** (July) 216--220 (1952).
[^12]: Edwin L. Carstensen, "Measurement of Dispersion of Velocity of Sound in Liquids," J. Acoust. Soc. Am. **26**, 858 (1954).
[^13]: E. L. Carstensen and H. P. Schwan, "Acoustic Properties of Hemoglobin Solutions," J. Acoust. Soc. Am. **31**, 305 (1959).
[^14]: P. N. T. Wells, "Absorption and Dispersion of Ultrasound in Biological Tissue," Ultrasound Med. Biol. **7**, 369 (1975).