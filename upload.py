import pandas as pd
import oci

# I am going to demonstrate working with Oracle's Cloud Service, more specifically,
# Object Storage. I will be uploading a sample piece of data from the data that we
# previously created and manipulated. Initially, I attempted to upload the entire dataset
# however, it is too large, presumably due to me using the free tier.

# Firstly, we must build our configuration settings. This can be done in an alternative way by
# using a config file, however, I prefer the more explicit dictionary method.

# Side note: if you are interested in working with Oracle yourself, if you navigate to the API Key
# Generation page and create a new key, the subsequent popup will provide you with most of this information
# below. I personally found this much easier than digging through the website for the information.

tenancy = "ocid1.tenancy.oc1..aaaaaaaagyhod5jyjj4y4xnbngb7cm7wvq7n4lalq5wi3i5g3xz5w5it7kdq" # Replace REDACTED with correct information
user = "ocid1.user.oc1..aaaaaaaaillyid4hota7d3n3btduul74ksyr7afnwsi36f6gydo7z5vbmhoa"       # ''
key_path = "C:/Users/Nick/.oci/philadelphia_nick@yahoo.com_2024-07-10T01_12_55.765Z.pem"    # ''
fingerprint = "ac:20:f6:b9:e0:fc:b0:8c:86:e7:44:e7:a1:63:74:02"                             # ''    

# Build the dictionary
config = {
    "user": user,
    "key_file": key_path,
    "fingerprint": fingerprint,
    "tenancy": tenancy,
    "region": "us-ashburn-1"
}

# Validate the configuration
validate_config = oci.config.validate_config(config)
# Create our client
client = oci.object_storage.ObjectStorageClient(config)

# Read in the data we want to send
data = pd.read_csv("fixedData.csv")

# Get a smaller sample
sampleData = data.head(1000)

# Send it to the Cloud!
client.put_object("idijgx3cir5f", "data", "SampleData.csv", sampleData.to_csv(index=False))