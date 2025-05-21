from flask import Flask, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# MySQL database connection settings
username = 'root'
password = 'manju@123'
host = '127.0.0.1'
database = 'care_4_u'

# Create a MySQL connection
cnx = mysql.connector.connect(
    user=username,
    password=password,
    host=host,
    database=database
)

# Create a cursor object
cursor = cnx.cursor()

# Create a table if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS income (
        id INT AUTO_INCREMENT,
        age INT,
        workClass VARCHAR(50),
        education INT,
        maritalStatus INT,
        occupation INT,
        relationship INT,
        race INT,
        sex INT,
        capitalGain INT,
        capitalLoss INT,
        hoursPerWeek INT,
        nativeCountry INT,
        PRIMARY KEY (id)
    )
""")

# Commit the changes
cnx.commit()

@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # Get the user input values
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

        # Insert the values into the table
        cursor.execute("""
            INSERT INTO income (
                age, workClass, education, maritalStatus, occupation, relationship, race, sex, capitalGain, capitalLoss, hoursPerWeek, nativeCountry
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            age, workClass, education, maritalStatus, occupation, relationship, race, sex, capitalGain, capitalLoss, hoursPerWeek, nativeCountry
        ))

        # Commit the changes
        cnx.commit()

        # Redirect to the result page
        return redirect(url_for('result'))

    return '''
        <html>
            <body>
                <h1>Predict Your Income</h1>
                <form action="" method="post">
                    <!-- form fields here -->
                    <button type="submit">Predict</button>
                </form>
            </body>
        </html>
    '''

@app.route('/result')
def result():
    return '''
        <html>
            <body>
                <h1>Result</h1>
                <!-- display the result here -->
            </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)