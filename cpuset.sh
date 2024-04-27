#!/usr/bin/env bash
sudo systemctl set-property --runtime system.slice AllowedCPUs=8-11
sudo systemctl set-property --runtime user.slice AllowedCPUs=8-11
sudo systemctl set-property --runtime machine.slice AllowedCPUs=8-11
