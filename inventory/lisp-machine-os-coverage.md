---
type: Inventory
title: Lisp-machine operating-system coverage
description: Machine-to-system-software audit for every family explicitly listed by the Computer History Wiki LISP-machine page.
tags: [inventory, lisp-machine, operating-system, multilingual]
status: active
generated: { by: codex/gpt-5, at: "2026-07-29T00:00:00-04:00" }
---

# Coverage rule

The machine list is a discovery source, not proof that every named software
environment is an operating system. The structured
[coverage inventory](lisp-machine-os-coverage.json) records whether a documented
system is cataloged, no separate OS is established, an integrated language
environment remains unclassified, or a backend processor's host OS is unresolved.

# Cataloged lineages

* [MIT Lisp Machine system software](/systems/mit-lisp-machine-system-software/)
  for the CONS/CADR lineage.
* [LMI Lisp Machine Software](/systems/lmi-lisp-machine-software/) for Series III
  and Lambda.
* [Genera](/systems/genera/) for Symbolics machines.
* [Explorer System Software](/systems/explorer-system-software/) for TI Explorer.
* [Alto Executive](/systems/alto-executive/) and
  [Interlisp-D/Medley](/systems/interlisp-d-medley/) for the layered Xerox
  workstation environment.

# Japanese machines

TAKITAC-7/FAST LISP, EVLIS, ELIS/TAO, FACOM α, and LIME remain in the
structured inventory even where no independent OS identity has been established.
This prevents both omission and false promotion of an interpreter, language
environment, or host-attached accelerator into the operating-system table.
