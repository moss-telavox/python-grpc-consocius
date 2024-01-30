# Simple gRPC client to talk to consocius

A small Python client that talks with the Conscius gRPC server. 

_Does not include all needed libraries, you generate them yourself_ 

## Set it up

1. start the virtual env

```
source bin/activate
```

2. Install the gRPC protoc 
```
pip install -r requirements

or 

pip install grpcio-tools
```

3. Generate libraries from Conscious .proto 
```
git clone git@github.com:Telavox/consocius.git /tmp/consocius

python -m grpc_tools.protoc -I/tmp/consocius/protocol/src/main/proto/ --python_out=./ --grpc_python_out=./ /tmp/consocius/protocol/src/main/proto/*         
```

You should now have a bunch of \*pb2.py files

4. Run the client

```
python client.py
```

