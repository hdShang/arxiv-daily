---
layout: default
title: SELF: A Robust Singular Value and Eigenvalue Approach for LLM Fingerprinting
---

# SELF: A Robust Singular Value and Eigenvalue Approach for LLM Fingerprinting

**arXiv**: [2512.03620v1](https://arxiv.org/abs/2512.03620) | [PDF](https://arxiv.org/pdf/2512.03620.pdf)

**作者**: Hanxiu Zhang, Yue Zheng

---

## 💡 一句话要点

**提出SELF方法，基于奇异值和特征值分解实现大语言模型鲁棒指纹识别以保护知识产权。**

**关键词**: `大语言模型` `指纹识别` `奇异值分解` `特征值分解` `知识产权保护` `鲁棒性`

## 📋 核心要点

1. 核心问题：现有大语言模型指纹识别方法易受虚假声明或权重操纵攻击，知识产权保护不足。
2. 方法要点：通过注意力权重奇异值和特征值分解提取变换不变指纹，结合少样本学习进行相似度比较。
3. 实验或效果：实验显示SELF在量化、剪枝和微调攻击下保持高检测准确率，代码已开源。

## 📄 摘要（原文）

> The protection of Intellectual Property (IP) in Large Language Models (LLMs) represents a critical challenge in contemporary AI research. While fingerprinting techniques have emerged as a fundamental mechanism for detecting unauthorized model usage, existing methods -- whether behavior-based or structural -- suffer from vulnerabilities such as false claim attacks or susceptible to weight manipulations. To overcome these limitations, we propose SELF, a novel intrinsic weight-based fingerprinting scheme that eliminates dependency on input and inherently resists false claims. SELF achieves robust IP protection through two key innovations: 1) unique, scalable and transformation-invariant fingerprint extraction via singular value and eigenvalue decomposition of LLM attention weights, and 2) effective neural network-based fingerprint similarity comparison based on few-shot learning and data augmentation. Experimental results demonstrate SELF maintains high IP infringement detection accuracy while showing strong robustness against various downstream modifications, including quantization, pruning, and fine-tuning attacks. Our code is available at https://github.com/HanxiuZhang/SELF_v2.

