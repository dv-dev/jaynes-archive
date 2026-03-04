---
title: "Ancient History of Free Electron Devices"
year: 1978
abstract: >
  We recall some early thinking about the production of light from
  high-energy electrons, that started with problems in the design of
  electron accelerators, in which the writer was an interested observer
  and (at Stanford, Berkeley, and Princeton in 1946-1960) a sometime
  participant. In fact, some of that work is being put on record here for
  the first time, since there was no encouragement to follow up such ideas
  then, beyond a few Seminar talks (although it has been inflicted since
  on generations of students, as pedagogical fodder and homework
  problems).
author: ["E.T. Jaynes"]
categories: ["Quantum Mechanics & Advanced Physics"]
tags: ["free electron devices", "betatrons", "synchrotrons", "linear accelerators", "undulators", "cyclotron-maser", "Schwarz-Hora effect"]
---

## BETATRONS AND SYNCHROTRONS

Radiation of light due to acceleration of free electrons occurs
naturally in Bremsstrahlung. In the early 1940's, when the betatron and
synchrotron were being developed, it was realized that this same
phenomenon would place an upper limit to the attainable energy from any
such device other than a linear accelerator.

Iwanenko and Pomeranchuk[^iwanenko1944] gave a formula for the betatron based on
the relativistic generalization of the Larmor power formula
$P_L = (2e^2/3c^3)\dot{v}^2$, and Schwinger[^schwinger1946][^schwinger1949] produced an
immense calculation of radiation from betatrons and synchrotrons, giving
its full spectral and directional distribution. The predicted radiation
was of surprisingly high frequency, as confirmed experimentally by
Elder, Langmuir, and Pollock[^elder1948] on the G. E. synchrotron. For an
electron in an orbit of radius R = 29.2 cm (orbital frequency 163.5 MHz)
it reached the optical region with the appearance of a dull red spot at
30 Mev, progressing to brilliant bluish-white light at 80 Mev.

The reason why the emitted radiation is mostly in extremely high
harmonics--millions of times the orbital frequency--can be seen as
follows. A transversely accelerated electron with energy
$E = \gamma mc^2$, $\gamma \gg 1$, emits radiation which in the
laboratory frame is concentrated mostly in the forward direction, in a
cone of angle $\theta \sim \gamma^{-1}$. A distant observer in the plane
of the orbit of radius R will be within this cone only for a path
segment $\delta x \sim 2R/\gamma$. But the pulse of radiation in the
forward direction will be foreshortened by a factor of
$1 - \beta \approx (2\gamma^2)^{-1}$, so he sees a pulse of duration
$\delta t = \delta x / 2\gamma^2 c = R/\gamma^3 c$. At 80 Mev, R = 29
cm, this gives $\delta t = 2 \times 10^{-16}$ sec, just the radian
period (1/w) of blue light.

Recently, those of us with mode-locked lasers were proud of having
produced picosecond light pulses. In fact, the synchrotron was producing
light pulses a thousand times shorter than that, thirty years ago!
In any problem involving the wave equation and the geometry of a circle,
Bessel functions are bound to show up; and Schwinger obtained the
following quantitative result. An electron in uniform circular motion at
orbital frequency $\omega_0$, velocity $v = \beta c = \omega_0 R$,
radiates power into the n'th harmonic of
$$
P_n = \frac{n \omega_0 e^2}{R \gamma^2} \left[ 2\beta^2 \gamma^2 J^\prime_{2n}(2n\beta) - \int_0^{2n\beta} J_{2n}(x)dx \right]
$$
where, as always, $\gamma = E/mc^2 = (1 - \beta^2)^{-1/2}$. This is the
exact formula for a point charge. In the nonrelativistic limit
$\beta \ll 1$, it goes into
$$
P_n = \frac{2\omega_0^2 e^2}{R} \frac{n+1}{(2n+1)!} (n\beta)^{2n+1}
$$
which for n=1 reproduces the elementary textbook result. In the extreme
relativistic limit $\gamma \gg 1$, various approximate forms exist,
depending on how n compares to a critical harmonic number
$n_c = 3\gamma^3/2$. For example, if $n \ll n_c$, we have
$$
P_n \approx \frac{3^{1/6}\Gamma(2/3)\omega_0 e^2}{\pi R} n^{1/3}
$$
slowly increasing with n, while if $n \gg n_c$,
$$
P_n \approx \frac{\omega_0 e^2}{R \gamma} \left( \frac{3n}{2\pi n_c} \right)^{1/2} \exp(-n/n_c)
$$
rapidly decreasing with n.

The total power radiated is
$$
P = \sum_{n=1}^\infty P_n = \frac{2\omega_0 e^2}{3R} \beta^3 \gamma^4
$$
which places the ultimate limit on attainable energy, as noted by
Iwanenko and Pomeranchuk; although for the aforementioned synchrotron at
80 Mev it is not yet serious, amounting only to about 12 ev per electron
per turn. However, it is only because of the high frequency of the
radiation, which keeps the emission from different electrons
incoherent, that the synchrotron will work. If the radiation were of
such a low frequency that the bunch of N electrons were smaller than a
wavelength, they would radiate coherently, losing energy at a rate
proportional to $N^2$ rather than N; and that would be fatal.

Finally, a controversy, amusing in retrospect, developed for a short
time on the validity of classical vs. quantum electrodynamics for this
problem. For the summing up, vindicating classical theory, see Schiff[^schiff1952].

## LINEAR ACCELERATORS

In the closing days of World War II, I found myself in the Navy headed
for the South Pacific; but just before leaving I visited my friend
Professor W. W. Hansen, at Stanford. Alarmed at my imminent cultural
deprivation, he gave me his copy of Whittaker and Watson, with all his
marginal comments on the theorems (which I still have and use), to work
through while away. This was just managed when, in the Spring of 1946,
finally out of the Navy and having a few months before starting graduate
school at Berkeley, I again visited Hansen and proclaimed myself an
analyst, thanks to his book.

He immediately put me to work for the Summer, applying all this
erudition on the design of the first linear accelerator tubes (about 4
inches in diameter, with loading discs to reduce the phase velocity to
c, spaced about one inch apart with central holes about one inch in
diameter). First, I had to prove myself by reproducing independently--in
whatever way I chose--his calculated results for the dispersion curve of
the structure, in its dependence on the dimensions of the loading discs.
Having passed that test, he then gave me the problem of developing
coupling systems to match the periodic accelerator structure to
conventional 3 GHz waveguide. Probably the only part of that work that
survives usefully today is the diagnostic method[^jaynes1952] worked
out to determine, from measurements in the waveguide, when we had a pure
running wave in the accelerator tube.

That Summer the news of Schwinger's still unpublished calculations had
already reached Stanford[^schiff1946], and those of us dreaming of
future LINACS felt left out, since it appeared that our machine would
not produce this interesting visible light whose color shows, at a
glance, the electron energy. But then it occurred to me that, because my
coupling systems surely would not work perfectly, giving an absolutely
pure running wave in the accelerator tube, the electrons in a real LINAC
would, after all, emit some high-frequency radiation.

The "useful" accelerating wave, carrying perhaps 10 megw of power,
will be accompanied, inevitably, by a small reflected wave of perhaps 1
megw.

Let us think of it as a plane wave, of a microwave frequency
$\omega_0/2\pi = 3$ GHz, Poynting vector
$S_0 = P_0/A = 2 \times 10^5 \text{ watts/cm}^2$, traveling in the (-z)
direction.
[Of course, the reflected wave in a LINAC is not a plane wave, the
transverse field $E_r \sim J_1(kr)$ vanishing on the axis where one
tries to keep the electron beam. But by the Poynting theorem, a given
reflected power $P_0$ requires a certain average $\langle E_r^2 \rangle$ over the disc
apertures A. Therefore, while our plane wave treatment does not describe
the situation that LINAC operators now try to achieve, it does describe,
within unimportant numerical factors.]

Now consider an electron moving in the (+z) direction with energy
$E = \gamma mc^2$. In the electron's reference frame F', this reflected
wave appears as one of frequency and Poynting vector
$$
\begin{aligned}
\omega^\prime &= \gamma(1 + \beta)\omega_0 \approx 2\gamma \omega_0 \\
S^\prime &= \gamma^2(1+\beta)^2 S_0 \approx 4\gamma^2 S_0
\end{aligned}
$$

For example, at 100 Mev,
$\gamma = 1 + (100/0.511) = 197$, the electron sees a plane wave of
wavelength $\lambda^\prime = \lambda_0/394 = 0.025 \text{ cm}$, with an energy
flux $S^\prime = (394)^2 S_0 = 31,000 \text{ megawatts/cm}^2$. From this, it
is clear why electron in a LINAC will, by Thomson scattering, emit a
considerable amount of high-frequency radiation. And in a wave of this
intensity, the electron might oscillate with such amplitude that it
generates appreciable radiation in harmonics of the frequency $\omega^\prime$.
We then need to discuss Thomson scattering in a wave of very high
intensity.

## RADIATION FROM AN OSCILLATING CHARGE

To fix numerical magnitudes, an energy flux of the above value S'
corresponds to an electric field strength $E_r \sim 10^4$ esu, and the
electron will oscillate with amplitude $a = eE_r/m\omega^2 \sim 10^{-4}$
cm, reaching a peak velocity $v = \omega a \sim 0.024 \text{ c}$. Even
at this intensity, therefore, the scattering as seen in the electron's
reference frame F' is not a particularly relativistic problem.

That an oscillating charge will in general radiate harmonics of its
orbital frequency is clear from the fourier expansion of the charge
distribution;
$$
\delta(x-a \cos \omega t) = \frac{1}{2\pi} \sum_{n=-\infty}^\infty \frac{2 T_n(x/a)}{\sqrt{a^2-x^2}} e^{-in\omega t}, \quad |x|\lt a
$$
where $T_n(z)$ are the Tchebycheff Polynomials:
$$
T_n(z) = \cos(n \cos^{-1} z) = T_{-n}(z)
$$

All harmonics are present,
but it looks at first glance as if we have escaped from Schwinger's
Bessel functions to something new. But of course linear sinusoidal
motion is just projected circular motion; and when we calculate the
resulting distant field the Bessel functions must inexorably reappear. For
example, in Lorentz gauge the potential $\phi$ from the retarded
solution of $\Box\phi + 4\pi\rho = 0$ is
$$
\phi(R) = \frac{e}{2\pi} \sum_n e^{-in\omega t} \int_{-a}^a \frac{T_n(x/a)}{\sqrt{a^2-x^2}} \frac{e^{inkr}}{r} dx
$$
where $k=\omega/c$, and r is the distance from the point of integration
to the point of observation R; a similar expression holds for the vector
potential. But when R >> a, these integrals go into the form
$$
\frac{1}{2\pi} \int_{-1}^1 \frac{T_n(z)}{\sqrt{1-z^2}} e^{iqz} dz = (i/2)^n J_n(q)
$$
and (10) reduces to
$$
\phi(R) = e \sum_n i^{-n} J_n(nka \cos\alpha) e^{-in\omega t} \frac{e^{inkR}}{R}
$$
where $\alpha$ is the angle between the direction of observation and the
direction of motion. Already, this looks very much like some of
Schwinger's results.

The rest of the solution is straightforward, and we find for the power
radiated, in the n'th harmonic, into the element of solid angle
$d\Omega$:
$$
\frac{dP_n}{d\Omega} d\Omega = \frac{e^2 \omega^2 n^2}{2\pi c} J_n^2(nka \cos\alpha) \tan^2\alpha d\Omega
$$
and the total power in the n'th harmonic is
$$
P_n = \frac{2e^2 n^2 \omega^2}{c} \int_0^1 J_n^2(nkaq) (q^{-2} - 1) dq
$$

These are the exact results for a point charge following the orbit (8).
If $nka \ll 1$, (14) goes into
$$
P_n = \frac{4e^2 n^2 \omega^2 (nka/2)^{2n}}{c(n!)^2(4n^2-1)}
$$
which again, for n=1 yields the elementary textbook result
$P_1 = e^2 a^2 \omega^4 / 3c^3$ (half of Schwinger's $P_1$, since his
circular orbit amounts in this limit to two orthogonal dipoles radiating
independently).

At other electron energies than 100 Mev, we see from (6), (7) that the
transverse displacement, a, will vary as $\gamma^{-1}$, while
$$
ka = \frac{e}{mc\omega_0} \left( \frac{4\pi S_0}{c} \right)^{1/2}
$$
is independent of $\gamma$. In the Stanford LINAC, $ka \sim 0.02$, and
harmonic production is always small. A machine operating at higher power
and/or lower frequency would generate correspondingly more harmonics.

## BACK TO THE LABORATORY SYSTEM

In view of the foregoing, we need consider only the conventional Thomson
scattering at the fundamental frequency $\omega^\prime$, in spite of the
enormous intensity S' of the incident wave. In the electron's reference
frame, it scatters a dipole wave of frequency $\omega^\prime$ and intensity
given from (13) as
$$
\frac{dP_1}{d\Omega} d\Omega = \frac{e^2 c}{8\pi a^2} (ka)^4 \sin^2\alpha d\Omega
$$

To find how this appears in the laboratory frame, we introduce an
azimuth angle $\phi$ about the z-axis measured from the plane of
polarization, and the angle $\theta^\prime$ between some propagation direction
and the z-axis, as seen in the electron's reference frame. From
spherical trigonometry, we can replace in (17)
$$
\sin^2\alpha = 1 - \cos^2\phi \sin^2\theta^\prime
$$

Applying the relativistic abberation and Doppler effect formulas,
radiation which in the electron's reference frame is emitted at an angle
$\theta^\prime$ to the z-axis with frequency $\omega^\prime$, will appear in the
laboratory frame to have direction $\theta$, frequency $\omega$, where
$$
\begin{aligned}
\cos\theta &= \frac{\beta + \cos\theta^\prime}{1+\beta\cos\theta^\prime} \\
\omega &= \gamma(1 + \beta\cos\theta^\prime)\omega^\prime = 2\gamma^2(1 + \beta\cos\theta^\prime)\omega_0
\end{aligned}
$$

In the electron's frame half the energy is emitted in the forward
hemisphere $0 < \cos\theta^\prime < 1$. This appears in the
laboratory frame as $\beta < \cos\theta < 1$, which becomes in the
extreme relativistic limit $0 < \gamma\theta < 1$, just the
aforementioned forward cone of angle $\theta = \gamma^{-1}$. Since both
energy and frequency of a plane wave transform as the time component of
a four-vector, the ratio $n = E/\hbar\omega$ is an invariant; i.e., half
the "photons" are emitted into this cone.

Eliminating $\theta^\prime$ between (19) and (20), we have the variation of
frequency with angle as seen in the laboratory system:
$$
\omega = \frac{(1+\beta)\omega_0}{1-\beta\cos\theta} = \frac{4\gamma^2\omega_0}{1+\gamma^2\theta^2}
$$

The observed frequency is a maximum in the forward direction, and drops
to half that value at the cone angle $\theta = \gamma^{-1}$.

At 100 Mev, with $\omega_0$ corresponding to a microwave wavelength
$\lambda_0 = 10$ cm, the wavelength at the center of this spot would be
$\lambda = \lambda_0/4\gamma^2 = 6460$ Å, or visible red light. At 127
Mev, we would have at the center of the spot $\lambda=4000$ Å, about the
limit of visibility in the blue; and this would shade through the
spectrum to red at an angle of somewhat less than
$\theta = \gamma^{-1} = 0.23$ degrees from the axis. At any higher
electron energy, the visible radiation would appear in a tiny circular
rainbow, blue on the inside to red on the outside, whose cone angle
would tells us the electron energy.

To find the absolute intensity and spectral distribution of energy as
seen in the laboratory system, we can take advantage of the invariance
of photon number (a useful mathematical property whether or not one has
a literal belief in photons). Suppose the accelerator pulse has duration
$t_0 \sim 2 \times 10^{-6}$ sec in the laboratory system. In the
electron's frame this will be contracted to $t^\prime = t_0/2\gamma$, during
which time it is scattering the power $P_1 = e^2 c(ka)^4/3a^2$. Crudely,
then, we can say that during a pulse an electron shakes off about
$$
N = \frac{P_1 t^\prime}{\hbar\omega^\prime} = \frac{e^2}{\hbar c}(ka)^2 \frac{\omega_0 t_0}{3}
$$
photons. Being invariant, this same number will appear in the laboratory
system, transformed to various frequencies. [In fact, as we see from
(16), N is not only Lorentz invariant, it is also independent of the
electron energy $\gamma$, being determined by the value of
$(S_0 t_0 / \omega_0)$ in the machine design; i.e., on the number of
microwave photons supplied per pulse.]

Integrating (18) over the azimuth angle $\phi$, the number of photons
emitted into the solid angle $d\Omega^\prime = 2\pi d\cos\theta^\prime$ of an
annular ring $d\theta^\prime$, is
$$
dN = \frac{3N}{4}(1+\cos^2\theta^\prime) d\cos\theta^\prime
$$

In the laboratory
frame, these same photons will appear in the annulus of solid angle
$d\Omega = 2\pi d\cos\theta = 2\pi\theta d\theta$. From (21) they have
frequencies in the range given by
$$
\frac{d\omega}{\omega} = - \frac{2\gamma^2\theta d\theta}{(1+\gamma^2\theta^2)}
$$
while in the relativistic limit, the abberation law (19) goes into
$$
\cos\theta^\prime = \frac{1-\gamma^2\theta^2}{1+\gamma^2\theta^2}
$$

In the
laboratory frame, therefore, we obtain an energy in the range $d\omega$
of $I(\omega)d\omega = \hbar\omega dN$; i.e., the spectral energy
density is from (23)-(25):
$$
I(\omega) = \frac{\hbar\omega dN}{d\omega} = 3\hbar N \left[\frac{\omega}{\omega_{\text{max}}}\right] \left[ 1 + \left(\frac{\omega_{\text{max}}}{\omega} - 1\right)^2 \right]
$$
where from (21), $\omega_{\text{max}} = 4\gamma^2\omega_0$ is the
highest frequency obtained.

The light energy per electron per pulse that is emitted into the forward
cone $\theta = \gamma^{-1}$ is then
$$
\int_{1/2 \omega_{\text{max}}}^{\omega_{\text{max}}} I(\omega) d\omega = \frac{25}{32} N \hbar \omega_{\text{max}}
$$

From (22) and the numerical values discussed above, we find N = 0.04. If
at each pulse the electron gun injects 100 milliamperes of current for
one microsecond, it would provide $6 \times 10^{11}$ electrons. Taking
$10^{11}$ as a conservative value, we then find that the machine should
emit, at each pulse, a light energy of about
$3 \times 10^9 \hbar\omega_{\text{max}}$, an easily visible amount.
This is only a crude estimate, ignoring the change of electron energy
during a pulse. Clearly, however, a device made specifically to enhance
this radiation could produce far more than our estimate. Thus, while the
LINAC does not provide the spectacular light radiation of the
synchrotron, it should produce some radiation that becomes visible above
100 Mev.

Of course, the fact that N $\ll$ 1 above is irrelevant to the argument,
which actually used only the fact that the ratio (energy)/(frequency) is
Lorentz invariant; and this is true whether or not photons are
physically real. Indeed, the term "photon" may be construed merely as
a convenient Lorentz-invariant unit of energy; just as "magneton"
denotes not a physical particle, but a certain amount of magnetic
moment. Then there can be no objection to use of the photon in purely
classical calculations. To emphasize this, note that our final result
(27) is independent of the numerical value of $\hbar$, because $N\hbar$
is.

## THE UNDULATOR

In the Summer of 1947 I returned to Stanford and wrote up the above
analysis, which was circulated privately to interested persons, but was
not considered of enough earth-shaking importance to warrant
publication. Clearly, as efficient sources of visible light,
synchrotrons and LINACS compare rather unfavorably with Thomas Edison's
tungsten filament. The idea of producing coherent visible light was at
that time far beyond the dreams of science fiction; probably, if anyone
had dared to suggest it, physicists would have held such a thing to be
fundamentally impossible for one of those mysterious quantum-mechanical
reasons that everybody invokes but nobody understands.

However, with the rapid development of molecular spectroscopy and
thoughts of ultra-short-pulse radars, efforts to push the usable
microwave spectrum into the millimeter-wave region were pursued
vigorously in many laboratories. My prediction of visible light from the
LINAC came to the attention of Hans Motz, and he conceived a variant of
the idea which could produce coherent millimeter waves from a
high-energy electron beam.

The Undulator[^motz1951] passes the electrons through a comb-like
structure of permanent magnets, reversing the magnetic field at each
tooth of the comb. Thus the electron beam is forced to "undulate" and
radiate light which, in the forward direction, can be relatively intense
because at these longer wavelengths a bunch of N electrons can be made
to radiate coherently. Needless to say, the Undulator worked as
predicted, but with the large amount of apparatus needed, it was hardly
competitive with other methods of generating millimeter waves. To the
best of my knowledge, no further work has been done on it since the
early 1950's.

## THE CYCLOTRON-MASER EQUATIONS

Also in the Summer of 1947, having just completed J. R. Oppenheimer's
course in quantum theory at Berkeley, I was toying with alternative ways
of writing the Schrödinger equation. One form in particular made an
impression on me, although it is simple only for a two-level system.
Suppose a two-level atom is perturbed by an electric field:

$V = -\mu E(t)$ where $\mu$ is the dipole moment matrix element between
the levels. Then writing $\psi(t) = a_1(t)\psi_1 + a_2(t)\psi_2$, the
amplitudes satisfy
$$
\begin{aligned}
i\hbar \dot{a}_1 &= E_1 a_1 - \mu E(t)a_2 \\
i\hbar \dot{a}_2 &= E_2 a_2 - \mu E(t)a_1
\end{aligned}
$$

If we introduce the quantities
$$
\begin{aligned}
W(t) &= E_1|a_1|^2 + E_2|a_2|^2 - \frac{1}{2}(E_1 + E_2) \\
M(t) &= 2\mu \text{Re}(a_1 a_2^*)
\end{aligned}
$$
usually interpreted as expectations of energy and dipole
moment, then Equations (28) can be rewritten in the suggestive form
$$
\begin{aligned}
\ddot{M} + \omega^2 M &= -K^2 W E(t) \\
\dot{W} &= E(t)\dot{M}
\end{aligned}
$$
where $\omega = (E_2-E_1)/\hbar$, $K=2\mu/\hbar$. We see
that the Schrödinger equation has a simple physical content that cannot
be seen from (28); it states that the dipole moment oscillates according
to a driven harmonic oscillator equation, the only "new" feature being
that the coupling constant ($-K^2 W$) varies slowly with time and has
opposite signs depending on whether the atom is near the upper or lower
state.

That a two-level system can be given a Bloch sphere representation is
seen at once from the fact that Equations (31) possess the first
integral
$$
\dot{M}^2 + \omega^2 M^2 + K^2 W^2 = \text{const} = \omega^2 \mu^2
$$
which, in suitable coordinates (x,y,z) proportional to $(\dot{M},M,W)$,
is the unit sphere, $x^2 + y^2 + z^2 = 1$.

When, in the middle 1950's, Professor Willis Lamb showed me his theory
of the ammonia maser, I immediately rewrote it in the form (31), which
made the physical operation of the device seem much clearer. This marked
the beginning of neoclassical theory[^jaynes1973].

Bear with me--we have not really left the topic of free electrons. For
also in the middle 1950's, Professor Charles Kittel gave a Seminar talk
at Stanford on cyclotron resonance techniques for elucidating band
structure in solids. This set me to thinking again about the generation
of radiation from fast electrons, using static magnetic fields in other
ways than in the undulator.

The most obvious thing is just the inverse cyclotron; fire electrons
into a uniform magnetic field and they will radiate at their cyclotron
frequency.

Although that idea has been pretty well exploited and extended in the
magnetrons that today cook our food, let us look at the equation of
motion of a nonrelativistic electron
$$
m\dot{\mathbf{v}} = e \left[ \mathbf{E} + \frac{1}{c}(\mathbf{v} \times \mathbf{H}) \right]
$$
in which $H_z = H_0 = \text{const.}$, while other field components may
be time dependent. If we have only oscillating electric fields,
$H_x = H_y = 0$, (33) yields
$$
\begin{aligned}
\dot{v}_x - \omega_0 v_y &= \frac{e}{m}E_x \\
\dot{v}_y + \omega_0 v_x &= \frac{e}{m}E_y
\end{aligned}
$$
where $\omega_0 = (e/mc)H_0$ is the cyclotron frequency. If $E_y = 0$, we
can write
$\ddot{y} = \dot{v}_y = -\omega_0 v_x = -\omega_0 \dot{x}$, whence by a
time integration and suitable choice of the origin, (34a) becomes a
driven harmonic oscillator equation for the x coordinate of the
electron:
$$
\ddot{x} + \omega_0^2 x = \frac{e}{m}E_x(t)
$$

This is the usual result, and is not of particular interest for present
purposes; the coupling constant is invariable and so the phenomena
allowed by (31) in the maser do not appear.

Now let's introduce a variable magnetic field $H_x(t)$. If $H_y$ and the
electric field are zero, the equations of motion are
$$
\begin{aligned}
\dot{v}_x - \omega_0 v_y &= 0 \\
\dot{v}_y + \omega_0 v_x &= \frac{e}{mc} v_z H_x \\
\dot{v}_z &= -\frac{e}{mc} v_y H_x
\end{aligned}
$$

By a time integration of (36a) and proper choice of the
origin we have $v_x = \omega_0 y$; and the equations of motion reduce to
$$
\begin{aligned}
\ddot{y} + \omega_0^2 y &= \frac{e}{mc} H_x v_z \\
\dot{v}_z &= -\frac{e}{mc} H_x \dot{y}
\end{aligned}
$$

It is apparent at once that these have the same
structure as (31); but let us make the analogy stronger by defining the
y-component of electric dipole moment, and a quantity of the dimensions
of the energy:
$$
\begin{aligned}
M(t) &= ey(t) \\
W(t) &= -mc v_z(t)
\end{aligned}
$$

Equations (37) then reduce to
$$
\begin{aligned}
\ddot{M} + \omega_0^2 M &= -K^2 W H_x(t) \\
\dot{W} &= H_x(t)\dot{M}
\end{aligned}
$$
with $K=(e/mc)$.

The formal analogy with the two-level Schrödinger equation (31) is
complete. Of course, the numerical constants and physical meanings are
different. For example, in the case of the ammonia molecule in a maser,
the right-hand side of (32) is fixed at $\omega^2\mu^2$ by laws of
physics [in fact, (32) is just the relation $|a_1|^2+|a_2|^2 = 1$
usually called conservation of probability]; while the corresponding
integral of (40) merely expresses conservation of energy, and the
right-hand side can have any value, determined by the initial
conditions. Also, a magnetic field alone cannot transfer energy to or
from the electron, since the Lorentz ($\mathbf{v} \times \mathbf{H}$)
force is orthogonal to the velocity. So we must introduce also electric
field terms into the equations of motion before we can obtain a
maser-like amplification.

Suppose, then, that the above field $H_x$ is part of a plane wave
traveling in the z-direction, so that we have a field
$E_y = -\alpha H_x$. [In free space $\alpha=1$, but in a guided wave
structure $\alpha$ measures the wave impedance, and can be either
greater or less than unity.] We must then add a term $(e^2/m)E_y$ to
the right-hand side of (40a), and it becomes
$$
\ddot{M} + \omega_0^2 M = \frac{e^2}{mc}(v_z - \alpha c) H_x
$$

Suppose
that initially an electron is injected at velocity $v_z$ along the z
axis, so that $M(0)=\dot{M}(0)=0$, and a wave
$H_x = H_1 \cos(\omega t - kz + \phi)$ is present. Let us solve (41) for
a time interval many cycles of $\omega_0$ but short enough so that $v_z$
has not changed appreciably. At time t, the electron then sees the field
at position $z=v_z t$, so its transverse motion is given by
$$
\ddot{M} + \omega_0^2 M = A \cos(\omega^\prime t + \phi)
$$
where
$$
\begin{aligned}
\omega^\prime &\equiv \omega - kv_z \\
A &\equiv \frac{e^2}{mc}(v_z - \alpha c) H_1
\end{aligned}
$$

The solution is
$$
M(t) = A \int_0^t \cos\omega_0(t-t^\prime) \cos(\omega^\prime t^\prime+\phi) dt^\prime = \frac{A}{2} \frac{\sin(\omega^\prime t+\phi) - \sin(\omega_0 t+\phi)}{\omega^\prime-\omega_0}
$$
and at time t the electron has transferred energy to the field of
$$
E(t) = -\int_0^t E_y(t^\prime) \dot{M}(t^\prime) dt
$$
$$
= \frac{\alpha A H_1}{4} \left[ \frac{1-\cos((\omega^\prime-\omega_0)t)}{(\omega^\prime-\omega_0)^2} \right]
$$
independent of the initial phase $\phi$. This is a maximum at resonance,
$\omega^\prime = \omega_0$, for which
$$
E(t) = \frac{e^2 H_1^2}{8mc}(v_z - \alpha c)^2 t^2
$$
and the criterion for amplification is
$$
v_z > \alpha c
$$

We then need $\alpha<1$, which
is the case for a TM waveguide mode.

From waveguide theory, the wave impedance and propagation constant for a
TM wave mode of cutoff frequency $\omega_c$ are given by
$$
ck = \omega\alpha = (\omega^2-\omega_c^2)^{1/2}
$$

The system will therefore amplify and oscillate, delivering the kinetic energy
$mv_z^2/2$ to the radiation field, at a frequency $\omega$ given by the
root of
$$
\omega - \frac{v_z}{c}\sqrt{\omega^2-\omega_c^2} = \omega_0
$$
provided that (48) is also satisfied at this value of $\omega$.

By graphical analysis one sees that these conditions are readily
satisfied; for example, choosing $\alpha=1/4$, $v_z/c = 1/2$, we find a
solution for
$$
\begin{aligned}
\omega &= \frac{8}{7}\omega_0 = 1.143 \omega_0 \\
\omega_c &= \frac{2}{\sqrt{7}}\sqrt{15} \omega_0 = 1.107 \omega_0
\end{aligned}
$$

The stimulation from Kittel's talk carried me this far by late 1959. Clearly,
much more analysis is needed, to calculate gain, power, efficiency, etc.
before one would be in a position to pass judgment on the practicality of
such a system. It is interesting that the possibility of wave
amplification arises here from the sign reversal of coupling coefficient
in (41) at $v_z = \alpha c$, just as the possibility of amplification
in a maser or laser arises from the sign reversal of W in (31) that
signifies the change from net absorption to net stimulated emission.
Needless to say, this analysis leaves it an open question whether other
configurations might be superior in power, efficiency, stability, etc.
Presumably, use of a circularly polarized wave would double the rate of
energy transfer.

## SCHWARZ-HORA EFFECT (?)

An entirely different principle by which free electrons might be made to
produce light, about which I and many other people did some thinking in
1970, concerns the "blue electron" effect reported by Schwarz and Hora[^schwarzhora1969]. I don't want to get into controversies about whether the effect
has in fact been seen; and whether it could have been, with present
electron optics techniques. But I think it is legitimate and important
to raise the question whether, *in principle, according to present
quantum theory, such an effect should exist*.

In fact, a number of theoreticians (including myself) were able, without
the slightest difficulty, to give quantum-mechanical calculations which
predicted virtually everything that Schwarz and Hora reported seeing.
And, at least in my own version of the theory, there was no reason to
think that technical problems of collimation would prevent one from
seeing this light.

It does not speak well for quantum theory if it can so glibly account
for nonexistent effects. Anyone who believes that this has happened can
hardly avoid asking how many other nonexistent effects it has been
predicting all these years; and how much we have been misled in our
picture of Nature's workings, as a result.

Schwarz and Hora reported that 50 kev electrons (v/c $\sim$ 0.4) were
diffracted by a crystal and simultaneously irradiated by blue light
(4880 Å) from an argon laser, polarized with the electric vector
parallel to the electron beam; and that on drifting 25 cm and striking
an alumina screen (nonluminescent or nearly so for ordinary electrons),
they emitted blue light at the position of the normal diffraction spots.
Many people immediately took up a simple classical explanation: the
light produces a periodic velocity modulation, making the arrangement an
"optical klystron." However, the reported primary beam current
($10^{-6}$ ampere) was only one electron per 100 optical cycles; the
current falling on any one diffraction spot must have been far less.
Thus there are no real "bunches." Under these conditions, one should
have observed instead an incoherent continuous spectrum of light, with
only a negligible portion appearing at the optical frequency $\omega$.
To demonstrate this, let us ignore for the moment the difficulties about
velocity spread and suppose perfect coherence; electrons can arrive at
the screen only at the instants $t_k=k\tau$, where $\tau = 2\pi/\omega$
is the optical period, and let $n_k$ be the number of electrons arriving
at time $t_k$. If the average current is n electrons per second, the
$n_k$ are random variables with expectations $\langle n_k \rangle = n\tau$, and the
net current is then the random function
$$
J(t) = e \sum_{k=-\infty}^\infty n_k \delta(t-t_k).
$$

 With independent
Poisson distributions for the $n_k$, the second moments are
$\langle n_k n_{k^\prime} \rangle = n^2 \tau^2 + n\tau\delta_{kk^\prime}$, which yields the
spectral density
$$
I(\nu) = \lim_{T\to\infty} \frac{1}{2T} \int_{-T}^T dt \int_{-T}^T dt^\prime \langle J(t)J(t^\prime) \rangle e^{i\nu(t-t^\prime)}
$$
$$
= e^2 \left[ n + 2\pi n^2 \sum_{r=-\infty}^{\infty} \delta(\nu-r\omega) \right]
$$
of which the first term was given long ago by Schottky. The radiation
from this current thus consists of a continuous spectrum of amplitude
proportional to n, superimposed on a line spectrum at the fundamental
and its harmonics, proportional to $n^2$. The ratio (energy in line
spectrum)/(energy in continuous spectrum) is from (54)

$2\pi n^2/n\omega = n\tau$, just the average number of electrons per
bunch.

In a microwave klystron, $n\tau \gg 1$, and we obtain essentially a pure
line spectrum; but in the SH experiment, $n\tau < 10^{-3}$ for any
diffraction spot, so according to classical bunching theory practically
all the radiation should be in the continuous spectrum. With imperfect
coherence, the line spectrum will be still further suppressed.

We conclude that the effect cannot depend on any regularity in arrival
times of different electrons; instead, each individual electron must, in
some way, retain a "memory" of the light frequency for at least a
million cycles after irradiation, and therefore the effect must be an
essentially quantum-mechanical one.

We indicate such a mechanism by a crude calculation. An incident
electron is represented by a wave packet
$$
\psi_0(\mathbf{x}, t) = (2\pi)^{-3}\int d^3k \, \psi_0(\mathbf{k}, t) \exp(i\mathbf{k}\cdot\mathbf{x})
$$
where
$$
\psi_0(\mathbf{k}, t) = \psi_0(\mathbf{k}) \exp(-i\omega_k t)
$$
with
$$
\omega_k = \hbar k^2/2m,
$$
and the light wave by the vector
potential
$$
\mathbf{A}(\mathbf{x},t) = \mathbf{A}_0 \epsilon \cos(\omega t - \mathbf{q}\cdot\mathbf{x} + \phi)
$$
where $\epsilon$ is a unit polarization vector,
$\epsilon\cdot\mathbf{q}=0$, and $\omega = cq$. Since the electron
momentum is well defined, $\psi_0(\mathbf{k})$ will be sharply peaked
about the value $\mathbf{k}_0$ such that $\hbar^2 k_0^2 = 2mE$, and
approximations of the form
$(\epsilon\cdot\mathbf{k}_0) = (\epsilon\cdot\mathbf{k})$ will be
justified.

The perturbed wave packet is $\psi(\mathbf{x},t) = \psi_0 + \psi_1 + \dots$, where the first-order term is the solution of
$$
i\hbar\dot{\psi}_1 - p^2/2m \psi_1 = -(e/mc)\mathbf{A}\cdot\mathbf{p} \psi_0(\mathbf{x},t)
$$
which vanishes in the remote past. In the experiment, the electrons
drifted through a narrow light beam, spending of the order of 40 to 400
optical cycles in it. Accordingly, suppose that the field (58) is
switched on at time t=0, and off again at $t=\tau$ (actually, the sharp
edges of the crystal provide this switching, which prevents the solution
from following adiabatically in the fringing field at the edge of the
light beam). The solution of (59) for $t > \tau$ is then
$$
\psi_1(\mathbf{k},t) = \frac{eA_0}{2mc}(\epsilon\cdot\mathbf{k}) \left[ e^{i\phi} \psi_0(\mathbf{k}+\mathbf{q}) \frac{e^{i\omega_+ \tau}-1}{\omega_+} + e^{-i\phi} \psi_0(\mathbf{k}-\mathbf{q}) \frac{e^{i\omega_- \tau}-1}{\omega_-} \right] e^{-i\omega_k t}
$$
where $\omega_\pm = \omega_k - \omega_{k\pm q} \mp \omega$. From this
one sees that there is no secular buildup of either term, since from the
exact dispersion law,
$\omega_k = c[k^2 + (mc/\hbar)^2]^{1/2}$, $\omega_+$ and $\omega_-$ cannot
vanish for any value of k (in diagram language, energy and
momentum cannot both be conserved at a single vertex). Furthermore, in
the experimental arrangement $\mathbf{q}\cdot\mathbf{k}_0=0$, and
$\omega_q/\omega = \hbar q/2mc \sim 10^{-6}$, so the differences
$|\omega_k - \omega_{k\pm q}|$ are negligible compared to $\omega$ for
all k values for which $\psi_0(\mathbf{k}\pm\mathbf{q})$ is appreciable.
Therefore, we may write simply $\omega_\pm = \pm\omega$.

Presence of the amplitude factor
$(\epsilon\cdot\mathbf{k}) = (\epsilon\cdot\mathbf{k}_0)$ in (60)
accounts for the reported polarization effect. However, because of the
lack of any secular buildup, the perturbation does not tend to emphasize
any particular frequency component in $\psi_1$, and so memory of the
light frequency is not contained in the subsequent time variation of the
wave function.

Equation (60) predicts that the amplitude of the effect should oscillate
periodically with the interaction time $\tau$, and therefore with the
beam voltage, according to $|e^{i\omega\tau}-1|$. In the following we
assume the optimum interaction time, corresponding to
$\exp(i\omega\tau)=-1$, and the optimum polarization,
$(\epsilon\cdot\mathbf{k}_0) = k_0$.

Noting that the factor $r_0 = eA_0/mc\omega$ is just the displacement of
a classical point electron in the field $A_0$ and transforming back to
ordinary space, the first-order change in the wave function becomes
$$
\psi_1(\mathbf{x},t) = k_0 r_0 [e^{i(\mathbf{q}\cdot\mathbf{x}-\phi)} \psi_0(\mathbf{x}-\mathbf{v}t,t) - e^{-i(\mathbf{q}\cdot\mathbf{x}-\phi)} \psi_0(\mathbf{x}+\mathbf{v}t,t)] e^{-i\omega_q t}
$$
where
$\mathbf{v} = \hbar\mathbf{q}/m = 1.5 \times 10^5 \text{ cm sec}^{-1}$
is the recoil velocity of an electron which has absorbed the momentum
$\hbar\mathbf{q}$ from the light wave. The frequency
$\omega_q = \hbar q^2/2m$ is in the microwave range, 1.53 GHz. In first
order, therefore, two new wave packets appear which separate from the
parent at the recoil velocity, their centers reaching a separation of 3
microns and the phase term $\exp(-i\omega_q t)$ oscillating through
about three cycles, during the 2 nsec drift time.

It is one of the most interesting features of this experiment that
nothing in the experimental conditions seems to determine the size or
shape of the incident wave packet $\psi_0(\mathbf{x},t)$; and yet, as we
will see, observable effects depend on these details. The dimensions of
a reasonable wave packet are very large compared to the electron's de
Broglie wavelength ($4\times 10^{-10}$ cm), and the "quantum-mechanical
spreading" of the packets will be negligible; thus we may approximate
the incident wave packet by an envelope function f(x,y,z) of constant
size and shape. We readily verify that if $\omega_0 = \hbar k_0^2/2m$,
and $\mathbf{v}_0 = \hbar\mathbf{k}_0/m$, the group velocity, the
function
$$
\psi_0(x,y,z,t) = f(x,y,z-v_0t) \exp(ik_0 z - i\omega_0 t)
$$
is an accurate solution of the free-space Schrödinger equation if
$\nabla^2 f$ can be neglected in comparison with $k_0^2 f$. In the
present case, any reasonably smooth envelope function f(x,y,z) of a few
microns width leads to $|\nabla^2 f/k_0^2 f| \sim 10^{-12}$. We have
chosen the hyperbolic secant function, taken for ease of calculation in
product form:
$$
f(x,y,z) = (8a^3)^{-1/2} \text{sech}(x/a)\text{sech}(y/a)\text{sech}(z/a)
$$

The choice a=1.70 microns yields a wave packet of width 3 microns
between "half-way down" points of $|\psi|^2$.

After irradiation, the perturbed wave function corresponds to an
effective charge density
$$
\rho = e|\psi_0 + \psi_1 + \dots|^2 = e|\psi_0|^2 + 2e\text{Re}(\psi_0^* \psi_1) + \dots
$$
in which the second term, arising from interference between the parent
and daughter wave packets, contains terms oscillating in space with the
wavelength of the light: from (61), (62), and (63) we have
$$
2e\text{Re}(\psi_0^*\psi_1) = \frac{ek_0r_0}{4a^3}[g_-(x)-g_+(x)]\text{sech}^2(y/a)\text{sech}^2((z-v_0t)/a)
$$
where
$$
g_\pm(x) = \cos[q(x\pm vt/2)-\phi] \text{sech}(x/a) \text{sech}[(x\pm vt)/a]
$$
in which we have used the relation $\omega_q = qv/2$ and chosen the
x-axis along the direction of the light propagation vector q.

Now the meaty part of the calculation begins. We use the charge density
(64) next to find the corresponding z-component of the current
$J_z(\mathbf{x},t) = \rho(\mathbf{x},t)v_0$. To calculate the radiation
we need the fourier transform
$$
J_z(\mathbf{k},\omega) = \int_{z\lt d} d^3x \int dt \, J_z(\mathbf{x},t) e^{i(\mathbf{k}\cdot\mathbf{x}-\omega t)},
$$
the constraint z<d expressing the fact that the current is suddenly
decelerated to zero at the screen, which we suppose to be the source of
the radiation. For radiation in the x-direction we find the analytical
result
$$
I(\omega) \sim \left| \frac{\sin(kvt/2)}{\sinh(vt/a)} \frac{\sin[(k-q)vt/2]}{\sinh[\pi(k-q)a/2]} \right|^2
$$

This yields an asymmetric spectrum in general; computer evaluations of
(68) show smooth bell-shaped curves centered at values of (k-q)a usually
in the range $\pm1$, with full width at half maximum of about
$\Delta k = a^{-1}$; thus in this version of the theory the dimensions
of the original wave packet are determined crudely by the observed
spectral width. The shape of the spectrum is a kind of convolution of the
shape of the original wave packet. Such a measurement, if successful,
would represent the first observation of a new property of free
electrons, that has never before been accessible to experiment. A
"periodicity" like that reported by Schwarz also appears if we examine
(68) over a wide range of (vt/a).

In this analysis the effect is contained, not in the time behavior of
the wave function, but in its space periodicity which develops in the
drift time following irradiation. Since each electron radiates
independently of the others, there should be no particular collimation
problems.

Since 1972 there has been a general disinclination to believe in the
existence of this effect. While I cannot judge the reliability of an
experiment that I did not witness, it does seem to me that definite
proof of its nonexistence would be a considerable embarrassment to
quantum theory (or at least to the quantum theorists who found it so
easy to account for). And against whatever improbability it may have, one
must balance the obvious importance of finding out about it, if it
does exist. So I hope experimentalists will not forget about it
entirely.

## REFERENCES

[^elder1948]: Elder, Langmuir, and Pollock, Phys. Rev. 74, 52 (1948).
[^iwanenko1944]: D. Iwanenko and I. Pomeranchuk, Phys. Rev. 65, 343 (1944).
[^jaynes1952]: E. T. Jaynes, Jour. App. Phys. 23, 1077 (1952).
[^jaynes1973]: E. T. Jaynes, in *Coherence and Quantum Optics*, L. Mandel and E. Wolf, Editors, Plenum Publishing Corp., New York (1973); pp. 35-81.
[^motz1951]: H. Motz, Jour. App. Phys. 22, 527, 1217 (1951).
[^schiff1946]: L. I. Schiff, Rev. Sci. Inst. 17, 6 (1946).
[^schiff1952]: L. I. Schiff, Am. Jour. Phys. 20, 474 (1952).
[^schwarzhora1969]: H. Schwarz and H. Hora, App. Phys. Lett. 15, 349 (1969). For a very complete bibliography of later discussions, see H. Hora, *Il Nuovo Cimento* 26, 295 (1975).
[^schwinger1946]: J. Schwinger, Phys. Rev. 70, 798 (1946).
[^schwinger1949]: J. Schwinger, Phys. Rev. 75, 1912 (1949).
