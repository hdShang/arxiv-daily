---
layout: default
title: OmniDexVLG: Learning Dexterous Grasp Generation from Vision Language Model-Guided Grasp Semantics, Taxonomy and Functional Affordance
---

# OmniDexVLG: Learning Dexterous Grasp Generation from Vision Language Model-Guided Grasp Semantics, Taxonomy and Functional Affordance

**arXiv**: [2512.03874v1](https://arxiv.org/abs/2512.03874) | [PDF](https://arxiv.org/pdf/2512.03874.pdf)

**作者**: Lei Zhang, Diwen Zheng, Kaixin Bai, Zhenshan Bing, Zoltan-Csaba Marton, Zhaopeng Chen, Alois Christian Knoll, Jianwei Zhang

---

## 💡 一句话要点

**提出OmniDexVLG框架，通过视觉语言模型引导的语义建模解决灵巧抓取生成中的语义可控性问题。**

**关键词**: `灵巧抓取生成` `视觉语言模型` `语义建模` `抓取分类` `功能可供性` `多模态推理`

## 📋 核心要点

1. 核心问题：灵巧抓取生成缺乏对抓取分类、接触语义和功能可供性的统一语义建模，导致语义可控性差。
2. 方法要点：构建语义丰富的抓取数据集生成管道，结合多模态语义推理模块，实现语言和视觉引导下的细粒度抓取合成。
3. 实验或效果：在仿真和真实世界实验中，显著优于现有方法，提升抓取多样性、语义一致性和功能可供性。

## 📄 摘要（原文）

> Dexterous grasp generation aims to produce grasp poses that align with task requirements and human interpretable grasp semantics. However, achieving semantically controllable dexterous grasp synthesis remains highly challenging due to the lack of unified modeling of multiple semantic dimensions, including grasp taxonomy, contact semantics, and functional affordance. To address these limitations, we present OmniDexVLG, a multimodal, semantics aware grasp generation framework capable of producing structurally diverse and semantically coherent dexterous grasps under joint language and visual guidance. Our approach begins with OmniDexDataGen, a semantic rich dexterous grasp dataset generation pipeline that integrates grasp taxonomy guided configuration sampling, functional affordance contact point sampling, taxonomy aware differential force closure grasp sampling, and physics based optimization and validation, enabling systematic coverage of diverse grasp types. We further introduce OmniDexReasoner, a multimodal grasp type semantic reasoning module that leverages multi agent collaboration, retrieval augmented generation, and chain of thought reasoning to infer grasp related semantics and generate high quality annotations that align language instructions with task specific grasp intent. Building upon these components, we develop a unified Vision Language Grasping generation model that explicitly incorporates grasp taxonomy, contact structure, and functional affordance semantics, enabling fine grained control over grasp synthesis from natural language instructions. Extensive experiments in simulation and real world object grasping and ablation studies demonstrate that our method substantially outperforms state of the art approaches in terms of grasp diversity, contact semantic diversity, functional affordance diversity, and semantic consistency.

