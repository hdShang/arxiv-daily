---
layout: default
title: DreamPRM-Code: Function-as-Step Process Reward Model with Label Correction for LLM Coding
---

# DreamPRM-Code: Function-as-Step Process Reward Model with Label Correction for LLM Coding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.15000" class="toolbar-btn" target="_blank">📄 arXiv: 2512.15000v1</a>
  <a href="https://arxiv.org/pdf/2512.15000.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.15000v1" onclick="toggleFavorite(this, '2512.15000v1', 'DreamPRM-Code: Function-as-Step Process Reward Model with Label Correction for LLM Coding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ruiyi Zhang, Peijia Qin, Qi Cao, Pengtao Xie

**分类**: cs.LG, cs.AI, cs.CL

**发布日期**: 2025-12-17

---

## 💡 一句话要点

**DreamPRM-Code：利用函数作为步骤的过程奖励模型，通过标签校正提升LLM代码生成能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `代码生成` `过程奖励模型` `大型语言模型` `元学习` `标签校正`

## 📋 核心要点

1. 现有的过程奖励模型在代码生成中效果有限，主要原因是代码步骤分解困难以及中间标签噪声大。
2. DreamPRM-Code将函数视为代码生成的推理步骤，并采用链式函数提示策略，鼓励生成模块化代码。
3. 该方法引入基于元学习的标签校正机制，利用最终单元测试结果来优化中间步骤的标签，提升模型性能。

## 📝 摘要（中文）

过程奖励模型(PRMs)对于通过测试时缩放改进大型语言模型(LLMs)至关重要，但由于代码中缺乏有意义的步骤分解以及蒙特卡洛生成的局部标签的噪声，它们在编码方面的有效性仍然有限。我们提出了DreamPRM-Code，一种以编码为中心的PRM，它使用链式函数提示策略将函数视为推理步骤，以诱导模块化代码生成，从而实现类似于数学推理任务的PRM训练和应用。为了解决标签噪声问题，DreamPRM-Code引入了一种基于元学习的校正机制，该机制利用干净的最终解决方案单元测试标签，并执行双层优化以细化中间标签。在测试时缩放的应用中，DreamPRM-Code在LiveCodeBench上实现了最先进的性能，pass@1率为80.9%，超过了OpenAI o4-mini。

## 🔬 方法详解

**问题定义**：现有的过程奖励模型(PRMs)在代码生成任务中面临两个主要问题：一是代码的步骤分解不像数学推理那样自然，难以定义有意义的中间步骤；二是使用蒙特卡洛方法生成的中间步骤标签通常包含噪声，影响PRM的训练效果。这些问题限制了PRMs在代码生成领域的应用。

**核心思路**：DreamPRM-Code的核心思路是将代码中的函数视为推理步骤，通过鼓励模型生成模块化的代码，从而将代码生成任务转化为类似于数学推理的任务。同时，为了解决中间标签噪声问题，该方法引入了一种基于元学习的标签校正机制，利用最终的单元测试结果来优化中间步骤的标签。

**技术框架**：DreamPRM-Code的整体框架包含以下几个主要模块：1) 链式函数提示模块：通过特定的prompting策略，引导LLM生成模块化的代码，每个函数对应一个推理步骤。2) 过程奖励模型训练模块：利用生成的代码和对应的中间步骤标签训练PRM。3) 基于元学习的标签校正模块：使用最终的单元测试结果，通过双层优化来校正中间步骤的标签。4) 测试时缩放模块：在测试阶段，利用训练好的PRM来指导LLM的代码生成过程。

**关键创新**：DreamPRM-Code的关键创新在于：1) 将函数作为代码生成的推理步骤，解决了代码步骤分解困难的问题。2) 引入基于元学习的标签校正机制，有效降低了中间标签的噪声。与现有方法相比，DreamPRM-Code能够更有效地利用PRM来提升LLM的代码生成能力。

**关键设计**：在链式函数提示模块中，设计了特定的prompting模板，引导LLM生成包含多个函数的模块化代码。在标签校正模块中，采用了双层优化策略：外层优化PRM的参数，内层优化中间步骤的标签。损失函数包括代码生成损失和标签校正损失。元学习器的具体结构未知。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15000v1/flowchart.png" alt="fig_0" loading="lazy">
</figure>
</div>

## 📊 实验亮点

DreamPRM-Code在LiveCodeBench数据集上取得了显著的性能提升，pass@1指标达到了80.9%，超过了OpenAI o4-mini模型，证明了该方法在代码生成领域的有效性。标签校正机制也显著提升了模型的性能，验证了其在降低标签噪声方面的作用。

## 🎯 应用场景

DreamPRM-Code具有广泛的应用前景，可以应用于自动化代码生成、代码补全、代码修复等领域。通过提升LLM的代码生成能力，可以显著提高软件开发的效率和质量。此外，该方法还可以推广到其他需要复杂推理的任务中，例如机器人控制、游戏AI等。

## 📄 摘要（原文）

> Process Reward Models (PRMs) have become essential for improving Large Language Models (LLMs) via test-time scaling, yet their effectiveness in coding remains limited due to the lack of meaningful step decompositions in code and the noise of Monte-Carlo-generated partial labels. We propose DreamPRM-Code, a coding-focused PRM that treats functions as reasoning steps using a Chain-of-Function prompting strategy to induce modular code generation, enabling PRM training and application analogous to mathematical reasoning tasks. To address label noise, DreamPRM-Code introduces a meta-learning-based correction mechanism that leverages clean final-solution unit-test labels and performs bi-level optimization to refine intermediate labels. Applying on test-time scaling, DreamPRM-Code achieved state-of-the-art performance on LiveCodeBench with 80.9 pass@1 rate, surpassing OpenAI o4-mini.

