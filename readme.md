#useful things to remember about this repo

git submodule update --init --recursive
git submodule update --recursive --remote

docker build --tag onkisdocker/talon-web:latest .

docker push onkisdocker/talon-web:latest