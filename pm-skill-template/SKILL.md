---
name: pm-skill-template
description: Reference template that defines the standard structure for all PM skills in the library. Use this to understand the format and consistency expected across all PM skills.
---

# Unified PM Skill Template

This template defines the standard structure for all PM Skills in the library. Every skill MUST follow this format to ensure consistency and enable reliable agent parsing.

---

## SKILL NAME: [Skill Name]

### Description
[1-2 sentence clear statement of this skill's core purpose in the PM practice. What problem does it solve? When would a PM use this skill?]

---

### Top Tasks
Core activities that define mastery in this skill. These are the 5-7 most important things a PM does when exercising this skill.

1. [Task 1 - imperative verb + clear outcome]
2. [Task 2 - imperative verb + clear outcome]
3. [Task 3 - imperative verb + clear outcome]
4. [Task 4 - imperative verb + clear outcome]
5. [Task 5 - imperative verb + clear outcome]
6. [Task 6 - optional]
7. [Task 7 - optional]

---

### Best Practices
5-8 actionable principles that separate strong execution from weak execution. Include a mix of Dos and Don'ts.

**Do:**
- [Positive practice with rationale]
- [Positive practice with rationale]
- [Positive practice with rationale]

**Don't:**
- [Anti-pattern with why it fails]
- [Anti-pattern with why it fails]
- [Anti-pattern with why it fails]

**Decision Rules:**
- [Key decision rule or heuristic this skill relies on]
- [Key decision rule or heuristic this skill relies on]

---

### Tools & Artifacts
5-8 specific tools, templates, or artifacts that enable this skill. Include what each is for and when to use it.

| Tool/Artifact | Purpose | When to Use |
|---|---|---|
| [Name] | [1 sentence: what it does] | [Trigger: what phase/condition] |
| [Name] | [1 sentence: what it does] | [Trigger: what phase/condition] |
| [Name] | [1 sentence: what it does] | [Trigger: what phase/condition] |
| [Name] | [1 sentence: what it does] | [Trigger: what phase/condition] |
| [Name] | [1 sentence: what it does] | [Trigger: what phase/condition] |

---

### Integration Points

#### Sends Information To
Data, decisions, or artifacts this skill produces that downstream skills depend on.

| Receiving Skill | Information/Artifact | When (Phase/Trigger) | Format |
|---|---|---|---|
| [Skill Name] | [What data] | [Phase X or event] | [JSON/Markdown/etc] |
| [Skill Name] | [What data] | [Phase X or event] | [JSON/Markdown/etc] |

#### Receives Information From
Data or decisions this skill depends on from upstream skills.

| Source Skill | Information/Artifact | When (Phase/Trigger) | Format |
|---|---|---|---|
| [Skill Name] | [What data] | [Phase X or event] | [JSON/Markdown/etc] |
| [Skill Name] | [What data] | [Phase X or event] | [JSON/Markdown/etc] |

---

### Validation Gates

**This skill must sign-off before proceeding to:** [Next phase or handoff]

**Validation criteria:**
- [ ] [Specific, checkable criterion]
- [ ] [Specific, checkable criterion]
- [ ] [Specific, checkable criterion]

**Validated by:** [Which skills perform quality check? Or is self-validation sufficient?]

**Escalation path:** [What happens if validation fails?]

---

### Decision Framework

[Optional but recommended: Decisions this skill owns, structured as simple rules or matrices]

**Decision:** [What decision?]
- **If** [Condition], **then** [Action]
- **If** [Condition], **then** [Action]

---

### Example / Real-world Application

[Optional: Brief 1-2 paragraph example of this skill in action during an actual product cycle]

---

## Notes for AI Agents

- This template uses markdown for human readability and machine parsability
- All Integration Points must include explicit phase/timing information
- Validation Gates must be specific and measurable, not vague
- If a section doesn't apply to this skill, explicitly note "N/A" rather than leaving it blank
- Best Practices should reflect common failure modes, not just ideal practices
