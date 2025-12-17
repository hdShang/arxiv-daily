---
layout: default
title: Flow-Guided Implicit Neural Representation for Motion-Aware Dynamic MRI Reconstruction
---

# Flow-Guided Implicit Neural Representation for Motion-Aware Dynamic MRI Reconstruction

**arXiv**: [2511.16948v1](https://arxiv.org/abs/2511.16948) | [PDF](https://arxiv.org/pdf/2511.16948.pdf)

**作者**: Baoqing Li, Yuanyuan Liu, Congcong Liu, Qingyong Zhu, Jing Cheng, Yihang Zhou, Hao Chen, Zhuo-Xu Cui, Dong Liang

---

## 💡 一句话要点

**提出流引导隐式神经表示框架，联合重建动态MRI图像与运动场**

**关键词**: `动态MRI重建` `隐式神经表示` `光流估计` `联合优化` `运动补偿`

## 📋 核心要点

1. 动态MRI面临采样不足和运动伪影问题，传统方法依赖预估计光流易不准确
2. 使用两个隐式神经表示分别建模图像序列和光流，通过光流方程耦合作为正则化
3. 实验显示在心脏MRI上优于现有方法，提升重建质量、运动估计精度和时间一致性

## 📄 摘要（原文）

> Dynamic magnetic resonance imaging (dMRI) captures temporally-resolved anatomy but is often challenged by limited sampling and motion-induced artifacts. Conventional motion-compensated reconstructions typically rely on pre-estimated optical flow, which is inaccurate under undersampling and degrades reconstruction quality. In this work, we propose a novel implicit neural representation (INR) framework that jointly models both the dynamic image sequence and its underlying motion field. Specifically, one INR is employed to parameterize the spatiotemporal image content, while another INR represents the optical flow. The two are coupled via the optical flow equation, which serves as a physics-inspired regularization, in addition to a data consistency loss that enforces agreement with k-space measurements. This joint optimization enables simultaneous recovery of temporally coherent images and motion fields without requiring prior flow estimation. Experiments on dynamic cardiac MRI datasets demonstrate that the proposed method outperforms state-of-the-art motion-compensated and deep learning approaches, achieving superior reconstruction quality, accurate motion estimation, and improved temporal fidelity. These results highlight the potential of implicit joint modeling with flow-regularized constraints for advancing dMRI reconstruction.

