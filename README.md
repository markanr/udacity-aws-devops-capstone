# udacity-aws-devops-capstone
Hello!

my name is Marko and this is my capstone project for the Udacity AWS DevOps Engineer nanodeegre! 

In this project we applied the all the skills that we learned during the course, which includes:

- Working in aws
- Implement CI/CD with an CI/CD Tool, in this project I used Circle CI to develop my builds
- Build an pipeline to deploy a flask app
- Build docker container images and Kubernetes clusters, afterwards deploy them to a EC instance
- Deploy and infrastructure, including VPC, LoadBalancers, Private and Public subnets and EC2 instances for app hosting

For the deployment type, I chose rolling deployment, the create-deployment job with given instructions in deployment.yml as resource

As CI/CD Tool I used Circle CI, as it's easy to implement and use in a repository with plenty of options, and it has a clear user interface.

For infrastructure and cluster creation, image update, the aws eks orb was used. Such community supported libraries as aws eks are often maintained to keep up with the possibilities of cloudformation, making it a good deployment option for a stable infrastructure

The pipeline consists 7 jobs,

- ``` lint-app ``` - to lint the docker file
- ``` build-push-container ``` - builds and pushes a docker container with the flask app to dockerhub
- ``` aws-eks/create-cluster ``` - creates the Amazon EKS cluster (Kubernetes)
- ``` create-deployment ``` - updates the Kubernetes config and creates or updates resources
- ``` aws-eks/update-container-image ``` - updates the kubectl configuration and container images
- ``` test-cluster ``` - tests the cluster
- ``` aws-eks/delete-cluster ``` - deletes the cluster, can be commented out

Screenshots of the first and second deployment of the app, green pipeline, linter success and fail can be found in the screenshots folder.

Pipeline status:
[![CircleCI](https://circleci.com/gh/markanr/udacity-aws-devops-capstone.svg?style=svg)](https://circleci.com/gh/markanr/udacity-aws-devops-capstone)
