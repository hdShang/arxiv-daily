---
layout: default
title: SAM3-I: Segment Anything with Instructions
---

# SAM3-I: Segment Anything with Instructions

**arXiv**: [2512.04585v1](https://arxiv.org/abs/2512.04585) | [PDF](https://arxiv.org/pdf/2512.04585.pdf)

**作者**: Jingjing Li, Yue Feng, Yuchen Guo, Jincai Huang, Yongri Piao, Qi Bi, Miao Zhang, Xiaoqi Zhao, Qiang Chen, Shihao Zou, Wei Ji, Huchuan Lu, Li Cheng

---

## 💡 一句话要点

**提出SAM3-I框架，通过指令感知级联适配机制，使SAM3能直接遵循自然语言指令进行分割。**

**关键词**: `指令感知分割` `级联适配机制` `开放词汇分割` `自然语言指令` `视觉语言对齐`

## 📋 核心要点

1. 核心问题：SAM3依赖外部代理将复杂指令转换为名词短语，导致分割精度不足，无法精确表示特定实例。
2. 方法要点：引入指令感知级联适配机制，逐步对齐指令语义与视觉语言表示，支持直接指令跟随分割。
3. 实验或效果：实验显示SAM3-I在保持概念驱动能力的同时，有效扩展至遵循自然语言指令，性能吸引人。

## 📄 摘要（原文）

> Segment Anything Model 3 (SAM3) has advanced open-vocabulary segmentation through promptable concept segmentation, allowing users to segment all instances corresponding to a given concept, typically specified with short noun-phrase (NP) prompts. While this marks the first integration of language-level concepts within the SAM family, real-world usage typically requires far richer expressions that include attributes, spatial relations, functionalities, actions, states, and even implicit reasoning over instances. Currently, SAM3 relies on external multi-modal agents to convert complex instructions into NPs and then conduct iterative mask filtering. However, these NP-level concepts remain overly coarse, often failing to precisely represent a specific instance. In this work, we present SAM3-I, an enhanced framework that unifies concept-level understanding and instruction-level reasoning within the SAM family. SAM3-I introduces an instruction-aware cascaded adaptation mechanism that progressively aligns expressive instruction semantics with SAM3's existing vision-language representations, enabling direct instruction-following segmentation without sacrificing its original concept-driven capabilities. Furthermore, we design a structured instruction taxonomy spanning concept, simple, and complex levels, and develop a scalable data engine to construct a dataset with diverse instruction-mask pairs. Experiments show that SAM3-I delivers appealing performance, demonstrating that SAM3 can be effectively extended to follow natural-language instructions while preserving its strong concept grounding. We open-source SAM3-I and provide practical fine-tuning workflows, enabling researchers to adapt it to domain-specific applications. The source code is available here.

