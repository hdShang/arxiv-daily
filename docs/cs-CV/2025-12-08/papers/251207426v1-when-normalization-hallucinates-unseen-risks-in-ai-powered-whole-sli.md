---
layout: default
title: When normalization hallucinates: unseen risks in AI-powered whole slide image processing
---

# When normalization hallucinates: unseen risks in AI-powered whole slide image processing

**arXiv**: [2512.07426v1](https://arxiv.org/abs/2512.07426) | [PDF](https://arxiv.org/pdf/2512.07426.pdf)

**作者**: Karel Moens, Matthew B. Blaschko, Tinne Tuytelaars, Bart Diricx, Jonas De Vylder, Mustafa Yousif

---

## 💡 一句话要点

**提出图像比较度量以检测全切片图像归一化中的幻觉风险**

**关键词**: `全切片图像归一化` `幻觉检测` `计算病理学` `深度学习` `图像比较度量` `临床验证`

## 📋 核心要点

1. 核心问题：深度学习驱动的全切片图像归一化可能引入幻觉内容，威胁下游分析。
2. 方法要点：设计新颖图像比较度量，自动检测归一化输出中的幻觉。
3. 实验或效果：在真实临床数据上评估方法，揭示传统指标未捕捉的显著不一致和失败。

## 📄 摘要（原文）

> Whole slide image (WSI) normalization remains a vital preprocessing step in computational pathology. Increasingly driven by deep learning, these models learn to approximate data distributions from training examples. This often results in outputs that gravitate toward the average, potentially masking diagnostically important features. More critically, they can introduce hallucinated content, artifacts that appear realistic but are not present in the original tissue, posing a serious threat to downstream analysis. These hallucinations are nearly impossible to detect visually, and current evaluation practices often overlook them. In this work, we demonstrate that the risk of hallucinations is real and underappreciated. While many methods perform adequately on public datasets, we observe a concerning frequency of hallucinations when these same models are retrained and evaluated on real-world clinical data. To address this, we propose a novel image comparison measure designed to automatically detect hallucinations in normalized outputs. Using this measure, we systematically evaluate several well-cited normalization methods retrained on real-world data, revealing significant inconsistencies and failures that are not captured by conventional metrics. Our findings underscore the need for more robust, interpretable normalization techniques and stricter validation protocols in clinical deployment.

