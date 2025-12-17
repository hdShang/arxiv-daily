---
layout: default
title: A Dataset and Baseline for Deep Learning-Based Visual Quality Inspection in Remanufacturing
---

# A Dataset and Baseline for Deep Learning-Based Visual Quality Inspection in Remanufacturing

**arXiv**: [2511.15440v1](https://arxiv.org/abs/2511.15440) | [PDF](https://arxiv.org/pdf/2511.15440.pdf)

**作者**: Johannes C. Bauer, Paul Geng, Stephan Trattnig, Petr Dokládal, Rüdiger Daub

---

## 💡 一句话要点

**提出基于对比正则化损失的深度学习模型以提升再制造视觉质量检测的泛化能力**

**关键词**: `再制造视觉检测` `深度学习泛化` `对比正则化损失` `图像数据集` `质量分类`

## 📋 核心要点

1. 核心问题：再制造中零件视觉质量检测依赖人工，深度学习模型泛化到新零件或缺陷模式困难
2. 方法要点：构建齿轮箱零件图像数据集，引入对比正则化损失增强模型鲁棒性
3. 实验或效果：评估不同模型，对比正则化损失能改善对未见零件类型的泛化性能

## 📄 摘要（原文）

> Remanufacturing describes a process where worn products are restored to like-new condition and it offers vast ecological and economic potentials. A key step is the quality inspection of disassembled components, which is mostly done manually due to the high variety of parts and defect patterns. Deep neural networks show great potential to automate such visual inspection tasks but struggle to generalize to new product variants, components, or defect patterns. To tackle this challenge, we propose a novel image dataset depicting typical gearbox components in good and defective condition from two automotive transmissions. Depending on the train-test split of the data, different distribution shifts are generated to benchmark the generalization ability of a classification model. We evaluate different models using the dataset and propose a contrastive regularization loss to enhance model robustness. The results obtained demonstrate the ability of the loss to improve generalisation to unseen types of components.

