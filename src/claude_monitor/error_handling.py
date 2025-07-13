"""Centralized error handling and Sentry reporting utilities for Claude Monitor.

This module provides a unified interface for error reporting, replacing duplicate
Sentry error handling patterns throughout the codebase.
"""

import logging
import os
import sys
from enum import Enum
from pathlib import Path
from typing import Any, Dict, Optional, Union

try:
    import sentry_sdk
    from sentry_sdk.scope import Scope

    SENTRY_AVAILABLE = True
except ImportError:
    SENTRY_AVAILABLE = False
    sentry_sdk = None  # type: ignore[assignment]
    Scope = None  # type: ignore[misc,assignment]
    logging.warning(
        "Sentry SDK not available - error reporting will be limited to logging"
    )


class ErrorLevel(str, Enum):
    """Error severity levels matching Sentry's level system."""

    INFO = "info"
    ERROR = "error"


def report_error(
    exception: Exception,
    component: str,
    context_name: Optional[str] = None,
    context_data: Optional[Dict[str, Any]] = None,
    tags: Optional[Dict[str, str]] = None,
    level: ErrorLevel = ErrorLevel.ERROR,
) -> None:
    """Report an exception to Sentry with standardized context and tagging.

    This replaces the common pattern:
    ```python
    with sentry_sdk.configure_scope() as scope:
        scope.set_tag("component", "component_name")
        scope.set_context("context_name", {...})
    sentry_sdk.capture_exception(exception)
    ```

    Args:
        exception: The exception to report
        component: Component name for tagging (e.g., "data_loader", "monitor_controller")
        context_name: Optional context name (e.g., "file_error", "parsing")
        context_data: Optional dictionary of context data
        tags: Optional additional tags beyond the component tag
        level: Error severity level
    """
    logger = logging.getLogger(component)
    log_method = getattr(logger, level.value, logger.error)
    log_method(
        f"Error in {component}: {exception}",
        exc_info=True,
        extra={"context": context_name, "data": context_data},
    )

    if not SENTRY_AVAILABLE:
        return

    try:
        with sentry_sdk.configure_scope() as scope:
            scope.set_tag("component", component)

            if tags:
                for tag_key, tag_value in tags.items():
                    scope.set_tag(tag_key, str(tag_value))

            if context_name and context_data:
                scope.set_context(context_name, context_data)
            elif context_data:
                scope.set_context(component, context_data)

            scope.level = level.value
        sentry_sdk.capture_exception(exception)

    except Exception as e:
        logger.warning(f"Failed to report error to Sentry: {e}")


def report_file_error(
    exception: Exception,
    file_path: Union[str, Path],
    operation: str = "read",
    additional_context: Optional[Dict[str, Any]] = None,
) -> None:
    """Report file-related errors with standardized context.

    Args:
        exception: The exception that occurred
        file_path: Path to the file
        operation: The operation that failed (read, write, parse, etc.)
        additional_context: Any additional context data
    """
    context_data = {
        "file_path": str(file_path),
        "operation": operation,
    }

    if additional_context:
        context_data.update(additional_context)

    report_error(
        exception=exception,
        component="file_handler",
        context_name="file_error",
        context_data=context_data,
        tags={"operation": operation},
    )


def get_error_context() -> Dict[str, Any]:
    """Get standard error context information.
    
    Returns:
        Dictionary containing system and application context
    """
    return {
        "python_version": sys.version,
        "platform": sys.platform,
        "cwd": os.getcwd(),
        "pid": os.getpid(),
        "argv": sys.argv,
    }


def report_application_startup_error(
    exception: Exception,
    component: str = "application_startup",
    additional_context: Optional[Dict[str, Any]] = None,
) -> None:
    """Report application startup-related errors with system context.
    
    Args:
        exception: The startup exception
        component: Component where startup failed
        additional_context: Additional context data
    """
    context_data = get_error_context()
    
    if additional_context:
        context_data.update(additional_context)
    
    report_error(
        exception=exception,
        component=component,
        context_name="startup_error",
        context_data=context_data,
        tags={"error_type": "startup"},
    )


def report_configuration_error(
    exception: Exception,
    config_file: Optional[Union[str, Path]] = None,
    config_section: Optional[str] = None,
    additional_context: Optional[Dict[str, Any]] = None,
) -> None:
    """Report configuration-related errors.
    
    Args:
        exception: The configuration exception
        config_file: Path to the configuration file
        config_section: Configuration section that failed
        additional_context: Additional context data
    """
    context_data = {
        "config_file": str(config_file) if config_file else None,
        "config_section": config_section,
    }
    
    if additional_context:
        context_data.update(additional_context)
    
    report_error(
        exception=exception,
        component="configuration",
        context_name="config_error",
        context_data=context_data,
        tags={"error_type": "configuration"},
    )
