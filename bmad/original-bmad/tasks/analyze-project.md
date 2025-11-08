# Analyze Project

**Task Type**: Analysis Task (Planning Agent)
**Agent Types**: BMAD Master, Analyst, Architect
**Environment**: Web UI or IDE
**Complexity**: Medium

## Purpose

Analyze any project structure, technology stack, and codebase to provide recommendations for BMAD Method implementation. This task is project-agnostic and works with any technology stack or domain.

## Task Instructions

### Step 1: Project Discovery

**Examine the project structure** by looking at:
- Root directory contents and organization
- Package/dependency management files (`package.json`, `requirements.txt`, `pom.xml`, etc.)
- Configuration files (`.env`, `config/`, `settings.py`, etc.) 
- Source code directory structure
- Documentation and README files

**Ask the user** for clarification if needed:
1. "What is the main purpose of this project?"
2. "Are there any specific constraints or requirements I should know about?"
3. "What are your main pain points with the current development process?"

### Step 2: Technology Stack Detection

**Identify and document**:

**Programming Languages**:
- Primary language(s) and versions
- Secondary languages for specific purposes

**Frameworks and Libraries**:
- Web frameworks (Django, React, Express, etc.)
- Testing frameworks and tools
- Database technologies and ORMs
- Build tools and package managers

**Infrastructure and Deployment**:
- Cloud platforms and services
- Containerization (Docker, Kubernetes)
- CI/CD pipelines and tools
- Monitoring and logging solutions

### Step 3: Architecture Analysis

**Analyze the current architecture**:

**Project Organization**:
- Monolithic vs modular structure
- Separation of concerns
- Code organization patterns

**Architecture Patterns**:
- MVC, MVP, MVVM patterns
- Microservices vs monolithic  
- Event-driven architecture
- API design patterns

**Quality and Maintainability**:
- Code quality indicators
- Testing coverage and practices
- Documentation completeness
- Technical debt indicators

### Step 4: BMAD Method Compatibility Assessment  

**Evaluate project readiness** for BMAD Method:

**Development Workflow**:
- Current development process
- Planning and requirement management
- Code review and quality processes
- Testing and deployment practices

**Team Structure**:
- Team size and roles
- Experience with AI-assisted development
- Collaboration tools and processes

**Project Complexity**:
- Feature complexity and scope
- Integration requirements
- Performance and scalability needs

### Step 5: Generate Recommendations

**Create comprehensive recommendations** including:

**BMAD Implementation Strategy**:
- Recommended agent types for this project
- Suggested workflow configuration
- Story-driven development adoption plan

**Specialized Agent Needs**:
- Domain-specific agents that would be beneficial
- Custom templates or workflows needed
- Integration with existing tools

**Implementation Roadmap**:
- Phase 1: Quick wins and foundation setup
- Phase 2: Core workflow implementation
- Phase 3: Advanced features and optimization

## Analysis Framework

### Project Classification

**Project Type**:
- Web Application (Frontend, Backend, Full-stack)
- API/Microservices
- Data Pipeline/Analytics
- Mobile Application
- Desktop Application
- Infrastructure/DevOps
- Other (specify)

**Complexity Level**:
- **Simple**: Single developer, basic features, minimal integrations
- **Medium**: Small team, moderate features, some integrations  
- **Complex**: Large team, complex features, extensive integrations
- **Enterprise**: Multiple teams, mission-critical, extensive compliance

**Development Stage**:
- **Greenfield**: New project, fresh start
- **Brownfield**: Existing codebase with history
- **Legacy Modernization**: Updating old systems
- **Maintenance Mode**: Bug fixes and minor updates

### Technology Stack Assessment

For each technology, evaluate:
- **Maturity**: How established is the technology choice?
- **Team Expertise**: How familiar is the team with this technology?
- **BMAD Compatibility**: How well does it work with AI-assisted development?
- **Ecosystem**: What tools and libraries are available?

### Quality Metrics

**Code Quality Indicators**:
- Linting and formatting consistency
- Test coverage and quality
- Code complexity metrics
- Documentation completeness

**Development Process Maturity**:
- Version control practices
- Code review processes  
- CI/CD pipeline sophistication
- Error monitoring and logging

## Output Format

Provide analysis in this structure:

```markdown
# Project Analysis Report

## Executive Summary
[Brief overview of project, technology stack, and key recommendations]

## Project Overview
- **Type**: [Project classification]
- **Complexity**: [Simple/Medium/Complex/Enterprise]
- **Stage**: [Greenfield/Brownfield/Legacy/Maintenance]

## Technology Stack
### Primary Technologies
- Language: [Programming language and version]
- Framework: [Primary framework]
- Database: [Database technology]

### Supporting Technologies
[Testing, build tools, deployment, etc.]

## Architecture Assessment
### Current Patterns
[Architecture patterns in use]

### Strengths
[What's working well]

### Areas for Improvement  
[Technical debt, architectural issues]

## BMAD Method Recommendations

### Recommended Agents
1. **[Agent Name]** - [Purpose and benefits]
2. **[Agent Name]** - [Purpose and benefits]

### Workflow Configuration
[Recommended BMAD workflow setup]

### Implementation Strategy
#### Phase 1: Foundation (1-2 weeks)
- [Quick wins and basic setup]

#### Phase 2: Core Implementation (2-4 weeks) 
- [Main workflow implementation]

#### Phase 3: Optimization (2-4 weeks)
- [Advanced features and customization]

### Custom Requirements
[Any specialized agents, templates, or workflows needed]

## Next Steps
1. [Immediate action items]
2. [Short-term goals]
3. [Long-term objectives]
```

## Success Criteria

The analysis is complete when:
1. Technology stack is fully identified and documented
2. Architecture patterns and quality metrics are assessed
3. BMAD Method compatibility is evaluated
4. Specific recommendations are provided for implementation
5. Clear next steps are defined

## Common Patterns to Look For

**Well-Structured Projects**:
- Clear separation of concerns
- Consistent naming conventions
- Comprehensive testing
- Good documentation

**Projects Needing Attention**:
- Large files with multiple responsibilities  
- Minimal or outdated tests
- Inconsistent code styles
- Missing documentation

**BMAD Method Opportunities**:
- Manual, repetitive development tasks
- Inconsistent requirement implementation
- Context loss between planning and development
- Quality assurance gaps

---

**Remember**: This analysis should provide actionable recommendations that help the user implement BMAD Method effectively for their specific project and context.