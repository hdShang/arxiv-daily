---
layout: default
title: CascadedViT: Cascaded Chunk-FeedForward and Cascaded Group Attention Vision Transformer
---

# CascadedViT: Cascaded Chunk-FeedForward and Cascaded Group Attention Vision Transformer

**arXiv**: [2511.14111v1](https://arxiv.org/abs/2511.14111) | [PDF](https://arxiv.org/pdf/2511.14111.pdf)

**作者**: Srivathsan Sivakumar, Faisal Z. Qureshi

---

## 💡 一句话要点

**提出CascadedViT以降低视觉Transformer的计算和能耗，适用于资源受限设备。**

**关键词**: `视觉Transformer` `轻量级架构` `计算效率` `能耗优化` `移动设备部署`

## 📋 核心要点

1. 视觉Transformer计算和内存需求高，限制在资源受限平台部署。
2. 引入级联分块前馈网络，分割输入特征提升参数和FLOP效率。
3. 在ImageNet-1K上验证，CViT-XL准确率75.5%，FLOPs减少15%，能耗降低3.3%。

## 📄 摘要（原文）

> Vision Transformers (ViTs) have demonstrated remarkable performance across a range of computer vision tasks; however, their high computational, memory, and energy demands hinder deployment on resource-constrained platforms. In this paper, we propose \emph{Cascaded-ViT (CViT)}, a lightweight and compute-efficient vision transformer architecture featuring a novel feedforward network design called \emph{Cascaded-Chunk Feed Forward Network (CCFFN)}. By splitting input features, CCFFN improves parameter and FLOP efficiency without sacrificing accuracy. Experiments on ImageNet-1K show that our \emph{CViT-XL} model achieves 75.5\% Top-1 accuracy while reducing FLOPs by 15\% and energy consumption by 3.3\% compared to EfficientViT-M5. Across various model sizes, the CViT family consistently exhibits the lowest energy consumption, making it suitable for deployment on battery-constrained devices such as mobile phones and drones. Furthermore, when evaluated using a new metric called \emph{Accuracy-Per-FLOP (APF)}, which quantifies compute efficiency relative to accuracy, CViT models consistently achieve top-ranking efficiency. Particularly, CViT-L is 2.2\% more accurate than EfficientViT-M2 while having comparable APF scores.

