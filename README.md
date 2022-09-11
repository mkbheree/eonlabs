# EonLabs
Data Collection TTA
<div id="top"></div>

<!-- ABOUT TTA -->
## About The Project

Python script that collects Google Trends weekly and daily data with the term "bitcoin" since 2015-01-01 and saves the 
results in csv format.
<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Python 3.8](https://www.python.org/downloads/release/python-380/)
* [pytrends](https://pypi.org/project/pytrends/)
* [Pandas](https://pandas.pydata.org/)


<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

The goal here is to use the third-party module "pytrends" to collect daily data from Google Trends for the key phrase 
"bitcoin." Use the pandas package to convert the daily data to weekly data.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* pytrends
  ```sh
  pip install pytrends
  ```
* pandas
  ```sh
  pip install pandas
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/mkbheree/eonlabs.git
   ```
### Execution

1. Command line interface
   ```sh
   python /path_to_dir/google-trends.py
   ```
2. or through IDE, Edit configuration to set the 
interpreter to python and run the google-trends.py file.


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- Approach-->
## Approach

- I started with generic methods like "build payload" and "interest over time," which collected weekly data.This method 
is not appropriate for converting weekly data to daily data.
- The above-mentioned submitted approach took one hour to program.
<p align="right">(<a href="#top">back to top</a>)</p>
