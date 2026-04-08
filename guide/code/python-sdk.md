---
sidebar: false
prev:
  text: 'Easydict'
  link: '/guide/code/easydict'
next:
  text: '代码设置'
  link: '/guide/code-config'
---

# 🐍 Python SDK

<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 20px 24px; border-radius: 12px; color: white; margin-bottom: 24px;">
  <p style="margin: 0; font-size: 16px;">枫叶AI Python SDK，方便 Python 开发者快速集成。兼容 OpenAI SDK 格式，开箱即用。</p>
</div>

## 📦 安装

::: code-group
```bash [pip]
pip install maple-ai-sdk
```
```bash [pip (国内镜像)]
pip install maple-ai-sdk -i https://pypi.tuna.tsinghua.edu.cn/simple
```
:::

---

## 🚀 基础调用示例

> 最简单的调用方式，适合快速上手。

```python
from openai import OpenAI

# 初始化客户端
client = OpenAI(
    api_key="sk-xxxxxxxx",              # 填入您的令牌
    base_url="https://api.katioai.com/v1" # 填入实际的API 地址
)

# 发送请求
response = client.chat.completions.create(
    model="gemini-2.5-pro",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello!"}
    ],
    stream=False
)

print(response.choices[0].message.content)
```

---

## 🎬 视频分析

> 通过抽取视频关键帧，利用视觉大模型分析视频内容。

::: details 点击展开完整代码
```python
import cv2
import base64
import requests
import os
import math

class VideoAnalyzer:
    def __init__(self, video_path):
        self.video_path = video_path
        if not os.path.exists(video_path):
            raise FileNotFoundError(f"❌ 找不到视频文件: {video_path}")
        
    def get_metadata(self):
        """1. 获取视频基础技术参数"""
        cap = cv2.VideoCapture(self.video_path)
        
        if not cap.isOpened():
            return None

        fps = cap.get(cv2.CAP_PROP_FPS)
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        duration = frame_count / fps if fps > 0 else 0
        
        cap.release()
        
        return {
            "width": width,
            "height": height,
            "fps": round(fps, 2),
            "frame_count": frame_count,
            "duration_sec": round(duration, 2),
            "file_size_mb": round(os.path.getsize(self.video_path) / (1024 * 1024), 2)
        }

    def extract_keyframes(self, max_frames=5, target_width=512):
        """2. 抽取关键帧用于AI分析"""
        print("📸 正在抽取关键帧...")
        cap = cv2.VideoCapture(self.video_path)
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        
        if total_frames == 0:
            return []
            
        interval = max(1, total_frames // max_frames)
        base64_frames = []
        
        for i in range(0, total_frames, interval):
            if len(base64_frames) >= max_frames:
                break
                
            cap.set(cv2.CAP_PROP_POS_FRAMES, i)
            ret, frame = cap.read()
            
            if ret:
                h, w, _ = frame.shape
                aspect_ratio = h / w
                new_height = int(target_width * aspect_ratio)
                resized_frame = cv2.resize(frame, (target_width, new_height))
                
                _, buffer = cv2.imencode('.jpg', resized_frame)
                
                base64_str = base64.b64encode(buffer).decode('utf-8')
                base64_frames.append(base64_str)
        
        cap.release()
        print(f"✅ 成功抽取 {len(base64_frames)} 帧关键画面")
        return base64_frames

    def analyze_content_with_ai(self, api_key, base64_frames):
        """3. 调用视觉大模型解析视频内容"""
        print("🧠 正在请求 AI 分析视频内容...")
        
        url = "https://api.katioai.com/v1/chat/completions"
        
        content_payload = [
            {"type": "text", "text": "这是同一个视频中按时间顺序抽取的几帧画面。请详细描述这个视频里发生了什么？包括场景、人物动作、氛围和主要事件。"}
        ]
        
        for b64 in base64_frames:
            content_payload.append({
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{b64}",
                    "detail": "low"
                }
            })

        payload = {
            "model": "gemini-3-pro-preview", 
            "messages": [{"role": "user", "content": content_payload}],
            "max_tokens": 1000,
            "stream": True
        }

        try:
            response = requests.post(url, headers={"Authorization": f"Bearer {api_key}"}, json=payload, stream=True)
            
            print("\n📝 视频分析报告:\n" + "="*30)
            full_analysis = ""
            
            for line in response.iter_lines():
                if line:
                    decoded = line.decode('utf-8')
                    if decoded.startswith('data: ') and decoded != 'data: [DONE]':
                        try:
                            chunk = decoded[6:]
                            import json
                            delta = json.loads(chunk)['choices'][0]['delta'].get('content', '')
                            print(delta, end='', flush=True)
                            full_analysis += delta
                        except:
                            pass
            
            print("\n" + "="*30)
            return full_analysis
            
        except Exception as e:
            print(f"❌ 分析失败: {e}")
            return None

# 使用示例
if __name__ == "__main__":
    video_file = r"你的视频文件路径.mp4"  # 替换为你的视频文件路径
    my_api_key = "sk-xxxxxxxx"  # 替换为你的API Key
    
    if not os.path.exists(video_file):
        print(f"⚠️ 未找到 {video_file}，请先准备一个视频文件。")
    else:
        analyzer = VideoAnalyzer(video_file)
        meta = analyzer.get_metadata()
        print(f"\n📊 视频元数据: {meta}")
        frames = analyzer.extract_keyframes(max_frames=5)
        if frames:
            analyzer.analyze_content_with_ai(my_api_key, frames)
```
:::

---

## 🖼️ 图片分析

> 使用视觉模型对本地图片进行内容描述与分析。

::: details 点击展开完整代码
```python
import requests, json, base64

API_URL = "https://api.katioai.com/v1/chat/completions"
API_KEY = "Bearer sk-xxxxxxxx"  # 替换为你的API Key

def analyze_image(img_path):
    """分析图片"""
    with open(img_path, "rb") as f:
        img_base64 = base64.b64encode(f.read()).decode()
    
    payload = {
        "model": "gemini-3-pro-preview",  # 模型名称
        "messages": [{
            "role": "user",
            "content": [
                {"type": "text", "text": "请描述这张图片"},
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/jpeg;base64,{img_base64}"}
                }
            ]
        }],
        "stream": True
    }
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": API_KEY
    }
    
    response = requests.post(API_URL, json=payload, headers=headers, stream=True)
    for line in response.iter_lines():
        if line:
            line = line.decode('utf-8').replace('data: ', '')
            if line.strip() == '[DONE]': break
            try:
                data = json.loads(line)
                if content := data['choices'][0]['delta'].get('content'):
                    print(content, end="", flush=True)
            except:
                continue
    print()

# 使用示例
analyze_image(r"你的图片路径.jpg")  # 替换为实际图片路径
```
:::

---

## 🎥 视频生成

> 利用 AI 模型生成视频内容，支持重试机制和流式输出。

::: details 点击展开完整代码
```python
import requests
import time
import json
import os

def generate_video_stream_with_retry(prompt, api_key, max_retries=3):
    """带重试机制的流式视频生成指令获取函数"""
    base_url = "https://api.katioai.com/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "veo_3_1",
        "messages": [
            {
                "role": "user",
                "content": f"请帮我生成一个视频，描述是：{prompt}。请告诉我视频生成的步骤或直接提供视频链接。"
            }
        ],
        "max_tokens": 5000,
        "temperature": 0.7,
        "stream": True
    }

    for attempt in range(max_retries):
        print(f"\n🔄 尝试 {attempt + 1}/{max_retries}...")
        full_content = ""
        
        try:
            response = requests.post(base_url, headers=headers, json=payload, timeout=120, stream=True)
            
            if response.status_code != 200:
                print(f"❌ 请求失败，状态码: {response.status_code}")
                if 500 <= response.status_code < 600:
                    print("⏳ 服务器端错误，等待后重试...")
                    time.sleep(5)
                    continue
                else:
                    return None

            print("✅ 连接成功，开始接收数据流...\n")
            print("-" * 30)

            for line in response.iter_lines():
                if line:
                    decoded_line = line.decode('utf-8')
                    if decoded_line.startswith('data: '):
                        data_str = decoded_line[6:]
                        if data_str.strip() == '[DONE]':
                            print("\n" + "-" * 30)
                            print("\n✅ 流式传输结束")
                            break
                        try:
                            data_json = json.loads(data_str)
                            delta = data_json['choices'][0]['delta'].get('content', '')
                            if delta:
                                print(delta, end='', flush=True)
                                full_content += delta
                        except json.JSONDecodeError:
                            continue
            
            if full_content:
                with open("ai_response.txt", "w", encoding="utf-8") as f:
                    f.write(full_content)
                print(f"📝 完整回复已保存到 ai_response.txt")
                return full_content
            else:
                print("⚠️ 未接收到任何内容")
                return None

        except requests.exceptions.Timeout:
            print("⏰ 连接超时")
            time.sleep(5)
            continue
        except Exception as e:
            print(f"❌ 未知错误: {e}")
            return None

    print(f"😞 经过 {max_retries} 次尝试后仍然失败")
    return None

# 使用示例
if __name__ == "__main__":
    my_api_key = "sk-xxxxxxxx"  # 替换为你的API Key
    
    result = generate_video_stream_with_retry(
        prompt="在海上冲浪的狗",
        api_key=my_api_key,
        max_retries=5
    )
    
    if result:
        print("\n🎬 任务完成")
    else:
        print("\n❌ 任务失败")
```
:::

---

## 🎨 图片生成

> 通过文字描述生成图片，自动提取返回的图片链接。

::: details 点击展开完整代码
```python
import requests
import json
import os
import re
from datetime import datetime
from pathlib import Path
from typing import Optional, Dict, Any, List
from urllib.parse import urlparse

class ImageGenerator:
    def __init__(self):
        self.api_key = "sk-xxxxxxxx"  # 替换为你的API密钥
        self.api_url = "https://api.katioai.com/v1/chat/completions"
        self.model = "nano-banana"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
    def generate_image(self, prompt: str, save_dir: str = "./generated_images") -> Dict[str, Any]:
        """生成图像并返回图片链接"""
        Path(save_dir).mkdir(parents=True, exist_ok=True)
        
        payload = {
            "model": self.model,
            "messages": [{"role": "user", "content": f"Generate an image based on this prompt: {prompt}"}],
            "max_tokens": 1000
        }
        
        print(f"正在生成图像...")
        print(f"提示词: {prompt}")
        
        try:
            response = requests.post(self.api_url, headers=self.headers, json=payload, timeout=600)
            
            if response.status_code == 200:
                return self._process_response(response, prompt, save_dir)
            else:
                print(f"API请求失败: {response.status_code}")
                return {"success": False, "error": f"HTTP {response.status_code}", "image_links": []}
                
        except requests.exceptions.RequestException as e:
            print(f"请求异常: {e}")
            return {"success": False, "error": str(e), "image_links": []}
    
    def _process_response(self, response, prompt, save_dir):
        result = {"success": False, "image_links": [], "content": "", "error": None}
        
        try:
            response_data = response.json()
            if "choices" in response_data and response_data["choices"]:
                content = response_data["choices"][0]["message"]["content"]
                result["content"] = content
                print(f"API响应内容: {content}")
                
                # 提取图片链接
                url_patterns = [
                    r'https?://[^\s]+?\.(?:jpg|jpeg|png|gif|bmp|webp)',
                    r'https?://[^\s]+?/image/[^\s]+',
                ]
                
                found_links = []
                for pattern in url_patterns:
                    matches = re.findall(pattern, content, re.IGNORECASE)
                    found_links.extend(matches)
                
                if found_links:
                    result["success"] = True
                    result["image_links"] = found_links
                    print(f"找到图片链接: {found_links}")
                else:
                    result["success"] = True
                    result["note"] = "API返回的是文本描述，未找到图片链接"
                    
        except Exception as e:
            result["error"] = f"处理响应失败: {e}"
        
        return result

def main():
    print("🎨 图像生成脚本")
    print("-" * 50)
    
    generator = ImageGenerator()
    prompt = "一只可爱的小狗在花园里玩耍"  # 修改这里的prompt内容
    
    result = generator.generate_image(prompt=prompt, save_dir="./test_images")
    
    print("\n" + "=" * 50)
    if result.get("success", False):
        print("✅ 请求成功!")
        if result.get("image_links"):
            print(f"\n📷 找到 {len(result['image_links'])} 个图片链接:")
            for i, link in enumerate(result["image_links"], 1):
                print(f"  {i}. {link}")
    else:
        print(f"❌ 生成失败: {result.get('error', '未知错误')}")

if __name__ == "__main__":
    main()
```
:::

---

## 👁️ 图片识别

> 如果需要发送图片进行识别，请使用模型 `gemini-2.5-flash-image-preview` 并参考标准 OpenAI Vision 格式。

```python
from openai import OpenAI
import base64

# 初始化客户端
client = OpenAI(
    api_key="sk-xxxxxxxx",                # 填入您的令牌
    base_url="https://api.katioai.com/v1"  # 填入实际的API 地址
)

# 读取本地图片并编码为 base64
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

image_base64 = encode_image("your_image.jpg")  # 替换为实际图片路径

# 发送图片识别请求
response = client.chat.completions.create(
    model="gemini-2.5-flash-image-preview",  # 图片识别专用模型
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "请描述这张图片的内容"},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{image_base64}"
                    }
                }
            ]
        }
    ],
    max_tokens=1000
)

print(response.choices[0].message.content)
```

::: tip 💡 提示
图片识别请务必使用 `gemini-2.5-flash-image-preview` 模型，该模型针对图片理解进行了专门优化，支持标准的 OpenAI Vision API 格式。
:::
