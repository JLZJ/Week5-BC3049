#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask
import joblib


# In[2]:


app = Flask(__name__)


# In[3]:


from flask import request, render_template

@app.route("/", methods = ["GET", "POST"])
def index(): 
  if request.method == "POST":
    sugar = request.form.get("sugar")
    milk = request.form.get("milk")
    model = joblib.load("CTaste")
    pred = model.predict([[sugar, milk]])
    if pred==0:
        s = "Predicted taste is bad"
    else:
        s = "Predicted taste is good"
    
    return(render_template("index.html", result = s))
  else:
    return(render_template("index.html", result = "Predict Chocolate Taste"))


# In[ ]:


app.run()


# In[ ]:




