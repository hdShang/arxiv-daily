---
layout: default
title: "Med-RewardBench: Benchmarking Reward Models and Judges for Medical Multimodal Large Language Models"
---

# Med-RewardBench: Benchmarking Reward Models and Judges for Medical Multimodal Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.21430" class="toolbar-btn" target="_blank">📄 arXiv: 2508.21430v1</a>
  <a href="https://arxiv.org/pdf/2508.21430.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.21430v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.21430v1', 'Med-RewardBench: Benchmarking Reward Models and Judges for Medical Multimodal Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Meidan Ding, Jipeng Zhang, Wenxuan Wang, Cheng-Yi Li, Wei-Chieh Fang, Hsin-Yu Wu, Haiqin Zhong, Wenting Chen, Linlin Shen

**分类**: cs.CL, cs.AI, cs.CV

**发布日期**: 2025-08-29

**备注**: 19 pages, 5 figures, 3 tables

---

## 💡 一句话要点

**提出Med-RewardBench以解决医疗多模态大语言模型评估问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `医疗AI` `多模态大语言模型` `奖励模型` `基准评估` `临床决策` `专家注释` `性能提升`

## 📋 核心要点

1. 现有的医疗奖励模型和评估者研究不足，缺乏针对临床需求的专门基准，导致评估维度的缺失。
2. 论文提出Med-RewardBench基准，专注于医疗场景中MRMs和评估者的评估，包含多模态数据集和严格的评估流程。
3. 评估结果显示，32个最先进的MLLMs在与专家判断对齐方面面临重大挑战，同时基线模型通过微调实现了显著的性能提升。

## 📝 摘要（中文）

多模态大语言模型（MLLMs）在医疗应用中具有重要潜力，包括疾病诊断和临床决策。然而，这些任务需要高度准确、上下文敏感且专业对齐的响应，因此可靠的奖励模型和评估者至关重要。尽管其重要性，医疗奖励模型（MRMs）和评估者仍然未被充分探索，缺乏专门针对临床需求的基准。现有基准主要关注一般MLLM能力或将模型视为求解器，忽视了诊断准确性和临床相关性等重要评估维度。为此，我们提出了Med-RewardBench，这是第一个专门设计用于评估医疗场景中MRMs和评估者的基准。该基准包含跨越13个器官系统和8个临床科室的多模态数据集，共有1,026个专家注释案例。通过严格的三步流程，确保在六个临床关键维度上提供高质量的评估数据。我们评估了32个最先进的MLLMs，包括开源、专有和医疗特定模型，揭示了输出与专家判断对齐的重大挑战。此外，我们开发的基线模型通过微调显示出显著的性能提升。

## 🔬 方法详解

**问题定义**：本论文旨在解决医疗多模态大语言模型（MLLMs）在临床应用中的评估问题，现有方法未能充分考虑诊断准确性和临床相关性等关键维度。

**核心思路**：提出Med-RewardBench基准，专门设计用于评估医疗场景中的奖励模型和评估者，通过构建多模态数据集和严格的评估流程来提高评估的可靠性和有效性。

**技术框架**：整体架构包括数据集构建、专家注释、评估流程三个主要模块。数据集涵盖13个器官系统和8个临床科室，确保多样性和代表性。

**关键创新**：Med-RewardBench是首个专门针对医疗场景的评估基准，填补了现有研究的空白，提供了系统化的评估标准和方法。

**关键设计**：在数据集构建中，采用了严格的三步流程，确保数据质量；评估维度包括诊断准确性、临床相关性等，使用专家注释来验证模型输出的有效性。

## 📊 实验亮点

实验结果显示，32个最先进的MLLMs在与专家判断对齐方面存在显著挑战，尤其是在诊断准确性和临床相关性方面。同时，基线模型通过微调实现了性能的显著提升，证明了该基准的有效性和实用性。

## 🎯 应用场景

该研究的潜在应用领域包括医疗诊断支持系统、临床决策辅助工具等，能够帮助医生提高诊断准确性和决策效率。未来，Med-RewardBench的建立将推动医疗AI领域的标准化评估，促进相关技术的进一步发展和应用。

## 📄 摘要（原文）

> Multimodal large language models (MLLMs) hold significant potential in medical applications, including disease diagnosis and clinical decision-making. However, these tasks require highly accurate, context-sensitive, and professionally aligned responses, making reliable reward models and judges critical. Despite their importance, medical reward models (MRMs) and judges remain underexplored, with no dedicated benchmarks addressing clinical requirements. Existing benchmarks focus on general MLLM capabilities or evaluate models as solvers, neglecting essential evaluation dimensions like diagnostic accuracy and clinical relevance. To address this, we introduce Med-RewardBench, the first benchmark specifically designed to evaluate MRMs and judges in medical scenarios. Med-RewardBench features a multimodal dataset spanning 13 organ systems and 8 clinical departments, with 1,026 expert-annotated cases. A rigorous three-step process ensures high-quality evaluation data across six clinically critical dimensions. We evaluate 32 state-of-the-art MLLMs, including open-source, proprietary, and medical-specific models, revealing substantial challenges in aligning outputs with expert judgment. Additionally, we develop baseline models that demonstrate substantial performance improvements through fine-tuning.

