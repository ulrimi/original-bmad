"""
Universal Agent Interface - Base contract for all BMAD agents

Defines the standard interface that all agents must implement for
consistent orchestration and interoperability.
"""

from abc import ABC, abstractmethod
from typing import Dict, Any, List, Optional
from dataclasses import dataclass
from enum import Enum
import logging


class AgentCapability(Enum):
    """Standard agent capabilities for classification"""
    ANALYSIS = "analysis"
    PLANNING = "planning"
    IMPLEMENTATION = "implementation"
    QUALITY_ASSURANCE = "quality_assurance"
    DOCUMENTATION = "documentation"
    ARCHITECTURE = "architecture"
    DEVOPS = "devops"
    SECURITY = "security"


class AgentScope(Enum):
    """Agent operational scope"""
    PROJECT_WIDE = "project_wide"
    MODULE_SPECIFIC = "module_specific"  
    FILE_SPECIFIC = "file_specific"
    CROSS_PROJECT = "cross_project"


@dataclass
class AgentContext:
    """Standardized context passed to all agents"""
    project_path: str
    project_type: str
    languages_detected: List[str]
    frameworks_detected: List[str]
    current_task: str
    safety_constraints: List[str]
    execution_phase: str
    metadata: Dict[str, Any]


@dataclass
class AgentResult:
    """Standardized result returned by all agents"""
    success: bool
    agent_id: str
    capability: AgentCapability
    execution_time: float
    confidence_score: float
    findings: List[Dict[str, Any]]
    recommendations: List[str]
    artifacts_created: List[str]
    next_steps: List[str]
    error_details: Optional[str] = None
    requires_human_review: bool = False


class BaseAgent(ABC):
    """
    Universal base class for all BMAD agents.
    
    Provides standard interface, logging, and common functionality
    that all specialized agents inherit from.
    """
    
    def __init__(
        self,
        agent_id: str,
        capabilities: List[AgentCapability],
        scope: AgentScope,
        logger: Optional[logging.Logger] = None
    ):
        """
        Initialize base agent
        
        Args:
            agent_id: Unique identifier for this agent
            capabilities: List of capabilities this agent provides
            scope: Operational scope of this agent
            logger: Optional logger instance
        """
        self.agent_id = agent_id
        self.capabilities = capabilities
        self.scope = scope
        self.logger = logger or logging.getLogger(f"bmad.agent.{agent_id}")
        self.execution_history: List[AgentResult] = []
        self.context: Optional[AgentContext] = None
        
        self.logger.info(f"Initialized agent: {agent_id} with capabilities: {[c.value for c in capabilities]}")
    
    @abstractmethod
    def analyze(self, context: AgentContext) -> AgentResult:
        """
        Analyze the current situation and provide insights
        
        Args:
            context: Current execution context
            
        Returns:
            AgentResult: Analysis findings and recommendations
        """
        pass
    
    @abstractmethod
    def plan(self, context: AgentContext, analysis_result: AgentResult) -> AgentResult:
        """
        Create detailed plan based on analysis
        
        Args:
            context: Current execution context
            analysis_result: Previous analysis findings
            
        Returns:
            AgentResult: Detailed execution plan
        """
        pass
    
    @abstractmethod
    def execute(self, context: AgentContext, plan_result: AgentResult) -> AgentResult:
        """
        Execute the planned actions
        
        Args:
            context: Current execution context
            plan_result: Plan to execute
            
        Returns:
            AgentResult: Execution results
        """
        pass
    
    def validate_context(self, context: AgentContext) -> bool:
        """
        Validate that context is suitable for this agent
        
        Args:
            context: Context to validate
            
        Returns:
            bool: True if context is valid
        """
        required_fields = ['project_path', 'project_type', 'current_task']
        
        for field in required_fields:
            if not hasattr(context, field) or getattr(context, field) is None:
                self.logger.error(f"Missing required context field: {field}")
                return False
        
        return True
    
    def can_handle_task(self, task_description: str, context: AgentContext) -> float:
        """
        Determine if this agent can handle the given task
        
        Args:
            task_description: Description of task to handle
            context: Current execution context
            
        Returns:
            float: Confidence score (0.0 to 1.0) that agent can handle task
        """
        # Base implementation - subclasses should override for specific logic
        return 0.5
    
    def get_dependencies(self) -> List[str]:
        """
        Get list of other agents this agent depends on
        
        Returns:
            List[str]: List of agent IDs this agent depends on
        """
        return []
    
    def supports_language(self, language: str) -> bool:
        """
        Check if agent supports the given programming language
        
        Args:
            language: Programming language to check
            
        Returns:
            bool: True if language is supported
        """
        # Base implementation supports common languages
        return language.lower() in ['python', 'javascript', 'typescript']
    
    def supports_framework(self, framework: str) -> bool:
        """
        Check if agent supports the given framework
        
        Args:
            framework: Framework to check
            
        Returns:
            bool: True if framework is supported
        """
        # Base implementation - subclasses should override
        return False
    
    def get_execution_history(self) -> List[AgentResult]:
        """Get complete execution history for this agent"""
        return self.execution_history.copy()
    
    def reset_state(self):
        """Reset agent state for new task execution"""
        self.context = None
        self.logger.debug(f"Agent {self.agent_id} state reset")
    
    def _log_result(self, result: AgentResult):
        """Log agent execution result"""
        self.execution_history.append(result)
        
        if result.success:
            self.logger.info(
                f"Agent {self.agent_id} completed successfully. "
                f"Confidence: {result.confidence_score:.2f}, "
                f"Findings: {len(result.findings)}, "
                f"Recommendations: {len(result.recommendations)}"
            )
        else:
            self.logger.error(
                f"Agent {self.agent_id} failed: {result.error_details}"
            )