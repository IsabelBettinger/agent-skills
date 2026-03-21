# SKILL NAME: PM Strategy

### Description
PM Strategy is the foundational skill for defining the "why" behind product work. It establishes the strategic context, validates problem/opportunity fit, and ensures all downstream decisions (prioritization, requirements, launch) align with business objectives and market realities. A PM exercises this skill when building business cases, conducting strategic discovery, validating market hypotheses, and ensuring work serves clear OKRs.

---

### Top Tasks

1. **Articulate strategic hypothesis** - Clearly define what problem/opportunity the work addresses and why now. Document the business case: market size, customer pain, competitive context, and expected impact.

2. **Validate strategic assumptions through evidence** - Conduct or synthesize market research, customer interviews, and data analysis to confirm that strategic hypotheses are sound before committing engineering resources.

3. **Map strategic fit to OKRs and business goals** - Connect proposed work explicitly to company objectives, key results, and financial goals. Identify potential conflicts or synergies with other strategic initiatives.

4. **Identify and articulate constraints** - Document technical, market, resource, timing, and financial constraints that will shape scope and sequencing. Make these explicit to prevent surprises later.

5. **Build and evolve success metrics framework** - Define how success will be measured (usage, revenue, efficiency, quality, market share, etc.) and tie metrics directly to strategic objectives. This framework guides decisions through the entire product circle.

6. **Communicate strategic context to stakeholders** - Ensure leadership, design, engineering, and launch teams understand the strategic rationale. This alignment prevents misalignment and scope creep downstream.

7. **Conduct strategic pivots or kill decisions** - Monitor whether assumptions hold during build and launch phases. Make explicit recommendations to pivot strategy, descope work, or kill initiatives when evidence contradicts initial hypothesis.

---

### Best Practices

**Do:**
- **Ground strategy in evidence, not intuition.** Every strategic hypothesis should be backed by customer research, market data, or historical precedent. Intuition is a starting point, not validation.
- **Document the "why" explicitly.** Future decisions are easier when people understand strategic rationale. A 1-2 page strategic brief is worth 10 hours of misaligned discussions later.
- **Challenge strategic assumptions early and often.** Create psychological safety for teams to surface doubts about strategic fit. The earlier you catch a bad hypothesis, the less waste occurs.
- **Connect strategy to personal incentives.** Tie OKRs to compensation, promotion, and team recognition. People optimize for what they're measured on; misaligned metrics kill strategy.
- **Revisit strategy as evidence accumulates.** Strategy is not one-and-done in Phase 0. Re-evaluate during Phases 1, 5, and 7 as you learn more about the market and customer.
- **Balance long-term vision with quarterly delivery.** Strategic thinking shouldn't trap you in 3-year planning without near-term milestones. Break long-term strategy into quarterly OKRs and measurable progress.
- **Identify and communicate trade-offs explicitly.** Strategy is about choices. Make clear what you're optimizing for (revenue, market share, efficiency, quality) and what you're trading away (other goals, resources, speed).

**Don't:**
- **Don't build strategy in a PM-only bubble.** Engineers, designers, and launch teams will resist strategy they didn't help shape. Co-create with stakeholders to build buy-in.
- **Don't confuse strategic goals with tactical measures.** "Ship feature by Q3" is a tactic, not strategy. Strategy is "dominate SMB market segment by expanding up-market," and tactics are the features that enable it.
- **Don't let strategy float.** If no one can articulate why work is happening, strategy has failed. Make it so ingrained that every team member can explain the strategic context in 2 minutes.
- **Don't ignore constraints.** Pretending technical debt, budget limits, or team capacity don't exist doesn't make them go away. Build strategy within constraints, not around them.
- **Don't pivot strategy without data.** If you pivot based on one customer comment or exec opinion, you'll thrash the organization. Require a threshold of evidence before pivoting.

**Decision Rules:**
- **Rule: If initiative doesn't clearly map to an OKR, don't fund it.** This prevents strategy drift and ensures focus.
- **Rule: If success can't be measured, don't build it.** Unmeasurable work is hard to defend and easy to continue indefinitely without progress.
- **Rule: If strategic hypothesis is questioned by multiple experts, investigate before proceeding.** Red flags from diverse sources often indicate a real problem.

---

### Tools & Artifacts

| Tool/Artifact | Purpose | When to Use |
|---|---|---|
| **Strategic Brief** | 1-2 pager that documents hypothesis, business case, target customer, problem, opportunity, success metrics, and constraints. Serves as north star for all downstream decisions. | Phase 0: Create at start of work. Update during Phase 5 (Beta) if major insights emerge. |
| **Business Case Canvas** | Structured template documenting problem, opportunity size, target customer, value prop, success metrics, investment required, expected ROI. Guides resource allocation decisions. | Phase 0-1: Build business case to secure funding/prioritization. |
| **Assumption Inventory** | List of all strategic assumptions (market size, customer willingness to pay, competitive response, adoption rate, etc.). Prioritized by impact and uncertainty. | Phase 0: Create at start. Update in Phases 1, 5, 7 as you test assumptions. |
| **Market Analysis Synthesis** | Structured summary of competitive landscape, market trends, customer segments, TAM/SAM/SOM, pricing insights. Draws from secondary research and interviews. | Phase 1: Conduct or synthesize existing analysis. Reference throughout product cycle to validate strategic fit. |
| **Success Metrics Framework** | Document defining how success will be measured. Includes leading indicators (activity), lagging indicators (outcomes), targets, measurement method, and how metrics align to OKRs. | Phase 0: Create initial framework. Phase 1: Refine based on research. Phase 5: Validate metrics are trackable and sensitive. Phase 7: Compare actual vs. target. |
| **Constraint Map** | Document listing technical, market, timing, resource, and financial constraints. Includes impact on scope/sequencing and mitigation strategies. | Phase 0: Identify constraints early. Phase 2: Use to inform prioritization trade-offs. |
| **Strategic Alignment Matrix** | Visualization showing how proposed work maps to multiple OKRs, showing synergies or conflicts. Helps deprioritize work that doesn't clearly align. | Phase 0-1: Use to defend strategic focus. Update quarterly or when strategy shifts. |

---

### Integration Points

#### Sends Information To

| Receiving Skill | Information/Artifact | When (Phase/Trigger) | Format |
|---|---|---|---|
| **Market & Customer Insights** | Strategic hypothesis, customer segmentation framework, research questions to answer, success metrics draft | Phase 0-1 (Start of Phase 1) | Strategic Brief + Assumption Inventory (Markdown) |
| **Roadmap Prioritization** | Strategic context, OKR alignment, success metrics framework, key opportunities/constraints | Phase 1-2 (End of Phase 1, ready for prioritization) | Strategic Brief + Assumption Inventory + Success Metrics Framework (Markdown) |
| **Requirements & Scoping** | Strategic context, success metrics, non-negotiable features (linked to strategy), constraint map | Phase 2-3 (When requirements kickoff) | Strategic Brief excerpt + Success Metrics Framework (Markdown) |
| **Launch Execution** | Success metrics framework, launch objectives (tied to strategy), competitive positioning, customer narrative | Phase 5 (End of Beta, preparing for launch) | Success Metrics Framework + Launch Objectives memo (Markdown) |
| **All Skills (Broadcast)** | Strategic Brief (updated), OKR alignment, strategic priorities for quarter | Phase 0 (Published) + Quarterly updates | Strategic Brief + Strategic Alignment Matrix (Markdown/Slide) |

#### Receives Information From

| Source Skill | Information/Artifact | When (Phase/Trigger) | Format |
|---|---|---|---|
| **Market & Customer Insights** | Market analysis, customer research findings, competitive intelligence, validation of assumptions | Phase 1 (Ongoing as research completes) | Market Analysis Synthesis + Research findings memo (Markdown/Slides) |
| **Roadmap Prioritization** | Prioritization framework and decisions (to validate against strategy), trade-off analysis | Phase 2 (End of Phase 2) | Prioritization document (Markdown) |
| **Launch Execution** | Early adoption metrics, customer feedback, launch outcomes vs. forecast | Phase 6 (Launch) + Phase 7 (Ongoing) | Launch metrics dashboard + Customer feedback synthesis (JSON/CSV + Markdown) |
| **Requirements & Scoping** | Scope decisions, descopes (for constraint management), technical feasibility findings | Phase 3-4 (As requirements evolve) | Requirements summary + Descope rationale (Markdown) |

---

### Validation Gates

**This skill must sign-off before proceeding to:** Phase 1 (Market & Customer Insights) research phase with full commitment of resources. Also must re-validate before Phase 3 (Requirements & Scoping) begins in earnest.

**Validation criteria:**
- [ ] Strategic hypothesis is clearly articulated and written down (not vague or in PM's head only)
- [ ] Strategic hypothesis is backed by at least 1-2 supporting data points (market research, customer feedback, historical precedent) - not pure intuition
- [ ] Strategic work maps clearly to an active OKR or business goal (at company, team, or product level)
- [ ] Success metrics are defined and measurable (not vague aspirations like "increase adoption")
- [ ] Key constraints (technical, resource, market, timing) have been identified and documented
- [ ] Stakeholders (leadership sponsor, design lead, tech lead) have reviewed and agreed on strategic hypothesis

**Validated by:** PM Strategy + PM's direct manager or exec sponsor + Key stakeholder representative (tech lead or design lead typically)

**Escalation path:** 
- If validation fails: Return to strategy refinement. Identify what evidence is missing, conduct additional research, or reframe hypothesis. Do NOT proceed to Phase 1 without validation.
- If stakeholders disagree: Facilitate alignment discussion. Document disagreement and decision made (don't pretend consensus exists if it doesn't). Escalate to leadership if needed.

---

### Decision Framework

PM Strategy owns several key decisions that shape the entire product circle:

**Decision 1: Should we pursue this opportunity/problem?**
- **If** strategic hypothesis is backed by evidence and aligns to OKRs, **then** proceed to Phase 1 (research)
- **If** hypothesis is weak or contradicts other strategic priorities, **then** deprioritize or kill
- **If** insufficient evidence to decide, **then** conduct light discovery research and revisit (don't commit full resources to Phase 1 yet)

**Decision 2: How do we measure success?**
- **If** success is primarily revenue or financial, **then** focus metrics on adoption, willingness-to-pay, revenue impact
- **If** success is primarily customer satisfaction or retention, **then** focus metrics on NPS, churn, engagement
- **If** success is primarily efficiency (cost reduction, speed), **then** focus metrics on utilization, time savings, error reduction
- **If** success is multi-dimensional, **then** define a north-star metric (usually revenue or retention) + 2-3 supporting metrics to prevent tradeoff blindness

**Decision 3: What are our constraints and how do they shape scope?**
- **If** budget constraint is real, **then** right-size MVP scope to fit budget; deprioritize nice-to-haves
- **If** time constraint is real (e.g., must launch by Q4), **then** ruthlessly scope down to what can ship in time; plan Phase 2 for remaining features
- **If** technical constraint exists (e.g., legacy system limits scalability), **then** either invest in foundation work now or scope product to work within constraints
- **If** resource constraint exists (small team), **then** design for efficiency; consider partnership or outsourcing to supplement internal capacity

**Decision 4: Is this work strategically coherent or are we chasing too many things?**
- **If** new initiative clearly aligns to existing OKRs, **then** add to backlog
- **If** new initiative competes for resources with higher-priority work, **then** deprioritize the lower one (explicitly communicate this decision)
- **If** multiple unrelated initiatives are competing for attention, **then** conduct portfolio prioritization to pick top 3-5 bets; explicitly kill or defer others

**Decision 5: Do we pivot, persevere, or kill based on evidence?**
- **If** beta shows success metrics on-track and customer feedback positive, **then** proceed to launch
- **If** beta shows metrics off-track but improvement path is clear, **then** extend beta, iterate, and re-test
- **If** beta shows fundamental market problem (customers don't want the solution), **then** pivot (different customer, different feature, different positioning) or kill
- **If** launch shows poor adoption despite good product quality, **then** investigate go-to-market (could be positioning, pricing, channels, or market readiness)

---

### Real-World Application: Example

**Scenario: SaaS company considering a mobile app for their core product**

**Phase 0 (Strategic Grounding):**

PM Strategy articulates: "We believe there's an untapped revenue opportunity in mobile-first customer segment (SMBs in field service). Current desktop product misses them because they work on-site without laptop access. Our hypothesis: mobile app targeting field service teams will increase TAM by 40% and drive $2M ARR within 18 months."

Strategic Brief includes:
- Target customer: Field service teams (electricians, plumbers, contractors)
- Problem: Can't access job data/updates in field without bringing laptop
- Opportunity: Market research shows 15% of field service SMBs use mobile-first tools; current desktop tool has 8% market share in this segment
- Success metrics: 10K mobile user signups in Year 1, 30% mobile adoption rate among existing customers, $0.50 CAC payback period
- Constraints: Mobile dev experience is weak (current team is web-focused); will require hiring or partnership

Assumption Inventory:
- Field service teams will pay for mobile app (confidence: medium - some research, no direct validation yet)
- We can build and maintain quality mobile product with small team (confidence: low - unknown)
- Current customers will adopt mobile if we build it (confidence: medium - need to ask them)
- Mobile will have 30% adoption within 12 months (confidence: low - depends on quality and marketing)

**Decision at validation gate:** Executive sponsor reviews strategic brief and asks: "Do we have evidence field service teams actually use mobile tools?" PM responds: "We have some market research suggesting it, but haven't talked to actual field service teams yet. Recommend Phase 1 research to validate before committing to mobile." Sponsor agrees. Work proceeds to Phase 1.

**Phase 1 (Market & Customer Insights):**

Market & Customer Insights skill conducts:
- 12 interviews with field service business owners about mobile tool usage
- Competitive analysis of 5 mobile solutions in field service space
- Survey of 50 existing customers: "How likely to adopt mobile version?"

Key findings:
- 8 of 12 interviewees said they'd "definitely" or "probably" use a mobile app
- Competitors have launched mobile solutions; some have gained 20-30% of customer base
- 62% of existing customers said they'd try mobile version
- Biggest pain points: (1) seeing job updates in field, (2) taking photos of work, (3) time tracking

**Assumption validation:** High confidence that field service teams want mobile. Revise metric: target 40% adoption in Year 1 (higher than 30% based on customer feedback).

**Phase 2 (Roadmap Prioritization):**

Now that strategy is validated, Roadmap Prioritization skill asks: "Given constraints (small mobile team needed), what's the MVP?"

Using customer research, priority features for MVP: (1) Job access in field, (2) Photo capture and annotation, (3) Time tracking. Nice-to-haves for Phase 2: Offline sync, GPS geolocation, Slack integration.

Prioritization uses Strategy's success metrics to guide decisions: Features that drive adoption get higher priority than nice-to-haves.

**Phases 3-4 (Requirements & Build):**

Strategy's success metrics framework is used throughout:
- Design: Focused on simplicity for field workers (drives adoption)
- Requirements: Include photo capture and time tracking as non-negotiable (customer research validated these)
- QA: Tests iOS and Android (field workers use both)
- Engineering: Prioritizes offline capability (field workers lose signal frequently)

**Phase 5 (Beta & Validation):**

Beta launched with 100 field service users from customer base. Key findings:
- Adoption: 45% of beta users active daily (above 40% target)
- Key metric: Time to access job info: 30 seconds vs. 5 minutes on desktop (validation!)
- Customer feedback: "Photo capture is great, but we need offline access" (scope expansion consideration)
- NPS: 62 (good for B2B SaaS)

**Decision:** Success metrics are on-track. Proceed to launch. Note: Offline sync moves to Phase 2 roadmap.

**Phase 6 (Launch):**

Mobile app launches to all customers. Marketing emphasizes: "Your team in the field, connected to the job. See updates, take photos, track time without leaving the site."

Launch metrics show: 12K signups in first 3 months (above target). 38% adoption among active customers (slightly below 40% target but acceptable). Revenue impact: $1.2M ARR in Year 1 (on pace for $2M in Year 2).

**Phase 7 (Optimization):**

PM Strategy reviews Year 1 outcomes:
- Revenue: On-track to $2M ARR
- Adoption: 38% (slightly below target but healthy growth trajectory)
- Customer feedback: 89% satisfaction; top request for Phase 2 is offline sync
- Market: Competitors launching similar features; time-to-value matters

**Recommendation:** Mobile investment validated. Continue with Phase 2 features. Update strategy for Year 2: expand to new geographic markets + add offline sync to increase adoption to 50%.

---

### Notes for AI Agents

- **PM Strategy is foundational.** All other skills depend on clear strategic direction. If you're working on another skill and strategy is unclear, push back and ask for strategic clarity.
- **Strategy is not one-time; it's continuous.** Re-validate strategy in Phases 1, 5, and 7 as evidence accumulates. Strategy written in Phase 0 may need adjustment.
- **"Evidence" means different things.** Early strategy is backed by market research and customer interviews. Mid-cycle strategy is backed by beta feedback and usage data. Post-launch strategy is backed by customer outcomes and competitive moves.
- **Constraints are features, not obstacles.** Limited budget often forces better prioritization. Small team often forces better focus. Use constraints to sharpen strategy, not as excuses.
- **Success metrics are critical.** Spend time on this. A bad metric creates perverse incentives downstream. Example: If you measure "feature adoption" instead of "business impact," teams will add features customers don't need.
- **Strategy and tactics are different.** Strategy is multi-year vision and positioning. Tactics are quarterly OKRs and near-term initiatives. Both matter; don't confuse them.
- **Communicate relentlessly.** Assume people forget strategy. Repeat it in every stand-up, every meeting, every decision. The more you repeat it, the better decisions teams make.
