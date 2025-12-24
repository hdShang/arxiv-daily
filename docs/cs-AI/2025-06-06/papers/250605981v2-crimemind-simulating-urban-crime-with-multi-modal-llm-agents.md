---
layout: default
title: "CrimeMind: Simulating Urban Crime with Multi-Modal LLM Agents"
---

# CrimeMind: Simulating Urban Crime with Multi-Modal LLM Agents

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05981" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05981v2</a>
  <a href="https://arxiv.org/pdf/2506.05981.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05981v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05981v2', 'CrimeMind: Simulating Urban Crime with Multi-Modal LLM Agents')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qingbin Zeng, Ruotong Zhao, Jinzhu Mao, Haoyang Li, Fengli Xu, Yong Li

**分类**: cs.AI

**发布日期**: 2025-06-06 (更新: 2025-06-10)

**备注**: Typos corrected

---

## 💡 一句话要点

**提出CrimeMind以解决城市犯罪模拟问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `城市犯罪模拟` `多模态学习` `常规活动理论` `大型语言模型` `代理建模` `犯罪热点预测` `反事实模拟`

## 📋 核心要点

1. 现有的城市犯罪建模方法在可解释性和预测准确性之间存在权衡，且缺乏对环境变化的适应能力。
2. CrimeMind通过结合大型语言模型与常规活动理论，提供了一种新的城市犯罪模拟框架，能够处理多模态信息。
3. 在四个主要美国城市的实验中，CrimeMind在犯罪热点预测上表现优异，提升幅度达到24%。

## 📝 摘要（中文）

城市犯罪建模是一项重要且具有挑战性的任务，需要理解城市环境中潜在的视觉、社会和文化线索。以往的研究主要集中在基于规则的代理建模和深度学习方法上，前者在可解释性方面表现良好，但预测准确性有限；后者则在预测上有效，但缺乏可解释性且需要大量训练数据。为了解决这些问题，本文提出了CrimeMind，一个基于大型语言模型的代理建模框架，能够在多模态城市背景下模拟城市犯罪。该框架的关键创新在于将常规活动理论（RAT）整合到代理工作流中，使其能够处理丰富的多模态城市特征并推理犯罪行为。实验结果表明，CrimeMind在犯罪热点预测和空间分布准确性方面优于传统的代理模型和深度学习基线，最高提升达24%。

## 🔬 方法详解

**问题定义**：论文旨在解决城市犯罪模拟中的可解释性与预测准确性之间的矛盾。现有的基于规则的代理建模方法虽然可解释，但预测能力不足，而深度学习方法则缺乏可解释性且对数据需求高。

**核心思路**：CrimeMind框架结合了大型语言模型的强大能力与常规活动理论，能够在多模态城市环境中进行犯罪行为的推理和模拟。这样的设计使得模型不仅具备较强的预测能力，还能理解复杂的社会和文化线索。

**技术框架**：CrimeMind的整体架构包括数据收集、特征提取、模型训练和模拟推理几个主要模块。通过对多模态数据的处理，模型能够在不同城市环境中进行有效的犯罪行为模拟。

**关键创新**：将常规活动理论整合进代理工作流是CrimeMind的核心创新，使其能够在评估环境安全时推理微妙的线索，这在现有方法中是未曾实现的。

**关键设计**：在模型设计中，采用了小规模的人类标注数据集，并通过无训练的文本梯度方法对CrimeMind的感知与人类判断进行对齐，确保模型的输出更符合实际情况。实验中还针对不同城市的特征进行了参数优化，以提升模型的适应性和准确性。

## 📊 实验亮点

实验结果显示，CrimeMind在犯罪热点预测和空间分布准确性方面显著优于传统的代理模型和深度学习基线，最高提升达24%。此外，模型能够成功捕捉外部事件和政策干预的反事实模拟，展示了其在实际应用中的有效性。

## 🎯 应用场景

CrimeMind的研究成果具有广泛的应用潜力，能够为城市规划、公共安全和犯罪预防策略提供科学依据。通过模拟不同政策干预的效果，决策者可以更有效地评估和调整城市管理策略，从而提高城市安全水平。未来，该框架还可以扩展到其他社会现象的模拟与分析中。

## 📄 摘要（原文）

> Modeling urban crime is an important yet challenging task that requires understanding the subtle visual, social, and cultural cues embedded in urban environments. Previous work has mainly focused on rule-based agent-based modeling (ABM) and deep learning methods. ABMs offer interpretability of internal mechanisms but exhibit limited predictive accuracy. In contrast, deep learning methods are often effective in prediction but are less interpretable and require extensive training data. Moreover, both lines of work lack the cognitive flexibility to adapt to changing environments. Leveraging the capabilities of large language models (LLMs), we propose CrimeMind, a novel LLM-driven ABM framework for simulating urban crime within a multi-modal urban context. A key innovation of our design is the integration of the Routine Activity Theory (RAT) into the agentic workflow of CrimeMind, enabling it to process rich multi-modal urban features and reason about criminal behavior. However, RAT requires LLM agents to infer subtle cues in evaluating environmental safety as part of assessing guardianship, which can be challenging for LLMs. To address this, we collect a small-scale human-annotated dataset and align CrimeMind's perception with human judgment via a training-free textual gradient method. Experiments across four major U.S. cities demonstrate that CrimeMind outperforms both traditional ABMs and deep learning baselines in crime hotspot prediction and spatial distribution accuracy, achieving up to a 24% improvement over the strongest baseline. Furthermore, we conduct counterfactual simulations of external incidents and policy interventions and it successfully captures the expected changes in crime patterns, demonstrating its ability to reflect counterfactual scenarios. Overall, CrimeMind enables fine-grained modeling of individual behaviors and facilitates evaluation of real-world interventions.

