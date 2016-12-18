# Installation Instructions

Student to fill in with instructions of how to use their selected tool to 
deploy application for final project.

I selected ansible for my final project implementation
(note these steps are assuming a container already exists)
->cd into the ansible directory of this project
->run the command ansible-playbook final.yml to execute the playbook and push it to all clients in the hosts.py file
->wait
->login manually via ssh and run curl http://localhost/quote/16 if you would like to verify the correct installation
