

<br />
<p align="center">
    <img src="Resources/img.png" alt="Logo" height="50">

  <h3 align="center">nopcommerce Web UI Automation</h3>

  <p align="center">
    ...
    <br />
    <a href="#"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="#">View Demo</a>
    ·
    <a href="https://github.com/rfnshare/nopCommerceAutomation/issues">Report Bug</a>
    ·
    <a href="#">Request Feature</a>
  </p>
Introduction

This is an selenium based framework that interacts with nopcommerce Web App and can be used to automate given below

1. Registration
2. **Placing Order**
3. Homepage

# Setup

1. Clone this repository
    ```
    git clone https://github.com/rfnshare/nopCommerceAutomation.git
    ```

2. If you clone this repository before then run this on the project's root directory
    ```
    git pull
    ```
3. Update your test data into Excel file.
    ```
    Test/TestData/test_data.xlsx
    ```
   
4. Go to the project's root directory and install requirements(Recommended create virtual env first).
    ```
    pip install -r requirements.txt
    ```
   
5. For Smoke set without report, Run this script.
    ```
    python -m pytest -m smoke
    ```
   This will open a web app in the chosen browser & run smoke set.

6. For Full Run this script from cmd line without report.
    ```
    python -m pytest -v -s
    ```
## Run Automated Tests

* To run all test cases in cmd line with html & allure report, run
```
python -m pytest -m <smoke/regression> --html=Reports/HTMLReports/index.html --self-contained-html -s --alluredir=./Reports/AllureReports/<smoke/regression>_report_allure
```
* Generate Allure HTML Report
```
allure serve ./Reports/AllureReports/<smoke/regression>_report_allure
```
* To run all test cases without cmd line, Go to project root directory & run `TestRunner.py` file by double click.
```
TestRunner.py
```
This will create an HTML, allure report. You can find report in Reports directory, report automatically will open in browser.
* You can configure Jenkins to parameterized run your test cases & generate html report, allure report, junit report. Also send mail to recipient.

## Sample Test Report

![Allure report screenshot](https://raw.githubusercontent.com/startrug/phptravels-selenium-py/screenshots/allure_report.png "Allure report screenshot")

Report is generated in a chosen browser.
### Usage


For more examples,  please refer to the [Documentation](https://example.com)

<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/rfnshare/workspace-laznormal/issues) for a list of proposed features (and known issues).



<!-- CONTACT -->
## Contact

Abdullah Al Faroque - [@rfnshare](https://twitter.com/rfnshare) - aalfaroque@gmail.com

Project Link: [nopCommerce Web Automation](https://github.com/rfnshare/nopCommerceAutomation.git)


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/badge/contributors-0-yellow?style=for-the-badge
[contributors-url]: https://github.com/rfnshare/nopCommerceAutomation/graphs/contributors
[forks-shield]: https://img.shields.io/badge/froks-0-blue?style=for-the-badge
[forks-url]: https://github.com/rfnshare/nopCommerceAutomation/network/members
[stars-shield]: https://img.shields.io/badge/stars-0-red?style=for-the-badge
[stars-url]: https://github.com/rfnshare/nopCommerceAutomation/stargazers
[issues-shield]: https://img.shields.io/badge/issues-0-success?style=for-the-badge
[issues-url]: https://github.com/rfnshare/nopCommerceAutomation/issues
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/rfnshare