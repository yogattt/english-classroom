# 课堂课件资料库

目录首页：https://yogattt.github.io/english-classroom/

当前课件：

- [美，是一种抵抗 ·《短文两篇》联读](https://yogattt.github.io/english-classroom/papers/meishi-dikang/)

- [2026年秋季九年级英语练习（一）](https://yogattt.github.io/english-classroom/papers/grade9-english-2026-autumn-01/)
- [2027届高考英语 建议信写作](https://yogattt.github.io/english-classroom/papers/gaokao-2027-advice-letter/)

## 仓库结构

```text
index.html                         生成的课件目录首页
papers.json                        全部课件元数据，目录的唯一数据来源
papers/
  grade9-english-2026-autumn-01/
    index.html                     独立课件，图片内嵌，支持离线使用
    README.md                      本份课件的内容范围及备注
tools/
  build_catalog.py                 目录生成器，仅需 Python 3 标准库
  catalog.template.html            目录首页模板
.nojekyll                          直接发布静态文件
```

## 新增一份卷子

1. 在独立 Git worktree 的功能分支中工作。
2. 创建永久 ID 对应的目录，例如 `papers/grade9-english-2026-autumn-02/`，放入独立的 `index.html` 和课件说明。每份 HTML 内嵌所需图片，不依赖网络。
3. 在 `papers.json` 的 `papers` 数组中追加一条记录，使用新的唯一 `id`，填写标题、学科、年级、学期、收录日期、内容范围、题型等信息。
4. 运行 `python3 tools/build_catalog.py`。生成器会检查重复 ID、字段、日期和本地文件路径，再把目录数据嵌入首页。
5. 本地打开首页，检查搜索、筛选、课件入口与离线下载；提交并发布课件文件、`papers.json` 及重新生成的 `index.html`。GitHub Pages 从 `main` 分支根目录自动部署。

不要复用其他卷子的 ID 或覆盖旧课件。对同一份卷子做更正时可更新原路径；新增卷子则新建目录，保证已分享链接持续可用。`addedOn` 表示收录日期，并非考试日期。

目录首页的 JavaScript 直接读取已嵌入的数据，不使用 fetch，因此把整个仓库下载到本地后，目录也能用 file:// 打开。只下载单份课件时，授课功能同样可离线使用；返回目录需要保留目录结构或访问在线首页。

## 元数据格式

```json
{
  "id": "grade9-english-2026-autumn-02",
  "title": "新卷子的标题",
  "subject": "英语",
  "grade": "九年级",
  "term": "2026年秋季",
  "addedOn": "2026-10-15",
  "description": "主要语篇与教学内容简介。",
  "scope": "说明实际包含的页码和题号，避免把部分页面标成整卷。",
  "unitCount": 8,
  "exerciseCount": 50,
  "hasWriting": true,
  "tags": ["阅读理解", "作文"],
  "href": "papers/grade9-english-2026-autumn-02/index.html"
}
```

目录支持标题／内容／题型搜索、学科和年级筛选，以及收录日期或标题排序。每份课件有固定地址，也提供下载入口。

## 当前课件备注

2026年秋季九年级英语练习（一）实际包含所附原卷第3—8页，第28—77题与书面表达，共八个单元。答案由题意推导，并非官方答案；第37题参考 A（library），依据较弱，已标注待核对。第77题和作文为参考表达。
