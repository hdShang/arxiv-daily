---
layout: default
title: "Klear-Reasoner: Advancing Reasoning Capability via Gradient-Preserving Clipping Policy Optimization"
---

# Klear-Reasoner: Advancing Reasoning Capability via Gradient-Preserving Clipping Policy Optimization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.07629" class="toolbar-btn" target="_blank">📄 arXiv: 2508.07629v2</a>
  <a href="https://arxiv.org/pdf/2508.07629.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.07629v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.07629v2', 'Klear-Reasoner: Advancing Reasoning Capability via Gradient-Preserving Clipping Policy Optimization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhenpeng Su, Leiyu Pan, Xue Bai, Dening Liu, Guanting Dong, Jiaming Huang, Wenping Hu, Fuzheng Zhang, Kun Gai, Guorui Zhou

**分类**: cs.LG, cs.AI, cs.CL

**发布日期**: 2025-08-11 (更新: 2025-08-12)

---

## 💡 一句话要点

**提出Klear-Reasoner以解决推理模型性能再现性问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `推理模型` `梯度保持` `剪切策略` `强化学习` `长链思维`

## 📋 核心要点

1. 现有推理模型在高性能再现性方面存在挑战，主要由于训练细节披露不足。
2. 提出梯度保持剪切策略优化（GPPO），通过温和反向传播剪切标记的梯度来解决现有剪切机制的问题。
3. Klear-Reasoner在数学和编程推理方面表现出色，在多个基准测试中取得了显著的分数提升。

## 📝 摘要（中文）

我们提出了Klear-Reasoner，这是一种具有长推理能力的模型，在问题解决过程中表现出细致的思考，能够在多个基准测试中取得优异的表现。尽管当前社区已有许多优秀的推理模型，但由于训练细节披露不完整，导致高性能推理模型的再现性存在问题。本文深入分析了推理模型的整个后训练工作流程，包括数据准备、长链思维监督微调（long CoT SFT）和强化学习（RL），并对每个实验组件进行了详细的消融研究。我们的实验表明，少量高质量数据源的效果优于大量多样化的数据源，且困难样本在没有准确性过滤的情况下也能取得更好的结果。此外，我们还探讨了当前RL剪切机制的两个关键问题，并提出了梯度保持剪切策略优化（GPPO），显著提升了模型的探索能力和从负样本中学习的效率。

## 🔬 方法详解

**问题定义**：本论文旨在解决推理模型在高性能再现性方面的不足，现有方法在训练细节披露不全的情况下，导致模型性能难以复现。

**核心思路**：论文提出了梯度保持剪切策略优化（GPPO），该方法通过温和地反向传播剪切标记的梯度，来增强模型的探索能力和学习效率，从而克服现有剪切机制的局限性。

**技术框架**：Klear-Reasoner的整体架构包括数据准备、长链思维监督微调（long CoT SFT）和强化学习（RL）三个主要阶段。每个阶段都经过详细的消融研究，以验证其对模型性能的贡献。

**关键创新**：最重要的技术创新点是GPPO方法，它与传统的剪切机制不同，能够保留重要的探索信号，并有效处理次优轨迹，从而提升模型的学习能力。

**关键设计**：在SFT数据方面，研究表明少量高质量数据源的效果优于大量多样化的数据源。此外，论文还探讨了困难样本的使用，发现其在没有准确性过滤的情况下也能取得更好的结果。实验中使用的损失函数和网络结构经过精心设计，以确保模型的高效学习。

## 📊 实验亮点

Klear-Reasoner在多个基准测试中表现优异，AIME 2024得分90.5%，AIME 2025得分83.2%，LiveCodeBench V5得分66.0%，LiveCodeBench V6得分58.1%。这些结果表明，该模型在推理能力上有显著提升，尤其是在复杂任务中的表现。

## 🎯 应用场景

Klear-Reasoner的研究成果在数学推理、编程任务等领域具有广泛的应用潜力。其高效的推理能力可以帮助开发更智能的教育工具、编程助手和自动化决策系统，推动人工智能在实际应用中的发展与落地。

## 📄 摘要（原文）

> We present Klear-Reasoner, a model with long reasoning capabilities that demonstrates careful deliberation during problem solving, achieving outstanding performance across multiple benchmarks. Although there are already many excellent works related to inference models in the current community, there are still many problems with reproducing high-performance inference models due to incomplete disclosure of training details. This report provides an in-depth analysis of the reasoning model, covering the entire post-training workflow from data preparation and long Chain-of-Thought supervised fine-tuning (long CoT SFT) to reinforcement learning (RL), along with detailed ablation studies for each experimental component. For SFT data, our experiments show that a small number of high-quality data sources are more effective than a large number of diverse data sources, and that difficult samples can achieve better results without accuracy filtering. In addition, we investigate two key issues with current clipping mechanisms in RL: Clipping suppresses critical exploration signals and ignores suboptimal trajectories. To address these challenges, we propose Gradient-Preserving clipping Policy Optimization (GPPO) that gently backpropagates gradients from clipped tokens. GPPO not only enhances the model's exploration capacity but also improves its efficiency in learning from negative samples. Klear-Reasoner exhibits exceptional reasoning abilities in mathematics and programming, scoring 90.5% on AIME 2024, 83.2% on AIME 2025, 66.0% on LiveCodeBench V5 and 58.1% on LiveCodeBench V6.

