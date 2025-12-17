---
layout: default
title: Buffer replay enhances the robustness of multimodal learning under missing-modality
---

# Buffer replay enhances the robustness of multimodal learning under missing-modality

**arXiv**: [2511.23070v1](https://arxiv.org/abs/2511.23070) | [PDF](https://arxiv.org/pdf/2511.23070.pdf)

**作者**: Hongye Zhu, Xuan Liu, Yanwen Ba, Jingye Xue, Shigeng Zhang

---

## 💡 一句话要点

**提出REplay Prompting以增强多模态学习在缺失模态下的鲁棒性**

**关键词**: `多模态学习` `缺失模态鲁棒性` `特征缓冲区` `残差旁路` `私有-共享特征解耦` `任务感知初始化`

## 📋 核心要点

1. 核心问题：缺失模态导致多模态模型性能显著下降，现有方法计算成本高或忽略长距离上下文信息。
2. 方法要点：通过残差旁路构建模态特征缓冲区，结合私有-共享特征解耦和任务感知动态初始化机制。
3. 实验或效果：在视觉-语言、视觉-语言-音频等基准上，REP在单/多模态缺失场景下优于先前方法，参数开销可忽略。

## 📄 摘要（原文）

> Missing modalities consistently lead to significant performance degradation in multimodal models. Existing approaches either synthesize missing modalities at high computational cost or apply prompt-based fine-tuning that relies only on adjacent-layer features and overlooks long-distance contextual information, which may offer additional tolerance to errors when one or more modalities are missing. To address this, we introduce REplay Prompting (REP): (1) construct modality-wise feature buffers via a residual bypass to cache early-layer representations and replay them in deeper layers, mitigating information loss as network depth increases; (2) employ a private-shared feature decoupling strategy, where private buffers preserve modality-specific signals and shared buffers encode cross-modal semantics; and (3) design a task-aware dynamic initialization mechanism to configure these buffers differently, improving stability and generalization under diverse missing-modality conditions. Experiments on vision-language, vision-language-audio, and temporal multimodal benchmarks demonstrate that REP consistently outperforms prior methods under both single- and multi-modality missing scenarios, while introducing only negligible parameter overhead. These results establish REP as a lightweight and effective paradigm for robust multimodal learning in challenging missing-modality environments.

