import os
import pandas as pd
from gensim.models import KeyedVectors
from flask import Flask, jsonify
app = Flask('app')

if not os.path.isfile("/content/download.php?file=embeddings%2Fword2vec%2Fcbow_s300.zip"):
  os.system('wget http://143.107.183.175:22980/download.php?file=embeddings/word2vec/cbow_s300.zip')
  os.system('unzip /content/download.php?file=embeddings%2Fword2vec%2Fcbow_s300.zip')
else:
  print("this file already was downloaded")

file_path = '/content/cbow_s300.txt'

if not 'word2vec_300_model' in locals() or not 'word2vec_300_model' in globals():
  word2vec_300_model = KeyedVectors.load_word2vec_format(file_path)

@app.route('/food/<name>', methods = ['GET'])
def get_product(name):

  return jsonify(word2vec_300_model.most_similar(name))

app.run(host='0.0.0.0', port=8080)
