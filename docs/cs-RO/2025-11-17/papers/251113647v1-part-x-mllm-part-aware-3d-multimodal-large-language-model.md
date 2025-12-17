---
layout: default
title: Part-X-MLLM: Part-aware 3D Multimodal Large Language Model
---

# Part-X-MLLM: Part-aware 3D Multimodal Large Language Model

**arXiv**: [2511.13647v1](https://arxiv.org/abs/2511.13647) | [PDF](https://arxiv.org/pdf/2511.13647.pdf)

**作者**: Chunshi Wang, Junliang Ye, Yunhan Yang, Yang Li, Zizhuo Lin, Jun Zhu, Zhuo Chen, Yawei Luo, Chunchao Guo

---

## 💡 一句话要点

**提出Part-X-MLLM以统一3D多模态任务，通过结构化程序生成驱动几何模块。**

**关键词**: `3D多模态大语言模型` `部分感知` `结构化程序生成` `几何编辑` `双编码器架构`

## 📋 核心要点

1. 核心问题：统一3D多模态任务，如部分级检测、描述和编辑。
2. 方法要点：使用双编码器架构，生成结构化令牌序列，解耦符号规划与几何合成。
3. 实验效果：在问答、生成和编辑任务中实现先进性能，通过单一接口控制。

## 📄 摘要（原文）

> We introduce Part-X-MLLM, a native 3D multimodal large language model that unifies diverse 3D tasks by formulating them as programs in a structured, executable grammar. Given an RGB point cloud and a natural language prompt, our model autoregressively generates a single, coherent token sequence encoding part-level bounding boxes, semantic descriptions, and edit commands. This structured output serves as a versatile interface to drive downstream geometry-aware modules for part-based generation and editing. By decoupling the symbolic planning from the geometric synthesis, our approach allows any compatible geometry engine to be controlled through a single, language-native frontend. We pre-train a dual-encoder architecture to disentangle structure from semantics and instruction-tune the model on a large-scale, part-centric dataset. Experiments demonstrate that our model excels at producing high-quality, structured plans, enabling state-of-the-art performance in grounded Q\&A, compositional generation, and localized editing through one unified interface. Project page: https://chunshi.wang/Part-X-MLLM/

