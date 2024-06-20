## Python环境准备



### 1. pyenv

- https://github.com/pyenv/pyenv



### 2. miniconda

- https://docs.anaconda.com/free/miniconda/
- 注意事项：
  - `conda`和`pip`都可以安装包，但是别混用。特别是升级包的时候，可能导致环境异常
  - 如果`conda`安装不ok的包，我们再考虑用`pip`



#### 2.1 MacOS M1安装miniconda

- 第一步：下载[./Miniconda3-latest-MacOSX-arm64.sh](https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh)

- 第二步：添加权限执行sh文件

  ```bash
  chmod +x ./Miniconda3-latest-MacOSX-arm64.sh
  ./Miniconda3-latest-MacOSX-arm64.sh
  ```

  一次回车，输入`yes`，再回车。就会安装好了。

#### 2.2 conda基本使用

- `conda --help`

  ```
  usage: conda [-h] [-v] [--no-plugins] [-V] COMMAND ...
  
  conda is a tool for managing and deploying applications, environments and packages.
  
  options:
    -h, --help          Show this help message and exit.
    -v, --verbose       Can be used multiple times. Once for detailed output, twice for INFO logging, thrice
                        for DEBUG logging, four times for TRACE logging.
    --no-plugins        Disable all plugins that are not built into conda.
    -V, --version       Show the conda version number and exit.
  
  commands:
    The following built-in and plugins subcommands are available.
  
    COMMAND
      activate          Activate a conda environment.
      clean             Remove unused packages and caches.
      compare           Compare packages between conda environments.
      config            Modify configuration values in .condarc.
      content-trust     Signing and verification tools for Conda
      create            Create a new conda environment from a list of specified packages.
      deactivate        Deactivate the current active conda environment.
      doctor            Display a health report for your environment.
      export            Export a given environment
      info              Display information about current conda install.
      init              Initialize conda for shell interaction.
      install           Install a list of packages into a specified conda environment.
      list              List installed packages in a conda environment.
      notices           Retrieve latest channel notifications.
      package           Create low-level conda packages. (EXPERIMENTAL)
      remove (uninstall)
                        Remove a list of packages from a specified conda environment.
      rename            Rename an existing environment.
      repoquery         Advanced search for repodata.
      run               Run an executable in a conda environment.
      search            Search for packages and display associated information using the MatchSpec format.
      update (upgrade)  Update conda packages to the latest compatible version.
  ```

#### 2.3 创建python环境

- 我们创建`deep-learning-in-action`名字的环境

  ```bash
  conda create -y -n deep-learning-in-action python=3.12
  ```

- 激活环境：

  ```bash
  conda activate deep-learning-in-action
  ```

- 安装依赖包：

  ```bash
   conda install pytorch::pytorch torchvision torchaudio -c pytorch
   
   conda install numpy pandas matplotlib
   
   conda install conda-forge::transformers
   conda install -c huggingface -c conda-forge datasets
   conda install tokenizers
   
   conda installbeautifulsoup4 requests sqlalchemy statsmodels scikit-learn pyarrow pytables
  ```

  

- 安装环境时输出日志：

  ```
  conda create -n deep-learning-in-action python=3.12
  Retrieving notices: ...working... done
  Channels:
   - conda-forge
  Platform: osx-arm64
  Collecting package metadata (repodata.json): done
  Solving environment: done
  
  ## Package Plan ##
  
    environment location: /Users/username/miniconda3/envs/deep-learning-in-action
  
    added / updated specs:
      - python=3.12
  
  
  The following packages will be downloaded:
  
      package                    |            build
      ---------------------------|-----------------
      bzip2-1.0.8                |       h93a5062_5         119 KB  conda-forge
      ca-certificates-2024.6.2   |       hf0a4a13_0         153 KB  conda-forge
      libexpat-2.6.2             |       hebf3989_0          62 KB  conda-forge
      libffi-3.4.2               |       h3422bc3_5          38 KB  conda-forge
      libsqlite-3.46.0           |       hfb93653_0         811 KB  conda-forge
      libzlib-1.3.1              |       hfb2fe0b_1          46 KB  conda-forge
      ncurses-6.5                |       hb89a1cb_0         776 KB  conda-forge
      openssl-3.3.1              |       hfb2fe0b_0         2.8 MB  conda-forge
      pip-24.0                   |     pyhd8ed1ab_0         1.3 MB  conda-forge
      python-3.12.3              |h4a7b5fc_0_cpython        12.6 MB  conda-forge
      readline-8.2               |       h92ec313_1         244 KB  conda-forge
      setuptools-70.0.0          |     pyhd8ed1ab_0         472 KB  conda-forge
      tk-8.6.13                  |       h5083fa2_1         3.0 MB  conda-forge
      tzdata-2024a               |       h0c530f3_0         117 KB  conda-forge
      wheel-0.43.0               |     pyhd8ed1ab_1          57 KB  conda-forge
      xz-5.2.6                   |       h57fd34a_0         230 KB  conda-forge
      ------------------------------------------------------------
                                             Total:        22.7 MB
  
  The following NEW packages will be INSTALLED:
  
    bzip2              conda-forge/osx-arm64::bzip2-1.0.8-h93a5062_5
    ca-certificates    conda-forge/osx-arm64::ca-certificates-2024.6.2-hf0a4a13_0
    libexpat           conda-forge/osx-arm64::libexpat-2.6.2-hebf3989_0
    libffi             conda-forge/osx-arm64::libffi-3.4.2-h3422bc3_5
    libsqlite          conda-forge/osx-arm64::libsqlite-3.46.0-hfb93653_0
    libzlib            conda-forge/osx-arm64::libzlib-1.3.1-hfb2fe0b_1
    ncurses            conda-forge/osx-arm64::ncurses-6.5-hb89a1cb_0
    openssl            conda-forge/osx-arm64::openssl-3.3.1-hfb2fe0b_0
    pip                conda-forge/noarch::pip-24.0-pyhd8ed1ab_0
    python             conda-forge/osx-arm64::python-3.12.3-h4a7b5fc_0_cpython
    readline           conda-forge/osx-arm64::readline-8.2-h92ec313_1
    setuptools         conda-forge/noarch::setuptools-70.0.0-pyhd8ed1ab_0
    tk                 conda-forge/osx-arm64::tk-8.6.13-h5083fa2_1
    tzdata             conda-forge/noarch::tzdata-2024a-h0c530f3_0
    wheel              conda-forge/noarch::wheel-0.43.0-pyhd8ed1ab_1
    xz                 conda-forge/osx-arm64::xz-5.2.6-h57fd34a_0
  
  
  Proceed ([y]/n)? y
  
  
  Downloading and Extracting Packages:
  
  Preparing transaction: done
  Verifying transaction: done
  Executing transaction: done
  #
  # To activate this environment, use
  #
  #     $ conda activate deep-learning-in-action
  #
  # To deactivate an active environment, use
  #
  #     $ conda deactivate
  ```

  

- 想要像pyenv一样自动激活python环境

  ```bash
  # 自动激活conda环境
  activate_conda_env_on_cd() {
      local target_dir="$1"
      # echo "进入：$1"
  
      # 后续优化成，遍历上一级目录看是否有这个文件
      if [ -f .python-conda ]; then
          local env_name=$(cat .python-conda)
          # echo "拥有.python-conda文件：${env_name}"
  
          # 如果目录名与conda环境名相同，则激活该环境
          if conda info --envs | grep -q "^\s*${env_name}\s"; then
              conda activate "${env_name}"
          fi
      fi
  }
  
  # 在每次cd命令后调用此函数
  cd() {
      builtin cd "$@"
      activate_conda_env_on_cd "$PWD"
  }
  ```

  可把以上代码写入到：`~/.bash_profile`。待优化