
## 模型下载

### 1. huggingface模型下载

```bash
# 设置mirror
export HF_ENDPOINT=https://hf-mirror.com

# 不指定local-dir就是默认的缓存位置中
huggingface-cli download --resume-download bert-base-uncased
# 下载模型到指定目录
huggingface-cli download --resume-download bert-base-uncased --local-dir ./bert-base-uncased
```
