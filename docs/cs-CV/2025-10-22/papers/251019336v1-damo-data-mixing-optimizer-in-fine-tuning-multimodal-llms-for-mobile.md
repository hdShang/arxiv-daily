---
layout: default
title: "DaMo: Data Mixing Optimizer in Fine-tuning Multimodal LLMs for Mobile Phone Agents"
---

# DaMo: Data Mixing Optimizer in Fine-tuning Multimodal LLMs for Mobile Phone Agents

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.19336" class="toolbar-btn" target="_blank">📄 arXiv: 2510.19336v1</a>
  <a href="https://arxiv.org/pdf/2510.19336.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.19336v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.19336v1', 'DaMo: Data Mixing Optimizer in Fine-tuning Multimodal LLMs for Mobile Phone Agents')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kai Shi, Jun Yang, Ni Yang, Binqiang Pan, Qingsong Xie, Chao Zhang, Zhenyu Yang, Tianhuang Su, Haonan Lu

**分类**: cs.CV

**发布日期**: 2025-10-22

**🔗 代码/项目**: [GITHUB](https://github.com/OPPO-Mente-Lab/DaMo.git)

---

## 💡 一句话要点

**DaMo：用于手机Agent多模态LLM微调的数据混合优化器**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态学习` `数据混合` `模型微调` `手机Agent` `性能预测`

## 📋 核心要点

1. 现有MLLM在处理复杂多任务手机Agent场景时，缺乏有效的数据混合策略，导致性能受限。
2. DaMo通过可训练网络预测不同数据混合比例下的任务性能，从而优化数据混合，提升模型效果。
3. 实验表明，DaMo在PhoneAgentBench和多个通用基准测试中均优于现有方法，展现了良好的泛化能力。

## 📝 摘要（中文）

手机Agent（MPA）因其在各种场景中的广泛适用性而成为一个有前景的研究方向。多模态大型语言模型（MLLM）是MPA的基础，但它们在同时处理多个手机任务方面的有效性仍然有限。多任务监督微调（SFT）被广泛用于多任务学习，但现有方法难以确定实现最佳性能的最佳训练数据组成。为了解决这个问题，我们提出了DaMo（数据混合优化器）——一种新颖的解决方案，它采用可训练网络，通过预测任何给定数据集比例的下游任务性能来预测最佳数据混合。为了支持全面评估，我们引入了PhoneAgentBench，这是第一个专门用于评估MLLM在多模态手机任务上的基准，包含1235个QA对，涵盖各种真实的工业手机应用场景。DaMo在小规模试点实验中表现出强大的预测能力（R^2=0.81），并能有效地推断出最佳数据混合配置。结果表明，与替代方法相比，DaMo在PhoneAgentBench上实现了3.38%的性能提升。此外，在包括BFCL-v3、MME-Reasoning、MME-Perception和OCRBench在内的已建立基准上的大量实验表明，DaMo具有卓越的泛化能力，在平均得分方面优于其他方法2.57%。当仅用于BFCL-v3任务上的MLLM优化时，DaMo比其他方法提高了12.47%的指标。值得注意的是，DaMo保持了强大的可扩展性，在应用于其他模型架构时仍能保持其有效性。代码和数据集可在https://github.com/OPPO-Mente-Lab/DaMo.git获得。

## 🔬 方法详解

**问题定义**：论文旨在解决多模态大型语言模型（MLLM）在手机Agent任务中，如何有效利用多任务数据进行微调的问题。现有方法通常采用简单的多任务监督微调，但缺乏对不同任务数据比例的优化，导致模型性能难以达到最优。现有方法的痛点在于无法根据下游任务的实际表现，自适应地调整训练数据的混合比例。

**核心思路**：论文的核心思路是引入一个可训练的网络，该网络能够预测不同数据混合比例下，模型在下游任务上的性能表现。通过预测性能，DaMo可以找到最佳的数据混合比例，从而优化模型的训练过程。这种方法避免了手动调整数据比例的繁琐过程，并能够根据实际情况自适应地调整数据混合策略。

**技术框架**：DaMo的技术框架主要包含两个部分：一是数据混合模块，负责根据预测的最佳比例混合不同任务的数据；二是性能预测网络，负责预测不同数据混合比例下模型的性能。整个流程如下：首先，性能预测网络预测不同数据混合比例下的性能；然后，根据预测结果，数据混合模块选择最佳的数据混合比例；最后，使用混合后的数据对MLLM进行微调。

**关键创新**：DaMo最重要的技术创新点在于引入了可训练的性能预测网络，该网络能够有效地预测不同数据混合比例下的模型性能。与现有方法相比，DaMo能够自适应地调整数据混合策略，从而更好地利用多任务数据。此外，DaMo还提出了PhoneAgentBench，这是一个专门用于评估MLLM在多模态手机任务上的基准测试。

**关键设计**：性能预测网络的设计是关键。具体来说，该网络以数据混合比例作为输入，输出模型在下游任务上的预测性能。论文中使用了R^2作为评估预测性能的指标，并取得了0.81的R^2值，表明该网络具有较强的预测能力。损失函数的设计也至关重要，需要确保性能预测网络能够准确地预测模型性能，并引导数据混合模块选择最佳的数据混合比例。具体的网络结构和损失函数细节在论文中有详细描述。

## 📊 实验亮点

DaMo在PhoneAgentBench上实现了3.38%的性能提升，在BFCL-v3上提升了12.47%。在MME-Reasoning、MME-Perception和OCRBench等通用基准测试中，DaMo的平均得分也优于其他方法2.57%。这些结果表明，DaMo具有良好的泛化能力和优化效果，能够有效地提升MLLM在多模态任务中的性能。

## 🎯 应用场景

DaMo可应用于各种需要多模态信息处理的智能Agent场景，例如智能家居控制、自动驾驶辅助、以及各种移动应用助手。通过优化数据混合，DaMo能够提升模型在复杂任务中的性能，提高用户体验，并降低开发成本。未来，该技术有望在更多领域得到应用，推动人工智能技术的普及。

## 📄 摘要（原文）

> Mobile Phone Agents (MPAs) have emerged as a promising research direction due to their broad applicability across diverse scenarios. While Multimodal Large Language Models (MLLMs) serve as the foundation for MPAs, their effectiveness in handling multiple mobile phone tasks simultaneously remains limited. Although multitask supervised fine-tuning (SFT) is widely adopted for multitask learning, existing approaches struggle to determine optimal training data compositions for peak performance. To address this challenge, we propose DaMo (Data Mixture Optimizer) - a novel solution employing a trainable network that predicts optimal data mixtures by forecasting downstream task performance for any given dataset ratio. To support comprehensive evaluation, we introduce PhoneAgentBench, the first specialized benchmark to evaluate MLLMs on multimodal mobile phone tasks, comprising 1235 QA pairs spanning diverse real-world industrial mobile application scenarios. Demonstrating strong predictive capability (R^2=0.81) in small-scale pilot experiments, DaMo efficiently extrapolates optimal data mixing configurations. Our results show DaMo achieves a 3.38% performance improvement on PhoneAgentBench compared to alternative methods. Furthermore, extensive experiments across established benchmarks including BFCL-v3, MME-Reasoning, MME-Perception, and OCRBench reveal DaMo's superior generalization, outperforming other approaches by 2.57% in terms of average score. When used solely for MLLM optimization on the BFCL-v3 task, DaMo improves the metrics by 12.47% than other methods. Notably, DaMo maintains robust scalability, preserving its effectiveness when applied to other model architectures. The code and dataset are available at https://github.com/OPPO-Mente-Lab/DaMo.git

