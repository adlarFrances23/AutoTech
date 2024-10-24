
import time
import csv
from PyQt6 import QtCore, QtGui, QtWidgets
from playwright.sync_api import sync_playwright


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("AutoTech")
        Form.resize(579, 354)
        Form.setStyleSheet("*{\n"
                           "background-color: #66a3ff;}")
        self.line = QtWidgets.QFrame(parent=Form)
        self.line.setGeometry(QtCore.QRect(0, 30, 581, 16))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(200, 10, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label.setFont(font)
        self.label.setStyleSheet("font-size:20px;\n"
                                 "")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit.setGeometry(QtCore.QRect(140, 70, 271, 31))
        self.lineEdit.setStyleSheet("Background-color:none;\n"
                                    "font-size:15px")
        self.lineEdit.setObjectName("lineEdit")
        self.comboBox = QtWidgets.QComboBox(parent=Form)
        self.comboBox.setGeometry(QtCore.QRect(140, 170, 271, 21))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.checkBox_4 = QtWidgets.QCheckBox(parent=Form)
        self.checkBox_4.setGeometry(QtCore.QRect(320, 220, 71, 16))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(parent=Form)
        self.checkBox_5.setGeometry(QtCore.QRect(140, 220, 70, 16))
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(parent=Form)
        self.checkBox_6.setGeometry(QtCore.QRect(230, 220, 71, 16))
        self.checkBox_6.setObjectName("checkBox_6")
        self.login_btn = QtWidgets.QPushButton(parent=Form)
        self.login_btn.setGeometry(QtCore.QRect(170, 260, 211, 41))
        self.login_btn.setMouseTracking(True)
        self.login_btn.setStyleSheet("background:black;\n"
                                     "border: 1px solid #3385ff;\n"
                                     "color:white;\n"
                                     "font-family: Georgia, serif;\n"
                                     "font-size:15px;\n"
                                     "\n"
                                     "\n"
                                     "")
        self.login_btn.setObjectName("login_btn")
        self.login_btn.clicked.connect(self.Yahoo)
        self.comboBox_2 = QtWidgets.QComboBox(parent=Form)
        self.comboBox_2.setGeometry(QtCore.QRect(140, 130, 271, 21))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Yahoo"))
        self.lineEdit.setPlaceholderText(_translate("Form", "File Name"))
        self.comboBox.setItemText(0, _translate("Form", "Chromium"))
        self.comboBox.setItemText(1, _translate("Form", "webkit"))
        self.checkBox_4.setText(_translate ("Form", "Keyboard Action"))
        self.checkBox_5.setText(_translate("Form", "Random Action"))
        self.checkBox_6.setText(_translate("Form", "Mouse action"))
        self.login_btn.setText(_translate("Form", "Login"))
        self.comboBox_2.setItemText(0, _translate("Form", "Without_Proxy"))
        self.comboBox_2.setItemText(1, _translate("Form", "Proxy"))

    def Yahoo(self):
        filename = self.lineEdit.text()
        browser_set = self.comboBox.currentText()
        proxy = self.comboBox_2.currentText()
        print(f"Proxy setting: {proxy}")
        print(f"Browser choice: {browser_set}")

        with sync_playwright() as p:
            if proxy == "Without_Proxy":
                self.process_emails_without_proxy(p, filename, browser_set)
            else:
                self.process_emails_with_proxy(p, filename, browser_set)

    def process_emails_without_proxy(self, p, filename, browser_set):
        try:
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    try:
                        email, e_password, auth_file = row[0], row[1], row[6]  # Adjust indices as needed
                        self.perform_email_actions(p, email, e_password, auth_file, browser_set)
                    except IndexError as e:
                        print(f"Index error: {e} for row: {row}")
                    except Exception as e:
                        print(f"An error occurred while processing email: {e}")
        except FileNotFoundError:
            print(f"File {filename} not found.")
        except Exception as e:
            print(f"An error occurred: {e}")


    def process_emails_with_proxy(self, p, filename):
        try:
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    try:
                        # Ensure that the row has enough columns
                        if len(row) < 7:
                            print(f"Row has insufficient columns: {row}")
                            continue

                        email, e_password, proxy_addr, port, prox_user, proxy_pass, auth_file = row[:7]
                        self.perform_email_actions_with_proxy(p, proxy_addr, port, prox_user, proxy_pass, auth_file)
                    except IndexError as e:
                        print(f"Index error: {e} for row: {row}")
                    except Exception as e:
                        print(f"An error occurred while processing email: {e}")

        except:
            print("ERROR")

    def process_emails_with_proxy(self, p, filename, browser_set):
        try:
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) < 7:
                        print(f"Row has insufficient columns: {row}")
                        continue

                    email, e_password, proxy_addr, port, prox_user, proxy_pass, auth_file = row[:7]
                    self.perform_email_actions_with_proxy(p, email, e_password, proxy_addr, port, prox_user, proxy_pass, auth_file, browser_set)

        except FileNotFoundError:
            print(f"File {filename} not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def perform_email_actions_with_proxy(self, p, email, e_password, proxy_addr, port, prox_user, proxy_pass, auth_file, browser_set):
        print(f"Using proxy: {proxy_addr}:{port} with user: {prox_user}")

        # Set up the proxy configuration
        browser = None
        try:
            if browser_set == "Chromium":
                browser = p.chromium.launch(
                    proxy={
                        "server": f"{proxy_addr}:{port}",
                        "username": prox_user,
                        "password": proxy_pass,
                    },
                    headless=False
                )
            elif browser_set == "Webkit":
                browser = p.webkit.launch(
                    proxy={
                        "server": f"{proxy_addr}:{port}",
                        "username": prox_user,
                        "password": proxy_pass,
                    },
                    headless=False
                )
            else:
                print("Invalid browser choice.")
                return

            context = browser.new_context(storage_state=f"./Auth/{auth_file}")  # Load authentication state if needed
            page = context.new_page()

            # Navigate to the Yahoo mail page
            page.goto('https://mail.yahoo.com/', wait_until="networkidle")
            page.wait_for_timeout(10000)  # Adjust timeout as needed

            try:
                page.goto('https://mail.yahoo.com/', wait_until="networkidle")
                # Click on Mail link (assuming this is where you want to navigate)
                page.click('xpath=//*[@id="app"]/div[2]/div/div[1]/nav/div/div[3]/div[1]/ul/li[7]/div')
                page.wait_for_timeout(9000)  # Adjust timeout as needed

                # Click on checkboxes and perform actions (example)
                checkboxes = page.query_selector_all('button[data-test-id="icon-btn-checkbox"]')
                checkboxes_size = len(checkboxes)
                for checkbox in checkboxes:
                    checkbox.click()
                    page.wait_for_timeout(3000)  # Adjust timeout as needed
                    page.locator("[data-test-id=\"toolbar-not-spam\"]").click()
                    page.wait_for_timeout(3000)
                page.locator("[data-test-id=\"folder-list\"] div").filter(has_text="Inbox").click()

                # Example: Print the email content (if needed)
                emails = page.query_selector_all('span[data-test-id="senders_list"]')
                email_size = len(emails)
                print(email_size)
                emails[0].click()
                for i in range(checkboxes_size):
                    page.locator("[data-test-id=\"message-view\"]").press("ArrowRight")
                    time.sleep(3)
                page.locator("[data-test-id=\"toolbar-back-to-list\"]").click()
                page.wait_for_timeout(3000)
            except Exception as e:
                print(f"An error occurred while processing email: {e}")
            finally:
                context.close()
                browser.close()

        except Exception as e:
            print(f"An error occurred while processing email actions with proxy: {e}")
        finally:
            # Close the browser context and browser
            context.close()
            browser.close()

    def perform_email_actions(self, p, email_id, e_password, auth_file, browser_set):
        # This method can handle actions like logging into Yahoo and performing email operations
        print(f"Performing actions for email: {email_id}")

        # Launch the browser
        if browser_set == "Chromium":
            browser = p.chromium.launch(headless=False)
        elif browser_set == "Webkit":
            browser = p.webkit.launch(headless=False)
        # browser = p.chromium.launch(headless=False)
        context = browser.new_context(storage_state="./Auth/" + auth_file)  # Load authentication state if needed
        page = context.new_page()

        try:
            page.goto('https://mail.yahoo.com/', wait_until="networkidle")
            # Click on Mail link (assuming this is where you want to navigate)
            page.click('xpath=//*[@id="app"]/div[2]/div/div[1]/nav/div/div[3]/div[1]/ul/li[7]/div')
            page.wait_for_timeout(9000)  # Adjust timeout as needed

            # Click on checkboxes and perform actions (example)
            checkboxes = page.query_selector_all('button[data-test-id="icon-btn-checkbox"]')
            checkboxes_size = len(checkboxes)
            for checkbox in checkboxes:
                checkbox.click()
                page.wait_for_timeout(3000)  # Adjust timeout as needed
                page.locator("[data-test-id=\"toolbar-not-spam\"]").click()
                page.wait_for_timeout(3000)
            page.locator("[data-test-id=\"folder-list\"] div").filter(has_text="Inbox").click()

            # Example: Print the email content (if needed)
            emails = page.query_selector_all('span[data-test-id="senders_list"]')
            email_size = len(emails)
            print(email_size)
            emails[0].click()
            for i in range(checkboxes_size):
                page.locator("[data-test-id=\"message-view\"]").press("ArrowRight")
                time.sleep(3)
            page.locator("[data-test-id=\"toolbar-back-to-list\"]").click()
            page.wait_for_timeout(3000)
        except Exception as e:
            print(f"An error occurred while processing email: {e}")
        finally:
            context.close()
            browser.close()
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
