# BMAD Complete Process Flow - Master Agent Orchestration

## CRITICAL: BMAD Master Agent Coordination Protocol

**🎯 BMAD MASTER IS THE GOD'S-EYE TASKMASTER FOR ALL STORY/DEVELOPMENT CYCLES**

### BMAD Master Orchestration Framework

**BMAD Master** serves as the central orchestrator with complete oversight and control:

#### Story Initiation and Decomposition
- **Story Analysis**: Receives story requirements and performs comprehensive analysis
- **Task Breakdown**: Decomposes story into specialist-specific tasks with clear deliverables
- **Agent Selection**: Identifies which specialist agents are needed for the story
- **Dependency Mapping**: Maps inter-agent dependencies and handoff requirements

#### Specialist Agent Delegation Structure
BMAD Master coordinates these specialist agents:
- **🏗️ Architect**: System design, technical planning, architecture decisions
- **🔌 API Specialist**: API design, implementation, integration endpoints
- **🔗 Integration Agent**: Third-party integrations, OAuth, external services
- **🎨 UX/UI Specialist**: User experience validation, design consistency, accessibility
- **🧪 QA Agent**: Testing protocols, quality assurance, validation
- **⚡ Performance Agent**: Optimization, monitoring, performance tuning  
- **📊 Data Architect**: Database design, migrations, data modeling

#### Master Orchestration Responsibilities
1. **📋 Master Todo Management**: Maintains comprehensive todo lists across ALL specialist agents
2. **🔄 Task Coordination**: Manages handoffs between specialists with clear deliverable requirements
3. **📊 Progress Consolidation**: Aggregates status updates from all agents into unified progress reports
4. **🚨 Quality Gate Enforcement**: Ensures ALL specialists follow Django protection protocols
5. **🧠 Knowledge Integration**: Synthesizes specialist expertise into cohesive implementation plans
6. **⚖️ Resource Optimization**: Balances workload and optimizes specialist utilization
7. **📁 Epic Organization**: Manages epic creation process and file organization standards

#### Epic Creation and Organization Standards
**MANDATORY for all epic creation processes:**

- **Epic Storage Location**: All new epics MUST be created in `/original-bmad/epics/[epic-name]/`
- **Epic Directory Structure**: 
  ```
  /original-bmad/epics/[epic-name]/
  ├── epic-overview.md
  └── stories/
      ├── story-[epic-name]-001-[story-name].md
      ├── story-[epic-name]-002-[story-name].md
      └── ...
  ```
- **Story Organization**: All stories for an epic MUST reside in that epic's `/stories/` subdirectory
- **Naming Conventions**: Epic directories use kebab-case, stories follow `story-[epic-name]-[number]-[story-name].md` format

#### Specialist Agent Handoff Protocol
```
BMAD Master → Story Analysis → Agent Assignment → Task Delegation → Progress Monitoring → Quality Verification → Integration → Delivery
```

**Each handoff includes:**
- Clear task specifications with acceptance criteria
- Required deliverables and documentation standards
- Django protection protocol requirements
- Reporting and communication expectations

## CRITICAL: Django Web Application Integrity Requirements  

**ALL SPECIALIST AGENT WORK MUST PRESERVE DJANGO WEB APPLICATION FUNCTIONALITY**

### Phase 0: MANDATORY Django QA Pre-Check (BEFORE ANY WORK)

**🚨 BEFORE starting any development work, ALL agents MUST:**

1. **Django Verification Check**
   ```bash
   python manage.py check --deploy
   python manage.py runserver --check-migrations
   ```

2. **Required File Verification**
   - ✅ `manage.py` exists and is executable
   - ✅ `example_django/` directory with all Django config files
   - ✅ `webapp/` directory with all models, views, templates
   - ✅ `api/`, `projects/`, `analytics/`, `billing/`, `videos/` Django apps
   - ✅ All Django migrations are applied (`python manage.py migrate`)

3. **Functional Verification**
   - ✅ Django server starts successfully without errors
   - ✅ All URL patterns resolve correctly  
   - ✅ Database connections work
   - ✅ Templates and static files load

**❌ STOP WORK IMMEDIATELY if any Django verification fails**

### Phase 8.12: MANDATORY Django QA Post-Check (AFTER ANY WORK)

**🚨 AFTER completing any development work, ALL agents MUST:**

1. **Django Restoration Verification**
   ```bash
   # Test that Django app still works
   python manage.py check
   python manage.py migrate  # Apply any new migrations
   python manage.py runserver # Must start without errors
   ```

2. **Critical File Protection**
   - ✅ NEVER delete or move Django core files
   - ✅ NEVER remove Django apps without explicit instruction
   - ✅ NEVER modify Django settings without understanding impact
   - ✅ ALWAYS preserve Django model relationships

3. **Quality Gates**
   - ✅ **Django Functionality Gate**: Web server must start successfully
   - ✅ **Migration Gate**: All migrations must apply cleanly
   - ✅ **Template Gate**: All Django templates must be accessible
   - ✅ **Model Gate**: All Django models must be importable

### Phase 8.13: Django Recovery Protocol (IF DJANGO BREAKS)

**If Django web application functionality is compromised:**

1. **Immediate Assessment**
   ```bash
   git status  # Check what files were modified
   python manage.py check  # Identify specific errors
   ```

2. **Recovery Options (in order of preference)**
   ```bash
   # Option 1: Restore from working branch
   git checkout bmad-1 -- manage.py example_django/ webapp/ api/ projects/ analytics/ billing/ videos/
   
   # Option 2: Restore from git stash
   git stash pop
   
   # Option 3: Reset to last working commit
   git reset --hard HEAD~1
   ```

3. **Post-Recovery Verification**
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

### ENFORCED AGENT COMPLIANCE RULES

**🚨 NO EXCEPTIONS - These rules are MANDATORY:**

#### Rule 1: Django Preservation Priority
- Django web application functionality has ABSOLUTE PRIORITY over any other development task
- If ANY conflict exists between a development task and Django functionality, Django wins
- Agent work is INVALID if it breaks Django web application

#### Rule 2: Pre-Work Django Verification
- EVERY agent MUST verify Django functionality before starting work
- Use `python manage.py runserver` test as the gold standard
- Document Django status in commit messages

#### Rule 3: Post-Work Django Testing
- EVERY agent MUST test Django functionality after completing work
- If Django is broken, work is considered FAILED regardless of other success
- Must fix Django issues before marking work complete

#### Rule 4: File Protection Standards
- NEVER delete files from: `webapp/`, `example_django/`, `api/`, `projects/`, `analytics/`, `billing/`, `videos/`
- NEVER remove `manage.py` 
- NEVER delete Django migrations without explicit instruction
- ALWAYS preserve Django model relationships and foreign keys

#### Rule 5: Recovery Responsibility
- If an agent breaks Django functionality, that agent MUST fix it before completion
- Recovery procedures are non-negotiable requirements
- Failed recovery results in escalation to human oversight

### Quality Assurance Checklist

**✅ Pre-Work Checklist:**
- [ ] Django server starts without errors
- [ ] All migrations are applied
- [ ] All Django apps are accessible
- [ ] All critical files exist

**✅ Post-Work Checklist:**
- [ ] Django server still starts without errors
- [ ] No new migration conflicts
- [ ] All Django functionality preserved
- [ ] All tests pass (if applicable)

### Emergency Escalation

**If Django recovery fails after following all protocols:**

1. **Document the failure state**
   ```bash
   git status > django_failure_report.txt
   python manage.py check 2>&1 >> django_failure_report.txt
   ```

2. **Create emergency branch**
   ```bash
   git checkout -b emergency/django-recovery-$(date +%Y%m%d-%H%M%S)
   git add django_failure_report.txt
   git commit -m "EMERGENCY: Django functionality compromised - requires human intervention"
   ```

3. **Escalate to human oversight** with complete failure documentation

---

## Core BMAD Process Flow (Master Agent Orchestration Model)

### Phase 1: BMAD Master Story Analysis & Agent Assignment
**🎯 BMAD Master Responsibilities:**
- Story analysis and decomposition into specialist tasks
- **🏗️ Architect Assignment**: Technical planning and Django impact assessment
- Resource allocation and specialist timeline coordination
- Risk assessment including Django functionality protection requirements

### Phase 2: Environment Setup & Validation (Architect + BMAD Master)
**🏗️ Architect Deliverables:**
- Development environment configuration
- **🚨 Django Baseline Verification**: Document current Django state
- Tool chain validation and initial codebase analysis

**🎯 BMAD Master Oversight:** Monitor Django verification completion

### Phase 2.5: UI/UX Design Validation (UX/UI Specialist + BMAD Master)
**🎨 UX/UI Specialist Responsibilities:**
- [ ] Review existing design system and theme consistency
- [ ] Validate that new features match existing UI patterns
- [ ] Ensure responsive design works across device sizes  
- [ ] Check accessibility compliance (WCAG 2.1 standards)

**🎨 UX/UI Design Consistency Tasks:**
- Apply existing theme and design patterns
- Ensure brand consistency across all pages
- Validate color scheme, typography, and spacing
- Check component reuse and design system adherence

**🎯 BMAD Master Integration:** Coordinate UX/UI findings with Architecture phase

### Phase 3: Design & Architecture (Architect → Handoff to Implementation Specialists)
**🏗️ Architect Deliverables:**
- Solution architecture design with Django integration planning  
- Component interface specifications
- **📊 Data Architect Coordination**: Database design preserving Django models

**🎯 BMAD Master Coordination:** Orchestrate handoff to implementation specialists

### Phase 4: Implementation & Development (Implementation Specialists + UX/UI)
**🔌 API Specialist / 🔗 Integration Agent Tasks:**
- **🚨 Pre-Implementation Django Check** (Phase 0)
- Code implementation following architect specifications
- Unit test development and execution

### Phase 4.5: UX Flow Validation (UX/UI Specialist + BMAD Master)
**🎨 UX/UI Specialist Flow Validation:**
- [ ] Test all user navigation flows end-to-end
- [ ] Validate page transitions and user feedback
- [ ] Ensure consistent styling across all pages
- [ ] Check error messages and success states

**🎨 Navigation Flow Validation Tasks:**
- Test all clickable elements and navigation paths
- Ensure no unstyled intermediate pages
- Validate user feedback and error states  
- Check mobile navigation and responsive behavior

**🎨 Integration with Implementation Specialists:**
- Collaborate on technical feasibility of UX improvements
- Ensure UX requirements can be implemented within Django constraints
- Guide template and view implementation for optimal user experience

**🎯 BMAD Master Oversight:** Coordinate specialist handoffs and monitor Django protection

### Phase 5: Integration & Testing (QA Agent + Performance Agent)
**🧪 QA Agent Responsibilities:**
- Component integration testing
- **🚨 Django Integration Testing**: Verify Django still works with changes
- End-to-end testing and security assessment

**⚡ Performance Agent Tasks:** Performance validation and optimization
**🎯 BMAD Master Integration:** Consolidate QA and performance reports

### Phase 6: Validation & Quality Assurance (QA Agent + UX/UI Final Audit)
**🧪 QA Agent Final Validation:**
- Comprehensive testing execution
- **🚨 Django Functionality Validation**: Full Django QA testing
- Security assessment

### Phase 6.5: Complete UX Audit (UX/UI Specialist + BMAD Master)
**🎨 UX/UI Specialist Final Audit:**
- [ ] Comprehensive user experience testing
- [ ] Visual consistency audit across entire application
- [ ] Mobile responsiveness validation
- [ ] Performance impact of UI changes

**🎨 UX/UI Quality Gates:**
- **UX Gate**: All user flows must be professionally styled and functional
- **Navigation Gate**: No broken or unstyled intermediate pages allowed
- **Mobile Gate**: All features must work on mobile devices  
- **Accessibility Gate**: Basic accessibility requirements must be met

**🎨 UX/UI Validation Checklist - For Every Story Implementation:**
- [ ] All new pages styled consistently with existing theme
- [ ] Navigation flows tested end-to-end by clicking through
- [ ] No unstyled or default framework pages exposed to users
- [ ] Error states and success feedback properly designed
- [ ] Mobile responsiveness verified
- [ ] Accessibility basics validated (contrast, focus states)

**🎨 OAuth/Authentication Specific Validation:**
- [ ] OAuth provider pages styled to match application theme
- [ ] Smooth transitions between application and provider pages
- [ ] Clear user guidance throughout authentication flows
- [ ] Error handling with professional, branded error pages
- [ ] Consistent button styling and branding guidelines

**🎨 Integration with Architecture Specialists:**
- Influence architecture decisions based on UX requirements
- Ensure UI components can be properly modularized
- Guide frontend architecture for scalable user interfaces

**🎯 BMAD Master Quality Gates:** Enforce all specialist quality standards including UX/UI professional standards

### Phase 7: Deployment Preparation (Integration Agent + BMAD Master)
**🔗 Integration Agent Tasks:**
- Production environment setup
- **🚨 Django Production Readiness**: Ensure Django deployment compatibility
- Deployment script preparation and rollback procedures

**🎯 BMAD Master Deployment Oversight:** Final deployment authorization

### Phase 8: Git Workflow & Version Control (BMAD Master Enforced)
- **Phase 8.10**: MANDATORY Remote Branch Push immediately after commit
- **Phase 8.11**: MANDATORY Enterprise Integration Workflow understanding  
- **🚨 Phase 8.12**: MANDATORY Django QA Post-Check (BMAD Master verified)
- **🚨 Phase 8.13**: Django Recovery Protocol (if needed)

### Phase 9: Documentation & Knowledge Transfer (Data Architect + BMAD Master)
**📊 Data Architect Responsibilities:**
- **🚨 Django Status Documentation**: Document Django state in all technical docs
- API documentation updates and user guide updates

**🎯 BMAD Master Knowledge Integration:** Consolidate all specialist deliverables and learnings

### Phase 10: Monitoring & Maintenance (Performance Agent + BMAD Master)
**⚡ Performance Agent Setup:**
- Performance monitoring setup
- **🚨 Django Health Monitoring**: Include Django functionality in health checks
- Error tracking implementation

**🎯 BMAD Master Maintenance Oversight:** Establish maintenance schedule and specialist responsibilities

---

## UX/UI Specialist Summary Integration

**🎨 UX/UI Specialist ensures professional user experience across all BMAD phases:**

### Core UX/UI Responsibilities
- **User Experience Quality**: Smooth user flows without jarring transitions
- **Professional Appearance**: Enterprise-grade visual standards matching project requirements
- **Accessibility Compliance**: WCAG 2.1 standards for inclusive design
- **Performance Awareness**: UI changes don't degrade application performance

### UX/UI Phase Integration Points
- **Phase 2.5**: Design system validation and accessibility compliance setup
- **Phase 4.5**: Real-time UX flow validation during implementation  
- **Phase 6.5**: Comprehensive UX audit before deployment authorization

**🎯 BMAD Master automatically invokes UX/UI Specialist for any story involving user-facing changes, ensuring comprehensive user experience validation prevents users from encountering unprofessional or broken interfaces.**

---

**This document establishes Django web application preservation as a CRITICAL requirement and UX/UI professional standards as MANDATORY quality gates for all BMAD development work. Non-compliance with Django protection protocols or UX/UI professional standards results in automatic work failure regardless of other achievements.**
