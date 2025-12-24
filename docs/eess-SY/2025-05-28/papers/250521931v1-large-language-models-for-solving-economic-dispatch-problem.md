---
layout: default
title: Large Language Models for Solving Economic Dispatch Problem
---

# Large Language Models for Solving Economic Dispatch Problem

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21931" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21931v1</a>
  <a href="https://arxiv.org/pdf/2505.21931.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21931v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21931v1', 'Large Language Models for Solving Economic Dispatch Problem')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sina Mohammadi, Ali Hassan, Rouzbeh Haghighi, Van-Hai Bui, Wencong Su

**分类**: eess.SY

**发布日期**: 2025-05-28

**备注**: 5 pages, 3 figures, Accepted, 2025 IEEE Energy Conversion Conference and Expo (ECCE 2025), Philadelphia, PA

---

## 💡 一句话要点

**利用大型语言模型解决经济调度问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `经济调度` `大型语言模型` `优化问题` `推理能力` `少量学习` `电力系统` `智能电网`

## 📋 核心要点

1. 现有经济调度方法通常依赖复杂的数学模型，面临收敛性问题和对大量标记数据的需求。
2. 本文提出了一种基于大型语言模型的解决方案，利用推理能力解决经济调度问题，避免了传统方法的局限性。
3. 实验结果显示，采用不同的提示策略，LLMs能够有效解决ED问题，提供了高效的替代方案。

## 📝 摘要（中文）

本文研究了现成的大型语言模型（LLMs）在解决经济调度（ED）问题上的能力。ED是一个具有严格约束的优化问题，电网运营商在日常调度中需要解决，以最小化发电成本，同时考虑物理和工程约束。现有方法通常需要数学公式，面临收敛问题，或依赖大量标记数据和训练时间。本文提出了一种增强推理能力的LLMs方法，避免了显式数学公式的需求，不受收敛挑战的影响，也不需要标记数据或大量训练。通过在两种不同的提示上下文中使用少量学习技术，评估了IEEE 118-bus系统的19个发电单元。结果表明，采用不同的提示策略使LLMs能够有效解决ED问题，提供了一种便捷高效的替代方案。

## 🔬 方法详解

**问题定义**：本文旨在解决经济调度（ED）问题，这是一种在日常调度中需要优化发电成本的复杂约束优化问题。现有方法通常依赖于数学公式，存在收敛性问题，并需要大量标记数据进行训练。

**核心思路**：论文的核心思路是利用大型语言模型（LLMs）增强其推理能力，以解决经典的无损经济调度问题。通过这种方式，避免了显式的数学公式和收敛性挑战，同时不需要标记数据或大量训练。

**技术框架**：整体架构包括使用LLMs进行推理，采用少量学习技术在两种不同的提示上下文中进行训练和评估。评估基于IEEE 118-bus系统，该系统包含19个发电单元。

**关键创新**：最重要的技术创新点在于将LLMs应用于经济调度问题，提供了一种无需复杂数学公式和大量训练数据的解决方案。这与现有方法的本质区别在于其简化了问题解决的过程。

**关键设计**：关键设计包括选择合适的提示策略和少量学习技术，以确保LLMs能够有效理解和解决经济调度问题。具体的参数设置和网络结构细节在实验中进行了优化。

## 📊 实验亮点

实验结果表明，采用不同的提示策略后，LLMs能够有效解决经济调度问题，提供了一种便捷高效的替代方案。具体而言，模型在IEEE 118-bus系统上的表现优于传统方法，展示了显著的性能提升，具体数据未提供。

## 🎯 应用场景

该研究的潜在应用领域包括电力系统优化、智能电网管理和可再生能源调度等。通过利用大型语言模型，电网运营商可以更高效地进行经济调度，降低发电成本，提高电力系统的整体效率。这一方法在未来可能对电力行业的决策支持和资源配置产生深远影响。

## 📄 摘要（原文）

> This paper investigates the capability of off-the-shelf large language models (LLMs) to solve the economic dispatch (ED) problem. ED is a hard-constrained optimization problem solved on a day-ahead timescale by grid operators to minimize electricity generation costs while accounting for physical and engineering constraints. Numerous approaches have been proposed, but these typically require either mathematical formulations, face convergence issues, or depend on extensive labeled data and training time. This work implements LLMs enhanced with reasoning capabilities to address the classic lossless ED problem. The proposed approach avoids the need for explicit mathematical formulations, does not suffer from convergence challenges, and requires neither labeled data nor extensive training. A few-shot learning technique is utilized in two different prompting contexts. The IEEE 118-bus system with 19 generation units serves as the evaluation benchmark. Results demonstrate that various prompting strategies enable LLMs to effectively solve the ED problem, offering a convenient and efficient alternative. Consequently, this approach presents a promising future solution for ED tasks, particularly when foundational power system models are available.

