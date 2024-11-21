# wait-for-postgres.sh
#!/bin/bash
# Chờ PostgreSQL sẵn sàng
while ! nc -z postgres 5432; do
  echo "Waiting for PostgreSQL to start..."
  sleep 2
done
echo "PostgreSQL is up and running!"