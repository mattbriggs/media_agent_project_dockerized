# Design Overview

## Object-Oriented Design Patterns
- SearchClient: Strategy Pattern
- ContactScraper: Single Responsibility
- NotionClientWrapper: Adapter Pattern
- MediaAgent: Facade Pattern

## Logging
Each class uses logging to trace major operations.

## Testing
Simple `pytest`-based tests for key modules.

## Deployment
- Dockerfile for easy containerization
- Railway-compatible
- Cron Jobs scheduled via Railway Schedules
