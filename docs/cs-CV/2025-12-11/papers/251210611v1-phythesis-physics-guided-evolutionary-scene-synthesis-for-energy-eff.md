---
layout: default
title: Phythesis: Physics-Guided Evolutionary Scene Synthesis for Energy-Efficient Data Center Design via LLMs
---

# Phythesis: Physics-Guided Evolutionary Scene Synthesis for Energy-Efficient Data Center Design via LLMs

**arXiv**: [2512.10611v1](https://arxiv.org/abs/2512.10611) | [PDF](https://arxiv.org/pdf/2512.10611.pdf)

**作者**: Minghao LI, Ruihang Wang, Rui Tan, Yonggang Wen

---

## 💡 一句话要点

**提出Phythesis框架，结合LLMs与物理引导进化优化，实现数据中心节能设计的仿真就绪场景合成。**

**关键词**: `数据中心设计` `物理引导优化` `大语言模型` `进化算法` `场景合成` `能效优化`

## 📋 核心要点

1. 核心问题：传统数据中心设计方法难以处理复杂系统，现有生成AI忽略物理约束，不适用于量化目标。
2. 方法要点：采用双层优化架构，LLM驱动生成物理合理布局，物理引导优化选择最优资产参数。
3. 实验或效果：在三个规模实验中，相比基于LLM的基线，生成成功率提升57.3%，PUE改善11.5%。

## 📄 摘要（原文）

> Data center (DC) infrastructure serves as the backbone to support the escalating demand for computing capacity. Traditional design methodologies that blend human expertise with specialized simulation tools scale poorly with the increasing system complexity. Recent studies adopt generative artificial intelligence to design plausible human-centric indoor layouts. However, they do not consider the underlying physics, making them unsuitable for the DC design that sets quantifiable operational objectives and strict physical constraints. To bridge the gap, we propose Phythesis, a novel framework that synergizes large language models (LLMs) and physics-guided evolutionary optimization to automate simulation-ready (SimReady) scene synthesis for energy-efficient DC design. Phythesis employs an iterative bi-level optimization architecture, where (i) the LLM-driven optimization level generates physically plausible three-dimensional layouts and self-criticizes them to refine the scene topology, and (ii) the physics-informed optimization level identifies the optimal asset parameters and selects the best asset combination. Experiments on three generation scales show that Phythesis achieves 57.3% generation success rate increase and 11.5% power usage effectiveness (PUE) improvement, compared with the vanilla LLM-based solution.

