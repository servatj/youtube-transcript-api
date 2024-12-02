from setuptools import setup, find_packages

setup(
    name="youtube-transcript-api",
    version="1.0.0",
    author="Josep Servat",
    author_email="josepservat@example.com",
    description="A FastAPI-based project for YouTube transcript analysis using OpenAI.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/josepservat/youtube-transcript-api",
    packages=find_packages(exclude=["tests*"]),
    include_package_data=True,
    python_requires=">=3.8",
    install_requires=[
        "fastapi",
        "uvicorn",
        "python-dotenv",
        "mysql-connector-python",
        "psycopg2-binary",
        "yoyo-migrations",
        "openai",
        "pydantic",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "youtube-transcript-api=app.main:app",
        ],
    },
)