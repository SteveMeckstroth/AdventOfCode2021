# Advent of Code 2021

Track my progress through the Advent of Code 2021 calendar of challenges at: https://adventofcode.com/2021

## You can run my python code samples as well after cloning this repo

It is easiest to build a Docker image after cloning this repository using the included Dockerfile
```bash
Docker build -t adventofcode2021:latest .
```

Then run the container interactively
```bash
Docker run -it adventofcode2021:latest bash
```

Run my test cases
```bash
pytest tests
```

Run the individual daily modules
```bash
python -m Day01.Day01
```
