---
layout: default
title: "Training Multimodal Large Reasoning Models Needs Better Thoughts: A Three-Stage Framework for Long Chain-of-Thought Synthesis and Selection"
---

# Training Multimodal Large Reasoning Models Needs Better Thoughts: A Three-Stage Framework for Long Chain-of-Thought Synthesis and Selection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.18956" class="toolbar-btn" target="_blank">📄 arXiv: 2512.18956v1</a>
  <a href="https://arxiv.org/pdf/2512.18956.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.18956v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.18956v1', 'Training Multimodal Large Reasoning Models Needs Better Thoughts: A Three-Stage Framework for Long Chain-of-Thought Synthesis and Selection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yizhi Wang, Linan Yue, Min-Ling Zhang

**分类**: cs.AI, cs.LG

**发布日期**: 2025-12-22

---

## 💡 一句话要点

**提出SynSelect框架，为多模态大模型生成高质量长链推理训练数据。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态推理` `长链思考` `数据合成` `数据选择` `大型推理模型` `视觉问答` `模型微调`

## 📋 核心要点

1. 多模态推理面临高质量长链思考数据稀缺的挑战，现有方法推理深度有限且易出错。
2. SynSelect框架通过多阶段合成与选择，生成高质量、多样化的多模态长链思考数据。
3. 实验表明，基于SynSelect训练的模型在多模态推理任务上显著优于现有基线方法。

## 📝 摘要（中文）

大型推理模型(LRMs)在复杂的推理任务中通过长链思考(CoT)推理表现出了卓越的性能。然而，由于整合不同输入模态的复杂性增加以及高质量长CoT训练数据的稀缺，将这些成功扩展到多模态推理仍然具有挑战性。现有的多模态数据集和CoT合成方法仍然存在推理深度有限、模态转换错误和生成流程僵化等问题，从而阻碍了模型的性能和稳定性。为此，本文提出了一种新颖的三阶段合成-选择框架SynSelect，用于生成针对多模态推理任务量身定制的高质量长CoT数据。具体来说，SynSelect首先利用多个异构多模态LRM来生成多样化的候选CoT，然后应用实例和批次级别的选择来过滤能够有效增强模型推理能力的高质量CoT。在多个多模态基准上的大量实验表明，在SynSelect生成的数据上进行监督微调的模型显著优于基线，并在强化学习后训练后取得了进一步的改进。我们的结果验证了SynSelect是提高多模态LRM推理能力的有效方法。

## 🔬 方法详解

**问题定义**：多模态大型推理模型在复杂推理任务中表现出色，但缺乏高质量的长链思考(CoT)训练数据。现有数据集和CoT生成方法存在推理深度不足、模态转换错误以及生成流程僵化等问题，限制了模型性能和稳定性。

**核心思路**：SynSelect的核心在于通过一个三阶段的合成-选择框架，生成高质量、多样化的长CoT数据。它利用多个异构的多模态LRM生成候选CoT，并通过实例和批次级别的选择机制，筛选出能够有效提升模型推理能力的CoT。这种方法旨在克服现有方法在数据质量和多样性方面的局限性。

**技术框架**：SynSelect框架包含三个主要阶段：
1. **CoT Synthesis (CoT合成)**：利用多个异构的多模态LRM生成多样化的候选CoT。
2. **Instance-level Selection (实例级别选择)**：对每个CoT进行质量评估，选择高质量的CoT。
3. **Batch-level Selection (批次级别选择)**：在批次层面进一步筛选，确保选出的CoT能够有效提升模型的推理能力。

**关键创新**：SynSelect的关键创新在于其三阶段的合成-选择框架，特别是批次级别的选择机制。与传统的只关注单个CoT质量的方法不同，SynSelect在批次层面考虑了CoT之间的关系，从而能够选择出更具信息量和互补性的CoT集合，更有效地提升模型性能。

**关键设计**：在CoT合成阶段，使用不同的多模态LRM以增加CoT的多样性。实例级别选择可能使用奖励模型或基于规则的过滤。批次级别选择可能涉及聚类或基于覆盖率的策略，以确保选择的CoT集合具有代表性，并能覆盖不同的推理路径。具体的损失函数和网络结构取决于所使用的多模态LRM。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.18956v1/x2.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.18956v1/x3.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.18956v1/x4.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，在SynSelect生成的数据上进行微调的模型，在多个多模态基准测试中显著优于基线模型。通过强化学习后训练，模型性能得到进一步提升，验证了SynSelect在提高多模态LRM推理能力方面的有效性。具体性能提升幅度未知，但摘要强调了“显著优于基线”。

## 🎯 应用场景

该研究成果可广泛应用于需要复杂推理的多模态任务中，例如视觉问答、图像描述生成、机器人导航等。通过提供高质量的训练数据，可以显著提升多模态大模型的推理能力，使其在实际应用中更加可靠和有效。未来，该方法可以进一步扩展到其他模态和任务，推动多模态人工智能的发展。

## 📄 摘要（原文）

> Large Reasoning Models (LRMs) have demonstrated remarkable performance on complex reasoning tasks through long Chain-of-Thought (CoT) reasoning. Extending these successes to multimodal reasoning remains challenging due to the increased complexity of integrating diverse input modalities and the scarcity of high-quality long CoT training data. Existing multimodal datasets and CoT synthesis methods still suffer from limited reasoning depth, modality conversion errors, and rigid generation pipelines, hindering model performance and stability. To this end, in this paper, we propose SynSelect, a novel three-stage Synthesis-Selection framework for generating high-quality long CoT data tailored to multimodal reasoning tasks. Specifically, SynSelect first leverages multiple heterogeneous multimodal LRMs to produce diverse candidate CoTs, and then applies both instance and batch level selection to filter high-quality CoTs that can effectively enhance the model's reasoning capabilities. Extensive experiments on multiple multimodal benchmarks demonstrate that models supervised fine-tuned on SynSelect-generated data significantly outperform baselines and achieve further improvements after reinforcement learning post-training. Our results validate SynSelect as an effective approach for advancing multimodal LRMs reasoning capabilities.

