# TODO add skos2jskos conversion

concepts=($(find ./data_loader/data -type f -name '*.ndjson'))
schemes=($(find ./data_loader/data -type f -name '*.json'))

for c in ${schemes[@]} ; do
  echo "Found scheme: $c"
  docker-compose exec jskos-server /usr/src/app/bin/import.js -- schemes ${c:1}
done

for c in ${concepts[@]} ; do
  echo "Found concept $c"
  docker-compose exec jskos-server /usr/src/app/bin/import.js -- concepts ${c:1}
done

docker-compose exec jskos-server /usr/src/app/bin/import.js --indexes
