from setuptools import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding='utf-8')

setup(
    name='open-weather_LW_Liza',
    version='0.0',
    description='Openweather API',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vasiliza2/proga_5_LR3",
    packages=['open-weather_LW'], 
    author='Elizaveta Vasileva',
    author_email='elizavetavasileva332@gmail.com',
    zip_safe=False
)
