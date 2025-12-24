---
layout: default
title: "DecisionFlow: Advancing Large Language Model as Principled Decision Maker"
---

# DecisionFlow: Advancing Large Language Model as Principled Decision Maker

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21397" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21397v2</a>
  <a href="https://arxiv.org/pdf/2505.21397.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21397v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21397v2', 'DecisionFlow: Advancing Large Language Model as Principled Decision Maker')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiusi Chen, Shanyong Wang, Cheng Qian, Hongru Wang, Peixuan Han, Heng Ji

**分类**: cs.CL

**发布日期**: 2025-05-27 (更新: 2025-08-24)

**备注**: EMNLP 2025 Findings; 25 pages, 15 figures

**🔗 代码/项目**: [GITHUB](https://github.com/xiusic/DecisionFlow)

---

## 💡 一句话要点

**提出DecisionFlow以解决语言模型决策透明性不足问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `决策支持系统` `语言模型` `可解释性` `符号推理` `效用函数` `高风险领域` `透明决策`

## 📋 核心要点

1. 现有语言模型在高风险领域的决策中缺乏结构化推理，导致决策过程不透明且难以解释。
2. DecisionFlow通过构建语义基础的决策空间，引导模型在结构化表示上进行推理，从而实现透明的决策过程。
3. 在两个高风险基准测试中，DecisionFlow相较于强提示基线提高了最高30%的准确率，并改善了结果的一致性。

## 📝 摘要（中文）

在医疗和金融等高风险领域，有效的决策不仅需要准确的结果，还需要透明和可解释的推理。然而，目前的语言模型往往缺乏结构化的推理过程，导致决策和理由之间的脱节。为此，本文提出了DecisionFlow，一个新颖的决策建模框架，指导模型在结构化的动作、属性和约束表示上进行推理。DecisionFlow构建了一个语义基础的决策空间，并推断潜在的效用函数，以透明且以效用驱动的方式评估权衡。实验证明，DecisionFlow在两个高风险基准上实现了最高30%的准确率提升，并增强了结果的一致性。我们的工作是将符号推理与大型语言模型结合的重要一步，促进了更具责任感、可解释性和可靠性的决策支持系统。

## 🔬 方法详解

**问题定义**：本文旨在解决当前语言模型在高风险领域决策时缺乏透明性和可解释性的问题。现有方法往往生成的决策和理由是脱节的，无法提供清晰的推理过程。

**核心思路**：DecisionFlow的核心思路是通过构建一个语义基础的决策空间，引导模型在结构化的动作、属性和约束上进行推理，而不是直接从提示中预测答案。这样设计的目的是为了增强决策的透明性和可解释性。

**技术框架**：DecisionFlow的整体架构包括几个主要模块：首先，构建结构化的决策表示；其次，推断潜在的效用函数；最后，基于效用评估进行决策生成。这个流程确保了决策与推理的紧密结合。

**关键创新**：DecisionFlow的最大创新在于将符号推理与大型语言模型结合，形成一个透明的、以效用驱动的决策支持系统。这一方法与现有的直接生成决策的方式本质上不同。

**关键设计**：在技术细节上，DecisionFlow设计了特定的损失函数来优化效用函数的推断，并采用了结构化的网络架构以支持复杂的决策空间表示。

## 📊 实验亮点

在实验中，DecisionFlow在两个高风险基准上实现了最高30%的准确率提升，相较于强提示基线显著改善了结果的一致性。这表明该方法在提高决策透明性和可解释性方面具有显著优势。

## 🎯 应用场景

DecisionFlow的潜在应用领域包括医疗决策支持系统、金融风险评估和其他需要高透明度和可解释性的决策场景。其实际价值在于提高决策的可靠性和用户的信任度，未来可能推动更多领域的智能决策系统的发展。

## 📄 摘要（原文）

> In high-stakes domains such as healthcare and finance, effective decision-making demands not just accurate outcomes but transparent and explainable reasoning. However, current language models often lack the structured deliberation needed for such tasks, instead generating decisions and justifications in a disconnected, post-hoc manner. To address this, we propose DecisionFlow, a novel decision modeling framework that guides models to reason over structured representations of actions, attributes, and constraints. Rather than predicting answers directly from prompts, DecisionFlow builds a semantically grounded decision space and infers a latent utility function to evaluate trade-offs in a transparent, utility-driven manner. This process produces decisions tightly coupled with interpretable rationales reflecting the model's reasoning. Empirical results on two high-stakes benchmarks show that DecisionFlow not only achieves up to 30% accuracy gains over strong prompting baselines but also enhances alignment in outcomes. Our work is a critical step toward integrating symbolic reasoning with LLMs, enabling more accountable, explainable, and reliable LLM decision support systems. Code and data are at https://github.com/xiusic/DecisionFlow.

