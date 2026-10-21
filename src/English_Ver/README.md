# English_Ver — SCS Modding Wiki 离线镜像（Markdown）

由 [`../../scripts/rebuild_mirror.py`](../../scripts/rebuild_mirror.py) 生成：
抓取（fetch_wiki_sources）→ 转换（html_to_markdown）→ 整理（organize_layout）。
**请勿手工编辑**，需要更新时重跑脚本即可。

- 抓取时间：2026-10-21 23:56:14 +0800
- 页面：757（全部命名空间中的现存页面，仅 Markdown）
- 图片：725 个文件
- 入口：[`index.md`](index.md)

## 目录结构

```
English_Ver/
├── README.md            本说明
├── index.md             ★ 全站索引（从这里进入）
├── manifest.json        机器清单（标题 / URL / 分组 / revid / 时间戳）
├── pages/               ★ 正文 Markdown（翻译工作区）
│   ├── articles/          主条目，保留 Documentation/… 层级
│   ├── files/             文件页（原 File: 前缀已去掉）
│   ├── templates/         模板页
│   ├── users/             用户页
│   ├── user_talk/         用户讨论页
│   ├── talk/              条目讨论页
│   ├── project/           项目命名空间页
│   ├── mediawiki/         界面消息页
│   └── category/          分类页
└── (无 images/；图片统一存放在上一级 ../images/<分组>/<页面路径>/)
```

| 分组 | 页面数 |
| --- | --- |
| `articles/` | 260 |
| `category/` | 1 |
| `files/` | 440 |
| `mediawiki/` | 5 |
| `project/` | 2 |
| `talk/` | 8 |
| `templates/` | 23 |
| `user_talk/` | 12 |
| `users/` | 6 |

`pages/` 按命名空间分区，图片按「引用它的页面」归档在上一级 `../images/<分组>/<页面路径>/`，
所有语言版本共享同一份图片。页面内链接均为相对路径；移动目录或重命名页面时请用脚本重算链接。

## 抓取范围

- **包含**：主条目、File 文件页、Template 模板、User 用户页、Talk 讨论页、Project、MediaWiki 命名空间页面。
- **不含**：`Special:` 动态页面、历史版本、编辑页（`robots.txt` 亦禁止）。
- 每个 `.md` 末尾保留 `<!-- source: … | revision: … -->` 注释，可据此判断上游是否更新。

## 更新流程（在仓库根目录执行）

```bash
python scripts/rebuild_mirror.py                # 抓取 → 转换 → 整理（约 35 分钟）
python scripts/share_images.py --root src       # 图片合并到 src/images/
```

## 版权

Wiki 内容版权归 SCS Software 及各位编辑者所有，本目录仅作离线翻译参考，不再分发。
