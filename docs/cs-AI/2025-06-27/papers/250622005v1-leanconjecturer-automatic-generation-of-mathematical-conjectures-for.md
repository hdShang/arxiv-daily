---
layout: default
title: "LeanConjecturer: Automatic Generation of Mathematical Conjectures for Theorem Proving"
---

# LeanConjecturer: Automatic Generation of Mathematical Conjectures for Theorem Proving

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.22005" class="toolbar-btn" target="_blank">📄 arXiv: 2506.22005v1</a>
  <a href="https://arxiv.org/pdf/2506.22005.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.22005v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.22005v1', 'LeanConjecturer: Automatic Generation of Mathematical Conjectures for Theorem Proving')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Naoto Onda, Kazumi Kasaura, Yuta Oriike, Masaya Taniguchi, Akiyoshi Sannai, Sho Sonoda

**分类**: cs.AI

**发布日期**: 2025-06-27

**备注**: 15 pages, 4 figures, 5 tables

---

## 💡 一句话要点

**提出LeanConjecturer以解决数学猜想生成问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `数学猜想生成` `定理证明` `大型语言模型` `自动化` `拓扑学` `强化学习`

## 📋 核心要点

1. 现有的形式定理证明方法面临数据稀缺的挑战，限制了其应用和发展。
2. LeanConjecturer通过结合规则基础的上下文提取与LLM生成定理陈述，提出了一种新的猜想生成方法。
3. 实验结果显示，该系统平均每个种子文件生成103.25个新猜想，并成功验证了多个非平凡的拓扑学定理。

## 📝 摘要（中文）

我们介绍了LeanConjecturer，这是一个利用大型语言模型（LLMs）在Lean 4中自动生成大学级数学猜想的管道。我们的混合方法结合了基于规则的上下文提取与基于LLM的定理陈述生成，解决了形式定理证明中的数据稀缺挑战。通过迭代生成和评估，LeanConjecturer从40个Mathlib种子文件中生成了12,289个猜想，其中3,776个被识别为语法有效且非平凡的猜想。我们展示了这些生成的猜想在通过群体相对策略优化（GRPO）进行强化学习中的实用性，表明针对特定领域猜想的有针对性训练可以增强定理证明能力。我们的系统成功验证了多个拓扑学中的非平凡定理，展示了其在数学发现中的潜力。

## 🔬 方法详解

**问题定义**：本论文旨在解决形式定理证明中的数据稀缺问题，现有方法往往依赖于手动生成的猜想，效率低下且覆盖面有限。

**核心思路**：LeanConjecturer通过混合使用规则基础的上下文提取与大型语言模型生成定理陈述，自动生成数学猜想，从而提高生成效率和质量。

**技术框架**：该系统的整体架构包括上下文提取模块、LLM生成模块和迭代评估模块。首先提取数学上下文，然后利用LLM生成猜想，最后通过评估筛选有效猜想。

**关键创新**：LeanConjecturer的主要创新在于其混合方法，结合了规则基础和LLM的优点，显著提高了猜想生成的数量和质量，与传统方法相比具有更高的自动化程度。

**关键设计**：在设计中，系统设置了特定的参数以优化生成过程，并使用了适合数学猜想的损失函数，确保生成的猜想在语法上有效且具有非平凡性。

## 📊 实验亮点

实验结果表明，LeanConjecturer从40个种子文件中生成了12,289个猜想，其中3,776个被识别为有效且非平凡的猜想，平均每个种子文件生成103.25个新猜想。此外，该系统成功验证了多个拓扑学中的非平凡定理，展示了其在数学发现中的潜力。

## 🎯 应用场景

LeanConjecturer的潜在应用领域包括数学研究、教育和自动定理证明系统。其自动生成的猜想可以作为研究人员的灵感来源，促进数学领域的创新和发现，同时为教育提供丰富的教学材料，提升学习效果。

## 📄 摘要（原文）

> We introduce LeanConjecturer, a pipeline for automatically generating university-level mathematical conjectures in Lean 4 using Large Language Models (LLMs). Our hybrid approach combines rule-based context extraction with LLM-based theorem statement generation, addressing the data scarcity challenge in formal theorem proving. Through iterative generation and evaluation, LeanConjecturer produced 12,289 conjectures from 40 Mathlib seed files, with 3,776 identified as syntactically valid and non-trivial, that is, cannot be proven by \texttt{aesop} tactic. We demonstrate the utility of these generated conjectures for reinforcement learning through Group Relative Policy Optimization (GRPO), showing that targeted training on domain-specific conjectures can enhance theorem proving capabilities. Our approach generates 103.25 novel conjectures per seed file on average, providing a scalable solution for creating training data for theorem proving systems. Our system successfully verified several non-trivial theorems in topology, including properties of semi-open, alpha-open, and pre-open sets, demonstrating its potential for mathematical discovery beyond simple variations of existing results.

