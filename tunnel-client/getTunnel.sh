SOURCE=${BASH_SOURCE[0]}
cd $(dirname $SOURCE)/tunnel
options="-F ./ssh_config"
name="myTestService"
host=Tunnel
if [ $# != 1 ] ; then
    echo "$0 <port>"
    exit -1
fi
port=$1
common="$options $host"
ssh -Oexit $common
ssh $common && \
    ssh $common register -n "${name}" -p $(ssh -Oforward -fCNR 0:localhost:$port $common)
