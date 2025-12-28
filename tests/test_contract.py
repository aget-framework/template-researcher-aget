#!/usr/bin/env python3
"""
Contract Tests for template-researcher-aget

Validates template compliance with AGET_TEMPLATE_SPEC v3.0.
"""

import json
import pytest
from pathlib import Path


def get_template_root():
    return Path(__file__).parent.parent


def is_template():
    version_path = get_template_root() / ".aget" / "version.json"
    if version_path.exists():
        with open(version_path) as f:
            return json.load(f).get("instance_type") == "template"
    return True


class TestTemplateStructure:
    def test_manifest_exists(self):
        assert (get_template_root() / "manifest.yaml").exists()

    def test_governance_files(self):
        root = get_template_root()
        assert (root / "governance" / "CHARTER.md").exists()
        assert (root / "governance" / "MISSION.md").exists()
        assert (root / "governance" / "SCOPE_BOUNDARIES.md").exists()

    def test_5d_directories(self):
        aget = get_template_root() / ".aget"
        for dim in ["persona", "memory", "reasoning", "skills", "context"]:
            assert (aget / dim).is_dir()

    def test_identity_file(self):
        assert (get_template_root() / ".aget" / "identity.json").exists()

    def test_version_file(self):
        assert (get_template_root() / ".aget" / "version.json").exists()


@pytest.mark.skipif(is_template(), reason="Template, not instance")
class TestInstanceConfiguration:
    def test_persona_configured(self):
        with open(get_template_root() / ".aget" / "version.json") as f:
            assert json.load(f).get("persona")

    def test_instance_type_is_aget(self):
        with open(get_template_root() / ".aget" / "version.json") as f:
            assert json.load(f).get("instance_type") == "aget"


class TestResearcherArchetype:
    def test_archetype_is_researcher(self):
        archetype = get_template_root() / ".aget" / "persona" / "archetype.yaml"
        if archetype.exists():
            assert "researcher" in archetype.read_text().lower()

    def test_governance_is_minimal(self):
        """Researcher has minimal governance for exploration."""
        archetype = get_template_root() / ".aget" / "persona" / "archetype.yaml"
        if archetype.exists():
            content = archetype.read_text().lower()
            assert "minimal" in content


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
