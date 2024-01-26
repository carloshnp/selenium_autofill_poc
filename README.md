# Forms autofill proof of concept

This script demonstrates how to use Selenium to automate form filling and submission on a web page.
It uses the SeleniumWire library to intercept and inspect network requests and responses.

The script performs the following steps:
1. Opens a Chrome browser using the Chrome WebDriver.
2. Navigates to a local web page.
3. Finds the email and password fields on the page and fills them with test values.
4. Submits the login form.
5. Inspects the network requests and prints the response message if it contains a specific pattern.
6. Waits for the page URL to change.
7. Finds a text field on the page and fills it with a test message.
8. Submits the form again.
9. Inspects the network requests and prints the response message if it contains a specific pattern.
10. Quits the browser.

Note: This script assumes that the Chrome WebDriver is installed and the web page being accessed is running locally.

## How to run

1. Clone this repository and install all needed dependencies:
   
   ```bash
   cd path/to/repository
   npm i
   pip install -r requirements.txt
   ```

2. Run the Node.js server:
   
    ```bash
    npm start
    ```

3. Open the `index.html` with some similar tool like Live Server on VS Code.

4. Make sure that the port of the localhost is 5500.

5. Run the Python script:

    ```bash
    python autofill.py
    ```
