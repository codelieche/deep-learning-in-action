### 参考文档

- https://ollama.com/
- https://github.com/ollama/ollama
- https://github.com/ollama/ollama-python



### 安装allama

> 直接官网下载APP然后安装。

- 查看版本

  ```bash
  ➜  app git:(main) ✗ which ollama
  /usr/local/bin/ollama
  ➜  app git:(main) ✗ ollama --version
  ollama version is 0.1.34
  ```

- 注意事项

  - 模型保存的位置：`~/.ollama/models/`

### 常用模型

- https://ollama.com/library/llama3

  > facebook出品

- https://ollama.com/library/gemma

  > google出品。

- https://ollama.com/library/qwen

  > 阿里巴巴出品。中文中比较好的模型，特别是72b的模型。
  >
  > Qwen 1.5 is a series of large language models by Alibaba Cloud spanning from 0.5B to 110B parameters。
  >
  > ollama run qwen:32b
  >
  > ```bash
  > ollama pull qwen:7b
  > ollama pull qwen:7b-chat-v1.5-fp16
  > ```

- https://ollama.com/library/llava

  > 分析图片中的内容。
  >
  > ```bash
  > ollama pull llava:34b-v1.6
  > ```
  >
  > https://ollama.com/library/llava:34b-v1.6

- https://ollama.com/library/gemma

  > Google DeepMind出品。
  >
  > ```bash
  > ollama pull gemma:7b
  > ```
  >
  > 翻译功能。

  

### 常用操作

- `ollama --help`: 查看帮助

  ```
  # ollama --help
  Large language model runner
  
  Usage:
    ollama [flags]
    ollama [command]
  
  Available Commands:
    serve       Start ollama
    create      Create a model from a Modelfile
    show        Show information for a model
    run         Run a model
    pull        Pull a model from a registry
    push        Push a model to a registry
    list        List models
    cp          Copy a model
    rm          Remove a model
    help        Help about any command
  
  Flags:
    -h, --help      help for ollama
    -v, --version   Show version information
  
  Use "ollama [command] --help" for more information about a command.
  ```

  

- `ollama pull llama3`: 

  

- `ollama list`: 查看拉取的模型

  ```bash
  ➜  app git:(main) ✗ ollama list
  NAME         	ID          	SIZE  	MODIFIED
  llama3:latest	a6990ed6be41	4.7 GB	16 seconds ago
  ```

  ![image-20240510145001071](../../../../../../../assets/image-20240510145001071.png)

- 运行模型：`ollama run llama3`

  

### 模型运行



## Model library



Ollama supports a list of models available on [ollama.com/library](https://ollama.com/library)

Here are some example models that can be downloaded:

| Model              | Parameters | Size  | Download                       |
| ------------------ | ---------- | ----- | ------------------------------ |
| Llama 3            | 8B         | 4.7GB | `ollama run llama3`            |
| Llama 3            | 70B        | 40GB  | `ollama run llama3:70b`        |
| Phi-3              | 3.8B       | 2.3GB | `ollama run phi3`              |
| Mistral            | 7B         | 4.1GB | `ollama run mistral`           |
| Neural Chat        | 7B         | 4.1GB | `ollama run neural-chat`       |
| Starling           | 7B         | 4.1GB | `ollama run starling-lm`       |
| Code Llama         | 7B         | 3.8GB | `ollama run codellama`         |
| Llama 2 Uncensored | 7B         | 3.8GB | `ollama run llama2-uncensored` |
| LLaVA              | 7B         | 4.5GB | `ollama run llava`             |
| Gemma              | 2B         | 1.4GB | `ollama run gemma:2b`          |
| Gemma              | 7B         | 4.8GB | `ollama run gemma:7b`          |
| Solar              | 10.7B      | 6.1GB | `ollama run solar`             |

> Note: You should have at least 8 GB of RAM available to run the 7B models, 16 GB to run the 13B models, and 32 GB to run the 33B models.