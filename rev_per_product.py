import pandas as pd
import ast
import numpy as np
import json
import os
dataset = pd.read_csv('./sales_transaction.csv')
"""X = dataset.drop(['start_date','end_date','sales','customer', 'status'], axis=1)
rev_per_product = X.groupby(['product'])['revenue'].sum().reset_index()"""

from flask import Flask, request, jsonify, Response
app = Flask(__name__)

@app.route('/rev_per_product', methods=['GET'])
def rev_per_product():
        X = dataset.drop(['start_date','end_date','sales','customer', 'status'], axis=1)
        rev_per_product = X.groupby(['product'])['revenue'].sum().reset_index()
        df = rev_per_product.to_json(orient='records')
        return Response(df, mimetype='application/json')

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8081)