---
layout: default
title: "HeadHunt-VAD: Hunting Robust Anomaly-Sensitive Heads in MLLM for Tuning-Free Video Anomaly Detection"
---

# HeadHunt-VAD: Hunting Robust Anomaly-Sensitive Heads in MLLM for Tuning-Free Video Anomaly Detection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.17601" class="toolbar-btn" target="_blank">📄 arXiv: 2512.17601v1</a>
  <a href="https://arxiv.org/pdf/2512.17601.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.17601v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.17601v1', 'HeadHunt-VAD: Hunting Robust Anomaly-Sensitive Heads in MLLM for Tuning-Free Video Anomaly Detection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhaolin Cai, Fan Li, Ziwei Zheng, Haixia Bi, Lijun He

**分类**: cs.CV

**发布日期**: 2025-12-19

---

## 💡 一句话要点

**HeadHunt-VAD：在MLLM中寻找异常敏感头，实现免调优视频异常检测**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视频异常检测` `多模态大语言模型` `注意力机制` `免调优学习` `鲁棒性` `异常敏感头` `知识挖掘`

## 📋 核心要点

1. 现有视频异常检测方法依赖大量标注数据和高计算成本，且基于MLLM的免调优方法存在信息损失和常态偏差。
2. HeadHunt-VAD通过直接在冻结的MLLM中寻找鲁棒的异常敏感注意力头，绕过文本生成，提升异常检测能力。
3. 实验表明，HeadHunt-VAD在两个VAD基准测试中实现了最先进的免调优性能，验证了头部级别探测的有效性。

## 📝 摘要（中文）

视频异常检测（VAD）旨在定位视频中偏离正常模式的事件。传统方法通常依赖于大量的标注数据，并产生高昂的计算成本。最近基于多模态大型语言模型（MLLM）的免调优方法，通过利用其丰富的世界知识，提供了一种有前景的替代方案。然而，这些方法通常依赖于文本输出，这会引入信息损失，表现出常态偏差，并受到提示敏感性的影响，使其不足以捕捉细微的异常线索。为了解决这些限制，我们提出了HeadHunt-VAD，一种新颖的免调优VAD范式，它通过直接在冻结的MLLM中寻找鲁棒的异常敏感内部注意力头来绕过文本生成。我们方法的核心是一个鲁棒头识别模块，该模块使用显着性和稳定性的多标准分析系统地评估所有注意力头，从而识别出在不同提示中始终具有区分性的稀疏头子集。然后，来自这些专家头的特征被馈送到轻量级异常评分器和时间定位器，从而能够以可解释的输出实现高效准确的异常检测。大量的实验表明，HeadHunt-VAD在两个主要的VAD基准测试中，在免调优方法中实现了最先进的性能，同时保持了高效率，验证了MLLM中的头部级别探测是用于实际异常检测的强大而实用的解决方案。

## 🔬 方法详解

**问题定义**：视频异常检测旨在识别视频中不符合正常模式的事件。现有基于多模态大语言模型（MLLM）的免调优方法，虽然避免了昂贵的微调过程，但依赖文本输出，导致信息损失，易受常态偏差影响，且对提示词敏感，难以捕捉细微异常。

**核心思路**：HeadHunt-VAD的核心在于直接挖掘MLLM内部的注意力机制，寻找那些对异常事件具有高度敏感性和鲁棒性的注意力头。通过分析这些“专家”注意力头的输出，绕过文本生成环节，从而更直接地捕捉视频中的异常信息。

**技术框架**：HeadHunt-VAD主要包含两个模块：鲁棒头识别模块和异常检测模块。鲁棒头识别模块负责从MLLM中筛选出对异常敏感且稳定的注意力头；异常检测模块则利用这些注意力头的特征进行异常评分和时间定位。整个流程无需对MLLM进行任何微调。

**关键创新**：该方法最重要的创新点在于将视频异常检测问题转化为对预训练MLLM内部知识的挖掘。通过寻找对异常事件具有区分性的注意力头，实现了免调优的异常检测，避免了传统方法对大量标注数据的依赖，并解决了文本输出带来的信息损失问题。

**关键设计**：鲁棒头识别模块采用多标准分析方法，综合考虑注意力头的显著性和稳定性。显著性评估注意力头对异常事件的响应强度，稳定性评估注意力头在不同提示下的响应一致性。通过设定阈值，筛选出既显著又稳定的注意力头子集。异常检测模块使用轻量级的异常评分器和时间定位器，例如简单的线性层或GRU网络，以实现高效的异常检测。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17601v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17601v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17601v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

HeadHunt-VAD在ShanghaiTech和UCF-Crime两个主流视频异常检测数据集上取得了显著的性能提升，在免调优方法中达到了state-of-the-art水平。实验结果表明，该方法能够有效识别异常事件，并具有较高的检测精度和效率，验证了其在实际应用中的可行性。

## 🎯 应用场景

HeadHunt-VAD具有广泛的应用前景，例如智能监控、工业质检、医疗影像分析等领域。该方法无需针对特定场景进行模型微调，降低了部署成本，提高了应用灵活性。未来，该技术有望应用于更复杂的异常检测任务，例如多模态异常检测、小样本异常检测等。

## 📄 摘要（原文）

> Video Anomaly Detection (VAD) aims to locate events that deviate from normal patterns in videos. Traditional approaches often rely on extensive labeled data and incur high computational costs. Recent tuning-free methods based on Multimodal Large Language Models (MLLMs) offer a promising alternative by leveraging their rich world knowledge. However, these methods typically rely on textual outputs, which introduces information loss, exhibits normalcy bias, and suffers from prompt sensitivity, making them insufficient for capturing subtle anomalous cues. To address these constraints, we propose HeadHunt-VAD, a novel tuning-free VAD paradigm that bypasses textual generation by directly hunting robust anomaly-sensitive internal attention heads within the frozen MLLM. Central to our method is a Robust Head Identification module that systematically evaluates all attention heads using a multi-criteria analysis of saliency and stability, identifying a sparse subset of heads that are consistently discriminative across diverse prompts. Features from these expert heads are then fed into a lightweight anomaly scorer and a temporal locator, enabling efficient and accurate anomaly detection with interpretable outputs. Extensive experiments show that HeadHunt-VAD achieves state-of-the-art performance among tuning-free methods on two major VAD benchmarks while maintaining high efficiency, validating head-level probing in MLLMs as a powerful and practical solution for real-world anomaly detection.

