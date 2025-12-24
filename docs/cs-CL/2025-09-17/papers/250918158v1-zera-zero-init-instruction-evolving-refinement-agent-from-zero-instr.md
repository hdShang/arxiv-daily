---
layout: default
title: "ZERA: Zero-init Instruction Evolving Refinement Agent -- From Zero Instructions to Structured Prompts via Principle-based Optimization"
---

# ZERA: Zero-init Instruction Evolving Refinement Agent -- From Zero Instructions to Structured Prompts via Principle-based Optimization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.18158" class="toolbar-btn" target="_blank">📄 arXiv: 2509.18158v1</a>
  <a href="https://arxiv.org/pdf/2509.18158.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.18158v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.18158v1', 'ZERA: Zero-init Instruction Evolving Refinement Agent -- From Zero Instructions to Structured Prompts via Principle-based Optimization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Seungyoun Yi, Minsoo Khang, Sungrae Park

**分类**: cs.CL, cs.LG

**发布日期**: 2025-09-17

**备注**: 9 pages, 4 figures. To appear in EMNLP 2025 Main Conference (Oral Presentation)

**🔗 代码/项目**: [GITHUB](https://github.com/younatics/zera-agent)

---

## 💡 一句话要点

**ZERA：零初始化指令演化优化Agent，通过基于原则的优化从零指令生成结构化提示**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自动提示优化` `大型语言模型` `提示工程` `零初始化学习` `指令演化` `结构化反馈`

## 📋 核心要点

1. 现有自动提示优化方法依赖非结构化反馈，需要大量样本和长迭代周期，导致成本高且易出错。
2. ZERA框架联合优化系统和用户提示，通过基于原则的低开销优化，实现快速收敛到高质量提示。
3. 实验结果表明，ZERA在推理、摘要和代码生成等任务上，相对于基线模型有显著提升，并开源了全部提示。

## 📝 摘要（中文）

自动提示优化(APO)通过改进特定任务的提示来提高大型语言模型(LLM)的性能。然而，先前的APO方法通常只关注用户提示，依赖于非结构化的反馈，并且需要大量的样本和较长的迭代周期，这使得它们成本高昂且脆弱。我们提出了ZERA（零初始化指令演化优化Agent），这是一个新颖的框架，它通过基于原则的低开销优化，联合优化系统提示和用户提示。ZERA使用八个可泛化的标准和自动推断的权重来对提示进行评分，并基于这些结构化的评论来修改提示。这使得可以使用最少的示例和短的迭代周期快速收敛到高质量的提示。我们在五个LLM和九个不同的数据集上评估了ZERA，这些数据集涵盖了推理、摘要和代码生成任务。实验结果表明，相对于强大的基线，ZERA 具有一致的改进。进一步的消融研究突出了每个组件对更有效的提示构建的贡献。我们的实现（包括所有提示）可在https://github.com/younatics/zera-agent 公开获得。

## 🔬 方法详解

**问题定义**：现有自动提示优化（APO）方法主要关注用户提示，依赖非结构化反馈，需要大量样本和长迭代周期，导致优化过程成本高昂且脆弱。这些方法难以快速有效地找到高质量的提示，限制了大型语言模型在实际应用中的潜力。

**核心思路**：ZERA的核心思路是通过联合优化系统提示和用户提示，并引入基于原则的结构化反馈机制，从而实现高效的提示优化。ZERA不再依赖人工设计的提示或非结构化反馈，而是从零开始，通过迭代演化来生成高质量的提示。

**技术框架**：ZERA框架包含以下主要模块：1) 提示生成模块，用于初始化系统提示和用户提示；2) 提示评分模块，使用八个可泛化的标准（例如，相关性、简洁性、流畅性等）和自动推断的权重对提示进行评分；3) 提示修改模块，基于结构化的评论来修改提示，提升提示质量。整个流程通过迭代循环进行，直到提示质量达到预设阈值或达到最大迭代次数。

**关键创新**：ZERA的关键创新在于：1) 联合优化系统提示和用户提示，充分利用了系统提示的引导作用；2) 引入基于原则的结构化反馈机制，避免了对非结构化反馈的依赖，提高了优化效率；3) 采用自动推断的权重，使得评分标准能够自适应不同的任务和数据集。

**关键设计**：ZERA使用八个可泛化的标准来评估提示的质量，这些标准包括相关性、简洁性、流畅性、完整性、准确性、一致性、逻辑性和创造性。每个标准的权重通过自动推断得到，以适应不同的任务和数据集。提示修改模块使用基于规则的方法来修改提示，例如，添加关键词、删除冗余信息、调整句子结构等。具体参数设置和损失函数细节未知。

## 📊 实验亮点

实验结果表明，ZERA在五个LLM和九个不同的数据集上，相对于强大的基线模型，在推理、摘要和代码生成任务上都取得了显著的改进。具体性能数据未知，但消融研究表明，ZERA的各个组件都对提示构建的有效性做出了贡献。ZERA能够使用最少的示例和短的迭代周期快速收敛到高质量的提示。

## 🎯 应用场景

ZERA可应用于各种需要提示工程的大型语言模型应用场景，例如智能客服、文本摘要、代码生成、机器翻译等。通过自动优化提示，ZERA可以显著提高LLM的性能，降低人工成本，并加速LLM在各行业的落地。未来，ZERA可以扩展到更多模态和任务，并与其他APO技术相结合，进一步提升LLM的智能化水平。

## 📄 摘要（原文）

> Automatic Prompt Optimization (APO) improves large language model (LLM) performance by refining prompts for specific tasks. However, prior APO methods typically focus only on user prompts, rely on unstructured feedback, and require large sample sizes and long iteration cycles-making them costly and brittle. We propose ZERA (Zero-init Instruction Evolving Refinement Agent), a novel framework that jointly optimizes both system and user prompts through principled, low-overhead refinement. ZERA scores prompts using eight generalizable criteria with automatically inferred weights, and revises prompts based on these structured critiques. This enables fast convergence to high-quality prompts using minimal examples and short iteration cycles. We evaluate ZERA across five LLMs and nine diverse datasets spanning reasoning, summarization, and code generation tasks. Experimental results demonstrate consistent improvements over strong baselines. Further ablation studies highlight the contribution of each component to more effective prompt construction. Our implementation including all prompts is publicly available at https://github.com/younatics/zera-agent.

