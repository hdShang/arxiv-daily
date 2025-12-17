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

**提出DISCODE方法以解决图像描述评估在域偏移场景下的鲁棒性问题**

🎯 **匹配领域**: **强化学习**

**关键词**: `图像描述评估` `大型视觉语言模型` `域偏移鲁棒性` `测试时自适应` `无参考评估` `多模态任务` `高斯先验分布` `解析解优化`

## 📋 核心要点

1. 现有大型视觉语言模型在图像描述评估中，尤其在域偏移场景下，鲁棒性不足，难以与人类判断对齐。
2. DISCODE采用测试时自适应评估，引入ATT损失和高斯先验，通过解析解优化，无需微调即可提升评估分数鲁棒性。
3. 在MCEval和四个现有基准上，DISCODE作为无参考评估指标实现了最先进性能，验证了其跨域鲁棒性。

## 📝 摘要（中文）

大型视觉语言模型（LVLMs）在多模态任务中表现出色，但用于图像描述评估时，在域偏移场景下仍面临鲁棒性挑战。为解决此问题，本文引入了分布感知分数解码器（DISCODE），这是一种无需微调的新方法，能生成更符合人类判断的鲁棒评估分数。DISCODE的核心思想是测试时自适应评估方法，通过引入自适应测试时（ATT）损失，利用高斯先验分布提升分数估计的鲁棒性，并推导出高效的最小化解析解。此外，本文还提出了多域描述评估（MCEval）基准，覆盖六个不同领域，用于评估指标的鲁棒性。实验表明，DISCODE在MCEval和四个现有基准上作为无参考评估指标达到了最先进性能。

## 🔬 方法详解

DISCODE的整体框架基于测试时自适应评估，核心是分布感知分数解码器。关键技术创新点包括：引入自适应测试时（ATT）损失，该损失利用高斯先验分布来建模评估分数的分布特性，从而在域偏移下增强鲁棒性；通过推导出的解析解，在测试时高效最小化ATT损失，避免了传统微调的需求。与现有方法的主要区别在于，DISCODE无需额外训练或微调，直接利用LVLMs的预训练能力，通过统计先验自适应调整评估过程，提高了跨域一致性。

## 📊 实验亮点

DISCODE在MCEval基准上作为无参考评估指标达到最先进性能，同时在四个代表性现有基准上表现优异，显著提升了跨域鲁棒性，验证了ATT损失和解析解的有效性。

## 🎯 应用场景

该研究可应用于图像描述生成系统的自动评估，特别是在多领域或域偏移场景下，如医疗影像、艺术创作或自动驾驶中的视觉描述任务，为模型优化和基准测试提供鲁棒的评估工具。

## 📄 摘要（原文）

> Large vision-language models (LVLMs) have shown impressive performance across a broad range of multimodal tasks. However, robust image caption evaluation using LVLMs remains challenging, particularly under domain-shift scenarios. To address this issue, we introduce the Distribution-Aware Score Decoder (DISCODE), a novel finetuning-free method that generates robust evaluation scores better aligned with human judgments across diverse domains. The core idea behind DISCODE lies in its test-time adaptive evaluation approach, which introduces the Adaptive Test-Time (ATT) loss, leveraging a Gaussian prior distribution to improve robustness in evaluation score estimation. This loss is efficiently minimized at test time using an analytical solution that we derive. Furthermore, we introduce the Multi-domain Caption Evaluation (MCEval) benchmark, a new image captioning evaluation benchmark covering six distinct domains, designed to assess the robustness of evaluation metrics. In our experiments, we demonstrate that DISCODE achieves state-of-the-art performance as a reference-free evaluation metric across MCEval and four representative existing benchmarks.

