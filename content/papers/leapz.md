---
title: "Straight Line Fitting: A Bayesian Solution"
year: 1991
abstract: >
  Fitting the "best" straight line to a scatter plot of data
  $D = \{(x_1, y_1)...(x_n, y_n)\}$ in which both variables $x_i, y_i$
  are subject to unknown error is undoubtedly the most common problem of
  inference faced by scientists, engineers, medical researchers, and
  economists. The problem is to estimate the parameters $\alpha, \beta$
  in the straight line equation $y = \alpha + \beta x$, and assess the
  accuracy of the estimates. Whenever we try to discover or estimate a
  relationship between two factors we are almost sure to be in this
  situation. But from the viewpoint of orthodox statistics the problem
  turned out to be a horrendous can of worms; generations of efforts led
  only to a long line of false starts, and no satisfactory solution.
  We give the Bayesian solution to the problem, which turns out to be
  eminently satisfactory and straightforward, although a little tricky
  in the derivation. However, not much of the final result is really
  new. Arnold Zellner (1971) gave a very similar solution long ago, but
  it went unnoticed by those who had the most need to know about it. We
  give a pedagogical introduction to the problem and add a few final
  touches, dealing with choice of priors and parameterizations.
  In any event, whether or not the following solution has anything new
  in it, the currently great and universal importance of the problem
  would warrant bringing the result to the attention of the scientific
  community. Many workers, from astronomers to biologists, are still
  struggling with the problem, unaware that the solution is known.
author: ["E.T. Jaynes"]
categories: ["Foundations of Probability & Bayesian Inference"]
tags: ["straight line fitting", "linear regression", "Bayesian inference", "nuisance parameters", "priors", "least squares", "parameterization"]
---
Presented at the Tenth Annual MAXENT Workshop, University of Wyoming,
July 1990. To appear in the Proceedings Volume, W. T. Grandy & L.
Schick, Editors, Kluwer Academic Publishers, Holland.
## INTRODUCTION
The following discussion is an instructive case history showing how
nontrivial Bayesian results evolve. It illustrates three very important
points:

In estimating $\alpha, \beta$, we have potentially $n+2$ nuisance
parameters, {$X_1 \dots X_n, \sigma_x, \sigma_y$}. Denoting prior
information by $I$, the most general solution will then have a joint
prior pdf for $n+4$ parameters:
$$p(\alpha, \beta, X_1 \dots X_n, \sigma_x, \sigma_y | I) = p(\alpha, \beta|I) p(X_1 \dots X_n, \sigma_x, \sigma_y | \alpha, \beta, I) \tag{1}$$and an unending variety of different kinds of prior information $I$
might be expressed by this function, which we understand is to be
properly normalized to unit integral.
By the product rule, $p(\alpha, \beta|I)$ can always be factored as
shown, although the possibility of a Borel-Kolmogorov paradox should be
kept in mind. That is, by a probability $p(A|\alpha, \beta, I)$
conditional on point values of $\alpha, \beta$, we must understand the
limit of the well-defined
$$P(A|d\alpha d\beta I) = \frac{P(A, d\alpha d\beta|I)}{P(d\alpha d\beta|I)} \tag{2}$$as $d\alpha \to 0, d\beta \to 0$. To avoid ambiguity it is necessary to
prescribe the exact way in which the limit is to be approached.

For example, if we set $d\alpha = \epsilon g(\beta)$ and pass first to
the limit $\epsilon \to 0$, our final results will in general depend on
which function $g(\beta)$ we chose. But there is no 'right choice' or
'wrong choice' because it is for us to say which limit we want to take;
i.e., which problem we want to solve. Any choice presumably corresponds
to a legitimate problem that we might want to reason about, and
probability theory will then give us the correct solution to that
problem. But having made one choice, we must stick to that choice
throughout the calculation, otherwise we are switching problems in
midstream and are pretty sure to generate contradictions.

This is Sermon #1 on mathematical limits; although it was given long ago
by Kolmogorov, many who try to do probability calculations still fail to
heed it and get themselves into trouble. The moral is that, unless they
are defined in the statement of a problem, probabilities of the form
$p(A|\dots I)$ conditional on point values of a parameter, have no
meaning until the specific limiting process is stated. More generally,
probabilities conditional on any propositions of probability zero, are
undefined.

In the following we use the abbreviations
$$x = \{x_1 \dots x_n\}, \quad Y = \{Y_1 \dots Y_n\}, \quad \text{etc.,} \tag{3}$$so that our data are denoted by $D=x,y$. Then the most general sampling
pdf would have the functional form
$$p(x, y | \alpha, \beta, X, \sigma_x, \sigma_y, I) \tag{4}$$ and the most
general solution we contemplate here would have the form
$$p(\alpha, \beta|x, y, I) = p(\alpha, \beta|I) \frac{p(x, y|\alpha, \beta, I)}{p(x, y|I)} \tag{5}$$in which
$$p(x, y|\alpha, \beta, I) = \int d^n X d\sigma_x d\sigma_y \, p(x, y|\alpha, \beta, X, \sigma_x, \sigma_y, I) p(X, \sigma_x, \sigma_y|\alpha, \beta, I) \tag{6}$$  
$$p(x,y|I) = \int d\alpha d\beta \, p(x, y|\alpha, \beta, I) p(\alpha, \beta|I) \tag{7}$$and, writing
$x^{*}, y^{*} = \{(x_{m+1}, y_{m+1}) \dots (x_{m+n}, y_{m+n})\}$, our most
general predictive distribution is
$$p(y^{*}|x^{*}, x, y, I) = \int p(y^{*}|x^{*}, \alpha, \beta, I) p(\alpha, \beta|x, y, I) d\alpha d\beta \tag{8}$$This defines our present horizon (but having found this solution, its
extension to such details as more than two variables, correlated noise,
noise known to vary with $x$, etc. is an easy homework problem,
involving little more than promoting some of our symbols from numbers to
matrices).
## SPECIAL CASES
Note first how the standard solutions are contained in this as special
cases. If, as is almost universally supposed, the prior pdf for the
errors factors completely:
$$p(e, f|I) = \prod_{i=1}^n p(e_i|I)p(f_i|I) \tag{9}$$with common Gaussian distributions
$$p(e_i|I) = \frac{1}{\sqrt{2\pi}\sigma_x} \exp\left(-\frac{e_i^2}{2\sigma_x^2}\right), \quad p(f_i|I) = \frac{1}{\sqrt{2\pi}\sigma_y} \exp\left(-\frac{f_i^2}{2\sigma_y^2}\right) \tag{10}$$Now, dropping the prior information symbol $I$, which we suppose
henceforth to be hidden in the right-hand side of all our probabilities,
our sampling pdf is
$$p(x, y | \alpha, \beta, \sigma_x, \sigma_y, X) = \prod_{i=1}^n \frac{1}{2\pi \sigma_x \sigma_y} \exp\left\{-\frac{(y_i - \alpha - \beta X_i)^2}{2\sigma_y^2} - \frac{(x_i - X_i)^2}{2\sigma_x^2}\right\}
= p(y|\alpha, \beta, X, \sigma_y)p(x|X, \sigma_x) \tag{11}$$ which we note
factors as shown. By Bayes' theorem,
$$p(\alpha, \beta | x, y, \sigma_x, \sigma_y) = \int d^n X p(\alpha, \beta, X | x, y, \sigma_x, \sigma_y)
= \int d^n X p(\alpha, \beta, X | \sigma_x, \sigma_y) \frac{p(x, y|\alpha, \beta, \sigma_x, \sigma_y)}{p(x, y|\sigma_x, \sigma_y)} \tag{12}$$and whether $\sigma_x, \sigma_y$ are known or unkwown, the solutions
will depend on the data only through their first and second moments,
which are sufficient statistics for $\alpha, \beta$. Introducing the
standard notations for the observed sample first and second moments,
$$\bar{x} = \frac{1}{n} \sum_{i=1}^n x_i, \quad \bar{y} = \frac{1}{n} \sum_{i=1}^n y_i, \tag{13}$$
$$\overline{x^2} = \frac{1}{n} \sum x_i^2, \quad \overline{xy} = \frac{1}{n} \sum x_i y_i, \quad \overline{y^2} = \frac{1}{n} \sum y_i^2, \tag{14}$$
and the sample central moments and correlation coefficient
$$s_{xx} = \overline{x^2} - \bar{x}^2, \quad s_{xy} = \overline{xy} - \bar{x}\bar{y}, \quad s_{yy} = \overline{y^2} - \bar{y}^2, \quad r = \frac{s_{xy}}{\sqrt{s_{xx} s_{yy}}}, \tag{15}$$
we note for later purposes that eventually all solutions involve the
fundamental quadratic form determined by the data
$$Q(\alpha, \beta) \equiv \frac{1}{n} \sum_{i=1}^n (y_i - \alpha - \beta x_i)^2
= C_{11}(\alpha - \hat{\alpha})^2 + 2C_{12}(\alpha - \hat{\alpha})(\beta - \hat{\beta}) + C_{22}(\beta - \hat{\beta})^2 + C_0 \tag{16}$$where the matrix $C$ is
$$C = \begin{pmatrix} 1 & \bar{x} \\\\ \bar{x} & \overline{x^2} \end{pmatrix} \tag{17}$$and the requirement that (16) be an identity in $\alpha, \beta$ uniquely
determines the coefficients: $$\begin{aligned}
\hat{\beta} &= s_{xy}/s_{xx} \\\\ 
\hat{\alpha} &= \bar{y} - \hat{\beta}\bar{x} \\\\ 
C_0 &= s_{yy} - s_{xy}^2/s_{xx} = s_{yy}(1-r^2). 
\end{aligned} \tag{18}$$ 
Of these, $\hat{\alpha}$ and $\hat{\beta}$ are just the original
least-squares estimates of $\alpha, \beta$ that one would make if the
errors were only in the $y_i$-measurmenents. But before reaching the
form $Q(\alpha, \beta)$, we have to integrate out the nuisance
parameters $X_1 \dots X_n$, and perhaps also $\sigma_x, \sigma_y$.
## THE ONE-POINT PROBLEM
To orient our thinking about this, consider first the 'baby' problem of
estimating $X_1$ given only the datum $x_1$. If $\sigma_x^2$ were known
and we had only the data component $x_1$, from (11) we would have
immediately for the posterior pdf for $X_1$:
$$p(X_1 | x_1, I) = A p(X_1|I) \exp\left[-\frac{(x_1 - X_1)^2}{2\sigma_x^2}\right] \tag{19}$$where here and what follows, $A$ always stands for a normalizing
constant, not necessarily the same in all equations. Suppose our prior
information had led us to estimate $X_1$ as about $x_0 \pm \delta$; we
could indicate this by the prior pdf
$$p(X_1|I) = \frac{1}{\sqrt{2\pi}\delta^2} \exp\left[-\frac{(X_1 - x_0)^2}{2\delta^2}\right] \tag{20}$$But we note that
$$\frac{(X_1 - x_0)^2}{\delta^2} + \frac{(x_1 - X_1)^2}{\sigma_x^2} = \frac{(X_1 - \bar{X}_1)^2}{\sigma^2} + (\text{const.}) \tag{21}$$where the (const.) is independent of $X_1$, and
$$\bar{X}_1 = \frac{x_0/\delta^2 + x_1/\sigma_x^2}{1/\delta^2 + 1/\sigma_x^2} \tag{22}$$
$$\frac{1}{\sigma^2} = \frac{1}{\delta^2} + \frac{1}{\sigma_x^2} \tag{23}$$whereupon (19) becomes
$$p(X_1|x_1,I) = \frac{1}{\sqrt{2\pi}\sigma^2} \exp\left[-\frac{(X_1 - \bar{X}_1)^2}{2\sigma^2}\right] \tag{24}$$We would estimate $X_1$ as (mean $\pm$ standard deviation)
$$(X_1)_{\text{est}} = \bar{X}_1 \pm \sigma \tag{25}$$ a weighted average of
the prior estimate $x_0$ and the datum $x_1$, weighted according to the
respective variances.

If we had almost no prior information about the unknown true value
$X_1$, then $\delta \gg \sigma_x$ and this would reduce for all
practical purposes to $(X_1)_{\text{est}} = x_1 \pm \sigma_x$. For
example, if $\delta > 10\sigma_x$, then the exact solution is within one
percent of this limiting value, and the prior information would hardly
help at all. But if we had prior information fixing $X_i$ to an
uncertainty comparable to $\sigma_x$, this would evidently be cogent,
enabling us to improve the accuracy of our estimates of $\alpha, \beta$.
This discussion of the 'baby' problem is to condition us to the usual
argument for passage to an improper prior, $\delta \to \infty$. Usually,
the data will be highly informative compared to our prior information
(indeed, data which tell us little that we did not know already, would be
hardly worth gathering). But if as usual our prior information is vague
compared to the accuracy of the data, then whether we keep the prior
with finite $\delta$ or pass to the limit of an improper prior,
$\delta \to \infty$, makes no difference in the results. This is the
conventional argument, surely valid for the simple problem being
considered.
## THE REAL PROBLEM
But note that the above passage to the limit is, in principle, to be
carried out only at the end of the calculation. In the real problem, the
properly normalized posterior distribution (5) is a ratio of two
integrals, (6) and (7), and if we want to approach an improper prior
it is the limit of the ratio, not the ratio of the limits, that should
be carried out according to the rules of probability theory. The former
limit is the well-behaved solution that we want; the latter may or may
not exist. Depending on how rapidly the likelihood factor cuts off away
from its peak, the separate integrals (6), (7) may diverge in the
limit.

In the integrations over $X_i$ it does not matter, because the Gaussian
factors guarantee convergence of the integrals. Then we may behave in a
rather reckless way and still get the right answer; but this is a rather
unfortunate accident, that encourages bad mathematical habits that will
fail on other similar-looking problems. For example, had we used a
Cauchy noise distribution $p(e_i) \propto (a^2+e_i^2)^{-1}$ instead of
the Gaussian (10), the limit of the ratio would still be a perfectly
well-behaved quantity, but the ratio of the limits would not exist. Our
present problem involves not only the safe integration over the $X_i$,
but also integration over $\sigma_x$ and $\sigma_y$, for which the limit
of the ratio continues to be well-behaved, but attempting to calculate
instead the ratio of the limits can get us into trouble.

Admittedly, the point we are making is quite trivial, since if one does
not see the distinction between the limit of a ratio and a ratio of the
limits, he cannot even grasp the concept of a derivative dy/dx.

Nevertheless, the recent literature of probability theory has examples
where the use of improper priors as limits of proper priors is rejected,
because well-known authors failed to perceive this trivial point and
tried to calculate the ratio of the limits instead of the limit of the
ratio. See, for example, our exchange with DSZ over the Marginalization
Paradox (Zellner, 1980).

Let us see how easy it is for the unwary to commit this error; but also
how easy it is to avoid once we understand the point. If we assign
uniform priors to the $X_i$ on the above grounds, and the Jeffreys
priors $d\sigma/\sigma$ to $\sigma_x, \sigma_y$, we may as noted
integrate $X_1 \dots X_n$ out of (11) without disaster, and this
constructs for us the quadratic form $Q(\alpha, \beta)$:
$$p(\alpha, \beta, \sigma_x, \sigma_y|x, y, I) = \frac{A}{(\sigma_x\sigma_y)(\sigma_y^2 + \beta^2\sigma_x^2)^{n/2}} \exp\left\{-\frac{nQ(\alpha,\beta)}{2(\sigma_y^2 + \beta^2\sigma_x^2)}\right\} \tag{26}$$and now we face the mathematical subtlety that is the real point of all
this discussion. If we try to get $p(\alpha, \beta|x, y, I)$ by
integrating out $\sigma_x, \sigma_y$ from this, the result diverges due
to the factor $(\sigma_x\sigma_y)^{-1}$, which expresses the Jeffreys
prior indicating ignorance of $\sigma_x, \sigma_y$.

But in (26) we have violated the rules of probablity theory by passing
to the limit of improper priors before doing the normalizing integral;
we are in effect trying to calculate the ratio of the limits. We got
away with this with the $X_i$, but not with the $\sigma_x, \sigma_y$.
Had we calculated the normalizing integral first for proper priors there
could have been no divergence; then passing to the limit of the improper
priors afterward would be a perfectly safe, uneventful procedure leading
to the useful result that we want.

In 1965, the writer did not yet perceive this and was carried along by
the arguments of Deming and Mandel, that the problem was indeterminate;
this led to a long comedy of errors which I have seen others repeating
many times since. My notebook entry of that time says: "This is
symptomatic of the fact that the data of the problem do not provide any
information at all about whether the errors are in x or in the y
measurement. Then supposing Deming's parameter $\lambda = \sigma_y/\sigma_x$
known, we can see whether this enables us to get a Bayesian solution;
instead of writing the joint prior proportional to $1/(\sigma_x\sigma_y)$, we
use
$$p(\sigma_x, \sigma_y|I) \propto \frac{\delta(\sigma_y - \lambda\sigma_x)}{\sigma_x} \tag{27}$$then integration over $\sigma_y$ merely makes the substitution
$\sigma_y = \lambda\sigma_x$, and it reduces to a convergent integral:
$$p(\alpha, \beta|x, y, I) = \frac{A}{(\lambda^2 + \beta^2)^{n/2}} \int_0^\infty \frac{d\sigma_x}{\sigma_x^{n+1}} \exp\left\{-\frac{nQ(\alpha, \beta)}{2(\lambda^2+\beta^2)}\right\}
= \frac{A}{Q(\alpha, \beta)^{n/2}} \tag{28}$$ which is just the bivariate
t-distribution that we would have had for the simpler regression problem
in which the errors are only in the y-measurement and $\sigma_y$ is
completely unknown. Then, for example, we can integrate out $\alpha$ to
get the posterior marginal pdf for $\beta$:
$$p(\beta|x, y, I) \propto [\gamma^2 + (\beta - \hat{\beta})^2]^{-(n-1)/2} \tag{29}$$where $\gamma^2 = s_{yy}(1-r^2)/s_{xx}$. As the initial pleasure at this
nice result wore off, a little warning bell started ringing in my mind
as it dawned on me that, unlike Deming's least squares result, (29) is
independent of $\lambda$. How can it be that the problem is
indeterminate if $\lambda$ is unknown; yet the solution when $\lambda$ is
known does not depend on $\lambda$?

A few years later, the answer suddenly seemed intuitively obvious.
Instead of supposing $\lambda$ known, make the change of variables
$(\sigma_x, \sigma_y) \to (\sigma, \lambda)$ in (26):
$$\sigma = \sqrt{\sigma_y^2 + \beta^2\sigma_x^2}, \quad \lambda = \sigma_y/\sigma_x \tag{30}$$The jacobian is
$$\frac{\partial(\sigma_x, \sigma_y)}{\partial(\sigma, \lambda)} = \frac{\sigma}{\lambda^2 + \beta^2} \tag{31}$$from which we find that the element of prior probability transforms as
$$\frac{d\sigma_x d\sigma_y}{\sigma_x \sigma_y} = \frac{d\lambda d\sigma}{\lambda \sigma} \tag{32}$$and (26) becomes
$$p(\alpha, \beta, \sigma, \lambda|x, y, I) = A \cdot \frac{d\lambda}{\lambda} \frac{d\sigma}{\sigma^{n+1}} \exp\left\{-\frac{nQ(\alpha, \beta)}{2\sigma^2}\right\} \tag{33}$$At the time, I drew the conclusion that $\lambda$ is completely
decoupled from the problem:
$$p(\alpha, \beta, \sigma, \lambda|x, y, I) = p(\lambda|x, y, I) p(\alpha, \beta, \sigma|x, y, I) \tag{34}$$so whatever prior we had assigned to $\lambda$ would just integrate out
again into a normalization constant, and contribute nothing to the final
result. The algebra now seems to tell us that, far from being
essential to make a determinate problem, $\lambda$ is completely
irrelevant to our problem! At least, from (33) it is clear how it can be
that integrating out $\lambda$ leads to divergence; yet supposing
$\lambda$ known leads to a result independent of $\lambda$.

The 'solution' which I offered at the 1973 Waterloo, Ontario meeting
(Jaynes, 1976) is then
$$p(\alpha, \beta|x, y, I) = \int_0^\infty p(\alpha, \beta, \sigma|I) d\sigma \propto Q(\alpha, \beta)^{-n/2}, \tag{35}$$the same as (28). But as the pleasure at this nice result wore off for
the second time, it dawned on me that $\lambda$ ought to be relevant to
the problem after all. The result (35) is identical with what everybody,
from Gauss on, had found for the case that $\sigma_x$ is known to be
zero; the measurement errors are only in y. In the opposite extreme,
where the errors are only in x, the roles of x and y ought to be
interchanged; but the quadratic form $Q(\alpha, \beta)$ is not a
symmetric function of $x_i$ and $y_i$. So where did I go wrong?

Let us go back to (33) and the conclusion we drew from it. Seeing only
(33), it appears that not only is $\lambda$ irrelevant to $\alpha, \beta$,
the data x, y tell us nothing about $\lambda$, for
$p(\lambda|x, y, I) = p(\lambda|I)$. That is what we meant by saying
that $\lambda$ is completely decoupled from the problem.

The error in this reasoning was that (33) was derived only in the case
of the Jeffreys prior (32); it has been shown thus far only that
$\lambda$ is decoupled for that prior. It turns out that exactly the
same error of interpretation generated the "marginalization paradox"
that was about to burst upon us (Dawid, et al, 1973; Jaynes, 1980). But
for a general prior $f(\sigma_x, \sigma_y)d\sigma_x d\sigma_y$ the
transformation would be, in place of (31),
$$f(\sigma_x, \sigma_y) d\sigma_x d\sigma_y = f(\sigma_x, \sigma_y) \frac{\sigma}{\lambda^2+\beta^2} d\lambda d\sigma \tag{36}$$Now the joint prior for $\lambda$ and $\sigma$ is
$$g(\lambda, \sigma) = \frac{\sigma}{\lambda^2 + \beta^2} f\left(\frac{\sigma}{\sqrt{\lambda^2 + \beta^2}}, \frac{\sigma\lambda}{\sqrt{\lambda^2 + \beta^2}}\right) \tag{37}$$which is in general very far from being decoupled!

But there is still another error in what we have done, which Steve Gull
recognized. We integrated out the $X_i$ with respect to independent
uniform priors on the grounds that our prior uncertainty $\delta$ is
large compared to $\sigma_x$ so its exact value does not matter
appreciably. Steve senses correctly that something is wrong here, but
fixes his attention on the matter of independence of the $X_i$. It is
true that if we have prior information making them logically related, we
should take this into account by a correlated prior, and this may enable
us to get better estimates of $\alpha, \beta$; but we think this is a
detail, not the crucial point.

The crucial point is that if we use any fixed prior for $X_i$, then as the
estimated line rotates we are expressing different states of knowledge
about the positions of the 'true' points $(X_i, Y_i)$ on it; and this is
true even in the limit where the prior is uniform. To see this most
clearly, suppose that instead of integrating out the $X_i$ we had
integrated out the $Y_i$ with respect to independent uniform priors. A
short calculation shows the surprising fact that we get a different
posterior pdf for $\alpha, \beta$:
**
But this is just the original Gauss solution for the case that
$\sigma_y = 0$; the errors are only in $x_i$. Merely by changing from a
prior uniform in $X_i$ to one uniform in $Y_i$ the roles of $x_i, y_i$
have somehow become interchanged. This is far more than we bargained
for; the conventional folklore which says that prior information does
not matter as long as the prior uncertainty is large compared to the
width of the likelihood function, is surely true in the conventional
situations one had in mind before; but now we see that the principle
needs to be stated more carefully in problems with many parameters.
The reasoning here is much like that for location parameters: our prior
information need not be translationally invariant, yet the likelihood
function for a location parameter will have an obvious translational
invariance; so a translationally invariant prior will lead to the
simplest final solution. This being the case, unless we have cogent
prior information which is not translationally invariant, it would be
foolish not to use a uniform prior (uniform, that is, over an interval
wide enough to include all the high likelihood region). Indeed, this
would be actively dishonest, in effect claiming to have more information
than we possess.

In our present problem, it is of course true that our prior information
need not be rotationally invariant. Indeed, even if x and y are
quantities of exactly the same kind, the mixture
$z = x\cos\theta + y\sin\theta$ may be without any meaning.

Nevertheless, in solving this problem we shall find ourselves dealing,
inevitably, with at least the mathematics of rotations in the x-y plane.
You can see from the beginning that this must be so, because with
Gaussian sampling distributions, only the second central moments of the
data will appear in the sufficient statistic. But the collection of all
those second moments forms a symmetric second rank tensor, and its
minimum eigenvalue is found by reduction to diagonal form, always
accomplished by a rotation of the coordinate axes. Therefore rotations
will appear naturally in the likelihood function whether or not our
prior information has rotational invariance. (In fact, we shall find a
rotational invariance property exactly analogous to the translational
invariance with a location parameter.)

This being the case, a rotationally invariant prior will lead to the
(analytically) simplest solution, so unless we have cogent prior
information which is not rotationally invariant, it will be prudent,
both for pragmatic and philosophical reasons, to use an invariant prior.
**
## REDUCTION OF THE RESULT
Examine the modified quadratic form that the mathematics led us to:
$$F(\alpha, \beta) \equiv \frac{Q(\alpha, \beta)}{1+\beta^2} = \frac{(s_{yy} - \beta^2 s_{xx}) + (\alpha - \hat{\alpha})^2 + 2\bar{x}(\alpha - \hat{\alpha})(\beta - \hat{\beta}) + \overline{x^2}(\beta - \hat{\beta})^2}{1+\beta^2} \tag{38}$$It is evident by inspection that this has a single unique minimum with
respect to $\alpha$; by differentiation we find this is reached when
$\alpha - \hat{\alpha} = -\bar{x}(\beta - \hat{\beta})$. So, keeping
$\alpha$ constantly fixed at this value, (38) reduces to
$$F(\beta) = \frac{(s_{xx} - \beta^2 s_{xx}) + s_{xx}(\beta - \hat{\beta})^2}{1+\beta^2} \tag{39}$$which looks quite complicated and unsymmetrical in terms of the
parameter $\beta$. But $\beta$ is a very unsymmetrical parameter; the
real sense of the modified quadratic form appears if we set
$\beta = \tan\theta$ and rewrite this in terms of the parameter
$\theta$. All the complications cancel out, and it reduces magically to
the standard form
$$F(\beta) = S(\theta) = s_{xx} \sin^2\theta - 2s_{xy} \sin\theta \cos\theta + s_{yy} \cos^2\theta \tag{40}$$which we recognize as a second rank tensor element $s^\prime_{yy}$ in a
coordinate system (x', y') rotated an angle $\theta$ from the original one.
Separating off the rotationally invariant part, this becomes
$$S(\theta) = \frac{1}{2}(s_{xx} + s_{yy}) + \frac{1}{2}(s_{xx} - s_{yy}) \cos 2\theta - s_{xy} \sin 2\theta \tag{41}$$To find the maxima and minima of this, define an angle $\phi$ by
$$\left\{ \begin{aligned}
 s_{xy} &= R \sin\phi \\\\ 
\frac{1}{2}(s_{xx} - s_{yy}) &= R \cos\phi
\end{aligned} \right. \quad (-\pi < \phi \le \pi) \tag{42}$$ or,
$$\begin{aligned}
\tan\phi &= \frac{2s_{xy}}{s_{xx}-s_{yy}} \\\\ 
2R &= \sqrt{(s_{xx}-s_{yy})^2 + 4s_{xy}^2} \ge 0
\end{aligned} \tag{43}$$ Note that this defines the branch of the function so
that $\phi$ has the same sign as $s_{xy}$, and if $s_{xx} > s_{yy}$, then
$|\phi| < \pi/2$, otherwise $\pi/2 \le |\phi| \le \pi$. Now we have
simply
$$S(\theta) = \frac{1}{2}(s_{xx}+s_{yy}) - R \cos(2\theta - \phi) \tag{44}$$ so
the minimum is reached at $\theta = \theta_0 = \phi/2$, the maximum at
right angles, $\theta = \theta_0 \pm \pi/2$. If the prior for $\alpha, \beta$
is rotationally invariant, we shall then estimate $\beta$ as $\tan(\phi/2)$;
now let us determine the accuracy of that estimate. Whatever the prior, the
quasi-likelihood function, which contains all the information the
data have to give us about $\theta$, is now
$$L(\theta) = \left[\frac{1}{S(\theta)}\right]^{n/2} \tag{45}$$ 
**
But although the algebra tells us this, can we understand it intuitively
in a way that makes it obvious from the start? Yes, and in fact the
solution to a more general problem than the one just discussed is
equally obvious, if we look at this way. Each data point has some error
which may be in either x, or y, or both. But if we make the estimates
$\hat{\alpha}, \hat{\beta}$, then the component of error parallel to
that line contributes nothing to the error in our estimate of either
$\alpha$ or $\beta$. Only the component of error perpendicular to the
estimated line matters.

Now an error vector $(e_i, f_i)$ has components parallel and
perpendicular to a regression line of slope $\beta = \tan\theta$ of
$$e_i \cos\theta + f_i \sin\theta = \frac{e_i + \beta f_i}{\sqrt{1+\beta^2}}, \quad -e_i\sin\theta + f_i\cos\theta = \frac{-\beta e_i + f_i}{\sqrt{1+\beta^2}} \tag{46}$$respectively. But these have mean square values of
$$\frac{\sigma_x^2 + \beta^2\sigma_y^2}{1+\beta^2}, \quad \frac{\sigma_y^2 + \beta^2\sigma_x^2}{1+\beta^2} \tag{47}$$respectively. Therefore the quantity $\sigma^2 = \sigma_y^2 + \beta^2\sigma_x^2$
generated by our integration over the $X_i$ was, essentially, just the
mean square value of the perpendicular component of error.

Recognizing this, it is clear that we need not have considered
independent sampling probabilities for $e_i, f_i$; whether the errors are
in x, in y, or in both; and whatever the shape or orientation of the
concentration ellipse, only the perpendicular component of the error can
matter and we shall be led to the same result. The algebra, once we learn
how to state the problem correctly, gives us this result so fast it seems
like magic.
## PRIOR PROBABILITIES AND TRANSFORMATION GROUPS
The transformation group principle for assigning priors in the
regression problem is quite simple. Given the straight line equation
$y = \alpha + \beta x$ with a prior probability element
$$f(\alpha, \beta) d\alpha d\beta \tag{48}$$we formulate Problem P:
Given a data set $D = \{(x_1, y_1) \dots (x_n, y_n)\}$, estimate $\alpha$
and $\beta$. Now consider a related problem: carry out a linear
coordinate transformation $(x, y) \to (x^\prime, y^\prime)$ such that in the new
variables (48) takes the form $$y^\prime = \alpha^\prime + \beta^\prime x^\prime \tag{49}$$with a
prior probability element $$g(\alpha^\prime, \beta^\prime) d\alpha^\prime d\beta^\prime \tag{50}$$and consider Problem P':
Given a data set $D^\prime = \{(x^\prime_1, y^\prime_1) \dots (x^\prime_n, y^\prime_n)\}$, estimate $\alpha^\prime$ and $\beta^\prime$. Now if the two priors (48), (50) express
the same prior information, it must be true that
$$f(\alpha, \beta) d\alpha d\beta = g(\alpha^\prime, \beta^\prime) d\alpha^\prime d\beta^\prime \tag{51}$$or,
$$f(\alpha, \beta) = g(\alpha^\prime, \beta^\prime) \frac{\partial(\alpha^\prime, \beta^\prime)}{\partial(\alpha, \beta)} \tag{52}$$This transformation equation tells how the two problems are related to
each other, and it will hold whatever linear transformation we carry
out, and whether or not we consider the problems P, P' to be equivalent.
But now suppose that our prior information is invariant under the
transformation. For example, if x is the distance from our present
location to some origin of whose location we know nothing, then after
the transformation x' = x+a, of walking a distance a, we are in the
same state of ignorance; ignorance of one's location is a state of
knowledge which is not changed by a small change in that location.
**[TRUNCATED: The original draft contains multiple place-holders and ends abruptly.]**
## REFERENCES
Bretthorst, G. L. (1988), *Bayesian Spectrum Analysis and Parameter
Estimation*, Lecture Notes in Statistics, Vol. 48, Springer-Verlag,
Berlin.
Cramér, H. (1946), *Mathematical Methods of Statistics*, Princeton
University Press.
Dawid, A. P., Stone, M. & Zidek, J. V. (1973), "Marginalization
Paradoxes in Bayesian and Structural Inference", *J. Roy Stat. Soc.
B35*, pp. 189--233.
Deming, W. E. (1943), *Statistical Adjustment of Data*, J. Wiley, New
York.
de Groot, M. H. (1985), *Probability and Statistics*, 2nd Edition,
Addison-Wesley Pub. Co., Reading MA.
Graybill, F. A. (1961), *An Introduction to Linear Statistical Models*,
Mc Graw-Hill Book Co., New York.
Gull, S. F. (1989), "Bayesian Data Analysis: Straight Line Fitting", in
*Maximum Entropy and Bayesian Methods*, J. Skilling, Editor, Kluwer
Academic Publishers, Holland.
Isobe, T., Feigelson, E. D., Akritas, M. G. & Babu G. J., (1990),
"Linear Regression in Astronomy", *Astrophys. Jour.* Nov 20.
Jaynes, E. T. (1980), "Marginalization and Prior Probabilities", in
*Bayesian Analysis in Econometrics and Statistics*, A. Zellner, Editor,
North-Holland Publishing Co., Amsterdam. Reprinted in Jaynes (1983).
Jaynes, E. T. (1986), "Bayesian Methods: General Background", in
Proceedings of the Workshop on Bayesian/Maximum Entropy methods in
Geophysical inverse problems, Calgary, Canada, August 1984; J. H.
Justice, Editor, Cambridge University Press.
Jaynes, E. T. (1987) "Bayesian Spectrum and Chirp Analysis", in
*Maximum Entropy and Bayesian Spectral Analysis and Estimation
Problems*, C. R. Smith & G. J. Erickson (editors), D. Reidel Publishing
Company, Holland; pp. 1--37.
Kendall, M. G. & Stuart, A. (1961), *The Advanced Theory of Statistics:
Volume 2, Inference and Relationship*, Hafner Publishing Co., New York.
Kempthorne, O. & Folks, L. (1974), *Probability, Statistics, and Data
Analysis*, Iowa State University Press, Ames IA.
Mandel, J. (1964), *The Statistical Analysis of Experimental Data*,
Interscience, New York. Straight orthodox adhockeries, one of which is
analyzed in Jaynes (1976).
Sokal, R. R. & Rohlf, J. J. (1981), *Biometry: The Principles and
Practice of Statistics in Biological Research*, 2nd edition, W. H.
Freeman & Co., San Francisco.
Strömberg, G. (1940), *Astrophys. J. 92*, 156.
Wald, A. (1940), "The fitting of straight lines if both variables are
subject to error" *Ann. Math. Stat. 11*, 284-300.
Zellner, A. (1971), *An Introduction to Bayesian Inference in
Econometrics*, J. Wiley & Sons, Inc., New York. Second printing (1987);
R. E. Krieger Pub. Co., Malabar, Florida.
Zellner, A. (editor, 1980), *Bayesian Analysis in Econometrics and
Statistics*, North-Holland Publishing Co.
