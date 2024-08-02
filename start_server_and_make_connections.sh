python3 server.py &

SERVER_PID=$!

sleep 3

CLIENT_PIDS=()
for i in {1..5}
do
    python3 client.py &
    CLIENT_PIDS+=($!)
done

sleep 30

for PID in "${CLIENT_PIDS[@]}"
do
    kill $PID
done

sleep 10
kill $SERVER_PID

