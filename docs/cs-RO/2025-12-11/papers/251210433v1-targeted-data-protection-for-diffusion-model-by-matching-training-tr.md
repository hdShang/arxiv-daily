---
layout: default
title: Targeted Data Protection for Diffusion Model by Matching Training Trajectory
---

# Targeted Data Protection for Diffusion Model by Matching Training Trajectory

**arXiv**: [2512.10433v1](https://arxiv.org/abs/2512.10433) | [PDF](https://arxiv.org/pdf/2512.10433.pdf)

**作者**: Hojun Lee, Mijin Koo, Yeji Song, Nojun Kwak

---

## 💡 一句话要点

**提出TAFAP方法，通过匹配训练轨迹实现扩散模型的目标数据保护**

**关键词**: `扩散模型` `目标数据保护` `训练轨迹匹配` `对抗扰动` `微调控制` `隐私保护`

## 📋 核心要点

1. 核心问题：现有目标数据保护方法因快照匹配导致可控性差，无法稳定控制扩散模型输出
2. 方法要点：TAFAP采用轨迹匹配，结合对抗扰动微调，控制整个训练过程以实现持久保护
3. 实验或效果：实验显示TAFAP在身份和视觉模式上实现首个成功的目标转换，优于现有方法

## 📄 摘要（原文）

> Recent advancements in diffusion models have made fine-tuning text-to-image models for personalization increasingly accessible, but have also raised significant concerns regarding unauthorized data usage and privacy infringement. Current protection methods are limited to passively degrading image quality, failing to achieve stable control. While Targeted Data Protection (TDP) offers a promising paradigm for active redirection toward user-specified target concepts, existing TDP attempts suffer from poor controllability due to snapshot-matching approaches that fail to account for complete learning dynamics. We introduce TAFAP (Trajectory Alignment via Fine-tuning with Adversarial Perturbations), the first method to successfully achieve effective TDP by controlling the entire training trajectory. Unlike snapshot-based methods whose protective influence is easily diluted as training progresses, TAFAP employs trajectory-matching inspired by dataset distillation to enforce persistent, verifiable transformations throughout fine-tuning. We validate our method through extensive experiments, demonstrating the first successful targeted transformation in diffusion models with simultaneous control over both identity and visual patterns. TAFAP significantly outperforms existing TDP attempts, achieving robust redirection toward target concepts while maintaining high image quality. This work enables verifiable safeguards and provides a new framework for controlling and tracing alterations in diffusion model outputs.

