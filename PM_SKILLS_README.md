# 📚 PM Skills Library - Agent Skills

This directory contains the complete **PM Skills Library** - a comprehensive framework for product management workflows built as reusable skills for AI agents.

## 🎯 Quick Navigation

### Core PM Skills (6 Total)

| Skill | Directory | Purpose | When Active |
|---|---|---|---|
| **PM Strategy** | `pm-strategy/` | Market opportunities, validation, strategy definition | Weeks 1-10+ |
| **Design & UX** | `tier2-design/` | User research, design validation, accessibility | Weeks 1-18 (Shift-Left) |
| **Tech Architecture** | `tier2-tech-architecture/` | System design, feasibility, scalability | Weeks 4-18 |
| **QA & Testing** | `tier2-qa/` | Testability review, quality gates (Shift-Left) | Weeks 8-20 |
| **PM Execution** | `pm-execution/` | Sprint planning, dependencies, risk management | Weeks 8-20 |
| **Launch & Marketing** | `product-launch/` | GTM strategy, campaigns, feedback | Weeks 10-22 |

### Foundation Skills (2 Total)

| Skill | Directory | Purpose |
|---|---|---|
| **Product Circle Workflow** | `pm-product-circle/` | 8-phase product development lifecycle |
| **Unified Skill Template** | `pm-skill-template/` | Framework template all skills follow |

---

## 📖 How to Use These Skills

### For AI Agents

Each skill is structured as a `SKILL.md` file with:
- **Description**: What the skill does
- **Top Tasks**: Core responsibilities (5-7 items)
- **Best Practices**: DOs and DON'Ts (5-8 items)
- **Tools**: Recommended tools and technologies (5-8 items)
- **Integration Points**: Which other skills this communicates with
- **Use Case Examples**: Real-world scenarios with step-by-step guidance

**To use**: Load the skill via your agent framework and reference the structured sections.

### For Product Teams

1. **Get oriented**: Read `pm-product-circle/SKILL.md` to understand the 8-phase cycle
2. **Know your role**: Pick the skill that matches your role (PM, Designer, Engineer, QA, Launch)
3. **Understand integration**: Review "Integration Points" to see how skills coordinate
4. **Follow the templates**: Use provided templates for handoffs and communication

### For Training/Onboarding

Each skill includes:
- **Real-world use cases** showing practical application
- **Decision frameworks** for common scenarios
- **Templates & checklists** ready to use
- **Integration points** showing team coordination

---

## 🔄 The 8-Phase Product Development Cycle

```
Phase 0: Stakeholder Alignment (Week 0)
    ↓
Phase 1: Discovery & Strategy (Weeks 1-4) - PM Strategy leads
    ↓
Phase 2/3: Design + Tech Architecture (Weeks 4-10) - PARALLEL
    ├─ Design: Specs, prototypes, user research
    └─ Tech: Architecture, feasibility, risk assessment
    ↓
Phase 4: PM Execution Planning (Weeks 8-12)
    ├─ Sprint planning
    ├─ Dependency mapping
    └─ Risk tracking
    ↓
Phase 5: Build + QA (Weeks 12-18) - PARALLEL with Shift-Left QA
    ├─ Engineering: Feature development
    └─ QA: Continuous testing, quality gates (starts Week 8!)
    ↓
Phase 6: Launch Prep (Weeks 10-18)
    ├─ GTM strategy
    ├─ Campaigns
    └─ Sales enablement
    ↓
Phase 7: Launch Execution (Weeks 18-20)
    ├─ Campaign activation
    ├─ Real-time monitoring
    └─ Customer engagement
    ↓
Phase 8: Post-Launch Iteration (Week 20+)
    ├─ Feedback analysis
    ├─ Lessons learned
    └─ Cycle back to Phase 1
```

---

## 🎯 Key Innovation: Shift-Left QA

**Traditional Approach:**
- QA starts Week 12 (after engineering starts building)
- Often discovers bugs too late
- Last-minute crises before launch

**This Library's Approach:**
- QA starts Week 8 (during design/tech phase)
- Reviews testability of designs and architecture
- Prevents issues early = faster, higher-quality delivery

**Result**: Save 4+ weeks, prevent late-stage bugs, reduce launch risk

---

## 🔗 Skill Integration Points

### Communication Flows

| From | To | What Info | When |
|---|---|---|---|
| **PM Strategy** | Design | Customer needs, acceptance criteria | Week 2 |
| **PM Strategy** | Tech Arch | Business goals, scale, budget | Week 2 |
| **Design** | Tech Arch | Design specs, feasibility questions | Week 6-8 |
| **Tech Arch** | PM Execution | Dependency map, critical path | Week 10 |
| **QA** | ALL | Testability feedback, quality metrics | Weeks 8, 16, 18 |
| **Launch** | PM Strategy | Customer feedback, market signals | Week 22 |

### Escalation Path (When Skills Disagree)

1. **Level 1**: Direct communication between skills (24 hours)
2. **Level 2**: PM Execution mediates (48 hours)
3. **Level 3**: PM Strategy makes decision (3 days)
4. **Level 4**: Executive override (5 days)

---

## 📊 Skill Details at a Glance

### PM Strategy
- **One-liner**: Identify market opportunities, validate assumptions, define product strategy
- **When**: Weeks 1-10, continuous feedback (Week 20+)
- **Talks to**: Design, Tech Arch, QA, PM Execution, Launch
- **Key Output**: Product strategy, success metrics, business goals

### Design & UX
- **One-liner**: User research, design validation, accessibility, design systems
- **When**: Weeks 1-18 (Shift-Left from Week 1)
- **Talks to**: PM Strategy, Tech Arch, QA, PM Execution, Launch
- **Key Output**: Design specs, prototypes, design system, accessibility audit

### Tech Architecture
- **One-liner**: System design, feasibility validation, scalability, technical risks
- **When**: Weeks 4-18, feasibility review starts Week 2
- **Talks to**: PM Strategy, Design, PM Execution, QA
- **Key Output**: Architecture Decision Records, tech stack, dependency map

### QA & Testing (Shift-Left!)
- **One-liner**: Testability review, test planning, quality gates, continuous testing
- **When**: Weeks 8-20 (NOT Week 12! Shift-Left starts Week 8)
- **Talks to**: Design, Tech Arch, PM Strategy, PM Execution
- **Key Output**: Test plans, quality metrics, go/no-go decision

### PM Execution
- **One-liner**: Sprint planning, dependency management, risk tracking, team coordination
- **When**: Weeks 8-20, central coordinator for all phases
- **Talks to**: ALL other skills (central hub)
- **Key Output**: Sprint plans, status reports, risk register

### Launch & Marketing
- **One-liner**: GTM execution, campaign coordination, post-launch feedback collection
- **When**: Weeks 10-22, early start for campaign planning
- **Talks to**: PM Strategy, Design, QA, PM Execution
- **Key Output**: Launch plan, campaign performance, customer feedback

---

## 📁 File Structure

```
agent-skills/
├── pm-strategy/
│   └── SKILL.md (PM Strategy Skill)
├── tier2-design/
│   └── SKILL.md (Design & UX Skill)
├── tier2-tech-architecture/
│   └── SKILL.md (Tech Architecture Skill)
├── tier2-qa/
│   └── SKILL.md (QA & Testing Skill)
├── pm-execution/
│   └── SKILL.md (PM Execution Skill)
├── product-launch/
│   └── SKILL.md (Launch & Marketing Skill)
├── pm-product-circle/
│   └── SKILL.md (8-Phase Workflow)
├── pm-skill-template/
│   └── SKILL.md (Unified Skill Template)
└── [other existing skills...]
```

---

## 🚀 Using These Skills with Your Agent System

### Loading a Skill

To load a PM skill in your agent system:

```bash
# Example: Loading the PM Strategy skill
opencode skill load pm-strategy

# Or load all PM skills
opencode skill load pm-*
```

### Invoking a Skill

When an agent needs to use a skill:

1. Load the relevant `SKILL.md` file
2. Review the skill's sections:
   - **Description**: Understand what the skill does
   - **Top Tasks**: Know the core responsibilities
   - **Best Practices**: Follow the guidance
   - **Integration Points**: Know who to coordinate with
   - **Use Case**: See practical examples
3. Execute the skill according to its workflow
4. Coordinate with other skills via integration points

### Multi-Skill Coordination

For complex workflows involving multiple skills:

1. Use the **Product Circle** skill to understand overall flow
2. Load the **Master PM Agent Prompt** (in parent PM_SKILLS_LIBRARY) for coordination logic
3. Reference **Communication Protocols** for handoff templates
4. Follow **Escalation Guide** if conflicts arise

---

## 📚 Related Resources

For additional context and full documentation:

- **Main README**: See parent directory `/PM_SKILLS_LIBRARY/README.md`
- **Complete Index**: See `/PM_SKILLS_LIBRARY/INDEX.md`
- **Communication Protocols**: See `/PM_SKILLS_LIBRARY/tier4/01_Communication_Protocols.md`
- **Escalation Guide**: See `/PM_SKILLS_LIBRARY/tier4/02_Escalation_Guide.md`
- **Agent Coordination**: See `/PM_SKILLS_LIBRARY/tier4/03_Master_PM_Agent_Prompt.md`

---

## ✨ Key Features

✅ **8 Skills** - Complete coverage of product development  
✅ **Structured Format** - Each skill follows consistent template  
✅ **Real-World Examples** - Practical use cases with steps  
✅ **AI-Ready** - Designed for agent integration  
✅ **Cross-Functional** - Clear coordination between skills  
✅ **Shift-Left** - Early QA, design, and launch involvement  
✅ **Decision Frameworks** - Guidance for complex scenarios  
✅ **Templates & Checklists** - Ready-to-use artifacts  

---

## 🎓 Learning Path

**For PMs**: `pm-strategy/` → `pm-product-circle/` → All other skills  
**For Designers**: `pm-product-circle/` → `tier2-design/` → `pm-strategy/`  
**For Engineers**: `tier2-tech-architecture/` → `pm-product-circle/` → `pm-execution/`  
**For QA**: `tier2-qa/` → `pm-product-circle/` → `pm-execution/`  
**For Launch**: `product-launch/` → `pm-strategy/` → `pm-product-circle/`  
**For Agents**: `pm-product-circle/` → All 6 skills → Communication flows  

---

## 📞 Questions?

- **What's this skill?** → Read the SKILL.md file (each has a Description section)
- **When do I use it?** → Check the "When it engages" section
- **Who do I work with?** → See "Integration Points" / "Who it talks to"
- **How do I do it?** → Follow the "Use Case Example" with step-by-step guidance
- **What are best practices?** → Read the "Best Practices" section
- **What if there's a conflict?** → See `/PM_SKILLS_LIBRARY/tier4/02_Escalation_Guide.md`

---

**Last Updated**: March 21, 2026

**Status**: ✅ Ready for production use

**Next Steps**: Start with `pm-product-circle/SKILL.md` to understand the full workflow, then explore individual skills based on your role.
