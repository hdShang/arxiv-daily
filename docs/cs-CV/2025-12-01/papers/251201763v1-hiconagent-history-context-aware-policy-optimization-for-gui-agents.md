---
layout: default
title: HiconAgent: History Context-aware Policy Optimization for GUI Agents
---

# HiconAgent: History Context-aware Policy Optimization for GUI Agents

**arXiv**: [2512.01763v1](https://arxiv.org/abs/2512.01763) | [PDF](https://arxiv.org/pdf/2512.01763.pdf)

**作者**: Xurui Zhou, Gongwei Chen, Yuquan Xie, Zaijing Li, Kaiwen Zhou, Shuai Wang, Shuo Yang, Zhuotao Tian, Rui Shao

---

## 💡 一句话要点

**提出HiconAgent，通过历史上下文感知策略优化解决GUI代理中历史信息利用效率低的问题。**

**关键词**: `GUI代理` `历史上下文优化` `策略优化` `计算效率` `导航任务`

## 📋 核心要点

1. 核心问题：GUI代理使用完整历史导致计算开销大和无关信息干扰。
2. 方法要点：采用动态上下文采样和锚点引导历史压缩，优化历史信息利用。
3. 实验效果：在GUI-Odyssey基准上超越GUI-R1-7B，实现计算加速和FLOPs减少。

## 📄 摘要（原文）

> Graphical User Interface (GUI) agents require effective use of historical context to perform sequential navigation tasks. While incorporating past actions and observations can improve decision making, naive use of full history leads to excessive computational overhead and distraction from irrelevant information. To address this, we introduce HiconAgent, a GUI agent trained with History Context-aware Policy Optimization (HCPO) for efficient and effective utilization of historical information. HCPO optimizes history usage in both sampling and policy updates through two complementary components: (1) Dynamic Context Sampling (DCS) presents the agent with variable length histories during sampling, enabling adaptive use of the most relevant context; (2) Anchor-guided History Compression (AHC) refines the policy update phase with a dual branch strategy where the compressed branch removes history observations while keeping history actions as information flow anchors. The compressed and uncompressed branches are coupled through a history-enhanced alignment loss to enforce consistent history usage while maintaining efficiency. Experiments on mainstream GUI navigation benchmarks demonstrate strong performance. Despite being smaller, HiconAgent-3B outperforms GUI-R1-7B by +8.46 percent grounding accuracy and +11.32 percent step success rate on GUI-Odyssey, while achieving comparable results on AndroidControl and AITW with up to 2.47x computational speedup and 60 percent FLOPs reduction.

