import setuptools

setuptools.setup(
    name="minitouch",
    version="0.0.1",
    description="MiniTouch benchmark",
    project_urls={
        "Source": "https://github.com/ServiceNow/MiniTouch",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=['gym', 'pybullet'],
    python_requires=">=3.6",
)