# Template: Researcher Agent

> Synthesize knowledge through literature search and documented findings

**Version**: v3.5.0 | **Archetype**: Researcher | **Skills**: 2 specialized + 13 universal

---

## Why Researcher?

The Researcher archetype expands **knowledge through systematic inquiry**. Unlike casual information gathering, researcher agents provide:

- **Literature search** — Search across sources with structured queries and citation tracking
- **Documented findings** — Record discoveries with evidence, methodology, and implications
- **Knowledge synthesis** — Connect disparate information into coherent understanding

**For evaluators**: If you need an AI that can conduct methodical research and document findings for future reference, the Researcher archetype brings scholarly rigor to your knowledge work.

---

## Skills

Researcher agents come with **2 archetype-specific skills** plus 13 universal AGET skills.

### Archetype Skills

| Skill | Description |
|-------|-------------|
| **aget-search-literature** | Search literature with structured queries. Tracks sources, extracts key findings, and maintains citation metadata. |
| **aget-document-finding** | Document research findings with evidence, methodology, and implications. Creates persistent, searchable records. |

### Universal Skills

All AGET agents include session management, knowledge capture, and health monitoring:

- `aget-wake-up` / `aget-wind-down` — Session lifecycle
- `aget-create-project` / `aget-review-project` — Project management
- `aget-record-lesson` / `aget-capture-observation` — Learning capture
- `aget-check-health` / `aget-check-kb` / `aget-check-evolution` — Health monitoring
- `aget-propose-skill` / `aget-create-skill` — Skill development
- `aget-save-state` / `aget-file-issue` — State and issue management

---

## Ontology

Researcher agents use a **formal vocabulary** of 6 concepts organized into 2 clusters:

| Cluster | Concepts |
|---------|----------|
| **Research Process** | Query, Source, Finding |
| **Knowledge Artifacts** | Citation, Synthesis, Hypothesis |

This vocabulary enables precise communication about research activities.

See: [`ontology/ONTOLOGY_researcher.yaml`](ontology/ONTOLOGY_researcher.yaml)

---

## Quick Start

```bash
# 1. Clone the template
git clone https://github.com/aget-framework/template-researcher-aget.git my-researcher-agent
cd my-researcher-agent

# 2. Configure identity
# Edit .aget/version.json:
#   "agent_name": "my-researcher-agent"
#   "domain": "your-domain"

# 3. Verify setup
python3 -m pytest tests/ -v
# Expected: All tests passing
```

### Try the Skills

```bash
# In Claude Code CLI
/aget-search-literature   # Search for information
/aget-document-finding    # Record a research finding
```

---

## What Makes Researcher Different

| Aspect | Casual Search | Researcher Agent |
|--------|---------------|------------------|
| **Search** | Ad-hoc queries | Structured literature review |
| **Sources** | Links forgotten | Citation tracking |
| **Findings** | Mental notes | Documented records |
| **Synthesis** | Implicit | Explicit knowledge connection |

---

## Framework Specification

| Attribute | Value |
|-----------|-------|
| **Framework** | [AGET v3.5.0](https://github.com/aget-framework/aget) |
| **Archetype** | Researcher |
| **Skills** | 15 total (2 archetype + 13 universal) |
| **Ontology** | 6 concepts, 2 clusters |
| **License** | Apache 2.0 |

---

## Learn More

- **[AGET Framework](https://github.com/aget-framework/aget)** — Core framework documentation
- **[Archetype Guide](https://github.com/aget-framework/aget/blob/main/docs/ARCHETYPE_GUIDE.md)** — All 12 archetypes explained
- **[Getting Started](https://github.com/aget-framework/aget/blob/main/docs/GETTING_STARTED.md)** — Full onboarding guide

---

## Related Archetypes

| Archetype | Best For |
|-----------|----------|
| **[Analyst](https://github.com/aget-framework/template-analyst-aget)** | Data analysis and metrics |
| **[Advisor](https://github.com/aget-framework/template-advisor-aget)** | Recommendations based on research |
| **[Spec-Engineer](https://github.com/aget-framework/template-spec-engineer-aget)** | Formalizing research into specs |

---

**AGET Framework** | Apache 2.0 | [Issues](https://github.com/aget-framework/template-researcher-aget/issues)
