## funasr

> ASR(自动语音识别)是`Automatic Speech Recognition`的简写。

### 参考文档
- https://github.com/modelscope/FunASR
- https://www.funasr.com/
- [FunASR README_zh.md](https://github.com/modelscope/FunASR/blob/main/README_zh.md)


### 核心功能
- `FunASR`是一个基础语音识别工具包，提供多种功能：   
  包括：语音识别(`ASR`)、语音端点检测(`VAD`)、标点恢复、语言模型、说话人验证、说话人分离和多人对话语音识别等。
  `FunASR`提供了便携的脚本和教程，支持预训练好的模型的推理和微调。

- 在[ModelScope](https://www.modelscope.cn/models?page=1&tasks=auto-speech-recognition)和[huggingface](https://huggingface.co/funasr)可下载器发布的模型
- 代表性的[Paraformer](https://www.modelscope.cn/models/iic/speech_paraformer-large_asr_nat-zh-cn-16k-common-vocab8404-pytorch/summary)
  非自回归端到端语音识别模型具有高精度、高效率、便携部署的优点，支持快速语音识别服务。

### 安装教程
在安装之前，请先安装好：`python>=3.8`、`torch>=1.3`、`torchaudio`

- pip 安装
  ```bash
  pip install -U funasr
  ```

- 如果需要使用工业预训练模型：安装`modelscope`与`huggingface_hub`
  ```bash
  pip install -U modelscope huggingface huggingface_hub
  ```

