from flask import Flask,render_template, request
import requests
import matplotlib.pyplot as plt
import io
import base64
import pandas as pd


app = Flask(__name__)

# Load the pre-trained model and scalers
#model = SARIMAXResults.load('D:\last main\model\sarimax_model.pkl')
#scaler = joblib.load('D:\last final\model\sarimax_model.joblib')
#df = pd.read_excel('D:\last main\data\Training_Data.xlsx')


@app.route('/')
def home():
   list_pre = None
   graph = None
   return render_template('index.html')


@app.route('/model', methods=['GET','POST'])
def model():
    output=None
    graph = None
    list_pre = None
    if request.method == "POST":
      date = request.form.get('date')
      end_date = request.form.get('End date')
      print("the date senddet is :-  ",date)
      print("end date senddet is :-  ",end_date)
      # forecast = model.predict('date')
      # list_pre = forecast.to_list()


      # plt.figure(figsize=(10, 6))
      # plt.plot(df['hours'], list_pre, marker='o', color='b', label='Predicted Demand (MW)')
      # plt.title(f'Predicted Electricity Demand for New Dehli on {date} (24-Hour)')
      # plt.xlabel('Time')
      # plt.ylabel('Predicted Demand (MW)')
      # plt.xticks(rotation=45)
      # plt.grid(True)
      # plt.legend()
      # plt.tight_layout()
      # #plt.show()

      #  #gentering Gragh Actual V/S Preticted
      # img = io.BytesIO()
      # plt.savefig(img, format='png')
      # img.seek(0)
      # graph_A_P = base64.b64encode(img.getvalue()).decode()
      # plt.close()


    
    return render_template('model.html',prediction=list_pre,Graph=graph)

@app.route('/about')
def about():
   return render_template('index.html#about')

if __name__ == '__main__':
   app.run(debug=True,port=5002)