# docs-demo

这是一个使用 VitePress 构建的文档网站项目。

## 部署到 Vercel

### 前置要求

- 安装 [pnpm](https://pnpm.io/installation)
- 拥有 Vercel 账户

### 本地开发

1. 安装依赖：
```bash
pnpm install
```

2. 启动开发服务器：
```bash
pnpm docs:dev
```

3. 构建项目：
```bash
pnpm docs:build
```

### 部署步骤

1. 将项目推送到 GitHub
2. 在 [Vercel](https://vercel.com) 中导入项目
3. 配置构建设置：
   - **框架预设**：选择"其它"
   - **构建命令**：`pnpm docs:build`
   - **输出目录**：`.vitepress/dist`
   - **安装命令**：`pnpm install`
4. 点击部署，等待完成
5. 访问分配的 Vercel 域名即可查看文档站点

### 项目信息

- 基于 VitePress 1.6.4
- 无后端依赖，纯静态站点
- 支持中英文双语
- 自定义主题和组件

欢迎反馈和贡献。
