curl -k -H 'User-Agent: api-test-agent' "https://api.hh.ru/vacancies?text=${1// /+}" | jq '.' > hh.json
