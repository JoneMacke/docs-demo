# 📚 VitePress 文档站点

基于 **VitePress 1.6.4** 构建的静态文档网站，支持中英文双语、自定义主题和组件，无后端依赖。

- 🔗 GitHub 仓库：[JoneMacke/docs-demo](https://github.com/JoneMacke/docs-demo)

---

## 📋 目录

- [本地开发](#本地开发)
- [部署方式](#部署方式)
  - [方式 1：Vercel 部署](#方式-1vercel-部署)
  - [方式 2：宝塔面板部署](#方式-2宝塔面板部署)
  - [方式 3：通用服务器部署](#方式-3通用服务器部署)
- [一键自动更新脚本](#一键自动更新脚本)
- [日常更新流程](#日常更新流程)
- [常见问题与优化](#常见问题与优化)

---

## 本地开发

### 前置要求

- [Node.js](https://nodejs.org/) 18+
- [pnpm](https://pnpm.io/installation)

### 快速开始

```bash
# 安装依赖
pnpm install

# 启动开发服务器
pnpm docs:dev

# 构建项目
pnpm docs:build
```

---

## 部署方式

### 方式 1：Vercel 部署

1. 将项目推送到 GitHub
2. 在 [Vercel](https://vercel.com) 中导入项目
3. 配置构建设置：
   - **框架预设**：选择「其它」
   - **构建命令**：`pnpm docs:build`
   - **输出目录**：`.vitepress/dist`
   - **安装命令**：`pnpm install`
4. 点击部署，等待完成
5. 访问分配的 Vercel 域名即可查看文档站点

---

### 方式 2：宝塔面板部署

1. **创建站点**
   - 登录宝塔面板 → 网站 → 添加站点
   - 填写域名、根目录设为 `/www/wwwroot/docs.example.com/.vitepress/dist`
   - 安装 Nginx 环境

2. **克隆项目**
   ```bash
   cd /www/wwwroot/docs.example.com
   git clone https://github.com/JoneMacke/docs-demo.git .
   ```

3. **安装依赖并构建**
   ```bash
   pnpm install
   pnpm run docs:build
   ```

4. **Nginx 伪静态配置**（必须，否则刷新会 404）
   ```nginx
   location / {
     try_files $uri $uri/ /index.html;
   }
   ```

---

### 方式 3：通用服务器部署

1. **准备目录并克隆**
   ```bash
   mkdir -p /var/www/docs.example.com
   cd /var/www/docs.example.com
   git clone https://github.com/JoneMacke/docs-demo.git .
   ```

2. **安装依赖并构建**
   ```bash
   pnpm install
   pnpm run docs:build
   ```

3. **Nginx 配置**
   ```nginx
   server {
       listen 80;
       server_name docs.example.com;
       root /var/www/docs.example.com/.vitepress/dist;
       index index.html;

       location / {
           try_files $uri $uri/ /index.html;
       }
   }
   ```

4. **重启 Nginx**
   ```bash
   systemctl restart nginx
   ```

---

## 一键自动更新脚本

项目根目录内置 `update.sh` 脚本，可自动拉取最新代码、安装依赖并重新构建。由于 Nginx root 已指向 `.vitepress/dist`，构建完成后无需额外复制文件。

### 创建脚本（如未创建）

```bash
cat > update.sh << 'EOF'
#!/bin/bash
echo "====================================="
echo "       开始自动更新文档网站"
echo "====================================="
echo ""
echo "1/3 拉取最新代码..."
git pull
echo ""
echo "2/3 安装依赖..."
pnpm install
echo ""
echo "3/3 开始构建..."
pnpm run docs:build
echo ""
echo "====================================="
echo "        ✅ 更新完成！"
echo "====================================="
EOF

chmod +x update.sh
```

---

## 日常更新流程

无论使用哪种部署方式（宝塔/通用服务器），更新步骤都一样：

1. **本地修改** → 提交并推送到 GitHub
2. **服务器执行更新**
   ```bash
   ./update.sh
   ```
3. **刷新浏览器** → 即可看到最新内容

---

## 常见问题与优化

### 刷新页面 404

- **原因**：缺少 Nginx 伪静态配置
- **解决**：添加 `try_files $uri $uri/ /index.html;` 规则

### 视频加载慢

- 建议开启 CDN 缓存，并在 Nginx 中添加：
  ```nginx
  location ~* \.(mp4|webm|ogg)$ {
      expires 30d;
      access_log off;
  }
  ```

### 脚本执行报错

- **`git pull` 报错**：检查仓库是否正确克隆，或重新 `git clone`
- **构建失败**：确认 `pnpm install` 已执行且依赖完整

---

## 作者

GitHub：[JoneMacke](https://github.com/JoneMacke)

欢迎反馈和贡献 🎉
