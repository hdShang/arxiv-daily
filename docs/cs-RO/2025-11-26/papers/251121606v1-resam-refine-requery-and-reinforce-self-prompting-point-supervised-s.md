---
layout: default
title: ReSAM: Refine, Requery, and Reinforce: Self-Prompting Point-Supervised Segmentation for Remote Sensing Images
---

# ReSAM: Refine, Requery, and Reinforce: Self-Prompting Point-Supervised Segmentation for Remote Sensing Images

**arXiv**: [2511.21606v1](https://arxiv.org/abs/2511.21606) | [PDF](https://arxiv.org/pdf/2511.21606.pdf)

**作者**: M. Naseer Subhani

---

## 💡 一句话要点

**提出ReSAM自提示框架，以点监督方式提升遥感图像分割性能**

**关键词**: `遥感图像分割` `点监督学习` `自提示机制` `领域适应` `SAM模型优化`

## 📋 核心要点

1. 核心问题：SAM在遥感图像上因领域偏移和标注稀缺而表现不佳
2. 方法要点：采用Refine-Requery-Reinforce循环，通过自构建提示优化分割
3. 实验或效果：在多个数据集上超越预训练SAM和点监督方法，提升鲁棒性

## 📄 摘要（原文）

> Interactive segmentation models such as the Segment Anything Model (SAM) have demonstrated remarkable generalization on natural images, but perform suboptimally on remote sensing imagery (RSI) due to severe domain shift and the scarcity of dense annotations. To address this, we propose a self-prompting, point-supervised framework that adapts SAM to RSIs using only sparse point annotations. Our method employs a Refine-Requery-Reinforce loop, where coarse pseudo-masks are generated from initial points (Refine), improved with self-constructed box prompts (Requery), and embeddings are aligned across iterations to reduce confirmation bias (Reinforce). Without relying on full-mask supervision, our approach progressively enhances SAM's segmentation quality and domain robustness through self-guided prompt adaptation . We evaluate our proposed method on three RSI benchmark datasets, including WHU, HRSID, and NWPU VHR-10, showing that our method consistently surpasses pretrained SAM and recent point-supervised segmentation methods. Our results demonstrate that self-prompting and semantic alignment provide an efficient path towards scalable, point-level adaptation of foundation segmentation models for remote sensing applications.

