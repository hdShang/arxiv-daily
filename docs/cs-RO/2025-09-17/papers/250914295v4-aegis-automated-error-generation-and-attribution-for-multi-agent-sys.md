---
layout: default
title: "Aegis: Automated Error Generation and Attribution for Multi-Agent Systems"
---

# Aegis: Automated Error Generation and Attribution for Multi-Agent Systems

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.14295" class="toolbar-btn" target="_blank">📄 arXiv: 2509.14295v4</a>
  <a href="https://arxiv.org/pdf/2509.14295.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.14295v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.14295v4', 'Aegis: Automated Error Generation and Attribution for Multi-Agent Systems')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Fanqi Kong, Ruijie Zhang, Huaxiao Yin, Guibin Zhang, Xiaofei Zhang, Ziang Chen, Zhaowei Zhang, Xiaoyuan Zhang, Song-Chun Zhu, Xue Feng

**分类**: cs.RO, cs.MA

**发布日期**: 2025-09-17 (更新: 2025-10-10)

**🔗 代码/项目**: [PROJECT_PAGE](https://kfq20.github.io/Aegis-Website/)

---

## 💡 一句话要点

**Aegis：用于多智能体系统的自动化错误生成与归因框架**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多智能体系统` `错误归因` `自动化数据生成` `大型语言模型` `监督学习`

## 📋 核心要点

1. 多智能体系统调试困难，缺乏大规模错误归因数据集是主要瓶颈，现有方法依赖手动标注，成本高且难以扩展。
2. Aegis框架利用LLM操纵器，自适应地向成功轨迹注入上下文相关的错误，自动生成大规模、多样化的错误数据集。
3. 实验表明，基于Aegis生成的数据训练的模型在错误归因方面取得了显著提升，性能可与更大的专有模型媲美。

## 📝 摘要（中文）

基于大型语言模型的多智能体系统(MAS)在解决复杂问题方面取得了显著进展，但其日益增长的能力也带来了结构上的脆弱性，使得调试变得困难。提高其可靠性的一个关键障碍是缺乏大规模、多样化的错误归因数据集，因为现有资源依赖于成本高昂且不可扩展的手动标注。为了解决这个瓶颈，我们提出了Aegis，一个用于多智能体系统的自动化错误生成和归因的新框架。Aegis构建了一个包含9,533条轨迹的大型数据集，其中标注了错误的智能体和错误模式，涵盖了不同的MAS架构和任务领域。这是通过使用基于LLM的操纵器实现的，该操纵器可以将上下文相关的错误自适应地注入到成功的执行轨迹中。利用细粒度的标签和正负样本对的结构化排列，Aegis支持三种不同的学习范式：监督微调、强化学习和对比学习。我们为每种范式开发了学习方法。综合实验表明，训练后的模型在错误归因方面始终取得了显著的改进。值得注意的是，我们的一些微调LLM表现出与大一个数量级的专有模型相当甚至更好的性能，验证了我们的自动化数据生成框架是开发更健壮和可解释的多智能体系统的关键资源。

## 🔬 方法详解

**问题定义**：论文旨在解决多智能体系统(MAS)的错误归因问题。现有方法依赖于手动标注错误数据，成本高昂且难以扩展，导致缺乏大规模、多样化的数据集，阻碍了MAS的可靠性和可解释性。

**核心思路**：论文的核心思路是利用大型语言模型(LLM)自动生成带有错误标注的数据集。通过LLM操纵器，将上下文相关的错误注入到成功的执行轨迹中，从而高效地创建正负样本对，用于训练错误归因模型。

**技术框架**：Aegis框架包含以下主要模块：1) LLM操纵器：负责根据上下文信息，向成功的轨迹中注入不同类型的错误。2) 数据集构建：利用LLM操纵器生成包含错误标注的大规模数据集。3) 模型训练：基于生成的数据集，采用监督微调、强化学习和对比学习等范式训练错误归因模型。

**关键创新**：Aegis的关键创新在于利用LLM自动生成错误数据，摆脱了对人工标注的依赖，显著降低了数据获取成本，并提高了数据集的多样性。此外，Aegis框架支持多种学习范式，可以灵活地训练不同类型的错误归因模型。

**关键设计**：LLM操纵器的设计至关重要，需要能够理解多智能体系统的上下文信息，并注入合理的、具有代表性的错误。论文可能涉及了错误类型的选择、注入位置的确定、以及如何保证生成数据的质量等关键设计细节。此外，不同学习范式下的损失函数设计，以及模型结构的选取也是重要的技术细节。

## 📊 实验亮点

Aegis构建了一个包含9,533条轨迹的大型数据集，并基于此训练了错误归因模型。实验结果表明，使用Aegis生成的数据训练的模型在错误归因方面取得了显著提升，性能甚至可以与大一个数量级的专有模型相媲美，验证了自动化数据生成框架的有效性。

## 🎯 应用场景

Aegis的研究成果可应用于各种多智能体系统，例如自动驾驶、机器人协作、智能交通等领域。通过提高多智能体系统的可靠性和可解释性，可以减少系统故障带来的风险，并提升用户对系统的信任度。未来，该技术有望促进多智能体系统在更多领域的应用。

## 📄 摘要（原文）

> Large language model based multi-agent systems (MAS) have unlocked significant advancements in tackling complex problems, but their increasing capability introduces a structural fragility that makes them difficult to debug. A key obstacle to improving their reliability is the severe scarcity of large-scale, diverse datasets for error attribution, as existing resources rely on costly and unscalable manual annotation. To address this bottleneck, we introduce Aegis, a novel framework for Automated error generation and attribution for multi-agent systems. Aegis constructs a large dataset of 9,533 trajectories with annotated faulty agents and error modes, covering diverse MAS architectures and task domains. This is achieved using a LLM-based manipulator that can adaptively inject context-aware errors into successful execution trajectories. Leveraging fine-grained labels and the structured arrangement of positive-negative sample pairs, Aegis supports three different learning paradigms: Supervised Fine-Tuning, Reinforcement Learning, and Contrastive Learning. We develop learning methods for each paradigm. Comprehensive experiments show that trained models consistently achieve substantial improvements in error attribution. Notably, several of our fine-tuned LLMs demonstrate performance competitive with or superior to proprietary models an order of magnitude larger, validating our automated data generation framework as a crucial resource for developing more robust and interpretable multi-agent systems. Our project website is available at https://kfq20.github.io/Aegis-Website/.

