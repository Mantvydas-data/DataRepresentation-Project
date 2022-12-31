# DataRepresentation-Project


<img src="https://images.unsplash.com/photo-1558494949-ef010cbdcc31?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1934&q=80" width="500"/>

Photo by <a href="https://unsplash.com/@tvick?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Taylor Vick</a> on <a href="https://unsplash.com/photos/M5tzZtFCOfs?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
  
  
<h2 style="text-align: center;">ATU Data Represntation Assessment 2022</h2>
<h2 style="text-align: center;">This repository contains Flask web application with RESTful API linked to a database and website that consumes API and performs CRUD operations.</h2>
<h4>Student: Mantvydas Jokubaitis</h4>

___

<h3>Introduction</h3>
<p>This repository contains assessment for Data Representation 2022 module. Files include: requirements, gitignore, readme file, Flask App, operational functions, website templates and its static files. <br>
Assessment instructions can be downloaded <a href="https://github.com/andrewbeattycourseware/datarepresentation/blob/main/project/Project%20Description.pdf">here</a>.</p>

<h3>Problem statement</h3>

<p>Create a Web application in Flask that has a RESTful API, the application should link to one or more database tables.</p>
<p>You should also create the web pages that can consume the API. I.e. performs CRUD operations on the data.</p>

<h3>Project</h3>

<p>Web application with web interface has been created based on lecture notes in ATU Data Representation module. Sever application is using Fask framework in viertual environment to route user requests and perform CRUD operations. Project theme is financial stock portfolio tracker where user can add stocks by ticker(stock identifier) also, name, purhase price and quantity.</p>
<p>Third party API is used to obtain market data and plot historical stock price changes for each position and also historical price comparison of two stocks entered. Website interface provides user friendly experience with comprehensive choices.</p>
<p> To try following best practices code is separeted out to respective files: CSS, Javascript. Flask templating is used for HTML files.</p>

___
<h3>Main Libraries and Packages Used</h3>

<p><a href="https://flask.palletsprojects.com/en/2.2.x/">Flask</a> - Flask is web framework in Python.</p>
<p><a href="https://www.anaconda.com/products/individual">Anaconda</a> - Python based platform for Data Science.</p>
<p><a href="https://www.mysql.com/">Mysql</a> - MySQL is an open-source relational database management system.</p>

___

<h3>Running the code</h3>

<p>Assignment has been completed using Python version 3.9.15 that can be downloaded <a href="https://www.python.org/downloads/">here</a> with Anaconda version 22.11.1 that can be downloaded <a href="https://www.anaconda.com/products/individual">here</a>. While Python and related libraries-packages can be installed separately it is encouraged to use latest Anaconda distribution that provides a wide variety of data science related tools.</p>

    
<p>To run the code <a href="https://github.com/Mantvydas-data/DataRepresentation-Project.git">repository</a> is to be cloned or files to be downloaded manually as a zip file by following <a href="https://docs.github.com/en/get-started/quickstart/fork-a-repo">Github guide</a>, zip file should be extracted.<br> Commander of choice can be used, that will require navigation to repository download location:<br></p>
<img src="https://github.com/Mantvydas-data/DataRepresentation-Project/blob/main/static/pictures/step1.PNG"/> 
<p>Create and activate virtual environment inside project directory:<br></p>
<img src="https://github.com/Mantvydas-data/DataRepresentation-Project/blob/main/static/pictures/step2.PNG"/> 
<p>Install required packages to virtual environment created based on requirenmnets.txt<br></p>
<img src="https://github.com/Mantvydas-data/DataRepresentation-Project/blob/main/static/pictures/step3.PNG"/> 
<p>As project conatains third party API keys they will be shared by email. Save .env file in project location.<br></p>
<p>Launch Flask server file:<br></p>
<img src="https://github.com/Mantvydas-data/pands-project2021/blob/main/readme_images/tim-russmann-hws29QtFM3U-unsplash.jpg" width="250"/> 
<p>Website should be accessible on localhost address 127.0.0.1:5000<br></p>
<img src="https://github.com/Mantvydas-data/DataRepresentation-Project/blob/main/static/pictures/step4.PNG"/> 
<p>Mysql database will be created containing stock table and one initial stock. Any stocks can be added and updated using website CRUD functionality. As long stock ticker is valid historical performance graphs will be generated. Stock identifier example list is available <a href="https://stockanalysis.com/stocks/">here</a>.<br></p>

___

<p>Project is hosted on PythonAnywhere and can be reached by following address: <a href="mattdata.pythonanywhere.com">mattdata.pythonanywhere.com</a><br></p>
<p>Main page:<br></p>
<img src="https://github.com/Mantvydas-data/DataRepresentation-Project/blob/main/static/pictures/pa1.PNG" width="500"/> 
<p>New stock and stock update:<br></p>
<img src="https://github.com/Mantvydas-data/DataRepresentation-Project/blob/main/static/pictures/pa2.PNG" width="250"/> <img src="https://github.com/Mantvydas-data/DataRepresentation-Project/blob/main/static/pictures/pa3.PNG" width="250"/>
<p>Historical stock price comparison page:<br></p>
<img src="https://github.com/Mantvydas-data/DataRepresentation-Project/blob/main/static/pictures/pa4.PNG" width="500"/>  

<h3>The End.</h3>

