---
layout: default
title: "SLIM: Subtrajectory-Level Elimination for More Effective Reasoning"
---

# SLIM: Subtrajectory-Level Elimination for More Effective Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.19502" class="toolbar-btn" target="_blank">📄 arXiv: 2508.19502v1</a>
  <a href="https://arxiv.org/pdf/2508.19502.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.19502v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.19502v1', 'SLIM: Subtrajectory-Level Elimination for More Effective Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xifeng Yao, Chengyuan Ma, Dongyu Lang, Yinhao Ni, Zhiwei Xu, Huarui Xie, Zihao Chen, Guang Shen, Dandan Tu, Yi Bai, Changzheng Zhang

**分类**: cs.AI

**发布日期**: 2025-08-27

**备注**: EMNLP 2025 Findings

---

## 💡 一句话要点

**提出SLIM框架以优化大语言模型的推理过程**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `复杂推理` `推理轨迹` `子轨迹优化` `5+2框架` `数学基准测试` `性能提升`

## 📋 核心要点

1. 现有大语言模型在复杂推理中生成的推理轨迹并不总是最优，某些部分可能对整体性能产生负面影响。
2. 本研究提出了“5+2”框架，通过系统识别和评估不理想的子轨迹，优化推理过程的流畅性和一致性。
3. 实验结果显示，该方法在推理过程中减少了25.9%的不理想子轨迹，并在数学基准测试中表现优异。

## 📝 摘要（中文）

近年来，大语言模型在复杂推理方面取得了显著进展，尤其是在测试时扩展的应用上。然而，现有方法生成的推理轨迹并不总是最优的。本研究将推理轨迹划分为子轨迹，并提出“5+2”框架，系统识别和评估不理想的子轨迹，确保其消除不会影响推理过程的整体流畅性。实验结果表明，该方法在推理过程中减少了25.9%的不理想子轨迹，并在仅使用三分之二的训练数据时，在困难的数学基准上实现了58.92%的平均准确率，超越了使用全部数据的58.06%的准确率。

## 🔬 方法详解

**问题定义**：本研究旨在解决大语言模型推理轨迹中存在的不理想子轨迹问题，现有方法未能有效识别和消除这些对推理性能有负面影响的部分。

**核心思路**：通过将推理轨迹划分为多个子轨迹，利用“5+2”框架系统识别不理想子轨迹，并确保其消除不会影响推理的整体流畅性。

**技术框架**：整体架构包括两个主要阶段：第一阶段是基于五个标准识别不理想子轨迹，第二阶段是评估这些子轨迹与后续内容的独立性。

**关键创新**：最重要的创新在于提出了“5+2”框架，系统化地识别和评估推理轨迹中的不理想子轨迹，与现有方法相比，显著提高了推理的有效性。

**关键设计**：在框架中，设计了特定的评估标准和采样算法，以确保选择的推理过程尽可能不包含不理想子轨迹，优化了数据的使用效率。

## 📊 实验亮点

实验结果显示，SLIM方法在推理过程中成功减少了25.9%的不理想子轨迹，并在仅使用三分之二的训练数据时，在困难的数学基准测试中实现了58.92%的平均准确率，超越了使用全部数据的58.06%的准确率，展现了显著的性能提升。

## 🎯 应用场景

该研究的潜在应用领域包括教育、金融和科学研究等需要复杂推理的场景。通过优化推理过程，能够提高大语言模型在实际应用中的准确性和效率，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> In recent months, substantial progress has been made in complex reasoning of Large Language Models, particularly through the application of test-time scaling. Notable examples include o1/o3/o4 series and DeepSeek-R1. When responding to a query, these models generate an extended reasoning trajectory, during which the model explores, reflects, backtracks, and self-verifies before arriving at a conclusion. However, fine-tuning models with such reasoning trajectories may not always be optimal. Our findings indicate that not all components within these reasoning trajectories contribute positively to the reasoning process; in fact, some components may affect the overall performance negatively. In this study, we divide a reasoning trajectory into individual subtrajectories and develop a "5+2" framework to: (1) systematically identify suboptimal subtrajectories within the reasoning trajectory based on five human-established criteria; (2) assess the independence of the suboptimal subtrajectories identified in (1) from the subsequent content, ensuring that their elimination does not compromise overall flow and coherence of the reasoning process. Additionally, a sampling algorithm, built upon the "5+2" framework, is employed to select data whose reasoning process is free from suboptimal subtrajectories to the highest degree. Experimental results demonstrate that our method can reduce the number of suboptimal subtrajectories by 25.9\% during the inference. Furthermore, our method achieves an average accuracy of 58.92\% on highly challenging math benchmarks with only two thirds of training data, surpassing the average accuracy of 58.06\% achieved with the entire data, and outperforming open-source datasets, when fine-tuning Qwen2.5-Math-7B. Finally, We validated our method under resource constraints and observed improved performance across various inference token limits.

