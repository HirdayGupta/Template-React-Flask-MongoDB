pids=$(sudo lsof -t -i:80)
for pid in $pids
do
  printf "killing $pid\n"
  sudo kill -9 "$pid" > /dev/null 2> /dev/null || :
done
