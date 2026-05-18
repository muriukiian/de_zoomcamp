docker run -it --rm\
  --network=pg-network \
  ingest_data:v001 \
    --pg_user=admin \
    --pg_pass=root \
    --pg_host=pgdatabase \
    --pg_port=5432 \
    --pg_db=ny_taxi \
    --chunksize=100000
    --target_table=ny_taxi_2021-01 \