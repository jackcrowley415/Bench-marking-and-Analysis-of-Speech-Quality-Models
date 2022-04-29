The Pipeline itself can be run from this link https://github.com/JackGeraghty/AQP.

Follow the instructions that are given in this GitHub repository and that should be the pipeline running.

Once the pipeine is running you need to change the --root_node_id to "Load Signal" and the --graph_config_path to "config/Test.json"

Within the Test.json file which is found in the config folder, you must change the name of the test node tot the specific Node that you want to run.

This is the list of nodes that I have created.
barchartperconditionnode
linearregressionnode
pearsonnode
rmsenode
scatplotperconditionnode

I made a jupyter notebook that if run will print out all the outputs of the nodes in case the pipeline isnt working as it is quite temperamental, you just need to change the location of the Dataframes to the location within your computer.
Eg. Data = pd_read.csv("Your location")