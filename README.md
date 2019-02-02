Python/Jython Simple HTTP Server to write to Google protobuf with file roll over
------

- Run command :: `make` - This will clean and start the server on port 1111
- To Test :: curl --header "Content-Type: application/json" --request POST --data '{"name":"Ankit","id":1}' http://localhost:1111 

Notes ::
- File Roll Over time is 10 seconds. Can be changed in the script. A file will be written in root directory every minute.
- protoc command line program needs to be installed - https://github.com/protocolbuffers/protobuf/releases/tag/v3.6.1
- pip install requirements.txt preferably to a virtualenv. 
