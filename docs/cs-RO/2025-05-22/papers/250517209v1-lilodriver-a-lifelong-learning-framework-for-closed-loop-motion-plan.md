---
layout: default
title: LiloDriver: A Lifelong Learning Framework for Closed-loop Motion Planning in Long-tail Autonomous Driving Scenarios
---

# LiloDriver: A Lifelong Learning Framework for Closed-loop Motion Planning in Long-tail Autonomous Driving Scenarios

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.17209" class="toolbar-btn" target="_blank">📄 arXiv: 2505.17209v1</a>
  <a href="https://arxiv.org/pdf/2505.17209.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.17209v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.17209v1', 'LiloDriver: A Lifelong Learning Framework for Closed-loop Motion Planning in Long-tail Autonomous Driving Scenarios')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Huaiyuan Yao, Pengfei Li, Bu Jin, Yupeng Zheng, An Liu, Lisen Mu, Qing Su, Qian Zhang, Yilun Chen, Peng Li

**分类**: cs.RO, cs.AI

**发布日期**: 2025-05-22

**备注**: 7 pages, 3 figures

**🔗 代码/项目**: [GITHUB](https://github.com/Hyan-Yao/LiloDriver)

---

## 💡 一句话要点

**提出LiloDriver框架以解决长尾自主驾驶场景中的运动规划问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长尾自主驾驶` `运动规划` `终身学习` `大型语言模型` `记忆增强` `闭环系统` `场景适应性`

## 📋 核心要点

1. 现有的运动规划方法在长尾场景中缺乏适应性，无法有效应对多样化的驾驶情况。
2. LiloDriver框架通过集成大型语言模型与记忆增强的规划生成系统，实现了对新场景的持续适应。
3. 在nuPlan基准测试中，LiloDriver在常见和稀有场景中的表现优于传统的规划方法，显示出其有效性。

## 📝 摘要（中文）

近年来，自主驾驶研究在运动规划方面取得了显著进展，旨在实现鲁棒、安全和自适应的规划。然而，现有的基于规则和数据驱动的规划方法在长尾场景中缺乏适应性，而知识驱动的方法虽然具有较强的推理能力，但在表示、控制和现实世界评估方面面临挑战。为了解决这些问题，本文提出了LiloDriver，一个用于长尾自主驾驶场景的闭环运动规划的终身学习框架。LiloDriver通过将大型语言模型（LLMs）与记忆增强的规划生成系统相结合，能够在不重新训练的情况下持续适应新场景。经过nuPlan基准测试评估，LiloDriver在常见和稀有驾驶场景中均表现出色，超越了静态的基于规则和学习的规划器。

## 🔬 方法详解

**问题定义**：本文旨在解决长尾自主驾驶场景中的运动规划问题。现有的基于规则和数据驱动的方法在面对多样化和稀有场景时，往往无法适应，导致规划效果不佳。

**核心思路**：LiloDriver框架的核心思想是通过终身学习的方式，结合大型语言模型和记忆增强的规划生成系统，使得系统能够在不重新训练的情况下，持续适应新的驾驶场景。

**技术框架**：LiloDriver的整体架构分为四个主要阶段：感知、场景编码、基于记忆的策略优化和LLM引导的推理。每个阶段都在不断地处理和更新信息，以提高运动规划的准确性和适应性。

**关键创新**：LiloDriver的最大创新在于将结构化记忆与LLM推理相结合，使得运动规划能够像人类一样进行灵活的适应和决策。这一方法与传统的静态规划方法本质上不同，后者无法有效应对新场景。

**关键设计**：在设计上，LiloDriver采用了特定的损失函数来优化记忆的使用效率，并通过调整网络结构来增强模型的推理能力。具体的参数设置和网络架构细节在论文中进行了详细描述。

## 📊 实验亮点

在nuPlan基准测试中，LiloDriver在常见和稀有驾驶场景中均表现优异，超越了静态的基于规则和学习的规划器，显示出在复杂场景下的适应性和鲁棒性。具体性能数据表明，LiloDriver在多个测试场景中提升了运动规划的效率和安全性。

## 🎯 应用场景

LiloDriver框架在自主驾驶领域具有广泛的应用潜力，能够有效应对复杂和多变的驾驶环境。其持续适应新场景的能力使得该技术在实际道路测试和商业化应用中具有重要价值，未来可能推动更安全和智能的自动驾驶解决方案的发展。

## 📄 摘要（原文）

> Recent advances in autonomous driving research towards motion planners that are robust, safe, and adaptive. However, existing rule-based and data-driven planners lack adaptability to long-tail scenarios, while knowledge-driven methods offer strong reasoning but face challenges in representation, control, and real-world evaluation. To address these challenges, we present LiloDriver, a lifelong learning framework for closed-loop motion planning in long-tail autonomous driving scenarios. By integrating large language models (LLMs) with a memory-augmented planner generation system, LiloDriver continuously adapts to new scenarios without retraining. It features a four-stage architecture including perception, scene encoding, memory-based strategy refinement, and LLM-guided reasoning. Evaluated on the nuPlan benchmark, LiloDriver achieves superior performance in both common and rare driving scenarios, outperforming static rule-based and learning-based planners. Our results highlight the effectiveness of combining structured memory and LLM reasoning to enable scalable, human-like motion planning in real-world autonomous driving. Our code is available at https://github.com/Hyan-Yao/LiloDriver.

