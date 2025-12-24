---
layout: default
title: "Learning to Refine: Self-Refinement of Parallel Reasoning in LLMs"
---

# Learning to Refine: Self-Refinement of Parallel Reasoning in LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.00084" class="toolbar-btn" target="_blank">📄 arXiv: 2509.00084v1</a>
  <a href="https://arxiv.org/pdf/2509.00084.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.00084v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.00084v1', 'Learning to Refine: Self-Refinement of Parallel Reasoning in LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qibin Wang, Pu Zhao, Shaohan Huang, Fangkai Yang, Lu Wang, Furu Wei, Qingwei Lin, Saravan Rajmohan, Dongmei Zhang

**分类**: cs.LG, cs.AI, cs.CL

**发布日期**: 2025-08-27

---

## 💡 一句话要点

**提出生成自我精炼方法以提升大语言模型的推理能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `自我精炼` `推理能力` `测试时扩展` `生成模型` `混合训练`

## 📋 核心要点

1. 现有的测试时扩展方法如最佳选择和多数投票依赖于候选响应的质量，无法处理所有候选均错误的情况。
2. 本文提出生成自我精炼（GSR）框架，通过并行生成候选响应并进行自我精炼，合成更优解以解决复杂推理问题。
3. 实验结果显示，GSR在五个数学基准上达到了最先进的性能，并且在不同模型规模上表现出良好的鲁棒性。

## 📝 摘要（中文）

为进一步增强大语言模型（LLMs）解决复杂多步骤推理问题的能力，测试时扩展（TTS）方法受到广泛关注。现有方法如最佳选择和多数投票受限于候选响应的质量，当所有候选均错误时无法产生正确解。为此，本文提出生成自我精炼（GSR）框架，统一模型并行生成候选响应，然后基于问题及候选进行自我精炼，合成更优解。实验结果表明，该方法在五个数学基准上实现了最先进的性能，并且这种自我精炼能力在不同模型规模上具有鲁棒性，能够推广到分布外推理任务。

## 🔬 方法详解

**问题定义**：本文旨在解决大语言模型在推理任务中面临的挑战，尤其是现有方法在候选响应质量不佳时的局限性。现有的测试时扩展方法无法在所有候选均错误的情况下提供正确解答。

**核心思路**：提出生成自我精炼（GSR）框架，通过并行生成多个候选响应，并在此基础上进行自我精炼，以合成更优的解决方案。该设计旨在提升模型的推理能力，克服直接提示时的精炼效果不佳的问题。

**技术框架**：GSR框架包括两个主要阶段：第一阶段是并行生成候选响应，第二阶段是基于问题和候选进行自我精炼。模型通过联合优化直接解决问题和精炼候选响应两个目标。

**关键创新**：最重要的技术创新在于引入了自我精炼机制，使得模型能够在生成候选后进行进一步的优化，而不是依赖外部选择模型。这一机制使得模型在处理复杂推理任务时更加灵活和高效。

**关键设计**：在训练过程中，采用了混合训练管道，优化损失函数以同时关注问题解决和候选响应精炼，确保模型在不同任务和规模下的适应性和鲁棒性。

## 📊 实验亮点

实验结果表明，GSR方法在五个数学基准上达到了最先进的性能，相较于现有方法，性能提升幅度显著，展示了其在复杂推理任务中的有效性和鲁棒性。

## 🎯 应用场景

该研究的潜在应用领域包括教育、金融、医疗等需要复杂推理的场景。通过提升大语言模型的推理能力，可以在自动问答、智能助手和决策支持系统中发挥重要作用，未来可能推动更智能的AI系统发展。

## 📄 摘要（原文）

> To further enhance the ability of Large Language Models (LLMs) to solve complex, multi-step reasoning problems, test-time scaling (TTS) methods have gained widespread attention. Existing approaches such as Best-of-N and majority voting are limited as their performance depends on the quality of candidate responses, making them unable to produce a correct solution when all candidates are incorrect. Introducing an additional model to select the best response also incurs significant deployment costs. To this end, we introduce Generative Self-Refinement (GSR), a novel parallel test-time scaling framework where a unified model first generates a set of candidate responses in parallel and then performs self-refinement to synthesize a new superior solution based on a prompt consisting of the problem and these candidates. However, LLMs struggle to perform refinement effectively when prompted directly. Therefore, we design a hybrid training pipeline by jointly optimizing for two complementary objectives, solving problems directly and refining candidate responses. Experimental results demonstrate that our method achieves state-of-the-art performance across five mathematical benchmarks. We further show that this learned self-refinement skill is a model-agnostic enhancement, robust across different model scales and generalizing to out-of-distribution reasoning tasks.

