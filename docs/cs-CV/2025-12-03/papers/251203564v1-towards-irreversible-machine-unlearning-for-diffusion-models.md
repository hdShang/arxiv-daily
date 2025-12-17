---
layout: default
title: Towards Irreversible Machine Unlearning for Diffusion Models
---

# Towards Irreversible Machine Unlearning for Diffusion Models

**arXiv**: [2512.03564v1](https://arxiv.org/abs/2512.03564) | [PDF](https://arxiv.org/pdf/2512.03564.pdf)

**作者**: Xun Yuan, Zilong Zhao, Jiayu Li, Aryan Pasikhani, Prosanta Gope, Biplab Sikdar

---

## 💡 一句话要点

**提出DiMRA攻击与DiMUM方法以增强扩散模型机器遗忘的鲁棒性**

**关键词**: `扩散模型` `机器遗忘` `鲁棒性增强` `对抗攻击` `微调方法` `生成模型`

## 📋 核心要点

1. 核心问题：基于微调的扩散模型机器遗忘方法易受DiMRA攻击，导致遗忘内容被重新学习
2. 方法要点：DiMUM通过记忆替代数据来防止生成目标遗忘元素，而非直接遗忘
3. 实验或效果：DiMRA成功逆转现有遗忘方法，DiMUM在保持生成性能的同时增强对抗攻击的鲁棒性

## 📄 摘要（原文）

> Diffusion models are renowned for their state-of-the-art performance in generating synthetic images. However, concerns related to safety, privacy, and copyright highlight the need for machine unlearning, which can make diffusion models forget specific training data and prevent the generation of sensitive or unwanted content. Current machine unlearning methods for diffusion models are primarily designed for conditional diffusion models and focus on unlearning specific data classes or features. Among these methods, finetuning-based machine unlearning methods are recognized for their efficiency and effectiveness, which update the parameters of pre-trained diffusion models by minimizing carefully designed loss functions. However, in this paper, we propose a novel attack named Diffusion Model Relearning Attack (DiMRA), which can reverse the finetuning-based machine unlearning methods, posing a significant vulnerability of this kind of technique. Without prior knowledge of the unlearning elements, DiMRA optimizes the unlearned diffusion model on an auxiliary dataset to reverse the unlearning, enabling the model to regenerate previously unlearned elements. To mitigate this vulnerability, we propose a novel machine unlearning method for diffusion models, termed as Diffusion Model Unlearning by Memorization (DiMUM). Unlike traditional methods that focus on forgetting, DiMUM memorizes alternative data or features to replace targeted unlearning data or features in order to prevent generating such elements. In our experiments, we demonstrate the effectiveness of DiMRA in reversing state-of-the-art finetuning-based machine unlearning methods for diffusion models, highlighting the need for more robust solutions. We extensively evaluate DiMUM, demonstrating its superior ability to preserve the generative performance of diffusion models while enhancing robustness against DiMRA.

