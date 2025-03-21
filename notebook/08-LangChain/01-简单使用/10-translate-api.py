# -*- coding:utf-8 -*-
import os

from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from fastapi import FastAPI
from langserve import add_routes
# import uvicorn

# 定义模板
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "请将以下内容翻译为{language}"),
        ("user", "{text}")
    ]
)

# 定义模型
model_name = 'qwen2.5:1.5b'
ollama_base_url = os.environ.get("OLLAMA_API_BASE")

model = init_chat_model(model=model_name, model_provider="ollama", base_url=ollama_base_url)

# 定义parser
str_parser = StrOutputParser()

# 定义链
chain = prompt_template | model | str_parser


app = FastAPI()


@app.get("/")
def index():
    return {"message": "Hello, World!"}


@app.post("/translate")
def translate(text: str, language: str = "中文"):
    if text:
        data = {"language": language, "text": text}
        result = chain.invoke(data)
        return result
    else:
        msg = "请传递text内容"
        return msg


# 利用langserve
add_routes(
    app,
    chain,
    path="/chain"
)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
