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
from flask import Flask
import os
import requests

app = Flask(__name__)


@app.route('/')
def get_main ():
    msg = ()
    msg = msg + get_register()
    msg = msg + get_login()
    msg = msg + get_loan()
    return msg

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)