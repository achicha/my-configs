##### Requirements:

    # user_name should be in docker group
    sudo usermod -aG docker user_name   # add user to docker group
    groups user_name                    # show all user's groups


#### Quick start
    # build container
    docker build -t my_image -f ./my_Dockerfile ./

    # run container
    docker run --restart=always --name jupnot --user root -p 8888:8888 -d -v /c/docker_folder:/home/folder my_image
    
    # attach to container's session
    docker exec -it [container_id] bash
    
    # show all containers
    docker ps -a
    
    # remove all stopped containers
    docker ps -q -f status=exited | xargs --no-run-if-empty docker rm
      