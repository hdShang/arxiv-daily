---
layout: default
title: FilmSceneDesigner: Chaining Set Design for Procedural Film Scene Generation
---

# FilmSceneDesigner: Chaining Set Design for Procedural Film Scene Generation

**arXiv**: [2511.19137v1](https://arxiv.org/abs/2511.19137) | [PDF](https://arxiv.org/pdf/2511.19137.pdf)

**作者**: Zhifeng Xie, Keyi Zhang, Yiye Yan, Yuling Guo, Fan Yang, Jiting Zhou, Mengtian Li

---

## 💡 一句话要点

**提出FilmSceneDesigner系统以自动化电影场景设计，解决传统手动建模效率低的问题。**

**关键词**: `电影场景生成` `程序化生成` `代理链框架` `3D资产数据集` `自然语言处理` `虚拟预演`

## 📋 核心要点

1. 核心问题：传统电影场景设计依赖专家手动建模，劳动密集且耗时。
2. 方法要点：基于代理链框架生成结构化参数，并通过程序化流程构建完整场景。
3. 实验或效果：系统生成结构合理、电影保真度高的场景，支持虚拟预演等下游任务。

## 📄 摘要（原文）

> Film set design plays a pivotal role in cinematic storytelling and shaping the visual atmosphere. However, the traditional process depends on expert-driven manual modeling, which is labor-intensive and time-consuming. To address this issue, we introduce FilmSceneDesigner, an automated scene generation system that emulates professional film set design workflow. Given a natural language description, including scene type, historical period, and style, we design an agent-based chaining framework to generate structured parameters aligned with film set design workflow, guided by prompt strategies that ensure parameter accuracy and coherence. On the other hand, we propose a procedural generation pipeline which executes a series of dedicated functions with the structured parameters for floorplan and structure generation, material assignment, door and window placement, and object retrieval and layout, ultimately constructing a complete film scene from scratch. Moreover, to enhance cinematic realism and asset diversity, we construct SetDepot-Pro, a curated dataset of 6,862 film-specific 3D assets and 733 materials. Experimental results and human evaluations demonstrate that our system produces structurally sound scenes with strong cinematic fidelity, supporting downstream tasks such as virtual previs, construction drawing and mood board creation.

