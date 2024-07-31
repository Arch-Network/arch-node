#!/bin/bash
set -e

chown -R bitcoin:bitcoin /data

if [ ! -s "$BITCOIN_DATA/bitcoin.conf" ]; then
	runuser -u bitcoin cat <<-EOF > "$BITCOIN_DATA/bitcoin.conf"
	printtoconsole=1
	rpcallowip=0.0.0.0/0
	regtest=1
	rpcauth=bitcoin:0358034332d92b5db82e6f94423745c8\$da1717f0b1a953c6404d94633dd3995c75391acd5a22777d0a62ad3f6886e7b9
	maxmempool=100
	dbcache=150
	fallbackfee=0.001
	maxtxfee=0.002
	txindex=1
	[regtest]
	rpcbind=0.0.0.0
	rpcport=18443
	wallet=devwallet
	EOF
fi

runuser -u bitcoin bitcoin-mine & 
exec runuser -u bitcoin "$@"
