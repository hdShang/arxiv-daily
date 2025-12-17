---
layout: default
title: COACH: Collaborative Agents for Contextual Highlighting - A Multi-Agent Framework for Sports Video Analysis
---

# COACH: Collaborative Agents for Contextual Highlighting - A Multi-Agent Framework for Sports Video Analysis

**arXiv**: [2512.01853v1](https://arxiv.org/abs/2512.01853) | [PDF](https://arxiv.org/pdf/2512.01853.pdf)

**作者**: Tsz-To Wong, Ching-Chun Huang, Hong-Han Shuai

---

## 💡 一句话要点

**提出COACH多智能体框架，以解决体育视频分析中时序层次理解不足的问题。**

**关键词**: `多智能体系统` `体育视频分析` `时序层次理解` `自适应管道` `可解释性`

## 📋 核心要点

1. 核心问题：现有端到端模型难以处理体育视频的微观到宏观时序层次，导致泛化性差、开发成本高和可解释性低。
2. 方法要点：采用可重构多智能体系统，每个智能体作为专用认知工具，通过迭代调用和灵活组合构建自适应分析管道。
3. 实验或效果：在羽毛球分析任务中验证框架适应性，实现细粒度事件检测与全局语义组织的桥接。

## 📄 摘要（原文）

> Intelligent sports video analysis demands a comprehensive understanding of temporal context, from micro-level actions to macro-level game strategies. Existing end-to-end models often struggle with this temporal hierarchy, offering solutions that lack generalization, incur high development costs for new tasks, and suffer from poor interpretability. To overcome these limitations, we propose a reconfigurable Multi-Agent System (MAS) as a foundational framework for sports video understanding. In our system, each agent functions as a distinct "cognitive tool" specializing in a specific aspect of analysis. The system's architecture is not confined to a single temporal dimension or task. By leveraging iterative invocation and flexible composition of these agents, our framework can construct adaptive pipelines for both short-term analytic reasoning (e.g., Rally QA) and long-term generative summarization (e.g., match summaries). We demonstrate the adaptability of this framework using two representative tasks in badminton analysis, showcasing its ability to bridge fine-grained event detection and global semantic organization. This work presents a paradigm shift towards a flexible, scalable, and interpretable system for robust, cross-task sports video intelligence.The project homepage is available at https://aiden1020.github.io/COACH-project-page

