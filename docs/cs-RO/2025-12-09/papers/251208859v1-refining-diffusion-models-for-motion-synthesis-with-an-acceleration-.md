---
layout: default
title: Refining Diffusion Models for Motion Synthesis with an Acceleration Loss to Generate Realistic IMU Data
---

# Refining Diffusion Models for Motion Synthesis with an Acceleration Loss to Generate Realistic IMU Data

**arXiv**: [2512.08859v1](https://arxiv.org/abs/2512.08859) | [PDF](https://arxiv.org/pdf/2512.08859.pdf)

**作者**: Lars Ole Häusler, Lena Uhlenberg, Göran Köber, Diyora Salimova, Oliver Amft

---

## 💡 一句话要点

**提出基于加速度损失的扩散模型微调方法，以生成更真实的IMU运动数据**

**关键词**: `扩散模型` `运动合成` `IMU数据生成` `加速度损失` `人类活动识别` `文本到运动`

## 📋 核心要点

1. 核心问题：现有文本到IMU运动合成框架生成的加速度信号不够真实，影响下游应用如人类活动识别。
2. 方法要点：通过引入加速度二阶损失（L_acc）微调预训练扩散模型，增强生成运动的时间一致性，对齐IMU加速度模式。
3. 实验或效果：L_acc降低12.7%，高动态活动改进显著；合成IMU数据分布更接近真实数据，HAR分类性能提升8.7%。

## 📄 摘要（原文）

> We propose a text-to-IMU (inertial measurement unit) motion-synthesis framework to obtain realistic IMU data by fine-tuning a pretrained diffusion model with an acceleration-based second-order loss (L_acc). L_acc enforces consistency in the discrete second-order temporal differences of the generated motion, thereby aligning the diffusion prior with IMU-specific acceleration patterns. We integrate L_acc into the training objective of an existing diffusion model, finetune the model to obtain an IMU-specific motion prior, and evaluate the model with an existing text-to-IMU framework that comprises surface modelling and virtual sensor simulation. We analysed acceleration signal fidelity and differences between synthetic motion representation and actual IMU recordings. As a downstream application, we evaluated Human Activity Recognition (HAR) and compared the classification performance using data of our method with the earlier diffusion model and two additional diffusion model baselines. When we augmented the earlier diffusion model objective with L_acc and continued training, L_acc decreased by 12.7% relative to the original model. The improvements were considerably larger in high-dynamic activities (i.e., running, jumping) compared to low-dynamic activities~(i.e., sitting, standing). In a low-dimensional embedding, the synthetic IMU data produced by our refined model shifts closer to the distribution of real IMU recordings. HAR classification trained exclusively on our refined synthetic IMU data improved performance by 8.7% compared to the earlier diffusion model and by 7.6% over the best-performing comparison diffusion model. We conclude that acceleration-aware diffusion refinement provides an effective approach to align motion generation and IMU synthesis and highlights how flexible deep learning pipelines are for specialising generic text-to-motion priors to sensor-specific tasks.

