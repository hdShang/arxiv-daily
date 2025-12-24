---
layout: default
title: "Chameleon: A Flexible Data-mixing Framework for Language Model Pretraining and Finetuning"
---

# Chameleon: A Flexible Data-mixing Framework for Language Model Pretraining and Finetuning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.24844" class="toolbar-btn" target="_blank">📄 arXiv: 2505.24844v1</a>
  <a href="https://arxiv.org/pdf/2505.24844.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.24844v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.24844v1', 'Chameleon: A Flexible Data-mixing Framework for Language Model Pretraining and Finetuning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wanyun Xie, Francesco Tonin, Volkan Cevher

**分类**: cs.LG, cs.CL

**发布日期**: 2025-05-30

**备注**: ICML 2025

**🔗 代码/项目**: [GITHUB](https://github.com/LIONS-EPFL/Chameleon)

---

## 💡 一句话要点

**提出Chameleon框架以高效混合数据提升语言模型性能**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `数据混合` `语言模型` `领域重加权` `杠杆分数` `模型微调` `少样本学习` `自然语言处理`

## 📋 核心要点

1. 现有的领域重加权方法计算成本高，并在新数据引入时需要重新训练，限制了其灵活性和效率。
2. Chameleon框架通过杠杆分数量化领域重要性，构建领域亲和矩阵，实现数据的高效混合和适应。
3. 实验结果显示，Chameleon在预训练和微调阶段均显著提升了模型性能，计算成本远低于传统方法。

## 📝 摘要（中文）

训练数据的混合对大型语言模型的泛化性能有重要影响。现有的领域重加权方法通常依赖于昂贵的权重计算，并在引入新数据时需要重新训练。为此，本文提出了一种灵活高效的数据混合框架Chameleon，该框架利用杠杆分数在学习的嵌入空间中量化领域的重要性。我们首先构建了一个领域亲和矩阵，杠杆分数的引入决定了一个混合方案，该方案提升了在嵌入空间中共享共同表示的领域的权重。该公式允许通过计算新的领域嵌入直接转移到新数据上。实验表明，我们的方法在三个关键场景中均有改进：计算的权重在预训练领域的性能提升上，计算成本仅为现有方法的一小部分；Chameleon能够在数据变化时适应，无需代理重新训练，提升了在新数据上的少样本推理准确性；我们的方案在微调中实现了高效的领域重加权，始终改善了所有微调领域的测试困惑度。

## 🔬 方法详解

**问题定义**：本文旨在解决现有领域重加权方法在新数据引入时的高计算成本和重新训练的需求，导致灵活性不足的问题。

**核心思路**：Chameleon框架通过杠杆分数来量化领域的重要性，利用领域嵌入构建亲和矩阵，从而实现高效的数据混合和适应新数据。

**技术框架**：Chameleon的整体架构包括领域嵌入的构建、领域亲和矩阵的生成以及基于杠杆分数的权重计算。该框架能够直接应用于新数据，无需重新训练。

**关键创新**：Chameleon的主要创新在于使用杠杆分数来量化领域重要性，允许模型在面对新数据时快速适应，显著提高了效率和性能。与现有方法相比，Chameleon减少了计算复杂度并提升了灵活性。

**关键设计**：在参数设置上，Chameleon通过优化领域亲和矩阵和杠杆分数的计算，确保了模型在不同领域间的有效迁移。损失函数设计上，强调了领域间的相似性，以增强模型的泛化能力。

## 📊 实验亮点

实验结果表明，Chameleon在预训练阶段的性能提升显著，计算成本仅为现有方法的一个小部分。此外，在少样本推理任务中，Chameleon能够在新数据上提升准确性，微调阶段的测试困惑度也在所有领域中均有改善，显示出其强大的适应能力和效率。

## 🎯 应用场景

Chameleon框架在自然语言处理、机器翻译和对话系统等领域具有广泛的应用潜力。其高效的数据混合能力能够帮助模型更好地适应不断变化的数据环境，提高模型的泛化能力和实际应用效果。未来，该框架可能推动更多领域的智能应用发展，提升人机交互的质量。

## 📄 摘要（原文）

> Training data mixtures greatly impact the generalization performance of large language models. Existing domain reweighting methods often rely on costly weight computations and require retraining when new data is introduced. To this end, we introduce a flexible and efficient data mixing framework, Chameleon, that employs leverage scores to quantify domain importance within a learned embedding space. We first construct a domain affinity matrix over domain embeddings. The induced leverage scores determine a mixture that upweights domains sharing common representations in embedding space. This formulation allows direct transfer to new data by computing the new domain embeddings. In experiments, we demonstrate improvements over three key scenarios: (i) our computed weights improve performance on pretraining domains with a fraction of the compute of existing methods; (ii) Chameleon can adapt to data changes without proxy retraining, boosting few-shot reasoning accuracies when transferred to new data; (iii) our method enables efficient domain reweighting in finetuning, consistently improving test perplexity on all finetuning domains over uniform mixture. Our code is available at https://github.com/LIONS-EPFL/Chameleon.

