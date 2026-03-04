---
title: "The Concept and Measurement of Impedance in Periodically Loaded Wave Guides"
year: 1952
abstract: >
  A generalization of ordinary circuit theory which enables one to
  define impedances in any periodic structure is developed, based on the
  concept of expansion of electromagnetic fields in terms of a set of
  linearly independent basis fields. Techniques for measurement of
  impedances in a periodic structure are described, involving a
  determination of the parameters of a coupling system by an extension
  of the well-known nodal shift method.
author: ["E.T. Jaynes"]
---
## INTRODUCTION
In a coupling system connecting two different transmission lines or wave
guides[^2] it is usually desired that a matched line on the load side be
reflected through the coupling system as a match in the input
transmission line. The obvious way to test for this is to install a
matched load and then measure the input SWR. However, an accurate match
may be very difficult to obtain; or if the output transmission line
happens to be of some special construction, such as the periodically
disk-loaded wave guides used in particle accelerators, there may be no
independent method of determining when the load line is matched, other
than looking at it through some coupling system.

It is always easy, however, to produce a pure reactance (i.e.,
completely reflecting) termination of the load line, and if the coupling
system is lossless, its input impedance must also be a pure reactance.
This reactance is determined merely by locating the position of the
extremely sharp node on the input transmission line, so that if we can
find a way of determining the coupling system parameters from the
relation of load reactance to input reactance, we can expect this method
to give us a more convenient as well as more accurate determination of
the coupling system performance. Once the parameters of the coupling
system are known, the relations between its input and output impedance
may be used backwards to measure impedances in the load transmission
system.

In Sec. II we review the well-known theory of the nodal shift method as
applied to "smooth" transmission lines. Sections III, IV, and V are
devoted to developing the concept of impedance in periodically loaded
wave guides, and in Sec. VI the theory of the nodal shift method is
extended to such guides. The resulting measurement technique was
developed and used by the writer in 1949 in connection with the design
of coupling systems for the Stanford linear accelerator tubes.[^3]

## NODAL SHIFT THEORY
First, we note the familiar fact that the voltage-current relationships
of any linear, passive, four-terminal network may be expressed in terms
of the network parameters $A, B, C, D$, in the form (see Fig. 1 for
notation)
$$
\begin{aligned}
V_1 &= AV_2 + BI_2, \\
I_1 &= CV_2 + DI_2, \\
\begin{vmatrix}
A & B \\
C & D
\end{vmatrix} &= 1.
\end{aligned}
$$
