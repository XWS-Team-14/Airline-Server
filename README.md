# Project startup
# 1. Install docker and docker-compose
### Linux
`sudo pacman -Syu docker`
`sudo pacman -Syu docker-compose`
### Windows 
Install app from official website <a href="https://docs.docker.com/desktop/install/windows-install/">guide</a>

# 2. Build a docker images
Position yourself in the project root folder
### Linux
`sudo docker-compose build`
Recommended to use a docker visualizer like `lazydocker` for an easier time
### Windows
Use PowerShell or follow the official guide on the docker website

# 3. Docker Services
## Docker stuff
`app` - Starts main django aplication
`mongo` - Starts mongo database
`mongo-dumpdata` - Dumps database data into json file in the fixtures folder (overwrites current file)
`mongo-loaddata` - Load data from json file in the fixtures folder (overwrites the current database)
`mongo-migrate` - Applies changes made to your model and migrates them


## Use cases
### 1. Setup from clean volumes
- **Up** `mongo` 
-  **Up** `mongo-migrate`
-  **Up** `mongo-loaddata`
-  **Up** `app`

Your `app` is now ready to be used with the initial data provided

### 2.  Make migrations
* **Up** `mongo-makemigrations`
 
Your migrations are created and documented automatically
### 3. Adding more initial data
1. Manual addition
	- Open file  `app/airline-app/fixures/init.json`
	- Add more data (needs to be structured well)
2. Through the app
	- Have either a clean `app` ran or have only had data u want to persist to file
	- Add data through the app's API
	- **Up** `mongo-dumpdata` <span style="color:red">! Important - data in the old init file will be overwritten</span>