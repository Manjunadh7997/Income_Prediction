from flask import Flask, request, jsonify,render_template
import mysql.connector

app = Flask(__name__)

# MySQL database configuration
config = {
    'user': 'root',
    'password': 'manju@123',
    'host': '127.0.0.1',
    'database': 'care_4_u',
    'raise_on_warnings': True
}

# Create a connection to the MySQL database
cnx = mysql.connector.connect(**config)

# Create a cursor object to execute SQL queries
cursor = cnx.cursor()
@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')
@app.route('/submit', methods=['POST'])
def submit_form():
    # Get the form data from the request
    age = request.form['age']
    workClass = request.form['workClass']
    education = request.form['education']
    maritalStatus = request.form['maritalStatus']
    occupation = request.form['occupation']
    relationship = request.form['relationship']
    race = request.form['race']
    sex = request.form['sex']
    capitalGain = request.form['capitalGain']
    capitalLoss = request.form['capitalLoss']
    hoursPerWeek = request.form['hoursPerWeek']
    nativeCountry = request.form['nativeCountry']

    # Insert the form data into the MySQL table
    query = ("INSERT INTO income_prediction "
             "(age, workClass, education, maritalStatus, occupation, relationship, race, sex, capitalGain, capitalLoss, hoursPerWeek, nativeCountry) "
             "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
    cursor.execute(query, (age, workClass, education, maritalStatus, occupation, relationship, race, sex, capitalGain, capitalLoss, hoursPerWeek, nativeCountry))

    # Commit the changes
    cnx.commit()

    # Close the cursor object
    cursor.close()

    # Return a success message
    return jsonify({'message': 'Form data submitted successfully'})

if __name__ == '__main__':
    app.run(debug=True)