from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.txt"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()



# Setting up
setup(
    name="Covidinfo",
    version='0.0.1',
    author="Dhanush-E",
    author_email="eaglephatidhanush@gmail.com",
    description='Covidinfo is a module to fetch data related to covid',
    long_description_content_type="text/markdown",
    long_description="# Covidinfo\n\n## How to install\npip install Covidinfo\n\n## How to use\n\n### import the module\n\n1.import Covidinfo\n2.import Covidinfo as ci\n\n### Functions available\n\n1.covid_intro()\n2.covid_symptoms()\n3.covid_news()\n4.covid_precautions()\n5.vaccination_effects()\n6.india_total_cases()\n7.india_active_cases()\n8.india_recovered_cases()\n9.india_death_cases()\n10.india_death_previos_day()\n11.india_test_previos_day()\n12.india_positive_previos_day()\n13.india_vaccination_count()\n14.world_vaccination_count()\n15.world_vaccination_previos_day(\n16.world_active_cases()\n17.world_death_cases()\n18.world_total_cases()\n\n### Using functions exanote:- here imported using second way1. cp.covid_intro()  - it returns a short intro regarding covid-19\n2. cp.world_total_cases() - it returns total covid-19 cases count\n 3. cp.india_vaccination_count() - it returns total vaccination count in india\n 4. cp.covid_news()  -it top returns news regarding covid-19\n5. cp.vaccination_effects()   -prints post vaccination effects\n",
    keywords=['python', 'covid', 'covid-19', 'covid data', 'Covidinfo', 'corona virus'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)