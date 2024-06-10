# Arch Node

Welcome Arch Node Validators! This repository is your go-to resource for downloading, setting up, and running an Arch validator node on the Arch network. Here you will find binaries for multiple platforms and detailed instructions on how to configure and run your node.

## Supported Platforms

We provide pre-compiled binaries for the following platforms:

- aarch64-apple-darwin (MacOS ARM64)
- aarch64-unknown-linux-gnu (Linux ARM64)
- x86_64-apple-darwin (MacOS x86_64)
- x86_64-unknown-linux-gnu (Linux x86_64)

## Installation

1. **Download the Binary**: Navigate to the Releases section and download the binary suitable for your platform.
   URL: https://github.com/Arch-Network/arch-node/releases

2. **Set Executable Permission**: After downloading, change the permissions to make the binary executable:
   ```bash
   chmod +x path/to/arch-node
   ```

## Usage

To start your node, you can simply run the binary with the following command:
```bash
./path/to/arch-node --leader-endpoint "http://leader.example.com" --data-dir "/custom/arch_data" --prover-endpoint "http://custom.prover:8001" --network-mode TESTNET --bitcoin-rpc-endpoint "192.168.1.100" --bitcoin-rpc-port 18332 --bitcoin-rpc-username "user" --bitcoin-rpc-password "pass" --bitcoin-rpc-wallet "mywallet"
```

### Configuring Your Node

You can customize the behavior of your Arch node using the following command-line arguments:

- ```--leader-endpoint```: Specify the leader endpoint URL (default: None).
- ```--data-dir```: Path to the data directory (default: ./arch_data).
- ```--prover-endpoint```: URL of the prover endpoint (default: http://127.0.0.1:8001).
- ```--network-mode```: Network mode (options: MAINNET, TESTNET, DEVNET; default: DEVNET).

#### Bitcoin Integration

- ```--bitcoin-rpc-endpoint```: Bitcoin RPC server IP address (default: 127.0.0.1).
- ```--bitcoin-rpc-port```: Port of the Bitcoin RPC server (default: 8332).
- ```--bitcoin-rpc-username```: Username for Bitcoin RPC authentication.
- ```--bitcoin-rpc-password```: Password for Bitcoin RPC authentication.
- ```--bitcoin-rpc-wallet```: Bitcoin wallet name (default: testwallet).

#### RPC Server Configuration

- ```--rpc-bind-ip```: IP address to bind the RPC server (default: 127.0.0.1).
- ```--rpc-bind-port```: Port to bind the RPC server (default: 9001).

## Hardware Requirements

### Combined Hardware Requirements for Running Both a Bitcoin Full Node and an Arch Node

For users intending to operate both a Bitcoin Full Node and an Arch Node on the same machine, the following specifications are recommended to handle the demands of both nodes efficiently:

- **Operating System**: Linux or MacOS. These systems are compatible with the software used by both nodes.

- **Processor (CPU)**: A high-end multi-core processor is essential to manage the intense computational load from both nodes, especially for tasks like verifying ZKVM proofs.

- **Memory (RAM)**: At least 32 GB of RAM is recommended.

- **Disk Space**: A combined total of at least 2 TB of SSD storage is necessary. This space will accommodate the full Bitcoin blockchain and the additional data from the Arch Node.

- **Bandwidth**: Internet connection with at least 3 megabytes per second upload and download speed is advisable. This increased bandwidth supports the data transmission requirements of both nodes, especially important when the network traffic is high.

By adhering to these enhanced specifications, users can ensure that both their Bitcoin and Arch Nodes operate effectively, contributing to the stability and security of both networks.

### Hardware Requirements for Running an Arch Node

To ensure optimal performance of an Arch Node the following hardware specifications are recommended:

- **Operating System**: Linux or MacOS.

- **Processor (CPU)**: A modern multi-core processor is recommended to handle the computational demands of verifying ZKVM proofs.

- **Memory (RAM)**: At least 16 GB of RAM is recommended to ensure smooth operation.

- **Disk Space**: A minimum of 1 TB of SSD storage is required to manage the blockchain data and logs. This allows for adequate storage of historical data and ensures quick data retrieval and processing.

- **Bandwidth**: A stable internet connection with a minimum of 2 megabytes per second upload and download speed is necessary to handle network communications and data transmission reliably.

### Hardware Requirements for Running a Full Bitcoin Node
For the most up-to-date information on running a full Bitcoin Node, please visit [Bitcoin.org](https://bitcoin.org/en/full-node).
