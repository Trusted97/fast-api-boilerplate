# 🐍 FastAPI Boilerplate
![CI](https://github.com/Trusted97/fast-api-boilerplate/actions/workflows/test.yml/badge.svg)
[![Python Version](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-380/)
[![FastAPI Version](https://img.shields.io/badge/FastAPI-0.103-green.svg)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Maintainability](https://api.codeclimate.com/v1/badges/6c1f5a9918d45c8cdf2b/maintainability)](https://codeclimate.com/github/Trusted97/fast-api-boilerplate/maintainability)


This is a boilerplate project to quickly start a web application using the FastAPI framework.

## Features

*   High-performance HTTP server based on FastAPI.
*   Dependency management using Poetry.
*   Docker setup for the development environment.
*   Sample FastAPI endpoint to get started.

## Requirements

*   Python 3.9 or higher.

## Getting Started

1. Clone this repository:
    
        git clone https://github.com/Trusted97/fast-api-boilerplate.git
        cd fast-api-boilerplate
    
2. Run the development server using Docker:
    
        docker-compose up --build -d
    
3. Access the FastAPI application: Open your web browser and go to [http://localhost:8000](http://localhost:8000)
4. Access the Swagger documentation at [http://localhost:8000/docs](http://localhost:8000/docs) to interact with the API.


## Project Structure

*   `router.py`: Sample FastAPI application and endpoint.
*   `pyproject.toml`: Project configuration and dependencies managed by Poetry.
*   `docker/dev/Dockerfile`: Docker configuration for the development environment.

## Contributing

Contributions are welcome! Feel free to submit issues and pull requests.

## License

This project is licensed under the MIT License.
