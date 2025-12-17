---
layout: default
title: Beyond Flatlands: Unlocking Spatial Intelligence by Decoupling 3D Reasoning from Numerical Regression
---

# Beyond Flatlands: Unlocking Spatial Intelligence by Decoupling 3D Reasoning from Numerical Regression

**arXiv**: [2511.11239v1](https://arxiv.org/abs/2511.11239) | [PDF](https://arxiv.org/pdf/2511.11239.pdf)

**作者**: Zhongbin Guo, Jiahe Liu, Yushan Li, Wenyu Gao, Zhen Yang, Chenzhi Li, Xinyue Zhang, Ping Jian

---

## 💡 一句话要点

**提出GEODE架构以解决视觉语言模型在3D空间推理中的双重瓶颈问题**

**关键词**: `视觉语言模型` `3D空间推理` `解耦架构` `连续数值回归` `几何感知编码` `链式思维推理`

## 📋 核心要点

1. 核心问题：现有VLMs因输入阶段几何编码器计算昂贵和输出阶段离散标记器无法生成连续数值而难以理解3D空间
2. 方法要点：引入DRM模块对齐3D与2D特征并生成空间推理逻辑，以及DRH模块通过轻量MLP实现精确连续回归
3. 实验或效果：1.5B参数模型在空间推理性能上达到与7B+模型相当的水平

## 📄 摘要（原文）

> Existing Vision Language Models (VLMs) architecturally rooted in "flatland" perception, fundamentally struggle to comprehend real-world 3D spatial intelligence. This failure stems from a dual-bottleneck: input-stage conflict between computationally exorbitant geometric-aware encoders and superficial 2D-only features, and output-stage misalignment where discrete tokenizers are structurally incapable of producing precise, continuous numerical values. To break this impasse, we introduce GEODE (Geometric-Output and Decoupled-Input Engine), a novel architecture that resolves this dual-bottleneck by decoupling 3D reasoning from numerical generation. GEODE augments main VLM with two specialized, plug-and-play modules: Decoupled Rationale Module (DRM) that acts as spatial co-processor, aligning explicit 3D data with 2D visual features via cross-attention and distilling spatial Chain-of-Thought (CoT) logic into injectable Rationale Tokens; and Direct Regression Head (DRH), an "Embedding-as-Value" paradigm which routes specialized control tokens to a lightweight MLP for precise, continuous regression of scalars and 3D bounding boxes. The synergy of these modules allows our 1.5B parameter model to function as a high-level semantic dispatcher, achieving state-of-the-art spatial reasoning performance that rivals 7B+ models.

