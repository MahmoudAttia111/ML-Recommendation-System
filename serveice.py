# -*- coding: utf-8 -*-
"""
Created on Thu Jul 10 11:24:06 2025

@author: Lenovo
"""

from flask import Flask
from Content_Based_Recommender import ContentBasedRecommender
app = Flask(__name__)
@app.route('/recommend/<string:userId>', methods=['GET'])
def recommend_item(userId):
    stored_model = ContentBasedRecommender()
    result = stored_model.recommend_items(int(userId))
    return result.to_json(orient='records',lines=True)
if __name__=='__main__':
    app.run(threaded=True ,host='0.0.0.0',port=5000)    