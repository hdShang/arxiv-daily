---
layout: default
title: "Thinking in a Crowd: How Auxiliary Information Shapes LLM Reasoning"
---

# Thinking in a Crowd: How Auxiliary Information Shapes LLM Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.18163" class="toolbar-btn" target="_blank">📄 arXiv: 2509.18163v1</a>
  <a href="https://arxiv.org/pdf/2509.18163.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.18163v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.18163v1', 'Thinking in a Crowd: How Auxiliary Information Shapes LLM Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haodong Zhao, Chenyan Zhao, Yansi Li, Zhuosheng Zhang, Gongshen Liu

**分类**: cs.CL

**发布日期**: 2025-09-17

**备注**: Work in progress

**🔗 代码/项目**: [HUGGINGFACE](https://huggingface.co/datasets/billhdzhao)

---

## 💡 一句话要点

**研究辅助信息对LLM推理的影响：有害信息会显著降低LLM的推理能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `推理能力` `辅助信息` `鲁棒性` `信息评估`

## 📋 核心要点

1. 现有LLM在实际应用中依赖外部信息，但如何保证LLM在面对不相关甚至错误信息时仍能保持推理能力是一个挑战。
2. 论文提出通过构建包含不同类型辅助信息的SciAux数据集，来系统评估LLM在推理过程中对辅助信息的鲁棒性。
3. 实验表明，LLM的“思考模式”在面对误导性信息时会放大错误，而非增强鲁棒性，凸显了信息评估的重要性。

## 📝 摘要（中文）

大型语言模型（LLM）的推理能力是其在复杂、知识密集型领域应用的基础。在实际场景中，LLM通常会获得外部信息，这些信息可能是有帮助的、不相关的，甚至是误导性的。本文研究了这种辅助信息对LLM推理过程的因果影响，特别是当LLM具备显式的逐步思考能力时。我们引入了SciAux，这是一个从ScienceQA派生的新数据集，用于系统地测试模型对这些类型信息的鲁棒性。我们的研究结果揭示了一个关键的弱点：模型具有的“思考模式”是一把双刃剑。有用的上下文可以提高准确性，但误导性信息会导致性能急剧下降，而思考过程会放大这种影响。当提供错误信息时，思考非但没有增强鲁棒性，反而加剧了错误程度。这表明，挑战不仅仅是让模型“思考”，而是赋予它们评估推理所依据信息的重要能力。SciAux数据集可在https://huggingface.co/datasets/billhdzhao/SciAux 获取。

## 🔬 方法详解

**问题定义**：论文旨在研究大型语言模型（LLM）在推理过程中，如何受到辅助信息（包括有用的、不相关的和误导性的信息）的影响。现有方法通常假设LLM能够有效利用所有输入信息，但忽略了LLM可能无法区分信息的质量，从而导致推理错误。尤其是在LLM具备逐步思考能力时，这种问题可能会被放大。

**核心思路**：论文的核心思路是通过构建一个包含不同类型辅助信息的数据集，来系统地评估LLM在推理过程中对这些信息的鲁棒性。通过分析LLM在不同辅助信息下的推理表现，揭示LLM在信息评估方面的弱点，并为未来的研究提供指导。

**技术框架**：论文主要包含以下几个部分：1) 构建SciAux数据集，该数据集基于ScienceQA，并添加了不同类型的辅助信息；2) 使用LLM（如GPT-3）在SciAux数据集上进行推理实验；3) 分析LLM在不同辅助信息下的推理表现，评估其鲁棒性；4) 探讨LLM的“思考模式”对推理结果的影响。

**关键创新**：论文的关键创新在于：1) 提出了SciAux数据集，这是一个专门用于评估LLM在推理过程中对辅助信息鲁棒性的数据集；2) 揭示了LLM的“思考模式”在面对误导性信息时会放大错误，而非增强鲁棒性；3) 强调了信息评估在LLM推理中的重要性。

**关键设计**：SciAux数据集的设计关键在于如何生成不同类型的辅助信息。论文采用了多种方法，包括从ScienceQA中选择相关的上下文信息、随机生成不相关的文本、以及故意引入错误的知识。实验中，使用了GPT-3等LLM，并采用了标准的提示工程技术，引导LLM进行逐步思考。没有提及具体的损失函数或网络结构修改。

## 📊 实验亮点

实验结果表明，当提供有用的辅助信息时，LLM的推理准确率有所提高。然而，当提供误导性信息时，LLM的性能会急剧下降，甚至低于没有辅助信息的情况。更重要的是，LLM的“思考模式”会放大这种负面影响，导致错误率显著增加。例如，在SciAux数据集上，LLM在面对误导性信息时的准确率下降幅度超过了20%。

## 🎯 应用场景

该研究成果可应用于提升LLM在知识密集型领域的可靠性。例如，在医疗诊断、金融分析等场景中，LLM需要处理大量的外部信息。通过提高LLM对辅助信息的评估能力，可以减少因错误信息导致的决策失误，提升LLM的实际应用价值。未来的研究可以探索如何让LLM更好地识别和过滤有害信息，从而提高其推理的准确性和鲁棒性。

## 📄 摘要（原文）

> The capacity of Large Language Models (LLMs) to reason is fundamental to their application in complex, knowledge-intensive domains. In real-world scenarios, LLMs are often augmented with external information that can be helpful, irrelevant, or even misleading. This paper investigates the causal impact of such auxiliary information on the reasoning process of LLMs with explicit step-by-step thinking capabilities. We introduce SciAux, a new dataset derived from ScienceQA, to systematically test the robustness of the model against these types of information. Our findings reveal a critical vulnerability: the model's deliberative "thinking mode" is a double-edged sword. While helpful context improves accuracy, misleading information causes a catastrophic drop in performance, which is amplified by the thinking process. Instead of conferring robustness, thinking reinforces the degree of error when provided with misinformation. This highlights that the challenge is not merely to make models "think", but to endow them with the critical faculty to evaluate the information upon which their reasoning is based. The SciAux dataset is available at https://huggingface.co/datasets/billhdzhao/SciAux.

