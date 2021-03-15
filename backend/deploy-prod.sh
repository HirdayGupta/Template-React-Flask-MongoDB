git checkout main &&
git pull &&
source .env/bin/activate &&
python -m pip install -r requirements.txt &&
printf "killing old server processes\n" &&
./kill_old_server_processes-prod.sh &&
sudo ./.env/bin/gunicorn \
    --bind 0.0.0.0:80 \
    --workers=5 \
    --threads=2 \
    wsgi \
    --daemon &&
printf "deploy successful!\n"