# Tanzu Application Platform

## Working on your my-qabot-1 project

### Deploying to Kubernetes as a TAP workload with Tanzu CLI

If you make modifications to the source you must push the changes to your Git repository.

When you are done developing your app and have pushed the latest changes to your Git repository, then you can simply deploy it using:

```
tanzu apps workload apply -f config/workload.yaml
```

If you would like to deploy the code from your local working directory you can use the following command:

```
tanzu apps workload create my-qabot-1 -f config/workload.yaml \
  --local-path . \
  --source-image <REPOSITORY-PREFIX>/my-qabot-1-source \
  --type web
```

### Accessing the app deployed to your cluster

Determine the URL to use for accessing the app by running:

```
tanzu apps workload get my-qabot-1
```

To access the deployed app use the URL shown under "Workload Knative Services".

This depends on the TAP installation having DNS configured for the Knative ingress.

## How to deploy without TAP

While the simplest and most robust deployment method is using Tanzu Application Platform, this accelerator has also been prepared to support building and deploying a container to any host running a docker or oci-compatible container engine, or to kubernetes.

### Building the container with cloud-native buildpacks and pack cli

[Cloud-Native buildpacks](https://buildpacks.io/) provide a simple, mature, open source solution for building containers without needing to prepare dockerfiles. Dockerfiles are great, but, people need to be trained and spend time to make them. And very few people know how to write dockerfiles according to best known practices. And they are very prone to human error.

Buildpacks are maintained by an open source community including a lot of people who are top experts on building containers. They use industry-best practices including multi-stage builds to automate building of containers. Most programming languages are supported, and a huge number of massive companies have been using buildpacks in production for over a decade. 

If you want to create a dockerfile, please do feel free if you prefer to, but instructions will only be provided here for using cloud native buildpacks with pack cli to build your container. Once you have built the container, all the other steps provided here are the same regardless of how you built the container.

Note: Ensure you are using a host with adequate ram, cpu and storage. I have not tested how much resources are required, but I test builds on a Ubuntu VM with 32GB Ram, 4vcpus and 100GB HDD.

To build a container that will serve the my-qabot-1 application, complete the following steps:

1. Install Pack CLI by following instructions here: [https://buildpacks.io/docs/tools/pack/](https://buildpacks.io/docs/tools/pack/)
2. Build the container with the command `pack build container_name:version --builder paketobuildpacks/builder:base` - replace the part that says "container_name:version" with whatever name and version number you want for your container.

### Deploying to docker/oci-compatible container engine

Once your container is built you can deploy it just like any other container. You can immediately deploy the container on the same host you built it on, or if you want to deploy it on any other host, you should push your container to an oci-compatible container registry that is accessible from the host you want to deploy the container on. 

I will not include instructions here on how to push the container to a registry as you would use the same process with any container and there are lots of articles on the topic. 

The web-ui in the container runs on port 7860, assuming you are running docker or an oci-compatible container engine on localhost, you could run the container using the command `docker run -p 8080:7860 container_name:version`, which would expose the application on port 8080. If you want to run the app on a different port, you could update the command accordingly. 

The container takes several minutes to initialize, once it has finished initializing and is ready to use, you should see the text `Running on local URL: 0.0.0.0:7860` in your terminal. Once you see this output, you should be able to access the my-qabot-1 app by opening a browser to http://localhost:8080.


### Deploying to kubernetes without TAP

To deploy the application to kubernetes, you must first build the container and push the container to an OCI compatible container registry that is accessible to your kubernetes nodes. If your container registry requires authentication, you must create any needed imagepullsecrets. In my test lab, I am using a publicly accessible container registry, and so I will not cover how to handle registry authentication here, but, it would be the same as for any container running on k8s. 

This repository includes 3 files for deploying to kubernetes located in the /k8s directory in the my-qabot-1 package/repository. One file is for deployment, one is for ingress if you are using contour ingress controller, and there is an alternate ingress provided if you are running nginx ingress controller. 

To deploy the application to kubernetes using a kubectl client that is configured to access your desired cluster, complete the following steps:

1. Open the [qabot1-deployment.yaml file](k8s/qabot1-deployment.yaml), look for the text that says `your_container_name:version` and replace it with your container name/version.
2. Create a namespace for the deployment if desired, for example: `kubectl create ns my-qabot-1`
3. Create the deployment and service with the command: `kubectl create -f k8s/qabot1-deployment.yaml -n my-qabot-1`
4. Note, the Ingress assumes that a cert-manager clusterissuer named letsencrypt-production is available. If it is not, update the ingress file as needed for your environment
5. Select the appropriate ingreess file depending on whether you are using contour or nginx ingress controller, edit the spec.tls.hosts and spec.rules.host values. These values are currently set to `my-qabot-1.example.com`, replace this value with the desired URL for your environment.
6. Deploy the ingress file for the ingress controller used in your environment, for example: `kubectl create -f k8s/qabot1-ingress-contour.yaml -n my-qabot-1` OR `kubectl create -f k8s/qabot1-ingress-nginx.yaml -n my-qabot-1`
7. Ensure your DNS is configured to route traffic for your ingress host URL to the appropriate IP address for your ingress controller configuration. 

Verify the deployment is up, and you should be able to access the app at the URL definied in your ingress configuration. 

