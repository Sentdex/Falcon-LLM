# Falcon-LLM
Helper scripts and examples for exploring the Falcon LLM models

Files:
- `api_server.py` - Run locally or in cloud. Should fully set up a proper web server if you intend to host on a public IP, this is using the basic flask demo web server. 
- `api_client.py` - Make requests to the server. Makes R&D a lot easier if you can load and access the model separately, even if everything is on the same machine, so you're not re-loading the model every single time you make a change to your script. You can also use a notebook, but, depending on the complexity of your project, this might not be good enough.
- `Falcon-40B-demo.ipynb` - a short notebook example of loading Falcon 40B with options for various datatypes (4, 8, and 16bit).
- `setup.sh` - a quick shell script for setup of requirements that I used for Lambda H100 machines. (`chmod +x setup.sh` & `./setup.sh`
