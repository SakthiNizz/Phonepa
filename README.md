# Phonepa

![image](https://user-images.githubusercontent.com/107666598/218308092-94dcfc7c-5109-45ca-824c-9849f02584e3.png)

# Problem Statement:
  The Phonepe pulse Github repository contains a large amount of data related to various metrics and statistics. The goal is to extract this data and process it to obtain insights and information that can be visualized in a user-friendly manner.
  
# Approach:
    1. Data extraction: Clone the Github using scripting to fetch the data from the Phonepe pulse Github repository and store it in a suitable format such as CSV or JSON.
    2. Data transformation: Use a scripting language such as Python, along with libraries such as Pandas, to manipulate and pre-process the data. This mayinclude cleaning the data, handling missing values, and transforming the data into a format suitable for analysis and visualization.
    3. Database insertion: Use the "mysql-connector-python" library in Python to connect to a MySQL database and insert the transformed data using SQL commands.
    4. Dashboard creation: Use the Streamlit and Plotly libraries in Python to create an interactive and visually appealing dashboard. Plotly's built-in geo map functions can be used to display the data on a map and Streamlit can be used to create a user-friendly interface with multiple dropdown options for users to select different facts and figures to display.
    5. Data retrieval: Use the "mysql-connector-python" library to connect to the MySQL database and fetch the data into a Pandas dataframe. Use the data in the dataframe to update the dashboard dynamically.
    6. Deployment: Ensure the solution is secure, efficient, and user-friendly. Test the solution thoroughly and deploy the dashboard publicly, making it accessible to users.
    
# Results:
    The result of this project will be a live geo visualization dashboard that displays information and insights from the Phonepe pulse Github repository in an interactive and visually appealing manner. The dashboard will have at least 10 different dropdown options for users to select different facts and figures to display. The data will be stored in a MySQL database for efficient retrieval and the dashboard will be dynamically updated to reflect the latest data.
    Users will be able to access the dashboard from a web browser and easily navigate the different visualizations and facts and figures displayed. The dashboard will provide valuable insights and information about the data in the Phonepe pulse Github repository, making it a valuable tool for data analysis and decision-making.
    Overall, the result of this project will be a comprehensive and user-friendly solution for extracting, transforming, and visualizing data from the Phonepe pulse Github repository. 
    
# Procedure:

Import required python libraries 
  1. streamlit
  2. pandas
  3. json
  4. plotly.express
  
 Command for run phonpe script:
 
    Open command Prompt. 
    
    Go to such directories.
    
    Run -> streamlit run overview.py
    
# Outcomes:

![p1](https://user-images.githubusercontent.com/107666598/218307951-86dbe8e6-483c-47f3-9e39-3b868da4132c.png)

![p2](https://user-images.githubusercontent.com/107666598/218307968-b49c8114-2e85-40e9-8160-2dae945b0d58.png)

![p3](https://user-images.githubusercontent.com/107666598/218307976-7ef9ed08-a679-491a-b0cd-4f26a100b10d.png)

![p4](https://user-images.githubusercontent.com/107666598/218307980-bda43c7f-62f1-4a14-8eee-9aef9ac01c20.png)
