# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.1] - 2024-01-XX

### Fixed
- **Repository URLs**: Updated all GitHub repository URLs to use correct username (eddiethedean)
- **Documentation links**: Fixed all GitHub links in README and project metadata
- **Badge URLs**: Updated CI, coverage, and other badge URLs to point to correct repository

## [0.1.0] - 2024-01-XX

### Added
- **Major rewrite and modernization** of the entire package
- **Performance optimizations**: Added subclass lookup caching for O(1) performance after first access
- **Enhanced functionality**: Added `get()`, `setdefault()`, `pop()`, `popitem()`, `copy()`, `clear()` methods
- **Better type safety**: Full generic type support with `SubclassDict[T]`
- **Comprehensive test suite**: >95% code coverage with unit, integration, and performance tests
- **Modern packaging**: Consolidated to `pyproject.toml` with PEP 621 standards
- **CI/CD pipeline**: GitHub Actions for testing, linting, and publishing
- **Quality tools**: Pre-commit hooks, ruff linter/formatter, updated mypy configuration
- **Documentation**: Comprehensive README with examples, API reference, and troubleshooting
- **Utility functions**: Enhanced `subclasses()` function with better documentation

### Changed
- **Fixed critical bug**: `__setitem__` logic now correctly handles new keys vs. existing keys
- **Improved caching**: Smart cache invalidation when keys are added/removed
- **Better error handling**: More descriptive error messages and edge case handling
- **Python version support**: Updated to support Python 3.8 through 3.13
- **Dependencies**: Updated to modern versions (ruff, pytest, mypy, etc.)

### Fixed
- **Bug fix**: `__setitem__` was incorrectly updating parent keys instead of creating new entries
- **Bug fix**: Missing `__contains__` method for proper `in` operator support
- **Bug fix**: Missing `__delitem__` method for key deletion
- **Bug fix**: Package data configuration in setup.cfg (was incorrectly referencing "tinyalchemy")

### Removed
- **Legacy files**: Removed `setup.py`, `setup.cfg`, `requirements.txt`, `requirements_dev.txt`
- **Outdated dependencies**: Removed flake8, old mypy version, outdated tox configuration

### Security
- **Dependency updates**: All dependencies updated to latest secure versions
- **Type safety**: Enhanced type checking with strict mypy configuration

## [0.0.5] - 2021-XX-XX

### Added
- Initial release with basic SubclassDict functionality
- Basic subclass lookup behavior
- Simple packaging with setup.py/setup.cfg

### Known Issues
- Performance issues with large hierarchies (O(n) lookups)
- Missing standard dictionary methods
- Limited type safety
- Outdated packaging standards
