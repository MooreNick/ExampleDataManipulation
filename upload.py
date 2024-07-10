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

tenancy = "REDACTED"       # Replace REDACTED with correct information
user = "REDACTED"          # ''
key_path = "REDACTED"      # ''
fingerprint = "REDACTED"   # ''    

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
