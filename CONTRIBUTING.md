# Contributing to SubclassDict

Thank you for your interest in contributing to SubclassDict! This document provides guidelines and information for contributors.

## Development Setup

### Prerequisites

- Python 3.8 or higher
- Git
- pip

### Installation

1. Fork the repository on GitHub
2. Clone your fork locally:
   ```bash
   git clone https://github.com/your-username/subclassdict.git
   cd subclassdict
   ```

3. Install the package in development mode:
   ```bash
   pip install -e .[dev]
   ```

4. Install pre-commit hooks:
   ```bash
   pre-commit install
   ```

## Development Workflow

### 1. Create a Feature Branch

```bash
git checkout -b feature/your-feature-name
```

### 2. Make Your Changes

- Write your code following the existing style
- Add tests for new functionality
- Update documentation as needed

### 3. Run Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=subclassdict --cov-report=html

# Run specific test file
pytest tests/test_subclassdict.py
```

### 4. Code Quality Checks

```bash
# Linting
ruff check .

# Formatting
ruff format .

# Type checking
mypy src/

# All checks at once
tox
```

### 5. Commit Your Changes

```bash
git add .
git commit -m "Add your descriptive commit message"
```

The pre-commit hooks will automatically run linting and formatting checks.

### 6. Push and Create Pull Request

```bash
git push origin feature/your-feature-name
```

Then create a pull request on GitHub.

## Code Style

### Python Code

- Follow PEP 8 style guidelines
- Use type hints for all functions and methods
- Write docstrings for all public functions, classes, and methods
- Use Google-style docstrings

### Example

```python
def example_function(param: str) -> int:
    """
    Example function with proper type hints and docstring.
    
    Args:
        param: A string parameter
        
    Returns:
        An integer result
        
    Raises:
        ValueError: If param is invalid
    """
    if not param:
        raise ValueError("param cannot be empty")
    return len(param)
```

### Test Style

- Use descriptive test names that explain what is being tested
- Group related tests in classes
- Use fixtures for common test data
- Aim for high test coverage (>95%)

### Example

```python
class TestExampleFunction:
    """Test the example_function."""
    
    def test_with_valid_input(self):
        """Test function with valid input."""
        result = example_function("hello")
        assert result == 5
    
    def test_with_empty_input(self):
        """Test function with empty input raises ValueError."""
        with pytest.raises(ValueError):
            example_function("")
```

## Testing Guidelines

### Test Coverage

- All new code must have corresponding tests
- Aim for >95% code coverage
- Test both success and failure cases
- Test edge cases and error conditions

### Test Categories

1. **Unit Tests**: Test individual functions and methods
2. **Integration Tests**: Test how components work together
3. **Performance Tests**: Test performance characteristics
4. **Edge Case Tests**: Test boundary conditions and error cases

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=subclassdict --cov-report=term-missing

# Run specific test categories
pytest tests/test_subclassdict.py  # Core functionality
pytest tests/test_integration.py   # Integration tests
pytest tests/test_subclasses.py    # Utility functions
```

## Documentation

### Code Documentation

- Add docstrings to all public functions, classes, and methods
- Include examples in docstrings where helpful
- Document parameters, return values, and exceptions

### User Documentation

- Update README.md for user-facing changes
- Add examples for new features
- Update API reference as needed

## Pull Request Guidelines

### Before Submitting

1. **Run all tests**: Ensure all tests pass
2. **Check code quality**: Run linting and type checking
3. **Update documentation**: Update relevant documentation
4. **Write clear commit messages**: Use descriptive commit messages

### Pull Request Template

When creating a pull request, include:

1. **Description**: What changes were made and why
2. **Testing**: How the changes were tested
3. **Documentation**: Any documentation updates
4. **Breaking changes**: Note any breaking changes

### Example

```markdown
## Description
Added support for custom key validation in SubclassDict.

## Changes
- Added `validate_key` parameter to SubclassDict constructor
- Added key validation before subclass lookup
- Updated type hints for better type safety

## Testing
- Added unit tests for key validation
- Added integration tests for custom validation scenarios
- All existing tests pass

## Documentation
- Updated README with validation examples
- Added docstring examples for new parameter
```

## Issue Reporting

### Before Creating an Issue

1. Check if the issue already exists
2. Search closed issues for similar problems
3. Try to reproduce the issue with the latest version

### Issue Template

When creating an issue, include:

1. **Description**: Clear description of the problem
2. **Steps to reproduce**: Detailed steps to reproduce the issue
3. **Expected behavior**: What should happen
4. **Actual behavior**: What actually happens
5. **Environment**: Python version, OS, package version
6. **Code example**: Minimal code example if applicable

## Release Process

### Version Numbering

We follow [Semantic Versioning](https://semver.org/):
- **MAJOR**: Breaking changes
- **MINOR**: New features (backward compatible)
- **PATCH**: Bug fixes (backward compatible)

### Release Checklist

1. Update version in `pyproject.toml`
2. Update `CHANGELOG.md`
3. Run full test suite
4. Update documentation if needed
5. Create release tag
6. Publish to PyPI (maintainers only)

## Community Guidelines

### Code of Conduct

- Be respectful and inclusive
- Focus on constructive feedback
- Help others learn and grow
- Follow the golden rule

### Getting Help

- **GitHub Issues**: For bug reports and feature requests
- **GitHub Discussions**: For questions and general discussion
- **Pull Requests**: For code contributions

## Recognition

Contributors will be recognized in:
- CONTRIBUTORS.md file
- Release notes for significant contributions
- GitHub contributor list

Thank you for contributing to SubclassDict!
