curl "https://api.todoist.com/rest/v2/tasks" \
    -X POST \
    --data '{"content": "Buy Milk"}' \
    -H "Content-Type: application/json" \
    -H "X-Request-Id: $(uuidgen)" \
    -H "Authorization: Bearer *****"