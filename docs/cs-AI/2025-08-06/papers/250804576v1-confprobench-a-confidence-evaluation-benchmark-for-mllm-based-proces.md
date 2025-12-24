---
layout: default
title: "ConfProBench: A Confidence Evaluation Benchmark for MLLM-Based Process Judges"
---

# ConfProBench: A Confidence Evaluation Benchmark for MLLM-Based Process Judges

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.04576" class="toolbar-btn" target="_blank">📄 arXiv: 2508.04576v1</a>
  <a href="https://arxiv.org/pdf/2508.04576.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.04576v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.04576v1', 'ConfProBench: A Confidence Evaluation Benchmark for MLLM-Based Process Judges')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yue Zhou, Yi Chang, Yuan Wu

**分类**: cs.AI

**发布日期**: 2025-08-06

---

## 💡 一句话要点

**提出ConfProBench以评估MLLM过程判断者的置信度**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `过程判断者` `置信度评估` `对抗性扰动` `鲁棒性测试` `评估指标`

## 📋 核心要点

1. 现有的MPJ基准主要关注步骤正确性分类，未能有效评估置信度分数的可靠性。
2. 提出ConfProBench基准，通过对抗性扰动测试MPJ的置信度鲁棒性，并引入新的评估指标。
3. 实验结果显示当前MPJ在置信度表现上存在局限性，为后续研究提供了有价值的基线。

## 📝 摘要（中文）

推理是多模态大语言模型（MLLM）解决复杂多模态任务的重要能力，而判断推理步骤的正确性对提升这一能力至关重要。近年来，基于MLLM的过程判断者（MPJ）被广泛应用于评估多模态任务中的推理步骤正确性。然而，现有的MPJ基准主要集中在步骤正确性分类和推理过程搜索上，忽视了一个关键方面：MPJ在步骤级别生成的置信度分数是否可靠。为了解决这一问题，我们提出了ConfProBench，这是第一个系统评估MPJ生成的步骤级置信度分数可靠性的综合基准。该基准构建了三种对抗性扰动的推理步骤：同义词替换、句法变换和图像扰动，以测试MPJ置信度在扰动下的鲁棒性。此外，我们引入了三种新的评估指标：置信度鲁棒性分数（CRS）、置信度敏感性分数（CSS）和置信度校准分数（CCS），分别评估鲁棒性、敏感性和校准性。我们评估了14个最先进的MLLM，包括专有和开源模型，实验揭示了当前MPJ置信度表现的局限性，并提供了竞争基线以支持未来研究。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有MPJ评估中对置信度分数可靠性缺乏关注的问题。现有方法主要集中在步骤正确性和推理过程的搜索上，未能全面评估MPJ的置信度表现。

**核心思路**：我们提出ConfProBench基准，通过构建对抗性扰动的推理步骤，系统性地评估MPJ生成的步骤级置信度分数的鲁棒性、敏感性和校准性。

**技术框架**：该基准包括三种类型的对抗性扰动：同义词替换、句法变换和图像扰动。每种扰动旨在测试MPJ在不同情况下的置信度表现。我们还设计了三种新的评估指标：CRS、CSS和CCS，分别用于评估鲁棒性、敏感性和校准性。

**关键创新**：最重要的创新在于首次提出了系统评估MPJ置信度分数可靠性的基准，并引入了新的评估指标，填补了现有研究的空白。

**关键设计**：在实验中，我们评估了14个最先进的MLLM模型，采用了多种对抗性扰动策略，确保评估的全面性和准确性。

## 📊 实验亮点

实验结果表明，当前MPJ在置信度表现上存在显著局限性，尤其在对抗性扰动下的鲁棒性较差。通过引入CRS、CSS和CCS指标，我们为未来的研究提供了竞争基线，促进了对MPJ的深入理解和改进。

## 🎯 应用场景

该研究的潜在应用领域包括多模态任务的自动评估、智能问答系统和人机交互等。通过提升MPJ的置信度评估能力，可以显著改善多模态系统的推理质量和用户体验，推动相关技术的进一步发展。

## 📄 摘要（原文）

> Reasoning is a critical capability of multimodal large language models (MLLMs) for solving complex multimodal tasks, and judging the correctness of reasoning steps is crucial for improving this capability. Recently, MLLM-based process judges (MPJs) have been widely used to assess the correctness of reasoning steps in multimodal tasks. Therefore, evaluating MPJs is important for identifying their limitations and guiding future improvements. However, existing benchmarks for MPJs mainly focus on tasks such as step correctness classification and reasoning process search, while overlooking a key aspect: whether the confidence scores produced by MPJs at the step level are reliable. To address this gap, we propose ConfProBench, the first comprehensive benchmark designed to systematically evaluate the reliability of step-level confidence scores generated by MPJs. Our benchmark constructs three types of adversarially perturbed reasoning steps: Synonym Substitution, Syntactic Transformation, and Image Perturbation, to test the robustness of MPJ confidence under perturbations. In addition, we introduce three novel evaluation metrics: Confidence Robustness Score (CRS), Confidence Sensitivity Score (CSS), and Confidence Calibration Score (CCS), which evaluate robustness, sensitivity, and calibration, respectively. We evaluate 14 state-of-the-art MLLMs, including both proprietary and open-source models. Experiments reveal limitations in current MPJs' confidence performance and offer competitive baselines to support future research.

