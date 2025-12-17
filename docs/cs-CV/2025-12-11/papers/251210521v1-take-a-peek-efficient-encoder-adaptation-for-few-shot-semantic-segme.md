---
layout: default
title: Take a Peek: Efficient Encoder Adaptation for Few-Shot Semantic Segmentation via LoRA
---

# Take a Peek: Efficient Encoder Adaptation for Few-Shot Semantic Segmentation via LoRA

**arXiv**: [2512.10521v1](https://arxiv.org/abs/2512.10521) | [PDF](https://arxiv.org/pdf/2512.10521.pdf)

**作者**: Pasquale De Marinis, Gennaro Vessio, Giovanna Castellano

---

## 💡 一句话要点

**提出Take a Peek方法，通过LoRA微调编码器以解决少样本语义分割中编码器对新类泛化能力不足的问题。**

**关键词**: `少样本语义分割` `编码器适应` `低秩适应` `跨域分割` `计算效率` `模型无关性`

## 📋 核心要点

1. 核心问题：少样本语义分割中编码器对新类特征提取能力有限，成为性能瓶颈。
2. 方法要点：使用低秩适应（LoRA）在支持集上高效微调编码器，提升适应性并减少计算开销。
3. 实验或效果：在多个基准测试中，TaP显著提升分割性能，尤其在多类场景下表现突出。

## 📄 摘要（原文）

> Few-shot semantic segmentation (FSS) aims to segment novel classes in query images using only a small annotated support set. While prior research has mainly focused on improving decoders, the encoder's limited ability to extract meaningful features for unseen classes remains a key bottleneck. In this work, we introduce \textit{Take a Peek} (TaP), a simple yet effective method that enhances encoder adaptability for both FSS and cross-domain FSS (CD-FSS). TaP leverages Low-Rank Adaptation (LoRA) to fine-tune the encoder on the support set with minimal computational overhead, enabling fast adaptation to novel classes while mitigating catastrophic forgetting. Our method is model-agnostic and can be seamlessly integrated into existing FSS pipelines. Extensive experiments across multiple benchmarks--including COCO $20^i$, Pascal $5^i$, and cross-domain datasets such as DeepGlobe, ISIC, and Chest X-ray--demonstrate that TaP consistently improves segmentation performance across diverse models and shot settings. Notably, TaP delivers significant gains in complex multi-class scenarios, highlighting its practical effectiveness in realistic settings. A rank sensitivity analysis also shows that strong performance can be achieved even with low-rank adaptations, ensuring computational efficiency. By addressing a critical limitation in FSS--the encoder's generalization to novel classes--TaP paves the way toward more robust, efficient, and generalizable segmentation systems. The code is available at https://github.com/pasqualedem/TakeAPeek.

