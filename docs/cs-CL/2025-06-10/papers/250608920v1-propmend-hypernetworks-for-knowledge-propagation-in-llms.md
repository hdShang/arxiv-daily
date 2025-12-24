---
layout: default
title: "PropMEND: Hypernetworks for Knowledge Propagation in LLMs"
---

# PropMEND: Hypernetworks for Knowledge Propagation in LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.08920" class="toolbar-btn" target="_blank">📄 arXiv: 2506.08920v1</a>
  <a href="https://arxiv.org/pdf/2506.08920.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.08920v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.08920v1', 'PropMEND: Hypernetworks for Knowledge Propagation in LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zeyu Leo Liu, Greg Durrett, Eunsol Choi

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-06-10

**备注**: Under review

---

## 💡 一句话要点

**提出PropMEND以解决大语言模型知识传播问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `知识传播` `大语言模型` `超网络` `元学习` `多跳推理`

## 📋 核心要点

1. 现有的知识编辑技术无法有效传播注入的知识，导致模型在推理时的表现不佳。
2. 本文提出的PropMEND通过元学习调整梯度，使得注入的信息能够在多跳问题中有效传播。
3. 实验结果显示，PropMEND在RippleEdit数据集上准确率几乎提高了2倍，且在新数据集上表现优异。

## 📝 摘要（中文）

大语言模型（LLMs）的知识编辑技术可以注入可重复的知识，但在知识传播方面存在不足，模型无法回答需要推理的相关问题。本文提出了一种基于超网络的知识传播方法PropMEND，通过元学习调整语言建模损失的梯度，以促进注入信息的传播。该方法扩展了MEND的元目标，使得知识的梯度更新能够支持多跳问题的回答。实验结果表明，在RippleEdit数据集上，PropMEND在复杂的多跳问题上准确率几乎提高了2倍。此外，本文还引入了新的Controlled RippleEdit数据集，以评估超网络的泛化能力，测试在超网络训练中未见的关系和实体上的知识传播。尽管PropMEND在未见的实体-关系对上仍优于现有方法，但性能差距显著减小，提示未来在广泛关系的知识传播方面的研究潜力。

## 🔬 方法详解

**问题定义**：本文旨在解决大语言模型在知识编辑后无法有效传播知识的问题。现有方法在处理需要推理的多跳问题时表现不足，无法利用注入的知识进行合理推理。

**核心思路**：PropMEND的核心思路是通过超网络结构进行元学习，调整语言建模损失的梯度，以促进知识的传播。这种设计使得模型能够在回答多跳问题时，利用注入的知识进行推理。

**技术框架**：PropMEND的整体架构包括超网络模块和梯度调整机制。超网络负责生成适应性梯度更新，而梯度调整机制则确保知识在多跳推理中有效传播。

**关键创新**：PropMEND的主要创新在于其超网络的设计，使得知识的梯度更新能够被转化为支持多跳推理的形式。这与现有方法的直接知识注入方式形成了显著区别。

**关键设计**：在技术细节上，PropMEND使用了特定的损失函数来优化梯度更新，并设计了超网络的结构以适应不同类型的知识注入，确保在未见的实体-关系对上也能有效工作。

## 📊 实验亮点

在RippleEdit数据集上，PropMEND的准确率几乎提高了2倍，显著优于现有方法。此外，在Controlled RippleEdit数据集上，PropMEND在未见实体-关系对上的表现仍然优异，尽管性能差距有所减小，显示出未来研究的潜力。

## 🎯 应用场景

该研究的潜在应用领域包括智能问答系统、知识图谱构建和人机交互等。通过有效的知识传播，PropMEND能够提升模型在复杂推理任务中的表现，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> Knowledge editing techniques for large language models (LLMs) can inject knowledge that is later reproducible verbatim, but they fall short on propagating that knowledge: models cannot answer questions that require reasoning with the injected knowledge. We present a hypernetwork-based approach for knowledge propagation, named PropMEND, where we meta-learn how to modify gradients of a language modeling loss to encourage injected information to propagate. Our approach extends the meta-objective of MEND [29] so that gradient updates on knowledge are transformed to enable answering multi-hop questions involving that knowledge. We show improved performance on the RippleEdit dataset, showing almost 2x accuracy on challenging multi-hop questions whose answers are not explicitly stated in the injected fact. We further introduce a new dataset, Controlled RippleEdit, to evaluate the generalization of our hypernetwork, testing knowledge propagation along relations and entities unseen during hypernetwork training. PropMEND still outperforms existing approaches in unseen entity-relation pairs, yet the performance gap decreases substantially, suggesting future work in propagating knowledge to a wide range of relations.

