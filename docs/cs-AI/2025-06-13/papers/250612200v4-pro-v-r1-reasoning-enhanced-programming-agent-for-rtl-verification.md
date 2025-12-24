---
layout: default
title: "PRO-V-R1: Reasoning Enhanced Programming Agent for RTL Verification"
---

# PRO-V-R1: Reasoning Enhanced Programming Agent for RTL Verification

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.12200" class="toolbar-btn" target="_blank">📄 arXiv: 2506.12200v4</a>
  <a href="https://arxiv.org/pdf/2506.12200.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.12200v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.12200v4', 'PRO-V-R1: Reasoning Enhanced Programming Agent for RTL Verification')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yujie Zhao, Zhijing Wu, Boqin Yuan, Zhongming Yu, Hejia Zhang, Wentao Ni, Chia-Tung Ho, Haoxing Ren, Jishen Zhao

**分类**: cs.AI, cs.AR

**发布日期**: 2025-06-13 (更新: 2025-12-08)

---

## 💡 一句话要点

**提出PRO-V-R1以解决RTL验证中的效率瓶颈问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `RTL验证` `大型语言模型` `开源框架` `强化学习` `功能正确率` `故障检测` `模块化系统`

## 📋 核心要点

1. 现有的RTL验证方法依赖于大型专有模型，导致高成本和数据隐私风险，缺乏开源解决方案。
2. 论文提出PRO-V-R1，一个模块化的自主验证框架，结合LLM推理与程序工具使用，提升RTL验证效率。
3. 实验结果显示，PRO-V-R1在功能正确率达到57.7%，故障检测率为34.0%，显著优于现有基线模型。

## 📝 摘要（中文）

寄存器传输级（RTL）验证是开发过程中的主要瓶颈，占据60-70%的开发时间。尽管大型语言模型（LLMs）在RTL自动化方面展现出潜力，但其研究重点主要集中在RTL生成而非验证上。目前的RTL验证方法依赖于大型专有模型（如GPT-4o）生成基于Python的功能参考，导致高成本和数据隐私风险。为此，我们提出了PRO-V-R1，这是首个可训练的开源自主RTL验证框架。我们的贡献包括设计了一个模块化的代理系统，建立了数据构建管道，并实现了高效的强化学习算法。实验结果表明，PRO-V-R1在功能正确率和故障检测方面显著优于现有的自动验证系统。

## 🔬 方法详解

**问题定义**：本论文旨在解决RTL验证过程中的效率瓶颈，现有方法依赖于大型专有模型，导致高成本和数据隐私风险，缺乏有效的开源解决方案。

**核心思路**：我们提出PRO-V-R1，通过结合大型语言模型（LLM）推理与程序化工具使用，构建一个模块化的代理系统，以实现自主的RTL验证。这样的设计旨在提高验证的效率和准确性，同时降低对专有模型的依赖。

**技术框架**：PRO-V-R1的整体架构包括三个主要模块：1) PRO-V sys模块，负责LLM推理与工具使用的结合；2) 数据构建管道，利用现有RTL数据集生成专家级轨迹；3) 强化学习算法，基于验证反馈优化验证流程。

**关键创新**：本研究的主要创新在于提出了一个开源的自主RTL验证框架，首次将LLM推理与程序工具使用相结合，显著提升了验证的功能正确率和故障检测能力。

**关键设计**：在设计中，我们采用了特定于验证的奖励机制，以强化学习算法优化整个验证工作流，确保了高效的训练和验证过程。

## 📊 实验亮点

实验结果表明，PRO-V-R1在功能正确率上达到了57.7%，而现有基线模型仅为25.7%；在故障检测方面，PRO-V-R1的检测率为34.0%，显著高于基线的21.8%。这些结果表明，PRO-V-R1在性能上具有显著优势。

## 🎯 应用场景

该研究的潜在应用领域包括集成电路设计、硬件验证和自动化测试等。通过提供一个开源的RTL验证框架，能够降低开发成本，提高验证效率，促进硬件设计领域的创新与发展。

## 📄 摘要（原文）

> Register-Transfer Level (RTL) verification is a primary bottleneck, consuming 60-70% of development time. While Large Language Models (LLMs) show promise for RTL automation, their performance and research focus have overwhelmingly centered on RTL generation rather than verification. Current methods for RTL verification rely on large scale proprietary models (e.g., GPT-4o) to generate Python-based functional references, incurring a high cost and raising data-privacy risks. To date, an end-to-end open-source solution for autonomous verification remains absent.
>   We introduce PRO-V-R1, the first trainable open-source agentic framework for autonomous RTL verification. Our contributions are threefold: (1) we design PRO-V sys, a modular agentic system that couples LLM-based reasoning with programmatic tool use for RTL verification; (2) we establish a data construction pipeline that leverages existing RTL datasets to build simulation-validated, expert-level trajectories tailored for supervised fine-tuning (SFT) RTL verification agents; and (3) we implement an efficient reinforcement learning (RL) algorithm that uses verification-specific rewards derived from program-tool feedback to optimize the end-to-end verification workflow. Our empirical evaluation demonstrates PRO-V-R1 achieves a 57.7% functional correctness rate and 34.0% in robust fault detection, significantly outperforming the base model's 25.7% and 21.8% (respectively) from the state-of-the-art (SOTA) automatic verification system. This configuration also outperforms large-scale proprietary LLMs in functional correctness and shows comparable robustness for fault detection.

