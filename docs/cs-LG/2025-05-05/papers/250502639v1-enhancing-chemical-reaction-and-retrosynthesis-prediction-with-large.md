---
layout: default
title: Enhancing Chemical Reaction and Retrosynthesis Prediction with Large Language Model and Dual-task Learning
---

# Enhancing Chemical Reaction and Retrosynthesis Prediction with Large Language Model and Dual-task Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.02639" class="toolbar-btn" target="_blank">📄 arXiv: 2505.02639v1</a>
  <a href="https://arxiv.org/pdf/2505.02639.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.02639v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.02639v1', 'Enhancing Chemical Reaction and Retrosynthesis Prediction with Large Language Model and Dual-task Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xuan Lin, Qingrui Liu, Hongxin Xiang, Daojian Zeng, Xiangxiang Zeng

**分类**: cs.LG, cs.AI, cs.CL

**发布日期**: 2025-05-05

**备注**: Accepted for publication at IJCAI 2025

---

## 💡 一句话要点

**提出ChemDual框架以解决化学反应与逆合成预测问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `化学反应预测` `逆合成预测` `大型语言模型` `双任务学习` `药物发现` `数据集构建`

## 📋 核心要点

1. 现有方法在化学反应和逆合成预测中面临数据集不足和任务关联性忽视的挑战。
2. ChemDual框架通过构建大规模指令数据集，并采用双任务学习策略，优化反应与逆合成的预测过程。
3. 在Mol-Instruction和USPTO-50K数据集上，ChemDual的表现超越了传统单任务方法和现有开源LLMs，显示出显著提升。

## 📝 摘要（中文）

化学反应和逆合成预测是药物发现中的基础任务。近期，大型语言模型（LLMs）在多个领域展现出潜力。然而，直接应用LLMs于这些任务面临两个主要挑战：缺乏大规模化学合成相关指令数据集，以及现有微调策略忽视反应与逆合成预测之间的密切关联。为此，本文提出ChemDual，一个新颖的LLM框架，构建了一个包含440万条指令的大规模数据集，并引入增强版LLaMA，采用多尺度分词器和双任务学习策略，优化反应与逆合成的预测过程。实验结果表明，ChemDual在Mol-Instruction和USPTO-50K数据集上实现了最先进的性能，显示出其在药物设计中的强大潜力。

## 🔬 方法详解

**问题定义**：本文旨在解决化学反应与逆合成预测中的数据集不足和任务关联性忽视的问题。现有方法通常依赖于小规模数据集，导致模型性能受限。

**核心思路**：ChemDual框架将反应与逆合成视为相关的重组与碎片化过程，通过构建大规模指令数据集来提升模型的学习能力，并采用双任务学习策略来共同优化这两个任务。

**技术框架**：ChemDual的整体架构包括数据集构建模块、增强版LLaMA模型、双任务学习模块和评估模块。数据集构建模块负责生成440万条指令，LLaMA模型则通过多尺度分词器进行优化。

**关键创新**：ChemDual的主要创新在于其双任务学习策略和大规模指令数据集的构建，这与传统的单任务方法形成鲜明对比，能够更好地捕捉反应与逆合成之间的关联性。

**关键设计**：在模型设计中，ChemDual采用了多尺度分词器以提高语言理解能力，并通过特定的损失函数来平衡反应与逆合成的学习过程，确保模型在两个任务上均能取得优异表现。

## 📊 实验亮点

ChemDual在Mol-Instruction和USPTO-50K数据集上的实验结果显示，其在反应和逆合成预测方面均达到了最先进的性能，显著超越了传统单任务方法和现有开源LLMs，具体提升幅度未知，进一步验证了其在药物设计中的应用潜力。

## 🎯 应用场景

ChemDual框架在药物发现领域具有广泛的应用潜力，能够加速化学反应和逆合成的预测过程，帮助研究人员更高效地设计新药物。其强大的性能和灵活性使其在制药行业和化学研究中具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Chemical reaction and retrosynthesis prediction are fundamental tasks in drug discovery. Recently, large language models (LLMs) have shown potential in many domains. However, directly applying LLMs to these tasks faces two major challenges: (i) lacking a large-scale chemical synthesis-related instruction dataset; (ii) ignoring the close correlation between reaction and retrosynthesis prediction for the existing fine-tuning strategies. To address these challenges, we propose ChemDual, a novel LLM framework for accurate chemical synthesis. Specifically, considering the high cost of data acquisition for reaction and retrosynthesis, ChemDual regards the reaction-and-retrosynthesis of molecules as a related recombination-and-fragmentation process and constructs a large-scale of 4.4 million instruction dataset. Furthermore, ChemDual introduces an enhanced LLaMA, equipped with a multi-scale tokenizer and dual-task learning strategy, to jointly optimize the process of recombination and fragmentation as well as the tasks between reaction and retrosynthesis prediction. Extensive experiments on Mol-Instruction and USPTO-50K datasets demonstrate that ChemDual achieves state-of-the-art performance in both predictions of reaction and retrosynthesis, outperforming the existing conventional single-task approaches and the general open-source LLMs. Through molecular docking analysis, ChemDual generates compounds with diverse and strong protein binding affinity, further highlighting its strong potential in drug design.

