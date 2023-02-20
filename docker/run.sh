#!/bin/bash

IMAGE="name_me"
CONTAINER="name_me"

found=$(docker images -q $IMAGE)

# if image is not found
if [ -z "$found" ]; then
  echo "🐳 Image not found, creating..."
  docker build -t $IMAGE .
else
  echo "🐳 Image found"
fi

docker run -it \
    -v $(pwd)/app:/app
    --name $CONTAINER \
    $IMAGE

# auto delete container after it ran
docker rm $CONTAINER
