 <h1 align="center">⚕️ ML Model Deployment with Flask</h1>

<p align="center">
  <em>A simple web application to deploy a machine learning model predicting the ten-year risk of coronary heart disease</em>
</p>

<hr/>

<h2>🎯 Objective</h2>

<p>
  This repository demonstrates an example of deploying a trained machine learning model to estimate the ten-year risk of coronary heart disease (TenYearCHD). Model deployment is a critical phase in the lifecycle of an ML project because it allows non-technical users, such as physicians, to leverage model predictions to automate and accelerate what would otherwise be a time-consuming process.
</p>

<h2>⚙️ How It Works</h2>

<ol>
  <li><strong>Application Initialization</strong>
    <ul>
      <li>A Flask app instance is created to initialize the web server.</li>
      <li>The pretrained machine learning model is loaded using the <code>joblib</code> library (stored as a <code>.pkl</code> file).</li>
    </ul>
  </li>
  <li><strong>Homepage (<code>/</code>)</strong>
    <ul>
      <li>The <code>/</code> route serves an HTML page (<code>index.html</code>) displaying a form.</li>
      <li>Users fill out this form with relevant information (e.g., age, gender, smoking habits, etc.).</li>
    </ul>
  </li>
  <li><strong>Data Submission (<code>/predict</code>)</strong>
    <ul>
      <li>When the form is submitted, the data is sent via an HTTP POST request.</li>
      <li>The data is retrieved using Flask’s <code>request.form.to_dict()</code> and converted into a Pandas DataFrame to match the model input format.</li>
      <li>Data types are explicitly set to ensure compatibility with the model.</li>
    </ul>
  </li>
  <li><strong>Prediction and Response</strong>
    <ul>
      <li>The model performs prediction on the input data.</li>
      <li>The prediction result (0 or 1, indicating absence or presence of ten-year coronary heart disease risk) is returned as a JSON response using Flask’s <code>jsonify</code>.</li>
    </ul>
  </li>
</ol>

<h2>🧰 Technologies Used</h2>

<ul>
  <li><strong>Flask</strong>: To build the web application and handle HTTP requests.</li>
  <li><strong>Joblib</strong>: To load the saved machine learning model from a <code>.pkl</code> file.</li>
  <li><strong>Pandas</strong>: To preprocess and transform input data into a DataFrame.</li>
  <li><strong>HTML</strong>: To create the user input form displayed in the web interface.</li>
</ul>

<h2>🚀 Example Usage</h2>

<ol>
  <li>Start the Flask server by running:
    <pre><code>python app.py</code></pre>
  </li>
  <li>Open a web browser and navigate to <code>http://localhost:5000/</code>.</li>
  <li>Fill in the form fields with patient information.</li>
  <li>Submit the form to receive a prediction indicating whether the patient is at risk of coronary heart disease in the next ten years.</li>
</ol>

<hr/>

<p align="center">
  <img src="https://media.giphy.com/media/hvRJCLFzcasrR4ia7z/giphy.gif" width="300" alt="Done"/>
</p>
