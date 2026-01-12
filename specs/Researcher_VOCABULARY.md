# Researcher Domain Vocabulary

**Version**: 1.1.0
**Status**: Active
**Owner**: template-researcher-aget
**Created**: 2026-01-10
**Updated**: 2026-01-11
**Scope**: Template vocabulary (DRIVES instance behavior per L481)
**Archetype**: Researcher
**Template**: VOCABULARY_TEMPLATE_v3.3

---

## Meta

```yaml
vocabulary:
  meta:
    domain: "research"
    version: "1.0.0"
    owner: "template-researcher-aget"
    created: "2026-01-10"
    theoretical_basis:
      - "L481: Ontology-Driven Agent Creation"
      - "L482: Executable Ontology - SKOS+EARS Grounding"
    archetype: "Researcher"
```

---

## Concept Scheme

```yaml
Researcher_Vocabulary:
  skos:prefLabel: "Researcher Vocabulary"
  skos:definition: "Vocabulary for researcher domain agents"
  skos:hasTopConcept:
    - Researcher_Core_Concepts
  rdf:type: skos:ConceptScheme
```

---

## Core Concepts

### Research_Question

```yaml
Research_Question:
  skos:prefLabel: "Research Question"
  skos:definition: "A focused inquiry that guides investigation and discovery"
  skos:broader: Researcher_Core_Concepts
  skos:inScheme: Researcher_Vocabulary
```

### Knowledge_Gap

```yaml
Knowledge_Gap:
  skos:prefLabel: "Knowledge Gap"
  skos:definition: "An identified area where current understanding is incomplete"
  skos:broader: Researcher_Core_Concepts
  skos:inScheme: Researcher_Vocabulary
```

### Evidence

```yaml
Evidence:
  skos:prefLabel: "Evidence"
  skos:definition: "Data, observations, or facts that support or refute a hypothesis"
  skos:broader: Researcher_Core_Concepts
  skos:inScheme: Researcher_Vocabulary
```

### Synthesis

```yaml
Synthesis:
  skos:prefLabel: "Synthesis"
  skos:definition: "Integration of multiple sources into coherent understanding"
  skos:broader: Researcher_Core_Concepts
  skos:inScheme: Researcher_Vocabulary
```

### Discovery

```yaml
Discovery:
  skos:prefLabel: "Discovery"
  skos:definition: "New knowledge or insight gained through systematic investigation"
  skos:broader: Researcher_Core_Concepts
  skos:inScheme: Researcher_Vocabulary
```

---

## Concept Relationships

```yaml
relationships:
  hierarchical:
    - parent: Researcher_Core_Concepts
      children: [Research_Question, Knowledge_Gap, Evidence, Synthesis, Discovery]

  associative:
    - subject: Research_Question
      predicate: skos:related
      object: Knowledge_Gap
    - subject: Evidence
      predicate: skos:related
      object: Synthesis
```

---

## EKO Cross-References

Per AGET_EXECUTABLE_KNOWLEDGE_SPEC.md:

| Vocabulary Term | EKO Term | Relationship |
|-----------------|----------|--------------|
| Research_Question | EKO:Investigation_Focus | skos:exactMatch |
| Evidence | EKO:Knowledge_Evidence | skos:closeMatch |
| Discovery | EKO:Knowledge_Asset | skos:broadMatch |

---

## Extension Points

Instances extending this template vocabulary should:
1. Add domain-specific terms under appropriate broader concepts
2. Maintain SKOS compliance (prefLabel, definition, broader/narrower)
3. Reference foundation L-docs where applicable
4. Use `research_status` for terms under investigation

---

## References

- L481: Ontology-Driven Agent Creation
- L482: Executable Ontology - SKOS+EARS Grounding
- R-REL-015: Template Ontology Conformance
- AGET_VOCABULARY_SPEC.md

---

*Researcher_VOCABULARY.md v1.0.0 — SKOS-compliant template vocabulary*
*Generated: 2026-01-10*
