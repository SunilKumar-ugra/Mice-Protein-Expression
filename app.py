from flask import Flask, render_template, request
import os 
import numpy as np
import pandas as pd
from mice.pipeline.prediction import PredictionPipeline


app = Flask(__name__) # initializing a flask app

@app.route('/',methods=['GET'])  # route to display the home page
def homePage():
    return render_template("index.html")
    
@app.route('/train',methods=['GET'])  # route to train the pipeline
def training():
    os.system("python main.py")
    return "Training Successful!" 
 										

@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            DYRK1A_N =float(request.form['DYRK1A_N'])
            #ITSN1_N =float(request.form['ITSN1_N'])
            BDNF_N =float(request.form['BDNF_N'])
            NR1_N =float(request.form['NR1_N'])
            NR2A_N =float(request.form['NR2A_N'])
            pAKT_N =float(request.form['pAKT_N'])
            pBRAF_N =float(request.form['pBRAF_N'])
            pCAMKII_N =float(request.form['pCAMKII_N'])
            pCREB_N =float(request.form['pCREB_N'])
            pELK_N =float(request.form['pELK_N'])
            #pERK_N =float(request.form['pERK_N'])
            pJNK_N =float(request.form['pJNK_N'])
            PKCA_N =float(request.form['PKCA_N'])
            pMEK_N =float(request.form['pMEK_N'])
            #pNR1_N =float(request.form['pNR1_N'])
            pNR2A_N =float(request.form['pNR2A_N'])
            #pNR2B_N =float(request.form['pNR2B_N'])
            pPKCAB_N =float(request.form['pPKCAB_N'])
            pRSK_N =float(request.form['pRSK_N'])
            AKT_N =float(request.form['AKT_N'])
            #BRAF_N =float(request.form['BRAF_N'])
            CAMKII_N =float(request.form['CAMKII_N'])
            CREB_N =float(request.form['CREB_N'])
            ELK_N =float(request.form['ELK_N'])
            ERK_N =float(request.form['ERK_N'])
            GSK3B_N =float(request.form['GSK3B_N'])
            JNK_N =float(request.form['JNK_N'])
            MEK_N =float(request.form['MEK_N'])
            TRKA_N =float(request.form['TRKA_N'])
            RSK_N =float(request.form['RSK_N'])
            APP_N =float(request.form['APP_N'])
            #Bcatenin_N =float(request.form['Bcatenin_N'])
            SOD1_N =float(request.form['SOD1_N'])
            MTOR_N =float(request.form['MTOR_N'])
            P38_N =float(request.form['P38_N'])
            pMTOR_N =float(request.form['pMTOR_N'])
            DSCR1_N =float(request.form['DSCR1_N'])
            AMPKA_N =float(request.form['AMPKA_N'])
            NR2B_N =float(request.form['NR2B_N'])
            pNUMB_N =float(request.form['pNUMB_N'])
            RAPTOR_N =float(request.form['RAPTOR_N'])
            TIAM1_N =float(request.form['TIAM1_N'])
            pP70S6_N =float(request.form['pP70S6_N'])
            NUMB_N =float(request.form['NUMB_N'])
            P70S6_N =float(request.form['P70S6_N'])
            pGSK3B_N =float(request.form['pGSK3B_N'])
            pPKCG_N =float(request.form['pPKCG_N'])
            CDK5_N =float(request.form['CDK5_N'])
            S6_N =float(request.form['S6_N'])
            ADARB1_N =float(request.form['ADARB1_N'])
            AcetylH3K9_N =float(request.form['AcetylH3K9_N'])
            RRP1_N =float(request.form['RRP1_N'])
            BAX_N =float(request.form['BAX_N'])
            ARC_N =float(request.form['ARC_N'])
            ERBB4_N =float(request.form['ERBB4_N'])
            ERBB4_N =float(request.form['ERBB4_N'])
            nNOS_N =float(request.form['nNOS_N'])
            Tau_N =float(request.form['Tau_N'])
            GFAP_N =float(request.form['GFAP_N'])
            GluR3_N =float(request.form['GluR3_N'])
            GluR4_N =float(request.form['GluR4_N'])								
            IL1B_N =float(request.form['IL1B_N'])
            P3525_N =float(request.form['P3525_N'])
            pCASP9_N =float(request.form['pCASP9_N'])
            PSD95_N =float(request.form['PSD95_N'])
            SNCA_N =float(request.form['SNCA_N'])
            Ubiquitin_N =float(request.form['Ubiquitin_N'])
            pGSK3B_Tyr216_N =float(request.form['pGSK3B_Tyr216_N'])
            SHH_N =float(request.form['SHH_N'])
            BAD_N =float(request.form['BAD_N'])
            BCL2_N =float(request.form['BCL2_N'])
            #pS6_N =float(request.form['pS6_N'])
            pCFOS_N =float(request.form['pCFOS_N'])
            SYP_N =float(request.form['SYP_N'])
            H3AcK18_N =float(request.form['H3AcK18_N'])
            EGR1_N =float(request.form['EGR1_N'])
            H3MeK4_N =float(request.form['H3MeK4_N'])
            CaNA_N =float(request.form['CaNA_N'])

       
         
            data = [DYRK1A_N,BDNF_N,NR1_N,NR2A_N,pAKT_N,pBRAF_N,pCAMKII_N,
                    pCREB_N,pELK_N,pJNK_N,PKCA_N,pMEK_N,pNR2A_N,pPKCAB_N,pRSK_N,
                    AKT_N,CAMKII_N,CREB_N,ELK_N,ERK_N,GSK3B_N,JNK_N,MEK_N,TRKA_N,
                    RSK_N,APP_N,SOD1_N,MTOR_N,P38_N,pMTOR_N,DSCR1_N,AMPKA_N,NR2B_N,
                    pNUMB_N,RAPTOR_N,TIAM1_N,pP70S6_N,NUMB_N,P70S6_N,pGSK3B_N,pPKCG_N,
                    CDK5_N,S6_N,ADARB1_N,AcetylH3K9_N,RRP1_N,BAX_N,ARC_N,ERBB4_N,nNOS_N,
                    Tau_N,GFAP_N,GluR3_N,GluR4_N,IL1B_N,P3525_N,pCASP9_N,PSD95_N,SNCA_N,
                    Ubiquitin_N,pGSK3B_Tyr216_N,SHH_N,BAD_N,BCL2_N,pCFOS_N,SYP_N,H3AcK18_N,
                    EGR1_N,H3MeK4_N,CaNA_N]
            data = np.array(data).reshape(1, 70)
            
            obj = PredictionPipeline()
            predict = obj.predict(data)

            return render_template('result.html', prediction = str(predict))

        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'

    else:
        return render_template('index.html')


if __name__ == "__main__":
	# app.run(host="0.0.0.0", port = 8080, debug=True)
	# app.run(host="0.0.0.0", port = 8080) #for AWS /Local host
    app.run(host="0.0.0.0", port = 80) # Asure 