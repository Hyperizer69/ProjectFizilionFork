FROM ghcr.io/qubitdimensions/fizilion:dev
RUN mkdir /Fizilion && chmod 777 /Fizilion && git clone https://github.com/Hyperizer69/ProjectFizilionFork -b pruh /Fizilion
WORKDIR /Fizilion
CMD ["python3","-m","userbot"]
