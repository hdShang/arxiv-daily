---
layout: default
title: Thinking with Images via Self-Calling Agent
---

# Thinking with Images via Self-Calling Agent

**arXiv**: [2512.08511v1](https://arxiv.org/abs/2512.08511) | [PDF](https://arxiv.org/pdf/2512.08511.pdf)

**作者**: Wenxi Yang, Yuzhong Zhao, Fang Wan, Qixiang Ye

---

## 💡 一句话要点

**提出自调用思维链以优化视觉推理，通过语言化处理提升训练效率与性能。**

**关键词**: `视觉推理` `思维链` `自调用代理` `强化学习优化` `多模态处理`

## 📋 核心要点

1. 核心问题：多模态思维链依赖高质量数据，强化学习优化困难。
2. 方法要点：将视觉推理重构为纯语言思维链，使用自调用代理分解任务。
3. 实验或效果：在HR-Bench 4K上性能提升1.9%，GPU时间减少约75%。

## 📄 摘要（原文）

> Thinking-with-images paradigms have showcased remarkable visual reasoning capability by integrating visual information as dynamic elements into the Chain-of-Thought (CoT). However, optimizing interleaved multimodal CoT (iMCoT) through reinforcement learning remains challenging, as it relies on scarce high-quality reasoning data. In this study, we propose Self-Calling Chain-of-Thought (sCoT), a novel visual reasoning paradigm that reformulates iMCoT as a language-only CoT with self-calling. Specifically, a main agent decomposes the complex visual reasoning task to atomic subtasks and invokes its virtual replicas, i.e. parameter-sharing subagents, to solve them in isolated context. sCoT enjoys substantial training effectiveness and efficiency, as it requires no explicit interleaving between modalities. sCoT employs group-relative policy optimization to reinforce effective reasoning behavior to enhance optimization. Experiments on HR-Bench 4K show that sCoT improves the overall reasoning performance by up to $1.9\%$ with $\sim 75\%$ fewer GPU hours compared to strong baseline approaches. Code is available at https://github.com/YWenxi/think-with-images-through-self-calling.

