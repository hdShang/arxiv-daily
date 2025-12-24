---
layout: default
title: "Theory of Mind in Action: The Instruction Inference Task"
---

# Theory of Mind in Action: The Instruction Inference Task

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2507.02935" class="toolbar-btn" target="_blank">📄 arXiv: 2507.02935v1</a>
  <a href="https://arxiv.org/pdf/2507.02935.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2507.02935v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2507.02935v1', 'Theory of Mind in Action: The Instruction Inference Task')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Fardin Saad, Pradeep K. Murukannaiah, Munindar P. Singh

**分类**: cs.CL, cs.AI, cs.MA

**发布日期**: 2025-06-26

**备注**: Submitted to Artificial Intelligence Journal (under review). 51 pages with appendix (28 pages article + 4 pages references + 19 pages appendix), 7 figures (Appendix: 26 Figures), 6 tables. Code available at: https://github.com/fardinsaad/Tomcat-LLM

---

## 💡 一句话要点

**提出Instruction Inference任务以评估代理的心智理论能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `心智理论` `大型语言模型` `人机协作` `推理任务` `常识知识` `动态环境` `指令理解`

## 📋 核心要点

1. 现有方法在动态协作环境中评估心智理论能力时面临挑战，尤其是在理解模糊指令方面。
2. 本文提出Instruction Inference任务，通过设计基于LLM的代理Tomcat，来实现对间接指令的推理与响应。
3. 实验结果表明，Tomcat在Fs-CoT变体下，尤其是使用GPT-4o和DeepSeek-R1时，其性能与人类参与者相当，展示了良好的ToM能力。

## 📝 摘要（中文）

心智理论（ToM）指的是代理推断其他代理心理状态的能力，这对于有效的协作至关重要。为评估在动态、目标导向和协作环境中的ToM能力，本文提出了一项新任务——Instruction Inference，代理通过解释间接或模糊的指令来帮助主要代理实现目标。我们设计了基于大型语言模型（LLM）的代理Tomcat，展示了ToM推理能力。Tomcat有两个变体，分别是基于少量示例的Fs-CoT和依赖常识知识的CP。我们在三个领先的LLM上实现了这两个变体，并通过与52名参与者的研究评估了Tomcat的有效性。结果显示，特别是Fs-CoT变体在GPT-4o和DeepSeek-R1上表现出与人类参与者相当的性能，突显了其在人工智能与人类协作中的潜力。

## 🔬 方法详解

**问题定义**：本文旨在解决在动态、目标导向的协作环境中，代理如何有效推断和理解模糊指令的问题。现有方法在此方面的表现不佳，缺乏对复杂指令的理解能力。

**核心思路**：论文提出的核心思路是通过Instruction Inference任务，设计一个能够理解和推理间接指令的代理Tomcat，利用大型语言模型的能力来增强其心智理论推理能力。

**技术框架**：Tomcat的整体架构包括两个主要变体：Fs-CoT和CP。Fs-CoT基于少量示例进行推理，而CP则依赖于常识知识。我们在GPT-4o、DeepSeek-R1和Gemma-3-27B上实现了这两个变体。

**关键创新**：最重要的创新点在于将心智理论推理与大型语言模型结合，通过Instruction Inference任务评估代理的理解能力。这与传统方法的直接指令理解方式有本质区别。

**关键设计**：在设计中，Fs-CoT变体使用少量示例进行链式推理，而CP变体则通过常识提示来增强理解。我们还设计了评估指标，包括意图准确性、行动最优性和规划最优性，以全面评估ToM能力。

## 📊 实验亮点

实验结果显示，Tomcat的Fs-CoT变体在GPT-4o和DeepSeek-R1上表现出与52名人类参与者相当的性能，意图准确性和行动最优性均达到较高水平，展示了其在心智理论推理方面的潜力。

## 🎯 应用场景

该研究的潜在应用领域包括人机协作、智能助手和教育技术等。通过提升代理的心智理论能力，可以使其更好地理解和响应用户的需求，从而提高协作效率和用户体验。未来，这种技术可能在自动化决策、社交机器人等领域发挥重要作用。

## 📄 摘要（原文）

> The Theory of Mind (ToM) refers to an agent's capacity to infer the mental states of other agents. ToM is essential for effective collaboration. To assess ToM in a dynamic, goal-oriented, and collaborative environment, we introduce a novel task, Instruction Inference, in which an agent assists a principal in reaching a goal by interpreting indirect or ambiguous instructions. We present Tomcat, an LLM-based agent, designed to exhibit ToM reasoning in interpreting and responding to the principal's instructions. We implement two variants of Tomcat. One, dubbed Fs-CoT, is based on a small number of examples (i.e., few-shot or Fs) demonstrating the requisite structured reasoning (i.e., chain-of-thought or CoT). One, dubbed CP, relies on commonsense knowledge and information about the problem (i.e., commonsense prompt or CP). We realized both variants of Tomcat on three leading large language models (LLMs), namely, GPT-4o, DeepSeek-R1, and Gemma-3-27B. To evaluate the effectiveness of Tomcat, we conducted a study with 52 human participants in which we provided participants with the same information as the CP variant of Tomcat. We computed intent accuracy, action optimality, and planning optimality to measure the ToM capabilities of Tomcat and our study participants. We found that Tomcat with Fs-CoT, particularly with GPT-4o and DeepSeek-R1, achieves performance comparable to the human participants, underscoring its ToM potential for human-AI collaboration.

