# **Python duplicate checker using streamlit**
> **Note**
> If you're using any other OS than windows this will probaly not work, because it is depending on the python libary os which is made for windows only, [see this doc for more info](https://docs.python.org/3/library/os.html)

## **Key Features**

* Be able to choose to different folders *(One for the duplicates and another for dumping the registered duplicates into)*
	*  Duplicates will not be deleted but moved to ensure that the wrong files isn't deleted
* Loading bar showing the progress of searched files compared to files to search
  - With text that shows an estimate of time to run the task
* End text that shows the checking has been complete and how many files have been transferred
* [Streamlit](https://streamlit.io/) library to UI


## **Installation and setup**

To clone and run this application, you'll need [Git](https://git-scm.com) and [Python 1.12.2](https://www.python.org/downloads/?ref=gfxhacks.com) many other python version should work as well, but 1.12.2 was used for the creation of the script. 

From your command line:
```bash
# Clone this repository
git clone https://github.com/BertramAakjaer/Python_duplicate_checker-Streamlit.git

# Install streamlit library
pip install streamlit

# Enter the directory
cd Python_duplicate_checker-Streamlit/

# Run the script using streamlit and it should open in your default browser
python -m streamlit run main.py
```
## **Usage**
![Image](screenshots/mainFolderUpload.jpg)

1. Firstly go to your prefered file explorer and find the path to folder including duplicated files. Paste this into the first textbox named *"Folder with duplicates"*.
   
2. Then find a temporary folder to fill with all the registered duplicates and paste the path into the textbox named *"Destination folder"*.
   
3. Then you're ready and should just be able to press the button *"Start duplicate check"* and the program should do the rest.

![Image](screenshots/progressVisualisation.jpg)

## **License**

This project is licensed under the [MIT License](LICENSE).


## **Socials**
> [Aakjaer.site](www.aakjaer.site) &nbsp;&middot;&nbsp;
> GitHub [@BertramAakjær](https://github.com/BertramAakjaer) &nbsp;&middot;&nbsp;
> Twitter [@BertramAakjær](https://twitter.com/BertramAakjaer)
