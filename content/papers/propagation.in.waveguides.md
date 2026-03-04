---
title: "Propagation in Ferrite-Filled Transversely Magnetized Waveguide"
author: ["P. H. Vartanian", "E.T. Jaynes"]
year: 1956
abstract: >
  A solution to the problem of propagation of higher modes
  in a transversely magnetized ferrite-filled rectangular waveguide has
  been found. The solutions to the problem are expressed in the form of
  four rigorous nonlinear algebraic equations which characterize the
  problem and are ready for numerical solution. The dependence of the
  fields in the direction of magnetization is the same as for the
  classical modes.
---
WE SHALL consider the problem of propagation in a rectangular waveguide
which is completely filled with ferrite and magnetized transversely to
the direction of propagation.

This problem is becoming of more interest as lower loss ferrites are
developed. As these very low-loss ferrites become available, a class of
devices depending on the ability of a dc magnetic field to change the
propagation constant within a waveguide will become practical. With the
transverse field geometry, these devices will operate at low field
values far from gyromagnetic resonance. They will be characterized by
transverse fields which are distorted by the applied magnetic field.
This will make this geometry useful in field displacement devices such
as isolators and radiators.

We shall hence find the fields and propagation constants for the modes
in this particular ferrite geometry. They will be characterized by
parameters which continuously vary with increasing magnetic field from
the classical TE and TM modes into a new set of modes having fields and
propagation constants which are magnetically controllable.

Gamo[^4] and Kales[^5] have investigated the case of the longitudinally
magnetized filled cylindrical waveguide. Van Trier[^6] has solved the
case of the TE~10~ mode in the transversely magnetized waveguide and
found that the new mode is a TE mode with a distorted transverse field
dependence. Mikaelyan[^7] and recently Chevalier[^8].

The problem
then, is that of propagation in an infinitely long rectangular waveguide
shown in Fig. 1, which is filled with ferrite and transversely
magnetized along the x direction. The solutions to the problem will be
expressed in terms of four rigorous nonlinear algebraic equations which
characterize the problem and are ready for numerical solution.

**[FIGURE: Coordinate system.]**

Eqs. (1) and (2) are Maxwell's equations written in a form to show the
tensor permeability. All field quantities vary as exp
($j\omega t-\gamma z$).
$$\begin{pmatrix} 0 & \gamma & \frac{\partial}{\partial y} \\\\ -\gamma & 0 & \frac{\partial}{\partial x} \\\\ \frac{\partial}{\partial y} & -\frac{\partial}{\partial x} & 0 \end{pmatrix}
    \begin{pmatrix} E_x \\\\ E_y \\\\ E_z \end{pmatrix}
    = -j\omega\mu_0 \begin{pmatrix} 1 & 0 & 0 \\\\ 0 & \mu & -jK \\\\ 0 & jK & \mu \end{pmatrix}
    \begin{pmatrix} H_x \\\\ H_y \\\\ H_z \end{pmatrix}\tag{1}$$
$$\begin{pmatrix} 0 & \gamma & \frac{\partial}{\partial y} \\\\ -\gamma & 0 & \frac{\partial}{\partial x} \\\\ \frac{\partial}{\partial y} & -\frac{\partial}{\partial x} & 0 \end{pmatrix}
    \begin{pmatrix} H_x \\\\ H_y \\\\ H_z \end{pmatrix}
    = j\omega\epsilon \begin{pmatrix} E_x \\\\ E_y \\\\ E_z \end{pmatrix}\tag{2}$$

The elements in the permeability tensor are known [^9], given the applied
magnetic field and frequency. For zero applied field, $\mu$ becomes
unity and $K$ zero. It is important to note that the tensor properties
of the ferrite are limited to the y-z plane, that is, the plane
perpendicular to the applied field.

From Maxwell's equations we derive the relations for the transverse
fields in terms of the longitudinal fields.

$$\begin{aligned}
    E_x &= \frac{1}{k_{tx}^2} \left( j\omega\mu_0 \frac{\partial H_z}{\partial x} - \gamma \frac{\partial E_z}{\partial y} \right) \\\\
    H_x &= \frac{1}{k_{tx}^2} \left( j\omega\epsilon \frac{\partial E_z}{\partial y} - \gamma \frac{\partial H_z}{\partial x} \right) \\\\
    E_y &= \frac{-1}{k_{ty}^2} \left( j\omega\epsilon_0 \frac{\partial E_z}{\partial x} + \gamma \frac{\partial H_z}{\partial y} - \omega\mu_0 K \gamma H_z \right) \\\\
    H_y &= \frac{-1}{k_{ty}^2} \left( j\omega\epsilon \frac{\partial E_z}{\partial y} + \gamma \frac{\partial H_z}{\partial x} - j\gamma K H_z \right)
\end{aligned}$$

where

$$k_{tx}^2 = \gamma^2+k^2 \qquad k^2 = \omega^2\epsilon\mu_0$$
$$k_{ty}^2 = \gamma^2+k^2\mu$$

It is seen that these are of the usual form except that the $E_y$ and
$H_y$ relations have extra terms proportional to $H_z$. Physically this
is the rotational effect of the ferrite, that is, electrons in the
ferrite driven in the z direction are caused to precess and generate a
field in the perpendicular plane. We shall work with the $E_z$ and $H_z$
fields and the transverse fields can then be found from these equations.
The two differential equations which $E_z$ and $H_z$ must satisfy are
obtained from Maxwell's equations.

$$\omega\epsilon \left[ \frac{j\gamma X}{k_{tx}^2 k_{ty}^2} \frac{\partial^2}{\partial x \partial y} + \frac{K}{k_{ty}^2} \frac{\partial}{\partial x} \right] E_z + \left[ \frac{1}{k_{tx}^2} \frac{\partial^2}{\partial x^2} + \frac{\mu}{k_{ty}^2} \frac{\partial^2}{\partial y^2} + \frac{k^2 K^2 \gamma^2}{k_{tx}^2 k_{ty}^4} \right] H_z = 0$$
$$\left[ \frac{1}{k_{tx}^2} \frac{\partial^2}{\partial x^2} + \frac{1}{k_{ty}^2} \frac{\partial^2}{\partial y^2} + 1 \right] E_z + \omega\mu_0 \left[ \frac{j\gamma X}{k_{tx}^2 k_{ty}^2} \frac{\partial^2}{\partial x \partial y} - \frac{K}{k_{tx}^2} \frac{\partial}{\partial x} \right] H_z = 0$$

where $X=\mu-1$.

There are three interesting cases here. For zero applied field, the
first term in the first equation and second term in the second equation,
are zero since $X$ and $K$ are zero. The remaining expressions reduce to
the usual forms for the classical TE and TM modes. Secondly if there is
no variation of the fields in the x direction, then the TE$_{n0}$ modes
found by Van Trier having a distorted transverse dependence and a
magnetically controllable propagation constant result. The third case is
the general one, of all the other higher order modes.

The fact that the tensor properties are limited to the y-z plane
suggests the form of the solutions shown in (9).
$$E_z = f(y) \sin \frac{m\pi x}{a} \qquad H_z = g(y) \cos \frac{m\pi x}{a}\tag{9}$$

Hence the x dependence of the fields remains unaltered by the ferrite.
Substituting this form of fields into the differential equations, the x
dependence drops out and we are left with two second order linear
differential equations in $f$ and $g$. The determinantal equation for
these two equations is
$$\left[ \frac{\partial^4}{\partial y^4} + B \frac{\partial^2}{\partial y^2} + C \right] \begin{Bmatrix} f \\\\ g \end{Bmatrix} = 0\tag{10}$$
where B and C depend on the propagation constant, frequency, and applied
field. Thus the functions f and g may be represented as a sum of four
independent trigonometric or exponential functions. We will choose
solutions consisting of products of two trigonometric functions each
having a different argument, $ry$ and $qy$.
$$\begin{Bmatrix} \sin \\\\ \cos \end{Bmatrix} ry \begin{Bmatrix} \sin \\\\ \cos \end{Bmatrix} qy.$$

This particular form is suggested by the requirement that the fields
reduce to the usual TE and TM modes for the case of zero applied field.
Hence we would expect that $r$ would go to $n\pi/b$ and $q$ to zero for
zero applied field. As an example, a plot for small values of $q$ of
$\sin ry \cos qy$ is shown in Fig. 2. It is seen that fields described by
this function are distorted towards one side of the waveguide
as the magnetic field is applied.
**[FIGURE: Distortion of transverse fields described by $\sin ry \cos qy$ for small $q$.]**

As in the case of the TE~n0~ modes
this may result in a Poynting vector which on one side of the guide is
opposite to the direction of propagation. This may be thought of as a
uniform Poynting vector with a superimposed circulating energy.

Substituting any of these four solutions in (10) yields two relations
which must be satisfied by the unknowns $r$ and $q$.

$$\gamma^2 = -k_{t}^2\left[ \frac{1}{2}\left(1+\frac{\mu}{\mu_e}\right) \right] + \left[ \left(\frac{m\pi}{a}\right)^2 \frac{1}{2\mu} \right] + r^2+q^2\tag{11}$$
$$r^2 q^2 = \frac{k_t^4(\mu_e-1)^2}{16} - \frac{(\frac{m\pi}{a})^2 k_t^2}{2} \left[1 - \frac{1}{4\mu_e}(1+\mu)(1+\mu_e) \right]
\times \left( \frac{X\mu}{4\mu} \right)^2 = k_t^2\tag{12}$$
and
$$\mu_e = \frac{\mu^2-K^2}{\mu}$$

For zero applied field the propagation
constant shown in (11) goes to the usual form since the $\mu$ and
$\mu_e$ become unity, $r$ goes to ($n\pi/b$) and $q$ vanishes, as we
postulated when choosing the form of the solutions. A further relation
between $r$ and $q$, (12), states that their product squared is a
function only of the applied magnetic field and frequency. Hence $q$ is
known as a function of $r$, and only $r$ must be determined in order to
find the propagation constant.

The $E_z$ and $H_z$ fields are shown in (13) and (14):
$$\begin{split}
E_z = R[S \sin ry \sin qy + T \cos ry \sin qy \\\\ + \sin ry \cos qy] \sin \frac{m\pi x}{a}
\end{split}\tag{13}$$
$$\begin{split}
H_z = L[M \sin ry \cos qy + N \cos ry \sin qy \\\\ + P \sin ry \sin qy + \cos ry \cos qy] \cos \frac{m\pi x}{a}
\end{split}\tag{14}$$

The boundary condition on the $E_z$ field at $y=0$
required the cos cos term to be identically zero. At $y=b$ the boundary
conditions require the quantity in the bracket in (13) to be zero.

The $H_z$ field in (14) must satisfy the boundary condition specified by
$$\left( \frac{\partial H_z}{\partial y} + \frac{j\gamma K H_x}{\mu} \right)_{y=0,b} = 0.\tag{15}$$

This magnetic boundary condition is most easily found by requiring that
$E_x$ be zero at the walls. Note that this boundary condition is
different from the usual in that an extra term is present. Substituting
(14) into (15) yields two equations which along with the one equation
from the $E_z$ fields gives 3 equations in 6 unknown amplitudes and the
quantity $r$. We hence need 4 more relations which are found by
substituting the $E_z$ and $H_z$ fields into one of the original
longitudinal differential equations. This can be manipulated into a set
of 4 nonlinear algebraic equations in four unknowns.

$$\begin{aligned}
G-J \tan rb \cot qb &= \frac{G \tan qb - \phi(-1, P, -M)}{J \tan qb - \phi(P, -1, -V)} \\\\
\begin{split}
(-r+Pq+M\frac{j\gamma K}{rb}) \sin rb \cos qb \\\\
+(Pr-q+N\frac{j\gamma K}{rb}) \cos rb \sin qb \\\\
+(-Nr-Mq+P\frac{j\gamma K}{rb}) \sin rb \sin qb = 0
\end{split} \\\\
\phi(N, M, P) &= GK \\\\
\mu(Mr+Nq) &= -j\gamma K
\end{aligned}$$

where

$$\begin{aligned}
G &= k_{tx}^2 \left( k_{ty}^2 - \frac{B}{2} \right) - \left( \frac{m\pi}{a} \right)^2 k_{tx}^2 \\\\
J &= -2F k_{tx}^2 k_{ty}^2 \\\\
\phi(u, v, w) &= 2F\mu[j\gamma X(ur+vq) + K k_{tx}^2 w].
\end{aligned}$$

The unknowns here are the three magnetic field
amplitudes and $r$. The electric amplitudes are known in terms of these
parameters. The theory leading to these equations has been rigorous and
they are now ready for solution by numerical methods or by approximation
techniques.

It can be shown that there are no pure TE or pure TM modes allowed in
the magnetized case. A similar result was found by Gamo and Kales in
their treatment of the longitudinally magnetized cylindrical waveguide.
This is physically reasonable since the transverse magnetic fields for
the TM modes now generate longitudinal fields through the rotational
nature of the ferrite and thus TM modes would not be expected. Maxwell's
equations permit TE modes only for modes with zero x dependence and
these are Van Trier's TE~n0~ modes.

In conclusion we have derived a set of four nonlinear equations whose
solution determines a rigorous solution to the problem of propagation in
a transversely magnetized ferrite-filled waveguide. The fields can be
expressed in the form of products of two trigonometric functions with
arguments which are asymptotic to $n\pi y/b$ and 0 in the limit of zero
applied field. The product of these arguments is dependent only on the
magnetic field and frequency.

[^4]: H. Gamo, \"The Faraday rotation of waves in a circular
    waveguide,\" *J. Phys. Soc. Jap.*, vol. 8, p. 176; March, 1953.
[^5]: M. L. Kales, \"Modes in waveguides containing ferrites,\" *J.
    Appl. Phys.* vol, 24, p. 609, May, 1953.

[^6]: A. A. Van Trier, Th. M., paper presented orally at meeting of
    Amer. Phys. Soc., Washington, D.C.; April, 1952.

[^7]: A. L. Mikaelyan, \"Electromagnetic waves in a rectangular
    waveguide filled with a magnetized ferrite,\" *Doklady, A.N. USSR*,
    vol. 98, p. 941; October, 1954.

[^8]: A. Chevalier, T. Kahan, and E. Polacco, \"Propagation des ondes
    electromagnetiques dans un milieu gyromagnetique anisotrope, contenu
    dans un guide rectangulaire,\" *Compt. Rend. (Paris)*, vol. 240, pp.
    1323--1324; March, 1955.

[^9]: C. L. Hogan, \"The ferromagnetic Faraday effect at microwave
    frequencies and its applications,\" *Bell Sys. Tech. J.* vol. 31,
    pp. 1--31; January, 1952.
