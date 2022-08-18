FROM laocoon667/jena-fuseki-docker:latest
USER root
RUN apk add --update --no-cache curl

LABEL maintainer="steffen.roertgen@gwdg.de"

# Fuseki config
ENV ASSEMBLER $FUSEKI_BASE/configuration/assembler.ttl
# for inferencing use assembler_inferencing.ttl
COPY assembler_inferencing.ttl $ASSEMBLER

# for inferencing
# COPY --chown=9008:root ./data/myrules.rules /fuseki-base/run/rules/myrules.rules

WORKDIR /jena-fuseki
EXPOSE 3030
USER 9008

