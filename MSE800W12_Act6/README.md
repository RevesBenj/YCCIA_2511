
# Flask Image Hyperlink Project


## Requirements

- Python 3.8 or higher
- Flask

Install Flask using pip:

pip install flask

---

## Running the Application

Run the Flask application:

python app.py

The server will start at:

http://127.0.0.1:5000

Open the link in a web browser.

---

## Application Pages

### Home Page
Displays:
- Greeting message
- Link to Flask Quickstart documentation
- Link to show the image

URL:
http://127.0.0.1:5000

### Image Page
Displays the Flask image stored in the static folder.

URL:
http://127.0.0.1:5000/show-image

---

## Key Flask Concepts Demonstrated

- Flask routing (@app.route)
- HTML template rendering (render_template)
- Static file handling using url_for('static')
- Navigation using hyperlinks

