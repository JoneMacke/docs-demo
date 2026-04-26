---
sidebar: false
prev:
  text: 'Easydict'
  link: '/en/guide/code/easydict'
next:
  text: 'Code Settings'
  link: '/en/guide/code-config'
---

# 🐍 Python SDK

<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 20px 24px; border-radius: 12px; color: white; margin-bottom: 24px;">
  <p style="margin: 0; font-size: 16px;">MapleAI Python SDK for Python developers to quickly integrate. Compatible with the OpenAI SDK format, ready to use out of the box.</p>
</div>

## 📦 Installation

::: code-group
```bash [pip]
pip install maple-ai-sdk
```
```bash [pip (China mirror)]
pip install maple-ai-sdk -i https://pypi.tuna.tsinghua.edu.cn/simple
```
:::

---

## 🚀 Basic Call Example

> The simplest way to call the API, suitable for quick start.

```python
from openai import OpenAI

# Initialize client
client = OpenAI(
    api_key="sk-xxxxxxxx",              # Enter your token
    base_url="https://ai.katioai.com/v1" # Enter the actual API address
)

# Send request
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

## 🎬 Video Analysis

> Analyze video content by extracting key frames and using a vision model.

::: details Click to expand full code
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
            raise FileNotFoundError(f"❌ Video file not found: {video_path}")
        
    def get_metadata(self):
        """1. Get basic video technical parameters"""
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
        """2. Extract key frames for AI analysis"""
        print("📸 Extracting key frames...")
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
        print(f"✅ Successfully extracted {len(base64_frames)} key frames")
        return base64_frames

    def analyze_content_with_ai(self, api_key, base64_frames):
        """3. Call vision model to analyze video content"""
        print("🧠 Requesting AI analysis of video content...")
        
        url = "https://ai.katioai.com/v1/chat/completions"
        
        content_payload = [
            {"type": "text", "text": "These are several frames extracted in chronological order from the same video. Please describe in detail what happens in this video, including the scene, character actions, atmosphere, and main events."}
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
            
            print("\n📝 Video Analysis Report:\n" + "="*30)
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
            print(f"❌ Analysis failed: {e}")
            return None

# Usage example
if __name__ == "__main__":
    video_file = r"your_video_file_path.mp4"  # Replace with your video file path
    my_api_key = "sk-xxxxxxxx"  # Replace with your API Key
    
    if not os.path.exists(video_file):
        print(f"⚠️ {video_file} not found, please prepare a video file first.")
    else:
        analyzer = VideoAnalyzer(video_file)
        meta = analyzer.get_metadata()
        print(f"\n📊 Video Metadata: {meta}")
        frames = analyzer.extract_keyframes(max_frames=5)
        if frames:
            analyzer.analyze_content_with_ai(my_api_key, frames)
```
:::

---

## 🖼️ Image Analysis

> Use a vision model to describe and analyze local images.

::: details Click to expand full code
```python
import requests, json, base64

API_URL = "https://ai.katioai.com/v1/chat/completions"
API_KEY = "Bearer sk-xxxxxxxx"  # Replace with your API Key

def analyze_image(img_path):
    """Analyze image"""
    with open(img_path, "rb") as f:
        img_base64 = base64.b64encode(f.read()).decode()
    
    payload = {
        "model": "gemini-3-pro-preview",  # Model name
        "messages": [{
            "role": "user",
            "content": [
                {"type": "text", "text": "Please describe this image"},
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

# Usage example
analyze_image(r"your_image_path.jpg")  # Replace with actual image path
```
:::

---

## 🎥 Video Generation

> Generate video content using AI models, with retry mechanism and streaming output.

::: details Click to expand full code
```python
import requests
import time
import json
import os

def generate_video_stream_with_retry(prompt, api_key, max_retries=3):
    """Streaming video generation with retry mechanism"""
    base_url = "https://ai.katioai.com/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "veo_3_1",
        "messages": [
            {
                "role": "user",
                "content": f"Please help me generate a video with the description: {prompt}. Please tell me the video generation steps or provide a video link directly."
            }
        ],
        "max_tokens": 5000,
        "temperature": 0.7,
        "stream": True
    }

    for attempt in range(max_retries):
        print(f"\n🔄 Attempt {attempt + 1}/{max_retries}...")
        full_content = ""
        
        try:
            response = requests.post(base_url, headers=headers, json=payload, timeout=120, stream=True)
            
            if response.status_code != 200:
                print(f"❌ Request failed, status code: {response.status_code}")
                if 500 <= response.status_code < 600:
                    print("⏳ Server error, waiting before retry...")
                    time.sleep(5)
                    continue
                else:
                    return None

            print("✅ Connection successful, receiving data stream...\n")
            print("-" * 30)

            for line in response.iter_lines():
                if line:
                    decoded_line = line.decode('utf-8')
                    if decoded_line.startswith('data: '):
                        data_str = decoded_line[6:]
                        if data_str.strip() == '[DONE]':
                            print("\n" + "-" * 30)
                            print("\n✅ Streaming complete")
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
                print(f"📝 Full response saved to ai_response.txt")
                return full_content
            else:
                print("⚠️ No content received")
                return None

        except requests.exceptions.Timeout:
            print("⏰ Connection timed out")
            time.sleep(5)
            continue
        except Exception as e:
            print(f"❌ Unknown error: {e}")
            return None

    print(f"😞 Failed after {max_retries} attempts")
    return None

# Usage example
if __name__ == "__main__":
    my_api_key = "sk-xxxxxxxx"  # Replace with your API Key
    
    result = generate_video_stream_with_retry(
        prompt="A dog surfing in the ocean",
        api_key=my_api_key,
        max_retries=5
    )
    
    if result:
        print("\n🎬 Task complete")
    else:
        print("\n❌ Task failed")
```
:::

---

## 🎨 Image Generation

> Generate images from text descriptions, automatically extracting returned image links.

::: details Click to expand full code
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
        self.api_key = "sk-xxxxxxxx"  # Replace with your API key
        self.api_url = "https://ai.katioai.com/v1/chat/completions"
        self.model = "nano-banana"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
    def generate_image(self, prompt: str, save_dir: str = "./generated_images") -> Dict[str, Any]:
        """Generate image and return image links"""
        Path(save_dir).mkdir(parents=True, exist_ok=True)
        
        payload = {
            "model": self.model,
            "messages": [{"role": "user", "content": f"Generate an image based on this prompt: {prompt}"}],
            "max_tokens": 1000
        }
        
        print(f"Generating image...")
        print(f"Prompt: {prompt}")
        
        try:
            response = requests.post(self.api_url, headers=self.headers, json=payload, timeout=600)
            
            if response.status_code == 200:
                return self._process_response(response, prompt, save_dir)
            else:
                print(f"API request failed: {response.status_code}")
                return {"success": False, "error": f"HTTP {response.status_code}", "image_links": []}
                
        except requests.exceptions.RequestException as e:
            print(f"Request exception: {e}")
            return {"success": False, "error": str(e), "image_links": []}
    
    def _process_response(self, response, prompt, save_dir):
        result = {"success": False, "image_links": [], "content": "", "error": None}
        
        try:
            response_data = response.json()
            if "choices" in response_data and response_data["choices"]:
                content = response_data["choices"][0]["message"]["content"]
                result["content"] = content
                print(f"API response content: {content}")
                
                # Extract image links
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
                    print(f"Found image links: {found_links}")
                else:
                    result["success"] = True
                    result["note"] = "API returned text description, no image links found"
                    
        except Exception as e:
            result["error"] = f"Failed to process response: {e}"
        
        return result

def main():
    print("🎨 Image Generation Script")
    print("-" * 50)
    
    generator = ImageGenerator()
    prompt = "A cute puppy playing in the garden"  # Modify this prompt as needed
    
    result = generator.generate_image(prompt=prompt, save_dir="./test_images")
    
    print("\n" + "=" * 50)
    if result.get("success", False):
        print("✅ Request successful!")
        if result.get("image_links"):
            print(f"\n📷 Found {len(result['image_links'])} image link(s):")
            for i, link in enumerate(result["image_links"], 1):
                print(f"  {i}. {link}")
    else:
        print(f"❌ Generation failed: {result.get('error', 'Unknown error')}")

if __name__ == "__main__":
    main()
```
:::

---

## 👁️ Image Recognition

> To send images for recognition, use the model `gemini-2.5-flash-image-preview` and follow the standard OpenAI Vision format.

```python
from openai import OpenAI
import base64

# Initialize client
client = OpenAI(
    api_key="sk-xxxxxxxx",                # Enter your token
    base_url="https://ai.katioai.com/v1"  # Enter the actual API address
)

# Read local image and encode to base64
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

image_base64 = encode_image("your_image.jpg")  # Replace with actual image path

# Send image recognition request
response = client.chat.completions.create(
    model="gemini-2.5-flash-image-preview",  # Dedicated image recognition model
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Please describe the content of this image"},
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

::: tip 💡 Tip
For image recognition, be sure to use the `gemini-2.5-flash-image-preview` model. This model is specifically optimized for image understanding and supports the standard OpenAI Vision API format.
:::
