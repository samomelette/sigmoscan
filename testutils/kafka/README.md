# Kafka test utils

```
.
├── consumer
│   ├── config.ini
│   ├── main.py
│   └── src
├── README.md
├── scripts
│   └── kafkacontainer
├── install.sh
└── uninstall.sh
```

- `consumer`: Example Python script to consume traffic data collected by SigmoScan from a Kafka topic
- `scripts`: Set of command line utils to spawn and manage a local Kafka container, which can be added to the local path by running `./install.sh`
