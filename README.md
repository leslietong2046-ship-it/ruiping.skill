# 🔥 锐评

> 每天看50条新闻有几条帮你做判断了？别人追热点，你追观点。

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://img.shields.io/badge/License-MIT-blue.svg)
[![Skill](https://img.shields.io/badge/虾评-4.3%2F5.0-green.svg)](https://xiaping.coze.site/skill/fbd59253-f9ed-4628-975b-b0671b768a1f?ref=8fa30089-2274-441a-a0c3-b2bd9aab0f8c)

---

## 🎯 一句话说明

三步走：追踪热点→筛选值得评的→给出犀利观点，帮你比99%的人多想一层。

---

## 🆕 v2.0 重大升级：从框架变工具

**升级前**：教你犀利思考 → **升级后**：丢条新闻直接出锐评

- ✅ 加了输出协议 → 锐评格式标准化
- ✅ 加了直接输出模式 → 丢新闻，直接出锐评
- ✅ 加了搜索模式强化 → 自动搜索背景信息
- ✅ 加了Python锐评生成器CLI → `demo.py` 可离线生成锐评

---

## 🚀 快速开始

### Coze Skill 使用
```markdown
激活后，丢一条新闻或话题，我来给你锐评
```

### CLI 锐评生成器（新增！）
```bash
# 安装依赖
pip install -r requirements.txt

# 基本用法
python demo.py "特斯拉宣布降价20%"

# 指定观点角度
python demo.py "AI监管新政策" --angle consumer

# 查看帮助
python demo.py --help
```

---

## 💻 CLI 使用示例

```bash
$ python demo.py "特斯拉宣布降价20%"

🎯 正在分析...
📊 搜索相关背景...
✍️ 生成锐评...

> 特斯拉不是在卖车，是在卖信仰。降价只是表象，真正杀的是竞品的信心——当价格战开打，所有人都得跟着卷。但卷死的是谁？不是特斯拉，是那些还在靠补贴活的玩家。**对普通消费者是好事，对投资者是警钟。**
```

---

## 🤔 你有同感吗

刷了一天新闻，感觉"我知道了"——

但朋友问"你怎么看"，你卡住了。

**问题不是信息不够，是缺少筛选和加工。**

---

## 🔑 核心三步

### 1. 追踪热点
- 先看，不急着表态
- 等24小时，让子弹飞一会儿
- 噪音自然沉淀

### 2. 筛选值得评的
不是每条都值得评，只追这三类：

| 类型 | 特征 | 例子 |
|------|------|------|
| 影响判断型 | 政策变化、行业洗牌 | 某行业新规出台 |
| 反直觉型 | 看起来对但仔细想不对 | "所有人都在说..." |
| 趋势预判型 | 现在是小圈子，3年后是大众 | 技术苗头、政策信号 |

### 3. 给出犀利观点
不用"据报道""有分析称"，用你的判断：

```
一句话结论 → 为什么重要 → 对谁有影响 → 该怎么做 → 一句话锐评
```

---

## 📁 项目结构

```
锐评/
├── SKILL.md           # Coze Skill 定义（输出协议+直接输出模式）
├── demo.py            # Python 锐评生成器 CLI
├── requirements.txt   # 依赖列表
├── examples/          # 示例
│   ├── tesla-price-cut.md
│   └── ai-regulation.md
└── README.md          # 本文件
```

---

## 💡 示例

**新闻**：某新能源车企大幅降价

**锐评输出**：
> 特斯拉不是在卖车，是在卖信仰。降价只是表象，真正杀的是竞品的信心——当价格战开打，所有人都得跟着卷。但卷死的是谁？不是特斯拉，是那些还在靠补贴活的玩家。**对普通消费者是好事，对投资者是警钟。**

---

## 🏆 为什么选这个

1. **不追热点追观点** — 信息洪流里，你需要的是判断力
2. **有筛选才有深度** — 不是每条新闻都值得评
3. **犀利不是刻薄** — 是比表面多想一层

---

## ⭐ 给我Star

开源不易，如果对你有用：
[![Star](https://img.shields.io/github/stars/leslietong2046-ship-it/ruiping.skill?style=social)](https://github.com/leslietong2046-ship-it/ruiping.skill)

---

## 📚 更多资源

- [虾评Skill详情](https://xiaping.coze.site/skill/fbd59253-f9ed-4628-975b-b0671b768a1f?ref=8fa30089-2274-441a-a0c3-b2bd9aab0f8c)
- [GitHub开源](https://github.com/leslietong2046-ship-it/ruiping.skill)

---

*信息消费的终点不是"知道"，是"能判断"。*
*别人追热点，你追观点。*

---

## 📝 Changelog

### v2.0 (2024-05-02)
- ✨ 加了输出协议（锐评格式标准化）
- ✨ 加了直接输出模式（丢新闻，直接出锐评）
- ✨ 加了搜索模式强化
- ✨ 加了 `demo.py` Python锐评生成器CLI
- ✨ 加了2个示例（tesla-price-cut/ai-regulation）

### v1.0 (2024-04-01)
- 🎉 初始版本
- 📖 犀利思考三步框架
