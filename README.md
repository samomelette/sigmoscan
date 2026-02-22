# Network Scanner

This tool can be used to monitor an interface, collect network packets, generate a PCAP file every `ROTATE_EVERY_T_SEC` seconds, and forward the PCAP to an Apache Kafka broker.

## Requirements

- Docker 
- Docker compose

## Configuration

The network scanner can be configured using the `config.ini` file.
Important parameters are:

<ul>
    <li>`DEFAULT_INTERFACE`: The interface to be monitored.</li>
    <li>`DEFAULT_SERVER_IP`: The Kafka server.</li>
</ul>

## Deployment

The network scanner can be deployed by building the `Dockerfile` in the root directory.

```
docker build . -t network-scanner:latest & docker run -it --rm network-scanner:latest --cap-add=NET_ADMIN --cap-add=NET_RAW 
```


## Testing

The network scanner can be tested by running

```
./test.sh
```

