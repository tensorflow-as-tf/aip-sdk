#!/bin/bash

# download protos from Maven Central
curl -L https://search.maven.org/remotecontent?filepath=com/palantir/aip/processors/api/aip-processor-api/0.0.2/aip-processor-api-0.0.2.tar --output aip-processor-api-0.0.2.tar
tar -xvf aip-processor-api-0.0.2.tar
mv processing-service-v2.proto proto/
mv configuration-service.proto proto/

# compile protos
python3 -m grpc_tools.protoc -Iproto --python_out proto --mypy_out proto --grpc_python_out proto proto/*.proto
python3 -m lib2to3 -wn proto --output-dir proto

