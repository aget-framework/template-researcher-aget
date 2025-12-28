# AGET Researcher Template

> **Research and knowledge discovery template**

Part of the [AGET Framework](https://github.com/aget-framework) v3.0.0.

## Archetype

**Researcher** - Expand knowledge through systematic investigation and discovery.

- **Extends**: advisor
- **Governance**: Minimal
- **Primary A-SDLC Phases**: 0 (Discovery)

## Key Capabilities

- Literature review and synthesis
- Hypothesis testing and validation
- Knowledge synthesis and documentation
- Exploratory investigation

## Inviolable

```
INV-RES-001: shall NOT claim Discovery WITHOUT Reproducible_Evidence
```

## Quick Start

1. Clone this template
2. Run instantiation script (see [Getting Started](docs/GETTING_STARTED.md))
3. Configure for your research domain

## Structure

```
template-researcher-aget/
├── manifest.yaml          # Template configuration
├── governance/            # Charter, Mission, Scope
├── tests/                 # Contract tests
└── .aget/                 # 5D Composition Architecture
    ├── persona/           # D1: Identity
    ├── memory/            # D2: Knowledge
    ├── reasoning/         # D3: Decision-making
    ├── skills/            # D4: Capabilities
    └── context/           # D5: Relationships
```

## License

Apache License 2.0 - See [LICENSE](LICENSE)

---

*AGET Framework - AI discovers patterns, you describe intent*
