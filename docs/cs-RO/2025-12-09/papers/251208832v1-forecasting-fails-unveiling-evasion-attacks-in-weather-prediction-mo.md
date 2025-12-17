---
layout: default
title: Forecasting Fails: Unveiling Evasion Attacks in Weather Prediction Models
---

# Forecasting Fails: Unveiling Evasion Attacks in Weather Prediction Models

**arXiv**: [2512.08832v1](https://arxiv.org/abs/2512.08832) | [PDF](https://arxiv.org/pdf/2512.08832.pdf)

**作者**: Huzaifa Arif, Pin-Yu Chen, Alex Gittens, James Diffenderfer, Bhavya Kailkhura

---

## 💡 一句话要点

**提出WAAPO框架以生成针对天气预测模型的隐蔽对抗扰动**

**关键词**: `天气预测模型` `对抗攻击` `扰动优化` `物理约束` `模型脆弱性`

## 📋 核心要点

1. 核心问题：评估AI天气预测模型对对抗扰动的脆弱性，需生成物理真实且不易察觉的扰动。
2. 方法要点：WAAPO通过通道稀疏性、空间局部性和平滑性约束，优化生成目标对抗扰动。
3. 实验或效果：在ERA5数据集和FourCastNet上，WAAPO能生成与预设目标紧密对齐的对抗轨迹，揭示模型关键漏洞。

## 📄 摘要（原文）

> With the increasing reliance on AI models for weather forecasting, it is imperative to evaluate their vulnerability to adversarial perturbations. This work introduces Weather Adaptive Adversarial Perturbation Optimization (WAAPO), a novel framework for generating targeted adversarial perturbations that are both effective in manipulating forecasts and stealthy to avoid detection. WAAPO achieves this by incorporating constraints for channel sparsity, spatial localization, and smoothness, ensuring that perturbations remain physically realistic and imperceptible. Using the ERA5 dataset and FourCastNet (Pathak et al. 2022), we demonstrate WAAPO's ability to generate adversarial trajectories that align closely with predefined targets, even under constrained conditions. Our experiments highlight critical vulnerabilities in AI-driven forecasting models, where small perturbations to initial conditions can result in significant deviations in predicted weather patterns. These findings underscore the need for robust safeguards to protect against adversarial exploitation in operational forecasting systems.

