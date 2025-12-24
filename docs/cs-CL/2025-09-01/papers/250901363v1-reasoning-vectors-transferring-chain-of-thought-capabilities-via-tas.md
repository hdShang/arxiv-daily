---
layout: default
title: "Reasoning Vectors: Transferring Chain-of-Thought Capabilities via Task Arithmetic"
---

# Reasoning Vectors: Transferring Chain-of-Thought Capabilities via Task Arithmetic

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.01363" class="toolbar-btn" target="_blank">📄 arXiv: 2509.01363v1</a>
  <a href="https://arxiv.org/pdf/2509.01363.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.01363v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.01363v1', 'Reasoning Vectors: Transferring Chain-of-Thought Capabilities via Task Arithmetic')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mohammad Zbeeb, Hasan Abed Al Kader Hammoud, Bernard Ghanem

**分类**: cs.CL

**发布日期**: 2025-09-01

**备注**: Under Review

---

## 💡 一句话要点

**通过任务算术迁移Chain-of-Thought能力：提取并复用LLM推理向量**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `推理能力迁移` `任务向量算术` `强化学习` `监督微调` `大语言模型` `模型优化`

## 📋 核心要点

1. 现有大型语言模型推理能力依赖昂贵的强化学习优化，成本高昂。
2. 论文提出通过任务向量算术，将已训练模型的推理能力迁移到其他模型。
3. 实验表明，该方法在多个推理基准上显著提升性能，且具有鲁棒性。

## 📝 摘要（中文）

大型语言模型通常需要昂贵的优化，例如强化学习，才能掌握复杂的推理任务。本文证明，推理能力一旦被学习，就可以作为紧凑的任务向量在模型之间提取和转移。我们使用了两个公开可用的、相同初始化的Qwen2.5模型，一个通过监督微调（SFT）进行微调，另一个通过组相对策略优化（GRPO）在相同数据集上进行微调。由此，我们提取了一个推理向量：$v_{\text{reason}} = θ_{\text{GRPO}} - θ_{\text{SFT}}$。我们假设这个向量捕获了强化学习所灌输的推理能力，同时剔除了SFT过程中的共享知识。当通过简单的算术将其添加到兼容的指令调整模型时，这个向量始终如一地提高了各种推理基准的性能：GSM8K (+4.9%)，HumanEval (+4.3%)，SciQ (+1.7%)，以及BigBenchHard（1.5B模型+12.3%）。性能提升在对抗条件下仍然存在。相反，减去该向量会导致显著的性能下降（GSM8K上-11.8%），表明该向量对模型的推理能力有很强的贡献。这项工作展示了如何从现有的开源模型中提取通常通过昂贵训练开发的推理能力，并通过简单的张量算术重用，从而提供了一种通过回收先前的计算投资来增强模型的实用方法。

## 🔬 方法详解

**问题定义**：现有大型语言模型（LLM）在复杂推理任务上表现出色，但通常需要耗费大量计算资源的强化学习进行优化。如何降低推理能力训练的成本，并实现推理能力的有效迁移，是本文要解决的核心问题。现有方法，如直接进行监督微调或从头开始训练，成本高昂且效率低下。

**核心思路**：论文的核心思路是，将通过强化学习获得的推理能力，以向量的形式从一个模型迁移到另一个模型。具体而言，通过计算经过强化学习微调的模型参数与经过监督微调的模型参数之间的差值，得到一个“推理向量”，该向量代表了强化学习所带来的推理能力的增量。

**技术框架**：该方法主要包含以下几个步骤：1) 使用相同的初始化模型，分别进行监督微调（SFT）和组相对策略优化（GRPO）；2) 计算GRPO模型和SFT模型参数的差值，得到推理向量；3) 将推理向量加到其他兼容的指令调整模型上，从而增强其推理能力。整个过程无需重新训练，只需进行简单的向量加法。

**关键创新**：该方法最重要的创新点在于，它提出了一种将推理能力从一个模型“提取”并“注入”到另一个模型的新方法。这种方法避免了昂贵的重新训练过程，实现了推理能力的有效迁移和复用。通过任务算术的方式，将推理能力表示为可操作的向量，为模型能力的模块化和组合提供了新的思路。

**关键设计**：关键设计在于推理向量的计算方式：$v_{\text{reason}} = θ_{\text{GRPO}} - θ_{\text{SFT}}$。这种计算方式旨在提取强化学习带来的推理能力增量，同时消除监督微调带来的共享知识的影响。此外，论文还验证了推理向量的可加性和可减性，即添加推理向量可以提升性能，而减去推理向量则会降低性能，从而验证了推理向量的有效性。

## 📊 实验亮点

实验结果表明，将推理向量添加到其他模型后，在GSM8K、HumanEval、SciQ和BigBenchHard等多个推理基准上均取得了显著的性能提升。例如，在BigBenchHard基准上，1.5B模型的性能提升了12.3%。更重要的是，减去推理向量会导致性能显著下降，验证了该向量对推理能力的贡献。这些结果表明，该方法能够有效地迁移推理能力，并具有良好的鲁棒性。

## 🎯 应用场景

该研究成果可广泛应用于各种需要复杂推理能力的场景，例如数学问题求解、代码生成、科学推理等。通过迁移已训练模型的推理能力，可以降低新模型训练的成本，加速AI技术的应用。此外，该方法还可以用于构建更模块化、可组合的AI系统，通过组合不同的任务向量，实现更复杂的功能。

## 📄 摘要（原文）

> Large language models often require costly optimization, such as reinforcement learning, to master complex reasoning tasks. This work demonstrates that reasoning ability, once learned, can be extracted and transferred between models as a compact task vector. We source two publicly available, identically initialized Qwen2.5 models, one fine-tuned with supervised fine-tuning (SFT) and the other with group relative policy optimization (GRPO) on the same dataset. From these, we extract a reasoning vector: $v_{\text{reason}} = θ_{\text{GRPO}} - θ_{\text{SFT}}$. We hypothesize that this vector captures the reasoning capability instilled by reinforcement learning while factoring out shared knowledge from the SFT process. When added to compatible instruction-tuned models through simple arithmetic, this vector consistently improves performance across diverse reasoning benchmarks: GSM8K (+4.9%), HumanEval (+4.3%), SciQ (+1.7%), and BigBenchHard (+12.3% for the 1.5B model). The performance improvements persist under adversarial conditions. Conversely, subtracting the vector causes significant performance degradation (-11.8% on GSM8K), demonstrating the vector's strong contribution to the model's reasoning abilities. This work shows how reasoning capabilities, typically developed through expensive training, can be extracted from existing open-source models and reused through simple tensor arithmetic, offering a practical way to enhance models by recycling prior computational investments.

