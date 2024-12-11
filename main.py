from flask import Flask,render_template
import io
import base64
import matplotlib.pyplot as plt


app = Flask(__name__)
# Load the pre-trained model and scalers
#model = SARIMAXResults.load('D:\last main\model\sarimax_model.pkl')

@app.route('/', methods =['GET','POST'])
def home():  
   return render_template('index.html')
@app.route('/model')
def model():
   
    
   #gentering Gragh Actual V/S Preticted


   img = io.BytesIO()
   plt.savefig(img, format='png')
   img.seek(0)
   graph_A_P = base64.b64encode(img.getvalue()).decode()
   plt.close()

   #

   return render_template('model.html',graph=graph_A_P)


if __name__ == '__main__':
   app.run(debug=True,port=5002)