# useful things to remember about this repo
## note this Should be built on an x86 box for prod and Apple Silicon for dev
git submodule update --init --recursive
git submodule update --recursive --remote

docker build --tag onkisdocker/talon-web:latest .

docker push onkisdocker/talon-web:latest



aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 461591761075.dkr.ecr.us-east-1.amazonaws.com


docker tag talon-web:latest 461591761075.dkr.ecr.us-east-1.amazonaws.com/talon-web:latest

docker push 461591761075.dkr.ecr.us-east-1.amazonaws.com/talon-web:latest

