---
layout: default
title: DuGI-MAE: Improving Infrared Mask Autoencoders via Dual-Domain Guidance
---

# DuGI-MAE: Improving Infrared Mask Autoencoders via Dual-Domain Guidance

**arXiv**: [2512.04511v1](https://arxiv.org/abs/2512.04511) | [PDF](https://arxiv.org/pdf/2512.04511.pdf)

**作者**: Yinghui Xing, Xiaoting Su, Shizhou Zhang, Donghao Chu, Di Xu

---

## 💡 一句话要点

**提出DuGI-MAE，通过双域引导改进红外掩码自编码器以提升红外图像理解性能**

**关键词**: `红外图像处理` `掩码自编码器` `双域引导` `自监督学习` `基础模型` `噪声过滤`

## 📋 核心要点

1. 针对红外图像特性，现有基础模型在红外任务中表现不佳，存在信息丢失、全局关联不足和非均匀噪声问题
2. 设计基于熵的确定性掩码策略和双域引导模块，增强信息保留并处理噪声，构建Inf-590K数据集进行预训练
3. 在红外目标检测、语义分割和小目标检测等下游任务中验证了方法的优越性和泛化能力

## 📄 摘要（原文）

> Infrared imaging plays a critical role in low-light and adverse weather conditions. However, due to the distinct characteristics of infrared images, existing foundation models such as Masked Autoencoder (MAE) trained on visible data perform suboptimal in infrared image interpretation tasks. To bridge this gap, an infrared foundation model known as InfMAE was developed and pre-trained on large-scale infrared datasets. Despite its effectiveness, InfMAE still faces several limitations, including the omission of informative tokens, insufficient modeling of global associations, and neglect of non-uniform noise. In this paper, we propose a Dual-domain Guided Infrared foundation model based on MAE (DuGI-MAE). First, we design a deterministic masking strategy based on token entropy, preserving only high-entropy tokens for reconstruction to enhance informativeness. Next, we introduce a Dual-Domain Guidance (DDG) module, which simultaneously captures global token relationships and adaptively filters non-uniform background noise commonly present in infrared imagery. To facilitate large-scale pretraining, we construct Inf-590K, a comprehensive infrared image dataset encompassing diverse scenes, various target types, and multiple spatial resolutions. Pretrained on Inf-590K, DuGI-MAE demonstrates strong generalization capabilities across various downstream tasks, including infrared object detection, semantic segmentation, and small target detection. Experimental results validate the superiority of the proposed method over both supervised and self-supervised comparison methods. Our code is available in the supplementary material.

