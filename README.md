## HD - Code Challange

### Objectives:

  1. Use the Google Trends API to retrieve 3 years of data from 5 different keywords and deliver the data to GCP Cloud Storage.

  2. Create a Dockerfile that allows to containerize the first requirement.

### Work Files:

   #### 1. Q1.py (python script)
   #### 2. requirements.txt (python packages) 
   #### 3. json key file
   #### 4. Dockerfile
   #### 5. df_trends.csv (Output file)
   #### 6. #Q1.ipynb (for better readability)

### Description:
I have used Visual Studio Code editor for all the tasks as they can handle python and Dockerfile.

Pull google trends data for five keywords ('machine learning','covid','Donald Trump','Apple','Merkel) in two countries (US and Germany). 

Using Python, there are six steps to achieve this:

  1. Install pytrends API
  2. Get exact keywords
  3. Pull Google trends data by exact keywords by country
  4. Visualize Google trends 
  5. Extract the dataframe to a CSV file
  6. Push the CSV file to Google Cloud bucket Storage 

### Excecute the files:
  - Gather all the 4 (Q1.py, requirements.txt, json key file, Dockerfile) files in one folder and make it as a working directory.
  - Run the Q1.py first and confirm there are no executional errors.
  - Open the Dockerfile and use `docker build` to create a docker image image.
  - once the docker image is ready, use the `docker run` command to execute.
  
### Bonus Task: Creating a DAG to schedule the process using Airflow.
  - A python (HD-Bonus.py) file with instructions on creating a DAG.
  



