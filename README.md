# MouseHunt Catalogue Website
#### Video Demo:  https://youtu.be/qiNzonHHEGw

#### Description: 
This is a website inspired by MouseHunt, a Facebook game where users sound the horn every 15 minutes to capture mice. The website is developed using html, css, javascript and flask. This website is basically a catalogue of mice from the game which keeps track of all the information of the different mice in the game. Some unique functions of this website includes a login and register page, a page which allows users to add new mice into the catalogue, and an interactive sidebar.


#### File description and usage:
##### Python files
The `__init__.py` file imports the `flask` and `flask_sqlalchemy` library, initialising the website and creating the database `mouse.db`

The `main.py` file runs the website into a live server

The `auth.py` file runs the backend of the **login and register pages** which creates and adds user data into the `mouse.db` database using the `flask` and `flask_sqlalchemy` library

The `views.py` file is where all the different pages of mouse categories are accessed

The `models.py` file creates and edits the **user table and mouse table** in `mouse.db`

##### HTML file
The `layout.html` file lays the groundwork for the website. It contains the navigation bar, the side bar and login, logout and register buttons. Using `jinja`, the navigation bar, side bar and logout buttons are only shown when the user is logged in. The login and register buttons are shown when an anonymous user enters the website. 

The `register.html` file contains a username input field, a password input field and a confirm password input field which adds the username into the database if it fulfils the conditions of a valid username and password and that the username does not already exist in the `mouse.db` database. The username is then added to the table `User` in `mouse.db` with a password hash generated using `generate_password_hash` function imported from the `werkzeug.security` library.

The `login.html` file contains a username input field and a password input field and logs the user in only if the username exists in the `mouse.db` database and the password matches the user. 

The `home.html` file is the main page after the user successfully logs in. It displays the description of the website and the credits.

The `add.html` file is another page that contains input fields which allows the user to add a new mouse into the table `Mouse` in `mouse.db`. The `Mouse` table contains `mouseName` and `mouseImg` which are unique table columns as every mouse in the game is different from one another. It also contains other columns of the mouse containing some of the other information of the mouse.

The other pages are all the different categories of mice which is a gallery of mice in the mouse group and pages containing the individual mice. 

##### Javascript file
The `layout.js` file handles the **animation** of the sidebar created using simple javascript for loops. The menu div in `layout.html` contains the `onclick` html tag which calls the function `openSidebar`, running a script in `layout.js` which shows the sidebar using `.style.display = "block"`

##### CSS file
The different css files handle the **design** of all the pages in the website


#### Using the website:
When opening the website, the user will first be directed to the login page where the user has to enter the username and password. Without logging in, the user has no access to the main functions of the website. 

Clicking on the register button, the user will be brought to the register page to register a usernae and a password.

Once registered, the user will be redirected to the home page which shows a description of the website and a table of contents. A hamburger menu also appears which allows the user to open the sidebar and navigate the website.

The website has a add mouse page that allows the user to add a mouse into the database with the different information of the mice. 

After adding the mouse, the mouse will appear on the page with the category that the mouse falls in. 
