---
layout: default
title: UniVA: Universal Video Agent towards Open-Source Next-Generation Video Generalist
---

# UniVA: Universal Video Agent towards Open-Source Next-Generation Video Generalist

**arXiv**: [2511.08521v1](https://arxiv.org/abs/2511.08521) | [PDF](https://arxiv.org/pdf/2511.08521.pdf)

**作者**: Zhengyang Liang, Daoan Zhang, Huichi Zhou, Rui Huang, Bobo Li, Yuechen Zhang, Shengqiong Wu, Xiaohan Wang, Jiebo Luo, Lizi Liao, Hao Fei

---

## 💡 一句话要点

**提出UniVA通用视频代理框架，以统一视频任务解决复杂工作流需求。**

**关键词**: `视频通用代理` `多代理框架` `视频工作流` `分层内存` `开源基准`

## 📋 核心要点

1. 核心问题：专业AI模型难以处理视频理解、编辑和生成的复杂迭代工作流。
2. 方法要点：采用计划-执行双代理架构，结合模块化工具和分层内存实现自动化。
3. 实验或效果：引入UniVA-Bench基准评估，并开源框架促进多模态AI研究。

## 📄 摘要（原文）

> While specialized AI models excel at isolated video tasks like generation or understanding, real-world applications demand complex, iterative workflows that combine these capabilities. To bridge this gap, we introduce UniVA, an open-source, omni-capable multi-agent framework for next-generation video generalists that unifies video understanding, segmentation, editing, and generation into cohesive workflows. UniVA employs a Plan-and-Act dual-agent architecture that drives a highly automated and proactive workflow: a planner agent interprets user intentions and decomposes them into structured video-processing steps, while executor agents execute these through modular, MCP-based tool servers (for analysis, generation, editing, tracking, etc.). Through a hierarchical multi-level memory (global knowledge, task context, and user-specific preferences), UniVA sustains long-horizon reasoning, contextual continuity, and inter-agent communication, enabling interactive and self-reflective video creation with full traceability. This design enables iterative and any-conditioned video workflows (e.g., text/image/video-conditioned generation $\rightarrow$ multi-round editing $\rightarrow$ object segmentation $\rightarrow$ compositional synthesis) that were previously cumbersome to achieve with single-purpose models or monolithic video-language models. We also introduce UniVA-Bench, a benchmark suite of multi-step video tasks spanning understanding, editing, segmentation, and generation, to rigorously evaluate such agentic video systems. Both UniVA and UniVA-Bench are fully open-sourced, aiming to catalyze research on interactive, agentic, and general-purpose video intelligence for the next generation of multimodal AI systems. (https://univa.online/)

