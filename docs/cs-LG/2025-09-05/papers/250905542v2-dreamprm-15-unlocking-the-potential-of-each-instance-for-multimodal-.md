---
layout: default
title: "DreamPRM-1.5: Unlocking the Potential of Each Instance for Multimodal Process Reward Model Training"
---

# DreamPRM-1.5: Unlocking the Potential of Each Instance for Multimodal Process Reward Model Training

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.05542" class="toolbar-btn" target="_blank">📄 arXiv: 2509.05542v2</a>
  <a href="https://arxiv.org/pdf/2509.05542.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.05542v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.05542v2', 'DreamPRM-1.5: Unlocking the Potential of Each Instance for Multimodal Process Reward Model Training')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qi Cao, Pengtao Xie

**分类**: cs.LG

**发布日期**: 2025-09-05 (更新: 2025-10-21)

---

## 💡 一句话要点

**DreamPRM-1.5：通过实例重加权提升多模态过程奖励模型的训练效果**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态学习` `过程奖励模型` `实例重加权` `双层优化` `分布偏移` `自适应权重` `神经网络` `模型训练`

## 📋 核心要点

1. 多模态过程奖励模型训练面临分布偏移和数据质量不平衡问题，现有领域级重加权方法存在性能瓶颈。
2. DreamPRM-1.5通过双层优化实现实例级重加权，为每个样本分配自适应权重，提升模型训练效果。
3. 实验表明，DreamPRM-1.5在多个数据集上取得了领先的性能，并缩小了与理想上限的差距。

## 📝 摘要（中文）

多模态过程奖励模型(PRM)的训练面临训练集与测试集之间的分布偏移以及训练数据样本质量不平衡的挑战。领域级重加权(如DreamPRM)虽然能使训练与测试目标对齐，但与理想上限(pass@N)仍存在差距，表明存在元级别欠参数化问题。本文提出了DreamPRM-1.5，一种实例级重加权框架，通过双层优化为每个训练样本分配自适应权重。为了实现跨尺度的实例重加权，开发了两种互补机制：Instance Table，擅长处理中小规模数据，学习显式的样本权重；Instance Net，一个轻量级神经网络，泛化能力更强，可扩展到大型语料库。通过时间尺度匹配、冷启动初始化和有界权重等稳定训练技巧，防止训练发散。结合测试时缩放，DreamPRM-1.5在MMMU验证集上达到84.6%的准确率，在R-Bench-V上达到31.3%的准确率，并与GPT-5-mini等领先骨干网络结合，在公开多模态推理排行榜上取得领先地位。实验结果表明，DreamPRM-1.5缩小了与理想上限的差距，实现了领先的性能，并能稳定训练。

## 🔬 方法详解

**问题定义**：现有的多模态过程奖励模型（PRM）训练方法，如DreamPRM，主要关注领域级别的重加权，忽略了单个训练样本之间的质量差异。这导致模型在训练过程中无法充分利用高质量样本，同时受到低质量样本的干扰，最终限制了模型的性能上限。此外，训练集和测试集之间的分布偏移进一步加剧了这一问题。

**核心思路**：DreamPRM-1.5的核心思路是进行实例级别的重加权，即为每个训练样本分配一个自适应的权重，以更精细地控制每个样本对模型训练的影响。通过双层优化，模型能够学习到每个样本的重要性，从而更好地利用高质量样本，抑制低质量样本的干扰，并缓解分布偏移带来的影响。

**技术框架**：DreamPRM-1.5采用双层优化框架。外层优化目标是提升模型在验证集上的性能，内层优化目标是学习每个训练样本的权重。为了实现实例级别的重加权，论文提出了两种互补的机制：Instance Table和Instance Net。Instance Table适用于中小规模数据集，通过显式地学习每个样本的权重来实现重加权。Instance Net则是一个轻量级的神经网络，能够更好地泛化到大规模数据集。

**关键创新**：DreamPRM-1.5的关键创新在于提出了实例级别的重加权方法，并设计了两种不同的实现机制（Instance Table和Instance Net）以适应不同规模的数据集。与现有的领域级别重加权方法相比，实例级别的重加权能够更精细地控制每个样本对模型训练的影响，从而更好地利用高质量样本，抑制低质量样本的干扰。

**关键设计**：为了保证训练的稳定性，论文提出了一系列关键的设计，包括：1) 时间尺度匹配：调整内外层优化器之间的学习率，以保证内外层优化能够同步进行。2) 冷启动初始化：对Instance Table和Instance Net进行合理的初始化，以避免训练初期出现梯度爆炸或梯度消失的问题。3) 有界权重：将样本权重限制在一个合理的范围内，以防止某些样本的权重过大或过小，从而影响模型的训练。

## 📊 实验亮点

DreamPRM-1.5在MMMU验证集上取得了84.6%的准确率，在R-Bench-V上取得了31.3%的准确率。与GPT-5-mini等领先的骨干网络结合后，在公开多模态推理排行榜上取得了领先地位。实验结果表明，DreamPRM-1.5能够有效地缩小与理想上限的差距，并实现了领先的性能。

## 🎯 应用场景

DreamPRM-1.5可应用于各种需要多模态推理的任务，例如视觉问答、图像描述生成、机器人导航等。通过提升多模态过程奖励模型的性能，可以提高这些任务的准确性和可靠性，从而在智能助手、自动驾驶、智能制造等领域发挥重要作用。该研究为多模态学习提供了一种新的训练范式，具有广泛的应用前景。

## 📄 摘要（原文）

> Training multimodal process reward models (PRMs) is hard due to (i) distribution shift between training set and test set and (ii) quality imbalance across training data samples. While domain-level reweighting (e.g., DreamPRM) aligns training with test-time objectives, it leaves a clear gap to an oracle upper bound (pass@N), even under a "sanity check" that uses test set data to probe headroom -- pointing to meta-level under-parameterization. We introduce DreamPRM-1.5, an instance-level reweighting framework that assigns an adaptive weight to every training example via bi-level optimization. To realize instance reweighting across scales, we develop two complementary regimes: Instance Table, which learns explicit per-sample weights and excels on small/medium data, and Instance Net, a lightweight neural network that generalizes better and scales to large corpora. A practical, stable training recipe -- time-scale matching between upper/lower updates, cold-start initialization, and bounded-range weights -- prevents divergence. Integrated with test-time scaling, DreamPRM-1.5 attains 84.6 accuracy on the MMMU validation set, 31.3 accuracy on R-Bench-V and, when paired with a leading backbone (e.g., GPT-5-mini), achieves first-place results on public multimodal reasoning leaderboards. Moreover, extensive experiments, including benchmark evaluations, baseline comparisons, and a sanity check, demonstrate that DreamPRM-1.5 closes the gap toward the oracle, achieves leading performance, and trains stably.

