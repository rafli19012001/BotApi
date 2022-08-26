import os
import requests
from flask import Flask
from datetime import datetime, timedelta
from requests.auth import HTTPBasicAuth
from CeriaRegister import get_register
from CeriaLogin import get_login
from CeriaApplyLoan import get_loan 
from CeriaCreditActivation import get_activation
from CeriaProfile import get_profile
from CeriaProfileChangePin import get_changepin
from CeriaProfileForgotPin import get_forgotpin
from CeriaBill import get_bill
from CeriaInstallment import get_installment
from CeriaMerchantPayment import get_merchant
from CeriaCashout import get_cashout

app = Flask(__name__)


@app.route('/responsecode')
def get_main ():
   register = get_register()
   login = get_login()  
   loan = get_loan()
   credit = get_activation()
   profile = get_profile()
   changepin = get_changepin()
   forgotpin = get_forgotpin()
   bill = get_bill()
   installment = get_installment()
   merchant = get_merchant()
   cashout = get_cashout()
   msg = register + '\n' + login + '\n' + loan + '\n' + credit + '\n' + profile + '\n' + changepin + '\n' + forgotpin + '\n' + bill + '\n' + installment + '\n' + merchant + '\n' + cashout
   return msg

  


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)