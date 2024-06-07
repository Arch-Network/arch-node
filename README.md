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
### Hardware Requirements for Running a Full Bitcoin Node

For validators in the Arch network, operating a full Bitcoin Node is essential. The Arch Node uses the Bitcoin Node to read from the Bitcoin blockchain, enabling the Arch network as an execution layer. Additionally, a coordinator chosen from Arch Node validators will write transactions to the Bitcoin blockchain. Running a full Bitcoin Node thus enables direct interaction with Bitcoin’s network, ensuring validators can effectively perform their roles within the Arch ecosystem.

- **Operating System**: Compatible with recent versions of Windows, Mac OS X, or Linux. Ensure the operating system is kept up to date for security and compatibility.

- **Memory (RAM)**: A minimum of 2 gigabytes of RAM is necessary. For optimal performance, 4 gigabytes or more is recommended.

- **Disk Space**: At least 350 gigabytes of free disk space on an SSD is recommended. The SSD improves read/write speeds essential during the IBD and normal operations as the blockchain size continuously grows.

- **Bandwidth**: A broadband Internet connection with at least 400 kilobits per second (50 kilobytes per second) upload speed. Full nodes often exceed 200 gigabytes of uploaded data per month and download about 20 gigabytes, with an additional 340 gigabytes on the initial setup.

- **Power Supply**: Continuous operation (24/7) is ideal for network support, but the node should be operational for at least 6 hours daily. Prevent the system from entering low-power modes like sleep or hibernate to maintain consistent network support.

For the most up-to-date information on running a full Bitcoin Node, please visit [Bitcoin.org](https://bitcoin.org/en/full-node).

Meeting these hardware requirements ensures that your full Bitcoin Node runs efficiently and contributes reliably to the network's health and decentralization.
