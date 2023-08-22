# Use the official PostgreSQL image as the base image
FROM postgres:15

# Set environment variables for the database
ENV POSTGRES_DB=flight_data
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=postgres

EXPOSE 5432
# Optionally, you can load initialization scripts
COPY init-scripts/ /docker-entrypoint-initdb.d/