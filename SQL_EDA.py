#!/usr/bin/env python
# coding: utf-8

# <center>
#     <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/labs/module_2/%20https:/cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/labs/images/IDSNlogo.png" width="300" alt="cognitiveclass.ai logo">
# </center>
# 
# <h1 align=center><font size = 5>Assignment: SQL Notebook for Peer Assignment</font></h1>
# 
# Estimated time needed: **60** minutes.
# 
# ## Introduction
# 
# Using this Python notebook you will:
# 
# 1.  Understand the Spacex DataSet
# 2.  Load the dataset  into the corresponding table in a Db2 database
# 3.  Execute SQL queries to answer assignment questions
# 

# ## Overview of the DataSet
# 
# SpaceX has gained worldwide attention for a series of historic milestones.
# 
# It is the only private company ever to return a spacecraft from low-earth orbit, which it first accomplished in December 2010.
# SpaceX advertises Falcon 9 rocket launches on its website with a cost of 62 million dollars wheras other providers cost upward of 165 million dollars each, much of the savings is because Space X can reuse the first stage.
# 
# Therefore if we can determine if the first stage will land, we can determine the cost of a launch.
# 
# This information can be used if an alternate company wants to bid against SpaceX for a rocket launch.
# 
# This dataset includes a record for each payload carried during a SpaceX mission into outer space.
# 

# ### Download the datasets
# 
# This assignment requires you to load the spacex dataset.
# 
# In many cases the dataset to be analyzed is available as a .CSV (comma separated values) file, perhaps on the internet. Click on the link below to download and save the dataset (.CSV file):
# 
# <a href="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/labs/module_2/data/Spacex.csv?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDS0321ENSkillsNetwork26802033-2022-01-01" target="_blank">Spacex DataSet</a>
# 

# ### Store the dataset in database table
# 
# **it is highly recommended to manually load the table using the database console LOAD tool in DB2**.
# 
# <img src = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/labs/module_2/images/spacexload.png">
# 
# Now open the Db2 console, open the LOAD tool, Select / Drag the .CSV file for the  dataset, Next create a New Table, and then follow the steps on-screen instructions to load the data. Name the new table as follows:
# 
# **SPACEXDATASET**
# 
# **Follow these steps while using old DB2 UI which is having Open Console Screen**
# 
# **Note:While loading Spacex dataset, ensure that detect datatypes is disabled. Later click on the pencil icon(edit option).**
# 
# 1.  Change the Date Format by manually typing DD-MM-YYYY and timestamp format as DD-MM-YYYY HH\:MM:SS.
# 
#     Here you should place the cursor at Date field and manually type as DD-MM-YYYY.
# 
# 2.  Change the PAYLOAD_MASS\_\_KG\_  datatype  to INTEGER.
# 
# <img src = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/labs/module_2/images/spacexload2.png">
# 

# **Changes to be considered when having DB2 instance with the new UI having Go to UI screen**
# 
# *   Refer to this insruction in this <a href="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/Labs_Coursera_V5/labs/Lab%20-%20Sign%20up%20for%20IBM%20Cloud%20-%20Create%20Db2%20service%20instance%20-%20Get%20started%20with%20the%20Db2%20console/instructional-labs.md.html?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDS0321ENSkillsNetwork26802033-2022-01-01">link</a> for viewing  the new  Go to UI screen.
# 
# *   Later click on **Data link(below SQL)**  in the Go to UI screen  and click on **Load Data** tab.
# 
# *   Later browse for the downloaded spacex file.
# 
# <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/labs/module_2/images/browsefile.png" width="800"/>
# 
# *   Once done select the schema andload the file.
# 
#  <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/labs/module_2/images/spacexload3.png" width="800"/>
# 

# In[2]:


get_ipython().system('pip install sqlalchemy==1.3.9')
get_ipython().system('pip install ibm_db_sa')
get_ipython().system('pip install ipython-sql')


# ### Connect to the database
# 
# Let us first load the SQL extension and establish a connection with the database
# 

# In[3]:


get_ipython().run_line_magic('load_ext', 'sql')


# **DB2 magic in case of old UI service credentials.**
# 
# In the next cell enter your db2 connection string. Recall you created Service Credentials for your Db2 instance before. From the **uri** field of your Db2 service credentials copy everything after db2:// (except the double quote at the end) and paste it in the cell below after ibm_db_sa://
# 
# <img src ="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/FinalModule_edX/images/URI.jpg">
# 
# in the following format
# 
# **%sql ibm_db_sa://my-username:my-password\@my-hostname:my-port/my-db-name**
# 
# **DB2 magic in case of new UI service credentials.**
# 
# <img src ="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/labs/module_2/images/servicecredentials.png" width=600>  
# 
# *   Use the following format.
# 
# *   Add security=SSL at the end
# 
# **%sql ibm_db_sa://my-username:my-password\@my-hostname:my-port/my-db-name?security=SSL**
# 

# In[ ]:





# In[ ]:





# In[5]:


get_ipython().run_line_magic('sql', 'ibm_db_sa://ydh08468:VIa9WhhY1aDA31hl@125f9f61-9715-46f9-9399-c8177b21803b.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud:30426/bludb?security=SSL')


# ## Tasks
# 
# Now write and execute SQL queries to solve the assignment tasks.
# 
# ### Task 1
# 
# ##### Display the names of the unique launch sites  in the space mission
# 

# In[6]:


get_ipython().run_line_magic('sql', 'SELECT DISTINCT LAUNCH_SITE FROM SPACEXDATASET')


# ### Task 2
# 
# ##### Display 5 records where launch sites begin with the string 'CCA'
# 

# In[7]:


get_ipython().run_line_magic('sql', "SELECT LAUNCH_SITE FROM SPACEXDATASET WHERE (LAUNCH_SITE) LIKE 'CCA%' LIMIT 5;")


# ### Task 3
# 
# ##### Display the total payload mass carried by boosters launched by NASA (CRS)
# 

# In[8]:


get_ipython().run_line_magic('sql', "SELECT SUM(PAYLOAD_MASS__KG_) FROM SPACEXDATASET WHERE CUSTOMER='NASA (CRS)';")


# ### Task 4
# 
# ##### Display average payload mass carried by booster version F9 v1.1
# 

# In[9]:


get_ipython().run_line_magic('sql', "SELECT AVG(PAYLOAD_MASS__KG_) FROM SPACEXDATASET WHERE BOOSTER_VERSION='F9 v1.1';")


# ### Task 5
# 
# ##### List the date when the first successful landing outcome in ground pad was acheived.
# 
# *Hint:Use min function*
# 

# In[10]:


get_ipython().run_line_magic('sql', "SELECT MIN(DATE) FROM SPACEX WHERE LANDING_OUTCOME = 'Success (ground pad)';")


# ### Task 6
# 
# ##### List the names of the boosters which have success in drone ship and have payload mass greater than 4000 but less than 6000
# 

# In[11]:


get_ipython().run_line_magic('sql', "SELECT BOOSTER_VERSION FROM SPACEX WHERE LANDING_OUTCOME = 'Success (drone ship)' AND PAYLOAD_MASS__KG_ > 4000 AND PAYLOAD_MASS__KG_ < 6000;")


# ### Task 7
# 
# ##### List the total number of successful and failure mission outcomes
# 

# In[16]:


get_ipython().run_line_magic('sql', 'SELECT sum(case when MISSION_OUTCOME LIKE \'%Success%\' then 1 else 0 end) AS "Successful Mission", sum(case when MISSION_OUTCOME LIKE \'%Failure%\' then 1 else 0 end) AS "Failure Mission" FROM SPACEX')


# ### Task 8
# 
# ##### List the   names of the booster_versions which have carried the maximum payload mass. Use a subquery
# 

# In[27]:


get_ipython().run_line_magic('sql', 'SELECT DISTINCT BOOSTER_VERSION FROM SPACEX WHERE PAYLOAD_MASS__KG_ =(SELECT MAX(PAYLOAD_MASS__KG_) FROM SPACEX);')


# ### Task 9
# 
# ##### List the failed landing_outcomes in drone ship, their booster versions, and launch site names for in year 2015
# 

# In[21]:


get_ipython().run_line_magic('sql', 'SELECT {fn MONTHNAME(DATE)} as "Month", BOOSTER_VERSION, LAUNCH_SITE FROM SPACEX WHERE year(DATE) = \'2015\' AND LANDING_OUTCOME = \'Failure (drone ship)\';')


# ### Task 10
# 
# ##### Rank the count of landing outcomes (such as Failure (drone ship) or Success (ground pad)) between the date 2010-06-04 and 2017-03-20, in descending order
# 

# In[23]:


get_ipython().run_line_magic('sql', "SELECT COUNT(LANDING_OUTCOME) FROM SPACEX WHERE LANDING_OUTCOME LIKE '%Success%' AND DATE > '2010-06-04' AND DATE < '2017-03-20'")


# ### Reference Links
# 
# *   <a href ="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/Labs_Coursera_V5/labs/Lab%20-%20String%20Patterns%20-%20Sorting%20-%20Grouping/instructional-labs.md.html?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDS0321ENSkillsNetwork26802033-2022-01-01&origin=www.coursera.org">Hands-on Lab : String Patterns, Sorting and Grouping</a>
# 
# *   <a  href="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/Labs_Coursera_V5/labs/Lab%20-%20Built-in%20functions%20/Hands-on_Lab__Built-in_Functions.md.html?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDS0321ENSkillsNetwork26802033-2022-01-01&origin=www.coursera.org">Hands-on Lab: Built-in functions</a>
# 
# *   <a  href="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/Labs_Coursera_V5/labs/Lab%20-%20Sub-queries%20and%20Nested%20SELECTs%20/instructional-labs.md.html?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDS0321ENSkillsNetwork26802033-2022-01-01&origin=www.coursera.org">Hands-on Lab : Sub-queries and Nested SELECT Statements</a>
# 
# *   <a href="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/Module%205/DB0201EN-Week3-1-3-SQLmagic.ipynb?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDS0321ENSkillsNetwork26802033-2022-01-01">Hands-on Tutorial: Accessing Databases with SQL magic</a>
# 
# *   <a href= "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DB0201EN-SkillsNetwork/labs/Module%205/DB0201EN-Week3-1-4-Analyzing.ipynb?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDS0321ENSkillsNetwork26802033-2022-01-01">Hands-on Lab: Analyzing a real World Data Set</a>
# 

# ## Author(s)
# 
# <h4> Lakshmi Holla </h4>
# 

# ## Other Contributors
# 
# <h4> Rav Ahuja </h4>
# 

# ## Change log
# 
# | Date       | Version | Changed by    | Change Description        |
# | ---------- | ------- | ------------- | ------------------------- |
# | 2021-10-12 | 0.4     | Lakshmi Holla | Changed markdown          |
# | 2021-08-24 | 0.3     | Lakshmi Holla | Added library update      |
# | 2021-07-09 | 0.2     | Lakshmi Holla | Changes made in magic sql |
# | 2021-05-20 | 0.1     | Lakshmi Holla | Created Initial Version   |
# 

# ## <h3 align="center"> © IBM Corporation 2021. All rights reserved. <h3/>
# 
