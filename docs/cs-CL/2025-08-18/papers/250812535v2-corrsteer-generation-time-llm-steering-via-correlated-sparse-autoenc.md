---
layout: default
title: "CorrSteer: Generation-Time LLM Steering via Correlated Sparse Autoencoder Features"
---

# CorrSteer: Generation-Time LLM Steering via Correlated Sparse Autoencoder Features

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.12535" class="toolbar-btn" target="_blank">📄 arXiv: 2508.12535v2</a>
  <a href="https://arxiv.org/pdf/2508.12535.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.12535v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.12535v2', 'CorrSteer: Generation-Time LLM Steering via Correlated Sparse Autoencoder Features')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Seonglae Cho, Zekun Wu, Adriano Koshiyama

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-08-18 (更新: 2025-10-17)

**备注**: 42 pages, 9 tables

---

## 💡 一句话要点

**提出CorrSteer以解决稀疏自编码器特征选择问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `稀疏自编码器` `特征选择` `语言模型` `自动化引导` `性能提升` `自然语言处理` `机器学习`

## 📋 核心要点

1. 现有的稀疏自编码器在下游引导任务中受限于对比数据集和大规模激活存储，影响了其有效性。
2. CorrSteer通过在推理时将样本正确性与SAE激活相关联，自动选择特征并提取引导系数，简化了流程。
3. 实验结果表明，CorrSteer在多个基准测试中显著提升了任务性能，尤其在MMLU和HarmBench上取得了显著的性能提升。

## 📝 摘要（中文）

稀疏自编码器（SAEs）能够从大型语言模型（LLMs）中提取可解释特征，但在下游引导任务中的有效性受到对比数据集或大规模激活存储的限制。为了解决这些问题，本文提出了CorrSteer，通过在推理时将样本正确性与SAE激活相关联来选择特征。该方法仅使用推理时的激活来提取更相关的特征，从而减少虚假相关性，并从平均激活中获取引导系数，自动化整个流程。我们的研究在Gemma-2 2B和LLaMA-3.1 8B上显示出在问答、偏见缓解、越狱防护和推理基准测试中的任务性能提升，特别是在4000个样本中MMLU性能提高了3.3%，在仅108个样本中HarmBench提高了27.2%。所选特征展示了与每个任务要求相一致的语义模式，揭示了驱动性能的潜在能力。我们的工作确立了基于相关性的选择作为在语言模型应用中自动化SAE引导的有效且可扩展的方法。

## 🔬 方法详解

**问题定义**：本文旨在解决稀疏自编码器在下游引导任务中由于对比数据集和大规模激活存储而导致的有效性不足的问题。现有方法在特征选择上存在局限性，难以实现自动化和高效性。

**核心思路**：CorrSteer的核心思路是通过在推理阶段将样本的正确性与SAE的激活进行关联，从而选择出更相关的特征。这种设计旨在减少虚假相关性，并提高特征选择的准确性和效率。

**技术框架**：CorrSteer的整体架构包括特征选择模块和引导系数提取模块。在推理过程中，系统首先计算SAE的激活，然后根据样本的正确性进行特征选择，最后从平均激活中提取引导系数，形成自动化的引导流程。

**关键创新**：CorrSteer的主要创新在于引入了基于相关性的特征选择方法，区别于传统的依赖对比数据集的方式。这种方法不仅提高了特征选择的相关性，还实现了引导过程的自动化。

**关键设计**：在关键设计方面，CorrSteer使用了特定的激活计算方式和引导系数提取策略，确保在推理时能够高效地选择出与任务相关的特征，同时减少了对存储资源的需求。

## 📊 实验亮点

在实验中，CorrSteer在MMLU基准测试中实现了3.3%的性能提升，使用4000个样本；在HarmBench基准测试中，使用仅108个样本时实现了27.2%的性能提升。这些结果表明，CorrSteer在多个任务中显著提高了模型的有效性和可靠性。

## 🎯 应用场景

CorrSteer的研究成果在多个领域具有潜在应用价值，包括自然语言处理中的问答系统、偏见检测与缓解、以及安全性增强等。通过自动化特征选择和引导过程，该方法能够提高模型在实际应用中的性能和可靠性，未来可能推动更多智能系统的开发与优化。

## 📄 摘要（原文）

> Sparse Autoencoders (SAEs) can extract interpretable features from large language models (LLMs) without supervision. However, their effectiveness in downstream steering tasks is limited by the requirement for contrastive datasets or large activation storage. To address these limitations, we propose CorrSteer, which selects features by correlating sample correctness with SAE activations from generated tokens at inference time. This approach uses only inference-time activations to extract more relevant features, thereby reducing spurious correlations. It also obtains steering coefficients from average activations, automating the entire pipeline. Our method shows improved task performance on QA, bias mitigation, jailbreaking prevention, and reasoning benchmarks on Gemma-2 2B and LLaMA-3.1 8B, notably achieving a +3.3% improvement in MMLU performance with 4000 samples and a +27.2% improvement in HarmBench with only 108 samples. Selected features demonstrate semantically meaningful patterns aligned with each task's requirements, revealing the underlying capabilities that drive performance. Our work establishes correlation-based selection as an effective and scalable approach for automated SAE steering across language model applications.

