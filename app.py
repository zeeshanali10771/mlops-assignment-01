from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load('model.pkl')


@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        #Furniture_id,Amount,Quantity,weight,Length,Wood,Width,Cutting,Extra,Finishing,Can

        Furniture_id = float(request.form['Furniture_id'])
        Amount = float(request.form['Amount'])
        Quantity = float(request.form['Quantity'])
        weight = float(request.form['weight'])
        Length = float(request.form['Length'])
        Wood = float(request.form['Wood'])
        Width = float(request.form['Width'])
        Cutting = float(request.form['Cutting'])
        Extra = float(request.form['Extra'])
        Finishing = float(request.form['Finishing'])
        Can = float(request.form['Can'])

        prediction = model.predict([[
            Furniture_id, Amount, Quantity, weight,
            Length, Wood, Width, Cutting,
            Extra, Finishing, Can
        ]])

        return render_template('result.html', prediction=prediction[0])

    return render_template('predict.html')


if __name__ == '__main__':
    app.run(port=8081, host="0.0.0.0")