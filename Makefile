build_proto:
	rm prot_pb2.py
	rm prot_pb2_grpc.py
	python3 -m grpc_tools.protoc -I ./protos --python_out=. --grpc_python_out=. ./protos/prot.proto

start_server: build_proto
	pip install pydub
	python3 main.py --start

