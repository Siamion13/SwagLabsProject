# SwagLabsProject

This is a Selenium automation project for testing the SwagLabs web application. The goal of this project is to demonstrate automated testing skills using Selenium WebDriver, including test case creation, execution, and reporting.


## Technologies Used

- [Python](https://www.python.org/) - Programming language
- [Selenium](https://www.selenium.dev/) - Web automation framework
- [pytest](https://pytest.org/) - Testing framework

## Features

- Login Functionality test
- Inventory Functionality test
- Cart Functionality test
- Check Out Step One Functionality test
- Check Out Step Two Functionality test
- Check Out Complete Functionality test

## Installation

To get started with this project, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Siamion13/SwagLabsProject.git

2. Navigate to the project directory:

cd SwagLabsProject

3. Create a virtual environment (optional but recommended if it is not created automatically. In case it is created automatically (.venv) should be visible in the terminal)):

python -m venv venv

4. Activate the virtual environment (if the virtual environment was not created automatically in step 3):

For Windows:

venv\Scripts\activate

For macOS/Linux:

source venv/bin/activate

5. Install required packages:
   
pip install -r requirements.txt

6. Set up '.env' file:

Create a file '.env' in the root of the project based on the '.env.example'

Include the public credentials for testing on the Sauce Demo website, which you could find in the '.env.example':

7. Run the tests:

pytest --alluredir=reports

8. Generate Allure Report:

allure serve reports
