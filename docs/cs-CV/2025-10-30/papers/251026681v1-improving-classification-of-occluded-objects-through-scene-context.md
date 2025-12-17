---
layout: default
title: Improving Classification of Occluded Objects through Scene Context
---

# Improving Classification of Occluded Objects through Scene Context

**arXiv**: [2510.26681v1](https://arxiv.org/abs/2510.26681) | [PDF](https://arxiv.org/pdf/2510.26681.pdf)

**作者**: Courtney M. King, Daniel D. Leeds, Damian Lyons, George Kalaitzis

---

## 💡 一句话要点

**提出两种场景信息融合方法以提升遮挡物体分类性能**

**关键词**: `遮挡物体识别` `场景上下文融合` `RPN-DCNN网络` `多训练策略` `物体检测鲁棒性`

## 📋 核心要点

1. 核心问题：遮挡导致物体识别算法性能下降，需额外信息增强鲁棒性。
2. 方法要点：基于场景背景选择定制网络，并在检测后融合场景知识优化得分。
3. 实验效果：在遮挡数据集上，召回率和精确度均优于基线方法。

## 📄 摘要（原文）

> The presence of occlusions has provided substantial challenges to
> typically-powerful object recognition algorithms. Additional sources of
> information can be extremely valuable to reduce errors caused by occlusions.
> Scene context is known to aid in object recognition in biological vision. In
> this work, we attempt to add robustness into existing Region Proposal
> Network-Deep Convolutional Neural Network (RPN-DCNN) object detection networks
> through two distinct scene-based information fusion techniques. We present one
> algorithm under each methodology: the first operates prior to prediction,
> selecting a custom object network to use based on the identified background
> scene, and the second operates after detection, fusing scene knowledge into
> initial object scores output by the RPN. We demonstrate our algorithms on
> challenging datasets featuring partial occlusions, which show overall
> improvement in both recall and precision against baseline methods. In addition,
> our experiments contrast multiple training methodologies for occlusion
> handling, finding that training on a combination of both occluded and
> unoccluded images demonstrates an improvement over the others. Our method is
> interpretable and can easily be adapted to other datasets, offering many future
> directions for research and practical applications.

