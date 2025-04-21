# 🛠️ Setup Notes – Day 2

## ✅ Goal
Install Haystack and dependencies, fix any issues, and run the basic QA pipeline tutorial.


---

While setting up and install dependencies, got an error related to Pillow verison which was not compatible with python 

## 🧰 Environment

- **OS**: Windows
- **Python Version**: 3.11
- **Virtual Environment**: `myenv`
  
1. Created a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate
  
2. Upgraded pip & tools:
  pip install --upgrade pip setuptools wheel
  Resolved Pillow compatibility issue with:
  
3. 
  pip install "pillow>=10.0.0"
  
4. Installed Haystack:
  pip install farm-haystack[colab,inference]
  
While installing dependencies, got an issue with pillow versioning, resolved it by installing a different version.