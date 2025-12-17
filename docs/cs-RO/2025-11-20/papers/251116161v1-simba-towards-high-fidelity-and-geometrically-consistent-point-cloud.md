---
layout: default
title: Simba: Towards High-Fidelity and Geometrically-Consistent Point Cloud Completion via Transformation Diffusion
---

# Simba: Towards High-Fidelity and Geometrically-Consistent Point Cloud Completion via Transformation Diffusion

**arXiv**: [2511.16161v1](https://arxiv.org/abs/2511.16161) | [PDF](https://arxiv.org/pdf/2511.16161.pdf)

**作者**: Lirui Zhang, Zhengkai Zhao, Zhi Zuo, Pan Gao, Jie Qin

---

## 💡 一句话要点

**提出Simba框架，通过变换扩散解决点云补全中细节保留与结构一致性问题**

**关键词**: `点云补全` `扩散模型` `对称变换` `分布学习` `Mamba架构` `几何一致性`

## 📋 核心要点

1. 核心问题：回归方法易过拟合且对输入噪声敏感，影响点云补全的鲁棒性
2. 方法要点：将点变换回归转为分布学习，结合对称先验与扩散模型生成
3. 实验或效果：在PCN等基准上验证了SOTA性能，提升细节与结构完整性

## 📄 摘要（原文）

> Point cloud completion is a fundamental task in 3D vision. A persistent challenge in this field is simultaneously preserving fine-grained details present in the input while ensuring the global structural integrity of the completed shape. While recent works leveraging local symmetry transformations via direct regression have significantly improved the preservation of geometric structure details, these methods suffer from two major limitations: (1) These regression-based methods are prone to overfitting which tend to memorize instant-specific transformations instead of learning a generalizable geometric prior. (2) Their reliance on point-wise transformation regression lead to high sensitivity to input noise, severely degrading their robustness and generalization. To address these challenges, we introduce Simba, a novel framework that reformulates point-wise transformation regression as a distribution learning problem. Our approach integrates symmetry priors with the powerful generative capabilities of diffusion models, avoiding instance-specific memorization while capturing robust geometric structures. Additionally, we introduce a hierarchical Mamba-based architecture to achieve high-fidelity upsampling. Extensive experiments across the PCN, ShapeNet, and KITTI benchmarks validate our method's state-of-the-art (SOTA) performance.

