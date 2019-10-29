
echo "...starting printing server"
cd printer && yarn install
echo "..leaving folder"
cd ..
node ./printer/server.js
echo "Good Luck:-) Big Data"
