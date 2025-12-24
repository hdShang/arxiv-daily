---
layout: default
title: "RetoVLA: Reusing Register Tokens for Spatial Reasoning in Vision-Language-Action Models"
---

# RetoVLA: Reusing Register Tokens for Spatial Reasoning in Vision-Language-Action Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.21243" class="toolbar-btn" target="_blank">📄 arXiv: 2509.21243v1</a>
  <a href="https://arxiv.org/pdf/2509.21243.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.21243v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.21243v1', 'RetoVLA: Reusing Register Tokens for Spatial Reasoning in Vision-Language-Action Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiyeon Koo, Taewan Cho, Hyunjoon Kang, Eunseom Pyo, Tae Gyun Oh, Taeryang Kim, Andrew Jaeyong Choi

**分类**: cs.RO

**发布日期**: 2025-09-25

---

## 💡 一句话要点

**RetoVLA：通过复用Register Tokens增强VLA模型在机器人操作中的空间推理能力**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉语言动作模型` `机器人操作` `空间推理` `Register Tokens` `轻量化模型`

## 📋 核心要点

1. 现有VLA模型体积庞大，计算成本高昂，难以实际部署，而轻量化方法又往往牺牲空间推理能力。
2. RetoVLA复用Vision Transformer中原本用于伪影移除后被丢弃的Register Tokens，将其注入Action Expert，增强空间推理。
3. 实验表明，RetoVLA在定制的7自由度机器人手臂上，复杂操作任务的成功率绝对提升了17.1%。

## 📝 摘要（中文）

近期的Vision-Language-Action (VLA) 模型在机器人领域展现了卓越的泛化能力，但其庞大的规模和计算成本限制了实际部署。传统的轻量化方法通常会牺牲关键能力，特别是空间推理。这导致了效率和性能之间的权衡。为了解决这个问题，本文复用了Register Tokens，这些tokens最初用于Vision Transformers中的伪影移除，但随后被丢弃。我们假设这些tokens包含重要的空间信息，并提出了RetoVLA，一种通过将它们直接注入到Action Expert中来复用它们的架构。RetoVLA在保持轻量级结构的同时，利用这种重新利用的空间上下文来增强推理能力。通过一系列全面的实验，我们证明了RetoVLA的有效性。在定制的7自由度机器人手臂上，该模型在复杂操作任务中的成功率绝对提高了17.1%。我们的结果证实，直接重用Register Tokens可以增强空间推理，表明以前被丢弃的伪影实际上是机器人智能的一个有价值的、未被探索的资源。

## 🔬 方法详解

**问题定义**：论文旨在解决VLA模型在机器人操作任务中，模型体积大、计算成本高和空间推理能力不足的问题。现有轻量化方法虽然降低了计算成本，但牺牲了重要的空间推理能力，导致性能下降。因此，如何在保证模型轻量化的同时，提升空间推理能力是本文要解决的核心问题。

**核心思路**：论文的核心思路是复用Vision Transformer中原本用于伪影移除后被丢弃的Register Tokens。作者认为这些tokens包含了重要的空间信息，如果能够有效地利用这些信息，就可以在不显著增加模型复杂度的前提下，提升模型的空间推理能力。

**技术框架**：RetoVLA的整体架构是在现有的VLA模型基础上，增加了一个Register Token复用模块。该模块将Vision Transformer提取的Register Tokens提取出来，并将其注入到Action Expert中。Action Expert利用这些Register Tokens提供的空间信息，生成更精确的动作指令。整个流程包括：视觉信息提取、Register Token提取与注入、Action Expert处理和动作指令生成。

**关键创新**：RetoVLA的关键创新在于发现了并有效利用了原本被认为是“伪影”的Register Tokens。与现有方法不同，RetoVLA没有增加额外的网络层或参数来提升空间推理能力，而是通过复用现有资源，实现了性能的提升。这种方法在保证模型轻量化的同时，显著提升了空间推理能力。

**关键设计**：论文中没有详细说明Register Token注入Action Expert的具体方式，例如是否使用了特定的注意力机制或融合策略。损失函数和网络结构等技术细节也未在摘要中提及，具体实现细节未知。

## 📊 实验亮点

RetoVLA在定制的7自由度机器人手臂上进行了实验，结果表明，该模型在复杂操作任务中的成功率绝对提高了17.1%。这一显著的性能提升证明了复用Register Tokens对于增强VLA模型空间推理能力的有效性。该结果表明，先前被丢弃的Register Tokens实际上是机器人智能的一个有价值的资源。

## 🎯 应用场景

RetoVLA具有广泛的应用前景，可应用于各种需要机器人进行复杂操作的场景，如智能制造、医疗手术、家庭服务等。通过降低VLA模型的计算成本和提高空间推理能力，RetoVLA有望推动机器人技术在实际场景中的广泛应用，并促进人机协作的智能化发展。

## 📄 摘要（原文）

> Recent Vision-Language-Action (VLA) models demonstrate remarkable generalization in robotics but are restricted by their substantial size and computational cost, limiting real-world deployment. However, conventional lightweighting methods often sacrifice critical capabilities, particularly spatial reasoning. This creates a trade-off between efficiency and performance. To address this challenge, our work reuses Register Tokens, which were introduced for artifact removal in Vision Transformers but subsequently discarded. We suppose that these tokens contain essential spatial information and propose RetoVLA, a novel architecture that reuses them directly by injecting them into the Action Expert.
>   RetoVLA maintains a lightweight structure while leveraging this repurposed spatial context to enhance reasoning. We demonstrate RetoVLA's effectiveness through a series of comprehensive experiments. On our custom-built 7-DOF robot arm, the model achieves a 17.1%p absolute improvement in success rates for complex manipulation tasks. Our results confirm that reusing Register Tokens directly enhances spatial reasoning, demonstrating that what was previously discarded as an artifact is in fact a valuable, unexplored resource for robotic intelligence. A video demonstration is available at: https://youtu.be/2CseBR-snZg

