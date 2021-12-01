from flask import Flask
from controllers import main_page_controller

# if __name__ == "main":
main_page_controller.app.run(debug=True)
