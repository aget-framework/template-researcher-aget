# Changelog

All notable changes to this template will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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

