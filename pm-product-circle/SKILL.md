# Product Circle Workflow: 8-Phase Development Lifecycle

A comprehensive mapping of how PM skills orchestrate through a complete product development cycle. This document defines the work phases, skill ownership, handoffs, and feedback loops.

---

## Overview

The Product Circle spans 8 phases (0-8) from strategic conception through post-launch optimization. Each phase has clear owners, parallel workstreams, and decision gates.

**Total cycle time:** 18-24 weeks (typical mid-size feature)
**Phase duration:** 2-4 weeks each (varies by complexity)

---

## Phase 0: Strategic Grounding (Weeks 1-2)

**Purpose:** Define strategic context and validate problem/opportunity fit

**Skill Owners:**
- **Primary:** PM Strategy
- **Supporting:** Market & Customer Insights, Roadmap Prioritization

**Key Activities:**
- Articulate strategic hypothesis or OKR this work serves
- Validate market/customer evidence for opportunity
- Define success metrics and key outcomes
- Identify constraints (technical, resource, timing)
- Secure executive alignment on strategic importance
- Map dependencies and risks

**Parallel Workstreams:**
- Strategy workstream: Business case development
- Research workstream: Deep market/customer validation (may start prep work)

**Key Outputs:**
- Strategic Brief (1-2 pager)
- OKR alignment mapping
- Initial success metrics framework
- Constraint and dependency map

**Validation Gate:**
- **Must confirm before proceeding:** Strategic hypothesis is sound and supported by evidence
- **Validated by:** PM Strategy + Leadership sponsor
- **Go/No-Go Decision:** Executive steering decides if work proceeds

**Feedback Loop:**
- If validation fails: Return to evidence gathering or reframe hypothesis
- If market signals shift: Strategy skill feeds updated assumptions to downstream phases

**Timing:** 2 weeks
**Next Phase:** Phase 1 (Market & Customer Insights)

---

## Phase 1: Market & Customer Insights (Weeks 3-5)

**Purpose:** Deep understanding of customer needs, market dynamics, and competitive landscape

**Skill Owners:**
- **Primary:** Market & Customer Insights
- **Supporting:** PM Strategy (validates strategic fit), Roadmap Prioritization (context)

**Key Activities:**
- Conduct customer interviews/research (5-15 customers)
- Map competitive landscape and positioning
- Define target customer segments and personas
- Identify critical job-to-be-done insights
- Document unmet needs and pain points
- Create customer narrative/story framework
- Validate initial success metric hypotheses

**Parallel Workstreams:**
- Research workstream: Primary and secondary research
- Strategy workstream: Positioning and messaging alignment
- Technical workstream: Feasibility exploration (async, light)

**Key Outputs:**
- Customer Research Summary (findings, quotes, personas)
- Competitive Positioning Analysis
- Job-to-be-Done framework document
- Refined success metrics (now evidence-backed)
- Customer narrative/messaging foundation

**Validation Gate:**
- **Must confirm before proceeding:** Sufficient customer evidence to inform roadmap decisions
- **Validated by:** Market & Customer Insights + PM Strategy
- **Escalation:** If insights contradict strategic hypothesis, loop back to Phase 0

**Feedback Loop:**
- If new customer needs emerge: Feed back to Strategy for re-evaluation
- Ongoing: Roadmap Prioritization uses these insights to evaluate features

**Timing:** 3 weeks (overlaps with Phase 0 end)
**Next Phase:** Phase 2 (Roadmap Prioritization) - can begin before Phase 1 fully complete

---

## Phase 2: Roadmap Prioritization (Weeks 4-7)

**Purpose:** Define what to build, in what order, and why (feature scope, sequencing, trade-offs)

**Skill Owners:**
- **Primary:** Roadmap Prioritization
- **Supporting:** PM Strategy (strategic alignment), Market & Customer Insights (evidence), Requirements & Scoping (feasibility check)

**Key Activities:**
- Define feature set and core user stories
- Evaluate trade-offs and alternative approaches
- Prioritize features/work using framework (value, effort, risk, dependencies)
- Build release sequencing (MVP, Phase 2, etc.)
- Identify go-to-market sequencing
- Create feature dependency map
- Document rationale for all prioritization decisions
- Stakeholder alignment on scope and sequence

**Parallel Workstreams:**
- Prioritization workstream: Feature evaluation and sequencing
- Requirements workstream: Begin user story writing and acceptance criteria definition
- Technical workstream: Deeper technical feasibility and architecture exploration
- Go-to-market workstream: Market entry strategy and sales enablement planning

**Key Outputs:**
- Prioritized Feature List (with rationale)
- Release Plan / Sequencing Document
- Feature Dependency Map
- Prioritization Matrix (shows decision criteria)
- Trade-off Analysis
- Stakeholder sign-off document

**Validation Gate:**
- **Must confirm before proceeding:** Prioritization reflects strategic intent, customer needs, and technical feasibility
- **Validated by:** Roadmap Prioritization + PM Strategy + Requirements & Scoping
- **Escalation:** If no clear priorities emerge or major disagreement, facilitate prioritization workshop

**Feedback Loop:**
- Technical team provides feasibility feedback → May reshape priorities
- New customer insights → May adjust sequencing
- Business constraints shift → Loop back to Strategy

**Timing:** 4 weeks (overlaps with Phase 1)
**Next Phase:** Phase 3 (Requirements & Scoping) - starts after MVP features locked

---

## Phase 3: Requirements & Scoping (Weeks 6-10)

**Purpose:** Define detailed requirements, acceptance criteria, and technical scope for build phase

**Skill Owners:**
- **Primary:** Requirements & Scoping
- **Supporting:** Roadmap Prioritization (validates against priorities), Launch Execution (early input)

**Key Activities:**
- Write detailed user stories with acceptance criteria for all MVP features
- Define non-functional requirements (performance, security, scalability, etc.)
- Create data models and workflows
- Identify edge cases and error conditions
- Map integrations and API contracts
- Define rollout/deployment strategy
- Create design specification (in collaboration with Design)
- Build testing strategy and test cases (with QA)
- Identify and document scope boundaries (what's NOT included)

**Parallel Workstreams:**
- Requirements workstream: User story and acceptance criteria development
- Design workstream: UX/visual design, flows, prototypes
- Technical workstream: Architecture, API design, implementation planning
- Testing workstream: Test case development
- Launch workstream: Early go-to-market planning (content, sales materials, docs)

**Key Outputs:**
- Requirements Document (user stories, acceptance criteria, data models)
- Design Specification (flows, wireframes, visual design)
- Technical Specification / Architecture Document
- Test Case Inventory
- Scope Boundary Document (what's included/excluded)
- Launch Readiness Checklist (early draft)
- Signed-off Requirements Backlog (ready for dev)

**Validation Gate:**
- **Must confirm before proceeding:** Requirements are clear, testable, and complete enough to code
- **Validated by:** Requirements & Scoping + Design + Tech Lead + QA
- **Escalation:** If requirements are ambiguous or team has concerns, return to requirements refinement

**Feedback Loop:**
- Design may surface UX gaps → Requirements adjustment
- Tech team may surface architectural concerns → Scope/requirement adjustment
- Testing may identify edge cases → Acceptance criteria refinement

**Timing:** 5 weeks (overlaps with Phase 2)
**Next Phase:** Phase 4 (Build & Development) - starts once MVP requirements complete

---

## Phase 4: Build & Development (Weeks 9-16)

**Purpose:** Engineering creates the product according to specifications

**Skill Owners:**
- **Primary:** Engineering (not a PM skill; included for context)
- **Supporting:** Requirements & Scoping (requirement clarification), Launch Execution (early coordination)

**Key Activities:**
- Development team codes features to spec
- Continuous integration and testing
- Code reviews and quality gates
- Design implementation and QA review
- Bug fixes and refinements
- Integration testing
- Performance optimization
- Security review and hardening

**Parallel Workstreams:**
- Development workstream: Feature coding and integration
- QA workstream: Testing, bug reporting, regression testing
- Documentation workstream: Product docs, API docs, support materials
- Launch workstream: Go-to-market asset preparation (sales decks, marketing copy, docs)

**Key Outputs:**
- Working product (features implemented to spec)
- Test Results / QA sign-off
- Documentation (user-facing and internal)
- Launch Readiness Checklist (updated)
- Known Issues / Bug List
- Performance Metrics / Baseline

**Validation Gate:**
- **Must confirm before proceeding:** Product meets acceptance criteria, no critical bugs, performance acceptable
- **Validated by:** QA + Engineering + Requirements & Scoping (spot-check against spec)
- **Escalation:** Critical bugs or requirement mismatches → Fix or descope

**Feedback Loop:**
- Ongoing: Requirements team answers clarification questions from dev
- QA surfaces bugs → Dev fixes
- Launch team may request minor feature adjustments → Handled in build phase if scope allows

**Timing:** 8 weeks
**Next Phase:** Phase 5 (Beta & Validation)

---

## Phase 5: Beta & Validation (Weeks 15-19)

**Purpose:** Test product with real users, validate assumptions, gather feedback, optimize before full launch

**Skill Owners:**
- **Primary:** Launch Execution (owns beta program)
- **Supporting:** Market & Customer Insights (user feedback analysis), Requirements & Scoping (defect triage)

**Key Activities:**
- Recruit beta users (20-100 depending on product)
- Deploy to beta environment with monitoring
- Collect structured feedback (surveys, interviews, analytics)
- Monitor technical metrics (performance, errors, adoption)
- Identify critical issues vs. nice-to-haves
- Iterate on product based on feedback
- Validate success metrics and KPIs
- Document lessons learned
- Prepare launch messaging based on beta feedback
- Create support runbooks and FAQ

**Parallel Workstreams:**
- Beta coordination workstream: User recruitment, feedback collection, issue triage
- Product iteration workstream: Bug fixes, quick iterations on feedback
- Launch preparation workstream: Final marketing materials, sales training, support prep
- Monitoring/analytics workstream: Real-time dashboard setup, KPI tracking

**Key Outputs:**
- Beta Feedback Summary (themes, quotes, impact assessment)
- Validated Success Metrics (vs. targets)
- Issue Backlog (prioritized: fix vs. monitor vs. accept)
- Product Iterations Applied (changelog)
- Launch Messaging / Value Prop (customer-tested)
- Go-to-Market Materials (draft)
- Support Runbooks / FAQ
- Launch Go/No-Go Assessment

**Validation Gate:**
- **Must confirm before proceeding:** Product is stable, success metrics are within acceptable range, team is ready to launch
- **Validated by:** Launch Execution + Requirements & Scoping + Engineering
- **Go/No-Go Decision:** PM + Leadership decides to proceed with launch
- **Escalation:** If success metrics miss targets or critical issues found, either fix and re-beta or adjust launch scope

**Feedback Loop:**
- Critical issues discovered → Return to build phase for fixes
- Success metrics trajectory unclear → Extend beta or define acceptable range
- Customer feedback contradicts assumptions → May inform Phase 6 messaging pivot

**Timing:** 5 weeks (overlaps with end of Phase 4)
**Next Phase:** Phase 6 (Launch Execution)

---

## Phase 6: Launch Execution (Weeks 18-22)

**Purpose:** Coordinate and execute product launch across all channels; begin customer onboarding and adoption

**Skill Owners:**
- **Primary:** Launch Execution
- **Supporting:** Roadmap Prioritization (post-launch roadmap), Market & Customer Insights (customer feedback loops)

**Key Activities:**
- Execute launch communications (email, in-app, social, press)
- Train sales and support teams
- Activate partnerships and marketing campaigns
- Monitor launch health (adoption, bugs, support volume)
- Triage launch issues and coordinate fixes
- Begin customer onboarding and education
- Track early KPIs against targets
- Adjust launch strategy if needed (boost marketing, extend support, etc.)
- Gather customer feedback loops for Phase 7

**Parallel Workstreams:**
- Communications workstream: Email campaigns, content, announcements
- Sales/CS enablement workstream: Training, messaging, sales materials
- Monitoring workstream: Real-time dashboards, alerting on critical issues
- Support workstream: Response to customer questions, issue escalation

**Key Outputs:**
- Launch Communications (all channels executed)
- Sales/CS Training Materials
- Launch Metrics Dashboard (adoption, usage, support volume, etc.)
- Post-Launch Issue Log (critical fixes applied)
- Customer Feedback Log (sentiment, feature requests, issues)
- Launch Retrospective (what worked, what didn't)

**Validation Gate:**
- **Ongoing validation:** Launch health metrics within acceptable range; no critical production issues
- **Validated by:** Launch Execution + Engineering (for critical issues)
- **Escalation:** If launch health fails (high errors, low adoption, critical bugs), escalate to incident response

**Feedback Loop:**
- Customer feedback feeds back to product team for Phase 7 planning
- Support issues identified → May create quick-fix backlog
- Usage patterns differ from assumptions → Inform messaging and roadmap adjustments

**Timing:** 5 weeks
**Next Phase:** Phase 7 (Optimization & Iteration)

---

## Phase 7: Optimization & Iteration (Weeks 21-26, ongoing)

**Purpose:** Drive adoption, fix issues, optimize based on real usage data, and plan next feature set

**Skill Owners:**
- **Primary:** Roadmap Prioritization (owns iteration backlog), Market & Customer Insights (usage analysis)
- **Supporting:** Launch Execution (ongoing monitoring), Requirements & Scoping (details iteration requirements)

**Key Activities:**
- Analyze usage data and adoption metrics
- Identify feature adoption gaps and friction points
- Prioritize bugs, optimizations, and iteration features
- Conduct customer interviews on post-launch experience
- Build iteration backlog for Phase 2 of product
- Optimize onboarding and activation flows
- Monitor and improve support metrics
- Begin planning next release/feature set
- Track progress against success metrics (do they hold?)

**Parallel Workstreams:**
- Analytics workstream: Deep dive into usage patterns, cohort analysis
- Customer research workstream: Post-launch interviews and feedback
- Iteration planning workstream: Backlog refinement for next build phase
- Support optimization workstream: Knowledge base expansion, FAQ updates

**Key Outputs:**
- Usage Analytics Report (adoption, engagement, churn, feature usage)
- Iteration Backlog (prioritized bugs, optimizations, quick wins)
- Customer Feedback Themes (synthesis of post-launch feedback)
- Optimization Roadmap (Phase 2 features and improvements)
- Success Metrics Review (tracking, on/off target)
- Onboarding Optimization Report (where do users get stuck?)

**Validation Gate:**
- **Ongoing validation:** Success metrics trending in right direction; customer satisfaction acceptable
- **Decision point:** If metrics off-target, develop intervention plan (double down on marketing, product changes, etc.)
- **Escalation:** If product fundamentally underperforming, may escalate to business review

**Feedback Loop:**
- Continuous: Customer feedback → Iteration backlog
- Continuous: Usage data → Optimization priorities
- Monthly: Success metrics review → Roadmap adjustments

**Timing:** 6+ weeks (ongoing, feeds into Phase 8)
**Next Phase:** Phase 8 (Scale & Sustain) AND/OR loop back to Phase 2 for next feature set

---

## Phase 8: Scale & Sustain (Weeks 24+, ongoing)

**Purpose:** Ensure product operates reliably at scale; plan for growth and long-term maintenance

**Skill Owners:**
- **Primary:** Roadmap Prioritization (owns scaling backlog), Market & Customer Insights (growth analysis)
- **Supporting:** Launch Execution (ongoing support), Requirements & Scoping (scaling requirements)

**Key Activities:**
- Monitor performance and reliability at scale
- Plan infrastructure scaling (if applicable)
- Expand to new customer segments or markets
- Build long-term support and maintenance processes
- Plan seasonal or usage-based scaling
- Review and update success metrics for scale
- Plan for next generation of product
- Monitor competitive landscape (may trigger roadmap updates)

**Parallel Workstreams:**
- Scaling workstream: Infrastructure, performance, reliability
- Growth workstream: New segment expansion, upsell/cross-sell strategy
- Maintenance workstream: Bug fixes, technical debt, support
- Future planning workstream: Next generation of product or roadmap refresh

**Key Outputs:**
- Scaling Plan (if needed)
- Growth Strategy (next markets/segments)
- Maintenance Roadmap (technical debt, support)
- Long-term Success Metrics and Monitoring
- Competitive Monitoring Report (if relevant)
- Product Sustainability Plan

**Validation Gate:**
- **Ongoing validation:** Product stable and meeting scale requirements
- **Review cadence:** Quarterly or as-needed
- **Escalation:** If scaling issues emerge or market shifts significantly, escalate to strategy review

**Feedback Loop:**
- Competitive intelligence → May inform roadmap priorities
- Growth opportunities → Feed into next feature planning
- Customer feedback → Continuous iteration backlog updates

**Timing:** Ongoing (typically 6+ months after launch)
**Cycle point:** May loop back to Phase 2 for next feature set or Phase 0 for strategic refresh

---

## Cross-Phase Decision Gates

| Gate | Phase | Decision | Stakeholders | Outcomes |
|---|---|---|---|---|
| **Strategic Validation** | 0 → 1 | Proceed with market research? | Strategy, Leadership | Go / Re-evaluate / Kill |
| **Go/No-Go Build** | 2 → 3 | Proceed to requirements? | Strategy, Roadmap, Tech Lead | Go / Adjust Scope / Kill |
| **Build Ready** | 3 → 4 | Can engineering start coding? | Requirements, Tech, QA | Go / Return to Requirements |
| **Beta Ready** | 4 → 5 | Can beta launch? | Engineering, QA, Launch | Go / Extend Build / Descope |
| **Launch Ready** | 5 → 6 | Can launch to all customers? | Launch, Exec, Product | Go / Extended Beta / Rollback |
| **Post-Launch Health** | 6 → 7 | Continue with optimization or investigate issues? | Launch, Product, Leadership | Continue / Incident Response |
| **Success Validation** | 7 → 8 | Are success metrics on target? | Product, Analytics, Leadership | Scale / Iterate / Pivot |

---

## Feedback Loops & Course Correction

### Backward Loops (When to Return to Earlier Phases)

1. **Phase 5 Beta → Phase 0 Strategy** (rare)
   - When: Product fundamentally doesn't solve the problem
   - Action: Revisit strategic hypothesis; consider pivot or kill

2. **Phase 5 Beta → Phase 2 Prioritization** (common)
   - When: User feedback suggests different feature priority
   - Action: Adjust feature set or sequencing before full launch

3. **Phase 4 Build → Phase 3 Requirements** (common)
   - When: Technical feasibility issues or design gaps surface
   - Action: Refine requirements; may descope some features

4. **Phase 6 Launch → Phase 4 Build** (rare but critical)
   - When: Critical production bugs or issues
   - Action: Hotfix or rollback; re-enter build phase

5. **Phase 7 Optimization → Phase 2 Prioritization** (common)
   - When: Usage data shows different priorities than planned
   - Action: Adjust next iteration priorities

### Forward Loops (Continuous Feedback)

- **Market signals → PM Strategy** (continuous): Competitive or market shifts inform strategy refresh
- **Customer feedback → Roadmap Prioritization** (continuous): Ongoing insights update prioritization
- **Usage analytics → Launch Execution** (continuous): Real-time adjustments to launch tactics

---

## Parallel Workstreams Overview

This product circle is NOT strictly waterfall. The following workstreams often overlap:

| Workstream | Phases | Duration | Dependencies | Owner |
|---|---|---|---|---|
| Strategy | 0-1 | 2-3 weeks | None (starts first) | PM Strategy |
| Customer Research | 1-3 | 4-6 weeks | Strategy complete | Market & Insights |
| Prioritization | 2 | 4 weeks | Strategy + Research | Roadmap Prioritization |
| Requirements | 3 | 5 weeks | Prioritization | Requirements & Scoping |
| Design | 3-4 | 6-8 weeks | Requirements start | Design (outside PM skills) |
| Build | 4 | 8 weeks | Requirements complete | Engineering (outside PM skills) |
| QA/Testing | 4-5 | 9 weeks | Requirements complete | QA (outside PM skills) |
| Launch Prep | 5-6 | 5-6 weeks | Build mostly complete | Launch Execution |
| Beta | 5 | 5 weeks | Build complete | Launch Execution |
| Optimization | 7+ | Ongoing | Launch complete | Roadmap Prioritization |

---

## Timing & Capacity Planning

**Typical timeline:** 18-24 weeks from Phase 0 to Phase 6 full launch
**Critical path:** Strategy → Research → Prioritization → Requirements → Build → Beta → Launch
**Slack phases:** Market research and design can overlap with other work

**Team capacity considerations:**
- One PM can own a complete cycle if workload is moderate
- Large initiatives may need PM specialization (Strategy PM, Launch PM, etc.)
- Cross-functional coordination is continuous, not episodic

---

## Escalation Paths

All validation gates must have clear escalation criteria:

1. **Strategic misalignment** (discovered in Phases 0-2): Escalate to leadership/sponsor
2. **Scope creep** (discovered in Phases 3-4): Escalate to prioritization framework
3. **Critical bugs** (discovered in Phases 4-6): Follow incident response process
4. **Launch failure** (discovered in Phase 6): Escalate to incident commander
5. **Success metrics miss** (discovered in Phases 7-8): Escalate to product leadership for strategy review

---

## Notes for AI Agents

- This workflow is NOT strictly sequential; overlaps are intentional and healthy
- Each phase has a clear owner skill, but all phases involve cross-functional collaboration
- Feedback loops are normal and expected; they represent learning and course correction
- Timing estimates are for medium-complexity features; adjust based on scope
- Use this framework to understand when information flows between skills and what data format is expected
