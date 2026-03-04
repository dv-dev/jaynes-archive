---
title: "Matrix Treatment of Nuclear Induction"
year: 1955
abstract: >
  This paper provides an exposition of matrix methods for solving the Bloch
  equations, particularly for radio frequency signals with constant frequency
  and stepwise constant amplitude. Part I, by E.T. Jaynes, focuses on the basic
  mathematical formalism, showing how transients and steady-state solutions can
  be represented through matrix operations and geometrical interpretations like
  the λ-cone. Part II, by Arnold Bloom, applies these matrix techniques to the
  theory of spin echoes, rederiving and extending Hahn's results to complex
  multi-pulse sequences and amplitude-modulated fields.
author: ["E.T. Jaynes", "Arnold Bloom"]
categories: ["Electrodynamics & Signal Processing"]
tags: ["Bloch equations", "nuclear induction", "matrix theory", "spin echoes", "r-f pulses", "transients", "relaxation time"]
---

## SECTION I: BASIC CONSIDERATIONS

### I. Introduction

The following is an exposition of a method of finding solutions of the Bloch[^1] equations for the case that the applied signal has a constant frequency and a stepwise constant amplitude. It has the advantage that formal solutions are carried out in matrix notation, where one can keep equations in reasonably neat form. Details are worked out only at the end of a calculation. Although it is probably true that no solutions can be found by matrix methods that could not have been found without them, the saving of labor due to the condensed notation makes a wider range of calculations feasible. In addition, the matrices have geometrical meanings that can be followed intuitively, so that one does not lose sight of the physical meaning of terms in the equations. In the analysis to follow we have in mind principally the elucidation of echo phenomena[^2] resulting from applied pulses.

The Bloch equations will be taken in the form

$$ \dot{M} + \frac{M - \chi H}{T} = \gamma(M \times H) \quad (1) $$

in which we have assumed $T_1 = T_2$. Choose a coordinate system rotating about $H_o$ with velocity $\omega$ ( = frequency of applied radio frequency). Then the time derivative of any vector A in the laboratory system is

$$ \frac{dA}{dt} = \frac{\partial A}{\partial t} + \omega \times A \quad (2) $$

where the partial derivative is the rate of change as seen in the rotating system. In the rotating system the equation of motion is therefore

$$ \frac{\partial M}{\partial t} + \frac{M - \chi H_o}{T} = M \times (\gamma H_o + \omega) + \gamma (M \times H_1) \quad (3) $$

where $H_1$ is a vector at right angles to $H_o$, which is constant during a pulse, zero between pulses. In other words, $H_1$ is the component of the applied field rotating with the coordinate system. The component rotating in the other direction is neglected.

### II. Steady-state Solution

For the steady state we have $\frac{\partial M}{\partial t} = 0$, and (3) is a linear algebraic equation for M. If we write out the components it is readily solved by determinants, and the result summarized by the following lemma. The solution of $M + (B \times M) = A$, can be written in the two forms:

$$ M = \frac{A + B(B \cdot A) + A \times B}{1 + B^2} \quad (4) $$

$$ = \frac{(A \times B) + (A \times B) \times B}{1 + B^2} + A $$

In our case,

$$ A = \chi H_o \quad (5) $$

$$ B = T(\gamma H + \omega) $$

so that the steady-state polarization is

$$ M = \chi H_o + \chi T \gamma \frac{(H_o \times H_1) + T H_1 H_o (\gamma H_o - \omega) - \gamma T H_o H_1^2}{1 + T^2 \left[ (\gamma H_o - \omega)^2 + \gamma^2 H_1^2 \right]} \quad (6) $$

which contains the usual expressions for the u- and v-modes.

### III. General Formalism for Transient Solutions

The equation of motion has the form

$$ \left. \begin{aligned} \frac{\partial M}{\partial t} + \frac{M}{T} + B \times M = A, \text{ with} \\ \end{aligned} \quad \right\} \quad \begin{aligned} A = \frac{\chi H_o}{T} \\ \\ B = \gamma H + \omega \end{aligned} \quad (7) $$

which is a system of three coupled linear equations with constant coefficients if the amplitude of the signal is unchanging. If M were a simple scalar this would be easily soluble, and in fact would be so even if the "driving-force" A were an arbitrary function of time. If all quantities are scalars and $\beta$ = constant, the equation

$$ \frac{\partial M}{\partial t} + \beta M = A \quad (8) $$

has the solution

$$ M(t) = e^{-\beta t} M(0) + \int_0^t e^{-\beta(t-t')} A(t') dt' \quad (9) $$

However, if we interpret M and A as vectors and $\beta$ as a matrix, (8) and (7) actually are identical, if we take $\beta$ to be the matrix

$$ \begin{pmatrix} \frac{1}{T} & -B_z & B_y \\ B_z & \frac{1}{T} & -B_x \\ -B_y & B_x & \frac{1}{T} \end{pmatrix} \quad (10) $$

Thus we are led to conjecture that (9) may be the correct solution of the matrix equation, provided the exponential of the matrix is interpreted as the corresponding power series, and a short calculation shows that this is actually the case. Therefore, we can give a rigorous solution of (7) in closed form for the case B = const., provided we can evaluate the matrix $\exp(-\beta t)$. [The restriction B = constant can be removed if the values of $\beta$ at different times commute, leading to the need for evaluating $\exp(-\int \beta dt)$].

This evaluation, although possible, is hard to do for the particular matrix (10), because its characteristic equation does not have any vanishing terms. Fortunately, a change of variables in the original differential equation leads to a simpler matrix. Suppose we take as the dependent variable the vector

$$ V = M e^{t/T} \quad (11) $$

Substitution into (7) leads to the differential equation

$$ \frac{\partial V}{\partial t} + B \times V = A e^{t/T} \quad (12) $$

and we have eliminated the term in $(1/T)$ at the expense of introducing a time dependence in the right-hand side. Equation (12) has the form of (8), in which the matrix $\beta$ reduces to

$$ \beta = \begin{pmatrix} 0 & -B_z & B_y \\ B_z & 0 & -B_x \\ -B_y & B_x & 0 \end{pmatrix} \quad (13) $$

instead of (10). It is now easy to evaluate $\exp(-\beta t)$ by making use of the Cayley-Hamilton theorem according to which every matrix satisfies its own characteristic equation. This is

$$ \det(\beta_{mn} - \lambda \delta_{mn}) = \sum_{k=0}^N C_k \lambda^k = 0 $$

and in our case it reduces to

$$ \lambda^3 + b^2 \lambda = 0 $$

where $b^2 = B_x^2 + B_y^2 + B_z^2$. Thus, our matrix satisfies the relation

$$ \beta^3 = (ib)^2 \beta \quad (14) $$

whence, by induction

$$ \beta^4 = (ib)^2 \beta^2 $$
$$ \beta^5 = (ib)^2 \beta^3 = (ib)^4 \beta, \text{ etc.} \quad (15) $$

Therefore the power series

$$ e^{-\beta t} = 1 - \beta t + \frac{\beta^2 t^2}{2!} - \frac{\beta^3 t^3}{3!} + \dots \quad (16) $$

can be reduced, by repeated application of (14), to a linear combination of $\beta$, $\beta^2$, and the unit matrix. Substituting (15) into (16), we have

$$ e^{-\beta t} = 1 - \frac{\sin bt}{b} \beta + \frac{1 - \cos bt}{b^2} \beta^2 \quad (17) $$

in which the power series for sin and cos have been recognized. As a check, the relation $\frac{d}{dt} (e^{-\beta t}) = - \beta e^{-\beta t}$ is easily verified. The formal problem of evaluating $\exp(-\beta t)$ may be regarded as solved by (17). However, in order to understand our later solutions physically it is necessary to examine the geometrical meaning of the various matrices. Comparing (12) and (13), it is seen that multiplying a vector by $\beta$ is equivalent to taking the cross-product with the vector B. Symbolically, $\beta = B \times$. Therefore, as $\epsilon \to 0$, the matrix $(1 - \epsilon \beta)$ represents an infinitesimal rotation about the vector B, through an angle $\epsilon |B| = \epsilon b$, and the exponential, which is the limit of an infinite number of repeated infinitesimal rotations:

$$ e^{-\beta t} = \lim_{\epsilon \to 0} (1 - \epsilon \beta)^{t/\epsilon} $$

represents a rotation about B through a finite angle $bt = (\Delta \omega^2 + \omega_1^2)^{1/2}t$, where $\Delta \omega = \gamma H_o - \omega$. To see this matrix explicitly, we may write out (17), with the result

$$ e^{-\beta t} = \frac{1}{b^2} \begin{pmatrix} (\omega_1^2 + \Delta \omega^2 \cos bt) & b \Delta \omega \sin bt & \omega_1 \Delta \omega (1 - \cos bt) \\ -b \Delta \omega \sin bt & b^2 \cos bt & b \omega_1 \sin bt \\ \omega_1 \Delta \omega (1 - \cos bt) & -b \omega_1 \sin bt & (\Delta \omega^2 + \omega_1^2 \cos bt) \end{pmatrix} \quad (18) $$

It is readily verified that this is an orthogonal matrix with determinant +1, and so represents a rigid rotation. Now, from (9), (12), (13) we can write down the solution

$$ V(t) = e^{-\beta t} V(0) + \int_0^t e^{-\beta(t-t')} A e^{t'/T} dt' $$

or, returning to the polarization as our variable,

$$ \vec{M}(t) = e^{-(\frac{1}{T} + \beta)t} \vec{M}(0) + \int_0^t e^{-(\frac{1}{T} + \beta)(t-t')} \vec{A} dt' \quad (19) $$

But since the vector $\vec{A}$ is a constant, it may as well be taken outside the integral sign (but to the right because there is a matrix to its left), giving the very simple formal solution

$$ \vec{M}(t) = \lambda(t) \vec{M}(0) + \mu(t) \vec{A} \quad (20) $$

where we have defined two new matrices,

$$ \lambda(t) = e^{-(\frac{1}{T} + \beta)t} \quad (21) $$

$$ \mu(t) = \int_0^t \lambda(t-t') dt' = \int_0^t \lambda(t') dt' $$

$\lambda$ is the product of the rotation matrix (18) already discussed and an exponential damping factor $\exp(-t/T)$. Therefore $\lambda(t)$ operating on any fixed vector results in a vector that rotates about $\vec{B}$ with angular velocity $b = [(\gamma H_o - \omega)^2 + \omega_1^2]^{1/2}$, at the same time shrinking in magnitude so that its tip describes a spiral on a cone, as illustrated in Figure 1. This will be called the $\lambda$-cone.

[**FIGURE 1**]
FIGURE 1
The $\lambda$-cone.
Locus of the tip of the vector $\lambda(t)A$ as t varies from 0 to $\infty$

Formal evaluation of $\mu(t)$ by substituting (17) into (21) and performing the time integration is tedious. For the time being we can avoid this by exhibiting $\mu(t)$ as a function of $\lambda(t)$. This is possible because of the fact that the usual formula for integration of the exponential function applies to matrices as well as scalars, so that we have

$$ \mu(t) = \int_0^t e^{-(\frac{1}{T} + \beta)t'} dt' = (\frac{1}{T} + \beta)^{-1} \left[ 1 - e^{-(\frac{1}{T} + \beta)t} \right] \quad (22) $$

$$ = (\frac{1}{T} + \beta)^{-1} [1 - \lambda(t)] = [1 - \lambda(t)] (\frac{1}{T} + \beta)^{-1} $$

In the last step we have noted that since $\lambda(t)$ and $(\frac{1}{T} + \beta)^{-1}$ are both functions of the same matrix $(\frac{1}{T} + \beta)$, they must commute with each other.

### IV. Response to a Steady Signal Applied at Time Zero

Substituting the last form of (22) into (20), we have the solution in a very convenient form:

$$ M(t) = \lambda(t) \left[ M(0) - (\frac{1}{T} + \beta)^{-1} A \right] + (\frac{1}{T} + \beta)^{-1} A \quad (23) $$

This represents the response occurring when the signal is turned on at time t = 0, and left on for all time. The first term represents a transient that dies out along the $\lambda$-cone leaving the steady-state value

$$ M(\infty) = (\frac{1}{T} + \beta)^{-1} A \quad (24) $$

As a check on the calculation thus far, we note that (24) should agree with the steady-state solution already found directly in Equation (6). To verify this we need to evaluate the inverse of the matrix $(\frac{1}{T} + \beta)$. Since it is only a 3 x 3 matrix, this is not too difficult to do by determinants; The result is

$$ (\frac{1}{T} + \beta)^{-1} = \frac{T^3}{1+b^2T^2} \begin{pmatrix} \left( \frac{1}{T^2} + B_x^2 \right) & \left( \frac{B_z}{T} + B_x B_y \right) & \left( B_x B_z - \frac{B_y}{T} \right) \\ \left( B_x B_y - \frac{B_z}{T} \right) & \left( \frac{1}{T^2} + B_y^2 \right) & \left( B_y B_z + \frac{B_x}{T} \right) \\ \left( B_x B_z + \frac{B_y}{T} \right) & \left( B_y B_z - \frac{B_x}{T} \right) & \left( \frac{1}{T^2} + B_z^2 \right) \end{pmatrix} \quad (25) $$

From (7) we find that A is

$$ A = \frac{\chi H_o}{T} \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix} \quad (26) $$

and we note that the coordinate system is so chosen that the applied magnetic field $H_1$ lies on the x-axis, making $B_y = 0$. Combining these results, the steady-state solution (24) reduces to

$$ M(\infty) = \frac{\chi H_o T^2}{1+b^2 T^2} \begin{pmatrix} B_x B_z - \frac{B_y}{T} \\ \frac{B_x}{T} \\ \frac{1}{T^2} + B_z^2 \end{pmatrix} \quad (27) $$

or, returning to the usual notation,

$$ M_x(\infty) = \chi H_o \frac{\gamma H_1 (\gamma H_o - \omega) T^2}{1 + T^2 \left[ (\gamma H_o - \omega)^2 + \gamma^2 H_1^2 \right]} $$

$$ M_y(\infty) = \chi H_o \frac{\gamma H_1 T}{1 + T^2 \left[ (\gamma H_o - \omega)^2 + \gamma^2 H_1^2 \right]} \quad (28) $$

$$ M_z(\infty) = \chi H_o \frac{1 + (\gamma H_o - \omega)^2 T^2}{1 + T^2 \left[ (\gamma H_o - \omega)^2 + \gamma^2 H_1^2 \right]} $$

This agrees with Equation (6) and with Equation (57) of Reference 1 for the case $T_1 = T_2$. $M_x(\infty)$ and $M_y(\infty)$ are respectively the u, or dispersion mode, and the v, or absorption mode.

The initial value of the transient term in (23) is just the departure of the initial polarization from the steady-state value, and since $\lambda(t)$ is a sort of matrix analogue of an exponential damping factor, the general form of the solution is unexpectedly simple; in matrix notation it is exactly like the formula for exponential build-up of voltage in a simple RC circuit.

We now work out the explicit expression for the transient term $\lambda(t) [M(0) - M(\infty)]$. This can be done algebraically using the expression (17) for $\lambda(t)$; or it may be reasoned out geometrically from the picture of the $\lambda$-cone in Figure 1. Putting $[M(0) - M(\infty)] = M'$ for brevity, the result in vector notation, is

$$ \lambda(t)M' = e^{-t/T} \left\{ \frac{B(B \cdot M')}{b^2} + \left[ M' - \frac{B(B \cdot M')}{b^2} \right] \cos bt + \frac{M' \times B}{b} \sin bt \right\} \quad (29) $$

The computation of (29) is especially simple in the case where we take the initial polarization as the quiescent state of equilibrium under the action of the steady polarizing field $H_o$:

$$ M(0) = \chi H_o, \quad (30) $$

for in this case the scalar product $(B \cdot M')$ vanishes, and the $\lambda$-cone reduces to a disc at right angles to B. (In general we have $B \cdot M(\infty) = \chi H_o \Delta \omega$.) The transient term then reduces to

$$ \lambda(t) M' = e^{-t/T} \left\{ M' \cos bt + \frac{M' \times B}{b} \sin bt \right\} \quad (31) $$

Intermediate results needed in evaluation of (31) are

$$ M' = \frac{\chi H_o \omega_1 T}{1+b^2T^2} \begin{pmatrix} - \Delta \omega T \\ -1 \\ \omega_1 T \end{pmatrix} \quad (32) $$

$$ M' \times B = \frac{\chi H_o \omega_1 T}{1+b^2T^2} \begin{pmatrix} - \Delta \omega \\ b^2 T \\ \omega_1 \end{pmatrix} \quad (33) $$

$$ \sin bt \pm bT \cos bt = (1 + b^2 T^2)^{1/2} \sin(bt \pm \theta) \quad (34) $$

$$ \cos bt \mp bT \sin bt = (1 + b^2 T^2)^{1/2} \cos(bt \mp \theta) $$

where $\tan \theta = bT$. Combining these, we have for the transient

$$ \lambda(t) M' = \frac{\chi H_o \omega_1 T e^{-t/T}}{b(1+b^2T^2)^{1/2}} \begin{pmatrix} - \Delta \omega \sin(bt + \theta) \\ -b \cos(bt + \theta) \\ \omega_1 \sin(bt + \theta) \end{pmatrix} \quad (35) $$

This expression is valid in the rotating coordinate system; in the laboratory system the $\lambda$-cone is rotating about the z-axis with angular velocity $\omega$, and so we have the further transformation to carry out:

$$ (\lambda M')_{\text{lab}} = \Omega(t) (\lambda M')_{\text{rotating}} \quad (36) $$

where $\Omega(t)$ is the matrix

$$ \Omega(t) = \begin{pmatrix} \cos \omega t & + \sin \omega t & 0 \\ - \sin \omega t & \cos \omega t & 0 \\ 0 & 0 & 1 \end{pmatrix} \quad (37) $$

which represents a rotation about the z-axis through an angle $\omega t$. Thus, the transient in the laboratory system is

$$ (\lambda M')_{\text{lab}} = \frac{\chi H_o \omega_1 T e^{-t/T}}{b(1+b^2T^2)^{1/2}} \begin{pmatrix} - \Delta \omega \sin(bt + \theta) \cos \omega t - b \cos(bt + \theta) \sin \omega t \\ \Delta \omega \sin(bt + \theta) \sin \omega t - b \cos(bt + \theta) \cos \omega t \\ \omega_1 \sin(bt + \theta) \end{pmatrix} \quad (38) $$

Remembering that $\omega \gg b$, we see that the output signal, proportional to the y-component of (38) can be described as a signal of frequency $\omega$ whose amplitude varies at the nutation frequency b, the ripples also dying out according to $\exp(-t/T)$. To get our final expression for the signal amplitude as a function of time, we must convert the expression (28) for $M(\infty)$ to the laboratory system with the $\Omega$ matrix and then add the y-components of (38) and the resulting vector. The steady-state solution in the laboratory system is

$$ [M(\infty)]_{\text{lab}} = \Omega(t) [M(\infty)]_{\text{rot}} = \frac{\chi H_o}{1+b^2 T^2} \begin{pmatrix} \omega_1 \Delta \omega T^2 \cos \omega t + \omega_1 T \sin \omega t \\ - \omega_1 \Delta \omega T^2 \sin \omega t + \omega_1 T \cos \omega t \\ (1 + \Delta \omega^2 T^2) \end{pmatrix} \quad (39) $$

Adding the y-components of (38) and (39) we find that the output signal is

$$ [M_y(t)]_{\text{lab}} = \frac{\chi H_o \omega_1 T}{1+b^2 T^2} \left[ \cos \omega t - \Delta \omega T \sin \omega t \right] \quad (40) $$

$$ + \frac{\chi H_o \omega_1 T}{b(1+b^2T^2)^{1/2}} e^{-t/T} \left[ \Delta \omega \sin(bt + \theta) \sin \omega t - b \cos(bt + \theta) \cos \omega t \right] $$

In the case of resonance ($\Delta \omega = 0$) and powerful driving field ($\omega_1 T \gg 1$) this reduces to

$$ M_y = \chi H_o \left[ \frac{1}{\omega_1 T} - e^{-t/T} \cos(\omega_1 t + \theta) \right] \cos \omega t \quad (41) $$

In this case, although the final amplitude is small, the time required for saturation to develop is many relaxation periods.

### V. General Formalism for Coherent Pulses

With the Solution (20) we can construct the response to a train of pulses as follows (see Figure 2). Initially, the polarization has some arbitrary value M(0). Then a pulse is turned on for a time $t_1$. At the end of the pulse, the polarization is given as $M(t_1)$ by (20). For the next period $t_2$ between pulses, this value of M is used as the initial condition, and the Solution (20) gives $M(t_1 + t_2) = M(\tau)$, the polarization just at the beginning of the second pulse. This value of initial polarization is then used as the initial condition for the third period, giving the value of $M(t_1 + \tau)$ just at the end of the second pulse. This can be carried on indefinitely, and one sees that by repeated application of (20) we can get the response to any signal whose frequency is constant and whose amplitude varies as a step-function.

[**FIGURE 2: Train of Coherent Pulses**]

FIGURE 2
Train of Coherent Pulses

Clearly, however, if this process were carried out in such a direct manner, the amount of labor involved would be enormous, and the results so complicated that one could not understand them. In order to get the answer at all, a more elegant method is needed. First let us work out from (20) the relation between polarization at times separated by one repetition period of the pulses. This will provide a difference equation which we might hope to solve.

Let $M_n = M(n \tau)$ be the polarization at the start of the n'th pulse, and $M_n' = M(n \tau + t_1)$ the polarization at the end of the n'th pulse. We wish to eliminate $M_n'$, and find $M_{n+1}$ directly in terms of $M_n$. The subscript 1 denotes a function used during a pulse; 2 denotes the period between pulses. The matrices $\lambda$ and $\mu$ have different forms during and between pulses, because b and B have different values depending on whether the signal is on or off. Thus, (20) leads to

$$ M_n' = \lambda_1(t_1) M_n + \mu_1(t_1) A \quad (42) $$

$$ M_{n+1} = \lambda_2(t_2) M_n' + \mu_2(t_2) A $$

and eliminating $M_n'$, we have

$$ M_{n+1} = \lambda_2 \lambda_1 M_n + (\lambda_2 \mu_1 + \mu_2) A \quad (43) $$

$$ = \alpha M_n + Q $$

The important thing is that the matrix

$$ \alpha = \lambda_2 \lambda_1 = e^{-\beta_2 t_2} e^{-\beta_1 t_1} e^{-\frac{(t_1+t_2)}{T}} \quad (44) $$

and the vector

$$ Q = (\lambda_2 \mu_1 + \mu_2) A \quad (45) $$

are both independent of M, so we have a very simple linear difference equation. The solution can be written down immediately:

$$ M_n = \alpha^n \left[ M_o - \frac{1}{1 - \alpha} Q \right] + \frac{1}{1 - \alpha} Q \quad (46) $$

where the first pulse is called the zero'th, and we see that the steady-state condition, reached after a large number of pulses, is just

$$ M_\infty = \frac{1}{1 - \alpha} Q \quad (47) $$

for the polarization just at the beginning of a pulse. (Since all the eigenvalues of $\alpha$ are less than unity, we have $\lim_{n \to \infty} \alpha^n = 0$). Equation (46) gives one a good over-all picture of the situation. The quantity in brackets is the departure of the initial polarization from its steady-state value, and each succeeding pulse reduces this "error" by the same factor $\alpha$.

The Solution (46) may be interpreted geometrically in a manner analogous to the picutre of the $\lambda$-cone in Figure 1. According to Equation (44) the matrix $\alpha$ is the product of an exponential damping factor and the two rotation matrices $\exp(-\beta_2 t_2)$ and $\exp(-\beta_1 t_1)$. Now since all rigid rotations form a group, the product of any two rotations about different axes is equivalent to some rotation about a third axis. Therefore the matrix $\alpha$ is itself a $\lambda$-matrix; that is, it represents a rigid rotation with accompanying exponential decrease of length, and thus any power of $\alpha$ converts a given vector into one lying on the surface of a cone, as in Figure 3. The operator $\alpha^n$ converts the vector A into one whose tip is at the point indicated. This is a discrete version of a $\lambda$-cone.

[**FIGURE 3: The $\alpha$-cone**]
FIGURE 3. The $\alpha$-cone

We note that any transient in the presence of coherent pulses has the following property. If we look at the polarization only at the same instant in each repetition period, we see the difference between present value and final value decaying to zero by discrete jumps along the $\alpha$-cone. At other times during the repetition period the polarization does not lie on the spiral curve connecting the points in Figure 3, but it describes a more complicated path from one point to the next.

Finally, we give the formal solution for polarization at any time during the repetition period. Using (20) we find,

During a pulse:

$$ M(n \tau + t) = \lambda_1(t) M_n + \mu_1(t) A, \quad (0 \leq t \leq t_1) \quad (48) $$

Between pulses:

$$ M(n \tau + t_1 + t) = \lambda_2(t) \lambda_1(t_1) M_n \quad (49) $$

$$ + \left[ \lambda_2(t) \mu_1(t_1) + \mu_2(t) \right] A, \quad (0 \leq t \leq t_2) $$

If the train of pulses is stopped after the n'th, then the subsequent behavior is given by (49) in which t is not bounded.

### VI. Steady State Under Action of Coherent Pulses

In this section we evaluate the steady-state polarization (47) which exists at the beginning of each pulse after a large number have been applied. In order to express the vector Q of (45) in terms of known quantities we use the relation

$$ \mu(t) = \left[ 1 - \lambda(t) \right] (\frac{1}{T} + \beta)^{-1} $$

previously found in Equation (22). Thus

$$ Q = (\lambda_2 \mu_1 + \mu_2) A $$

$$ = \left[ \lambda_2 (1 - \lambda_1) (\frac{1}{T} + \beta_1)^{-1} + (1 - \lambda_2) (\frac{1}{T} + \beta_2)^{-1} \right] A \quad (50) $$

$$ = \lambda_2 (1 - \lambda_1) M_1(\infty) + (1 - \lambda_2) M_2(\infty) $$

Here we have recognized the vectors

$$ M_1(\infty) = (\frac{1}{T} + \beta_1)^{-1} A \quad (51) $$

$$ M_2(\infty) = (\frac{1}{T} + \beta_2)^{-1} A = \chi H_o $$

as the steady-state values from (24), which would be reached if the signal were left on and off respectively (the latter being of course just the static polarization produced by the magnet). $M_1(\infty)$ has been given explicitly in Equations (27) and (28). We may now write the pulsed steady-state polarization (47) in the form:

$$ M_\infty = M_1(\infty) + \frac{1}{1 - \alpha} (1 - \lambda_2) \left[ M_2(\infty) - M_1(\infty) \right] \quad (52) $$

Here use has been made of (50) and the identity

$$ \frac{1}{1 - \lambda_2 \lambda_1} \lambda_2(1 - \lambda_1) = 1 - \frac{1}{1 - \lambda_2 \lambda_1} (1 - \lambda_2) $$

With (52) the calculation of $M_\infty$ is reduced to the problem of evaluating the matrix $(1 - \alpha)^{-1} = (1 - \lambda_2 \lambda_1)^{-1}$.

### VII. Spinor Representation of Rotations

Calculating the resultant of several successive rotations using the above (3 x 3) matrices is very tedious, and the results appear in a form too complicated for easy interpretation. For such calculations it is a practical necessity to use the two-dimensional representation of the rotation group, also known as the Cayley-Klein parameters. To every direction of the polarization vector M there corresponds a spinor $\psi$, which is a vector in a two-dimensional complex vector space; and to every rotation of M there corresponds a unitary transformation of this space. We use the usual notation and conventions of the theory of particles of spin 1/2 in quantum mechanics. Thus, denoting the spinor by

$$ \psi = \begin{pmatrix} \psi_+ \\ \psi_- \end{pmatrix} $$

and the Pauli spin matrices

$$ \sigma_x = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \quad \sigma_y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \quad \sigma_z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}, $$

the direction of the spin axis is given by the unit vector n which satisfies

$$ (\vec{n} \cdot \vec{\sigma}) \psi = \psi \quad (53) $$

or

$$ \begin{pmatrix} n_z & n_x - i n_y \\ n_x + i n_y & -n_z \end{pmatrix} \begin{pmatrix} \psi_+ \\ \psi_- \end{pmatrix} = \begin{pmatrix} \psi_+ \\ \psi_- \end{pmatrix} \quad (54) $$

Writing out the first row of (54), we have

$$ \frac{\psi_+}{\psi_-} = \frac{n_x - i n_y}{1 - n_z} = \cot \frac{\theta}{2} e^{-i\phi} \quad (55) $$

where $\theta$ and $\phi$ are the usual colatitude and azimuth angles of spherical coordinates, i.e.,

$$ n_x = \sin \theta \cos \phi $$
$$ n_y = \sin \theta \sin \phi \quad (56) $$
$$ n_z = \cos \theta $$

Thus the direction of the spin axis depends only on the ratio of the components of the spinor. Now the correspondence between $\psi$ and our polarization vector M may be chosen, to a large extent, arbitrarily. In order to make the correspondence with spin 1/2 quantum mechanics as close as possible, we choose M to have the direction of the unit vector n above, and normalize $\psi$ according to

$$ |\psi|^2 \equiv |\psi_+|^2 + |\psi_-|^2 = M \quad (57) $$

(in quantum mechanics this quantity would be interpreted as the probability density for finding the particle with either sign of spin). Now

$$ M_x = M \sin \theta \cos \phi $$
$$ M_y = M \sin \theta \sin \phi \quad (58) $$
$$ M_z = M \cos \theta $$

But, from (55) and (57),

$$ |\psi_+|^2 = |\psi_-|^2 \cot^2 \left( \frac{\theta}{2} \right) = M - |\psi_-|^2 $$

so that we must take

$$ |\psi_-|^2 = M \sin^2 \left( \frac{\theta}{2} \right) \quad (59) $$
$$ |\psi_+|^2 = M \cos^2 \left( \frac{\theta}{2} \right) $$

Some ambiguity in $\psi$ remains; $\psi_+$ and $\psi_-$ may be changed to $\psi_+ e^{i\alpha}$, $\psi_- e^{i\alpha}$, without affecting either (55) or (59), corresponding to the fact that in quantum mechanics the absolute phase of $\psi$ has no physical meaning. We choose the phase angles so that

$$ \psi_+ = M^{1/2} \cos \frac{\theta}{2} e^{-i \frac{\phi}{2}} \quad (60) $$
$$ \psi_- = M^{1/2} \sin \frac{\theta}{2} e^{i \frac{\phi}{2}} $$

and now only one ambiguity in the correspondence between $\psi$ and M remains; the spinors $\psi$ and $-\psi$ both correspond to the same M. This last ambiguity cannot be removed, as we will show presently. It arises fundamentally from the topological properties of the rotation group, and all representations corresponding to half-odd integer spin are double-valued.

Now for any real number $\xi$, consider the matrix $\exp(-i \sigma_z \frac{\xi}{2})$, defined by its power series. Since $\sigma_z^2 = 1$, it is equal to

$$ e^{-i \sigma_z \frac{\xi}{2}} = 1 \cos \left( \frac{\xi}{2} \right) - i \sigma_z \sin \left( \frac{\xi}{2} \right) = \begin{pmatrix} e^{-i \frac{\xi}{2}} & 0 \\ 0 & e^{i \frac{\xi}{2}} \end{pmatrix} \quad (61) $$

Applying this matrix to the spinor (60), we get

$$ e^{-i \sigma_z \frac{\xi}{2}} \psi(\theta, \phi) = \begin{pmatrix} M^{1/2} \cos \frac{\theta}{2} e^{-i \left( \frac{\phi + \xi}{2} \right)} \\ M^{1/2} \sin \frac{\theta}{2} e^{i \left( \frac{\phi + \xi}{2} \right)} \end{pmatrix} = \psi(\theta, \phi + \xi) \quad (62) $$

Therefore, $\exp(-i \sigma_z \xi/2)$ represents a rotation about the z-axis through an angle $\xi$. Similarly, it may be shown that the matrix

$$ e^{-i \sigma_x \frac{\eta}{2}} = 1 \cos \left( \frac{\eta}{2} \right) - i \sigma_x \sin \left( \frac{\eta}{2} \right) = \begin{pmatrix} \cos \frac{\eta}{2} & -i \sin \frac{\eta}{2} \\ -i \sin \frac{\eta}{2} & \cos \frac{\eta}{2} \end{pmatrix} \quad (63) $$

represents a rotation about the x-axis through an angle $\eta$, etc.

In general, the matrix

$$ e^{-i \frac{\theta}{2} (\vec{\sigma} \cdot \vec{n})} = 1 \cos \frac{\theta}{2} - i (\sigma \cdot n) \sin \frac{\theta}{2} \quad (64) $$

represents a rotation through an angle $\theta$ about an axis parallel to the unit vector $\vec{n}$. (We see now why the ambiguity $\psi \to -\psi$ cannot be removed; putting $\xi = 2\pi$ in (62) returns M to its original direction, but it sends $\psi$ into $-\psi$). Now the most general rotation may be specified by three Eulerian angles $\xi, \eta, \zeta$:

$$ e^{-i \sigma_z \frac{\xi}{2}} e^{-i \sigma_x \frac{\eta}{2}} e^{-i \sigma_z \frac{\zeta}{2}} = \begin{pmatrix} \alpha & \beta \\ -\beta^* & \alpha^* \end{pmatrix} \quad (65) $$

where

$$ \alpha = \cos \frac{\eta}{2} e^{-i \left( \frac{\xi + \zeta}{2} \right)} \quad (66) $$
$$ \beta = -i \sin \frac{\eta}{2} e^{-i \frac{\xi - \zeta}{2}} $$

To find the axis and magnitude of the resulting rotation, we need the law of composition of rotations. This is easily derived from (64): The axis and angle (n, $\theta$) of the resultant of the rotation ($n_1, \theta_1$) followed by

($n_2, \theta_2$), are determined by the relation

$$ e^{-i \frac{\theta}{2} (\sigma \cdot n)} = e^{-i \frac{\theta_2}{2} (\sigma \cdot n_2)} e^{-i \frac{\theta_1}{2} (\sigma \cdot n_1)} \quad (67) $$

or

$$ \cos \frac{\theta}{2} - i (\sigma \cdot n) \sin \frac{\theta}{2} = \left[ \cos \frac{\theta_2}{2} - i (\sigma \cdot n_2) \sin \frac{\theta_2}{2} \right] \left[ \cos \frac{\theta_1}{2} - i (\sigma \cdot n_1) \sin \frac{\theta_1}{2} \right] $$

$$ = \cos \frac{\theta_2}{2} \cos \frac{\theta_1}{2} - i \sigma \cdot \left[ n_1 \sin \frac{\theta_1}{2} \cos \frac{\theta_2}{2} + n_2 \sin \frac{\theta_2}{2} \cos \frac{\theta_1}{2} \right] \quad (68) $$

$$ - (n_1 \cdot n_2) \sin \frac{\theta_1}{2} \sin \frac{\theta_2}{2} - i \sigma \cdot (n_2 \times n_1) \sin \frac{\theta_1}{2} \sin \frac{\theta_2}{2} $$

where we have used the identity

$$ (\sigma \cdot n_2) (\sigma \cdot n_1) = n_2 \cdot n_1 + i \sigma \cdot (n_2 \times n_1). \quad (69) $$

Equating real and imaginary parts of (68) then gives the desired composition law. This can be written compactly as follows. Represent a rotation through an angle $\theta$ about an axis determined by the unit vector $\vec{n}$ by a vector $\vec{w} = \vec{n} \tan(\theta/2)$. Then the resultant of the rotation $w_1$ followed by $w_2$ is

$$ w = \frac{w_1 + w_2 + (w_2 \times w_1)}{1 - (w_2 \cdot w_1)} \quad (70) $$

This rule is applied twice to find the resultant of the three successive rotations

$$ w_1 = \tan \frac{\xi}{2} \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}, \quad w_2 = \tan \frac{\eta}{2} \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}, \quad w_3 = \tan \frac{\zeta}{2} \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix} \quad (71) $$

and the final result is

$$ w = \frac{w_1 + w_2 + w_3 + [w_2 \times (w_1 - w_3)] + w_2(w_1 \cdot w_3)}{1 - (w_1 \cdot w_3)} \quad (72) $$

from which the condition for w to have no y-component (i.e., the resultant axis of rotation lies in the x-z plane) is seen to be $w_1 = w_3$, or $\xi = \zeta$. Then the resultant vector (72) reduces to

$$ w = \frac{2 w_1 + w_2 (1 + w_1^2)}{1 - w_1^2} \begin{pmatrix} \sec \xi \tan \frac{\eta}{2} \\ 0 \\ \tan \xi \end{pmatrix} \quad (73) $$

But the rotation during a pulse is given by the vector

$$ w = \begin{pmatrix} \cos \phi \tan \frac{bt}{2} \\ 0 \\ \sin \phi \tan \frac{bt}{2} \end{pmatrix} \quad (74) $$

Comparing (73), (74), we get

$$ \tan \xi = \sin \phi \tan \frac{bt}{2} \quad (75) $$
$$ \sin \frac{\eta}{2} = \cos \phi \sin \frac{bt}{2} $$

and the Cayley-Klein parameters (66) which give the rotation during a pulse are

$$ \alpha = \cos \frac{\eta}{2} e^{-i\xi} = \cos \frac{bt}{2} - i \sin \phi \sin \frac{bt}{2} \quad (76) $$
$$ \beta = -i \sin \frac{\eta}{2} = -i \cos \phi \sin \frac{bt}{2} $$

These relations are the same as Equation (13) of the following section.

## SECTION II: THEORY OF SPIN ECHO

### I. Introduction

Some of the most interesting solutions of Bloch's[^1] equations are those that have to do with spin echoes. Spin echoes were first discovered by Hahn[^2], who in his original paper derived solutions for simple two- and three-pulse echoes using long notation. In this paper, we shall rederive Hahn's original results using matrix methods and we will extend the results to problems considerably more complicated than those handled in Hahn's original derivations. We shall also derive an approximate solution for nuclear induction in an amplitude-modulated r-f field.

Our purpose in carrying out these derivations and studying the solutions is to see how we can use the spin echo analysis to predict all the signals that may be expected out of a nuclear resonance probe in a very inhomogeneous field. If one derives solutions for the net polarization directly from Bloch's equations, it is then necessary to integrate over all values of field $\Delta \omega$ in order to obtain a solution which corresponds to an observable signal. In the spin echo analysis, however, the integration is done implicitly and we merely look for characteristic terms in the solution which predict a signal. Our approach will be to expect that, in general, polarizations corresponding to different values of $\Delta \omega$ will at any instant point in different directions in the xy-plane so that on the average they cancel out and produce no net signal. The exception to this rule which will produce a signal is as follows: if the term corresponding to the polarization in the xy-plane contains a factor of the form $e^{i \Delta \omega (t - t_1)}$, we shall expect a signal, or coherence as we shall sometimes call it, at time $t_1$. We shall find that this type of analysis is capable of predicting not only the times at which signals occur, but can also give considerable information about the amplitudes and shapes of signals.

To begin with, let us assume that the magnetic moments obey Bloch's equations for the case $T_1 = T_2 = T$,

$$ \frac{d\vec{M}}{dt} + \frac{\vec{M}}{T} + \gamma \vec{H} \times \vec{M} = \frac{M_o \vec{z}}{T} \quad (1) $$

where H is the instantaneous vector sum of all magnetic fields acting on the nucleus. It is convenient, although not necessary in the rotation-covariant formalism we are using to transfer to a rotating frame, rotating with the angular velocity of the r-f field. In the rotating frame, Equation (1) can be written as

$$ \frac{d\vec{M}}{dt} + \frac{\vec{M}}{T} + \vec{B} \times \vec{M} = \frac{M_o \vec{z}}{T}, \quad (2) $$

where $B = \gamma H - \omega_o$.

For simplicity we shall refer to B as the effective field, although it is actually written in frequency units. The general solution of Equation (2) for r-f fields of fixed frequency and variable amplitude has been derived by Section I[^3]. The solution during a steady step or pulse of r-f can be described by

$$ \vec{M}(t) = e^{-t/T} e^{-\beta t} \vec{M}_1 + (1 - e^{-t/T} e^{-\beta t}) \vec{M}_2, \quad (3) $$

where $M_1$ is the polarization at the beginning of the pulse or step, $M_2$ is the steady state polarization that would be reached if the r-f were left at its particular value indefinitely, and $e^{-\beta t}$ is the precession matrix. This precession matrix has been discussed in greater detail in I, and it will merely be necessary at this point to describe it as a rotation matrix describing a rotation about B with an angular velocity $b = |B|$. Although a rotation matrix is normally three-dimensional, we shall often find it convenient to describe rotations in terms of operators on two-component spinors. Consider a formalism in which we write

$$ \vec{M} = M_x \sigma_x + M_y \sigma_y + M_z \sigma_z \quad (4) $$

where the $\sigma$ are the Pauli spin operators for particles of spin one-half. In such a notation, the polarization vector M can be written as

$$ \vec{M} = \begin{pmatrix} M_z & M_x - i M_y \\ M_x + i M_y & -M_z \end{pmatrix} \quad (5) $$

For simplicity, we shall hereafter denote M only by its subscripts, thus

$$ \vec{M} = \begin{pmatrix} z & x - iy \\ x + iy & -z \end{pmatrix} = \begin{pmatrix} z & x- \\ x_+ & -z \end{pmatrix}. \quad (6) $$

A rotation of M can be described in terms of a unitary hermitean matrix, Q, such that

$$ \vec{M}' = Q \vec{M} Q^*, \quad (7) $$

where Q* is the hermitean adjoint. In detail the matrix, Q, can be written as

$$ Q = \begin{pmatrix} \alpha & \beta \\ \gamma & \delta \end{pmatrix}, \quad (8) $$

where $\alpha, \beta, \gamma$, and $\delta$ are known as the Cayley-Klein parameters[^4]. If on the other hand, M is written as a simple three-component vector

$$ \vec{M} = \begin{pmatrix} x_+ \\ x_- \\ z \end{pmatrix}, \quad (9) $$

then we can write

$$ \vec{M}' = R \vec{M}, \quad (10) $$

where R is a 3 x 3 matrix. In terms of the Cayley-Klein parameters, we have

$$ R = \begin{pmatrix} \delta^2 & -\gamma^2 & 2 \gamma \delta \\ -\beta^2 & \alpha^2 & -2 \alpha \beta \\ \beta \delta & -\alpha \gamma & (\alpha \delta + \beta \gamma) \end{pmatrix} \quad (11) $$

The set of Q's is isomorphic to the set of R's.

We shall describe the precessional motion in terms of the Cayley-Klein parameters (see Figure 1). We define

$$ \left. \begin{aligned} b = |B| \\ \\ \phi = \tan^{-1} \frac{\gamma H_o - \omega}{\gamma H_1} \end{aligned} \right\} \quad (12) $$

then $Q = e^{-\beta t}$ is described as

$$ \alpha = \cos \frac{bt}{2} - i \sin \phi \sin \frac{bt}{2} $$

$$ \beta = \gamma = -i \cos \phi \sin \frac{bt}{2} \quad (13) $$

$$ \delta = \cos \frac{bt}{2} + i \sin \phi \sin \frac{bt}{2}. $$

For positive $\gamma$ the precession is clockwise when viewed from the front of the vector $\vec{B}$.

### II. Simple Analysis

In order to show in a simple manner how our analysis will work, we shall consider the simplest possible case, that of two pulses followed by an echo. The production of the echo can be understood in four steps, as follows:

1. The thermal equilibrium polarization vector z is transformed by the first pulse into a vector which can be described by x+.

2. After the first pulse, x+ is transformed into x+ $e^{-i \Delta \omega t}$.

3. The effect of the second pulse, in Hahn's experiments where all moments are fairly near resonance, is to rotate the entire moment distribution about the x-axis. In this analysis, we shall accomplish the same thing by transforming x+ (t) into x- (t) thus x+ $e^{i \Delta \omega t}$ transforms into x- $e^{-i \Delta \omega t_1}$, and vice versa.

4. At the end of the second pulse, the new x+ can be written as x- $e^{-i \Delta \omega t_1}$; after a time t this becomes (x- $e^{-i \Delta \omega t_1}$) $e^{i \Delta \omega t}$ which can be written as x- $e^{i \Delta \omega (t - t_1)}$.

We see by this simple means that we can predict the presence of an echo at a time $t_1$ following the second pulse. We can obtain the amplitude of the echo, neglecting relaxation and diffusion effects, directly from the matrix elements of the transformations described in steps 1 through 4. Thus, looking at the R matrix in Equation (11), we see that the matrix element for step 1 is $(2 \gamma \delta)$, for step 2 it is unity since the transformation is already described by the term $e^{i \Delta \omega t}$, for step 3 the matrix element is $-\beta^2$, and for step 4 it is again unity. Thus, the amplitude of the echo is proportional to $-2 \gamma \delta \beta^2$. If both pulses are identical and if we consider the nuclear moments very close to resonance so that $\phi \approx 0$, then

$$ -2 \gamma \delta \beta^2 = \sin bt \sin^2 \frac{bt}{2}. \quad (14) $$

This is identical to the expression for the echo amplitude derived in a relatively laborious way by Hahn. However, our analysis is not only more direct but can also be applied to any arbitrary value of $\Delta \omega$ as well as for two arbitrary unequal pulses having different r-f amplitudes and lengths. A more general equation for this echo amplitude will be given in Equation (22).

### III. General Analysis

#### A. Introduction

In this section we shall calculate the amplitudes and shapes of signals in an idealized situation in which both $T_1$ and $T_2$ (if they are not equal) are very long compared to the times required to do the experiments, and in which self-diffusion effects are absent. For each instant of time we must solve the corresponding Equation (3):

$$ M(t) = e^{-t/T} e^{-\beta t} \vec{M}_1 + (1 - e^{-t/T} e^{-\beta t}) \vec{M}_2. \quad (3) $$

It is customary in treatments of spin echo[^2][^5] to assume an initial polarization $\vec{M} = M_o \vec{z}$ prior to the first pulse, and to solve only for the first term in (3), ignorning the effect of $M_2$. The neglect of this second term during the time between pulses, when it corresponds to a recovery of initial polarization, is justifiable only for long relaxation times; actually the recovery is quite useful for the measurement of $T_1$. Neglect of $(1 - e^{-t/T} e^{-\beta t}) M_2$ during a pulse is not so easily justified. In most spin echo experiments, however, the r-f level, if left on continuously, would correspond to a high degree of saturation; in such cases it can be shown that $\vec{M}_2$ is either very small or is nearly parallel to $\vec{B}$, so that the total effect of the term is small. It is nevertheless clear that there are circumstances under which one cannot neglect $M_2$, even for relatively short pulses and intense radio frequency.

The conditions of our experiment are such that we need to calculate only the term in $\vec{M}_1$. Since we start out with only a z component of polarization and wish to know the component in the xy plane after a given elapsed time, it is sufficient to calculate the corresponding matrix element, $(- 2 \alpha \beta)$ in (11), connecting z and (x - iy). [We could just as well use its complex conjugate, $(2 \gamma \delta)$, connecting z with $(x + iy)$]. It is necessary to multiply together the matrices corresponding to the pulses and the intervals between pulses, but rather than multiply 3 x 3 matrices it is far simpler to multiply the corresponding 2 x 2 Q-matrices and then multiply together the final $\alpha$ and $\beta$. Analysis will then consist of inspection of the product $(- 2 \alpha \beta)$.

When the matrices are displayed it is fairly evident how one may modify them to include the effects of relaxation and self-diffusion. These effects have already been calculated in detail for two- and three-pulse systems[^2][^5], and it does not appear that their applications to more complex systems will produce much that is physically new or interesting. Exceptions to this latter statement will be discussed qualitatively.

#### B. Events Following a Single Pulse

All events occurring during the first pulse will be referred to by subscript 1, those following the pulse by subscript 2 (Figure 2). The Q matrix for the transformations involved is given by

$$ Q = \begin{pmatrix} e^{-i \frac{\Delta \omega t'_2}{2}} & 0 \\ 0 & e^{i \frac{\Delta \omega t'_2}{2}} \end{pmatrix} \begin{pmatrix} \alpha_1 & \beta_1 \\ \gamma_1 & \delta_1 \end{pmatrix} \quad (15) $$

The $\alpha_1, \beta_1, \gamma_1, \delta_1$ are defined in (13). In Equations (15) through (34) the time variable is denoted by a prime; unprimed t's are fixed or elapsed times. As has been pointed out earlier, we are interested in terms of the form $\exp[i \Delta \omega (t' - t_i)]$ in the product of $\alpha$ and $\beta$ of the final matrix Q. The product is

$$ -2 \alpha \beta = -2 \alpha_1 \beta_1 e^{-i \Delta \omega t'_2}, \quad (16) $$

and substituting Equation (13) we have

$$ -2 \alpha \beta = (\sin 2 \phi \sin^2 \frac{b t_1}{2} + i \cos \phi \sin b t_1) e^{-i (\Delta \omega) t'_2} \quad (17) $$

In studying (17), we first observe that the formula predicts a coherence immediately after the end of the pulse, at $t'_2 = 0$. This is usually known as the free decay following the pulse, and has been observed by Torrey, Hahn and others. We shall have more to say about the detailed shape of this free decay later. In addition to the free decay, however, (17) also predicts a small signal at a time following the pulse equal to the length of the pulse, i.e., when $t'_2 = t_1$. To see why this is so, we observe that for very large values of $\Delta \omega$, b is very nearly equal to $\Delta \omega$. If we then substitute $\Delta \omega$ for b in (17), we observe terms of the form $e^{i \Delta \omega (t'_2 - t_1)}$. This coherence, which we shall call an "edge echo" is of relatively small amplitude and is produced only by the nuclear moments that are far from resonance. An experimental example of edge echos is shown in Figure 3.

#### C. Events Following Second Pulse

The Q matrix corresponding to all the transformations up to time interval 4 is

$$ Q = \begin{pmatrix} e^{-4'} & 0 \\ 0 & e^{4'} \end{pmatrix} \begin{pmatrix} \alpha_3 & \beta_3 \\ \gamma_3 & \delta_3 \end{pmatrix} \begin{pmatrix} e^{-2} & 0 \\ 0 & e^2 \end{pmatrix} \begin{pmatrix} \alpha_1 & \beta_1 \\ \gamma_1 & \delta_1 \end{pmatrix} \quad (18) $$

where $e^{-2}$ is short for $e^{-i \frac{\Delta \omega t_2}{2}}$, $e^{4'}$ for $e^{+i \frac{\Delta \omega t'_4}{2}}$, etc. (see Figure 4). The matrix element in R connecting initial state z and final state x- is again given by the produce $-2 \alpha \beta$ of the Q matrix (18). The result is

$$ -2 \alpha \beta = -2 \left( \alpha_1 \alpha_3 e^{-2 -4'} + \beta_3 \gamma_1 e^{+2 -4'} \right) \left( \alpha_3 \beta_1 e^{-2 -4'} + \beta_3 \delta_1 e^{+2 -4'} \right) \quad (19) $$

Of the four terms in (19) one of them refers to times which are negative with respect to the second pulse and which we shall disregard. The other two represent coherences at $t'_4 = 0$ (free decay of the second pulse), and at $t'_4 = t_2$ which is the simple two-pulse echo. Substituting (13) into the coefficient for the free decay we obtain for the free decay amplitude

$$ (-2 \alpha \beta)_{t'_4 = 0} = -(\alpha_1 \delta_1 + \beta_1 \gamma_1) (2 \alpha_3 \beta_3). \quad (20) $$

The amplitude of the echo is given by

$$ (-2 \alpha \beta)_{t'_4 = t_2} = -2 \gamma_1 \delta_1 \beta_3^2, \quad (21) $$

which is identical to the result obtained in subsection II (Simple Analysis). Substituting (13) into (21) we obtain the following expression for the echo amplitude as a function of different pulse widths and spacings, but equal r-f amplitudes:

$$ -2 \gamma_1 \delta_1 \beta_3^2 = \left( \sin 2 \phi \cos^2 \phi \sin^2 \frac{b t_1}{2} \sin^2 \frac{b t_3}{2} \right. $$

$$ \left. - i \cos^3 \phi \sin b t_1 \sin^2 \frac{b t_3}{2} \right) e^{-i \Delta \omega (t'_4 - t_2)} \quad (22) $$

This reduces to Equation (14) for the special case considered there.

In addition to the free decay and the echo following the second pulse, there is an "edge echo" following the second pulse and both preceding and following the echo. These may be deduced by an examination of the corresponding matrix elements. We will not discuss them further.

#### D. Three Pulses with Unequal Spacing*

We will assume initially that $t_4 > t_2$, thus the two-pulse echo has had time to occur before the onset of the third pulse (see Figure 4). Corresponding to this situation, we can write a Q matrix which will be a product of six matrices corresponding to the six time intervals after the third pulse. We shall not be concerned at the moment with the coefficients of these matrix elements but shall look only at the exponents in the matrix elements $\alpha, \beta$. Both $\alpha$ and $\beta$ consist of four terms with the following exponents:

$$ e^{-2 -4 -6'}, \quad e^{-2 +4 -6'}, \quad e^{+2 -4 -6'}, \quad e^{+2 +4 -6'} \quad (23) $$

When we multiply these together to obtain $(-2 \alpha \beta)$ we obtain ten terms corresponding to the combinations of the terms in (23) taken two at a time. Of these ten terms, two of them occur at $t'_6 = 0$ and represent the free decay following the third pulse. Of the remaining eight terms, four must occur at negative time $t_6$ and four at positive time. We temporarily disregard those at negative time and consider those at positive time, which predict echoes. What are the coherences for which these terms in $t_6$ are the echoes? Prior to the third pulse, the only coherences are the free decay following each of the first two pulses plus the echo. These coherences are reflected in inverted order in $t_6$ at their appropriate times. They form the only possible two-pulse echoes which can occur in $t_6$; however, we have just found that there must be four echoes instead of three in the time $t_6$ following the third

* We shall neglect the edge echoes from here on.

pulse. There is therefore one echo which cannot be explained in terms of two pulses. This echo which occurs at $t'_6 = t_2$ is called by Hahn the "stimulated echo". In terms of Hahn's vector diagrams[^2] the moment distribution, after fanning out during the time $t_2$, is turned only $90^\circ$; the distribution is then stacked in different positions in the z direction which remain unchanged during time $t_4$. After the third pulse the distribution is returned to the xy plane. From the term $(-2 \alpha \beta)$ corresponding to the situation in Figure 4, we find that the coefficient of $e^{-i \Delta \omega (t'_6 - t_2)}$ is

$$ (-2 \alpha \beta)_{t'_6 = t_2} = -4 \gamma_1 \delta_1 \beta_3 \delta_3 \alpha_5 \beta_5 \quad (24) $$

For the special case in which $\phi = 0$ and the three pulses are identical, (24) reduces to

$$ (-2 \alpha \beta)_{t'_6 = t_2} = 1/2 \sin^3 bt \quad (25) $$

in agreement with the result calculated by Hahn.

#### E. Three Equally Spaced Pulses

The numbers of echoes and their amplitudes is also a function of the positions of the pulses. In section D above we were careful to state that the third pulse should occur after the simple echo following the first two pulses. Obviously, if the third pulse occurs too soon, certain "echoes of echoes" cannot occur and the amplitudes and the numbers of the echoes following the third pulses will be different. This has been briefly mentioned by Hahn[^2]. Here we will discuss an interesting special case, that of three equally spaced pulses ($t_2 = t_4$). In this particular case, there will be only two echoes following the third pulse and these echoes will be spaced so as to continue the original pulse train.

The details of the calculations are the same as in the preceding cases, and we shall merely state the result for the coefficient of the echo which occurs at a time $t_2$ (or $t_4$) following the third pulse, i.e., the first of the two echoes. This coefficient is given by

$$ (-2 \alpha \beta)_{t'_6 = t_2} = -2 \left[ 2 \gamma_1 \delta_1 \beta_3 \delta_3 \alpha_5 \beta_5 + (\alpha_1 \delta_1 + \beta_1 \gamma_1) \delta_3 \gamma_3 \beta_5^2 \right] \quad (26) $$

Although one would expect a phenomenon such as this to be complicated, a description of what is happening in (26) is really quite simple. The first term we recognize from (24) to be the formula for the three-pulse "stimulated" echo. In the second term, the first section $(\alpha_1 \delta_1 + \beta_1 \gamma_1)$ we recognize from (11) to be the matrix element in R which leaves the Z component unchanged; the rest of this term is the formula for the two-pulse echo produced by the second and third pulses. We thus get the rather amusing result that the echo is merely the direct sum of two echoes, one of which is the stimulated echo produced by the three pulses, the other is the two-pulse echo of the free decay following the second pulse. One might think that such a direct sum of echoes would be likely under certain conditions to give an amplitude greater than the original polarization; however, an analysis of the coefficients shows that this is not so.

#### F. More Than Three Pulses

In his original article, Hahn[^2] pointed out the existence of two- and three-pulse echoes. It was of interest in connection with this project to find out if these were the only types of echoes that could be produced, or if there were also echoes that could be understood only in terms of four pulses, five pulses, or n pulses. In this discussion, we shall not try to prove the existence of n-pulse echoes for any n but we shall investigate the possibility that there exist four-pulse echoes, which will imply that if such things exist there may also exist echoes that could be formed only with n > 4 pulses.

We suppose that we apply four pulses spaced so that all echoes which can be produced by any one set of pulses occur before the next pulse is applied (Figure 4). The calculation proceeds in exactly the same way as for the case of three unequally spaced pulses; it is somewhat laborious and there is no point in showing the details. We will point out, however, that the matrix elements $\alpha \beta$ each consist of eight terms which, taken two at a time and combining similar exponents, gives a total of 36 terms in the product $-2 \alpha \beta$. Of these 36 terms, four occur at $t'_8 = 0$ and represent the free decay following the fourth pulse. The remaining terms are symmetrically located about $t'_8 = 0$ giving 16 terms prior to the fourth pulse, which we disregard, and 16 positive corresponding to echoes. Now if we look at all possible combinations of coherences which can produce two- and three-pulse echoes following the fourth pulse, we find on first count that there are only 12 such echoes. Before going any further, let us return for a moment to the case of three unequally spaced pulses. We note that there must be four coherence terms for $t_6 < 0$, symmetric about the third pulse with respect to the four echoes in $t_6$. However, there are only three actual coherences in the time prior to the third pulse. The extra term, shown by a dotted line in Figure 4, is therefore a "virtual" echo that does not exist until the third pulse is applied, but following the third pulse the nuclear system behaves in every way as if the virtual echo had actually occurred.

If we include the virtual echo among the source of two- and three-pulse echoes following the fourth pulse, we get a total of 14 such echoes. This still leaves two echoes unaccounted for, which must be four-pulse or "super-stimulated" echoes.

The analysis can be extended readily to n pulses. If all pulse spacings are unequal, and if $t_{2n-2} > \sum_{k=2}^{2n-4} t_k$ as before, then, following the nth pulse there will be $2^{2n-4}$ echoes. Since the total number of coherences, real and virtual, due to the (n-1)st pulse is $2(2^{2n-6}) + 1$ the nth pulse must create $(2^{2n-5} - 1)$ new virtual coherences.

#### G. Sets of Double Pulses

A special case of four pulses which is of particular interest is that of a two-pulse spin-echo experiment repeated in a time $\lesssim T_1$, so that the sample still has some memory of the previous set of two pulses. In this case one usually observes at least one additional echo, marked S in Figure 5, following the primary echo. The origin of this echo is as follows: Pulse 3, Figure 5, creates a virtual echo, V, which is mathematically similar to the stimulated echo which would occur at the position occupied by pulse 4. Pulse 4, however, transforms V into a two-pulse echo at S. That this analysis is essentially correct can be seen by calculating the matrix element for this echo. The calculation gives

$$ (-2 \alpha \beta)_S = -4 \gamma_1 \delta_1 \beta_2 \delta_2 \gamma_3 \delta_3 \beta_4^2 \quad (27) $$

(the subscripts apply to Figure 5), which is a stimulated echo transformed by another pulse.

As can be seen from its genesis, this secondary echo has many properties in common with Hahn's stimulated echo. In particular, its amplitude is more nearly dependent on $T_1$ than on $T_2$ and is relatively immune to self-diffusion effects. Experimentally, if the signal-to-noise is high, this echo can often be seen even when the time between double pulses is several times $T_1$.

In the vicinity of resonance, and for pulses of equal length and amplitude, Equation (27) reduces to

$$ (-2 \alpha \beta)_S = \frac{1}{2} \sin^3 bt \sin^2 \frac{bt}{2} \quad (28) $$

which has its maximum at $\cos bt = (-\frac{1}{4})$. If the experimental repetition rate is fast enough, additional echoes can be seen following S which can be explained in terms of virtual echoes of S on pulse three, etc. In some cases real echoes can be seen preceding the pulses as well as following them but these must be explained by the methods used in Subsection V (see Figure 8).

### IV. Coherence Detail

#### A. Introduction

In the original spin echo experiments[^2] performed in fields that were only slightly inhomogeneous, it was shown that:

1. The spacing between second pulse and echo was approximately the same as between lst and second pulse.

2. The free decay was the Fourier transform of the moment distribution in the magnetic field.

3. The echo was shaped like two free decays placed back to back.

In this section we shall consider a somewhat different case, that of a magnetic field so inhomogeneous that the total inhomogeneity, $\gamma \Delta H$, is very much greater than the frequency spectrum of the pulses. We shall assume an "infinite flat-topped" distribution $[M_o(\Delta \omega) = \text{constant for all } \Delta \omega]$, and we shall calculate the exact location and the shape of the free decay and the two-pulse echo.

#### B. Free Decay

The shape of the free decay can be deduced from the matrix element for this coherence (Equation 17). Before proceeding any further, we may remark that only the component in the y direction, corresponding to the imaginary part of the matrix element, is effective in producing a signal. This result, which is true for all the phenomena considered in this paper, follows from the fact that the two vectors for each value of $|\Delta \omega|$ are at all times symmetrically located about the yz plane. We thus consider the imaginary part of Equation (17):

$$ \text{Im}(-2 \alpha \beta) = \cos \phi \sin b t_1 \cos \Delta \omega t'_2 - \sin 2 \phi \sin^2 \frac{b t_1}{2} \sin \Delta \omega t'_2 \quad (29) $$

The frequency spectrum of the free decay is determined in this case not by the field inhomogeneity, but by the r-f level. Thus for a given value of $\gamma H_1 t_1$, a long pulse of weak radio frequency will have a long free decay and a short pulse of strong radio frequency will have a short decay.

It is possible to write (29) as

$$ \text{Im}(-2 \alpha \beta) = \cos \Delta \omega t \cos \Delta \omega t'_2 + \sin \Delta \omega t \sin \Delta \omega t'_2 \quad (30) $$

where the maximum coherence presumably occurs at $t'_2 = t$. A little algebra gives

$$ \tan \Delta \omega t = - \sin \phi \tan \frac{b t_1}{2} \quad (31) $$

From (31) we see that there is no one instant of time when all components are exactly in phase. However, we can determine a time (prior to the end of the pulse) when the free decay, projected back to this time, would have had its maximum value. If $\gamma H_1 t_1$ is small ($\le 1$) and we consider only the components about resonance, we can approximate (31) by

$$ \Delta \omega t = - \frac{b t_1}{2} \sin \phi \quad (32) $$

and since $\sin \phi = \frac{\Delta \omega}{b}$ we have simply

$$ t = - \frac{1}{2} t_1 \quad (33) $$

so the free decay behaves as if it had started from the midpoint of the pulse. When $\gamma H_1 t_1 > 1$, t is different for different groups of values of $\Delta \omega$, with the result that the free decay may show considerable structure. An example of such a free decay is shown in Figure 6.

#### C. Edge Echo

The edge echo, produced only by nuclei that are far from resonance, is contained primarily in the second term of Equation (29). In the vicinity of maximum coherence the amplitude is approximately proportional to $\int \sin \Delta \omega (t_2 - t_1) d(\Delta \omega)$. The shape of this signal is not the single lobe usually associated with an echo. Instead, if detected by a phase-sensitive detector, it reaches a maximum, goes sharply through zero at $t'_2 = t_1$,

and goes through a maximum in the opposite direction. If the edge echo is viewed only in absolute value, it appears as two maxima separated by a sharp minimum. An example of this characteristic shape is shown in Figure 3.

#### D. Two-Pulse Echo

The two-pulse echo signal is given by the imaginary part of (22):

$$ \text{Im}(-2 \gamma \delta \beta^2) = - \cos^3 \phi \sin b t_1 \sin^2 \frac{b t_3}{2} \cos \Delta \omega (t'_4 - t_2) $$

$$ - \sin 2 \phi \cos^2 \phi \sin^2 \frac{b t_1}{2} \sin^2 \frac{b t_3}{2} \sin \Delta \omega (t'_4 - t_2) \quad (34) $$

This differs considerably from (29) and the echo is therefore not the same as two free decays placed back-to-back. The common factor $\cos^2 \phi$ in (30) cuts down the high frequency terms in the echo, with the result that the echo is a considerably rounded-off version of the original square pulse. If we write (34) in the form $\cos \Delta \omega (t'_4 - t_2 - t)$ we again get (32) and (33) as expressions for t. In other words, if we sweep the oscilloscope with repetition rate $\tau$, where $\tau$ is the time between pulses, and if $\gamma H_1 t_1 = \gamma H_1 t_3 \le 1$, we will find the echo superimposed on the pulse traces with the echo maximum exactly at the center of the pulse (see Figure 7). For $\gamma H_1 t_1 > 1$, the echo shape can get quite complicated (Figure 6).

### V. Continuous Pulse Trains

#### A. Introduction

In the previous sections, we discussed solutions of Bloch's equations which were applicable to spin echo for the case of a small or at least finite number of pulses. In this and the following subsection (V and VI) we will attempt to do the same thing for continuous trains of pulses. We can assume that the pulse trains start at some initial time $t = 0$ and then continue for a time very much longer than the relaxation time T of the substance so that the sample has essentially forgotten when the beginning of the pulse train occurred. In general, the same assumptions hold here as held in the previous sections with regard to equality of relaxation times and negligible self-diffusion, except that from now on we shall include the relaxation effects explicitly in our equations. This is necessary, because we will be working with infinite series which must converge and may not do so unless we include the relaxation terms.

In what follows, we shall call the repetition time between successive cycles of pulses $\tau$ and other definitions shall be as in preceding paragraphs. We shall, in general, assume that pulse widths are short compared to $\tau$ and that $\tau$ is short compared to the relaxation time T.

#### B. Symmetry with Respect to Time Inversions

One of the most important properties of the nuclear system when subjected to continuous pulse trains is the property of time symmetry. Consider the basic equation for the motion of the polarization

$$ \frac{d\vec{M}}{dt} + \frac{\vec{M}}{T} + \gamma \vec{H} \times \vec{M} = \frac{M_o \vec{z}}{T} \quad (1) $$

Suppose in Equation (1) we make T large so that the relaxation term is small compared with the other terms in the equation. We see that, in this case, reversal of the sign of t is equivalent to a reversal of the sign of the gyromagnetic ratio $\gamma$. Thus, if we go backward in time, any solutions which we obtain must also be solutions of Bloch's equations, except for the sign of $\gamma$, which will make no difference in a system which does not detect phase[^6-note]. Now, if we have a driving function which is an even function of time, then after the system has settled down to steady state, so that it has forgotten the beginning of the train of pulses, it will make no difference to the system whether we take time in the backward or forward direction since the driving function is equivalent in each case. The symmetry argument then states that except for 180 degree change in phase the solutions of our equations must be symmetrical on both sides of the axis of time symmetry of the original pulse train. Thus the system must not only produce free decays and edge echoes following the pulses but must anticipate the pulses in exactly the same way. If the driving function consists of double pulses there will be echoes preceding and following the pulses. This property of anticipating the driving function is shown in Figure 8. Actually, the signal shown in this figure is not perfectly symmetrical owing to self-diffusion effects.

#### C. End of a Train of Single Pulses

We have just shown that the nuclear system, exposed to a train of single pulses, will eventually set up a configuration in which it will anticipate the onset of the pulses. It is also of interest to see what will happen if the pulse train is suddenly stopped.

The solution of Bloch's equations for a continuous train of pulses has been given in I. If subscript 1 applies to the pulse and 2 to the interval between pulses, then the solution can be written as

$$ M = (1 - \alpha)^{-1} \left[ (1 - \lambda_1) M_1 + \lambda_1 (1 - \lambda_2) M_2 \right]. \quad (35) $$

The notation used in (35) is identical to that used in the derivations in I. It is, unfortunately, not possible to add R-matrices by performing any simple operation on the corresponding Q-matrices. Calculation of (35) must therefore be carried out with 3 x 3 matrices and becomes quite tedious. The solution can be written in the form

$$ M = \left[ f + g e^{i \Delta \omega t_2} + h e^{-i \Delta \omega t_2} \right] e^{-i \Delta \omega t_2} / \det (1 - \alpha) \quad (36) $$

where f, g, h are polynomials in $\alpha_1, \beta_1, \gamma_1, \delta_1$, and $e^{-\tau/T}$. Of interest to us is the effect of the denominator, which can be expanded in a power series as follows:

$$ \frac{1}{\det (1 - \alpha)} \propto \sum_{n=1}^\infty \left[ \frac{e^{-\tau/T} \left( 1 - e^{-\tau/T} \right) \left( \delta_1^2 e^{i \Delta \omega t_2} + \alpha_1^2 e^{-i \Delta \omega t_2} \right)}{\left( 1 - e^{-\tau/T} \{ \alpha_1 \delta_1 + \beta_1 \gamma_1 \} \right) \left( 1 - e^{-2 \tau/T} \{ \alpha_1 \delta_1 + \beta_1 \gamma_1 \} \right)} \right] \quad (37) $$

From (36), (37) and Subsection IV D (showing that the center of an echo is related to $\tau$ rather than $t_2$) we see that the response of the nuclear system is a series of echoes spaced apart a time $\tau$, in essence trying to extend the train of pulses. From (37) we see that the echoes decay exponentially with a decay constant which is a function of $\gamma H_1 t_1$, but not of elapsed time and only indirectly of relaxation time. In other words, the decay takes place in a certain number of pulse repetition lengths, rather than in a given elapsed time. This is shown in Figure 9, which shows a decay which was independent of time even though $\tau$ was varied by almost a factor of three.

### VI. Semi-Linear Treatment of the Steady State Condition

It is well-known that the response of a nuclear resonance system to a "weak" r-f driving field, ($\gamma^2 H_1^2 T_1 T_2 \ll 1$), is a simple linear function of the radio frequency. The bulk of this paper, on the other hand, is concerned with the nonlinear effects that arise when the r-f field is strong. In this section we shall take an intermediate approach and derive an approximate solution for the response of the nuclear system to a periodic, moderately strong r-f driving function. The approximation to be taken is that the z component of polarization is constant in time, although not necessarily equal to the weak r-f polarization, $M_o$. Such a condition, in which we neglect higher order nonlinear effects due to changes in $M_z$, can be approximated if the period of the driving function, $\tau$, is short compared to $T_2$ so that $M_z$ cannot change by more than 10 per cent during the time $\tau$. If, in addition, the r-f signal is only strong enough so that $\gamma H_1 t_1 \le 0.1$ during a pulse, then the approximate solution will be valid at all times; if the r-f signal is stronger the solution will be valid between pulses but not during a pulse.

In the notation of Bloch[^1] and of Jacobsohn and Wangness[^6], Bloch's equations can be written

$$ \left. \begin{aligned} \frac{dF}{dt} + (\frac{1}{T_2} + i \Delta \omega) F = - \gamma H_1 M_z \\ \\ \frac{dM_z}{dt} + \frac{M_z - M_o}{T_1} = \gamma H_1 v \end{aligned} \right\} \quad (38) $$

$$ F = v + iu $$

The integral solution of these equations can be written[^6] as

$$ M_z = M_o + \int_{-\infty}^t \gamma H_1 v e^{-\frac{t-t'}{T_1}} dt' \quad (39) $$

$$ F = - \int_{-\infty}^t \gamma H_1 M_z \exp \left[ - \frac{t - t'}{T_1} - i \int_{t'}^t \Delta \omega (t'') dt'' \right] dt' \quad (40) $$

Here $H_1$, v and $M_z$ are all functions of time. We shall be considering the case where $H_1$ is amplitude modulated, but not frequency modulated, so that Equation (40) simplifies to

$$ F = - \int_{-\infty}^t \gamma H_1 M_z e^{(-\frac{1}{T_2} - i \Delta \omega)(t-t')} dt' \quad (41) $$

Let us return to Equation (39). After steady state has been reached $H_1$ and v will both be periodic with period $\tau$. We can then split the integral in (39) into units each of duration $\tau$. From the periodicity, we have

$$ \int_{t-(n+2)\tau}^{t-(n+1)\tau} \gamma H_1 v \exp(-\frac{t-t'}{T_1}) dt' = e^{-\tau/T_2} \int_{t-(n+1)\tau}^{t-n\tau} \gamma H_1 v \exp(-\frac{t-t'}{T_1}) dt' \quad (42) $$

As a result, (39) can be written as an infinite series which, when summed, gives us

$$ M_z = M_o + \frac{1}{1 - e^{-\tau/T}} \int_{t-\tau}^t \gamma H_1 v e^{-\frac{t-t'}{T_1}} dt' \quad (43) $$

Now if $\tau \ll T_1$, we can write

$$ M_z = M_o + \frac{1}{1 - e^{-\tau/T_1}} \overline{\gamma H_1 v} \tau \quad (44) $$

where the bar indicates the average value of the product $H_1 v$ over a cycle. Using the same approximation, we can simplify Equation (44) still further and arrive at

$$ M_z = M_o + \overline{\gamma H_1 v} T_1 \quad (45) $$

We shall observe later that the average quantity $\overline{H_1 v}$ is always negative.

To solve Equation (41), let us first expand $H_1$ in a Fourier series. Let $(\Omega / 2 \pi) = 1 / \tau$ be the repetition frequency of $H_1$ and let us define $A_n$ as the Fourier coefficient of $H_1$.

$$ H_1 = \sum_n A_n e^{in \Omega t} \quad (46) $$

Let us now substitute (46) into (41), considering $M_z$ as constant, and integrate termwise. We thus get

$$ F = - \gamma M_z \sum_n \frac{A_n e^{in \Omega t}}{\frac{1}{T_2} + i \Delta \omega + i n \Omega} \quad (47) $$

Now taking $v = \frac{1}{2} (F + F^*)$, $\overline{v H_1} = \frac{1}{2} (\overline{F H_1} + \overline{F^* H_1})$,

$$ F H_1 = - \gamma M_z \sum_m \sum_n \frac{A_m A_n e^{i(m+n)\Omega t}}{\frac{1}{T_2} + i \Delta \omega + i n \Omega} \quad (48) $$

and similarly for $F^* H_1$. Since the average value simply consists of the zero frequency terms in (48) we have

$$ \overline{v H_1} = - \frac{1}{2} \gamma M_z \sum_k \left[ \frac{A_k A_{-k}}{\frac{1}{T_2} + i (\Delta \omega + k \Omega)} + \frac{A_k^2}{\frac{1}{T_2} - i (\Delta \omega + k \Omega)} \right] \quad (49) $$

which can be written

$$ \overline{v H_1} = - C M_z \quad (50) $$

In Equation (50), C is a function only of the driving field and is defined by Equation (49). We can now substitute (50) into (45), and obtain an explicit expression for $M_z$ as follows:

$$ M_z = \frac{M_o}{1 + \gamma T_1 C} \quad (51) $$

We then substitute (51) into (47) to get an explicit expression for the polarization in the xy-plane wherein all terms are either constant or can be derived from a knowledge of the driving function.

$$ F = \frac{-\gamma M_o}{1 + \gamma T_1 C} \left[ \sum_n \frac{A_n e^{in \Omega t}}{\frac{1}{T_2} + i \Delta \omega + i n \Omega} \right] \quad (52) $$

Equation (52) is our semi-linear solution. The term in brackets is the linear part; it is simply the response of a linear filter with Lorentzian bandpass characteristics, for example, a resonant electric circuit or a nuclear resonance driven by weak r-f signal. The nonlinear effects are contained in C. If we specialize to a case where $H_1(t)$ is an even function of time we can simplify (49) to the following:

$$ C = \frac{\gamma}{T_2} \sum_k \frac{A_k^2}{\frac{1}{T_2^2} + (\Delta \omega + k \Omega)^2} \quad (53) $$

Inspection of Equation (53) shows that C becomes appreciably large only if $\Delta \omega$ is at or very close to a sideband of the driving radio frequency. Thus, if $\Delta \omega + k \Omega \approx 0$, we have $C \approx T_2 \gamma A_k^2$, otherwise we have $C \approx 0$. The effect of Equation (53) on $M_z$ and therefore also on F is that $M_z \approx M_o$ in between sidebands; but at a sideband we have

$$ M_z \approx \frac{M_o}{1 + \gamma^2 T_1 T_2 A_k^2} \quad (54) $$

Thus, in this approximation, the response of the nuclear resonance to an amplitude-modulated r-f signal can be described as behaving like a saturable Lorentzian filter, the amount of saturation obeying Bloch's slow-passage equations[^1] for the Fourier components of $H_1$ which are in the vicinity of resonance.

If the sample is in an inhomogeneous magnetic field, then the semilinear approximation predicts that a strong r-f signal will "burn holes" in the net polarization at each sideband of the r-f signal. This is identical to an effect described by Bloembergen, Purcell and Pound[^7] for slow-passage (i.e., single frequency) r-f signal; the analysis presented here shows that the same effect is produced by amplitude-modulated r-f signal.

### VII. Experimental Apparatus

Although the spin echo apparatus used in making the traces shown in Figures 3, 6, 7-9 and in testing the theory generally was of fairly conventional design, a few words will be said concerning the characteristics and performance of this particular instrument. The apparatus employed a coherent source of 30 megacycles, consisting of a free-running crystal oscillator whose output was keyed after it had passed through several doubler and buffer stages. The r-f pulses had a rise time of 10 microseconds and produced a maximum field, $2 H_1$, at the sample, of about 10 gauss. Both r-f intensity and pulse length were variable. The probe used crossed coils[^8]. The proton sample, about 25 cc in volume, was placed in a permanent magnet whose pole faces were shimmed in such a way that the field inhomogeneity across the sample was approximately 25 gauss, corresponding to a "bandwidth" of 100 kc. The distribution of nuclei in this field was such that the polarization was approximately constant over more than half of the total bandwidth. The bandwidths of the transmitter and receiver circuits were likewise about 100 kc. Although the direct coupling between transmitter and receiver in a crossed-coil probe tends to be frequency dependent, it was found possible to reduce the overall coupling to the point where the r-f pulses would not overload the receiver amplifiers.

In a magnetic field as inhomogeneous as the one used here, the effects of self-diffusion severly limit the time in which one can do echo and pulse-train experiments. Experiments involving only a few pulses can be done in ten milliseconds or less; for this a fairly viscous material, such as glycerine or SAE-30 motor oil, is useful. Experiments involving repeated pulses require longer times; for these the best sample material is a non-viscous liquid in a fairly viscous emulsion. Most of the photographs shown here were taken with a sample of water mixed in lanolin, of the type used in cosmetic-cream preparations. Even so, the lifetime for two-pulse echoes before disappearance under self-diffusion effects was only about 60 milliseconds.

[**FIGURE 1**]
FIGURE 1
DIAGRAM OF THE VECTORS $\vec{M}$, $\vec{B}$, AND THE PRECESSION CONE

[**FIGURE 2**]
FIGURE 2
DIAGRAM FOR THE SINGLE PULSE PROBLEM

[**FIGURE 3**]
FIGURE 3
PULSE, FREE DECAY AND EDGE ECHO IN A TRAIN OF SINGLE REPEATED PULSES

[**FIGURE 4**]
FIGURE 4
DIAGRAM FOR PROBLEM OF FOUR UNEQUALLY SPACED PULSES

[**FIGURE 5**]
FIGURE 5
DIAGRAM FOR PROBLEM OF SETS OF TWO PULSES

[**FIGURE 6**]
FIGURE 6
FREE DECAY, EDGE ECHO AND ECHO FOR $\gamma H_1 t_1$, SEVERAL TIMES $360^\circ$

[**FIGURE 7**]
FIGURE 7
SUPERPOSITION OF FIRST PULSE, SECOND PULSE AND ECHO SHOWING ECHO SHAPE AND POSITION OF ECHO MAXIMUM

[**FIGURE 8**]
FIGURE 8
CLOSELY REPEATED DOUBLE PULSE TRAIN SHOWING SECONDARY ECHOES AND ONE ANTICIPATORY ECHO. (THE TWO LARGEST PULSES ARE THE DRIVING PULSES. THE OVERSHOOT FOLLOWING THE PULSES WAS CAUSED BY AN AUDIO FILTER PRECEDING THE OSCILLOSCOPE.)

[**FIGURE 9**]
FIGURE 9
EFFECTS AT END OF A PULSE TRAIN SHOWING TWO DIFFERENT REPETITION RATES
(a) $\tau = 1$ millisecond
(b) $\tau = 2.5$ milliseconds

[^1]: F. Bloch, *Phys. Rev.* **70**, 460 (1946).
[^2]: E. L. Hahn, *Phys. Rev.* **80**, 580 (1950).
[^3]: E. T. Jaynes, "Basic Considerations," hereinafter referred to as I.
[^4]: H. Goldstein, *Classical Mechanics* (Addison-Wesley Press, Cambridge, Mass., 1951).
[^5]: T. Das and A. Saha, *Phys. Rev.* **93**, 749 (1954).
[^6]: B. Jacobsohn and R. K. Wangsness, *Phys. Rev.* **73**, 942 (1948).
[^6-note]: This symmetry argument is similar to the property discussed in reference [^6]; there it is valid for a weak, frequency-modulated r-f signal and requires no assumptions about the magnitude of $T_1$.
[^7]: N. Bloembergen, E. M. Purcell, and R. V. Pound, *Phys. Rev.* **73**, 679 (1948).
[^8]: F. Bloch, W. W. Hansen, and M. Packard, *Phys. Rev.* **70**, 474 (1946).
