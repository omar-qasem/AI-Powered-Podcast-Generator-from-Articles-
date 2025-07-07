# Contributing to AI Podcast Generator

Thank you for your interest in contributing to the AI Podcast Generator! This document provides guidelines and information for contributors.

## 🤝 How to Contribute

### Reporting Bugs

1. **Check existing issues** to avoid duplicates
2. **Use the bug report template** when creating new issues
3. **Provide detailed information** including:
   - Operating system and Python version
   - Steps to reproduce the bug
   - Expected vs actual behavior
   - Error messages and logs
   - Sample input that causes the issue

### Suggesting Features

1. **Check existing feature requests** to avoid duplicates
2. **Use the feature request template**
3. **Provide clear use cases** and benefits
4. **Consider implementation complexity**

### Code Contributions

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/your-feature-name`
3. **Make your changes** following our coding standards
4. **Add tests** for new functionality
5. **Update documentation** as needed
6. **Commit with clear messages**
7. **Push to your fork**: `git push origin feature/your-feature-name`
8. **Create a Pull Request**

## 🛠️ Development Setup

### Local Development

```bash
# Clone your fork
git clone https://github.com/your-username/ai-podcast-generator.git
cd ai-podcast-generator

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -r requirements.txt
pip install -e ".[dev]"

# Run tests
pytest

# Run linting
flake8 .
black .
mypy .
```

### Google Colab Development

1. Open the notebook in Google Colab
2. Make your changes
3. Test thoroughly
4. Download the modified notebook
5. Commit to your fork

## 📝 Coding Standards

### Python Code Style

- Follow **PEP 8** guidelines
- Use **Black** for code formatting
- Use **type hints** where appropriate
- Write **docstrings** for all functions and classes
- Keep functions **small and focused**
- Use **meaningful variable names**

### Example Function

```python
def extract_article_text(url: str, timeout: int = 10) -> str:
    """
    Extracts the main text content from a given URL.
    
    Args:
        url: The URL to extract text from
        timeout: Request timeout in seconds
        
    Returns:
        Extracted text content or error message
        
    Raises:
        requests.RequestException: If the request fails
    """
    # Implementation here
    pass
```

### Documentation

- Update **README.md** for user-facing changes
- Add **docstrings** for new functions
- Update **requirements.txt** for new dependencies
- Add **examples** for new features

## 🧪 Testing

### Running Tests

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_text_processing.py

# Run with coverage
pytest --cov=src
```

### Writing Tests

- Write tests for **all new functionality**
- Use **descriptive test names**
- Test **edge cases** and **error conditions**
- Mock **external dependencies** (APIs, file system)

### Example Test

```python
def test_summarize_text_with_valid_input():
    """Test that summarize_text returns a shorter summary."""
    input_text = "This is a long article about AI..." * 100
    summary = summarize_text(input_text)
    
    assert len(summary) < len(input_text)
    assert isinstance(summary, str)
    assert len(summary.strip()) > 0
```

## 📋 Pull Request Guidelines

### Before Submitting

- [ ] Code follows style guidelines
- [ ] Tests pass locally
- [ ] Documentation is updated
- [ ] Commit messages are clear
- [ ] No merge conflicts

### PR Description Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement
- [ ] Code refactoring

## Testing
- [ ] Tests added/updated
- [ ] Manual testing completed
- [ ] Google Colab tested

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] No breaking changes
```

## 🎯 Priority Areas

We're especially looking for contributions in these areas:

### High Priority
- **Better text extraction** from various website formats
- **Multi-language support** for TTS and summarization
- **Performance optimizations** for large texts
- **Error handling improvements**

### Medium Priority
- **Voice cloning** integration
- **Batch processing** capabilities
- **Advanced audio effects**
- **User authentication** system

### Low Priority
- **UI/UX improvements**
- **Additional audio formats**
- **Podcast RSS feed** generation
- **Social media integration**

## 🏷️ Issue Labels

- `bug`: Something isn't working
- `enhancement`: New feature or request
- `documentation`: Improvements to docs
- `good first issue`: Good for newcomers
- `help wanted`: Extra attention needed
- `priority-high`: Critical issues
- `priority-medium`: Important issues
- `priority-low`: Nice to have

## 💬 Communication

- **GitHub Issues**: For bugs and feature requests
- **GitHub Discussions**: For questions and ideas
- **Pull Requests**: For code contributions
- **Email**: For private matters

## 🎉 Recognition

Contributors will be:
- **Listed in README.md**
- **Mentioned in release notes**
- **Given credit in documentation**
- **Invited to join the core team** (for significant contributions)

## 📚 Resources

### Learning Resources
- [Transformers Documentation](https://huggingface.co/docs/transformers/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [gTTS Documentation](https://gtts.readthedocs.io/)
- [PyDub Documentation](https://pydub.com/)

### Development Tools
- [Black Code Formatter](https://black.readthedocs.io/)
- [Flake8 Linter](https://flake8.pycqa.org/)
- [MyPy Type Checker](https://mypy.readthedocs.io/)
- [Pytest Testing Framework](https://pytest.org/)

## ❓ Questions?

Don't hesitate to ask questions! We're here to help:

1. Check existing **GitHub Discussions**
2. Create a new **discussion** for general questions
3. Open an **issue** for specific problems
4. Email us for **private matters**

Thank you for contributing to AI Podcast Generator! 🎙️

