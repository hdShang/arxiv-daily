---
layout: default
title: Unsupervised Motion-Compensated Decomposition for Cardiac MRI Reconstruction via Neural Representation
---

# Unsupervised Motion-Compensated Decomposition for Cardiac MRI Reconstruction via Neural Representation

**arXiv**: [2511.11436v1](https://arxiv.org/abs/2511.11436) | [PDF](https://arxiv.org/pdf/2511.11436.pdf)

**作者**: Xuanyu Tian, Lixuan Chen, Qing Wu, Xiao Wang, Jie Feng, Yuyao Zhang, Hongjiang Wei

---

## 💡 一句话要点

**提出MoCo-INR方法，以无监督方式解决心脏MRI重建问题**

**关键词**: `心脏MRI重建` `隐式神经表示` `运动补偿` `无监督学习` `高加速成像`

## 📋 核心要点

1. 核心问题：心脏MRI重建中图像质量不足和真实数据稀缺限制临床应用
2. 方法要点：结合隐式神经表示与运动补偿框架，实现精确运动分解和高质量重建
3. 实验或效果：在模拟和真实数据上优于现有方法，支持超高加速因子重建

## 📄 摘要（原文）

> Cardiac magnetic resonance (CMR) imaging is widely used to characterize cardiac morphology and function. To accelerate CMR imaging, various methods have been proposed to recover high-quality spatiotemporal CMR images from highly undersampled k-t space data. However, current CMR reconstruction techniques either fail to achieve satisfactory image quality or are restricted by the scarcity of ground truth data, leading to limited applicability in clinical scenarios. In this work, we proposed MoCo-INR, a new unsupervised method that integrates implicit neural representations (INR) with the conventional motion-compensated (MoCo) framework. Using explicit motion modeling and the continuous prior of INRs, MoCo-INR can produce accurate cardiac motion decomposition and high-quality CMR reconstruction. Furthermore, we introduce a new INR network architecture tailored to the CMR problem, which significantly stabilizes model optimization. Experiments on retrospective (simulated) datasets demonstrate the superiority of MoCo-INR over state-of-the-art methods, achieving fast convergence and fine-detailed reconstructions at ultra-high acceleration factors (e.g., 20x in VISTA sampling). Additionally, evaluations on prospective (real-acquired) free-breathing CMR scans highlight the clinical practicality of MoCo-INR for real-time imaging. Several ablation studies further confirm the effectiveness of the critical components of MoCo-INR.

