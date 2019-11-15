
# coding: utf-8

# In[1]:


from os import path


# In[2]:


BASE_PATH = "fer2013"
INPUT_PATH = path.sep.join([BASE_PATH, "fer2013/fer2013.csv"])


# In[3]:


INPUT_PATH


# In[4]:


NUM_CLASSES = 6


# In[5]:


TRAIN_HDF5 = path.sep.join([BASE_PATH, "hdf5/train.hdf5"])
VAL_HDF5 = path.sep.join([BASE_PATH, "hdf5/val.hdf5"])
TEST_HDF5 = path.sep.join([BASE_PATH, "hdf5/test.hdf5"])


# In[6]:


BATCH_SIZE = 128

 # define the path to where output logs will be stored
OUTPUT_PATH = path.sep.join([BASE_PATH, "output"])

