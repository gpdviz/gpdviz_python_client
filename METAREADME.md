## How was this generated

This was generated from the command line using
[swagger-codegen](https://github.com/swagger-api/swagger-codegen).

    mkdir gpdviz_python_client
    cd    gpdviz_python_client
    
With the Gpdviz server running on `http://localhost:5050`:

    swagger-codegen generate -i http://localhost:5050/api-docs/swagger.json -l python --git-repo-id gpdviz_python_client --git-user-id gpdviz
    
