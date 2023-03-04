@echo off
[FIXME USERNAME CANNOT HAVE SPACES]

set IMAGE=groupassignment1_image
set CONTAINER=groupassignment1_container

for /f "tokens=*" %%i in ('docker images -q %IMAGE%') do set found=%%i

if [%found%] == [] (
  echo 🐳 Image not found, creating...
  docker build -t %IMAGE% .
) else (
  echo 🐳 Image found
)

docker run -it ^
    -v %cd%/main.cc:/app/main.cc ^
    --name %CONTAINER% ^
    %IMAGE%

docker rm %CONTAINER%
