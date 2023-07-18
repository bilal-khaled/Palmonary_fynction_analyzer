from flask import Flask, render_template, request, url_for, redirect
import joblib
import pandas as pd

app = Flask(__name__)

model_1 = joblib.load('models/model1.pkl')
model_3 = joblib.load('models/model3.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/details')
def enter_data_page():
    return render_template('details.html')

@app.route('/Report')
def report():
    return render_template('Report.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Retrieve the feature values from the form data
    fev1_value = float(request.form['fev1_pre_value'])
    fev1_pred = float(request.form['fev1_pre_percent'])
    fvc_value = float(request.form['fvc_pre_value'])
    fvc_pred = float(request.form['fvc_pre_percent'])
    fef_value = float(request.form['fef_pre_value'])
    fef_pred = float(request.form['fef_pre_percent'])

    # Create a DataFrame from the data
    df = pd.DataFrame({
        'FEV1 Value': [fev1_value],
        'FEV1 Pred': [fev1_pred],
        'FVC Value': [fvc_value],
        'FVC Pred': [fvc_pred],
        'FEF Value': [fef_value],
        'FEF Pred': [fef_pred]
    })
    print(df)

    # Perform prediction using model_1
    prediction = model_1.predict(df)

    # Map the prediction classes to their labels
    class_labels = ['Normal', 'Obstructive', 'Restrictive']
    prediction_label = class_labels[prediction[0]]
    print(prediction_label)

    # Redirect to the res-obs.html page with the prediction label as a URL parameter
    return redirect(url_for('res_obs_page', prediction_label=prediction_label))


@app.route('/res-obs' )
def res_obs_page():
        
        
        # Retrieve the prediction label from the form data
        prediction_label = request.args.get('prediction_label')
        print(prediction_label)

        # Process the data as needed
        return render_template('res-obs.html', prediction_label=prediction_label)


@app.route('/small-table')
def small_table():
    return render_template('small-table.html')


@app.route('/intro')
def intro_page():
    return render_template('intro.html')


@app.route('/obs-table')
def obs_table_page():
    return render_template('obs-table.html')


@app.route('/predict_obs', methods=['POST'])
def predict_obs():
    print(request.form)
        # Retrieve the feature values from the form data
    fev1_value = float(request.form['fev1_pre_value'])
    fev1_pred = float(request.form['fev1_pre_pecent'])
    fev1_post_value = float(request.form['fev1_post_value'])
    fev1_post_pred = float(request.form['fev1_post_percent'])
    fvc_value = float(request.form['fvc_pre_value'])
    fvc_pred = float(request.form['fvc_pre_percent'])
    fvc_post_value = float(request.form['fvc_post_value'])
    fvc_post_pred = float(request.form['fvc_post_percent'])
    fef_value = float(request.form['fef_pre_value'])
    fef_pred = float(request.form['fef_pre_percent'])
    fef_post_value = float(request.form['fef_post_value'])
    fef_post_pred = float(request.form['fef_post_percent'])

    print(fev1_value, fev1_pred, fev1_post_value, fev1_post_pred, fvc_value, fvc_pred, fvc_post_value, fvc_post_pred, fef_value, fef_pred, fef_post_value, fef_post_pred)

        # Create a DataFrame from the data
    df_1 = pd.DataFrame({
            'FEV1 Pre-BD Value': [fev1_value],
            'FEV1 Pre-BD Pred': [fev1_pred],
            'FEV1 Post-BD Value': [fev1_post_value],
            'FEV1 Post-BD Pred': [fev1_post_pred],
            'FVC Pre-BD Value': [fvc_value],
            'FVC Pre-BD Pred': [fvc_pred],
            'FVC Post-BD Value': [fvc_post_value],
            'FVC Post-BD Pred': [fvc_post_pred],
            'FEF Pre-BD Value': [fef_value],
            'FEF Pre-BD Pred': [fef_pred],
            'FEF Post-BD Value': [fef_post_value],
            'FEF Post-BD Pred': [fef_post_pred]
        })
    print(df_1)

        # Perform prediction using model_3
    prediction = model_3.predict(df_1)


        # Map the prediction classes to the labels
    prediction_obs = "Asthma" if prediction[0] == 0 else "COPD"
    print(prediction_obs)

        # Redirect to the more-detailed-obs-rev.html page with the prediction label as a URL parameter
    return redirect(url_for('more_detailed', prediction_obs=prediction_obs))

    




@app.route('/more_detailed_obs_rev')
def more_detailed():

        # Retrieve the prediction label from the form data
        prediction_obs = request.args.get('prediction_obs')
        

        # Process the data as needed
        return render_template('more_detailed_obs_rev.html', prediction_obs=prediction_obs)




@app.route('/res-info')
def res_info():
    return render_template('Res-info.html')


if __name__ == '__main__':
    app.run()
