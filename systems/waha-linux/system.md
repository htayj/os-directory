---
type: Operating System
title: "واحــة لينكس"
description: Draft multilingual inventory record for واحــة لينكس.
tags: [operating-system, multilingual-discovery]
status: draft
schema_version: "0.1"
as_of: 2026-07-26
catalog_completeness: { level: inventory, note: "Draft coverage record; no verified claim is asserted." }
field_dispositions:
  # BEGIN GENERATED TEXT EDITOR DISPOSITION
  - { field: text_editors, disposition: no-evidence-found, checked_at: 2026-07-26 }
  # END GENERATED TEXT EDITOR DISPOSITION
  - { field: organizations, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: countries_of_origin, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: design_purposes, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: lifecycle_events, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: rights_regime, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: licenses, disposition: no-evidence-found, checked_at: 2026-07-26 }
  - { field: programming_languages, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: system_organization, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: interfaces, disposition: not-researched, checked_at: 2026-07-26 }
  - { field: architectures, disposition: not-researched, checked_at: 2026-07-26 }
discovery_provenance:
  - { method: multilingual-manifest, language: ar, native_label: "واحــة لينكس", source: inventory/multilingual/manifests/batch-001.json, observed_at: 2026-07-26, disposition: included-system }
names:
  - { value: "واحــة لينكس", kind: official, language: ar, script: Arab, evidence: [multilingual-manifest], assertion_status: provisional }
countries_of_origin: []
first_pass_attributes:
  developer: null
  country_of_origin: null
  purpose: null
  programming_languages: null
  first_release: null
  latest_release: null
  last_updated: null
  development_status: null
  source_model: null
  os_family: null
  gui: null
  platforms: null
  kernel_type: null
  license: null
first_pass_attribute_dispositions:
  developer: not-researched
  country_of_origin: not-researched
  purpose: not-researched
  programming_languages: not-researched
  first_release: not-researched
  latest_release: not-researched
  last_updated: not-researched
  development_status: not-researched
  source_model: not-researched
  os_family: not-researched
  gui: not-researched
  platforms: not-researched
  kernel_type: not-researched
  license: no-evidence-found
sources:
  - { id: multilingual-manifest, resource: "inventory/multilingual/manifests/batch-001.json", title: "Multilingual catalog batch 001", source_kind: inventory-manifest }
  - { id: arabeyes-distros, resource: "https://www.arabeyes.org/index.php?title=Distros&oldid=82007", title: "Distros", source_kind: arabic-community-project-history }
  - { id: arabeyes-arabbix, resource: "https://wiki.arabeyes.org/Arabbix", title: "Arabbix", source_kind: arabic-community-project-history }
  - { id: waha-project, resource: "https://wahaproject.org/", title: "مشروع واحــة", source_kind: arabic-project-site }
  - { id: waha-linux, resource: "https://linux.wahaproject.org/", title: "واحــة لينكس", source_kind: arabic-project-site }
  - { id: ojuba-project, resource: "https://ojuba.org/linux:%D8%A7%D9%84%D8%B1%D8%A6%D9%8A%D8%B3%D8%A9", title: "نظام التشغيل أعجوبة لينكس", source_kind: arabic-project-site }
  - { id: ojuba-releases, resource: "https://ojuba.org/ojuba-releases", title: "ojuba-releases", source_kind: arabic-project-release-policy }
  - { id: helwan-project, resource: "https://helwan-linux.github.io/helwanlinux/about.html", title: "About Helwan Linux", source_kind: project-site }
  - { id: uruk-article, resource: "https://en.wikipedia.org/wiki/Uruk_GNU/Linux", title: "Uruk GNU/Linux", source_kind: article }
  - { id: kfupm-arabian-linux, resource: "https://faculty.kfupm.edu.sa/ICS/muhtaseb/Teaching/ACStLect.pdf", title: "Arabian Linux", source_kind: arabic-university-course-material }
  - { id: hilali-community, resource: "https://www.linuxac.org/node/84", title: "توزيعة هلال Helal لينُكس العربية", source_kind: arabic-community-archive }
  - { id: sabily-ubuntu, resource: "https://wiki.ubuntu.com/DerivativeTeam/Derivatives/Sabily", title: "Sabily derivative record", source_kind: upstream-project-wiki }
# BEGIN GENERATED MULTILINGUAL WIKIDATA
multilingual_wikidata_snapshot:
  candidate_id: waha-linux
  wikidata_entity: null
  source: null
  assertion_status: unknown
  note: Discovery metadata from Wikidata statements. It is not independently verified
    and does not replace native or primary-source research.
  fields: {}
  retrieved_at: '2026-07-26'
# END GENERATED MULTILINGUAL WIKIDATA
# BEGIN GENERATED TEXT EDITORS
text_editor_research:
  inventory: /inventory/text-editor-associations.json
  checked_at: '2026-07-26'
  disposition: no-evidence-found
  note: No editor relationship was found in the linked Wikipedia page or direct Wikidata
    text-editor platform statements; primary manuals and distribution manifests still
    require research.
text_editors: []
# END GENERATED TEXT EDITORS
# BEGIN GENERATED DEEP RESEARCH
deep_research:
  batch_id: wave-001-batch-003
  researcher: deep_commercial_001
  researched_at: '2026-07-27'
  identity_status: confirmed
  research_summary: Waha Linux is an Arabic-localized, independently operated Debian-based GNU/Linux distribution.
    Its Arabic project documentation states goals of bringing GNU/Linux and free/open-source programs
    to Arabic users, including users without network access, while retaining freedom to use, modify, and
    distribute. The official download/news pages document Waha 11.0 (Iṣrār) as the presented stable release,
    but do not publish an exact distribution license, a development-location statement, an implementation-language
    account, or a current maintenance commitment.
  sources:
  - id: waha-home-ar
    title: واحــة لينكس – توزيعة جنو / لينكس عربيّة سهلة الاستخدام
    url: https://linux.wahaproject.org/
    archived_url: null
    source_kind: official-project-page
    language: ar
    date: '2026'
    primary: true
    notes: Arabic project home page describing Waha as an easy-to-use Debian-based GNU/Linux distribution,
      available in 32-bit and 64-bit editions.
  - id: waha-faq-ar
    title: الأسئلة الشائعة – واحــة لينكس
    url: https://linux.wahaproject.org/faq/
    archived_url: null
    source_kind: official-faq
    language: ar
    date: '2026'
    primary: true
    notes: Arabic FAQ states that Waha is a localized Debian derivative and an independent project operationally
      separate from Debian.
  - id: waha-download-ar
    title: التنزيل – واحــة لينكس
    url: https://linux.wahaproject.org/download/
    archived_url: null
    source_kind: official-download-page
    language: ar
    date: '2023'
    primary: true
    notes: Official Arabic download page describes Waha 11.0, code-named إصرار, as the stable release
      and names Linux 5.10 and GNOME 3.38.
  - id: waha-11-news-ar
    title: إصدار واحــة لينكس 11.0 إصرار
    url: https://linux.wahaproject.org/category/news/
    archived_url: null
    source_kind: official-release-news
    language: ar
    date: '2023-04-13'
    primary: true
    notes: Arabic project news index records the Waha 11.0 announcement, based on Debian 11.6.
  claims:
  - field: organizations
    value:
      organization: مشروع واحــة (Waha Project)
      role: project operator and distributor
    source_ids:
    - waha-home-ar
    - waha-faq-ar
    assertion_status: documented
    source_term: مشروع واحــة
    scope:
      releases:
      - Waha Linux 11.0
    locator: Project home page, project-goal text; FAQ, project relationship to Debian
    evidence_note: The Arabic project pages describe Waha's stated goals and say the distribution is an
      independent project operationally separate from Debian.
  - field: design_purposes
    value:
      purpose: Arabic-localized general-purpose desktop distribution
      primary: true
      source_term: تقريب نظام جنو/لينكس والبرامج الحرّة/مفتوحة المصدر للمستخدم العربي
    source_ids:
    - waha-home-ar
    assertion_status: documented
    source_term: easy-to-use Arabic GNU/Linux distribution
    scope:
      releases:
      - Waha Linux
    locator: Project home page, هدف المشروع
    evidence_note: The Arabic project statement says the project brings GNU/Linux and free/open-source
      programs closer to Arabic users through a modern, integrated, easy-to-use system, including for
      users without a network connection.
  - field: lifecycle_events
    value:
      event: release
      date: '2023-04-13'
      release: Waha Linux 11.0 (إصرار)
    source_ids:
    - waha-11-news-ar
    - waha-download-ar
    assertion_status: documented
    source_term: إصدار واحــة لينكس 11.0 إصرار
    scope:
      releases:
      - Waha Linux 11.0
    locator: Official news index entry dated 2023-04-13; official download page
    evidence_note: The project news page announces Waha 11.0 and the download page presents it as the
      stable release.
  - field: system_organization
    value:
      organization: distinct-kernel
      source_term: توزيعة مبنية على دبيان
    source_ids:
    - waha-home-ar
    - waha-download-ar
    assertion_status: inferred
    source_term: Debian-based GNU/Linux distribution; Linux 5.10
    scope:
      releases:
      - Waha Linux 11.0
    locator: Project home page; download page, release component list
    evidence_note: The source calls Waha a Debian-based GNU/Linux distribution and names its Linux kernel
      version. The vocabulary classification is an explicit inference from that documented distribution/kernel
      relationship.
  - field: kernels
    value:
      name: Linux
      version: '5.10'
      architecture: unknown
    source_ids:
    - waha-download-ar
    assertion_status: documented
    source_term: نواة لينكس 5.10
    scope:
      releases:
      - Waha Linux 11.0
    locator: Download page, Waha 11.0 component list
    evidence_note: The Arabic release page explicitly lists the Linux 5.10 kernel for Waha 11.0 but does
      not classify its kernel architecture.
  - field: interfaces
    value:
      name: GNOME
      version: '3.38'
      style: graphical
      provisioning: bundled-default
      access: local-session
    source_ids:
    - waha-download-ar
    assertion_status: documented
    source_term: واجهة جنوم 3.38
    scope:
      releases:
      - Waha Linux 11.0
    locator: Download page, Waha 11.0 component list
    evidence_note: The project lists GNOME 3.38 as the Waha 11.0 desktop interface.
  - field: platforms
    value:
      platform: 32-bit and 64-bit editions
      support_origin: original-target
      execution_mode: native
    source_ids:
    - waha-home-ar
    - waha-download-ar
    assertion_status: documented
    source_term: 32 بت و64 بت
    scope:
      releases:
      - Waha Linux 11.0
    locator: Project home page; download page
    evidence_note: The Arabic project documentation explicitly advertises both 32-bit and 64-bit editions;
      it does not identify an ISA beyond those edition labels.
  editor_associations: []
  unresolved:
  - field: countries_of_origin
    disposition: no-evidence-found
    reason: Arabic-language audience and localization goals do not establish the geographical location
      of original development or project operation.
    source_ids:
    - waha-home-ar
    - waha-faq-ar
  - field: development_status
    disposition: unknown
    reason: The live project site still presents Waha 11.0 as stable, but the consulted pages do not state
      whether the project is actively developing, in maintenance, or discontinued after its 2023 announcement.
    source_ids:
    - waha-download-ar
    - waha-11-news-ar
  - field: rights_regime
    disposition: no-evidence-found
    reason: The project commits to user freedom to use, modify, and distribute and calls its software
      free/open source, but it does not provide a license inventory or enough material to characterize
      the entire distribution's legal regime.
    source_ids:
    - waha-home-ar
    - waha-faq-ar
  - field: licenses
    disposition: no-evidence-found
    reason: No consulted official Arabic page identifies a Waha distribution license or component-license
      manifest.
    source_ids:
    - waha-home-ar
    - waha-download-ar
  - field: programming_languages
    disposition: no-evidence-found
    reason: The distribution and release pages document included components, not the implementation language(s)
      of Waha-specific software or the distribution as a whole.
    source_ids:
    - waha-download-ar
    - waha-faq-ar
  - field: text_editors
    disposition: no-evidence-found
    reason: The release page lists desktop applications such as LibreOffice but no plain-text editor with
      a documented Waha relationship; a word processor is not treated as a text-editor association here.
    source_ids:
    - waha-download-ar
# END GENERATED DEEP RESEARCH
---

# واحــة لينكس

Arabic-facing Linux distribution; detailed technical attributes remain unresearched.
