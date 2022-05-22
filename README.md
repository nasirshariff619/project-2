# project-2

## Contents



## Brief <a name="Brief"></a>

 My overall objective during the completion of this project is to create a service orientated application with utilisation of supporting tools, methodologies and technologies that encapsulate all core modules covered during training.

 This enables the trainers to assess our capabilty of using the technologies and concepts that have been taught to us.


 ### My Approach <a name="My Approach"></a>
 Considering all this information, I have decided on creating a random holiday task generator. 
 The back-end of this app consists of 4 services which interact with eachother.

 Service 1 is responsible of communicating with all the other 3 services. Service 2 and 3 are both responsible with generating a random object from a list, for example, service 2 generates a random country and service 3 generates a random food. Service 1 gets this information from service 2 and 3 and posts it to service 4. Service 4 then geneartes a task based on the information from service 2 and 3.


## Design <a name="Design"></a>

### Database Structure <a name="Database Structure"></a>



### CI Pipeline <a name="CI Pipeline"></a>



### Feature Branch Model <a name="Feature Branch Model"></a>

As learnt in training, when working on a software project, it is good practise to implement the feature branch model. This meant that work carried out on the project was done on a development branch, which meant that the code was tested and deployed from this branch before it was merged into the main branch.

image

## Project Tracking <a name="Project Tracking"></a>

The overall tracking of the project was carried out on a kanban board website known as Trello.




## Risk Assessment <a name="Risk Assessment"></a>

The image below shows a quick screenshot of the risk assessment, which was used to assess and analyse the risks that could arise from this project. Here is a link to the full risk assessment:

## Testing <a name="Testing"></a>

Unit testing was carried out on the application. This was done using pytest and pytest coverage and shown by the output below:





## Front-End Design <a name="Front-End Design "></a>




## Future improvements <a name="Future Improvements"></a>



## Acknowledgements <a name="Acknowledgements"></a>

I would like to give thanks to the QA trainers that have taught me over _______, providing the learning required to complete this project. I also give thanks to my fellow QA trainees for making the learning experience pleasant and providing help when I needed it.

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



## Author <a name="Author"></a>
Nasir Shariff
