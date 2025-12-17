---
layout: default
title: rNCA: Self-Repairing Segmentation Masks
---

# rNCA: Self-Repairing Segmentation Masks

**arXiv**: [2512.13397v1](https://arxiv.org/abs/2512.13397) | [PDF](https://arxiv.org/pdf/2512.13397.pdf)

**作者**: Malte Silbernagel, Albert Alonso, Jens Petersen, Bulat Ibragimov, Marleen de Bruijne, Madeleine K. Wyburd

---

## 💡 一句话要点

**提出rNCA作为通用分割模型的后处理机制，通过局部迭代更新修复拓扑错误。**

**关键词**: `分割掩码修复` `神经细胞自动机` `拓扑一致性` `后处理技术` `局部迭代更新`

## 📋 核心要点

1. 核心问题：通用分割模型常产生碎片化或不连通的掩码，需手动或专用方法修复。
2. 方法要点：利用神经细胞自动机（NCA）作为细化机制，基于图像上下文进行局部迭代更新。
3. 实验或效果：在视网膜血管和心肌分割任务中，提升Dice/clDice指标，显著减少拓扑错误。

## 📄 摘要（原文）

> Accurately predicting topologically correct masks remains a difficult task for general segmentation models, which often produce fragmented or disconnected outputs. Fixing these artifacts typically requires hand-crafted refinement rules or architectures specialized to a particular task. Here, we show that Neural Cellular Automata (NCA) can be directly re-purposed as an effective refinement mechanism, using local, iterative updates guided by image context to repair segmentation masks. By training on imperfect masks and ground truths, the automaton learns the structural properties of the target shape while relying solely on local information. When applied to coarse, globally predicted masks, the learned dynamics progressively reconnect broken regions, prune loose fragments and converge towards stable, topologically consistent results. We show how refinement NCA (rNCA) can be easily applied to repair common topological errors produced by different base segmentation models and tasks: for fragmented retinal vessels, it yields 2-3% gains in Dice/clDice and improves Betti errors, reducing $β_0$ errors by 60% and $β_1$ by 20%; for myocardium, it repairs 61.5% of broken cases in a zero-shot setting while lowering ASSD and HD by 19% and 16%, respectively. This showcases NCA as effective and broadly applicable refiners.

