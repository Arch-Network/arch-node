# Docker

This folder contains docker images than can be used as starting point for running your arch-network node.

## Requirements:
- [Docker](https://www.docker.com/)

## Running arch-node

- Clone this git repository and `cd` into the `docker` folder. You'll find a `compose.yaml` file.
- The compose file is pre-configured, so everything should work well as-is. Feel free to update any configuration parameter.
- To start `arch-node`, run `docker compose pull` followed by `docker compose up`.

---

# Troubleshooting
#### Common errors and their solution.

___
### Error: Could not find node matching this node's pubkey on the boot node's node list

This error is caused because your node has not been identified by the network boot node. You must provide your node public RPC endpoint (IP, port) to the boot node administrator. After the administrator confirms that your node endpoint has been added to the node list, restart `arch-node`.
___
