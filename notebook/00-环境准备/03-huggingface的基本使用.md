## HuggingFace的基本使用



### 参考文档

- https://huggingface.co/
- https://huggingface.co/docs/transformers/index





### Transformers基本使用

- 准备库：transformers

  ```bash
  pip install transformers
  ```

- pipline简单示例：

  - https://huggingface.co/docs/transformers/quicktour#pipeline

  ```python
  from transformers import pipeline  
    
  # 初始化sentiment-analysis pipeline  
  nlp = pipeline("sentiment-analysis")  
    
  # 定义一个待分析的语句  
  sentence = "This is a happy day!"  
    
  # 使用pipeline处理语句  
  result = nlp(sentence)  
    
  # 输出结果  
  print(f"Sentence: {sentence}")  
  print(f"Sentiment: {result[0]['label']}, Score: {result[0]['score']}")
  ```

  **初次运行，会下载模型，会有点慢。**

  ```
  No model was supplied, defaulted to distilbert/distilbert-base-uncased-finetuned-sst-2-english and revision af0f99b (https://huggingface.co/distilbert/distilbert-base-uncased-finetuned-sst-2-english).
  Using a pipeline without specifying a model name and revision in production is not recommended.
  /Users/alex.zhou/.pyenv/versions/3.11.5/envs/env_3.11_pytorch/lib/python3.11/site-packages/huggingface_hub/file_download.py:1132: FutureWarning: `resume_download` is deprecated and will be removed in version 1.0.0. Downloads always resume when possible. If you want to force a new download, use `force_download=True`.
    warnings.warn(
  config.json: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 629/629 [00:00<00:00, 920kB/s]
  model.safetensors: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 268M/268M [01:21<00:00, 3.27MB/s]
  tokenizer_config.json: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 48.0/48.0 [00:00<00:00, 261kB/s]
  vocab.txt: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 232k/232k [00:01<00:00, 116kB/s]
  Sentence: This is a happy day!
  Sentiment: POSITIVE, Score: 0.9998838901519775
  ```

  

