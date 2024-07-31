########################################################################
FROM debian:bookworm-slim AS builder

RUN set -ex \
	&& apt-get update \
	&& apt-get install -qq --no-install-recommends ca-certificates wget

ENV BITCOIN_VERSION=27.1
ENV BITCOIN_URL=https://bitcoincore.org/bin/bitcoin-core-$BITCOIN_VERSION/bitcoin-$BITCOIN_VERSION-x86_64-linux-gnu.tar.gz \
	BITCOIN_SHA256=c9840607d230d65f6938b81deaec0b98fe9cb14c3a41a5b13b2c05d044a48422

RUN set -ex \
	&& cd /tmp \
	&& wget -qO bitcoin.tar.gz "$BITCOIN_URL" \
	&& echo "$BITCOIN_SHA256 bitcoin.tar.gz" | sha256sum -c - \
	&& tar -xzvf bitcoin.tar.gz -C /usr/local --strip-components=1 --exclude=*-qt
########################################################################
FROM debian:bookworm-slim
RUN set -ex \
	&& apt-get update \
	&& apt-get install -qq --no-install-recommends jq

COPY --from=builder /usr/local/bin/bitcoind /usr/local/bin/bitcoin-cli /usr/local/bin/
RUN groupadd -r bitcoin && useradd -r -m -g bitcoin bitcoin \
	&& ln -s /usr/local/bin/bitcoin-cli /usr/local/bin/c

ENV BITCOIN_DATA=/data

# create data directory
RUN mkdir "$BITCOIN_DATA" \
	&& chown -R bitcoin:bitcoin "$BITCOIN_DATA" \
	&& ln -sfn "$BITCOIN_DATA" /home/bitcoin/.bitcoin \
	&& chown -h bitcoin:bitcoin /home/bitcoin/.bitcoin

VOLUME /data

COPY entrypoint.sh /entrypoint.sh
COPY bitcoin-mine /usr/local/bin/bitcoin-mine

EXPOSE 18443

ENTRYPOINT ["/entrypoint.sh"]
CMD ["bitcoind"]
########################################################################
