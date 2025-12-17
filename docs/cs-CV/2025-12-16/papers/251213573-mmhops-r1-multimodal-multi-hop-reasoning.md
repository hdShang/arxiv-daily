---
layout: default
title: MMhops-R1: Multimodal Multi-hop Reasoning
---

# MMhops-R1: Multimodal Multi-hop Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.13573" class="toolbar-btn" target="_blank">📄 arXiv: 2512.13573</a>
  <a href="https://arxiv.org/pdf/2512.13573.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.13573" onclick="toggleFavorite(this, '2512.13573', 'MMhops-R1: Multimodal Multi-hop Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tao Zhang, Ziqi Zhang, Zongyang Ma, Yuxin Chen, Bing Li, Chunfeng Yuan, Guangting Wang, Fengyun Rao, Ying Shan, Weiming Hu

**分类**: cs.CV

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出MMhops基准和MMhops-R1框架，用于评估和提升多模态多跳推理能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态学习` `多跳推理` `检索增强生成` `强化学习` `知识整合`

## 📋 核心要点

1. 现有MLLM主要局限于单步推理，缺乏评估和驱动多跳能力的复杂基准。
2. 提出MMhops-R1，一个基于检索增强生成(mRAG)的框架，利用强化学习优化推理路径规划。
3. 实验表明，MMhops-R1在MMhops上显著优于基线，并展现出良好的泛化能力。

## 📝 摘要（中文）

为了解决现有多模态大语言模型(MLLM)在多步推理能力上的不足，本研究提出了一个名为MMhops的大规模基准数据集，旨在系统地评估和促进多模态多跳推理。MMhops包含两种具有挑战性的任务形式：Bridging和Comparison，要求模型通过整合外部知识动态构建复杂的推理链。为了应对MMhops的挑战，我们提出了MMhops-R1，一种新颖的多模态检索增强生成(mRAG)框架，用于动态推理。该框架利用强化学习来优化模型，使其能够自主地规划推理路径、制定有针对性的查询并综合多层次的信息。综合实验表明，MMhops-R1在MMhops上显著优于强大的基线模型，突出了动态规划和多模态知识整合对于复杂推理的重要性。此外，MMhops-R1在需要固定跳数推理的任务中也表现出强大的泛化能力，强调了我们动态规划方法的鲁棒性。总之，我们的工作贡献了一个具有挑战性的新基准和一个强大的基线模型，我们将发布相关的代码、数据和权重，以促进该关键领域的未来研究。

## 🔬 方法详解

**问题定义**：现有的大型多模态语言模型（MLLM）在复杂现实场景下的多模态多跳推理能力不足。现有的基准数据集缺乏足够的复杂性来评估和驱动模型进行多跳推理，限制了模型在需要整合多种模态信息和外部知识的复杂任务中的应用。

**核心思路**：论文的核心思路是提出一个更具挑战性的基准数据集MMhops，并设计一个能够动态规划推理路径的多模态检索增强生成框架MMhops-R1。通过强化学习优化推理路径，使模型能够自主地进行多跳推理，并整合多层次的信息。

**技术框架**：MMhops-R1是一个多模态检索增强生成(mRAG)框架，主要包含以下几个模块：1)推理路径规划器：使用强化学习来学习如何规划推理路径，确定每一步需要检索的信息。2)查询生成器：根据推理路径生成针对性的查询，用于从外部知识库中检索相关信息。3)多模态知识整合器：将检索到的信息与原始的多模态输入进行整合，形成新的上下文信息。4)答案生成器：根据整合后的上下文信息生成最终的答案。

**关键创新**：该论文的关键创新在于提出了一个基于强化学习的动态推理路径规划方法。与传统的固定推理路径方法不同，该方法能够根据不同的输入动态地调整推理路径，从而更好地适应复杂的多模态推理任务。此外，该框架还能够有效地整合多层次的信息，从而提高推理的准确性。

**关键设计**：在强化学习部分，使用了策略梯度算法来训练推理路径规划器。奖励函数的设计考虑了推理的准确性和效率。在多模态知识整合部分，使用了注意力机制来选择重要的信息。损失函数包括交叉熵损失和强化学习奖励损失。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.13573/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.13573/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.13573/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

MMhops-R1在MMhops基准测试中显著优于其他基线模型，证明了动态规划和多模态知识整合对于复杂推理的重要性。具体而言，MMhops-R1在Bridging和Comparison任务上均取得了显著的性能提升，并且在固定跳数推理任务中也表现出强大的泛化能力。这些实验结果表明，MMhops-R1是一种有效的多模态多跳推理方法。

## 🎯 应用场景

该研究成果可应用于需要复杂推理和知识整合的场景，例如智能问答系统、视觉对话、医疗诊断辅助等。通过提升模型的多模态多跳推理能力，可以更好地理解和处理真实世界的复杂问题，为用户提供更准确、更智能的服务。未来可以进一步探索如何将该方法应用于更多的领域，例如机器人导航、自动驾驶等。

## 📄 摘要（原文）

> The ability to perform multi-modal multi-hop reasoning by iteratively integrating information across various modalities and external knowledge is critical for addressing complex real-world challenges. However, existing Multi-modal Large Language Models (MLLMs) are predominantly limited to single-step reasoning, as existing benchmarks lack the complexity needed to evaluate and drive multi-hop abilities. To bridge this gap, we introduce MMhops, a novel, large-scale benchmark designed to systematically evaluate and foster multi-modal multi-hop reasoning. MMhops dataset comprises two challenging task formats, Bridging and Comparison, which necessitate that models dynamically construct complex reasoning chains by integrating external knowledge. To tackle the challenges posed by MMhops, we propose MMhops-R1, a novel multi-modal Retrieval-Augmented Generation (mRAG) framework for dynamic reasoning. Our framework utilizes reinforcement learning to optimize the model for autonomously planning reasoning paths, formulating targeted queries, and synthesizing multi-level information. Comprehensive experiments demonstrate that MMhops-R1 significantly outperforms strong baselines on MMhops, highlighting that dynamic planning and multi-modal knowledge integration are crucial for complex reasoning. Moreover, MMhops-R1 demonstrates strong generalization to tasks requiring fixed-hop reasoning, underscoring the robustness of our dynamic planning approach. In conclusion, our work contributes a challenging new benchmark and a powerful baseline model, and we will release the associated code, data, and weights to catalyze future research in this critical area.

