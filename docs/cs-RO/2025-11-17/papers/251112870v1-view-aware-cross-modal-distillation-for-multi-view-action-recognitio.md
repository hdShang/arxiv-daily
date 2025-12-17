---
layout: default
title: View-aware Cross-modal Distillation for Multi-view Action Recognition
---

# View-aware Cross-modal Distillation for Multi-view Action Recognition

**arXiv**: [2511.12870v1](https://arxiv.org/abs/2511.12870) | [PDF](https://arxiv.org/pdf/2511.12870.pdf)

**作者**: Trung Thanh Nguyen, Yasutomo Kawanishi, Vijay John, Takahiro Komamizu, Ichiro Ide

---

## 💡 一句话要点

**提出视图感知跨模态蒸馏以解决部分重叠多视图动作识别问题**

**关键词**: `多视图动作识别` `跨模态蒸馏` `视图感知一致性` `部分重叠视图` `知识蒸馏` `多模态学习`

## 📋 核心要点

1. 核心问题：部分重叠多视图场景中动作仅部分可见，且模态和标注有限。
2. 方法要点：使用跨模态注意力和视图一致性模块，蒸馏多模态教师知识到学生模型。
3. 实验或效果：在MultiSensor-Home数据集上超越竞争方法，并在有限条件下优于教师模型。

## 📄 摘要（原文）

> The widespread use of multi-sensor systems has increased research in multi-view action recognition. While existing approaches in multi-view setups with fully overlapping sensors benefit from consistent view coverage, partially overlapping settings where actions are visible in only a subset of views remain underexplored. This challenge becomes more severe in real-world scenarios, as many systems provide only limited input modalities and rely on sequence-level annotations instead of dense frame-level labels. In this study, we propose View-aware Cross-modal Knowledge Distillation (ViCoKD), a framework that distills knowledge from a fully supervised multi-modal teacher to a modality- and annotation-limited student. ViCoKD employs a cross-modal adapter with cross-modal attention, allowing the student to exploit multi-modal correlations while operating with incomplete modalities. Moreover, we propose a View-aware Consistency module to address view misalignment, where the same action may appear differently or only partially across viewpoints. It enforces prediction alignment when the action is co-visible across views, guided by human-detection masks and confidence-weighted Jensen-Shannon divergence between their predicted class distributions. Experiments on the real-world MultiSensor-Home dataset show that ViCoKD consistently outperforms competitive distillation methods across multiple backbones and environments, delivering significant gains and surpassing the teacher model under limited conditions.

