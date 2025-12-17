---
layout: default
title: ZeroDexGrasp: Zero-Shot Task-Oriented Dexterous Grasp Synthesis with Prompt-Based Multi-Stage Semantic Reasoning
---

# ZeroDexGrasp: Zero-Shot Task-Oriented Dexterous Grasp Synthesis with Prompt-Based Multi-Stage Semantic Reasoning

**arXiv**: [2511.13327v1](https://arxiv.org/abs/2511.13327) | [PDF](https://arxiv.org/pdf/2511.13327.pdf)

**作者**: Juntao Jian, Yi-Lin Wei, Chengjie Mou, Yuhao Lin, Xing Zhu, Yujun Shen, Wei-Shi Zheng, Ruizhen Hu

---

## 💡 一句话要点

**提出ZeroDexGrasp框架以解决零样本任务导向灵巧抓取泛化问题**

**关键词**: `灵巧抓取合成` `零样本学习` `多模态推理` `任务导向抓取` `抓取优化`

## 📋 核心要点

1. 现有方法依赖标注数据，难以泛化到多样物体和任务指令
2. 结合多模态大语言模型与抓取优化，推理初始抓取配置并优化物理可行性
3. 实验显示在未见物体和复杂任务上实现高质量零样本抓取

## 📄 摘要（原文）

> Task-oriented dexterous grasping holds broad application prospects in robotic manipulation and human-object interaction. However, most existing methods still struggle to generalize across diverse objects and task instructions, as they heavily rely on costly labeled data to ensure task-specific semantic alignment. In this study, we propose \textbf{ZeroDexGrasp}, a zero-shot task-oriented dexterous grasp synthesis framework integrating Multimodal Large Language Models with grasp refinement to generate human-like grasp poses that are well aligned with specific task objectives and object affordances. Specifically, ZeroDexGrasp employs prompt-based multi-stage semantic reasoning to infer initial grasp configurations and object contact information from task and object semantics, then exploits contact-guided grasp optimization to refine these poses for physical feasibility and task alignment. Experimental results demonstrate that ZeroDexGrasp enables high-quality zero-shot dexterous grasping on diverse unseen object categories and complex task requirements, advancing toward more generalizable and intelligent robotic grasping.

