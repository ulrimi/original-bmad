# Create Development Story

**Task Type**: Planning Task (Rich Context)
**Agent Types**: Scrum Master, Planning Agents
**Environment**: Web UI preferred
**Complexity**: Medium

## Purpose

Create a comprehensive development story using the BMAD story-file workflow system. Stories are the primary way to pass complete context from planning agents to implementation agents, ensuring no context loss during handoffs.

## Prerequisites

Before creating a story, ensure you have:
- [ ] PRD (Product Requirements Document) available
- [ ] Architecture document available  
- [ ] Epic or feature breakdown identified
- [ ] User stories or requirements defined

## Task Instructions

### Step 1: Gather Story Context

**Elicit from user** (required):
1. **Epic/Feature Name**: What larger feature does this story belong to?
2. **User Story**: What specific user value are we delivering?
3. **Priority Level**: High/Medium/Low priority?
4. **Business Context**: Why is this story important?

### Step 2: Extract Technical Context

From available PRD and Architecture documents, gather:
- Relevant architecture patterns and decisions
- Technology stack and frameworks to use
- Existing code patterns to follow
- Integration points and dependencies
- Database or API changes needed

### Step 3: Define Implementation Details

Create specific implementation guidance:
- Files that need to be created or modified
- Function signatures or component structures
- Database schema changes or migrations
- Configuration or environment changes
- Integration requirements

### Step 4: Create Comprehensive Story

Use the `story-template.yaml` to create a complete story file that includes:

1. **Story Header** with metadata and identification
2. **User Story** in standard "As a/I want/So that" format
3. **Business Context** explaining the value and rationale
4. **Acceptance Criteria** using Given-When-Then format
5. **Technical Context** from PRD and Architecture documents
6. **Implementation Guidance** with specific technical details
7. **Testing Requirements** for comprehensive coverage
8. **Definition of Done** with quality gates
9. **Development Notes** sections for agent communication
10. **References & Links** to related documents

### Step 5: Validate Story Completeness

Ensure the story contains everything a dev agent needs:
- [ ] Clear user value proposition
- [ ] Specific, testable acceptance criteria
- [ ] Complete technical context from planning documents
- [ ] Actionable implementation guidance
- [ ] Comprehensive testing requirements
- [ ] Clear definition of completion

### Step 6: Save and Link Story

Save the story file using the naming convention:
`story-{epic-name}-{number}-{slug}.md`

Example: `story-user-auth-001-login-component.md`

## Story Quality Standards

A high-quality BMAD story:

### Context Completeness
- Contains all context a dev agent needs to implement autonomously
- References relevant sections from PRD and Architecture documents
- Includes business rationale and user value
- Provides technical implementation guidance

### Specificity  
- Acceptance criteria are specific and testable
- Implementation guidance is actionable
- Testing requirements cover all scenarios
- Definition of done is measurable

### Communication
- Written in clear, unambiguous language
- Uses consistent terminology from project documentation
- Includes sections for dev/QA agent notes
- Links to related stories and resources

## Common Story Anti-Patterns to Avoid

❌ **Vague Requirements**: "Improve user experience"
✅ **Specific Requirements**: "Reduce login time to <2 seconds with clear error messages"

❌ **Missing Technical Context**: No architecture or implementation guidance
✅ **Complete Context**: References architecture, provides implementation details

❌ **Untestable Criteria**: "Users should be happy with the feature"
✅ **Testable Criteria**: "95% of users complete login within 3 attempts"

❌ **Implementation Details Only**: Just technical tasks without user value
✅ **Value-Driven**: Clear user story with technical implementation guidance

## Output Format

Create a markdown file using the story template that contains:
- Complete story context for autonomous implementation
- Clear acceptance criteria and definition of done
- Technical implementation guidance
- Comprehensive testing requirements
- Sections for dev/QA agent communication

## Success Criteria

The story is complete when:
1. A dev agent can implement the feature autonomously using only the story file
2. QA agent can validate the implementation against the acceptance criteria
3. All technical context from planning documents is included
4. Testing requirements ensure quality and coverage

---

**Remember**: The story file is the primary communication vehicle between planning and implementation phases. It must contain complete context to eliminate the context loss problem in AI-assisted development.