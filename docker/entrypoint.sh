#!/bin/bash

NAME=hunyuan

USER_ID=${SANDBOX_UID:-10002}
GROUP_ID=${SANDBOX_GID:-10002}

echo "Starting with UID: $USER_ID, GID: $GROUP_ID"

useradd -u $USER_ID -o -m $NAME
groupmod -g $GROUP_ID $NAME
chown -R $NAME:$NAME /app

python3 -m kernel.launcher
