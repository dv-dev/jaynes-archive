---
title: "Phase-Sensitive Optical Amplifier"
year: 1980
abstract: >
  The application of Armstrong's super-regenerative principle to a laser
  amplifier shows that it is possible to control the phase of even a
  low-gain He-Ne laser amplifier by injecting as few as four or five
  photons just after the laser is turned on and while it goes through
  threshold. Estimation of the uncertainties in determining the level of
  the injected signal and the phase of the laser output indi- cates that
  measurements approaching the limit ΔnΔϕ = 1/2 may be possible.
author: ["D.R. Matthys", "E.T. Jaynes"]
categories: ["Quantum Mechanics & Advanced Physics"]
tags: ["optical amplifier", "super-regenerative principle", "laser amplifier", "He-Ne laser", "phase sensitivity", "Heisenberg uncertainty principle", "quantum noise"]
---
## INTRODUCTION
A high-gain linear (i.e., phase-sensitive) amplifier at optical
frequencies would have many applications in communications and as a
research tool. Previous efforts[^1] to use a laser amplifier as a
phase-measuring device have stressed the need for a high-gain laser such
as a Nd:YAG system.

In the early days of radio, Armstrong's super-regenerative
principle[^2] made possible unlimited gain from a single vacuum tube
stage of modest intrinsic gain. We have confirmed that the same
principle, applied at optical frequencies, allows one to achieve any
desired gain from the intrinsically low-gain helium-neon laser while
retaining phase sensitivity. The following reports an experimental
determination of the noise level of such an amplifier.

At low frequencies ($h\omega \ll kT$) a theoretical limit on usable gain
is set by thermal noise at the input as given by the Nyquist formula
$P_N = kTB$ for the available noise power in a bandwidth B.

Experimentally, super-regenerative amplifiers at both radio[^3] and
microwave[^4] frequencies readily approach this limiting sensitivity.
At optical frequencies ($h\omega \gg kT$) an often quoted theoretical
limitation arising from quantum theory replaces the Nyquist formula by
$P_Q = h\omega B$. The physical origin of this "quantum noise" is
ascribed variously[^5][^6][^7] to spontaneous emission, zero-point field
fluctuations, or the Heisenberg uncertainty principle. Also, Ross[^7]
has noted some qualitative differences in the nature of thermal noise
and quantum noise.

For present purposes, we need not go into these matters beyond noting
that, while the Nyquist thermal noise formula has been confirmed by
innumerable experimental measurements, there appear to be no direct
experimental tests of the quantum noise formula (of course, we have many
measurements of related phenomena such as amplitude and phase
fluctuations in cw lasers[^8]). A measurement of the noise level of a
super-regenerative optical amplifier is, therefore, of interest not
only for determining its possible useful applications, but also because
such a measurement might provide a direct test of some fundamental
aspects of quantum theory, i.e., how does the attainable amplitude and
phase measurability compare with the Heisenberg limit
$\Delta n \Delta\phi \ge 1/2$? (It should be pointed out here that this
formulation of the Heisenberg principle for a fully quantized theory has
been rejected,[^9][^10] but in a semiclassical treatment it follows
easily from the usual $\Delta p \Delta q$ form.)
## EXPERIMENTAL PROCEDURE
The physical setup used to obtain answers to these questions consisted
of two He-Ne lasers operating in Gaussian mode at 633 nm arranged around
a Mach-Zehnder interferometer as shown in Fig. 1. The cw laser was a
Spectra-Physics Model 131 with dc excitation, while the pulsed laser
amplifier was locally constructed and driven by a rf transmitter.
Variations in frequency and amplitude due to thermal and other effects
were negligible during the time required to record each sample. Due to
different cavity dimensions, only one mode of each laser could interfere
at any time with a mode of the other laser. The amplifier laser was
turned on for about 100 $\mu$s at a 4-kHz repetition rate, by pulsing
its 20-MHz rf excitation (cutting off the screen grid of the final
amplifier stage). Part of the output from the cw laser was coupled into
the cavity of the pulsed laser. If during the initial buildup of laser
oscillation in the pulsed laser this injected signal is within the
amplified frequency band and has a sufficient amplitude, then a definite
phase relationship should exist between the original laser beam and the
output of the pulsed laser. Otherwise, the phase difference between the
two beams should vary randomly from pulse to pulse.

If it could be determined how much injected energy was present in the
amplifier cavity at the time it was pulsed on, then monitoring the phase
relationships in the interferograms produced at the two outputs of the
interferometer would allow not only the determination of the minimum
energy injection required for phase control, but also a measurement of
the uncertainty product $\Delta n\Delta\phi$ for the injected signal.
To record the interferograms produced at each turn-on of the pulsed
laser three EMI 9558B photomultipliers were used as detectors D1, D2,
D3, arranged as shown in Fig. 2 to intercept the output signals. The
glass-dielectric interface of the output beamsplitter BS2 introduced a
different phase shift for the reflected portion of the beam entering
from the dielectric side than for the reflected portion of the beam
entering from the glass side, so the two outputs are not the same but
have a phase difference of 180° between them, i.e., they have the form
$I = I_0 (1 \pm \cos \phi)$, where $\phi$ is the phase difference at
each point of the interferograms.
**[FIGURE 1: Experimental arrangement of the two lasers and the interferometer. BS are beamsplitters; M are mirrors; M’ is special edge mirror cutting halfway into the beam; D1, D2, D3, D4 are photomultiplier tubes.]**
**[FIGURE 2: (A) Detail of interferometer output showing detectors D1, D2, D3. (B) Plot of intensity variation across the output beam seen by D3. (C) Plot of intensity variation across output as seen by D1 and D2.]**
## METHOD OF ANALYSIS
Since the output of each laser is restricted to the lowest-order
Gaussian mode, the form of the electromagnetic field in the cw beam and
in the output beam of the pulsed laser can be expressed in the forms
$$E_1(r,t) = A_1\exp(-r^2/w_1^2)\cos \omega t,$$ 
$$E_2(r,t) = A_2\exp(-r^2/w_2^2)\cos[\omega t + \phi(t)],$$ 
respectively. Here $A_1, A_2$ represent the maximum field strength at
the center of the beams and $w_1, w_2$ are the beam radii at which the
field strength has fallen to 1/e of the central maximum. It is assumed
that the two frequencies are the same and that the phase difference
$\phi(t)$ between the beams, though time-dependent, changes slowly with
respect to the measurement time of the experiment. Adjusting the shear
and tilt between the two beams will produce a linear variation of phase
across the interference pattern at the outputs, such that the intensity
over the plane transverse to the beams at the location of minimum shear
is found to be
$$
\begin{split}
I(r) &= \langle[E_1(r,t) + E_2(r,t)]^2\rangle_{\text{av}} \\\\
&= 1/2 [A_1^2\exp(-2r^2/w_1^2) + A_2^2\exp(-2r^2/w_2^2)] \\\\
&\qquad + A_1A_2\exp(-r^2/\alpha^2) \cos \phi(r),
\end{split}
$$
where
$$
\alpha^2 = w_1^2w_2^2/(w_1^2 + w_2^2)
$$
is the effective beam size.

Adjusting the tilt between the beams changes the fringe spacing, of
course, so if b is introduced as a parameter specifying the
half-fringe spacing, $\phi_0$ is the phase difference at the center of
the pattern, and the fringes are specified as perpendicular to the x
axis, then the total integrated intensity in the output beams is found
to be
$$
\begin{split}
I &= (\pi/4)(A_1^2 w_1^2 + A_2^2 w_2^2) \\\\
& \qquad \pm 2A_1 A_2\alpha\sqrt{\pi} \int_{0}^{\infty} \exp(-x^2/\alpha^2)\cos(\pi x/b)dx \cos\phi_0,
\end{split}
$$
where the $\pm$ indicates the phase shift between the two outputs.

The first term is a constant background value and the second term
contains all the interference effects. In this latter term, the first
factor shows the effect of different beam sizes and power levels, and
the exponential and cosine factors give the relationship between the
half-fringe spacing b and the beam size w.

In order to obtain intensity and phase information in a form suitable
for display on an oscilloscope, detectors D1, D2, and D3 are arranged as
shown in Fig. 2. An edge mirror M' is inserted into one of the output
beams from the interferometer at BS2, splitting the beam in half
parallel to the fringes. Then the halves are sent to detectors D1 and
D2. The other beam from the interferometer is sent to the detector D3.
The total integrated intensity received at each of these detectors is
$$
\begin{split}
I_{D1} &= (\pi/8)(A_1^2 w_1^2 + A_2^2 w_2^2) \\\\
&\quad -A_1A_2\alpha\sqrt{\pi} \int_0^\infty \exp(-x^2/\alpha^2)[\cos(\pi x/b)\cos\phi_0 \\\\
&\qquad + \sin(\pi x/b)\sin\phi_0]dx,
\end{split}
$$
$$
\begin{split}
I_{D2} &= (\pi/8)(A_1^2 w_1^2 + A_2^2 w_2^2) \\\\
&\quad -A_1A_2\alpha\sqrt{\pi} \int_0^\infty \exp(-x^2/\alpha^2)[\cos(\pi x/b)\cos\phi_0 \\\\
&\qquad - \sin(\pi x/b)\sin\phi_0]dx,
\end{split}
$$
$$
\begin{split}
I_{D3} &= (\pi/4)(A_1^2 w_1^2 + A_2^2 w_2^2) - 2A_1A_2\alpha\sqrt{\pi} \\\\
&\qquad \times \int_0^\infty \exp(-x^2/\alpha^2)\cos(\pi x/b)dx \cos\phi_0.
\end{split}
$$
Subtracting the signals received at D1 and D2 gives
$$
\begin{split}
I_{D1} - I_{D2} &= [-2A_1A_2\alpha\sqrt{\pi} \\\\
&\qquad \times \int_0^\infty \exp(-x^2/\alpha^2)\sin(\pi x/b) dx] \sin\phi_0.
\end{split}
$$
On the other hand, subtracting the signal at D3 from the combined
signals from D1 and D2 leads to
$$
\begin{split}
I_{D1} + I_{D2} - I_{D3} = [-4A_1A_2\alpha\sqrt{\pi} \int_0^\infty \exp(-x^2/\alpha^2)\cos(\pi x/b)dx] \\\\
\times \cos\phi_0.
\end{split}
$$
These equations for $I_{D1} - I_{D2}$ and $I_{D1} + I_{D2} - I_{D3}$
contain the desired amplitude and intensity and phase difference in a
form suitable for an X-Y display on an cathode ray oscilloscope. That
is, by inserting proper gain factors, the signals (9 and 10) become
proportional to A sin$\phi_0$ and A cos$\phi_0$, respectively, and the
CRT display effectively shows the phase space diagram of the pulsed
laser output, indicating simultaneously its amplitude and phase. The
reproducibility of this on successive pulses then indicates how
accurately the amplitude and phase of the injected signal are being
determined by the pulsed amplifier.

The two equations involve integrals relating the effect of the beam-size
to fringe-spacing ratio, or the strength of the detected signal. Solving
the two integrals for equal balanced signals on the X-Y coordinates
gives an optimum ratio of half-fringe spacing b to effective beam size
$\pi\alpha/(2b) \approx 1.1$. This value determines the proper
adjustment of the interferometer for desired tilt between the beams.
However, it is also necessary to determine the level of the injected
signal for each turn-on of the pulsed laser. This is obtained by
monitoring the turn-on time of the laser amplifier. A slightly modified
form of the equation of Sargent et al.[^11] for the buildup of laser
amplification is given by
$$d\langle n \rangle / dt = (\alpha - \beta\langle n \rangle)\langle n \rangle + \beta s$$ 
where $\alpha$ is the gain of the lasing medium, $\beta$ represents the
scattering and diffraction losses, s is a phenomenological term added
to account for saturation effects, and $\langle n \rangle$ is the photon
number within the cavity. This equation predicts that a logarithmic plot
of resonator energy versus time after turn-on would be logarithmic at
very low levels, become linear over most of the interval from threshold
to saturation, and then level off at saturation.

The effect of starting buildup from a low-level signal rather than from
the noise level will be to shorten the time required to reach some
specified level of laser output. If a reference level is chosen on the
linear portion of the buildup curve well below saturation effects, and
if the gain of the laser is known, then a knowledge of how much the
turn-on time was shortened allows a calculation of the injected energy
present in the cavity when the laser began to turn on.
## EXPERIMENTAL RESULTS
Figure 3 shows typical data obtained from pulsing the laser amplifier
while an external signal was fed into it. The dotted line indicates the
effect of removing the incoming signal.

The main body of the curve gives the distribution of turn-on times
required to reach the reference level, while the left side of the curve
indicates those pulses of the laser when lasing built up from energy
coupled in from the external laser. The width of the main peak
corresponds to fluctuations in the noise level of the laser amplifier
and sets a limit of how closely the shortening of turn-on time can be
determined for any particular sample.

Referring back to Fig. 1, which gives the basic experimental layout, it
is seen that part of the output from the laser amplifier is fed to a
fourth detector D4. This last detector is coupled to a voltage
comparator and a timing circuit so that information of the type shown in
Fig. 3 can be collected.

Combining this information about turn-on times with the data obtained
from the interferometer outputs allows a determination of the minimum
signal required to control the laser amplifier and also an estimation of
the uncertainty $\Delta n \Delta\phi$ in these measurements.

The attenuator used between the lasers as shown in Fig. 1 reduced the
incident laser intensity by an order of magnitude, but much larger
attenuation resulted from not matching the parameters of beam size and
curvature for the two lasers. Since only minimal coupling was desired, the
first laser was simply pointed down the cavity of the second laser.
Aside from avoiding any direct reflections back into the pulsed laser
cavity no effort was made to prevent the possibility of scattered light
by the use of optical isolators. The pulsed laser, operating as a
super-regenerative amplifier for any signal coupled in, is at the limit
of turn-on time pulsed at 4 kHz and the signals from the interferometer
outputs and the timing signal marking time after turn-on of the laser
amplifier were all recorded on tape. Since the available recorder was an
incremental digital recorder, only short samples per second, or about 1%
of the signals, could be recorded.

It was found that there were three types of interferogram, shown in Fig.
4. These represented no interference and no coupling, interference but
no coupling, and interference with coupling, respectively. The
electronics at each detector was arranged so that 1 $\mu$A from each
photomultiplier produced a 1.0 V output. Under these conditions the mean
radius of the noise spot shown in the polar plot of Fig. 4 was 11 mV.
Because of thermal drift the two laser cavities were generally resonant
at different frequencies. Thus by far the majority of the recorded data
showed no interference, some showed interference without coupling (the
first laser interfered after the second laser had already turned on), and a
few thousand samples showed both coupling and interference. Because of the
large amount of background and the low recording rate, the results
obtained do not have a large statistical reliability; however, using the
shortened turn-on times as a criterion of coupling and utilizing only
those samples that turned on well before the peak of the timing
distribution curve, a small subset of several dozen samples still
remained which allowed an estimate of the level of injected signal
required to establish phase control of the second laser.
**[FIGURE 3: Plot of time distribution curve for laser turn-on. Dotted curve shows results obtained when no signal is injected.]**
**[FIGURE 4: Typical interference patterns. (A) No interference and no coupling. (B) Interference but no coupling. (C) Interference with coupling.]**
## DETERMINATION OF $\Delta\phi$ AND $\Delta n$
The uncertainty $\Delta\phi$ in measuring the relative phase between the
interfering beams was caused by the statistical noise in the signals
(cf. Fig. 5). Although the end point of the interference patterns for
each signal could be readily determined, the exact origin of the signal
was masked by the central noise spot. On the other hand, the uncertainty
$\Delta n$ in the determination of the injected signal is due to the
finite width of the timing distribution curve for laser turnon. The
problem is clearly seen by examining the solid-line curve of Fig. 3,
which shows the timing distribution for laser turn-on with an injected
signal. Lower levels of injected signal produce less shortening of the
turn-on times and it becomes more difficult to assert that the early
turn-on of a particular sample is due to the injected signal rather than
to random fluctuations. In order to have reasonable confidence that the
early turn-on is indeed due to the injected signal, only samples which turn
on at least four standard deviations ahead of the mean of the distribution
curve are chosen. Staying this far out from the mean gives almost 100%
probability that the sample is indeed responding to the injected signal.
In order to measure the energy level in the pulsed laser resonator when
the laser is turned on, and also to estimate the uncertainty in this
measurement, the timing information recorded by detector D4 for each
sample is combined with the measured gain of the laser. As discussed
earlier in reference to Eq. (11) the buildup of energy in the laser
cavity is basically exponential until saturation effects become
significant. If a reference level well below saturation is chosen, the
cavity energy will build up to that level in exponential fashion. It is
assumed that with no injected signal, the laser will build up from its
noise level of about $h\omega$ per mode,[^12] so at t = 0, n = 1, where t
is time after turn-on and n is the resonator energy expressed in units
of $h\omega$. This gives the peak at 6.6 $\mu$s in the timing distribution
curve shown in Fig. 3. The fluctuations in noise give rise to the finite
width of the peak, in this case a FWHM value of 0.12 $\mu$s.

An example is shown in Fig. 6 of a sample which reached the reference
level in 5.6 $\mu$s, or 1 $\mu$s earlier than the peak. Extrapolating back
from this point using the easily measured gain of the laser shows that
this sample built up from a cavity energy of n = 13. Since the FWHM
spread of the peak limits the accuracy with which the time shortening
can be known, the sample turn-on time is bracketed by dashed lines 0.12
$\mu$s ahead and behind the measured turn-on time of 5.6 $\mu$s.

Extrapolation from these values gives the uncertainty in the
specification of the cavity energy at turn-on. For the sample shown,
n = 13 with $\Delta n = +5, -4$. Using this procedure for all the
samples that turned on sufficiently ahead of the timing distribution
peak (four standard deviations was used as a criterion) shows that with
an uncertainty in the injected signal of $\Delta n = 1.6$, as few as 4
or 5 photons were sufficient to control the laser amplifier. The
corresponding uncertainty in measuring the phase difference for these
same samples was about 0.3 rad. The range of $\Delta n \Delta\phi$
products obtained was from 0.4 to 0.7.
**[FIGURE 5: Polar plot of intensity versus phase showing how the value of $\Delta\phi$ is determined.]**
**[FIGURE 6: Plot of pulsed cavity energy versus time after turn-on for a particular sample.]**
## SUMMARY AND CONCLUSIONS
Even with the limited accuracy of these preliminary results, two
conclusions are supported by this experiment. First, the extreme
sensitivity of the super-regenerative amplifier system obviates the need
for a high-gain laser in this type of phase-measuring setup. Only a few
photons are required to establish phase control of the laser amplifier.
Second, the uncertainty product $\Delta n \Delta\phi \approx 1/2$ which
was obtained shows that the debate over various interpretations of
Heisenberg's principle such as the Copenhagen interpretation,[^13] the
statistical interpretation,[^14] and the challenge from those theories
which reject field quantization[^15] (which is usually regarded as the
source of the resultant uncertainty) need not be regarded as purely
theoretical or philosophical. Physical experiments within the bounds of
present technology are capable of testing at least some of the many
proposed interpretations.[^16]
## ACKNOWLEDGMENT
This work was supported in part by the AFOSR.
## FOOTNOTES
[^1]: H. Gerhardt, H. Welling, and D. Frölich, "Ideal laser amplifier as a phase measuring system of a microscopic radiation field," Appl. Phys. **2**, 91--93 (1973).
[^2]: E. Armstrong, "Some Recent Developments of Regenerative Circuits," Proc. IRE **10**, 244--260 (1922).
[^3]: F. E. Terman, *Radio Engineer's Handbook* (McGraw-Hill, New York, 1943), pp. 662--664.
[^4]: E. T. Jaynes, unpublished (1945). A 1-kW pulsed triode oscillator using a "lighthouse" tube at 1050 MHz was readily phase controlled by an injected cw signal at a level corresponding to energy $\approx kT$ in the tank circuit. This device proved to be the most sensitive microwave receiver available at the Naval Research Laboratory (Combined Research Group).
[^5]: A. Siegman, *Microwave Solid State Masers* (McGraw-Hill, New York, 1964), Chap. 8.
[^6]: R. Serber and C. H. Townes, "Limits on Electromagnetic Amplification Due to Complementarity," in *Quantum Electronics*, edited by C. H. Townes (Columbia University, New York, 1960), pp. 233--255.
[^7]: Monte Ross, *Laser Receivers* (Wiley, New York, 1966), pp. 29--32.
[^8]: K. Manes and A. Siegman, "Observation of quantum phase fluctuations in infrared gas lasers," Phys. Rev. A **4**, 373--386 (1971).
[^9]: L. Susskind and J. Glogower, "Quantum Mechanical Phase and Time Operator," Physics **1**, 49--61 (1964).
[^10]: P. Carruthers and M. Nieto, "Coherent states and the number-phase uncertainty relation," Phys. Rev. Lett. **14**, 387--389 (1965).
[^11]: M. Sargent, M. Scully, and W. Lamb, "Buildup of laser oscillations from quantum noise," Appl. Opt. **9**, 2423--2427 (1970).
[^12]: A. Siegman, *Introduction to Lasers and Masers* (McGraw-Hill, New York, 1971), p. 416.
[^13]: J. von Neumann, *Mathematical Foundations of Quantum Mechanics* (Princeton University, Princeton, N.J., 1955), Secs. IV.1--IV.2.
[^14]: L. Ballentine, "Statistical Interpretation of Quantum Mechanics," Rev. Mod. Phys. **42**, 358--381 (1970).
[^15]: E. Jaynes, "Survey of the Present Status of Neoclassical Radiation Theory," in *Coherence and Quantum Optics*, edited by L. Mandel and E. Wolf (Plenum, New York, 1973), pp. 35--81. See especially p. 36.
[^16]: D. Matthys, Ph.D. thesis, Washington University, St. Louis, Mo., 1975 (unpublished).
