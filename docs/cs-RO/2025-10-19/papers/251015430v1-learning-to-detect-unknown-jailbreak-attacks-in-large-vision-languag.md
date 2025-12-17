---
layout: default
title: Learning to Detect Unknown Jailbreak Attacks in Large Vision-Language Models
---

# Learning to Detect Unknown Jailbreak Attacks in Large Vision-Language Models

**arXiv**: [2510.15430v1](https://arxiv.org/abs/2510.15430) | [PDF](https://arxiv.org/pdf/2510.15430.pdf)

**作者**: Shuang Liang, Zhihao Xu, Jialing Tao, Hui Xue, Xiting Wang

---

## 💡 一句话要点

**提出学习检测框架以解决大型视觉语言模型未知越狱攻击检测问题**

**关键词**: `大型视觉语言模型` `越狱攻击检测` `多模态安全表示` `无监督分类` `泛化性提升`

## 📋 核心要点

1. 大型视觉语言模型易受未知越狱攻击，现有方法泛化性差或效率低
2. 框架包括多模态安全概念激活向量模块和安全模式自动编码器模块
3. 实验显示在多种未知攻击上检测AUROC更高且效率提升

## 📄 摘要（原文）

> Despite extensive alignment efforts, Large Vision-Language Models (LVLMs)
> remain vulnerable to jailbreak attacks, posing serious safety risks. To address
> this, existing detection methods either learn attack-specific parameters, which
> hinders generalization to unseen attacks, or rely on heuristically sound
> principles, which limit accuracy and efficiency. To overcome these limitations,
> we propose Learning to Detect (LoD), a general framework that accurately
> detects unknown jailbreak attacks by shifting the focus from attack-specific
> learning to task-specific learning. This framework includes a Multi-modal
> Safety Concept Activation Vector module for safety-oriented representation
> learning and a Safety Pattern Auto-Encoder module for unsupervised attack
> classification. Extensive experiments show that our method achieves
> consistently higher detection AUROC on diverse unknown attacks while improving
> efficiency. The code is available at
> https://anonymous.4open.science/r/Learning-to-Detect-51CB.

