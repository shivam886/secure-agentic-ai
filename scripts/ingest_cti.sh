#!/usr/bin/env bash
# Clone or update the MITRE CTI STIX repo
if [ -d "cti/enterprise-attack/.git" ]; then
  cd cti/enterprise-attack && git pull && cd ../../
else
  git clone https://github.com/mitre/cti.git cti/enterprise-attack
fi
