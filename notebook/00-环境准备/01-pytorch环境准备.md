## PyTorch环境准备

- 参考文档
  - https://pytorch.org/
  - https://jupyter.org/

### MacOS环境准备

- 安装虚拟环境

  ```bash
  # brew install pyenv && brew install pyenv-virtualenv
  pyenv virtualenv 3.11.5 env_pytorch_action
  pyenv local env_pytorch_action
  ```

- 安装PyTorch

  ```bash
  pip3 install torch torchvision torchaudio
  ```

  > 执行上面语句后，环境中也会自动安装好`pillow`，`numpy`了

- 安装Jupyter Notebook

  ```bash
  pip install --upgrade pip
  pip install ipython
  pip install notebook
  ```

- 安装timm库：Torch Image Models是一个在PyTorch中实现的留下深度学习模型库

  ```bash
  pip install timm
  ```

- 安装其它库

  ```bash
  pip install matplotlib
  pip install pandas
  pip install gradio
  ```

- 查看安装的库

  ```bash
  pip freeze
  ```

  得到的输出：
  
  ```bash
  ipython==8.24.0
  matplotlib==3.8.4
  matplotlib-inline==0.1.7
  notebook==7.1.3
  numpy==1.26.4
  pandas==2.2.2
  pillow==10.3.0
  timm==0.9.16
  torch==2.3.0
  torchaudio==2.3.0
  torchvision==0.18.0
  ```
  
  