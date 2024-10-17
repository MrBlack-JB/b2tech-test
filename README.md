# b2tech-test
Hello.
Input data:
1. Create a simple web application with the following components:
a. Backend - could be created using any high level language of your choice - Level 3
b. Proxy / Load balancer - a simple router to serve requests to the backend service, you may choose any solution to create it such as Nginx, Apache2, etc - Level 6

2. The backend service should return a simple page with "Hello world!" in it upon receiving requests on the root page - Level 3

3. Deploy partial Elastic (Elasticsearch Platform - Find real-time answers at scale) stack deployment with:

a. Elasticsearch (Database) - Level 4
b. Kibana (Dashboard) - Level 4

4. The Proxy / Load balancer will redirect the traffic by the following - Level 4

a. http://yourdomain/ -> point to your application (backend)
b. http://yourdomain/kibana/ -> point to the Kibana service

5. Send the application (backend) logs to Elasticsearch in a way of your choice - Level 6

6. Discover the logs with Kibana - Level 2

Tips:
You can send logs with code or with 3rd party application.
You can use any infrastructure to your solution (docker-compose, kubernetes)

My set of services:
1. My application - I chose Python+Flask. The application will write logs directly to elasticsearch since I am limited in time, but it would be good to use a log collector. I wrote it myself, but to save time I honestly looked at a couple of constructions on stackoverflow. But I will gladly tell you how it works and why I did it this way and not otherwise.
2. Docker - of course.
	a. I tried to make things more difficult for myself and make containers a little more secure and not run services in them as root.
	b. requirements.txt - Well, this is the default for python. It is easier to manage dependencies and docker does not check dependencies every time if the file has not changed.
2. Docker-compose - You may not have Kubernetes at hand, but almost everyone has Docker. Alternative - Minikube will require installation + there is a risk of making a mistake during installation/configuration.
	a. P.S. I know that all services by default are included in the default docker network, but I decided to play it safe and explicitly specified the network for the services + this will separate them from your default docker network.
3. Nginx - my personal opinion - simpler and better than Apache.
	a. The nginx.conf file contains proxy settings for / and /kibana. And it is delivered to the container by a dockerfile.
	b. Nginx is also not launched from under root and therefore port 8080 is used and the dockerfile has rights to directories for creating a pid file, etc.
	c. There could have been fewer lines in the config, but this is the minimum configuration with which everything worked for me without problems. I haven't touched nginx for a long time, but my hands remember))
4. Elasticsearch
5. Kibana
