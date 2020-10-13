<h1>Media Clown Text Generator Website</h1>
<h3>Development</h3>
<hr>
<p>This repo contains the code that runs the text generation website. It is built using the <code>Django Framework</code> and the <code>Textgenrnn library</code>
To get up and running you will need python 3.8+ and pip installed on your computer. To install the project packages run the command
<code>pip install -r requirements.txt</code>. 
<br>
<br>
The project will require you to copy the textgenrnn files to the root of the project.
These three files are called: <code>des-train_config.json</code>, <code>des-train_vocab.json</code>, <code>des-train_weights.hdf5</code>.
Once these are copied the <code>Django</code> server can be started by running <code>python manage.py runserver</code> in your terminal.
</p>
<h3>Deployment</h3>
<hr>
Once the project is ready to be deployed it can be bundled into a Docker Container. To do so run the command 
<code>docker build . -f Dockerfile-prod</code>. Once the image is built it can be run using the command 
<code>docker container run -d -p "8055:8055" {image_tag_name}</code>
