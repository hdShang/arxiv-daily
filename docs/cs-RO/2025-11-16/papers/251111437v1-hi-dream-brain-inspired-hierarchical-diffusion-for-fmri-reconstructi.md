---
layout: default
title: Hi-DREAM: Brain Inspired Hierarchical Diffusion for fMRI Reconstruction via ROI Encoder and visuAl Mapping
---

# Hi-DREAM: Brain Inspired Hierarchical Diffusion for fMRI Reconstruction via ROI Encoder and visuAl Mapping

**arXiv**: [2511.11437v1](https://arxiv.org/abs/2511.11437) | [PDF](https://arxiv.org/pdf/2511.11437.pdf)

**作者**: Guowei Zhang, Yun Zhao, Moein Khajehnejad, Adeel Razi, Levin Kuhlmann

---

## 💡 一句话要点

**提出Hi-DREAM框架，通过分层扩散和ROI编码解决fMRI重建中视觉信息组织模糊问题。**

**关键词**: `fMRI重建` `分层扩散模型` `视觉皮层分析` `ROI编码` `脑启发计算`

## 📋 核心要点

1. 核心问题：现有方法忽略大脑视觉皮层层次结构，导致早期、中期和晚期区域角色混淆。
2. 方法要点：使用ROI适配器构建多尺度皮层金字塔，并通过ControlNet在去噪中注入尺度特定提示。
3. 实验或效果：在NSD数据集上实现语义指标最优，同时保持低层保真度竞争力。

## 📄 摘要（原文）

> Mapping human brain activity to natural images offers a new window into vision and cognition, yet current diffusion-based decoders face a core difficulty: most condition directly on fMRI features without analyzing how visual information is organized across the cortex. This overlooks the brain's hierarchical processing and blurs the roles of early, middle, and late visual areas. We propose Hi-DREAM, a brain-inspired conditional diffusion framework that makes the cortical organization explicit. A region-of-interest (ROI) adapter groups fMRI into early/mid/late streams and converts them into a multi-scale cortical pyramid aligned with the U-Net depth (shallow scales preserve layout and edges; deeper scales emphasize objects and semantics). A lightweight, depth-matched ControlNet injects these scale-specific hints during denoising. The result is an efficient and interpretable decoder in which each signal plays a brain-like role, allowing the model not only to reconstruct images but also to illuminate functional contributions of different visual areas. Experiments on the Natural Scenes Dataset (NSD) show that Hi-DREAM attains state-of-the-art performance on high-level semantic metrics while maintaining competitive low-level fidelity. These findings suggest that structuring conditioning by cortical hierarchy is a powerful alternative to purely data-driven embeddings and provides a useful lens for studying the visual cortex.

