---
layout: default
title: "Alignment Quality Index (AQI) : Beyond Refusals: AQI as an Intrinsic Alignment Diagnostic via Latent Geometry, Cluster Divergence, and Layer wise Pooled Representations"
---

# Alignment Quality Index (AQI) : Beyond Refusals: AQI as an Intrinsic Alignment Diagnostic via Latent Geometry, Cluster Divergence, and Layer wise Pooled Representations

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.13901" class="toolbar-btn" target="_blank">📄 arXiv: 2506.13901v1</a>
  <a href="https://arxiv.org/pdf/2506.13901.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.13901v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.13901v1', 'Alignment Quality Index (AQI) : Beyond Refusals: AQI as an Intrinsic Alignment Diagnostic via Latent Geometry, Cluster Divergence, and Layer wise Pooled Representations')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Abhilekh Borah, Chhavi Sharma, Danush Khanna, Utkarsh Bhatt, Gurpreet Singh, Hasnat Md Abdullah, Raghav Kaushik Ravi, Vinija Jain, Jyoti Patel, Shubham Singh, Vasu Sharma, Arpita Vats, Rahul Raja, Aman Chadha, Amitava Das

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-16

---

## 💡 一句话要点

**提出AQI以解决大型语言模型对齐评估问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `对齐质量指数` `大型语言模型` `潜在空间` `聚类分析` `安全性评估` `LITMUS数据集` `对齐评估` `几何度量`

## 📋 核心要点

1. 现有的对齐评估方法如拒绝率和毒性分类器存在盲点，无法全面反映大型语言模型的对齐情况。
2. 本文提出的对齐质量指数（AQI）通过分析潜在空间中的激活分离，提供了一种新的几何度量来评估模型对齐。
3. 在LITMUS数据集上的实验证明，AQI能够有效揭示模型的脆弱性，并与外部评判者的评估结果高度相关。

## 📝 摘要（中文）

对齐已成为大型语言模型（LLMs）在教育、医疗、治理和法律等高风险领域的必要条件。现有评估方法依赖于行为代理，如拒绝率和毒性分类器，存在显著盲点。为此，本文提出了对齐质量指数（AQI），通过分析潜在空间中安全与不安全激活的分离，提供了一种几何和提示不变的度量。AQI结合多种聚类质量指标，能够检测隐藏的错位和越狱风险，并作为对齐伪装的早期警告信号。此外，本文还提出了LITMUS数据集，以支持在复杂条件下的稳健评估。实验证明AQI与外部评判者的相关性，并揭示了拒绝指标未能捕捉的脆弱性。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型对齐评估的不足，现有方法如拒绝率和毒性分类器无法全面捕捉模型的对齐情况，导致潜在风险未被识别。

**核心思路**：提出对齐质量指数（AQI），通过分析潜在空间中安全与不安全激活的分离，提供一种几何和提示不变的度量，能够更准确地评估模型的对齐程度。

**技术框架**：AQI结合了Davies-Bouldin Score、Dunn Index、Xie-Beni Index和Calinski-Harabasz Index等多种聚类质量指标，形成一个综合评估框架。该框架通过聚类分析来检测模型的隐藏错位和越狱风险。

**关键创新**：AQI的最大创新在于其几何性质和提示不变性，使其能够在不同的生成条件下保持稳定性，超越了传统的行为代理评估方法。

**关键设计**：在AQI的实现中，采用了多种聚类指标的组合，以确保评估的全面性和准确性，同时设计了LITMUS数据集以支持在复杂条件下的评估。具体的参数设置和损失函数设计在文中进行了详细描述。

## 📊 实验亮点

在LITMUS数据集上的实验结果显示，AQI与外部评判者的评估结果具有高度相关性，能够有效揭示拒绝指标未能捕捉的脆弱性。AQI的引入使得模型的对齐评估更加全面，提升了对齐检测的准确性。

## 🎯 应用场景

AQI的提出为大型语言模型在高风险领域的应用提供了新的评估工具，能够帮助开发者更好地理解和优化模型的对齐程度，确保其输出符合人类价值观和安全标准。未来，AQI有望在教育、医疗和法律等领域得到广泛应用，提升模型的安全性和可靠性。

## 📄 摘要（原文）

> Alignment is no longer a luxury, it is a necessity. As large language models (LLMs) enter high-stakes domains like education, healthcare, governance, and law, their behavior must reliably reflect human-aligned values and safety constraints. Yet current evaluations rely heavily on behavioral proxies such as refusal rates, G-Eval scores, and toxicity classifiers, all of which have critical blind spots. Aligned models are often vulnerable to jailbreaking, stochasticity of generation, and alignment faking.
>   To address this issue, we introduce the Alignment Quality Index (AQI). This novel geometric and prompt-invariant metric empirically assesses LLM alignment by analyzing the separation of safe and unsafe activations in latent space. By combining measures such as the Davies-Bouldin Score (DBS), Dunn Index (DI), Xie-Beni Index (XBI), and Calinski-Harabasz Index (CHI) across various formulations, AQI captures clustering quality to detect hidden misalignments and jailbreak risks, even when outputs appear compliant. AQI also serves as an early warning signal for alignment faking, offering a robust, decoding invariant tool for behavior agnostic safety auditing.
>   Additionally, we propose the LITMUS dataset to facilitate robust evaluation under these challenging conditions. Empirical tests on LITMUS across different models trained under DPO, GRPO, and RLHF conditions demonstrate AQI's correlation with external judges and ability to reveal vulnerabilities missed by refusal metrics. We make our implementation publicly available to foster future research in this area.

