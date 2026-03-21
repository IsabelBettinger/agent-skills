---
name: Technical Architecture & System Design
description: Define technical foundations, system design, and feasibility validation for products. Ensures architectural decisions enable product goals, support scalability, and provide clear implementation guidance for development teams.
---

# Technical Architecture & System Design Skill

This skill guides technical architects through system design, feasibility validation, and architectural decision-making, emphasizing early collaboration with PM and Design to validate product requirements are technically sound.

---

## When Tech Architecture Engages

**Involvement Timeline:**
- **Phase 1-2 (Weeks 1-4):** Strategy & Planning - Tech Arch evaluates feasibility, identifies risks, validates PM approach is technically sound
- **Phase 3-4 (Weeks 5-8):** Concept & Architecture - Tech Arch leads technical design, creates architecture diagrams, defines API contracts
- **Phase 5-6 (Weeks 9-12):** Build & Refinement - Tech Arch supports implementation, approves critical decisions, ensures adherence to design
- **Phase 7 (Weeks 12+):** QA & Launch - Tech Arch validates performance, approves scaling decisions, supports production readiness

---

## Top Technical Architecture Responsibilities

1. **Feasibility Analysis & Risk Assessment** - Evaluate PM requirements for technical feasibility, identify risks, propose mitigation strategies
2. **System Architecture Design** - Design system components, data flows, integrations, and scaling approach
3. **API & Data Contract Definition** - Define API schemas, data models, and integration contracts for frontend and backend teams
4. **Technology Selection & Evaluation** - Recommend technology stack, libraries, and frameworks; justify choices against alternatives
5. **Performance & Scalability Planning** - Define performance budgets, caching strategies, database optimization, and scaling architecture
6. **Security & Compliance Architecture** - Design authentication, authorization, data protection, and compliance requirements into system
7. **Infrastructure & DevOps Design** - Plan deployment architecture, CI/CD pipeline, monitoring, logging, and infrastructure automation

---

## Best Practices: DOs and DON'Ts

### DOs

1. **Validate PM feasibility early** - In Phase 1-2, conduct feasibility review of business requirements and alert PM to technical risks or constraints
2. **Design for the actual scale** - Understand real user volume, data volume, and growth projections; don't over-architect for imagined scale
3. **Create architecture artifacts** - Document system design with diagrams (data flow, component interaction, deployment topology)
4. **Define clear API contracts** - Specify endpoint schemas, authentication, rate limiting, and error codes before development starts
5. **Plan for failure modes** - Design for graceful degradation, circuit breakers, retry logic, and monitoring for failure detection
6. **Document architectural decisions** - Record ADRs (Architecture Decision Records) explaining the "why" behind major choices
7. **Establish security from the foundation** - Integrate threat modeling, data classification, and security controls into initial architecture design

### DON'Ts

1. **Don't design in isolation** - Never create architecture without understanding PM business requirements and Design interaction complexity
2. **Don't ignore operational constraints** - Don't propose architecture that requires infrastructure expertise or operational complexity the team can't support
3. **Don't overengineer for future needs** - Avoid adding layers of abstraction, service boundaries, or complexity for features not in scope
4. **Don't skip performance planning** - Don't assume performance will be acceptable; define performance budgets and validate through load testing
5. **Don't defer security decisions** - Don't postpone security architecture to later phases; security must be designed from the foundation
6. **Don't design without knowing team capability** - Don't recommend technologies or patterns the team lacks expertise to maintain and debug
7. **Don't lock in decisions without alternatives** - Avoid making irreversible architectural choices without documenting alternatives and tradeoffs

---

## Key Architecture Tools & Artifacts

1. **Architecture Diagramming** (Miro, Lucidchart, ArchiMate) - Create system architecture, data flow, and deployment topology diagrams
2. **API Definition & Documentation** (OpenAPI/Swagger, AsyncAPI) - Specify API contracts, schemas, and integration points
3. **Database Design Tools** (DBDiagram, Vertabelo) - Design relational schemas, data models, and query optimization
4. **Performance Testing Tools** (JMeter, Gatling, k6) - Load test system, identify bottlenecks, validate scaling assumptions
5. **Infrastructure as Code** (Terraform, CloudFormation) - Define infrastructure as code, version control deployment topology
6. **Monitoring & Observability** (Prometheus, ELK, Datadog) - Design monitoring strategy, logging, and alerting architecture
7. **Security & Compliance Tools** (OWASP threat modeling, ZAP) - Conduct threat modeling, security audits, compliance validation
8. **Architecture Decision Records (ADRs)** - Document major decisions with context, alternatives, and consequences

---

## Tech Architecture Integration Points

### Tech Architecture Sends To:
- **PM Strategy** - Feasibility assessment, timeline impact analysis, technical constraints affecting product scope
- **Design** - Technical constraints on interaction patterns, performance budgets, responsive design feasibility
- **PM Execution** - Architecture specifications, technology choices, implementation guidance for dev teams
- **QA** - Performance budgets, scalability testing requirements, security testing scope

### Tech Architecture Receives From:
- **PM Strategy** - Business requirements, scale assumptions, timeline and resource constraints, success metrics
- **Design** - Interaction patterns, performance requirements, component complexity, accessibility implications

### Tech Architecture Validation Gate
**Feasibility & Architecture Sign-Off** - Before handoff to development:
- PM requirements reviewed for technical feasibility; risks and constraints documented
- Architecture diagram created showing system components, data flows, and integrations
- API contracts fully specified with schemas, authentication, error handling, rate limiting
- Technology stack justified against alternatives with clear decision rationale
- Performance budgets and scalability assumptions validated through load testing
- Security threat modeling completed; authentication, authorization, and data protection designed
- Infrastructure/DevOps requirements documented; team capability verified for chosen approach
- Dev team confirms architecture is understood and implementable within timeline

---

## Tech Architecture's Feasibility Validation (Phase 1-2)

### Week 1-2: Requirements Review & Risk Assessment
- Participate in requirements workshop; ask clarifying questions on scale, performance, and constraints
- Conduct quick feasibility assessment: Can this be built with current tech? What are the risks?
- Identify technical blockers (external APIs, database requirements, infrastructure needs)
- Propose architecture at 30,000-foot level; identify alternative approaches
- Flag performance, security, or scalability concerns early to PM

### Week 3-4: Preliminary Architecture & Collaboration
- Share draft architecture with Design and PM; understand interaction complexity and performance implications
- Define technology recommendations with rationale
- Identify gaps in requirements (e.g., performance targets, scale assumptions)
- Create preliminary data model and API structure
- Assess team capability to execute chosen approach

**Feasibility Validation Principle:** By week 4, PM, Design, and Tech Arch must align on whether the product vision is technically achievable in scope and timeline. Early risk surfacing prevents expensive discoveries during development.

---

## Architecture Decision Record (ADR) Template

For every major architectural decision, document:

```
# ADR [Number]: [Decision Title]

## Context
What business or technical problem requires this decision?

## Decision
What did we choose and why?

## Alternatives Considered
What other approaches did we evaluate? Why weren't they chosen?

## Consequences
What are the tradeoffs and long-term implications?

## Related ADRs
Links to related decisions or dependencies.
```

---

## Critical Architecture Review Checklist

Before development begins, confirm:
- [ ] PM business requirements understood and validated as technically feasible
- [ ] Scale assumptions documented (users, data volume, API request volume)
- [ ] Architecture diagram created showing all components and data flows
- [ ] API schemas defined for all frontend-backend, service-to-service, and third-party integrations
- [ ] Database schema designed and normalized appropriately
- [ ] Performance budgets set (page load time, API latency, database query time)
- [ ] Caching strategy defined (HTTP caching, CDN, application-level caching)
- [ ] Authentication & authorization approach specified
- [ ] Data protection and compliance requirements addressed
- [ ] Monitoring, logging, and alerting architecture designed
- [ ] Infrastructure topology documented; cloud platform and services identified
- [ ] Deployment strategy defined (blue-green, canary, rolling deployment)
- [ ] Team capability assessed for chosen technology and patterns

---

## Success Metrics

- **Feasibility Accuracy:** No architectural surprises during development; >90% of architecture remains unchanged post-design review
- **Performance Achievement:** System meets defined performance budgets at launch
- **Development Velocity:** Clear architecture reduces implementation questions and rework cycles
- **Scalability Readiness:** System can handle 3x initial user/data volume without architectural changes
- **Security Compliance:** Zero security vulnerabilities in architecture audit; all compliance requirements met
- **Operational Efficiency:** Monitoring and alerting catch issues before customer impact; <15 min mean time to detection
