---
name: Quality Assurance & Testing
description: Ensure product quality through shift-left testing, comprehensive test coverage, and continuous quality validation from design through launch. QA participates from Week 8 onward with expanded responsibilities in test planning, automation, performance validation, and security testing.
---

# Quality Assurance & Testing Skill

This skill guides QA teams through shift-left quality practices, starting early with testability reviews and expanding significantly during build phase to ensure products are reliable, performant, and production-ready before launch.

---

## When QA Engages

**Involvement Timeline:**
- **Phase 1-2 (Weeks 1-4):** Strategy & Planning - Minimal engagement; QA monitors requirements
- **Phase 3-4 (Weeks 5-8):** Concept & Architecture - **EXPANDED ROLE** - QA begins testability reviews, test planning, and test case creation
- **Phase 5-6 (Weeks 9-12):** Build & Refinement - **PRIMARY PHASE** - QA executes testing, performs load testing, security validation, and defect management
- **Phase 7 (Weeks 12+):** QA & Launch - Final quality sign-off, production readiness validation, post-launch monitoring

---

## Top QA Responsibilities (Shift-Left Emphasis)

1. **Testability Review & Test Planning** (Week 8+) - Review design and architecture for testability gaps; create comprehensive test plans, test case matrices, and acceptance criteria
2. **Functional Testing & Defect Management** - Execute manual and automated tests; track, reproduce, and prioritize defects; verify fixes
3. **Automation Strategy & Framework Setup** (Week 8+) - Design test automation architecture; create page objects, test utilities, CI/CD integration
4. **Performance & Load Testing** (Week 9+) - Define performance baselines, execute load tests, identify bottlenecks, validate scaling behavior
5. **Security Testing & Compliance Validation** - Conduct security testing (authentication, authorization, input validation), compliance validation
6. **Accessibility Testing & WCAG Compliance** - Validate WCAG AA compliance, screen reader testing, keyboard navigation, color contrast verification
7. **Integration & End-to-End Testing** - Test system integration, data flows, API contracts, third-party integrations
8. **Release Readiness & Production Validation** - Conduct final quality gate, production environment validation, smoke tests post-launch

---

## Best Practices: DOs and DON'Ts

### DOs

1. **Start testability review in Week 8** - Review design specs and architecture with Dev before development; identify testing gaps and edge cases early
2. **Create detailed test case matrices** - For each feature, document positive cases, negative cases, edge cases, state combinations, and error scenarios
3. **Automate the right tests** - Automate regression tests, happy paths, and data-heavy scenarios; keep complex manual tests and exploratory testing for humans
4. **Test against acceptance criteria** - Use acceptance criteria from design and PM as the source of truth; QA doesn't define quality
5. **Perform performance testing early** - Load test early and often; identify bottlenecks in Week 10-11, not during final launch validation
6. **Include security testing proactively** - Test authentication, authorization, input validation, and data protection as part of functional test execution
7. **Test accessibility throughout development** - Use screen readers and keyboard navigation during feature development; don't defer accessibility testing
8. **Validate against multiple browsers/devices** - Test on actual devices and browsers customers use; don't rely solely on emulators

### DON'Ts

1. **Don't wait until week 12 to start testing** - Shift-left means QA engages Week 8 with testability review; delaying until week 12 guarantees launch delays
2. **Don't test without written test cases** - Avoid ad-hoc testing; document what you're testing, why, and what passes/fails for consistency and traceability
3. **Don't automate the wrong things** - Avoid automating UI tests that are brittle (visual regression); focus automation on logic, data validation, and workflows
4. **Don't defer security testing** - Don't skip OWASP testing, authentication/authorization testing, and data protection validation thinking "we'll address it later"
5. **Don't test without understanding acceptance criteria** - Don't assume you know what "done" looks like; get written acceptance criteria from PM and Design
6. **Don't skip performance baseline establishment** - Don't test performance only at launch; establish performance baselines and metrics early
7. **Don't consider accessibility "nice to have"** - Don't defer accessibility testing; WCAG AA compliance is required for quality products

---

## Key QA Tools & Artifacts

1. **Test Management Platform** (TestRail, Zephyr, Azure Test Plans) - Manage test cases, test runs, defect tracking, and test coverage reporting
2. **Functional Test Automation** (Selenium, Cypress, Playwright, WebDriver) - Create automated UI and API tests; execute regression test suites in CI/CD
3. **Performance Testing Tools** (JMeter, Gatling, k6, LoadRunner) - Execute load tests, baseline performance, identify bottlenecks and scaling limits
4. **API Testing Tools** (Postman, SoapUI, REST Assured) - Test API contracts, request/response validation, authorization testing
5. **Security Testing Tools** (OWASP ZAP, Burp Suite, Snyk) - Conduct vulnerability scanning, penetration testing, dependency checking
6. **Accessibility Testing Tools** (Axe, WAVE, NVDA Screen Reader, Lighthouse) - Test WCAG AA compliance, screen reader compatibility, keyboard navigation
7. **Bug Tracking & Reporting** (Jira, Azure DevOps, GitHub Issues) - Log defects with reproduction steps, evidence (screenshots, videos), severity, and priority
8. **Continuous Integration & Testing** (Jenkins, GitHub Actions, GitLab CI) - Automate test execution, report results, block merges on test failure

---

## QA Integration Points

### QA Sends To:
- **PM Strategy** - Quality metrics, defect trends, test coverage reporting, risk assessments for future releases
- **All Skills** (Design, Tech Arch, PM Execution, Development) - Test coverage reports, defect feedback, performance metrics, acceptance validation
- **Launch** - Final quality sign-off, production readiness assessment, known limitations and workarounds

### QA Receives From:
- **Design** - Design specifications, acceptance criteria, accessibility requirements, state matrices
- **Tech Architecture** - Performance budgets, API contracts, security requirements, scalability testing parameters
- **PM Execution** - Sprint schedule, feature priority, timeline constraints, definition of done criteria
- **Development** - Code commits, test results, build status, defect analysis and root causes

### QA Validation Gate
**Final Quality Sign-Off** - Before launch:
- Test coverage >80% for critical functionality (measured by test case execution)
- All critical and high-severity defects resolved; medium defects assessed and accepted/deferred
- Performance testing validates system meets defined performance budgets
- Security testing confirms OWASP Top 10 risks mitigated
- Accessibility audit confirms WCAG AA compliance
- Load testing validates system can handle anticipated user load with acceptable performance
- Smoke tests pass in production environment
- Regression test suite passes; no new failures introduced
- Release notes document known limitations and workarounds
- Customer-facing documentation (help text, error messages) is accurate and clear

---

## QA's Expanded "Shift-Left" Role (Starting Week 8)

### Week 8-9: Testability Review & Test Planning
- Review design specifications for testability: Are all states documented? Are edge cases clear?
- Review architecture with Dev for testing implications: How do we test integrations? What about error scenarios?
- Create detailed test plans: Feature scope, test scenarios, manual vs. automated approach, test environment requirements
- Define acceptance criteria for each feature (partner with PM and Design to clarify)
- Create test case matrix with positive cases, negative cases, edge cases, error scenarios, state combinations
- Identify performance testing requirements and load test scenarios
- Identify security testing requirements (authentication, authorization, data validation, encryption)
- Identify accessibility testing requirements (WCAG AA conformance, screen reader compatibility)

### Week 9-10: Automation Framework & Test Execution Begins
- Set up test automation framework (page objects, test utilities, CI/CD integration)
- Create automated regression tests for completed features
- Develop automation around critical workflows and data-heavy scenarios
- Begin manual exploratory testing of completed features
- Execute performance baseline tests; identify performance hotspots early
- Conduct security testing on authentication and authorization mechanisms
- Test accessibility of released features using NVDA/JAWS and keyboard navigation

### Week 10-11: Load Testing & Performance Validation
- Execute load testing at anticipated user volume + 2x headroom
- Identify performance bottlenecks; share results with Tech Arch for optimization
- Validate caching strategy effectiveness
- Test under degraded conditions (high latency, packet loss)
- Measure metrics: page load time, API latency, database query performance, third-party service impact

### Week 11-12: Integration Testing & Final Quality Checks
- Execute end-to-end tests covering complete workflows
- Test API integrations with third-party services
- Validate data flow across system components
- Conduct final security testing (OWASP Top 10 validation)
- Execute final accessibility audit
- Perform smoke tests in production environment
- Verify documentation accuracy against actual behavior

**Shift-Left Principle:** QA engaged in Week 8, not Week 12, means:
- Testability issues caught early; design/architecture improved before development
- Automation framework in place from the start; testing scales with development pace
- Performance issues found mid-development, not at launch
- Security and accessibility integrated into quality checks, not bolted on at the end
- Launch delays prevented through continuous quality validation instead of final-phase firefighting

---

## Test Case Matrix Template

For each feature, document:

```
Feature: [Feature Name]
Acceptance Criteria: [From PM/Design]

| Test Case ID | Scenario | Steps | Expected Result | Automated? | Priority |
|---|---|---|---|---|---|
| TC-001 | Happy Path | 1. Do X 2. Do Y | Z happens | Yes | Critical |
| TC-002 | Error - Invalid Input | 1. Enter invalid X | Error message displayed | Yes | High |
| TC-003 | State Combo - A+B | 1. Set A 2. Set B | Combined behavior works | Manual | High |
| TC-004 | Edge Case - Boundary | 1. Enter max value | System handles gracefully | Yes | Medium |
| TC-005 | Performance - Load | 1. Load with 1000 users | Page load <2s | Automated Load Test | High |
| TC-006 | Accessibility - Keyboard | Navigate entire feature using keyboard | All interactions reachable | Manual | Critical |
| TC-007 | Security - XSS | Enter script tags in input | Input sanitized; script blocked | Automated | Critical |
```

---

## QA Readiness Checklist

**Week 8-9: Testability Review Complete**
- [ ] Design specifications reviewed for testability gaps; issues documented
- [ ] Architecture reviewed for testing implications
- [ ] Test plan created and approved by PM and Tech Arch
- [ ] Acceptance criteria clarified and documented
- [ ] Test case matrix completed for all planned features
- [ ] Performance budget and load test scenarios defined
- [ ] Security testing scope documented
- [ ] Accessibility requirements documented

**Week 10-12: Testing in Progress**
- [ ] Automation framework set up and operational
- [ ] Regression tests created and passing
- [ ] Manual test execution on schedule; defects logged and tracked
- [ ] Performance baseline established; load tests initiated
- [ ] Security testing underway; vulnerabilities logged
- [ ] Accessibility testing ongoing; non-compliance issues documented

**Week 12+ : Final Quality Sign-Off**
- [ ] Test coverage >80% achieved
- [ ] All critical/high defects resolved; medium defects assessed
- [ ] Performance testing complete; system meets budgets
- [ ] Security audit complete; OWASP Top 10 risks mitigated
- [ ] Accessibility audit complete; WCAG AA compliance confirmed
- [ ] Load testing complete; scaling behavior validated
- [ ] Production smoke tests pass
- [ ] Release notes complete with known limitations

---

## Success Metrics

- **Test Coverage:** >80% of functionality covered by test cases
- **Defect Detection Rate:** Quality issues caught before production (defect escape rate <1%)
- **Time to Fix:** Average defect resolution time <2 days for critical, <1 week for high
- **Performance Validation:** System meets defined performance budgets under load
- **Security Compliance:** Zero OWASP Top 10 vulnerabilities in security testing
- **Accessibility Compliance:** Zero WCAG AA violations in accessibility audit
- **Launch Readiness:** Zero critical/high defects at launch; all systems smoke-tested in production
- **Automation ROI:** Automated tests execute in <5 minutes; regression suite provides >70% coverage
