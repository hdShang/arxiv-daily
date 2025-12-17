---
layout: default
title: ShapeCraft: LLM Agents for Structured, Textured and Interactive 3D Modeling
---

# ShapeCraft: LLM Agents for Structured, Textured and Interactive 3D Modeling

**arXiv**: [2510.17603v1](https://arxiv.org/abs/2510.17603) | [PDF](https://arxiv.org/pdf/2510.17603.pdf)

**作者**: Shuyuan Zhang, Chenhan Jiang, Zuoou Li, Jiankang Deng

---

## 💡 一句话要点

**提出ShapeCraft多智能体框架，通过图程序形状表示解决文本到3D生成的结构化和交互性问题**

**关键词**: `文本到3D生成` `多智能体框架` `图程序形状表示` `结构化3D建模` `交互式3D资产`

## 📋 核心要点

1. 现有文本到3D方法生成非结构化网格且交互性差，难以用于艺术工作流
2. 引入图程序形状表示，分解自然语言为子任务图，提升LLM对空间关系和语义细节的理解
3. 实验显示ShapeCraft在几何精度和语义丰富度上优于现有方法，支持动画和用户定制编辑

## 📄 摘要（原文）

> 3D generation from natural language offers significant potential to reduce
> expert manual modeling efforts and enhance accessibility to 3D assets. However,
> existing methods often yield unstructured meshes and exhibit poor
> interactivity, making them impractical for artistic workflows. To address these
> limitations, we represent 3D assets as shape programs and introduce ShapeCraft,
> a novel multi-agent framework for text-to-3D generation. At its core, we
> propose a Graph-based Procedural Shape (GPS) representation that decomposes
> complex natural language into a structured graph of sub-tasks, thereby
> facilitating accurate LLM comprehension and interpretation of spatial
> relationships and semantic shape details. Specifically, LLM agents
> hierarchically parse user input to initialize GPS, then iteratively refine
> procedural modeling and painting to produce structured, textured, and
> interactive 3D assets. Qualitative and quantitative experiments demonstrate
> ShapeCraft's superior performance in generating geometrically accurate and
> semantically rich 3D assets compared to existing LLM-based agents. We further
> show the versatility of ShapeCraft through examples of animated and
> user-customized editing, highlighting its potential for broader interactive
> applications.

