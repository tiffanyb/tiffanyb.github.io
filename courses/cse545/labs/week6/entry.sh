#!/bin/bash
cd /tmp
socat tcp4-listen:6666,reuseaddr,fork exec:"setarch x86_64 -R ./stack"
