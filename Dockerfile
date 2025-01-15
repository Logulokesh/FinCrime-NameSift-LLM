FROM postgres:latest

RUN apt-get update && \
    apt-get install -y build-essential git postgresql-server-dev-all && \
    git clone https://github.com/pgvector/pgvector.git && \
    cd pgvector && \
    make && \
    make install && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /pgvector