---
title: "You CAN Parallel Storage Batteries"
year: 1968
abstract: >
  Jaynes explains how high-amperage solid-state rectifiers make it practical to
  parallel wet cell storage batteries for increased ampere-hour capacity. He
  describes a diode bridge circuit that prevents damaging circulating currents
  between batteries while allowing them to be charged simultaneously and to
  supply current to a common load.
author: ["E.T. Jaynes"]
categories: ["Electrodynamics & Signal Processing"]
tags: ["storage batteries", "diodes", "circulating current", "parallel connection", "battery charging"]
---
UNTIL high-amperage solid-state rectifiers became commonly available, it
was not practical to parallel wet cell storage batteries. The slightest
difference in the open-circuit voltages of parallel-connected batteries
will set up a circulating current whereby the battery with the greater
voltage will tend to charge the one with the lesser voltage. This
circulating current is capable of damaging both batteries.
**[FIGURE: Diodes D1, D2, D3, and D4 prevent circulating current loops from being set up between batteries A and B when the batteries are connected in parallel.]**
When the solid-state rectifier came along, it became practical to
parallel storage batteries for increased ampere-hour capacity without
setting up a circulating current loop. If, for example, diodes
D1, D2, D3, and D4 are connected in a parallel circuit containing
two batteries as shown in the schematic diagram, potential differences
between the batteries cannot cause an appreciably large current to
circulate. The little current that does circulate with the
reverse-biasing of D1 through D4 is generally on the order of a few
milliamperes.

The diodes form a bridge circuit, allowing a battery charger to charge
both batteries through D1 and D2. Batteries A and B deliver current
through D3 and D4, respectively, to the load. And, because D1-D2
and D3-D4 are connected back-to-back, the possibility of a
circulating current loop being set up is overcome. Both batteries,
however, will still supply current to the load.

If more than two batteries are to be connected in parallel, another pair
of diodes (connected as shown for D2 and D4) must be used with each
additional battery. Be sure that the PIV and current ratings of the
diodes are sufficient for the potentials and currents that must be
handled. For example, if you want to charge a 12-volt battery at 10
amperes and have a 10-ampere drain by the load, the diodes you use would
have minimum 25-volt PIV and 10-ampere ratings. (Radio Shack's Stock No.
276-1060 stud-mounted diodes, with 50-PIV and 12-ampere ratings, will
suffice for most applications. These diodes sell for 59 cents each.)
When two or more batteries are to be used independently (as for mobile
CB or ham radio) but charged from a single generator or battery charger,
diodes D3 and D4 should be eliminated and the connections from D1
and D2 should be used as the "hot" lines for two separate circuits.
The interesting feature of the arrangement shown is that during
recharging the weaker battery will receive the lion's share of the
charge current. Conversely, the battery with the greater charge will
deliver the greater amount of current to the load without interactions.
It isn't often that nature cooperates so nicely to bring about the most
desirable conditions.