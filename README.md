# EMOTION-RECOGITION-USING-KERAS
I strongly recomend you to follow exact directory structure the way I have folllowed.

## Task 1 : Build Dataset

After downloading dataset create following folders:

--fer2013
|  |--fer2013 {In this folder keep .csv file}
        
|  |--hdf5    {We will convert images into hdf5 format and store here }

|  |--output  {we will save training plot into output directory}


Now open your command prompt go to directory where you keep build_dataset.py and write these:

python build_dataset.py

After executing it, you will find that in directory fer2013/hdf5 three hdf5 file will be generated.


##  Task 2: Train Model from scratch

To train the model open command prompt and execute following command

# let's say you want to train model for 20 epoch at some learning rate let's say 'LR1' and want to check training loss,validation loss ,training accuracy ,validation accuracy and  their plot then follow these steps:

step 1: First open train_recognizer.py and change learning rate (at line 67 and 76)  and also change epoch(number of epoch) at line 95.

step 2: Open command prompt and execute this command:

    python train_recognizer.py --checkpoints checkpoints

After executing this you will see in directory fer2013/output one image will be formed titled as 'vggnet_emotion.png' it will have loss and accuracy plots.....u can analyze from this plot and make sure we are not overfitting or underfitting .

# If you do not satisfied from your model perfomance you can again start training from where you have left it............HOW?

ANSWER:

In --checkpoints directory we are storing model weights as the network is trained. If you open directory checkpoints you will see that after every 5 epoch we are storing model weights .

Only thing we need to do is we need to load a specific epoch from disk and we can restart training, we can supply the --model path to the specific checkpoint and provide the --start-epoch of the associated checkpoint.

EXample: let's say you want to restart training after 20 epoch. open command prompt and write:

          python train_recognizer.py --checkpoints checkpoints --model checkpoints/epoch_20.hdf5 --start 20
         
# At Last .....RESULT:


