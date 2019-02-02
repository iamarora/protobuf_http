all: clean proto run 

clean:
	rm -rf *.pyc *.class
proto:
	protoc -I=. --python_out=. person.proto
run:
	./server.py
