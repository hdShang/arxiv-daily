---
layout: default
title: Test-Time Matching: Unlocking Compositional Reasoning in Multimodal Models
---

# Test-Time Matching: Unlocking Compositional Reasoning in Multimodal Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.07632" class="toolbar-btn" target="_blank">📄 arXiv: 2510.07632v1</a>
  <a href="https://arxiv.org/pdf/2510.07632.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.07632v1" onclick="toggleFavorite(this, '2510.07632v1', 'Test-Time Matching: Unlocking Compositional Reasoning in Multimodal Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yinglun Zhu, Jiancheng Zhang, Fuzhi Tang

**分类**: cs.AI, cs.CL, cs.CV, cs.LG

**发布日期**: 2025-10-09

---

## 💡 一句话要点

**提出测试时匹配(TTM)算法，提升多模态模型在组合推理任务上的性能**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态学习` `组合推理` `测试时自适应` `视觉语言模型` `模型评估` `自监督学习`

## 📋 核心要点

1. 现有评估指标低估了多模态模型在组合推理上的能力，导致模型性能被错误评估。
2. 提出测试时匹配(TTM)算法，通过迭代优化模型在特定测试集上的表现，挖掘模型潜力。
3. 实验表明，TTM在多个数据集上显著提升了模型性能，甚至超越了GPT-4.1等先进模型。

## 📝 摘要（中文）

前沿AI模型取得了显著进展，但最近的研究表明，它们在组合推理方面表现不佳，在已建立的基准测试中通常表现得与随机水平相当甚至更低。本文重新审视了这个问题，并表明广泛使用的评估指标系统性地低估了模型的能力。为了解决这个问题，本文引入了一种组匹配得分，更好地利用了组结构，揭示了对比视觉-语言模型（VLM）和多模态大型语言模型（MLLM）中大量的隐藏能力。此外，简单地在测试时过拟合到诱导的组匹配，就可以将这种隐藏的能力转化为标准评估指标下的更高分数，从而缩小了报告中的大部分差距。这种调整使SigLIP-B16超越了所有先前的结果，GPT-4.1在Winoground上产生了第一个超过估计人类性能的结果。在此基础上，本文提出了一种测试时匹配（TTM）算法，这是一种迭代的、自我改进的算法，可以在没有任何外部监督的情况下进一步引导模型性能。TTM提供了额外的、重要的改进：例如，TTM使SigLIP-B16在MMVP-VLM上超越了GPT-4.1，建立了一个新的state of the art。重要的是，TTM即使在没有度量诱导效应或组结构的基准测试中仍然广泛有效，在WhatsUp等具有挑战性的数据集上实现了高达85.7%的相对收益。在跨越不同设置的16个数据集变体中，实验表明TTM始终如一地提高了模型性能，并推进了组合推理的前沿。

## 🔬 方法详解

**问题定义**：现有评估方法在评估多模态模型组合推理能力时存在偏差，导致模型真实性能被低估。现有方法难以充分利用模型中蕴含的组合推理能力，在复杂场景下表现不佳。

**核心思路**：通过在测试阶段对模型进行自适应调整，使其更好地适应当前测试数据的分布，从而挖掘模型中隐藏的组合推理能力。核心思想是利用测试数据本身的信息来提升模型性能，无需额外的训练数据或监督信号。

**技术框架**：TTM算法是一个迭代的优化过程，主要包含以下步骤：1. 初始化：使用预训练的多模态模型。2. 推理：使用当前模型对测试数据进行推理，得到预测结果。3. 匹配：根据预测结果和测试数据的组结构，计算组匹配得分。4. 优化：根据组匹配得分，调整模型参数，使其更好地适应当前测试数据。5. 迭代：重复步骤2-4，直到模型性能收敛。

**关键创新**：TTM算法的关键创新在于其测试时自适应调整的能力。与传统的离线训练方法不同，TTM算法能够在测试阶段利用测试数据的信息来优化模型，从而更好地适应当前场景。这种自适应调整能够挖掘模型中隐藏的组合推理能力，显著提升模型性能。

**关键设计**：TTM算法的关键设计包括：1. 组匹配得分：用于衡量模型预测结果与测试数据组结构的一致性。2. 优化策略：用于根据组匹配得分调整模型参数，例如使用梯度下降等优化算法。3. 迭代次数：控制TTM算法的迭代次数，以平衡模型性能和计算成本。具体参数设置可能因数据集和模型而异，需要在实验中进行调整。

## 📊 实验亮点

TTM算法在多个数据集上取得了显著的性能提升。例如，在MMVP-VLM数据集上，TTM使SigLIP-B16超越了GPT-4.1，建立了新的state of the art。在WhatsUp数据集上，TTM实现了高达85.7%的相对收益。此外，TTM还使GPT-4.1在Winoground上产生了第一个超过估计人类性能的结果。这些实验结果表明，TTM算法能够有效提升多模态模型在组合推理任务上的性能。

## 🎯 应用场景

该研究成果可应用于各种需要组合推理能力的多模态任务，例如图像描述生成、视觉问答、机器人导航等。通过TTM算法，可以提升模型在复杂场景下的理解和推理能力，从而提高相关应用的性能和可靠性。该方法具有广泛的应用前景，尤其是在资源受限或无法获取大量训练数据的场景下。

## 📄 摘要（原文）

> Frontier AI models have achieved remarkable progress, yet recent studies suggest they struggle with compositional reasoning, often performing at or below random chance on established benchmarks. We revisit this problem and show that widely used evaluation metrics systematically underestimate model capability. To address this, we introduce a group matching score that better exploits group structure and reveals substantial hidden capability in both contrastive vision-language models (VLMs) and multimodal large language models (MLLMs). Moreover, simply overfitting to the induced group matchings at test time transfers this hidden capability into higher scores under standard evaluation metrics, closing much of the reported gap. This adjustment enables SigLIP-B16 to surpass all previous results and GPT-4.1 to yield the first result surpassing estimated human performance on Winoground.
>   Building on this insight, we propose Test-Time Matching (TTM), an iterative, self-improving algorithm that further bootstraps model performance without any external supervision. TTM delivers additional, non-trivial improvements: for example, TTM enables SigLIP-B16 to surpass GPT-4.1 on MMVP-VLM, establishing a new state of the art. Importantly, TTM remains broadly effective even on benchmarks without metric-induced effects or group structures, achieving relative gains up to 85.7% on challenging datasets such as WhatsUp. Across 16 dataset variants spanning diverse setups, our experiments demonstrate that TTM consistently improves model performance and advances the frontier of compositional reasoning.

