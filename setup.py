# from setuptools import setup, find_packages
# from typing import List
# # Required packages (automatically installed when your package is installed)
# INSTALL_REQUIRES = [
#     "numpy>=1.21.0",
#     "pandas>=1.3.0",
#     "scikit-learn>=1.0.0",
#     # Add other dependencies here
# ]

# # Development dependencies (optional)
# EXTRAS_REQUIRE = {
#     "dev": [
#         "pytest>=6.0",
#         "black>=22.0", 
#         "flake8>=4.0",
#     ],
# }
# HYPHEN_E_DOT='-e .'
# def install_requirments(file_path:str)->List[str]:
     
#     '''this function will return list of libraries that i will need as reuiments
#     it will read these from a file named requiments .txt and return a list
#     '''
#     reqq=[]
#     with open(file_path) as file_obj:
#         reqq=file_obj.readlines
#         reqq=[r.replace("\n","")for r in reqq]
#         if HYPHEN_E_DOT in reqq:
#             reqq.remove(HYPHEN_E_DOT)


# setup(
#     name="mlproject",  # Your package name (should be PyPI-unique)
#     version="0.0.1",   # Follows Semantic Versioning (SemVer)
#     author="Harpreet Singh",
#     author_email="hshappysidhu280@gmail.com",
#     description="A short description of your ML project",
#     long_description=open("README.md").read(),
#     long_description_content_type="text/markdown",
#     url="https://github.com/yourusername/mlproject",  # Project URL
#     packages=find_packages(include=["mlproject", "mlproject.*"]),  # Auto-find Python packages
#     install_requires=install_requirments('requirments.txt'),
#     extras_require=EXTRAS_REQUIRE,
#     python_requires=">=3.8",  # Minimum Python version
#     classifiers=[  # PyPI classifiers (optional but recommended)
#         "Programming Language :: Python :: 3",
#         "License :: OSI Approved :: MIT License",
#         "Operating System :: OS Independent",
#     ],
# )






from setuptools import setup, find_packages
from typing import List  # Only needed for Python < 3.9

# Development dependencies (optional)
EXTRAS_REQUIRE = {
    "dev": [
        "pytest>=6.0",
        "black>=22.0", 
        "flake8>=4.0",
    ],
}

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return list of requirements from a file
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = [line.strip() for line in file_obj.readlines()]
    
    # Remove editable install if present
    if '-e .' in requirements:
        requirements.remove('-e .')
    
    return requirements

setup(
    name="mlproject",
    version="0.0.1",
    author="Harpreet Singh",
    author_email="hshappysidhu280@gmail.com",
    description="A short description of your ML project",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/mlproject",
    packages=find_packages(include=["mlproject", "mlproject.*"]),
    install_requires=get_requirements('requirments.txt'),
    extras_require=EXTRAS_REQUIRE,
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)