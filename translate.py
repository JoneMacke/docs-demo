# -*- coding: utf-8 -*-
import os, re

root = r'd:\my-docs\docs-demo'

# Translation mappings for common Chinese text
translations = {
    # Frontmatter
    '接口示例': 'API Examples',
    '应用设置': 'App Config',
    '代码配置': 'Code Config',
    
    # Section headers and common phrases
    '软件信息': 'Software Info',
    '官方网站': 'Official Website',
    '支持平台': 'Supported Platforms',
    '视频教程': 'Video Tutorial',
    '配置步骤': 'Configuration Steps',
    '注意事项': 'Notes',
    '图文教程': 'Step-by-Step Guide',
    '点击跳转': 'Click to visit',
    '您的浏览器不支持视频播放。': 'Your browser does not support video playback.',
    '填入您的令牌/密钥': 'Enter your token/key',
    '填入您的密钥': 'Enter your key',
}

def translate_content(content, source_path):
    """Translate Chinese content to English while preserving structure"""
    # Fix frontmatter links: /guide/ -> /en/guide/
    content = re.sub(r"link:\s*'/guide/", "link: '/en/guide/", content)
    
    # Translate common frontmatter text
    content = content.replace("text: '接口示例'", "text: 'API Examples'")
    content = content.replace("text: '应用设置'", "text: 'App Config'")
    content = content.replace("text: '代码配置'", "text: 'Code Config'")
    
    # Translate prev/next links for apps
    app_names = {
        'BotGem': 'BotGem', 'Chatbox': 'Chatbox', 'Cherry Studio': 'Cherry Studio',
        'SillyTavern': 'SillyTavern', 'RikkaHub': 'RikkaHub', 'Tavo': 'Tavo',
        'DreamLove': 'DreamLove', 'Kelivo': 'Kelivo', 'Omate': 'Omate',
        'Operit AI': 'Operit AI', 'Prompt Optimizer': 'Prompt Optimizer',
        '小手记': 'XiaoShouJi', '小溢': 'XiaoYi',
    }
    
    # Translate section headers
    content = content.replace('## 📹 视频教程', '## 📹 Video Tutorial')
    content = content.replace('## 📝 配置步骤', '## 📝 Configuration Steps')
    content = content.replace('## 📸 图文教程', '## 📸 Step-by-Step Guide')
    
    # Translate info boxes
    content = re.sub(r'::: info 软件信息', '::: info Software Info', content)
    content = re.sub(r'::: warning 注意事项', '::: warning Notes', content)
    content = re.sub(r'::: warning ⚠️ 注意', '::: warning ⚠️ Note', content)
    content = re.sub(r'::: danger 🔐 安全提醒', '::: danger 🔐 Security Warning', content)
    content = re.sub(r'::: danger 🔐 密钥安全', '::: danger 🔐 Key Security', content)
    content = re.sub(r'::: tip 💡 说明', '::: tip 💡 Description', content)
    content = re.sub(r'::: tip 💡 小贴士', '::: tip 💡 Tips', content)
    content = re.sub(r'::: tip 📝 其他提示', '::: tip 📝 Other Tips', content)
    content = re.sub(r'::: tip 🎯 使用建议', '::: tip 🎯 Usage Tips', content)
    content = re.sub(r'::: info 💡 提示', '::: info 💡 Tips', content)
    content = re.sub(r'::: info 🧩 角色说明', '::: info 🧩 Role Description', content)
    content = re.sub(r'::: info 📦 前置要求', '::: info 📦 Prerequisites', content)
    
    # Translate common labels
    content = content.replace('**官方网站：**', '**Official Website:**')
    content = content.replace('**支持平台：**', '**Supported Platforms:**')
    content = content.replace('（点击跳转）', '(Click to visit)')
    content = content.replace('(点击跳转)', '(Click to visit)')
    content = content.replace('您的浏览器不支持视频播放。', 'Your browser does not support video playback.')
    
    # Translate step labels
    content = re.sub(r'### 步骤 (\d+)：(.+)', lambda m: f'### Step {m.group(1)}: {translate_step(m.group(2))}', content)
    
    # Translate back link
    content = re.sub(r'← 返回接口示例', '← Back to API Examples', content)
    content = re.sub(r'← 返回应用设置', '← Back to App Config', content)
    content = re.sub(r'← 返回代码配置', '← Back to Code Config', content)
    
    # Fix href links in back buttons
    content = content.replace('href="/guide/', 'href="/en/guide/')
    
    return content

def translate_step(text):
    """Translate step descriptions"""
    step_map = {
        '打开设置': 'Open Settings',
        '选择服务商': 'Select Provider',
        '添加服务商': 'Add Provider',
        '选择添加': 'Select Add',
        '填写配置信息': 'Fill in Configuration',
        '填写服务商信息': 'Fill in Provider Info',
        '获取并添加模型': 'Fetch and Add Models',
        '选择模型': 'Select Model',
        '保存配置信息': 'Save Configuration',
        '完成配置': 'Complete Configuration',
        '自行填写名称': 'Enter a Custom Name',
        '填写配置要素': 'Fill in Configuration Details',
        '自动获取添加模型': 'Auto-Fetch and Add Models',
        '手动添加模型': 'Manually Add Model',
        '选择自己添加的模型': 'Select Your Added Model',
        '添加配置': 'Add Configuration',
        '填写接口信息': 'Fill in API Info',
        '获取模型列表': 'Fetch Model List',
        '开始聊天': 'Start Chatting',
        '添加提供商': 'Add Provider',
        '配置接口': 'Configure API',
        '保存并使用': 'Save and Use',
    }
    return step_map.get(text.strip(), text)

def translate_file(src_path, dst_path):
    """Read source file, translate, and write to destination"""
    with open(src_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    translated = translate_content(content, src_path)
    
    os.makedirs(os.path.dirname(dst_path), exist_ok=True)
    with open(dst_path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(translated)
    
    print(f'Created: {dst_path}')

# Process all missing directories
dirs_to_translate = ['api-notes', 'apps', 'code']

for subdir in dirs_to_translate:
    src_dir = os.path.join(root, 'guide', subdir)
    dst_dir = os.path.join(root, 'en', 'guide', subdir)
    
    if not os.path.exists(src_dir):
        continue
    
    for fname in sorted(os.listdir(src_dir)):
        if fname.endswith('.md'):
            src_path = os.path.join(src_dir, fname)
            dst_path = os.path.join(dst_dir, fname)
            translate_file(src_path, dst_path)

print('\nDone! All English translation files created.')
