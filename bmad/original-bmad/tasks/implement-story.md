# Implement Story

**Task Type**: Implementation Task (Dev Agent)
**Agent Types**: Dev Agent
**Environment**: IDE  
**Complexity**: Variable (depends on story)

## Purpose

Implement a complete feature from a BMAD story file. This task is the core of the BMAD Method development workflow, where dev agents autonomously implement features using the complete context provided in story files.

## Prerequisites

Before starting implementation:
- [ ] Story file exists and is complete
- [ ] Story has passed validation (all required sections present)
- [ ] Development environment is set up
- [ ] Previous dependencies/stories are completed

## Task Instructions

### Step 1: Load and Parse Story Context

**Read the complete story file** and extract:

**Story Metadata**:
- Story ID and epic name
- Priority and estimated effort
- Current status and assignment

**Implementation Context**:
- User story and business value
- Acceptance criteria (functional and non-functional)
- Technical context from architecture documents
- Implementation guidance (files, functions, patterns)
- Testing requirements and coverage needs

**Quality Gates**:
- Definition of done checklist
- Code quality requirements
- Performance and security criteria

### Step 2: Validate Story Completeness

**Ensure the story contains everything needed**:
- [ ] Clear acceptance criteria that are testable
- [ ] Technical implementation guidance with specific files/functions
- [ ] Architecture context and patterns to follow
- [ ] Testing requirements with coverage expectations
- [ ] Definition of done with measurable criteria

**If context is incomplete**, request clarification rather than making assumptions.

### Step 3: Plan Implementation Approach

**Based on story guidance, plan**:

**File Structure Changes**:
- New files to create
- Existing files to modify
- Directory structure changes needed

**Implementation Order**:
- Database/model changes first
- Core business logic
- API/service layer
- UI/presentation layer
- Integration points

**Testing Strategy**:
- Unit tests for business logic
- Integration tests for API endpoints  
- End-to-end tests for user workflows
- Performance/security tests as needed

### Step 4: Follow Existing Project Patterns

**Maintain consistency** with existing codebase:

**Code Patterns**:
- Follow established naming conventions
- Use existing architectural patterns
- Maintain consistent error handling
- Follow existing logging practices

**Quality Standards**:
- Match existing code formatting and style
- Maintain or improve test coverage
- Follow existing documentation patterns
- Use established linting/quality tools

### Step 5: Implement Core Functionality

**Implement features step by step**:

**Database/Model Layer**:
```python
# Example: Follow existing model patterns
class UserProfile(models.Model):
    # Follow existing field naming and validation patterns
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # ... implementation following story guidance
```

**Business Logic/Service Layer**:
```python
# Example: Implement business logic with proper error handling
def create_user_profile(user_data):
    """Create user profile following business rules from story."""
    # Implementation following acceptance criteria
    # Include proper validation and error handling
```

**API/Controller Layer**:
```python
# Example: Create API endpoints following existing patterns
@api_view(['POST'])
def create_profile(request):
    """Create user profile endpoint."""
    # Follow existing API response patterns
    # Include proper error handling and validation
```

**UI/Frontend Layer**:
```jsx
// Example: Create components following existing patterns
const UserProfileForm = () => {
    // Follow existing component patterns
    // Include proper state management and error handling
};
```

### Step 6: Implement Comprehensive Testing

**Create tests following story requirements**:

**Unit Tests**:
```python
# Example: Test business logic thoroughly
class TestUserProfile(TestCase):
    def test_create_profile_success(self):
        """Test successful profile creation."""
        # Test happy path from acceptance criteria
        
    def test_create_profile_validation_error(self):
        """Test validation error handling."""
        # Test error cases from acceptance criteria
```

**Integration Tests**:
```python
# Example: Test API endpoints and database interactions
class TestProfileAPI(APITestCase):
    def test_create_profile_endpoint(self):
        """Test profile creation endpoint."""
        # Test complete request/response cycle
```

**End-to-End Tests**:
```javascript
// Example: Test complete user workflows
describe('User Profile Creation', () => {
    it('should allow user to create profile', () => {
        // Test complete user workflow from story
    });
});
```

### Step 7: Validate Against Acceptance Criteria

**Test implementation against each acceptance criterion**:

For each "Given-When-Then" criterion:
1. **Set up the "Given" condition**
2. **Execute the "When" action**  
3. **Verify the "Then" result**
4. **Document the validation**

**Example**:
```
AC1: User profile creation happy path
✅ Given: New user with valid data
✅ When: User submits profile form
✅ Then: Profile created and user redirected to dashboard
```

### Step 8: Complete Definition of Done

**Check off each item** in the definition of done:

**Code Quality**:
- [ ] Code follows project conventions
- [ ] No linting/formatting violations
- [ ] Code is self-documenting
- [ ] Performance is acceptable

**Testing**:
- [ ] Unit test coverage ≥ 80%
- [ ] Integration tests pass
- [ ] End-to-end tests pass
- [ ] Manual testing completed

**Documentation**:
- [ ] Code comments for complex logic
- [ ] API documentation updated
- [ ] README updated if needed

**Deployment Readiness**:
- [ ] Works in development environment
- [ ] No breaking changes
- [ ] Database migrations successful
- [ ] Environment variables configured

### Step 9: Add Development Notes

**Update the story file** with implementation notes:

```markdown
### Dev Agent Notes
**Implementation Date**: [Date]
**Files Modified/Created**:
- `models/user_profile.py` - Created UserProfile model with validation
- `api/profile.py` - Added profile creation endpoint
- `components/ProfileForm.jsx` - Created profile form component

**Key Implementation Decisions**:
- Used existing User model relationship pattern
- Followed established validation error handling
- Implemented client-side validation for better UX

**Testing Coverage**:
- Unit tests: 85% coverage
- Integration tests: All API endpoints covered
- E2E tests: Profile creation workflow tested

**Performance Notes**:
- Profile creation takes <500ms
- Database queries optimized with select_related

**Next Steps**:
- Ready for QA review
- Consider adding profile image upload in next story
```

### Step 10: Request Review (if needed)

If the story requires review:
- Mark story as "Ready for Review"
- Add comprehensive dev notes
- Ensure all tests are passing
- Verify definition of done is complete

## Implementation Quality Standards

### Code Quality
- **Readable**: Clear variable and function names
- **Maintainable**: Logical structure and organization  
- **Consistent**: Follows existing project patterns
- **Documented**: Comments for complex logic only
- **Tested**: Comprehensive test coverage

### Performance
- **Responsive**: UI interactions feel instant (<100ms)
- **Efficient**: API responses under 2 seconds
- **Scalable**: Code handles expected load
- **Optimized**: Database queries are efficient

### Security  
- **Validated**: All inputs are validated and sanitized
- **Authenticated**: Proper authentication checks
- **Authorized**: Appropriate access controls
- **Encrypted**: Sensitive data is protected

## Common Implementation Patterns

### Error Handling
```python
try:
    # Implementation logic
    result = create_user_profile(data)
    return success_response(result)
except ValidationError as e:
    return error_response("Invalid data", e.errors)
except Exception as e:
    logger.error(f"Profile creation failed: {e}")
    return error_response("Internal error")
```

### API Response Consistency
```python
def success_response(data):
    return Response({
        'success': True,
        'data': data,
        'message': 'Operation completed successfully'
    })

def error_response(message, errors=None):
    return Response({
        'success': False,
        'message': message,
        'errors': errors
    }, status=400)
```

### Component Structure
```jsx
const Component = ({ props }) => {
    const [state, setState] = useState(initialState);
    
    const handleAction = useCallback(() => {
        // Event handling logic
    }, [dependencies]);
    
    if (loading) return <LoadingSpinner />;
    if (error) return <ErrorMessage error={error} />;
    
    return (
        <div className="component">
            {/* Component JSX */}
        </div>
    );
};
```

## Success Criteria

Implementation is complete when:
1. All acceptance criteria are met and validated
2. Comprehensive testing is implemented and passing
3. Code quality standards are maintained
4. Definition of done is 100% complete
5. Story file is updated with implementation notes
6. Feature works in development environment

## Common Anti-Patterns to Avoid

❌ **Implementing beyond the story scope**
✅ **Implement exactly what's specified in acceptance criteria**

❌ **Skipping tests to save time**  
✅ **Write tests as you implement, not as an afterthought**

❌ **Ignoring existing project patterns**
✅ **Follow established conventions and architectural patterns**

❌ **Making assumptions about unclear requirements**
✅ **Ask for clarification when story context is incomplete**

❌ **Implementing without understanding the user value**
✅ **Understand the business context and user story rationale**

---

**Remember**: The story file contains everything you need to implement autonomously. Trust the context provided and implement exactly what's specified in the acceptance criteria.