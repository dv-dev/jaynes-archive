---
title: "Circuit Analysis by Laplace and Fourier Transforms"
year: 1945
abstract: >
  A series of nine lectures given at the Combined Research Group,
  Naval Research Laboratory, Washington, D. C. in August 1945.
  The course provides a technique for solving practical transient problems
  using classical, Heaviside, and Laplace transform methods.
author: ["E.T. Jaynes"]
---

## FIRST LECTURE: Classical and Heaviside Methods

**Textbook:** Gardner and Barnes, *Transients in Linear Systems*, Wiley, 1942.[^gardner-barnes-1942]
**Other books** by Berg, Bush, Cohen, Carson, Kurtz and Corcoran, Skilling, Stephens, and Churchill may be consulted.

**Aim of course:** to provide a technique for solving practical transient problems.

The classical method will be studied first, using as an example a series-peaked video amplifier stage. This problem will later be solved operationally. We assume a "unit step" current applied to the interstage coupling circuit, defined by:

$$
i(t) = 
\begin{cases} 
0 & t < 0 \\
i_0 & t > 0 
\end{cases}
$$

The circuit and terminology are as shown below:

*(Diagram: Current $i(t)$ enters a parallel circuit. Branch 1 is a capacitor $C$ with current $i_1(t)$. Branch 2 is an inductor $L$ and resistor $R$ in series with current $i_2(t)$. The voltage across the parallel combination is $e(t)$.)*

The problem will be solved when we have found $e(t)$. The standard classical procedure would be to set up a differential equation in which $e(t)$ is the unknown and $i(t)$ the driving function. However, in this relatively simple problem, the driving function is not differentiable, and the procedure described would fail.

Hence, even in this case we must use an artifice in order to arrive at $e(t)$, which consists of finding $i_2(t)$ first, and then using the solution of the sub-problem to find $e(t)$.

The fundamental equations of the circuit may be written as follows:

$$
\begin{aligned}
i_1 &= i - i_2 = C \frac{de}{dt} \quad &(1) \\
R i_2 &+ L \frac{di_2}{dt} = e(t) \quad &(2) \\
\frac{de}{dt} &= L \frac{d^2 i_2}{dt^2} + R \frac{di_2}{dt} = \frac{1}{C}(i - i_2) \quad &(3)
\end{aligned}
$$

In order to eliminate $i_1$, we differentiate (2). Rearranging this equation, we have for the differential equation giving $i_2$:

$$
\frac{d^2 i_2}{dt^2} + \frac{R}{L} \frac{di_2}{dt} + \frac{i_2}{LC} = \frac{i(t)}{LC} \quad (4)
$$

This may be put into a standard form by substituting:
$$
2a = \frac{R}{L} \quad (5)
$$
$$
h^2 = \frac{1}{LC} \quad (6)
$$

The differential equation is then:
$$
\frac{d^2 i_2}{dt^2} + 2a \frac{di_2}{dt} + h^2 i_2 = \frac{i(t)}{LC} \quad (7)
$$

The solution is:
$$
i_2 = C_1 e^{-(a + \sqrt{a^2 - h^2})t} + C_2 e^{-(a - \sqrt{a^2 - h^2})t}
$$

It is seen that the condition for oscillations is $h^2 > a^2$, or:
$$
\frac{1}{LC} > \frac{R^2}{4L^2} \quad \text{or} \quad Q > \frac{1}{2}
$$
where $Q \equiv \frac{1}{R} \sqrt{\frac{L}{C}}$.

The constants $C_1$ and $C_2$ may be evaluated from the initial conditions:
$$
i_2 = 0, \quad \frac{di_2}{dt} = 0 \quad \text{at } t=0
$$

We have then:
$$
\begin{aligned}
C_1 + C_2 + i_0 &= 0 \\
C_1(a + \sqrt{a^2 - h^2}) + C_2(a - \sqrt{a^2 - h^2}) &= 0
\end{aligned}
$$

Solving for the constants:
$$
C_1 = \frac{i_0}{2} \left[ \frac{a}{\sqrt{a^2 - h^2}} - 1 \right]
$$
$$
C_2 = -\frac{i_0}{2} \left[ \frac{a}{\sqrt{a^2 - h^2}} + 1 \right]
$$

The voltage $e(t)$ may then be found from $i_2$:
$$
e(t) = R i_2 + L \frac{di_2}{dt} = R \frac{i_0}{2} \left[ \left(\frac{a}{\rho} - 1\right) e^{-(a+\rho)t} - \left(\frac{a}{\rho} + 1\right) e^{-(a-\rho)t} \right] + L \frac{i_0}{2} \left[ -\frac{L^2}{\rho} e^{-(a+\rho)t} + \frac{L^2}{\rho} e^{-(a-\rho)t} \right]
$$

Combining terms, we have:
$$
e(t) = R i_0 \left[ 1 - \frac{1}{4} \left( 2 - \frac{a}{\rho} - \frac{\rho}{a} \right) e^{-(a+\rho)t} - \frac{1}{4} \left( 2 + \frac{a}{\rho} + \frac{\rho}{a} \right) e^{-(a-\rho)t} \right] \quad (8)
$$
where
$$
\rho \equiv \sqrt{a^2 - h^2} = \sqrt{\frac{R^2}{4L^2} - \frac{1}{LC}} = \omega_0 \sqrt{\left(\frac{1}{2Q}\right)^2 - 1} \quad (9, 10)
$$

This is the solution of the problem.

There are a few generalizations that may be made about the classical method. It is found that in all networks in which the components are linear and independent of time, the differential equations are of the type known as linear equations with constant coefficients.

Their solution consists of the **complementary function**, which is the general solution of the homogeneous differential equation obtained by putting the driving-force equal to zero, and a **particular integral** which depends on the form of the driving-force function. These are known to the engineer as the **transient** and **steady-state** responses respectively.

The transient part of the solution contains a sufficient number of arbitrary constants to enable it to meet all the prescribed initial conditions. The functions appearing in the transient are always exponential. If these exponentials are complex they always occur in complex conjugate pairs, so that their sum represents a real, exponentially damped oscillation. The difference between two real exponential functions occurs often and is called a **surge function**. It has the form illustrated below:

$$f(t) = e^{-at} - e^{-bt}$$

The two modes for a simple LRC circuit vary with increasing losses as shown below. 
*(Diagram of complex s-plane showing poles)*
With no losses ($Q=\infty$), the modes are at $\pm j\omega_0$, and represent an undamped sine wave, since $e^{j\omega_0 t} + e^{-j\omega_0 t} = 2 \cos \omega_0 t$.
As losses increase, the modes move along the arc of a circle, representing an exponentially decaying oscillation of lower frequency than $\omega_0$.
Critical damping occurs when the modes coincide at:
$$
Q = \frac{\omega_0 L}{R} = \frac{1}{R} \sqrt{\frac{L}{C}} = \frac{1}{2}
$$
and at this point there is only a single exponential term $e^{-\omega_0 t}$. As the losses increase further, the modes separate, and move along the real axis, where at infinite loss one approaches $(-\infty)$ and the other approaches zero.

The distinction between transient and steady-state is very great in the classical method, but it is a mathematical rather than physical distinction, which is lost in the operational method.

### The Heaviside Operational Method

In the Heaviside method, we obtain an operational equation from the differential equation by substituting $p = \frac{d}{dt}$, $p^2 = \frac{d^2}{dt^2}$, $\frac{1}{p} = \int_{0-}^t dt$, $\frac{1}{p^2} = \int_{0-}^t \int_{0-}^\tau (\cdot) dt^2$, etc. This transforms an integro-differential equation into an algebraic one.

If this is solved for the unknown treating $p$ as an algebraic quantity, the result is a symbolic solution involving $p$ and the driving function. This can be converted into a real time function if we know how to interpret the operational equations; we will now consider how this is done. The fundamental type of driving function is the unit step $1$ which is defined by:
$$
1 = \begin{cases} 0 & t < 0 \\ 1 & t > 0 \end{cases}
$$

Heaviside found, by working backwards from known solutions of simple differential equations, that the following interpretations of operational expressions could be made:
$$
\frac{1}{p} 1 = \int_{0-}^t dt = t \cdot 1
$$
$$
\frac{1}{p^2} 1 = \int_0^t t dt = \frac{t^2}{2} \cdot 1
$$
and, in general, we have:
$$
\frac{1}{p^n} 1 = \frac{t^n}{n!} 1 \quad (11)
$$

It should be clearly understood what this type of equation means; it is not valid to cancel out the $1$ sign, because the left hand side of the equation is not a product, but rather represents an operation on $1$. The right hand side, however, is an ordinary product, and simply means that the time function is cut off before $t$ equals 0, which amounts to assuming zero for all initial conditions.

We see that if some function $F(p)$ is given, the result of operating with this function on the unit step $1$ may be found by expanding $F(p)$ in a power series in $1/p$, after which each term may be interpreted according to equation (11). Heaviside called this process "algebrizing". By means of it, an answer in the form of a power series in $t$ can be obtained for any $F(p)$ that is analytic in $1/p$. Some of these power series are recognized as well-known functions; in this way the following identities have been established:
$$
\frac{1}{p^n} 1 = \frac{t^n}{n!} 1
$$
$$
\frac{p}{p+a} 1 = e^{-at} 1
$$
$$
\frac{ap}{p^2 + a^2} 1 = \sin(at) 1
$$
$$
\frac{p}{\sqrt{p^2 + a^2}} 1 = J_0(at) 1 \quad (12)
$$

We see that a time function can also be obtained in the form of a series of exponential terms if we expand $F(p)$ into partial fractions of the form $\frac{p}{p+a}$ and use the appropriate formula above.

The general rule for this process is called the **Heaviside expansion theorem**. If $F(p)$ is expressible as the ratio $N(p)/D(p)$ of two rational algebraic polynomials, we have:
$$
\frac{N(p)}{D(p)} 1 = \frac{N(0)}{D(0)} + \sum_{k=1}^n \frac{N(p_k)}{p_k D'(p_k)} e^{p_k t} \quad (13)
$$
where the $p_k$ are the roots of the equation $D(p)=0$ and $D'(p_k)$ is the derivative $\frac{d D(p)}{d p}$ evaluated at $p = p_k$.

It is seen that the different "modes" of network response appear as different solutions of $D(p)=0$, which ensures that all complex roots will appear in complex conjugate pairs.

If the time function operated on by $F(p)$ is not the unit step, it is usually easiest to express that time function in terms of a function $G(p)$ operating on the unit step, so that the product $F(p)G(p)$ then becomes the function to interpret. For example:
$$
\frac{1}{p+a}(e^{-bt} 1) = \frac{1}{p+a}\left(\frac{p}{p+b} 1\right) = \frac{p}{(p+a)(p+b)} 1 = \frac{e^{-at} - e^{-bt}}{b-a} 1 \quad (14)
$$

---

## SECOND LECTURE: Laplace Transforms

The last lecture covered classical and Heaviside methods of solving differential equations. The reason for success of Heaviside method was that it reduced the differential equation to an algebraic one which could be solved easily. This was because we put $p = d/dt$ and $1/p = \int dt$. All this was formalism, and its justification depended upon the possibility of interpreting the result of the algebraic solution, which interpretation could usually, but not always be made.

There is, however, another method of solution which has the same property of reducing the differential equation to an algebraic one, in a very similar way. The Laplace transform is defined by:
$$
\mathcal{L}[f(t)] = \int_{0}^{\infty} f(t) e^{-st} dt = F(s) \quad (1)
$$

It defines a functional transformation, and relates a time function $f(t)$ to a function of the complex variable $s$ which for the moment has no physical significance. Examples are:

$$
\mathcal{L}[1] = \int_{0}^{\infty} e^{-st} dt = -\frac{1}{s} e^{-st} \Big|_0^\infty = \frac{1}{s} \quad (2)
$$

$$
\mathcal{L}[t] = \int_{0}^{\infty} t e^{-st} dt = \frac{1}{s^2} \quad (\text{integrate by parts}) \quad (3)
$$

In general,
$$
\mathcal{L}\left[ \frac{t^n}{n!} \right] = \frac{1}{s^{n+1}}
$$

Compare Heaviside formulae:
$$
\frac{1}{p^n} 1 = \frac{t^n}{n!} 1
$$
$$
\mathcal{L}[e^{-at}] = \frac{1}{s+a} \quad \longleftrightarrow \quad \frac{p}{p+a} 1 = e^{-at} \quad (4)
$$
$$
\mathcal{L}[\sin at] = \frac{a}{s^2 + a^2} \quad \longleftrightarrow \quad \frac{ap}{p^2 + a^2} 1 = \sin at
$$
$$
\mathcal{L}[J_0(at)] = \frac{1}{\sqrt{s^2 + a^2}} \quad \longleftrightarrow \quad \frac{p}{\sqrt{p^2 + a^2}} 1 = J_0(at)
$$

Notice the great similarity; there is one more power of $p$ than of $s$ in each case. This is true in general, and is in fact the relation by means of which mathematicians have been able to justify the Heaviside rules for the solution of differential equations.

The operations of differentiation and integration are analyzed as follows:
$$
\mathcal{L}[f'(t)] = \int_{0}^{\infty} \frac{df(t)}{dt} e^{-st} dt
$$
Integrate by parts: $du = f'(t) dt \implies u = f(t)$, $v = e^{-st} \implies dv = -s e^{-st} dt$.
$$
= f(t)e^{-st} \Big|_0^\infty + s \int_0^\infty f(t) e^{-st} dt
$$
$$
= s F(s) - f(0) \quad (\text{if } f(t) \text{ is continuous}) \quad (6)
$$

$$
\mathcal{L}\left[ \int_{0}^{t} f(t) dt \right] = \frac{1}{s} [F(s) + f^{(-1)}(0)] \quad (7)
$$

The initial conditions are introduced automatically. It is seen that the correspondence with the Heaviside method is kept here, differentiation corresponding to multiplication of the time function by $p$ in the Heaviside system, and to multiplication of the complex function by $s$ in the Laplace method.

The reduction of the differential equation to an algebraic one is then done as follows:
$$
L \frac{di}{dt} + R i + \frac{1}{C} \int i dt = e(t)
$$

Taking the $L$ transform of both sides, we have:
$$
\mathcal{L}\left[ L \frac{di}{dt} + R i + \frac{1}{C} \int i dt \right] = \mathcal{L}[e(t)] = E(s)
$$
Or, since the $L$ transform is linear:
$$
L \mathcal{L}\left[\frac{di}{dt}\right] + R \mathcal{L}[i] + \frac{1}{C} \mathcal{L}\left[\int i dt\right] = E(s) \quad (10)
$$

Using our formulas (6) and (7), we have:
$$
L [s I(s) - i(0)] + R I(s) + \frac{1}{Cs} [I(s) + q(0)] = E(s) \quad (11)
$$

This is now reduced to an algebraic equation in $s$. Note that the initial conditions give the correct quantities to specify, namely the initial current in an $L$, and the initial charge on a $C$. Quantities such as the initial voltage on $L$ are not permissible initial conditions, because they can be changed instantaneously.

The Heaviside method automatically assumes zero initial conditions, because the operational interpretation of $1/p = \int_{0-}^t dt$ requires the $(-0)$ as the lower limit, in order that $p$ and $1/p$ be exactly inverse operations, whereas the Laplace transforms have $(+0)$ as the lower limit.

If we solve (11) for $I(s)$, we have:
$$
I(s) = \frac{E(s) + L i_0 - \frac{q_0}{Cs}}{R + L s + \frac{1}{Cs}} \quad (12)
$$

The denominator of (12) looks very much like the standard expression for the steady-state impedance, if we replace $s$ by $j\omega$. It can be shown that this is true in general; in other words: **The relation between the transforms $I(s)$ and $E(s)$ is identical with the relation between the A.C. vectors $I$ and $E$ for the steady-state case, if $j\omega$ is replaced by $s$.**

This rule is of great convenience, and enables us to bypass the differential equation stage unless there is some difficulty with initial conditions. If initial conditions are ignored, the solution assumes them to be zero.

---

## THIRD LECTURE

We may apply this rule to the series-peaked video amplifier circuit discussed in lecture one, as follows:
$$
E(s) = \frac{I(s) \left[ (R+Ls)\frac{1}{Cs} \right]}{R + Ls + \frac{1}{Cs}} = \frac{I(s) [R + Ls]}{1 + RCs + LCs^2} \quad (1)
$$

The current applied was a unit step of amplitude $i_0$, $I(s) = \frac{i_0}{s}$, and:
$$
E(s) = \frac{i_0}{s} \frac{(R+Ls)}{(1 + RCs + LCs^2)}
$$

Consulting the tables,[^gardner-barnes-1942] we find pair 1.109 to be closest, but it requires factoring the denominator of the equation:
$$
E(s) = \frac{i_0}{C} \frac{(s + \frac{R}{L})}{s(s^2 + \frac{R}{L}s + \frac{1}{LC})}
$$

This requires solving the following equation for $s$:
$$
s^2 + \frac{R}{L}s + \frac{1}{LC} = 0
$$
The quadratic formula is used:
$$
\text{roots} = -\frac{R}{2L} \pm \sqrt{\frac{R^2}{4L^2} - \frac{1}{LC}}
$$

We then can identify:
$$
a_0 = \frac{R}{L}
$$
$$
\alpha = \frac{R}{2L} + \sqrt{\frac{R^2}{4L^2} - \frac{1}{LC}} = \frac{R}{2L} + \rho
$$
$$
\gamma = \frac{R}{2L} - \sqrt{\frac{R^2}{4L^2} - \frac{1}{LC}} = \frac{R}{2L} - \rho
$$

The solution is then:
$$
e(t) = \frac{i_0}{C} \left[ \frac{a_0}{\alpha \gamma} + \frac{a_0 - \alpha}{\alpha(\alpha - \gamma)} e^{-\alpha t} + \frac{a_0 - \gamma}{\gamma(\gamma - \alpha)} e^{-\gamma t} \right] \quad (6)
$$

Substituting:
$$
e(t) = \frac{i_0}{C} \left[ \frac{(R/L)}{(1/LC)} + \frac{R/L - R/2L - \rho}{(R/2L + \rho)(2\rho)} e^{-(R/2L + \rho)t} + \frac{R/L - R/2L + \rho}{(R/2L - \rho)(-2\rho)} e^{-(R/2L - \rho)t} \right]
$$

This reduces to:
$$
e(t) = R i_0 \left[ 1 + \frac{1}{2} \left( \frac{R}{2L\rho} - \frac{1}{\rho R C} - 1 \right) e^{-(R/2L + \rho)t} - \frac{1}{2} \left( \frac{R}{2L\rho} - \frac{1}{\rho R C} + 1 \right) e^{-(R/2L - \rho)t} \right]
$$

This may be rearranged in the more symmetrical form:
$$
e(t) = R i_0 \left[ 1 - \frac{1}{4} \left( 2 - \frac{a}{\rho} - \frac{\rho}{a} \right) e^{-(a+\rho)t} - \frac{1}{4} \left( 2 + \frac{a}{\rho} + \frac{\rho}{a} \right) e^{-(a-\rho)t} \right]
$$
which agrees with the result arrived at in the classical method in lecture one.

---

## FOURTH LECTURE

Correspondence between Laplace and Fourier transforms may be seen by writing:
$$
F(s) = \int_{0}^{\infty} f(t) e^{-st} dt
$$
then put $s = \sigma + j\omega$.
$$
f(t) = \frac{1}{2\pi j} \int_{c-j\infty}^{c+j\infty} F(s) e^{st} ds
$$
If $\sigma \to 0$:
$$
F(s) \to F(j\omega) = \int_{0}^{\infty} f(t) e^{-j\omega t} dt = \int_{-\infty}^{\infty} f(t) u(t) e^{-j\omega t} dt
$$
$$
f(t) = \frac{1}{2\pi j} \int_{-j\infty}^{j\infty} F(j\omega) e^{j\omega t} d(j\omega) = \frac{1}{2\pi} \int_{-\infty}^{\infty} F(j\omega) e^{j\omega t} d\omega
$$

The extension of the lower limit to $-\infty$ in the direct transform is made easily if $f(t) = 0$, $t < 0$. This is the main difference between the Fourier and Laplace transforms, and we will investigate further to see just how the complex inversion formula leads to time functions vanishing before $t=0$.

As a tool useful for later work, let us derive a preliminary result. Consider the function
$$
\frac{\sin \omega t}{t} = \omega \frac{\sin(\omega t)}{(\omega t)}
$$
as $\omega$ increases without limit.

*(Diagram showing $\frac{\sin \omega t}{t}$ becoming sharper and taller as $\omega$ increases)*

The central peak becomes higher and sharper, and the "cycles" crowd together as $\omega$ increases. However, the area under the curve remains finite and independent of $\omega$, since:
$$
\int_{-\infty}^{\infty} \frac{\sin \omega t}{t} dt = \pi \quad (4)
$$

Now if this function is multiplied by a function $f(t)$ and integrated, the rapidly alternating plus and minus values of $(\sin \omega t)/t$ will cancel out contributions except in the neighborhood of $t$ equals 0, where one infinite loop is not cancelled out by another one. This means that it is only values of $f(t)$ near to $t$ equals 0 that can contribute appreciably to the integral. In the limit, the integral is given simply by the value of $f(0)$ multiplied by the area under the oscillating curve, which is $\pi$:
$$
\lim_{\omega \to \infty} \int_{-\infty}^{\infty} f(t) \frac{\sin(\omega t)}{t} dt = \pi f(0) \quad (5)
$$

Generalizing slightly by shifting the origin of the oscillating curve, we have a formula:
$$
\lim_{\omega \to \infty} \frac{1}{\pi} \int_{-\infty}^{\infty} f(t) \frac{\sin \omega(t-u)}{(t-u)} dt = f(u) \quad (6)
$$
or, swapping variables:
$$
\lim_{\omega \to \infty} \frac{1}{\pi} \int_{-\infty}^{\infty} f(u) \frac{\sin \omega(t-u)}{(t-u)} du = f(t) \quad (6a)
$$

Now we return to the Laplace formulae:
$$
F(s) = \int_{0}^{\infty} f(t) e^{-st} dt = \int_{0}^{\infty} f(u) e^{-su} du \quad (7)
$$
$$
f(t) = \frac{1}{2\pi j} \int_{c-j\infty}^{c+j\infty} F(s) e^{st} ds \quad (8)
$$

If we substitute (7) into (8), we have:
$$
f(t) = \lim_{\omega \to \infty} \frac{1}{2\pi j} \int_{c-j\omega}^{c+j\omega} e^{st} ds \int_{0}^{\infty} f(u) e^{-su} du \quad (9)
$$

The order of integration may be reversed, giving:
$$
f(t) = \lim_{\omega \to \infty} \frac{1}{2\pi j} \int_{0}^{\infty} f(u) du \int_{c-j\omega}^{c+j\omega} e^{s(t-u)} ds \quad (10)
$$

Evaluating the inner integral, we have:
$$
\int_{c-j\omega}^{c+j\omega} e^{s(t-u)} ds = \frac{e^{s(t-u)}}{(t-u)} \Bigg|_{c-j\omega}^{c+j\omega} = \frac{1}{(t-u)} e^{c(t-u)} [e^{j\omega(t-u)} - e^{-j\omega(t-u)}]
$$
$$
= 2j e^{c(t-u)} \frac{\sin \omega(t-u)}{(t-u)}
$$

We then have:
$$
f(t) = \lim_{\omega \to \infty} \frac{1}{\pi} \int_{0}^{\infty} f(u) e^{c(t-u)} \frac{\sin \omega(t-u)}{(t-u)} du \quad (11)
$$

This is seen to be the same as $(6a)$ except for the limits of integration. From the discussion preceding $(6a)$ it is clear that negative values of $t$ must lead to the value $f(t)$ equals 0, since contributions to the integral arise only when $t$ and $u$ "cross over".

It is seen that the extra "converging power" of the Laplace transform due to the factor $e^{-\sigma t}$ is obtained at the expense of cutting off all time functions before $t$ equals 0. If we wish to keep $f(t)$ for all values of time, we cannot use the term $e^{-\sigma t}$, but must put $s$ equals $j\omega$, as in equations (2) and (3), which are standard Fourier transforms. In general, whatever lower limit was taken in the integral defining the direct transformation is the time before which the inversion integral gives $f(t)$ equals 0.

We may also see the above result from the theory of residues.

*(Diagram: Complex plane with contour integration)*

The Cauchy residue theorem is:
$$
\text{Res}(a) \equiv \frac{1}{2\pi j} \oint \frac{f(z)}{z-a} dz = f(a)
$$
where the integral encloses the point $z=a$ and $f(z)$ has no poles enclosed in the region. The loop integral around any region is then equal to $2\pi j \sum \text{Res}$.

For $t > 0$, we can define a loop enclosing all poles of the function $F(s)$. As the integral around the semi-circle vanishes for $R \to \infty$, the integral along the straight line is equal to $2\pi j \sum \text{Res}$.

For $t < 0$, the factor $e^{st}$ becomes divergent on the semicircle, and we have to complete the loop by a semicircle to the right of the straight line path. Since the new loop encloses no poles, we have $f(t) = 0$ for $t < 0$.

---

## FIFTH LECTURE

**Development of Fourier Integral from Fourier Series**

The usual form of a Fourier series is:
$$
f(t) = \frac{a_0}{2} + \sum_{n=1}^{\infty} a_n \cos n \omega_0 t + \sum_{n=1}^{\infty} b_n \sin n \omega_0 t \quad (14)
$$
where
$$
a_n = \frac{1}{\pi} \int_{-\pi}^{\pi} f(t) \cos n \omega_0 t d(\omega_0 t), \quad b_n = \frac{1}{\pi} \int_{-\pi}^{\pi} f(t) \sin n \omega_0 t d(\omega_0 t) \quad (15)
$$

This can be put into the complex form by noting that the sine and cosine terms of any frequency may be combined as follows:
$$
a_n \cos n \omega_0 t + b_n \sin n \omega_0 t = C_n e^{j n \omega_0 t} + C_{-n} e^{-j n \omega_0 t}
$$
where
$$
C_n = \frac{1}{2}(a_n - j b_n), \quad C_{-n} = \frac{1}{2}(a_n + j b_n) = C_n^*, \quad C_0 = \frac{1}{2} a_0
$$

We then have:
$$
f(t) = \sum_{n=-\infty}^{\infty} C_n e^{j n \omega_0 t} \quad (16)
$$
$$
C_n = \frac{1}{2\pi} \int_{-\pi}^{\pi} f(t) e^{-j n \omega_0 t} d(\omega_0 t) \quad (17)
$$

The similarity between these and the Fourier transform formulae is evident. We will not go through the limit process because it is too difficult, but it can be seen that a change of variable results in the formula:
$$
C_n = \frac{\omega_0}{2\pi} \int_{-\pi/\omega_0}^{\pi/\omega_0} f(t) e^{-j n \omega_0 t} dt
$$

If now we let $\omega_0 \to 0$, the limits on variation of $t$ increase without limit, and we become interested in much larger values of $n$, such that the product $n\omega_0$ remains finite, and equal to $\omega$. Then we put:
$$
C_n = \frac{\omega_0}{2\pi} F(n\omega_0) = \frac{\omega_0}{2\pi} F(\omega)
$$
$$
F(\omega) = \int_{-\infty}^{\infty} f(t) e^{-j\omega t} dt \quad (20)
$$
$$
f(t) = \sum_{n=-\infty}^{\infty} \frac{\omega_0}{2\pi} F(n\omega_0) e^{j n \omega_0 t} \quad (21)
$$
$$
f(t) = \frac{1}{2\pi} \int_{-\infty}^{\infty} F(\omega) e^{j\omega t} d\omega \quad (22)
$$

This suggests the definition of an integral, which becomes, in the limit of $\omega_0 \to \infty$ ($\omega \to 0$), so that both of the Fourier integral formulae can be deduced from the Fourier series formulae.

The geometrical/physical interpretation of a Fourier series is that of rotating vectors of various frequencies:
$\omega_0, 2\omega_0, 3\omega_0, 4\omega_0, \dots$ most active out here.
As $\omega_0 \to 0$, this merges into a continuous curve, the projection of the end of which is the voltage.

*("Snake in Complex Plane" diagram)*

In general, Laplace transforms will solve definite problems with known initial conditions more easily, while the Fourier transform is best for general arguments about phase and amplitudes, since they are directly measurable.

---

## SIXTH LECTURE

There are certain general conclusions that can be drawn from the Fourier analysis that are useful in a number of practical cases.

For instance, if $f(t)$ and $F(\omega)$ are transforms of each other, we find that $f(t-t_0)$ and $F(\omega)e^{-j\omega t_0}$ are also transforms, so that an addition of a linear phase term corresponds to a time delay.

Similarly, $f(t)e^{\pm j\omega_0 t}$ and $F(\omega \mp \omega_0)$ are transforms. The time function represents an amplitude-modulated carrier of frequency $\omega_0$, and the $F(\omega \mp \omega_0)$ term shows that the spectrum is simply that of $f(t)$ but centered around $\omega_0$ instead of zero.

The following table:

| If $f(t)$ is: | Then $F(\omega)$ is: |
| :--- | :--- |
| Real | Real part Even, Imaginary part Odd |
| Even | Real, Even |
| Odd | Imaginary, Odd |

Using these theorems, we can find the effect of suddenly impressing a sine wave of frequency $\omega_0$ on a filter which passes frequencies from $\omega_1$ to $\omega_2$.

The impressed force is represented as $\text{Re}[u(t)e^{j\omega_0 t}]$.
The transform of the bracket is:
$$
F(\omega) = \frac{1}{j(\omega - \omega_0)} \quad (1)
$$
The network function is given by:
$$
H(\omega) = 
\begin{cases} 
1 & \omega_1 \le |\omega| \le \omega_2 \\
0 & |\omega| > \omega_2 \text{ or } |\omega| < \omega_1
\end{cases} \quad (2)
$$
(No phase shift need be considered, as it would merely lead to a time delay.)

The response is then:
$$
f_1(t) = \text{Re} \frac{1}{2\pi} \int_{-\infty}^{\infty} F(\omega) H(\omega) e^{j\omega t} d\omega
$$
$$
= \text{Re} \frac{1}{2\pi j} \int_{-\omega_2}^{-\omega_1} \frac{e^{j\omega t}}{(\omega - \omega_0)} d\omega + \text{Re} \frac{1}{2\pi j} \int_{\omega_1}^{\omega_2} \frac{e^{j\omega t}}{(\omega - \omega_0)} d\omega \quad (3)
$$

The integral over negative frequencies may be neglected if $\omega_0$ is not too far from the positive pass band, so we have:
$$
f_1(t) = \text{Re} \frac{1}{2\pi j} \int_{\omega_1}^{\omega_2} \frac{e^{j\omega t}}{(\omega - \omega_0)} d\omega = \text{Re} \frac{e^{j\omega_0 t}}{2\pi j} \int_{(\omega_1 - \omega_0)t}^{(\omega_2 - \omega_0)t} \frac{e^{ju}}{u} du
$$
$$
= \text{Re} \frac{e^{j\omega_0 t}}{2\pi} \left\{ \frac{1}{j} \int \frac{\cos u}{u} du + \int \frac{\sin u}{u} du \right\}
$$

Definitions:
$$
Si(x) = \int_{0}^{x} \frac{\sin u}{u} du \quad (5)
$$
$$
Ci(x) = -\int_{|x|}^{\infty} \frac{\cos u}{u} du \quad (6)
$$

The $\cos$ integral may be split into four integrals:
$$
\int_{x_1}^{x_2} \frac{\cos u}{u} du = \int_{x_1}^{-\epsilon} + \int_{-\epsilon}^{\epsilon} + \int_{\epsilon}^{x_2} \dots
$$

*(Graphs of $Si(x)$ and $Ci(x)$)*

---

## SEVENTH LECTURE

If $x_1$ and $x_2$ are positive, $|x_1| = x_1$, $|x_2| = x_2$, and integrals vanish, leaving:
$$
\int_{x_1}^{x_2} \frac{\cos u}{u} du = Ci(x_2) - Ci(x_1)
$$

If $x_1 < 0 < x_2$, we have
$$
\int_{x_1}^{x_2} \frac{\cos u}{u} du = \int_{x_1}^{-\epsilon} \frac{\cos u}{u} du + \int_{-\epsilon}^{\epsilon} \frac{\cos u}{u} du + \int_{\epsilon}^{x_2} \frac{\cos u}{u} du
$$
The 1st and 3rd integrals cancel (if limits symmetric?), since $\cos(u)/u$ is an odd function. We are left with:
$$
\int_{-\epsilon}^{\epsilon} \frac{\cos u}{u} du = \ln(\epsilon) - \ln(-\epsilon) = \ln(-1) = j\pi
$$
$$
\int_{x_1}^{x_2} \frac{\cos u}{u} du = j\pi + Ci(x_2) - Ci(|x_1|)
$$

If $x_1 < x_2 < 0$, we have
$$
\int_{x_1}^{x_2} \frac{\cos u}{u} du = j\pi - Ci(|x_1|) - [j\pi - Ci(|x_2|)] = Ci(|x_2|) - Ci(|x_1|)
$$

The integral
$$
\int_{(\omega_1 - \omega_0)t}^{(\omega_2 - \omega_0)t} \frac{\sin u}{u} du = Si(\omega_2 - \omega_0)t - Si(\omega_1 - \omega_0)t
$$

The total response is then:
$$
v_1(t) = \text{Re} \frac{e^{j\omega_0 t}}{2\pi} \{ [Si(\omega_2 - \omega_0)t - Si(\omega_1 - \omega_0)t] + j[Ci(\omega_1 - \omega_0)t - Ci(\omega_2 - \omega_0)t] \}
$$
if $\omega_0$ is outside the pass band. If $\omega_0$ is in the band, we have:
$$
v_1(t) = \text{Re} \frac{e^{j\omega_0 t}}{2\pi} \{ [\pi + Si(\omega_2 - \omega_0)t - Si(\omega_1 - \omega_0)t] + j[Ci(\omega_1 - \omega_0)t - Ci(\omega_2 - \omega_0)t] \}
$$

**Paradox:** When the impressed frequency is not in the passband, the response ultimately dies out. Then if the impressed frequency is suddenly cut off, the principle of superposition requires that another response of reversed sign shall take place. But the network has physically no driving force at that time, so this response must be a free transient, with modes characteristic of the network alone.

How is it then that $\omega_0$ can appear in the solution? In particular, how does the network know what frequency to oscillate at when the drive is removed? How can the network "remember" the frequency $\omega_0$?

---

## EIGHTH LECTURE

**Concluding Remarks on Fourier Integrals**

Certain general features of Fourier integrals can often be used to get qualitative answers from physical reasoning without any equations. Thus, discontinuities in either $f(t)$ or $F(\omega)$ produce wiggles in the other function. This can be seen from the "Snake in the Complex plane" interpretation of the Fourier integral.

If the snake is cut off at a certain frequency, the severed end is rotating at that frequency, and wiggles of that frequency appear in the time function. This fact may be used in antenna design where it is desired to eliminate side lobes. In a broadside array, the angular radiation pattern is the Fourier transform of the amplitude distribution pattern across the array. Since side lobes represent wiggles on the pattern, it is seen that the way to avoid side lobes is to make the amplitude distribution fall off as smoothly as possible, the smoothest way being a Gauss error curve. The pattern is then another Gauss error curve.

The way the frequency function falls off may be found by inspection of the function $f(t)$ and the following rules:

The following table:

| If $f(t)$ has a: | $F(\omega)$ goes down as: |
| :--- | :--- |
| finite discontinuity | $1/\omega = 6$ db/octave |
| $df/dt$ discontinuity | $1/\omega^2 = 12$ db/octave |
| $d^2f/dt^2$ discontinuity | $1/\omega^3 = 18$ db/octave |
| $d^n f/dt^n$ discontinuity | $1/\omega^{n+1} = 6(n+1)$ db/octave |
| No discontinuity in any derivative | $\sim e^{-\omega^2}$ |
| infinite discontinuity (impulse) | $F(\omega)$ constant |
| infinite doublet disc. | $F(\omega) \sim \omega$ |

The reason for this is in the varying quality of cancellation in the integral defining $F(\omega)$, due to the smoothness of $f(t)$. The smoother this function, the more perfect the cancellation will be between adjacent half-cycles of the kernel $e^{j\omega t}$.

**Analysis of Transmission Lines by the Laplace Transform**

Fundamental equations are:
$$
v = v(x,t), \quad i = i(x,t)
$$
$$
\frac{\partial v}{\partial x} = -(R i + L \frac{\partial i}{\partial t}) \quad (1)
$$
$$
\frac{\partial i}{\partial x} = -(G v + C \frac{\partial v}{\partial t}) \quad (2)
$$

Taking the Laplace transforms of these equations:
$$
V(x,s) \equiv \int_{0}^{\infty} v(x,t) e^{-st} dt, \quad I(x,s) \equiv \int_{0}^{\infty} i(x,t) e^{-st} dt
$$
we have:
$$
\frac{\partial V}{\partial x} = -(RI + L s I - L i_0) = -(R+Ls)I + L i_0(x)
$$
$$
\frac{\partial I}{\partial x} = -(GV + C s V - C v_0) = -(G+Cs)V + C v_0(x)
$$

In most practical cases we have $i_0 = 0$, $v_0 = 0$, so we may set up a differential equation for $V$ or $I$ as follows:
$$
\frac{\partial^2 V}{\partial x^2} = (R+Ls)(G+Cs)V = \gamma^2 V \quad (3)
$$
where
$$
\gamma^2 = (R+Ls)(G+Cs) = LC[(s+\rho)^2 - \sigma^2]
$$
$$
\rho = \frac{1}{2}\left(\frac{R}{L} + \frac{G}{C}\right), \quad \sigma = \frac{1}{2}\left(\frac{R}{L} - \frac{G}{C}\right)
$$

The solution of (3) is obviously:
$$
V = C_1 e^{\gamma x} + C_2 e^{-\gamma x} \quad (4)
$$
$$
I = \frac{1}{Z_0} [C_1 e^{\gamma x} - C_2 e^{-\gamma x}] \quad (5)
$$
where
$$
Z_0 \equiv \sqrt{\frac{R+Ls}{G+Cs}}
$$

If we have finite initial values, we may put:
$$
V_0(x) = L \frac{d i_0(x)}{dx} - (R+Ls) C v_0(x)
$$
and we then add to the solution for $V$ the terms:
$$
\frac{e^{\gamma x}}{2\gamma} \int e^{-\gamma x} V_0(x) dx - \frac{e^{-\gamma x}}{2\gamma} \int e^{\gamma x} V_0(x) dx
$$

Equations (4, 5) are recognized as traveling waves, and their similarity with the well-known, steady-state equations suggests that we can simply use the steady-state equations in all manipulations, and then take the inverse transform of the result to get our transient solution.

---

## NINTH LECTURE

**Example: Distortion of a Unit Step After Traveling thru a Length of Transmission Line.**

Initial voltage $= v(0,t) = 1(t)$
Voltage at point $x = v(x,t)$

Transform of initial voltage:
$$
V(0,s) = \frac{1}{s}
$$
Transform at point $x$ is:
$$
V(x,s) = V(0,s) e^{-\gamma x} = \frac{1}{s} e^{-\gamma x}
$$
$$
\gamma = \frac{1}{v_0} \sqrt{(s+\rho)^2 - \sigma^2}
$$
where $v_0 = \frac{1}{\sqrt{LC}}$, $\rho = \frac{1}{2}(\frac{R}{L} + \frac{G}{C})$, $\sigma = \frac{1}{2}(\frac{R}{L} - \frac{G}{C})$.

$$
V(x,s) = \frac{1}{s} e^{-\frac{x}{v_0}\sqrt{(s+\rho)^2 - \sigma^2}}
$$

Pair 863.1 of Campbell & Foster is:[^campbell-foster]
$$
e^{-y\sqrt{(s+r)(s+p)}} - e^{-y[s+\frac{1}{2}(r+p)]} \leftrightarrow \frac{y(r-p)}{2\sqrt{t^2-y^2}} e^{-\frac{1}{2}(r+p)t} I_1 \left[ \frac{1}{2}(r-p)\sqrt{t^2-y^2} \right]
$$
(attenuation constant, distortion constant)

We identify $(s+r)(s+p) = (s+\rho)^2 - \sigma^2$
$$
\frac{1}{2}(r+p) = \rho
$$
$$
\frac{1}{2}(r-p) = \sigma
$$
$$
y = \frac{x}{v_0} = t_0 \quad (y < t)
$$

So the pair becomes:
$$
e^{-t_0 \sqrt{(s+\rho)^2 - \sigma^2}} - e^{-(s+\rho)t_0} \leftrightarrow \frac{\sigma t_0}{\sqrt{t^2 - t_0^2}} e^{-\rho t} I_1[\sigma \sqrt{t^2 - t_0^2}] \quad (t_0 < t)
$$

The quantity $e^{-(s+\rho)t_0}$ has the inverse transform $e^{-\rho t_0} u_{-1}(t-t_0)$, a "unit impulse" at $t=t_0$ with area $e^{-\rho t_0}$. So we have:
$$
e^{-t_0 \sqrt{(s+\rho)^2 - \sigma^2}} \leftrightarrow \frac{\sigma t_0}{\sqrt{t^2 - t_0^2}} e^{-\rho t} I_1[\sigma \sqrt{t^2 - t_0^2}] + e^{-\rho t_0} u_{-1}(t-t_0)
$$

This is the same as $V(x,s)$ except for a factor $1/s$ which denotes integration with respect to $t$. Therefore, we have:
$$
v(x,t) = \sigma x \int_{t_0}^{t} \frac{1}{v_0 \sqrt{\tau^2 - t_0^2}} e^{-\rho \tau} I_1[\sigma \sqrt{\tau^2 - t_0^2}] d\tau + e^{-\rho t_0} u(t-t_0)
$$

This is a unit step of height $e^{-\rho t_0}$ at $t=t_0$, plus distortion terms due to the integral. The modified Bessel Function $I_1$ bears somewhat the same relation to an ordinary Bessel Function $J_n(z)$ as hyperbolic functions do to trigonometric ones. Thus:
$$
I_n(z) = i^{-n} J_n(iz)
$$
which corresponds to $\cosh(z) = \cos(iz)$.

This analogy can be seen also from the equations:
$$
J_{1/2}(z) = \sqrt{\frac{2}{\pi z}} \sin z, \quad I_{1/2}(z) = \sqrt{\frac{2}{\pi z}} \sinh z
$$

Infinite series for $I_n(z)$ is:
$$
I_n(z) = \left(\frac{z}{2}\right)^n \sum_{m=0}^{\infty} \frac{(z/2)^{2m}}{m! (n+m)!}
$$
The series for $J_n(z)$ is the same except that signs alternate.

Using the infinite series representation for $I_1(z)$:
$$
v(x,t) = \frac{\sigma t_0}{2} \int_{t_0}^{t} e^{-\rho \tau} \sum_{m=0}^{\infty} \frac{[\frac{\sigma}{2} \sqrt{\tau^2 - t_0^2}]^{2m}}{m!(m+1)!} d\tau + e^{-\rho t_0} u(t-t_0)
$$

The result is expressed as an infinite series. The accuracy attained depends on the number of terms carried. If we carry the first two, with $m=0$ and $m=1$, the result will be valid for $\sigma \sqrt{t^2 - t_0^2} \ll 1$.

If $m=0$, we have:
$$
\int_{t_0}^{t} e^{-\rho \tau} d\tau = \frac{1}{\rho} [e^{-\rho t_0} - e^{-\rho t}]
$$
When $m=1$,
$$
\int_{t_0}^{t} e^{-\rho \tau} [\tau^2 - t_0^2] d\tau = -\frac{e^{-\rho t}}{\rho} [t^2 + \frac{2t}{\rho} + \frac{2}{\rho^2}] + \frac{e^{-\rho t_0}}{\rho} [t_0^2 + \frac{2t_0}{\rho} + \frac{2}{\rho^2}] + \dots
$$

For the voltage we then have, to this approximation:
$$
v(x,t) = \frac{\sigma t_0}{2\rho} \left\{ \left(1 - \frac{\sigma^2 t_0^2}{\rho} \right)(e^{-\rho t_0} - e^{-\rho t}) + \frac{\sigma^2}{8} \left[ e^{-\rho t_0}(t_0^2 + \frac{2t_0}{\rho} + \frac{2}{\rho^2}) - e^{-\rho t}(t^2 + \frac{2t}{\rho} + \frac{2}{\rho^2}) \right] \right\} + e^{-\rho t_0} u(t-t_0)
$$

The final value at $t \to \infty$ may be found from the following theorem:
$$
f(\infty) = \lim_{s \to 0} s F(s) = e^{-x\sqrt{RG}}
$$
so that the final distribution is a steady voltage, decreasing exponentially with distance from the generator.

The pulse shape taking only the 1st term of the infinite series is given by:
$$
v(x,t) = \frac{\sigma^2 t_0}{2\rho} [e^{-\rho t_0} - e^{-\rho t}] + e^{-\rho t_0} u(t-t_0)
$$

This predicts a final value of
$$
e^{-\rho t_0} \left[ 1 + \frac{\sigma^2 t_0}{2\rho} \right]
$$
whereas the exact value has been found equal to:
$$
e^{-x\sqrt{RG}} = e^{-\gamma \sqrt{\rho^2 - \sigma^2}} = e^{-\rho t_0 \sqrt{1 - (\sigma/\rho)^2}}
$$

This may be approximated by:
$$
e^{-\rho t_0 \sqrt{1 - (\sigma/\rho)^2}} \cong e^{-\rho t_0 [1 - \sigma^2/2\rho^2]} = e^{-\rho t_0} e^{\frac{\sigma^2 t_0}{2\rho}} \cong e^{-\rho t_0} \left[ 1 + \frac{\sigma^2 t_0}{2\rho} \right]
$$

This is identical with the value given by the first term of the series, showing that the approximate solution is quite good, even for large $t$. Incidentally, the equations show that the percentage of distortion terms increases as we go down the line, so that eventually the initial sharp rise is lost in distortion terms. The final value is always greater than the value of the initial sharp jump.

[^gardner-barnes-1942]: Gardner, M. F., and J. L. Barnes, *Transients in Linear Systems*. Wiley, 1942.
[^campbell-foster]: Campbell, G. A., and R. M. Foster, *Fourier Integrals for Practical Applications*. Van Nostrand, 1948.
