---
layout: default
title: DISCODE: Distribution-Aware Score Decoder for Robust Automatic Evaluation of Image Captioning
---

# DISCODE: Distribution-Aware Score Decoder for Robust Automatic Evaluation of Image Captioning

**arXiv**: [2512.14420v1](https://arxiv.org/abs/2512.14420) | [PDF](https://arxiv.org/pdf/2512.14420.pdf)

**作者**: Nakamasa Inoue, Kanoko Goto, Masanari Oi, Martyna Gruszka, Mahiro Ukai, Takumi Hirose, Yusuke Sekikawa

**分类**: cs.CV, cs.AI

**发布日期**: 2025-12-16

**备注**: Paper accepted to AAAI 2026

---

## 💡 一句话要点

**提出DISCODE分布感知分数解码器，以解决大视觉语言模型在跨域图像描述评估中的鲁棒性问题。**

**关键词**: `图像描述评估` `大视觉语言模型` `跨域鲁棒性` `测试时自适应` `无参考评估` `多模态任务` `高斯先验分布` `自动评估指标`

## 📋 核心要点

1. 现有大视觉语言模型在图像描述评估中，尤其在跨域场景下，鲁棒性不足，难以与人类判断对齐。
2. 提出DISCODE方法，基于测试时自适应评估，引入ATT损失和高斯先验，无需微调即可提升评估分数鲁棒性。
3. 在MCEval和四个现有基准上，DISCODE作为无参考评估指标实现了最先进的性能，验证了其有效性。

## 📝 摘要（中文）

大视觉语言模型（LVLMs）在多模态任务中表现出色，但在图像描述评估中，尤其是在域偏移场景下，鲁棒性仍面临挑战。为解决这一问题，我们提出了分布感知分数解码器（DISCODE），这是一种无需微调的新方法，能够生成更符合人类判断的鲁棒评估分数。DISCODE的核心思想是测试时自适应评估方法，引入了自适应测试时（ATT）损失，利用高斯先验分布提高评估分数估计的鲁棒性。我们推导出该损失的解析解，可在测试时高效最小化。此外，我们提出了多域描述评估（MCEval）基准，这是一个覆盖六个不同领域的新图像描述评估基准，旨在评估评估指标的鲁棒性。实验表明，DISCODE在MCEval和四个现有基准上作为无参考评估指标达到了最先进的性能。

## 🔬 方法详解

DISCODE的整体框架是一个测试时自适应评估系统，核心创新点包括：1）引入自适应测试时（ATT）损失，该损失基于高斯先验分布，旨在优化评估分数估计的鲁棒性；2）推导出ATT损失的解析解，允许在测试时高效计算和最小化损失，无需额外训练或微调。与现有方法的主要区别在于，DISCODE不依赖于模型微调，而是通过测试时自适应机制直接调整评估过程，利用分布信息来减少域偏移影响，从而在跨域场景下提供更稳定和准确的评估分数。

## 📊 实验亮点

DISCODE在MCEval基准（覆盖六个领域）和四个现有基准上作为无参考评估指标达到了最先进的性能，显著提升了跨域评估的鲁棒性，与人类判断更一致，验证了其方法的有效性。

## 🎯 应用场景

该研究可应用于图像描述生成系统的自动评估，特别是在多领域或跨域场景下，如新闻、医疗、艺术等，帮助开发者和研究者快速、鲁棒地评估模型性能，减少人工标注成本，推动多模态AI技术的实际部署。

## 📄 摘要（原文）

> Large vision-language models (LVLMs) have shown impressive performance across a broad range of multimodal tasks. However, robust image caption evaluation using LVLMs remains challenging, particularly under domain-shift scenarios. To address this issue, we introduce the Distribution-Aware Score Decoder (DISCODE), a novel finetuning-free method that generates robust evaluation scores better aligned with human judgments across diverse domains. The core idea behind DISCODE lies in its test-time adaptive evaluation approach, which introduces the Adaptive Test-Time (ATT) loss, leveraging a Gaussian prior distribution to improve robustness in evaluation score estimation. This loss is efficiently minimized at test time using an analytical solution that we derive. Furthermore, we introduce the Multi-domain Caption Evaluation (MCEval) benchmark, a new image captioning evaluation benchmark covering six distinct domains, designed to assess the robustness of evaluation metrics. In our experiments, we demonstrate that DISCODE achieves state-of-the-art performance as a reference-free evaluation metric across MCEval and four representative existing benchmarks.

