---
layout: default
title: Modality-Collaborative Low-Rank Decomposers for Few-Shot Video Domain Adaptation
---

# Modality-Collaborative Low-Rank Decomposers for Few-Shot Video Domain Adaptation

**arXiv**: [2511.18711v1](https://arxiv.org/abs/2511.18711) | [PDF](https://arxiv.org/pdf/2511.18711.pdf)

**作者**: Yuyang Wanyan, Xiaoshan Yang, Weiming Dong, Changsheng Xu

---

## 💡 一句话要点

**提出模态协作低秩分解器以解决少样本视频域适应问题**

**关键词**: `少样本学习` `视频域适应` `多模态融合` `低秩分解` `域对齐` `特征分解`

## 📋 核心要点

1. 核心问题：视频多模态特征在少样本域适应中，域偏移影响单模态与融合特征的泛化性能。
2. 方法要点：使用低秩分解器分离模态独有与共享特征，并引入路由器和一致性损失优化对齐。
3. 实验或效果：在三个公开基准测试中，模型性能显著优于现有方法。

## 📄 摘要（原文）

> In this paper, we study the challenging task of Few-Shot Video Domain Adaptation (FSVDA). The multimodal nature of videos introduces unique challenges, necessitating the simultaneous consideration of both domain alignment and modality collaboration in a few-shot scenario, which is ignored in previous literature. We observe that, under the influence of domain shift, the generalization performance on the target domain of each individual modality, as well as that of fused multimodal features, is constrained. Because each modality is comprised of coupled features with multiple components that exhibit different domain shifts. This variability increases the complexity of domain adaptation, thereby reducing the effectiveness of multimodal feature integration. To address these challenges, we introduce a novel framework of Modality-Collaborative LowRank Decomposers (MC-LRD) to decompose modality-unique and modality-shared features with different domain shift levels from each modality that are more friendly for domain alignment. The MC-LRD comprises multiple decomposers for each modality and Multimodal Decomposition Routers (MDR). Each decomposer has progressively shared parameters across different modalities. The MDR is leveraged to selectively activate the decomposers to produce modality-unique and modality-shared features. To ensure efficient decomposition, we apply orthogonal decorrelation constraints separately to decomposers and subrouters, enhancing their diversity. Furthermore, we propose a cross-domain activation consistency loss to guarantee that target and source samples of the same category exhibit consistent activation preferences of the decomposers, thereby facilitating domain alignment. Extensive experimental results on three public benchmarks demonstrate that our model achieves significant improvements over existing methods.

