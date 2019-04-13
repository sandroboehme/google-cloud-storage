# firestore-http
This is an example for using the Google Cloud Storage
See the [Google Docu](https://cloud.google.com/storage/docs/reference/libraries) for further information.

## Requirements
* Python 3
* The JSON file for the service account. The [Docu](https://cloud.google.com/storage/docs/reference/libraries#setting_up_authentication) describes how to create it. Add it as `auth.json` to the root of this repo. It is already added to `.gitignore`

## Installation
```
virtualenv --python python3 env
source env/bin/activate
pip3 install -r requirements.txt
```

## Run
``` 
./test.sh
```

## Exit virtualenv
``` 
deactivate
```
