## Getting Started 🚀

### Prerequisites

- [Docker](https://www.docker.com/get-started) installed on your machine.

### Build the Docker Image

To build the Docker image, run:

```bash
docker build "path-to-DockerFile" -t iris_classifier_image .
```
### Run the Docker Container

To start a container from the image and map port 8000 on your host to port 8000 in the container, use:

```bash
docker run -d -p 8000:8000 iris_classifier_image
```

### Use the API

To make predictions, send a POST request to http://0.0.0.0:8000/predict with the following JSON body:

{
    "features": [5.1, 3.5, 1.4, 0.2]
}

#### Example Request

You can test the API using curl:

```bash
curl -X POST "http://0.0.0.0:8000/predict" -H "Content-Type: application/json" -d '{"features": [5.1, 3.5, 1.4, 0.2]}'
```

## Contributing
Feel free to open issues or submit pull requests if you have any improvements or fixes. Contributions are welcome! 😊
