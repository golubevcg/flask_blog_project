docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q) 
docker-compose build flask_blog_prod
docker-compose run -d -p 80:80 flask_blog_prod