---
layout: default
title: MDReID: Modality-Decoupled Learning for Any-to-Any Multi-Modal Object Re-Identification
---

# MDReID: Modality-Decoupled Learning for Any-to-Any Multi-Modal Object Re-Identification

**arXiv**: [2510.23301v1](https://arxiv.org/abs/2510.23301) | [PDF](https://arxiv.org/pdf/2510.23301.pdf)

**作者**: Yingying Feng, Jie Li, Jie Hu, Yukang Zhang, Lei Tan, Jiayi Ji

---

## 💡 一句话要点

**提出MDReID框架，通过模态解耦学习解决多模态物体重识别中的模态不一致问题。**

**关键词**: `多模态物体重识别` `模态解耦学习` `模态感知度量学习` `跨模态检索` `特征分解`

## 📋 核心要点

1. 核心问题：现实物体重识别常面临模态不一致，如RGB与NIR图像查询，现有方法假设模态匹配，限制实用性。
2. 方法要点：引入模态解耦学习和模态感知度量学习，分解特征为共享与特定部分，增强跨模态检索能力。
3. 实验效果：在多个基准测试中，模态匹配和不匹配场景下均取得显著mAP提升，最高达11.5%。

## 📄 摘要（原文）

> Real-world object re-identification (ReID) systems often face modality
> inconsistencies, where query and gallery images come from different sensors
> (e.g., RGB, NIR, TIR). However, most existing methods assume modality-matched
> conditions, which limits their robustness and scalability in practical
> applications. To address this challenge, we propose MDReID, a flexible
> any-to-any image-level ReID framework designed to operate under both
> modality-matched and modality-mismatched scenarios. MDReID builds on the
> insight that modality information can be decomposed into two components:
> modality-shared features that are predictable and transferable, and
> modality-specific features that capture unique, modality-dependent
> characteristics. To effectively leverage this, MDReID introduces two key
> components: the Modality Decoupling Learning (MDL) and Modality-aware Metric
> Learning (MML). Specifically, MDL explicitly decomposes modality features into
> modality-shared and modality-specific representations, enabling effective
> retrieval in both modality-aligned and mismatched scenarios. MML, a tailored
> metric learning strategy, further enforces orthogonality and complementarity
> between the two components to enhance discriminative power across modalities.
> Extensive experiments conducted on three challenging multi-modality ReID
> benchmarks (RGBNT201, RGBNT100, MSVR310) consistently demonstrate the
> superiority of MDReID. Notably, MDReID achieves significant mAP improvements of
> 9.8\%, 3.0\%, and 11.5\% in general modality-matched scenarios, and average
> gains of 3.4\%, 11.8\%, and 10.9\% in modality-mismatched scenarios,
> respectively. The code is available at:
> \textcolor{magenta}{https://github.com/stone96123/MDReID}.

