# sudo cset set -d docker
# sudo cset shield --userset=docker_executor --cpu 0,1  -k on

/bin/cat <<EOF > /etc/docker/daemon.json
{
    "cgroup-parent": "/docker_executor"
}
EOF

service docker restart

# makes all programs use cgroup /system and docker use /docker_executor
