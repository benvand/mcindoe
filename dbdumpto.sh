
fn=mcindoe.sql.$(date +%d-%m-%y-%H-%M-%S)
touch $fn && pg_dump -U mcindoe mcindoe > $fn && scp $fn $1:

