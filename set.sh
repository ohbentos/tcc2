systemctl set-property --runtime system.slice AllowedCPUs=10,11
systemctl set-property --runtime docker.slice AllowedCPUs=0
