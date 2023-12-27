docker stop $(docker ps -q)
docker rm $(docker ps -a -q)
docker-compose build flask_blog_prod
docker-compose run -d -p 80:80 -p 443:443 flask_blog_prod