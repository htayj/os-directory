---
type: Catalog Policy
title: Scope and identity
description: Defines the catalog's subject boundaries and rules for distinguishing systems, releases, and artifacts.
tags: [methodology, identity, scope]
status: stable
generated: { by: codex/gpt-5, at: "2026-07-26T14:51:53-04:00" }
---

# Scope

The catalog covers historical operating systems and closely related system
software when that context is necessary to understand an operating system.
Historical does not require that a system be extinct: a historically important
version of a continuing lineage is in scope.

# Units of Description

Use distinct concepts for distinct things:

* **Operating System** describes a named software lineage or system identity.
* **Operating System Release** describes a particular release, version, edition,
  dated state, or vendor distribution.
* **Software Artifact** describes a concrete surviving object: an installation
  image, disk or tape dump, source snapshot, binary set, listing, or preserved
  machine state.
* **Organization** describes a company, university, laboratory, project group,
  standards body, or other responsible institution.
* **Hardware Platform** describes a machine family, model, or architecture.
* **Historical Source** describes evidence such as a manual, archive, source
  tree, advertisement, oral history, or scholarly work.

A release title is not an artifact identity. Multiple artifacts may preserve
the same release, and one artifact may contain several releases or components.
Likewise, a later reimplementation or emulator is not the historical operating
system it reproduces.

# Identity Rules

Create a separate operating-system record when the evidence supports a distinct
name or lineage recognized by its contemporary developers or users. Represent
renames, forks, ports, predecessors, and successors with links and prose; do not
collapse them solely because they share code.

Create a separate release record when a version, edition, target platform, or
distribution has claims that must be sourced independently. Do not invent a
release boundary from an undated artifact.

Create a separate artifact record whenever provenance, checksum, custody,
format, completeness, or access restrictions differ.

# Uncertainty

Prefer explicit uncertainty over forced normalization:

* State whether a date is exact, approximate, inferred, or disputed.
* Preserve the source's terminology and explain any normalized name.
* Record conflicting claims with per-claim source footnotes.
* Use `status: draft` while identity or scope remains unresolved.
* Never mark a concept `verified` merely because its YAML is valid.
