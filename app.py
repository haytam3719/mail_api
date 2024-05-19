from __future__ import print_function
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-key
configuration = sib_api_v3_sdk.Configuration()
configuration.api_key['api-key'] = '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'

# Create an instance of the API class
api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))

# Define the email parameters
email = sib_api_v3_sdk.SendSmtpEmail(
    to=[{"email": "serge.salah4@gmail.com", "name": "Recipient Name"}],
    sender={"email": "haytam.elmoufti@gmail.com", "name": "Attijariwafa"},
    subject="Hello from Sendinblue",
    html_content="<html><body><h1>Congratulations!</h1><p>You successfully sent this email via the Sendinblue API.</p></body></html>"
)

# Send the email
try:
    api_response = api_instance.send_transac_email(email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionalEmailsApi->send_transac_email: %s\n" % e)
