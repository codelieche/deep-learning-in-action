## Transformers

### Transformers简介
> 为`PyTorch`、`TensorFlow`和`JAX`打造的先进的机器学习工具。
> `Transformer`提供了可以轻松地下载并且训练先进的预训练模型的API和工具。


这些模型支持不同模态中的常见任务，如：
- 自然语言处理：
  > 文本分类、命名实体识别、问答、语言建模、摘要信息、文本翻译、多项选择和文本生成。
- 机器视觉：
  > 图像分类、目标检测和语义分割。
- 音频：
  > 自然语音识别和音频分类。
- 多模态：
  > 表格问答、光学字符识别、从扫描文档提取信息、视频分类和视觉问答。


API主要类别：`configuration`(配置)、`model`(模型)、`tokenizer`(分词器)和`pipeline`(流水线）这几个重要的类。


### 环境准备

- 安装命令
  ```bash
  pip install transformers datasets evaluate accelerate
  ```

### Pipeline任务

- 参考文档：https://huggingface.co/docs/transformers/v4.41.3/zh/main_classes/pipelines

- 任务列表

    | **任务**     | **描述**                                                   | **模态**        | **Pipeline**                                  |
    | ---         | ---                                                        | -------------  | ------------------------------------------    |
    | 文本分类     | 为给定的文本序列分配一个标签                               | NLP             | pipeline(task=“sentiment-analysis”)           |
    | 文本生成     | 根据给定的提示生成文本                                     | NLP             | pipeline(task=“text-generation”)              |
    | 命名实体识别 | 为序列里的每个 token 分配一个标签（人, 组织, 地址等等）    | NLP             | pipeline(task=“ner”)                          |
    | 问答系统     | 通过给定的上下文和问题, 在文本中提取答案                   | NLP             | pipeline(task=“question-answering”)           |
    | 掩盖填充     | 预测出正确的在序列中被掩盖的token                          | NLP             | pipeline(task=“fill-mask”)                    |
    | 文本摘要     | 为文本序列或文档生成总结                                   | NLP             | pipeline(task=“summarization”)                |
    | 文本翻译     | 将文本从一种语言翻译为另一种语言                           | NLP             | pipeline(task=“translation”)                  |
    | 图像分类     | 为图像分配一个标签                                         | Computer vision | pipeline(task=“image-classification”)         |
    | 图像分割     | 为图像中每个独立的像素分配标签（支持语义、全景和实例分割） | Computer vision | pipeline(task=“image-segmentation”)           |
    | 目标检测     | 预测图像中目标对象的边界框和类别                           | Computer vision | pipeline(task=“object-detection”)             |
    | 音频分类     | 给音频文件分配一个标签                                     | Audio           | pipeline(task=“audio-classification”)         |
    | 自动语音识别 | 将音频文件中的语音提取为文本                               | Audio           | pipeline(task=“automatic-speech-recognition”) |
    | 视觉问答     | 给定一个图像和一个问题，正确地回答有关图像的问题           | Multimodal      | pipeline(task=“vqa”)                          |



