---
layout: default
title: "Compliant Residual DAgger: Improving Real-World Contact-Rich Manipulation with Human Corrections"
---

# Compliant Residual DAgger: Improving Real-World Contact-Rich Manipulation with Human Corrections

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.16685" class="toolbar-btn" target="_blank">📄 arXiv: 2506.16685v4</a>
  <a href="https://arxiv.org/pdf/2506.16685.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.16685v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.16685v4', 'Compliant Residual DAgger: Improving Real-World Contact-Rich Manipulation with Human Corrections')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiaomeng Xu, Yifan Hou, Zeyi Liu, Shuran Song

**分类**: cs.RO, cs.LG

**发布日期**: 2025-06-20 (更新: 2025-12-11)

---

## 💡 一句话要点

**提出Compliant Residual DAgger以解决真实环境中接触丰富的操作问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `接触丰富操作` `人机协作` `策略学习` `合规控制` `机器人学习`

## 📋 核心要点

1. 现有的DAgger方法在收集人类修正数据和有效更新策略方面存在挑战，尤其是在接触丰富的操作任务中。
2. 提出的CR-DAgger通过合规干预接口和合规残差策略，允许人类在机器人执行任务时提供实时修正，提升了学习效率。
3. 实验结果表明，CR-DAgger在书本翻转和皮带组装任务中，成功率提高超过50%，优于传统的从头训练和微调方法。

## 📝 摘要（中文）

本文针对真实环境中接触丰富的操作任务中的数据集聚合（DAgger）面临的关键挑战，提出了Compliant Residual DAgger（CR-DAgger）。该方法包括两个创新组件：1）合规干预接口，利用合规控制，使人类能够在不打断机器人政策执行的情况下提供温和、准确的增量动作修正；2）合规残差策略的制定，能够在学习人类修正的同时，结合力反馈和力控制。通过使用最少的修正数据，我们的系统显著提升了在精确接触丰富操作任务上的表现，在书本翻转和皮带组装两个具有挑战性的任务中，基础策略的成功率提高了超过50%。

## 🔬 方法详解

**问题定义**：本文旨在解决在真实环境中进行接触丰富操作时，如何有效收集人类修正数据和更新策略的问题。现有方法在这方面的表现不足，难以适应复杂的操作场景。

**核心思路**：CR-DAgger的核心思路是通过合规干预接口和合规残差策略，允许人类在机器人执行任务时提供实时的、温和的修正，从而提高策略的学习效率和适应性。

**技术框架**：该方法的整体架构包括两个主要模块：合规干预接口和合规残差策略。合规干预接口负责接收人类的修正输入，而合规残差策略则在学习过程中结合力反馈进行策略更新。

**关键创新**：CR-DAgger的关键创新在于合规干预接口的设计，使得人类可以在不打断机器人操作的情况下进行修正，这一设计显著提高了人机协作的效率。

**关键设计**：在技术细节上，合规干预接口采用了力控制机制，确保修正动作的精确性和安全性。同时，合规残差策略通过引入力反馈，增强了对环境变化的适应能力。具体的损失函数和网络结构设计也经过优化，以提升学习效果。

## 📊 实验亮点

实验结果显示，CR-DAgger在书本翻转和皮带组装任务中，基础策略的成功率提高超过50%。与传统的从头训练和微调方法相比，CR-DAgger在数据利用效率和任务成功率上均表现出显著优势。

## 🎯 应用场景

该研究的潜在应用领域包括工业机器人、服务机器人以及任何需要与人类协作的自动化系统。通过提高机器人在复杂环境中的操作能力，CR-DAgger能够显著提升生产效率和安全性，未来可能在智能制造和家庭自动化等领域产生深远影响。

## 📄 摘要（原文）

> We address key challenges in Dataset Aggregation (DAgger) for real-world contact-rich manipulation: how to collect informative human correction data and how to effectively update policies with this new data. We introduce Compliant Residual DAgger (CR-DAgger), which contains two novel components: 1) a Compliant Intervention Interface that leverages compliance control, allowing humans to provide gentle, accurate delta action corrections without interrupting the ongoing robot policy execution; and 2) a Compliant Residual Policy formulation that learns from human corrections while incorporating force feedback and force control. Our system significantly enhances performance on precise contact-rich manipulation tasks using minimal correction data, improving base policy success rates by over 50\% on two challenging tasks (book flipping and belt assembly) while outperforming both retraining-from-scratch and finetuning approaches. Through extensive real-world experiments, we provide practical guidance for implementing effective DAgger in real-world robot learning tasks. Result videos are available at: https://compliant-residual-dagger.github.io/

