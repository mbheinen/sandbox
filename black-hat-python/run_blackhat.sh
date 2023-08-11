docker build -t mbheinen/blackhat .
docker run --rm -it -v network:$(HOME)/network mbheinen/blackhat bash
