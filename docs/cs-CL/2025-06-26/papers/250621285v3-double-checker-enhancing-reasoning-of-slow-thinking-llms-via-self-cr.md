---
layout: default
title: "Double-Checker: Enhancing Reasoning of Slow-Thinking LLMs via Self-Critical Fine-Tuning"
---

# Double-Checker: Enhancing Reasoning of Slow-Thinking LLMs via Self-Critical Fine-Tuning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.21285" class="toolbar-btn" target="_blank">📄 arXiv: 2506.21285v3</a>
  <a href="https://arxiv.org/pdf/2506.21285.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.21285v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.21285v3', 'Double-Checker: Enhancing Reasoning of Slow-Thinking LLMs via Self-Critical Fine-Tuning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xin Xu, Tianhao Chen, Fan Zhang, Wanlong Liu, Pengxiang Li, Ajay Kumar Jaiswal, Yuchen Yan, Jishan Hu, Yang Wang, Hao Chen, Shiwei Liu, Shizhe Diao, Can Yang, Lu Yin

**分类**: cs.CL

**发布日期**: 2025-06-26 (更新: 2025-10-02)

**备注**: 10 pages

**🔗 代码/项目**: [GITHUB](https://github.com/XinXU-USTC/DoubleChecker)

---

## 💡 一句话要点

**提出Double-Checker以增强慢思维LLMs的推理能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `慢思维LLMs` `自我批评` `推理能力` `模型微调` `迭代优化` `AIME基准测试`

## 📋 核心要点

1. 现有的慢思维LLMs在生成批评和优化解决方案方面能力有限，影响了其推理效果。
2. Double-Checker框架通过自我批评和迭代优化，提升了LLMs的推理能力，增强了其生成的解决方案的可靠性。
3. 在AIME基准测试中，Double-Checker将通过率从4.4%提升至18.2%，显示出显著的性能提升。

## 📝 摘要（中文）

尽管慢思维的大型语言模型（LLMs）展现了类似反思的推理能力，但它们生成信息性批评和优化先前解决方案的能力仍然有限。本文提出了Double-Checker，一个旨在通过促进显式自我批评和迭代优化来增强慢思维LLMs推理能力的框架。通过在我们精心策划的1730个自我批评实例上进行微调，Double-Checker使长链推理LLMs能够在推理过程中迭代批评和优化其输出，直到它们在自生成的批评下评估其解决方案为正确。我们在全面的推理基准测试中验证了Double-Checker的有效性，结果表明，迭代自我批评显著增强了长链推理LLMs的推理能力。

## 🔬 方法详解

**问题定义**：本文旨在解决慢思维LLMs在生成信息性批评和优化先前解决方案方面的不足，现有方法无法有效提升其推理能力。

**核心思路**：Double-Checker通过引入显式自我批评机制，促使LLMs在推理过程中不断反思和优化其输出，从而提高推理的准确性和可靠性。

**技术框架**：该框架包括数据准备、模型微调和推理阶段。首先，使用1730个自我批评实例对模型进行微调，然后在推理过程中进行多轮自我批评和优化。

**关键创新**：Double-Checker的核心创新在于引入了迭代自我批评机制，使得LLMs能够在生成输出后进行反思和修正，这与传统的单次生成方法有本质区别。

**关键设计**：在模型微调过程中，采用特定的损失函数来鼓励模型生成更具批判性的输出，同时设计了适应性参数设置，以确保模型在自我批评时能够有效地调整其生成策略。

## 📊 实验亮点

实验结果显示，Double-Checker在AIME基准测试中的通过率从4.4%提升至18.2%，表明迭代自我批评显著增强了LLMs的推理能力。这一提升展示了该方法在复杂推理任务中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括教育、智能客服和内容生成等。通过提升LLMs的推理能力，Double-Checker能够为用户提供更准确和可靠的答案，进而提高人机交互的质量和效率。未来，该框架可能推动更高级的自我学习和自我优化模型的发展。

## 📄 摘要（原文）

> While slow-thinking large language models (LLMs) exhibit reflection-like reasoning, commonly referred to as the "aha moment:, their ability to generate informative critiques and refine prior solutions remains limited. In this paper, we introduce Double-Checker, a principled framework designed to enhance the reasoning capabilities of slow-thinking LLMs by fostering explicit self-critique and iterative refinement of their previous solutions. By fine-tuning on our curated 1,730 self-critical instances, Double-Checker empowers long-CoT LLMs to iteratively critique and refine their outputs during inference until they evaluate their solutions as correct under self-generated critiques. We validate the efficacy of Double-Checker across a comprehensive suite of reasoning benchmarks, demonstrating that iterative self-critique significantly enhances the reasoning capabilities of long-CoT LLMs. Notably, our Double-Checker increases the pass@1 performance on challenging AIME benchmarks from 4.4% to 18.2% compared to the original long-CoT LLMs. These results highlight a promising direction for developing more trustworthy and effective LLMs capable of structured self-critique. Our codes and data are available at https://github.com/XinXU-USTC/DoubleChecker

