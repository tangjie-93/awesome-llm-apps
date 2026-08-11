This is a [Next.js](https://nextjs.org) project bootstrapped with [`create-next-app`](https://nextjs.org/docs/app/api-reference/cli/create-next-app).
这是一个使用 [`create-next-app`](https://nextjs.org/docs/app/api-reference/cli/create-next-app) 引导创建的 [Next.js](https://nextjs.org) 项目。

## Setup
## 设置

1. **Install dependencies:**
1. **安装依赖：**
   ```bash
   pnpm install
   ```

2. **Configure environment:**
2. **配置环境：**
   ```bash
   cp .env.example .env.local
   ```

   Update `.env.local` with your database credentials if needed.
   如有需要，请使用你的数据库凭据更新 `.env.local`。

3. **Setup database:**
3. **设置数据库：**
   ```bash
   pnpm prisma generate
   pnpm prisma db push
   ```

## Getting Started
## 开始使用

First, run the development server:
首先，运行开发服务器：

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.
用浏览器打开 [http://localhost:3000](http://localhost:3000) 查看结果。

You can start editing the page by modifying `app/page.tsx`. The page auto-updates as you edit the file.
你可以通过修改 `app/page.tsx` 开始编辑页面；页面会在你编辑文件时自动更新。

This project uses [`next/font`](https://nextjs.org/docs/app/building-your-application/optimizing/fonts) to automatically optimize and load [Geist](https://vercel.com/font), a new font family for Vercel.
该项目使用 [`next/font`](https://nextjs.org/docs/app/building-your-application/optimizing/fonts) 自动优化并加载 [Geist](https://vercel.com/font)，这是 `Vercel` 的新字体系列。

## Learn More
## 了解更多

To learn more about Next.js, take a look at the following resources:
要进一步了解 `Next.js`，请查看以下资源：

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Next.js 文档](https://nextjs.org/docs) - 了解 `Next.js` 功能和 `API`。
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.
- [学习 Next.js](https://nextjs.org/learn) - 一个交互式 `Next.js` 教程。

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js) - your feedback and contributions are welcome!
你也可以查看 [Next.js GitHub 仓库](https://github.com/vercel/next.js)，欢迎反馈和贡献。

## Deploy on Vercel
## 部署到 Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.
部署 `Next.js` 应用最简单的方式，是使用 `Next.js` 创建者提供的 [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme)。

Check out our [Next.js deployment documentation](https://nextjs.org/docs/app/building-your-application/deploying) for more details.
更多细节请查看我们的 [Next.js 部署文档](https://nextjs.org/docs/app/building-your-application/deploying)。
