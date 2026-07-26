---
type: Catalog Schema
title: Graphical-environment record
description: Defines identity, layering, interface, and application-model fields for historical desktop and operating environments.
tags: [schema, graphical-environment, desktop-environment, user-interface]
status: stable
generated: { by: codex/gpt-5, at: "2026-07-26T14:51:53-04:00" }
---

# Scope

Catalog a graphical environment separately when it has a distinct name,
release history, developer, application/interface contract, or preservation
history. Use the narrowest accurate `type`:

* `Graphical Operating Environment`
* `Desktop Environment`
* `Window System`
* `Display Server`
* `Workspace Manager`
* `User Interface Shell`

Marketing language does not decide the type. Determine what services the
product supplies, what host it requires, and whether applications target the
host OS, the environment, or both.

# Core Information

Every record supplies or explicitly disposes:

1. Names, developer, country of origin, purpose, and intended audience.
2. First and latest release, lifecycle state, rights, and license.
3. Accurate environment kind and host-system boundary.
4. Interface style, input model, visual paradigm, and window behavior.
5. Display architecture, desktop/shell components, and file/session management.
6. Native application model, API/toolkit, bundled applications, and data
   exchange.
7. Programming languages and supported hardware platforms.
8. Distribution, surviving media/source/manuals, emulation, and known gaps.

# Relationship to Operating Systems

Link each environment to host systems with `host_systems`. Link an operating
system back through `desktop_environments`, `window_systems`, or `interfaces`.
State whether the environment was bundled, optional, separately sold, or
third-party.

An environment that requires MS-DOS is not cataloged as an independent OS.
Conversely, an OS with an integral GUI still has a separate environment concept
when that GUI has an independently meaningful identity or release history.

# Expected Body Sections

* **Overview**
* **Purpose and Design**
* **History and Releases**
* **Host Systems and Platforms**
* **Interface and Visual Model**
* **Application Architecture**
* **Licensing and Distribution**
* **Preservation**
* **Open Questions**
