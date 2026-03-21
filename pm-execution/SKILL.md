---
name: pm-execution
description: Guide for tactical execution of project plans through sprint management, dependency coordination, and risk tracking. Focuses on day-to-day delivery execution—not strategic planning—ensuring teams stay aligned, blockers are escalated, and realistic schedules are maintained against all constraints.
---

# PM Execution Skill

## Overview

Project Management & Execution focuses on **tactical delivery**: translating strategic roadmaps into executable sprint plans, coordinating dependencies across functions, tracking blockers, and ensuring realistic timeline management. This skill drives teams through iterative delivery cycles while maintaining alignment with design timelines, technical architecture constraints, QA schedules, and launch requirements.

---

## Core PM Execution Responsibilities

### 1. Sprint Planning & Capacity Management
- Break down epics into sprint-sized work items with clear acceptance criteria
- Map team capacity against work to prevent overcommitment
- Balance new features against tech debt and infrastructure work
- Establish velocity baselines and trend analysis
- Plan iteration scope with realistic buffers for unknowns

### 2. Dependency Mapping & Coordination
- Identify and document cross-team dependencies early
- Build dependency maps showing critical path and parallel work streams
- Schedule dependency handoffs with buffer time between phases
- Coordinate with Design for asset delivery dates
- Coordinate with QA for testing schedule integration
- Align Launch timeline with release milestones

### 3. Risk Tracking & Escalation
- Maintain active risk register with probability, impact, and mitigation plans
- Surface technical risks weekly with Tech Arch team
- Flag schedule risks when dates slip or scope creeps
- Establish escalation thresholds and protocols
- Communicate risks transparently to stakeholders

### 4. Blocker Resolution & Unblocking
- Identify blockers in daily standups and sprint reviews
- Categorize blockers by severity and owner
- Drive rapid resolution with appropriate urgency
- Remove dependencies where possible to enable parallel work
- Follow escalation procedures when blockers can't be resolved by team

### 5. Progress Tracking & Visibility
- Track sprint progress daily with burn-down charts
- Update stakeholder dashboards with predictability metrics
- Monitor team utilization and capacity trends
- Flag when predictions shift more than threshold (e.g., 5 days)
- Provide weekly forecast updates on key milestones

### 6. Team Coordination & Communication
- Run daily standups with clear focus on blockers and dependencies
- Facilitate cross-functional planning sessions
- Maintain shared project timeline and work board
- Communicate schedule changes immediately to affected teams
- Ensure alignment on priorities when scope conflicts arise

### 7. Release Planning & Milestone Tracking
- Plan release cycles with clear go/no-go criteria
- Coordinate with QA on testing phases and sign-off timing
- Work with Launch on GTM timeline alignment
- Track readiness against release gates
- Manage launch day coordination and rollback procedures

---

## Best Practices

### 1. Build Realistic Sprint Plans
- Include 20% buffer for unknowns and interruptions
- Validate capacity with actual historical velocity (not wishful thinking)
- Cross-check with Design timeline availability
- Validate against QA capacity for testing windows
- Confirm no conflicts with Launch event dates

### 2. Establish Clear Dependency Protocols
- Document all cross-team dependencies in shared format
- Define "handoff ready" criteria for each dependency
- Build 2-3 day buffers between dependent work phases
- Schedule weekly sync points for coordinated teams
- Assign single owner for each dependency tracking

### 3. Maintain Active Risk Register
- Review risks weekly in planning meetings
- Score risks by probability × impact for prioritization
- Document mitigation plans for all high-risk items
- Update risks in real-time as situations change
- Review risk assumptions monthly with Tech Arch

### 4. Create Escalation Clarity
- Define escalation triggers (e.g., 5+ day slips, tech debt blocking feature, dependency missed)
- Specify escalation path (tech lead → engineering manager → director)
- Include escalation criteria and response SLA (e.g., 24 hours)
- Document resolved escalations to identify patterns
- Review escalation themes monthly for root cause fixes

### 5. Run Effective Daily Standups
- Focus on three items: What's done, what's blocked, what's next
- Address blockers in real-time or schedule rapid follow-up
- Keep standup to 15 minutes (deep-dives happen in parallel)
- Identify dependency impacts early
- Track blocker age to prevent stalled work

### 6. Coordinate Dependencies with Lead Time
- Request Design assets 2 sprints before implementation sprint
- Request Tech Arch dependency reviews 1 sprint ahead
- Book QA testing windows 1 sprint in advance
- Notify Launch of feature readiness at final sprint start
- Confirm Launch GTM timeline conflicts at roadmap level

### 7. Track to Reality, Not Optimism
- Use actual historical velocity, not best-case estimates
- Flag when burn-down deviates from plan before day 3 of sprint
- Surface schedule risks weekly with transparent data
- Adjust future plans based on actual delivery pace
- Celebrate accurate prediction as much as on-time delivery

### 8. Maintain Visible Cross-Functional Alignment
- Publish weekly timeline showing all critical milestones
- Include Design delivery dates, QA test phases, Launch prep
- Show current status (on-track, at-risk, blocked) for each stream
- Highlight dependencies and potential impact zones
- Share publicly to enable self-service dependency checking

---

## Key PM Execution Tools

### 1. **Jira**
- Core platform for sprint planning, backlog management, and work tracking
- Workflow automation for status transitions
- Built-in burn-down charts and velocity tracking
- Custom fields for dependency tagging and risk tracking

### 2. **Asana**
- Portfolio-level timeline and dependency visualization
- Cross-functional work coordination with multiple teams
- Timeline view showing critical path dependencies
- Resource management and capacity planning

### 3. **Monday.com**
- Flexible sprint board with capacity indicators
- Real-time status updates and blocker tracking
- Automations for escalation and notification workflows
- Integration with external tools for dependency feeds

### 4. **Linear**
- Streamlined issue tracking for engineering teams
- Cycle-based planning (alternative to traditional sprints)
- Built-in dependency linking and blocking relationships
- Quick status updates and progress indicators

### 5. **Google Sheets/Confluence**
- Risk register template with scoring and mitigation tracking
- Milestone timelines with color-coded status by function
- Dependency maps and critical path visualization
- Escalation log for pattern analysis

### 6. **Slack Integration Bots**
- Daily blockers and progress notifications
- Escalation alerts to appropriate channels
- Sprint planning reminders and meeting automation
- Real-time dependency status updates

### 7. **Project Management Dashboards** (Tableau/Looker/Metabase)
- Executive dashboards showing on-track/at-risk status
- Velocity trends over 6+ sprint periods
- Capacity utilization by team and skill
- Milestone burn-down and delivery predictability

---

## Integration Points

### Sends to ALL Skills (Coordination Hub)
- **Sprint Schedule**: When sprints start/end, when features are scheduled
- **Milestone Dates**: Key delivery dates and launch readiness points
- **Blocker Alerts**: When external dependencies need resolution
- **Capacity Requests**: When design assets, QA testing, or launch prep is needed

### Receives from PM Strategy
- **Roadmap**: Quarterly/annual initiatives and business priorities
- **Prioritization Framework**: Which features matter most
- **Investment Levels**: Budget and team allocation for roadmap
- **Success Metrics**: What we're optimizing for this quarter

### Receives from Design
- **Asset Timeline**: When design assets will be delivered
- **Design Dependencies**: What backend must support for feature
- **Design Capacity**: How much capacity available for iterations
- **Brand/UX Standards**: Quality bar for implementation

### Receives from Tech Architecture
- **Dependency Map**: What systems are affected by changes
- **Technical Constraints**: Architecture limitations or requirements
- **Infrastructure Timeline**: When infrastructure changes are available
- **Technical Risks**: Known risks in implementation approach
- **API Specs**: Contracts between systems

### Receives from QA
- **Testing Schedule**: When QA can test features (capacity window)
- **Quality Gates**: Acceptance criteria and QA standards
- **Known Issues**: Bugs that block release or require workarounds
- **Test Environment Availability**: When staging/test environments ready

### Receives from Launch
- **GTM Timeline**: Marketing and sales readiness dates
- **Go/No-Go Criteria**: What must be true before launch
- **Launch Date**: Fixed date when feature must be live
- **Post-Launch Plan**: Support and monitoring requirements

### Validation Gate: Realistic Sprint Plans

**Before committing to sprint:**
- ✓ Capacity check: Velocity × team count = realistic work volume
- ✓ Dependency check: All dependencies marked; timeline gaps identified
- ✓ Risk check: Technical risks reviewed with Tech Arch; mitigation plans exist
- ✓ Design check: Design assets scheduled to arrive before work starts
- ✓ QA check: Test phase windows booked; QA capacity confirmed
- ✓ Launch check: No conflicts with GTM events or launch date
- ✓ Buffer check: 15-20% capacity reserved for interruptions

---

## Dependency Mapping Process

### Step 1: Identify All Dependencies
- Map cross-team blockers (Design → Eng, Eng → QA, etc.)
- Identify system dependencies (Backend needs infra, frontend needs API, etc.)
- Surface external dependencies (third-party APIs, vendor deliverables)
- Document known unknowns that could create dependencies

### Step 2: Create Dependency Timeline
```
Design Phase (Sprint -2):    Assets deliver → [2-day buffer]
Implementation Phase (Sprint -1 to +1):  Engineers build → [3-day buffer]  
QA Phase (Sprint +2):        Test and sign-off → [1-day buffer]
Launch Prep (Sprint +3):     Marketing ready + monitoring active
```

### Step 3: Establish Handoff Criteria
For each dependency, define what "ready" means:
- **Design → Eng**: Design assets in shared repo, tech specs reviewed, edge cases documented
- **Eng → QA**: Feature deployed to staging, smoke tests pass, test plan provided
- **QA → Launch**: Feature signed off as production-ready, known issues logged, mitigation plans documented
- **Eng → Infra**: Deployment scripts tested, monitoring configured, rollback plan documented

### Step 4: Build Buffers
- Add 2-3 days between dependent phases for discovery/rework
- Schedule "just-in-time" handoffs (not too early to avoid scope creep)
- Track buffer consumption; if buffers vanish, escalate risk

---

## Risk Tracking Protocol

### Risk Register Template
| Risk | Probability | Impact | Score | Owner | Mitigation | Status |
|------|------------|--------|-------|-------|-----------|--------|
| Design assets late | Medium | High | 6 | Design Lead | Start with wireframes; implement incrementally | Active |
| API endpoint changes | Medium | High | 6 | Tech Arch | Finalize API spec in Sprint 0; test early | Active |
| QA environment outage | Low | Critical | 3 | Ops | Backup environment ready; failover procedure documented | Monitoring |

### Weekly Risk Review Process
1. **Monday**: List all risks and score them (P × I)
2. **Tuesday**: Deep-dive on top 5 risks with owners
3. **Wednesday**: Update mitigation plans; identify new risks
4. **Thursday**: Escalate risks where mitigation failing
5. **Friday**: Report risk summary to stakeholders

### Escalation Triggers
- Risk score > 8 (high probability × high impact)
- Mitigation plan failing or risk probability increasing
- Blocker unresolved for > 2 days
- Schedule slip > 5 days or > 10% of sprint
- Technical blocker affecting multiple sprints

---

## Escalation Procedures

### Blocker Escalation Path
```
Level 1 (Daily): Discuss in standup; try to resolve same-day
         → If unresolved after 4 hours: escalate to tech lead

Level 2 (Tech Lead): Problem-solve with stakeholders; remove blockers
         → If unresolved after 1 day: escalate to engineering manager

Level 3 (Manager): Executive decision-making; allocate resources
         → If unresolved after 1 day: escalate to director

Level 4 (Director): Cross-functional resolution; change priorities if needed
         → Director has authority to replan or add resources
```

### Escalation Communication
- **Format**: Slack notification + email to escalation chain
- **Content**: What's blocked, impact on timeline, requested action, deadline for decision
- **Frequency**: Every 24 hours until resolved
- **Resolution**: Log resolution and review for patterns

### Schedule Risk Escalation
- **Threshold**: 5+ days of slip on any milestone
- **Action**: Notify PM Strategy and affected teams immediately
- **Timeline**: Decision on replanning within 48 hours
- **Recovery**: Identify what can be moved to next sprint; assess market impact

---

## Sprint Planning Template

### Sprint Name: [Project] - Sprint [Number] - [Dates]

**Velocity Target**: [Historical velocity] + [Risk adjustments]

**Capacity Available**: [Team size] × [Historical velocity] = [Available hours]

**High-Level Goals**:
1. [Feature or outcome 1]
2. [Feature or outcome 2]
3. [Feature or outcome 3]

**Dependencies**:
- [ ] Design assets for Feature A (due Date X)
- [ ] API spec from Tech Arch (due Date Y)
- [ ] QA environment ready (due Date Z)

**Known Risks**:
- [Risk 1 - probability/impact]
- [Risk 2 - probability/impact]

**Blockers To Resolve Before Sprint Start**:
- [ ] Blocker 1 (owner, target resolution date)
- [ ] Blocker 2 (owner, target resolution date)

**Milestone Alignment**:
- [ ] On track for Design delivery? (confirm with Design lead)
- [ ] On track for Launch date? (confirm with Launch lead)
- [ ] QA testing window available? (confirm with QA lead)

---

## Weekly Standup Agenda

**Time**: 15 minutes | **Frequency**: Daily (or 3x/week minimum)

**Agenda**:
1. **What's Done** (3 min): Recap completed work; celebrate wins
2. **What's Blocked** (5 min): Surface all blockers; assign resolution owners and target time
3. **What's Next** (5 min): Next 2-3 days priorities; preview upcoming blockers
4. **Dependencies** (2 min): Any handoff status changes; confirm timeline still on track

**Post-Standup**:
- Resolve blockers in parallel breakout sessions
- Update Jira/project board with status
- Escalate if blocker can't be resolved within 4 hours

---

## Milestone Tracking Dashboard

**Key Metrics to Track**:
- Sprint velocity (historical trend)
- On-time delivery rate by team
- Blocker age (days unresolved)
- Dependency handoff delays (vs. planned)
- Risk register score trend
- Schedule accuracy (predicted vs. actual)

**Weekly Report Template**:
```
SPRINT STATUS: [On Track / At Risk / Blocked]

Velocity:          [Completed pts] / [Committed pts] = [% done]
Blockers:          [Count] active, [Age] avg age
Risk Score:        [Aggregate score] vs. [Target]
Schedule Buffer:   [Days remaining] vs. [Contingency days]
Next Milestone:    [Date] - [Status]
Escalations:       [Count] in progress, [Count] resolved this week
```

---

## Key Metrics for PM Execution

### Delivery Predictability
- **Sprint Accuracy**: % of sprints where committed work = delivered work (target: 85%+)
- **Milestone On-Time**: % of key milestones hit on schedule (target: 90%+)
- **Velocity Consistency**: Sprint-to-sprint variance (target: ±10%)

### Team Health
- **Blocker Resolution Time**: Hours from identification to resolution (target: < 24h for critical)
- **Unplanned Work %**: % of sprint capacity consumed by interruptions (target: < 20%)
- **Team Utilization**: % of capacity used (target: 75-85%)

### Cross-Functional Alignment
- **Dependency Success Rate**: % of planned handoffs completed on schedule (target: 90%+)
- **Design Iteration Loops**: Number of design revisions per feature (target: 2-3)
- **Risk Escalation Resolution Time**: Days to resolve escalated risks (target: < 5 days)

### Schedule Management
- **Schedule Variance**: Planned vs. actual completion dates (target: ±2 days)
- **Buffer Consumption**: % of sprint buffer used (target: < 50%)
- **Rework Rate**: % of work that requires rework (target: < 10%)

