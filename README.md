🖼️ Baidu Image Screenshot Bot

一个能自动点击百度图片搜索结果，并批量截图保存的大图爬取工具。

---

💡 项目简介

你想获取百度图片搜索结果中的**高清图**？  
你想截图“点击后弹出的那张大图”而不是小缩略图？  
你不想自己点图、切图、截图？

这个项目就是为你设计的。

- 🔍 支持自定义搜索关键词（例如：张韶涵、赵丽颖、猫猫狗狗…）
- 📸 支持打开每一张图的大图预览，并系统级截图（不是浏览器截图！）
- 🔄 支持自动关闭 tab、回到主页面、继续点击下一张
- ✅ 实现了**网页结构的递推建模**（ul[i]/li[j]）
- 🧠 项目设计过程中参考了数学归纳法的思想

---

🚀 快速演示

| 点击第一张图 | 自动截图 | 关闭页面再点第二张图 |
|--------------|----------|------------------------|
| ✅            | ✅        | ✅                      |

（你可以在 `real_screenshots/` 中看到截图示例）

---

📦 安装依赖

```bash
pip install -r requirements.txt

依赖包括：
selenium
pyautogui

💻 如何运行
bash：python request.py
运行后将自动：

打开百度图片

点击前 N 张图（当前默认 3 张）

每次截图并保存为：image_1.png, image_2.png...

✨ 核心亮点
系统级截图：使用 PyAutoGUI，而非浏览器截图，不会错过弹窗、图层、大图！

XPath 控制结构：通过 ul[i]/li[1] 精准定位任意列图像，实现稳定结构化访问。

操作真实可见图：模拟用户行为，准确还原“你点我图，我截你看的”全过程。

📁 文件结构
bash：
📁 real_screenshots/       # 自动保存的截图
📄 request.py              # 主程序
📄 README.md               # 你正在看的说明文档

🧠 关于归纳法建模
百度图片的搜索结果布局并不是线性列表，而是“列状 ul + 行状 li 的瀑布流结构”。
本项目通过观察第一张图与第二张图的 XPath 差异，归纳出结构：

css：
ul[i]/li[j]/.../img
因此我们得以从任意列中递推出其结构，控制点击目标。
这就是一个基于数学归纳思想的真实网页行为模型设计。

🤝 欢迎贡献 & 点赞
如果你觉得这个项目对你有用，请点个 ⭐Star！
或者你有任何想要批量采图的关键词，也欢迎提交 PR / Issues ！
