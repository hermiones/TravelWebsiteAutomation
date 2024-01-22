# ✈️ Travel Website Automation Script 🤖

## STAR Approach

### Situation 🌍

In response to the need for efficient testing and automation of the BlazeDemo travel website, this project was initiated. The goal was to automate tasks such as searching for flights, selecting hotels, and making reservations to streamline the testing process.

### Task 📋

The task was to create a robust automation script using Selenium WebDriver, Python, and Pytest. The project aimed to provide a solution for automating interactions with the travel website [BlazeDemo](https://blazedemo.com/). The primary assignment was based on a Techlistic challenge, and the intention was to create an easily maintainable and scalable automation framework.

### Action 🚀

To address this task, the following steps were taken:

1. **Script Development 🖥️:**
   - A main automation script (`travel_automation_script.py`) was developed to interact with the BlazeDemo website.
   - Configuration settings were modularized in the `conftest.py` file, allowing for easy customization.

2. **Dependency Management 📦:**
   - A `requirements.txt` file was created to document and manage the required Python packages.

3. **Setup Instructions 🛠️:**
   - Clear setup instructions were provided in the README, including steps to clone the repository, install dependencies, configure Selenium WebDriver, and run the automation script.

4. **Test Case Coverage 🧪:**
   - Test cases were developed to cover various scenarios related to the login functionality of the BlazeDemo website.

5. **Documentation  📝:**
   - Clear documentation was added in the README to guide users on how to use the script, and contribute to the project.

### Result 🌟

The result of this project is a functional and well-documented automation script that addresses the initial testing needs for BlazeDemo. The script allows for efficient and repeatable testing of the website's features, providing value in terms of time savings and accuracy in the testing process.

## Setup Instructions 🚀

To run the automation script successfully, follow the setup instructions below:

1. **Clone the Repository:**
   - Clone this repository to your local machine:
     ```bash
     git clone https://github.com/hermiones/TravelWebsiteAutomation.git
     ```

2. **Navigate to the Project Directory:**
   - Change to the project directory:
     ```bash
     cd TravelWebsiteAutomation
     ```

3. **Install Python:**
   - Ensure you have Python version 3.5 or higher installed on your system.

4. **Install Pip:**
   - Install the pip package, a package manager for Python.

5. **Install Dependencies:**
   - Install the required Python packages using the following command:
     ```bash
     pip install -r requirements.txt
     ```

6. **Configure Selenium WebDriver:**
   - Download the appropriate WebDriver for your browser (e.g., ChromeDriver) from [here](https://chromedriver.chromium.org/).
   - Specify the local path where the WebDriver executable is saved in the `config.py` file.

7. **Run the Automation Script:**
   - After completing the setup, execute the automation script using the following command:
     ```bash
     python travel_automation_script.py
     ```
8. **Generate the Allure Reports of the tests:**
9. - execute the tests using this command and generate the report
   - ```pytest --alluredir=./allure-results```
   - ```allure  generate './allure-results' --clean  ``` 
   - ``` allure open './allure-report' ```

## Software Specifications 🛠️

- **Browser:** Google Chrome
- **Python Version:** 3.5
- **PIP Version:** [Specify your PIP version]
- **IDE:** PyCharm

## Project Structure 📂

- **`Testcases Folder`:** The main automation script.
- **`conftest.py`:** Configuration file for specifying website URL (https://blazedemo.com/), login credentials, etc.
- **`requirements.txt`:** List of required Python packages.
- **`report.html`:** Test reports in HTML structure. 

## Contributing 🤝

Contributions are welcome! If you have suggestions, bug reports, or want to add features, please create an issue or submit a pull request.

Happy automating! 🤖✈️
