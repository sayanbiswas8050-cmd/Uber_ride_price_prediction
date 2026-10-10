import setuptools

HYPHEN_E_DOT = "-e ."

def get_requirements(file_path: str):
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "").strip() for req in requirements]

        # Filter out '-e .' so it is not passed to install_requires
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
            
    return requirements

setuptools.setup(
    name="ubar_ride_price_prediction",
    version="0.0.1",
    author="Sayan",
    author_email="sayanbiswas8050@gmail.com",
    url="https://github.com/sayanbiswas8050-cmd/Uber_ride_price_prediction",
    packages=setuptools.find_packages(),
    install_requires=get_requirements("requirements.txt")
)