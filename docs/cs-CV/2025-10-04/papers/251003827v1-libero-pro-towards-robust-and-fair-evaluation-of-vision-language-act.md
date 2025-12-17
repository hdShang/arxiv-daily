---
layout: default
title: LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization
---

# LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.03827" target="_blank" class="toolbar-btn">arXiv: 2510.03827v1</a>
    <a href="https://arxiv.org/pdf/2510.03827.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.03827v1" 
            onclick="toggleFavorite(this, '2510.03827v1', 'LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Xueyang Zhou, Yangming Xu, Guiyao Tie, Yongchao Chen, Guowen Zhang, Duanfeng Chu, Pan Zhou, Lichao Sun

**分类**: cs.CV, cs.RO

**发布日期**: 2025-10-04

**备注**: 12 pages,7 figures, 5 tables

**🔗 代码/项目**: [GITHUB](https://github.com/Zxy-MLlab/LIBERO-PRO)

---

## 💡 一句话要点

**提出LIBERO-PRO以解决现有VLA模型评估不公正问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉-语言-动作` `模型评估` `泛化能力` `系统评估` `多维度扰动`

## 📋 核心要点

1. 现有LIBERO基准在评估VLA模型时存在训练和评估设置不合理的问题，导致性能估计不准确。
2. LIBERO-PRO通过在操作对象、初始状态、任务指令和环境等四个维度上引入合理扰动，系统评估模型性能。
3. 实验结果显示，现有模型在标准评估中表现良好，但在LIBERO-PRO的设置下性能急剧下降，暴露出其对记忆的依赖。

## 📝 摘要（中文）

LIBERO已成为评估视觉-语言-动作（VLA）模型的广泛采用基准，但其当前的训练和评估设置存在问题，常导致性能估计膨胀，阻碍模型的公平比较。为了解决这些问题，本文提出了LIBERO-PRO，一个扩展的LIBERO基准，系统地在四个维度上评估模型性能：操作对象、初始状态、任务指令和环境。实验结果表明，尽管现有模型在标准LIBERO评估中达到90%以上的准确率，但在我们的广义设置下，其性能崩溃至0.0%。这一差异揭示了模型对训练集中的动作序列和环境布局的死记硬背依赖，而非真正的任务理解或环境感知。

## 🔬 方法详解

**问题定义**：本文旨在解决现有LIBERO基准在评估VLA模型时存在的训练和评估设置不合理的问题，这导致了模型性能的虚高估计和不公平比较。

**核心思路**：LIBERO-PRO通过引入合理的扰动，系统地评估模型在多种条件下的性能，确保模型不仅依赖于记忆，而是具备真正的任务理解能力。

**技术框架**：LIBERO-PRO的整体架构包括四个主要模块：操作对象的操控、初始状态的设定、任务指令的变化和环境的多样化。这些模块共同作用，形成一个综合的评估体系。

**关键创新**：LIBERO-PRO的最大创新在于其系统性地引入多维度扰动，显著提高了评估的严谨性和模型的泛化能力，与现有方法相比，提供了更为真实的性能评估。

**关键设计**：在设计中，关键参数包括扰动的类型和强度，损失函数的选择，以及网络结构的适应性调整，以确保模型在各种条件下的稳定性和准确性。通过这些设计，LIBERO-PRO能够有效评估模型的真实能力。

## 📊 实验亮点

实验结果显示，尽管现有模型在标准LIBERO评估中表现超过90%的准确率，但在LIBERO-PRO的广义设置下，其性能降至0.0%。这一结果揭示了模型对训练数据的过度依赖，强调了LIBERO-PRO在评估模型泛化能力方面的重要性。

## 🎯 应用场景

该研究的潜在应用领域包括机器人控制、自动驾驶、智能助手等需要视觉、语言和动作相结合的任务。通过提供更公正的模型评估，LIBERO-PRO能够推动VLA模型的实际应用和发展，提升其在复杂环境中的表现。未来，该基准可能成为VLA领域的标准评估工具，促进更高水平的研究和应用。

## 📄 摘要（原文）

> LIBERO has emerged as a widely adopted benchmark for evaluating Vision-Language-Action (VLA) models; however, its current training and evaluation settings are problematic, often leading to inflated performance estimates and preventing fair model comparison. To address these issues, we introduce LIBERO-PRO, an extended LIBERO benchmark that systematically evaluates model performance under reasonable perturbations across four dimensions: manipulated objects, initial states, task instructions, and environments. Experimental results reveal that, although existing models achieve over 90% accuracy under the standard LIBERO evaluation, their performance collapses to 0.0% under our generalized setting. Crucially, this discrepancy exposes the models' reliance on rote memorization of action sequences and environment layouts from the training set, rather than genuine task understanding or environmental perception. For instance, models persist in executing grasping actions when the target object is replaced with irrelevant items, and their outputs remain unchanged even when given corrupted instructions or even messy tokens. These findings expose the severe flaws in current evaluation practices, and we call on the community to abandon misleading methodologies in favor of robust assessments of model generalization and comprehension. Our code is available at: https://github.com/Zxy-MLlab/LIBERO-PRO.

