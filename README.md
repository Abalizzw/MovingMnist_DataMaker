# MovingMnist Data Maker
Making the own data which the structure is similar to Moving_mnist dataset

***
# Environment installing
Command `pip install -r enviroment.txt` to install the required packages.  
# Data Processing Operation 
  1.Run `do.py` to save each singal frame in the video data and resize them.  
  2.Run `read_videolist.py` to show videos information, mainly contains `frame size`,`fps` and `total amount of frames`.  
  3.Run `npy2txt.py` to restore the .npy data into .txt files, then you can check the specific values in the data.  
  4.Run `generate_dataset.py` to generate the processed frames by calling AlphaPose.  
  5.Run `img2npy.py` to save the image data into .npy and package to .npz file, which the format is the same as origin MovingMnist data.  
