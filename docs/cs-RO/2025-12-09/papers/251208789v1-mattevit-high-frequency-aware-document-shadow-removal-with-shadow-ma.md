---
layout: default
title: MatteViT: High-Frequency-Aware Document Shadow Removal with Shadow Matte Guidance
---

# MatteViT: High-Frequency-Aware Document Shadow Removal with Shadow Matte Guidance

**arXiv**: [2512.08789v1](https://arxiv.org/abs/2512.08789) | [PDF](https://arxiv.org/pdf/2512.08789.pdf)

**作者**: Chaewon Kim, Seoyeon Lee, Jonghyuk Park

---

## 💡 一句话要点

**提出MatteViT框架，利用高频感知和阴影遮罩指导解决文档阴影去除问题。**

**关键词**: `文档阴影去除` `高频感知` `阴影遮罩指导` `视觉变换器` `光学字符识别`

## 📋 核心要点

1. 核心问题：文档阴影去除需保留高频细节如文本边缘，阴影常模糊精细结构。
2. 方法要点：结合空间与频域信息，引入高频放大模块和连续亮度阴影遮罩指导。
3. 实验或效果：在公开基准测试中达到先进性能，提升下游任务如OCR的识别效果。

## 📄 摘要（原文）

> Document shadow removal is essential for enhancing the clarity of digitized documents. Preserving high-frequency details (e.g., text edges and lines) is critical in this process because shadows often obscure or distort fine structures. This paper proposes a matte vision transformer (MatteViT), a novel shadow removal framework that applies spatial and frequency-domain information to eliminate shadows while preserving fine-grained structural details. To effectively retain these details, we employ two preservation strategies. First, our method introduces a lightweight high-frequency amplification module (HFAM) that decomposes and adaptively amplifies high-frequency components. Second, we present a continuous luminance-based shadow matte, generated using a custom-built matte dataset and shadow matte generator, which provides precise spatial guidance from the earliest processing stage. These strategies enable the model to accurately identify fine-grained regions and restore them with high fidelity. Extensive experiments on public benchmarks (RDD and Kligler) demonstrate that MatteViT achieves state-of-the-art performance, providing a robust and practical solution for real-world document shadow removal. Furthermore, the proposed method better preserves text-level details in downstream tasks, such as optical character recognition, improving recognition performance over prior methods.

