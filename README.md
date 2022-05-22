# project-2

## Contents
*   [Brief](#brief-a-name"brief"a)
    *   [My Approach](#my-approach-a-name"my-approach"a)
*   [Design](#design-a-name"design"a)
    *   [Virtual Machine Setup](#virtual-machine-setup-a-name"virtual-machine-setup"a)
    *   [CI Pipeline](#ci-pipeline-a-name"ci-pipeline"a)
    *   [Feature Branch Model](#feature-branch-model-a-name"feature-branch-model"a)
*   [Project Tracking](#project-tracking-a-name"project-tracking"a)
*   [Risk Asessment](#risk-assessment-a-name"risk-assessment"a)
*   [Testing](#testing-a-name"testing"a)
*   [Front-End Design](#front-end-design-a-name"front-end-design-"a)
*   [Future Improvements](#future-improvements-a-name"future-improvements"a)
*   [Acknowledgements](#acknowledgements-a-name"acknowledgements"a)
*   [Licensing](#licensing-a-name"licensing"a)
*   [Presentation](#presentation-a-name"presentation"a)
*    [Author](#author-a-name"author"a)



## Brief <a name="Brief"></a>

 My overall objective during the completion of this project is to create a service orientated application with utilisation of supporting tools, methodologies and technologies that encapsulate all core modules covered during training.

 This enables the trainers to assess our capabilty of using the technologies and concepts that have been taught to us.


 ### My Approach <a name="My Approach"></a>
 Considering all this information, I have decided on creating a random holiday task generator. 
 The back-end of this app consists of 4 services which interact with eachother.

 Service 1 is responsible of communicating with all the other 3 services. Service 2 and 3 are both responsible with generating a random object from a list, for example, service 2 generates a random country and service 3 generates a random food. Service 1 gets this information from service 2 and 3 and posts it to service 4. Service 4 then geneartes a task based on the information from service 2 and 3.


## Design <a name="Design"></a>

### Virtual Machine Setup <a name="Virtual Machine Setup"></a>

This project used 3 GCP virtual machines which were designed as follows:
![vm](https://user-images.githubusercontent.com/101716216/169696077-318cff1b-8d27-46ea-bbf8-857ceb6260c5.jpg)
The main virtual machine (VM) was used to develop the application and set up Ansible, Docker Swarm and Nginx.



### CI Pipeline <a name="CI Pipeline"></a>

The following depicts the desired continuous integration (CI) pipeline:
![ci](https://user-images.githubusercontent.com/101716216/169697193-1c03f9f1-6040-40f4-966b-f56f7d738e34.jpg)




### Feature Branch Model <a name="Feature Branch Model"></a>

As learnt in training, when working on a software project, it is good practise to implement the feature branch model. This meant that work carried out on the project was done on a development branch, which meant that the code was tested and deployed from this branch before it was merged into the main branch.

*****image********

## Project Tracking <a name="Project Tracking"></a>

The overall tracking of the project was carried out on a kanban board website known as Jira.
The kanban board was used to add tasks to and track their progress. The initial kanban board looked as follows:
![image](https://user-images.githubusercontent.com/101716216/169698171-3c419339-4dd2-4452-9ff7-e1e186e2f030.png)
This kanban board was updated with new tasks and other tasks were processed by stage until they were completed. The updated kanban board looked as follows:
![image](https://user-images.githubusercontent.com/101716216/169698338-877b9431-c90a-4c3f-8478-8f1e018f3983.png)





## Risk Assessment <a name="Risk Assessment"></a>

The image below shows a quick screenshot of the risk assessment, which was used to assess and analyse the risks that could arise from this project. As the project development continued, the risk assessment was also updated, which was tracked by the added. Here is a link to the full risk assessment:
https://docs.google.com/spreadsheets/d/1VV1P8t2pfBq8ljTdY-ddTQVFnFJPgFQ8/edit?usp=sharing&ouid=109921713876439168912&rtpof=true&sd=true

## Testing <a name="Testing"></a>

Unit testing was carried out on each service in the application. This was done using pytest and pytest coverage.

Service 1 pytest output:
![image](https://user-images.githubusercontent.com/101716216/169699388-7d22f195-82f2-44c4-aede-2ecda00c5dd0.png)

Service 2 pytest output:
![image](https://user-images.githubusercontent.com/101716216/169699547-3471ade9-d240-40d4-a800-7537815b3767.png)

Service 3 pytest output:
![image](https://user-images.githubusercontent.com/101716216/169699907-2b315170-be18-4391-8895-03ef8d742807.png)

Service 4 pytest output:
![image](https://user-images.githubusercontent.com/101716216/169699945-2f7f55d0-f4d4-481d-99ab-3fddabdff64e.png)






## Front-End Design <a name="Front-End Design "></a>
When accessing the application, you are given a random country, random food and task based on the two random generated pieces of information. A few snapshots of the website are shown below:
![image](https://user-images.githubusercontent.com/101716216/169700094-7d2043c8-b3a0-4e95-a71d-8cdedbab4d1f.png)
![image](https://user-images.githubusercontent.com/101716216/169700125-737d9d75-7e06-4d7b-97dd-05407a30b2af.png)
![image](https://user-images.githubusercontent.com/101716216/169700158-3c16361a-3215-4bfe-845b-900dfe9d9039.png)





## Future improvements <a name="Future Improvements"></a>

Following the requirements set out by the project specification, I was able to implement most tools required. However, eventhough jenkins was able to clone the repositry and install the requirements, due to errors and time constraints, I was unsuccessful at getting the jenkins script to test, build and build & deply the application. Therefore I was required to use a method of continuous delivery to manually build and deploy the application using docker-compose and ansible.

My attempt at getting the jenkins script to run can be seen below:

![image](https://user-images.githubusercontent.com/101716216/169701389-e6b8c010-f22f-4437-a63c-c8ae51cd1b9d.png)

The jenkins script used is as follows:

![image](https://user-images.githubusercontent.com/101716216/169701542-fafc8ed6-ad27-4683-b79d-e66041a8afa7.png)
![image](https://user-images.githubusercontent.com/101716216/169701560-cf703d86-30ab-4d22-a931-6d8e6200cb05.png)
![image](https://user-images.githubusercontent.com/101716216/169701586-d258f88a-0a83-42f1-ba04-59ccde96cc13.png)


## Acknowledgements <a name="Acknowledgements"></a>

I would like to give thanks to the QA trainers that have taught me over the second portion of training, providing the learning required to complete this project. I also give thanks to my fellow QA trainees for making the learning experience pleasant and providing help when I needed it.

## Licensing <a name="Licensing"></a>
This app will be licensed with the Apache License 2.0. Under this license, the users are allowed to:

* Use the code commercially.
* Alter the code.
* Distribute any copies or modifications of the code.
* Sublicense the code.
* Use patent claims.
* Place warranty.

Copyright [2022] [Nasir Shariff]

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

## Presentation <a name="Presentation"></a>

Here is a link to the video presentation:
https://drive.google.com/file/d/1umnzxQQSvsj6fuzIgM-_vz7xeaqnoVc8/view?usp=sharing



## Author <a name="Author"></a>
Nasir Shariff
