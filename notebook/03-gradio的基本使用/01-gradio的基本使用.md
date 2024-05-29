## Gradio的基本使用

- 参考文档

  - https://www.gradio.app/docs
  - https://www.gradio.app/playground

- 安装：

  ```bash
  pip install gradio
  ```



### 基本介绍

> Gradio是一个开源Python包，允许您为机器学习模型、API或任何任意Python函数快速构建演示或Web应用程序。然后，您可以使用Gradio的内置共享功能在几秒钟内共享演示或Web应用程序的链接。没有JavaScript，CSS，或网页寄存的经验需要！
>
> 只需要几行Python代码即可构建一个漂亮的界面。



### 第一个应用

- 代码：

  ```python
  import gradio as gr
  
  def greet(name, intensity):
      return "Hello, " + name + "!" * int(intensity)
  
  demo = gr.Interface(
      fn=greet,
      inputs=["text", "slider"],
      outputs=["text"],
  )
  
  demo.launch()
  ```

