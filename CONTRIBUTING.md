# 贡献与构建

本仓库面向第一次系统接触纯数学的读者。贡献的目标是让定义有条件、例子可复算、定理有边界、读者知道下一步学什么。

## 内容约定

1. 正文使用中文，第一次出现的关键术语给出通用英文名称。先给具体例子，再解释抽象定义。
2. 区分定义、定理、证明、直觉和类比。说明所用的域、非空性、有限性、选择公理或经典逻辑等前提。
3. “主要数学分支”是一张可扩充且相互交叉的地图，不声称存在唯一或穷尽的分类。
4. 范畴论是研究结构与结构间映射的语言，与代数、几何、拓扑、逻辑等多个方向相连。
5. 教学章节至少包含一个可独立核对的具体例子、一个带解答的练习、一个常见误解和可靠延伸资料；地图与索引页应提供清楚的分类边界和学习入口。
6. 引用优先采用原始论文、作者公开教材、大学课程或数学组织资料；只链接，不搬运受版权保护的长篇内容。
7. 修改 Markdown 源文档；在线阅读版和 Wiki 都由源文档导出。章节链接用标准 Markdown 相对链接。

## 公式写法

行内使用 `$x$`；独立公式用两行 `$$` 包围正文。公式内容与结束定界符之间不要留多余空白，含竖线的表格公式由构建器保护。代码块中的公式示例保持字面内容。

GitHub 的实际公式渲染器会拒绝 `\operatorname`。命名算子使用 `\mathop{\mathrm{Hom}}\nolimits` 这样的兼容写法，保留算子间距与侧置上下标。原生 Markdown 接口能生成数学节点，并不代表前端一定能显示；发布时还应抽查浏览器中的实际公式。

Wiki 导出器会把公式转换为 GitHub 专用数学语法，并保留与在线版对应的显式锚点。不要直接修改生成的 `.site-docs/`、`site/` 或 `.wiki-docs/`。

## 本地构建

需要 Python 3.12 或兼容版本、Node.js 22、Git。

```sh
python -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements-site.txt
npm ci --ignore-scripts
python -m unittest discover -s scripts -p 'test_*.py'
python scripts/prepare_site.py
python -m mkdocs build --strict
python scripts/check_site.py
node scripts/check_math.cjs
python scripts/check_completeness.py
python scripts/prepare_wiki.py
```

检查器会验证内部链接、锚点、静态资源、遗漏的公式定界符和每一段 MathJax 公式。数学测试只核验指定的例子，不等同于形式化验证整本书。

## 发布

`main` 的提交在 GitHub Actions 中通过检查后部署 GitHub Pages。Wiki 在网页创建首次首页后可以作为独立 Git 仓库克隆：

```sh
git clone https://github.com/CacinieP/pure-mathematics-primer.wiki.git ../pure-mathematics-primer.wiki
cp .wiki-docs/*.md ../pure-mathematics-primer.wiki/
git -C ../pure-mathematics-primer.wiki add -- '*.md'
git -C ../pure-mathematics-primer.wiki commit -m 'Sync reviewed content'
git -C ../pure-mathematics-primer.wiki push
```

复制前先确认 Wiki 工作树无未提交修改；若有人直接编辑了 Wiki，先把修改合并回源仓库。保留现有历史，不强制推送。导出的页脚记录来源提交，便于追踪。

## 许可

正文和仓库内构建工具采用 [CC BY-SA 4.0](LICENSE)。引用资料、外部链接和第三方依赖保留各自许可。
