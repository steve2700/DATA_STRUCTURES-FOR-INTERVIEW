from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return 'This is the home page'

@app.route('/about', methods=['GET'])
def about():
    return 'This is the about page'

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Do something with the submitted form data
        return 'Thank you for submitting the form!'
    else:
        # Display the contact form
        return '''
        <form method="post">
            <label>Name:</label><br>
            <input type="text" name="name"><br>
            <label>Email:</label><br>
            <input type="email" name="email"><br>
            <label>Message:</label><br>
            <textarea name="message"></textarea><br>
            <input type="submit" value="Submit">
        </form>
        '''

if __name__ == '__main__':
    app.run(debug=True)
