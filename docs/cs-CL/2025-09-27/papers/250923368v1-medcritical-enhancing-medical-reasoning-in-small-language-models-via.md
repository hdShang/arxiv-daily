---
layout: default
title: "MedCritical: Enhancing Medical Reasoning in Small Language Models via Self-Collaborative Correction"
---

# MedCritical: Enhancing Medical Reasoning in Small Language Models via Self-Collaborative Correction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.23368" class="toolbar-btn" target="_blank">📄 arXiv: 2509.23368v1</a>
  <a href="https://arxiv.org/pdf/2509.23368.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.23368v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.23368v1', 'MedCritical: Enhancing Medical Reasoning in Small Language Models via Self-Collaborative Correction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xinchun Su, Chunxu Luo, Yixuan Li, Weidong Yang, Lipeng Ma

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-27

---

## 💡 一句话要点

**MedCritical：通过自协作校正增强小语言模型在医疗推理中的能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `医疗推理` `小语言模型` `知识蒸馏` `自协作学习` `直接偏好优化` `长链思维` `模型自博弈`

## 📋 核心要点

1. 小语言模型在医疗推理任务中表现不足，现有知识蒸馏方法依赖大型模型作为教师，成本高昂。
2. MedCritical框架利用小语言模型自博弈，通过长链思维模板引导和自迭代DPO优化，提升推理能力。
3. 实验表明，MedCritical 7B模型在CMExam基准上超越同级别模型，实现了显著的性能提升。

## 📝 摘要（中文）

在医学领域，临床诊断、治疗计划和医学知识整合等复杂推理任务极具挑战性，小语言模型在这方面的表现通常不如GPT-4和Deepseek等大型语言模型。最近基于知识蒸馏的方法旨在通过教师引导的错误纠正来解决这些问题，但这种将LLM作为评判者的方法在成本、时间和效率方面仍然具有挑战性。为了规避这个问题，我们提出了一种新颖的两阶段框架MedCritical，它使用由大型教师模型微调的小型语言模型与自身进行博弈。在第一阶段，我们从教师模型中提取高层次和详细的长链思维模板，以指导学生模型生成更复杂的推理思维。在第二阶段，我们通过模型自迭代协作引入直接偏好优化（DPO），通过在训练期间与微调模型的校正轨迹进行博弈来增强学生模型的推理能力。这种模型自学习DPO方法教导学生模型利用自身错误驱动的见解来巩固其技能和知识，从而解决复杂问题，并以较低的成本实现了与使用教师模型的传统知识蒸馏方法相当的结果。值得注意的是，我们的MedCritical 7B模型在CMExam基准测试中优于Taiyi和Huatuo-o1-7B模型，分别提高了3.04％和10.12％，在7B级别的小型模型中实现了新的SOTA性能。

## 🔬 方法详解

**问题定义**：论文旨在解决小语言模型在复杂医疗推理任务中表现不佳的问题。现有基于知识蒸馏的方法依赖大型语言模型作为教师，存在成本高、效率低等问题，限制了其在资源受限场景下的应用。

**核心思路**：论文的核心思路是利用小语言模型自身进行学习和提升，避免对大型教师模型的依赖。通过让模型与自身生成的校正轨迹进行博弈，模拟教师指导的过程，从而提高模型的推理能力。

**技术框架**：MedCritical框架包含两个主要阶段：1) **长链思维模板引导**：从大型教师模型中提取高层次和详细的推理链模板，用于指导学生模型生成更复杂的推理过程。2) **自迭代直接偏好优化（DPO）**：通过让学生模型与自身微调后的校正轨迹进行博弈，利用DPO算法优化模型的偏好，使其更倾向于正确的推理路径。

**关键创新**：该方法的核心创新在于利用模型自身进行学习和优化，避免了对大型教师模型的依赖。通过自博弈和DPO算法，实现了知识的自我提炼和能力的提升，降低了训练成本，提高了效率。

**关键设计**：长链思维模板的设计需要仔细考虑，以确保能够有效地引导学生模型进行推理。DPO算法中的奖励函数需要合理设计，以区分正确的推理路径和错误的推理路径。此外，自迭代的次数也需要进行调整，以达到最佳的训练效果。

## 📊 实验亮点

MedCritical 7B模型在CMExam基准测试中取得了显著的性能提升，超越了Taiyi和Huatuo-o1-7B模型，分别提高了3.04%和10.12%，在7B级别的小型模型中实现了新的SOTA性能。这表明该方法能够有效地提升小语言模型在医疗推理任务中的能力。

## 🎯 应用场景

MedCritical具有广泛的应用前景，可用于辅助临床决策、医学知识问答、智能诊断等领域。该方法降低了对大型语言模型的依赖，使得小语言模型也能在医疗领域发挥重要作用，尤其适用于资源受限的医疗机构和移动医疗应用。

## 📄 摘要（原文）

> In the field of medicine, complex reasoning tasks such as clinical diagnosis, treatment planning, and medical knowledge integration pose significant challenges, where small language models often underperform compared to large language models like GPT-4 and Deepseek. Recent knowledge distillation-based methods aim to address these issues through teacher-guided error correction, but this LLM as judge approach remains challenging in terms of cost, time, and efficiency. To circumvent this issue, we propose a novel two-stage framework, MedCritical, which uses a small language model fine-tuned by a large teacher model to play against itself. In the first stage, we extract high-level and detailed long-chain thought templates from the teacher model to guide the student model to generate more complex reasoning thoughts. In the second stage, we introduce direct preference optimization (DPO) through model self-iteration collaboration to enhance the reasoning ability of the student model by playing against the correction trajectory of the fine-tuned model during training. This model self-learning DPO approach teaches the student model to use its own error-driven insights to consolidate its skills and knowledge to solve complex problems, and achieves comparable results to traditional knowledge distillation methods using teacher models at a lower cost. Notably, our MedCritical 7B model outperforms the Taiyi and Huatuo-o1-7B models by 3.04\% and 10.12\% respectively on the CMExam benchmark, achieving new SOTA performance among 7B-class small models.

