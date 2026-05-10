# Changelog

All notable changes to this template will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [3.17.0] - 2026-05-09

**Theme**: Aligned with framework v3.17.0 (Theme C3 — Canonical Coherence + Structural Self-Conformance)

### Changed

- Version bump: 3.16.0 → 3.17.0 (framework alignment)
- `AGENTS.md` `@aget-version` updated to 3.17.0
- Inherits framework v3.17.0 deliverables: framework-manager archetype formalization (Q4=A.2 disposition); T2.18 SOP_scope_lock_ceremony LANDED v1.0.0; T2.19 AGET_SKILL_LIFECYCLE_SPEC LANDED v1.0.0 with full V-test authoring; T2.20 AGET_FLEET_UPGRADE_SPEC v0.1 DRAFT; T2.23 AGET_TASK_ROUTING_SPEC v0.1 DRAFT.
- CAP-REL-030 + CAP-REL-031 (post-release CHANGELOG + tag validators) IMPLEMENTED (closes v3.16 sleeping CAPs); CAP-REL-032 + CAP-REL-033 grace-extended to v3.18.0 per Q1=B disposition.

### Compatibility

- **No breaking changes** in v3.17. Existing instances upgrade by version-bump only.
- Optional adoption: `framework-manager` archetype field in `.aget/identity.json`; existing `archetype` values continue to function.

---

## [3.16.0] - 2026-05-02

**Theme**: Aligned with framework v3.16.0 (Framework-Discipline Closure + Wave-1A Spec Contracts + /aget-go Production)

### Changed

- Version bump: 3.15.0 → 3.16.0 (framework alignment)
- `AGENTS.md` `@aget-version` updated to 3.16.0
- **Universal-skills migration (#1120)**: 15 missing universal skills added from worker baseline (advisor/analyst/architect/consultant/developer/executive/operator/researcher/reviewer/spec-engineer pre-bump count 19 → post-migration 34, then post-archetype-fit-revert 31 = 29 universal + 2 archetype-specific).
- **Release-triad revert (CAP-TPL-016-07 NEW)**: 3 release-triad skills (`aget-release-build`, `aget-release-audit-specs`, `aget-release-critique`) removed from this template — moved to release-execution archetype catalog (worker, supervisor only). Closes the "presence-not-fit" misfit surfaced by Gate 1 defects audit.

### Compatibility

- **No breaking changes** in v3.16. Existing instances upgrade by version-bump only.
- Optional adoption: `**Plan_Status**:` / `**Gate_Status:**` schema in new PROJECT_PLAN files (CAP-PP-003 disambiguation; backward-compatible).

---

## [3.15.0] - 2026-04-25

**Theme**: Aligned with framework v3.15.0 (Two-Level Model Coherence + Security Hardening)

### Changed

- Version bump: 3.14.0 → 3.15.0 (framework alignment)
- `AGENTS.md` `@aget-version` updated to 3.15.0

### Breaking

- **BC-001**: `.aget/version.json` old field names removed (e.g. `agent_name` → `aget_agent_name`). See `aget/docs/BREAKING_CHANGES_v3.15.md`.
- **BC-002**: `--fix` flag removed from `/aget-check-health` (SKILL-003). Use `/aget-enhance-health` instead.

---

## [3.14.0] - 2026-04-18

**Theme**: Aligned with framework v3.14.0 (v3.13 Loop Closure + Scope-Lock Discipline)

### Changed

- Version bump: 3.13.0 → 3.14.0 (framework alignment)
- `AGENTS.md` `@aget-version` updated to 3.14.0

### Notes

Per-template CHANGELOG entries for 3.12.0 and 3.13.0 were not individually maintained; template work in those cycles is captured in `aget-framework/aget/CHANGELOG.md`. Gap flagged for v3.14.x / v3.15 retrospective.

---

## [3.11.1] - 2026-04-04

### Changed

- Renamed `aget_housekeeping_protocol.py` → `health_check.py`
- Renamed `study_up.py` → `study_topic.py`
- Config key `skip_sanity` → `skip_health_check`

---
## [3.11.0] - 2026-03-28 - "Skill Conformance, Requirements & Hooks"

### Added

- **requirements/** directory scaffolded (L742 two-level model, #725)
- **.claude/hooks/** directory with README (ADR-008 Generator, #505)
- **governance_intensity** field in AGENTS.md (#732)

### Changed

- 17 skill SKILL.md files updated for L736 conformance (SICR, #678)
- "sanity check" → "health check" terminology (#658)
- RUBRIC.template.md v2.0 deployed

---

## [3.10.0] - 2026-03-21 - "Structural Enforcement"

### Added
- MUST-invoke directives for /aget-create-project and /aget-file-issue (D71)
- Gate Boundary Protocol: plan update + commit as structural proof of gate completion
- Skill Completion Signal pattern in /aget-create-project and /aget-enhance-spec
- SOP Phase -0.5: Content Sync governance (D69/GOV-040)
- SKILL_SPEC_TEMPLATE.yaml (#439)

### Changed
- Skill renames: aget-capture-observation → aget-record-observation, aget-capture-nugget → aget-record-nugget, aget-study-up → aget-study-topic (#480)
- `capture` verb retired from Learning family
- Gate Execution Discipline strengthened with MUST update + MUST commit

### Fixed
- Template hygiene: VERSION, classifier, SECURITY.md corrections (#574)

## [3.9.0] - 2026-03-15 - "Governance Enforcement"

### Added
- Gate 0: Spec Verification (MP-1) in project plan template
- Phase -1: Release Readiness governance in SOP

### Changed
- Version bump to v3.9.0 (5/5 artifact types)
- version_bump.py: extended to cover AGENTS.md, codemeta.json, CITATION.cff
- TEMPLATE_PROJECT_PLAN.md: mandatory Gate 0 added

### Fixed
- aget-enhance-spec: Phase 6 consistency (#418), phantom spec reference (#419)

 - 2026-03-08 - "Governance Maturation"

### Added
- AGENTS.md governance patterns: capability declarations, CLI feature adoption guidance
- `.claude/` scaffolding: settings.json, skills directory structure
- Skill: `aget-expand-ontology` v1.0.0 (optional, acquirable)
- Skill: `aget-enhance-spec` v1.1.0 (specification enhancement lifecycle)

### Changed
- Version bump to v3.8.0
- identity.json: `type` field added
- SOP headers: CAP-SOP-001 compliance
- Migration history entry added

### Notes
- See aget/CHANGELOG.md [3.8.0] for framework changes
- Part of Governance Maturation release (principle codification, deliverable conformance)

---

## [3.7.0] - 2026-03-05 - "Quality Reconciliation"

### Added
- AGENTS.md governance patterns backported (TEMPLATE_AGENTS_MD_SPEC v1.0.0)
- `.claude/` directory scaffolding for CLI feature adoption

### Changed
- Skill renames: `aget-studyup` → `aget-study-up`, `aget-healthcheck-*` → `aget-check-*`
- README positioning: evidence-based reframe, removed undemonstrated claims
- Version bump to v3.7.0
- Migration history entry added

### Notes
- See aget/CHANGELOG.md [3.7.0] for framework changes
- Part of Quality Reconciliation release (content integrity, SOP lifecycle, positioning reframe)

---

## [3.6.0] - 2026-02-21 - "Infrastructure Maturation"

### Added
- Universal skill: `aget-studyup` (focused KB research before implementation)
- Canonical script: `scripts/study_up.py`

### Changed
- Platform claims: "Claude Code, Codex CLI, Gemini CLI" (was "Claude Code, Cursor, Aider, Windsurf")
- Version bump to v3.6.0
- Migration history entry added

### Notes
- See aget/CHANGELOG.md [3.6.0] for framework changes
- Part of Infrastructure Maturation release (observability, content integrity, ontology)

---

## [3.5.0] - 2026-02-14 - "Archetype Customization"

### Added
- Archetype-specific skills: `aget-search-literature`, `aget-document-finding`
- Formal ontology: `ontology/ONTOLOGY_researcher.yaml` (7 concepts, 2 clusters)
- Universal skill: `aget-file-issue` (14th universal)
- Evaluator-focused README narrative

### Changed
- SKILL_VOCABULARY.md v1.2.0 with SKOS reference
- README structure: "Why Researcher?" value proposition

### Notes
- See aget/CHANGELOG.md [3.5.0] for framework changes
- Part of Archetype Customization release

---

## [3.4.0] - 2026-01-18 - "Session Skills Maturity"

### Added
- Session protocol enhancements (re-entrancy guard, calendar awareness)
- Template infrastructure: `sops/SOP_escalation.md`

### Changed
- Cross-CLI validation (Claude Code, Codex CLI, Gemini CLI)
- Governance formalization patterns

### Notes
- See aget/CHANGELOG.md [3.4.0] for framework changes

---

## [3.3.0] - 2026-01-11 - "Framework Alignment"

### Changed
- Updated to AGET framework v3.3.0
- Major upgrade from 3.0.0-beta.1 (skipping 3.0.x, 3.1.x, 3.2.x)

### Notes
- See aget/CHANGELOG.md for cumulative framework changes since 3.0.0
- L517 remediation: Template_Abandonment closure
- This template was in beta status; now aligned with stable release

---

## [3.0.0-beta.1] - 2025-12-27 - "Initial Beta"

### Added
- Initial template creation
- 5D Composition Architecture
- Basic analyst capabilities

