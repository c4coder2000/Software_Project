from flask import Flask, flash, redirect, render_template, request, url_for
import pymysql

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong secret key for session management


def get_db_connection():
    return pymysql.connect(
        host='localhost',
        user='root',  # Replace with your MySQL username
        password='hassnain2000',  # Replace with your MySQL password
        database='lms',
        cursorclass=pymysql.cursors.DictCursor
    )


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/admin_login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM admin WHERE username = %s AND password = %s', (username, password))
        admin = cursor.fetchone()
        connection.close()
        if admin:
            return redirect(url_for('admin_page'))
        else:
            flash('Incorrect username or password.')
            return redirect(url_for('admin_login'))
    return render_template('admin_login.html')


@app.route('/member_login', methods=['GET', 'POST'])
def member_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        connection = get_db_connection()
        cursor = connection.cursor()

        # Query to fetch the member
        cursor.execute('SELECT * FROM member WHERE username = %s AND password = %s', (username, password))
        member = cursor.fetchone()
        connection.close()

        if member:
            # Correct credentials, redirect to the member page
            return redirect(url_for('member_page'))
        else:
            # Incorrect credentials
            flash('Incorrect username or password.')
            return redirect(url_for('member_login_page'))
    
    return render_template('member_login.html')


@app.route('/admin.html')
def admin_page():
    return render_template('admin.html')


@app.route('/member.html')
def member_page():
    return render_template('member.html')


@app.route('/members')
def contact_page():
    return "Contact Page Placeholder"


@app.route('/manage_books.html')
def manage_books():
    return render_template('manage_books.html')


@app.route('/manage_members.html')
def manage_members():
    return render_template('manage_members.html')


@app.route('/manage_loans.html')
def manage_loans():
    return render_template('manage_loans.html')


@app.route('/manage_authors.html')
def manage_authors():
    return render_template('manage_authors.html')


@app.route('/report.html')
def reports():
    return render_template('report.html')


@app.route('/home.html')
def home_button():
    return render_template('home.html')


@app.route('/admin_login.html')
def admin_login_page():
    return render_template('admin_login.html')


@app.route('/member_login.html')
def member_login_page():
    return render_template('member_login.html')

@app.route('/signup.html')
def sign_up():
    return render_template('signup.html')


if __name__ == '__main__':
    app.run(debug=True)
