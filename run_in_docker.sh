# Source the environment variables from env_docker.sh
source env_docker.sh

# Get the current date and time in ISO 8601 format
DATE_WITH_TIME=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

# Convert the current directory path to lowercase and assign it to a variable this is a fix for "docker: invalid reference format: repository name must be lowercase."
CURRENT_DIR=$(pwd | tr '[:upper:]' '[:lower:]')

# Run the Docker command
winpty docker run --rm -it \
-v "$CURRENT_DIR/mbtest:/automation/mbtest" \
-e WC_KEY=$WC_KEY \
-e WC_SECRET=$WC_SECRET \
-e WP_HOST=$WP_HOST \
-e MACHINE=$MACHINE \
-e DB_USER=$DB_USER \
-e DB_PASSWORD=$DB_PASSWORD \
mbtest_api_python \
pytest -c /automation/mbtest/pytest.ini \
--html mbtest/reports/report_$DATE_WITH_TIME.html \
-m smoke