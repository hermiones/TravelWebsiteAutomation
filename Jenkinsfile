# Navigate to the project directory
cd TravelWebsiteAutomation

# Install Python dependencies
pip install -r requirements.txt

# Download and configure Selenium WebDriver
# Make sure to replace '/path/to/chromedriver' with the actual path to your WebDriver executable
#echo "webdriver_path = '/path/to/chromedriver'" > config.py

# Run the automation script
python travel_automation_script.py

# Generate Allure Reports
pytest --alluredir=./allure-results
allure generate ./allure-results --clean
allure open ./allure-report
