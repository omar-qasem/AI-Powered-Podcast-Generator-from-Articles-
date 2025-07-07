from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="ai-podcast-generator",
    version="1.0.0",
    author="AI Podcast Generator Team",
    author_email="contact@example.com",
    description="Transform AI articles into engaging podcast-style audio content",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/your-username/ai-podcast-generator",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Content Creators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Multimedia :: Sound/Audio :: Speech",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Text Processing :: Linguistic",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=6.0",
            "black>=21.0",
            "flake8>=3.8",
            "mypy>=0.800",
        ],
        "colab": [
            "pyngrok>=5.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "ai-podcast-generator=streamlit_app:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.mp3", "*.md", "*.txt"],
    },
)

