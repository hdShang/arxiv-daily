---
layout: default
title: "AdaThink-Med: Medical Adaptive Thinking with Uncertainty-Guided Length Calibration"
---

# AdaThink-Med: Medical Adaptive Thinking with Uncertainty-Guided Length Calibration

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.24560" class="toolbar-btn" target="_blank">📄 arXiv: 2509.24560v1</a>
  <a href="https://arxiv.org/pdf/2509.24560.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.24560v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.24560v1', 'AdaThink-Med: Medical Adaptive Thinking with Uncertainty-Guided Length Calibration')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shaohao Rui, Kaitao Chen, Weijie Ma, Xiaosong Wang

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-29

---

## 💡 一句话要点

**AdaThink-Med：提出一种不确定性引导长度校准的医学自适应思考框架**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `医学大语言模型` `自适应思考` `不确定性引导` `长度校准` `推理效率`

## 📋 核心要点

1. 医学大语言模型推理过程冗长，忽略了问题难度，导致推理成本增加，亟需自适应思考能力。
2. AdaThink-Med通过不确定性引导的长度校准，使模型能够根据问题难度调整推理长度。
3. 实验表明，AdaThink-Med在保持性能的同时，显著减少了推理长度，并展现出两种推理模式。

## 📝 摘要（中文）

本文提出AdaThink-Med，一种端到端框架，旨在增强医学推理模型中的自适应思考能力，该框架通过不确定性引导的长度校准实现。AdaThink-Med首先为每个问题生成多个候选输出，评估每个候选的正确性和不确定性，然后通过不确定性引导的长度校准模块估计问题难度。对于难度低且答案正确的输出，该框架会惩罚较长的推理路径；而对于难度高且答案错误的输出，则鼓励扩展思考链以探索替代解决方案。在六个公共医学问答基准测试中，AdaThink-Med平均实现了高达6.4倍的长度缩减，同时保持了性能，仅有最小的下降。有趣的是，我们观察到AdaThink-Med自发地发展出两种不同的推理模式，我们将其描述为“非思考”和“思考”，这证明了该模型动态抑制冗余推理过程的能力。

## 🔬 方法详解

**问题定义**：现有医学大语言模型在推理时，无论问题难易程度，都倾向于进行冗长的思考链，这导致了不必要的计算资源消耗，尤其是在实际应用中，效率低下。因此，如何使医学大语言模型能够根据问题的难度自适应地调整推理长度，成为一个重要的研究问题。

**核心思路**：AdaThink-Med的核心思路是利用模型自身对答案的不确定性来指导推理长度的调整。具体来说，模型会生成多个候选答案，并评估每个答案的正确性和不确定性。基于这些信息，模型可以估计问题的难度，并根据难度来调整推理长度：对于简单的问题，减少推理步骤；对于复杂的问题，增加推理步骤。

**技术框架**：AdaThink-Med框架主要包含以下几个模块：1) 候选答案生成模块：为每个问题生成多个候选答案。2) 正确性和不确定性评估模块：评估每个候选答案的正确性和不确定性。3) 不确定性引导的长度校准模块：基于候选答案的正确性和不确定性，估计问题难度，并调整推理长度。整体流程是，输入问题，生成多个候选答案，评估候选答案，根据评估结果调整推理长度，最终输出答案。

**关键创新**：AdaThink-Med的关键创新在于其利用不确定性来引导推理长度的自适应调整。与以往方法不同，AdaThink-Med不是预先设定固定的推理长度，而是根据模型自身对答案的置信度来动态调整推理长度。这种方法能够更有效地利用计算资源，并在保证性能的同时，显著减少推理时间。

**关键设计**：AdaThink-Med的关键设计包括：1) 不确定性度量方式：论文采用了一种基于模型输出概率分布的不确定性度量方法。2) 长度校准策略：论文设计了一种基于问题难度和答案正确性的长度校准策略，对于简单且正确的答案，惩罚过长的推理链；对于困难且错误的答案，鼓励更长的推理链。3) 损失函数设计：损失函数包含两部分，一部分是标准的交叉熵损失，用于保证模型的准确性；另一部分是长度惩罚项，用于鼓励模型生成更短的推理链。

## 📊 实验亮点

AdaThink-Med在六个公共医学问答基准测试中取得了显著的成果。实验结果表明，AdaThink-Med平均实现了高达6.4倍的推理长度缩减，同时仅有最小的性能下降。更重要的是，模型自发地学习到了两种不同的推理模式：“非思考”和“思考”，这表明模型能够根据问题的难度动态地抑制冗余的推理过程。

## 🎯 应用场景

AdaThink-Med具有广泛的应用前景，例如辅助医生进行诊断、提供个性化治疗建议、以及进行医学研究等。通过自适应地调整推理长度，AdaThink-Med可以显著提高医学大语言模型的效率，降低计算成本，使其更易于部署在实际医疗环境中。未来，该技术可以进一步扩展到其他医疗领域，例如药物研发、基因组学等。

## 📄 摘要（原文）

> Recent advances in inference time scaling with extended long chain-of thought have significantly improved the reasoning capabilities of both general and medical large language models (LLMs). However, these models tend to engage in lengthy reasoning processes regardless of the difficulty of the input question, leading to increased inference costs in real-world applications. Therefore, enabling adaptive thinking where models think less for simpler questions and think more for complex ones is critical for the effective use of medical LLMs in practice. Despite its importance, there is a lack of end-to-end approaches designed to enhance the adaptive thinking capabilities of medical LLMs while providing a comprehensive examination of the trade-off between performance and computational cost. To bridge this gap, we propose AdaThink-Med, the first end-to-end framework designed to enhance adaptive thinking ability in medical reasoning models with uncertainty-guided length calibration. AdaThink-Med first generates multiple candidate outputs for each question, evaluates the correctness and uncertainty of each candidate, and then estimates problem difficulty via an uncertainty-guided length calibration module. For outputs with low difficulty and correct answers, the framework penalizes longer reasoning paths; whereas for those with high difficulty and incorrect answers, it encourages extending the chain of thought to explore alternative solutions. On six public medical QA benchmarks, AdaThink-Med achieves up to 6.4x length reduction on average while retaining performance with only minimal degradation. Intriguingly, we observe that AdaThink-Med spontaneously develops two distinct reasoning modes, which we characterize as "non-thinking" and "thinking", demonstrating the model's ability to suppress redundant reasoning processes dynamically.

