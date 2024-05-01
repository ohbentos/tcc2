#!/usr/bin/env bash
sudo systemctl set-property --runtime system.slice AllowedCPUs=10-11
sudo systemctl set-property --runtime user.slice AllowedCPUs=10-11
sudo systemctl set-property --runtime machine.slice AllowedCPUs=10-11
sudo chmod 777 /sys/fs/cgroup/cgroup.procs
