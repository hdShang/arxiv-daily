---
layout: default
title: "SEVADE: Self-Evolving Multi-Agent Analysis with Decoupled Evaluation for Hallucination-Resistant Irony Detection"
---

# SEVADE: Self-Evolving Multi-Agent Analysis with Decoupled Evaluation for Hallucination-Resistant Irony Detection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.06803" class="toolbar-btn" target="_blank">📄 arXiv: 2508.06803v1</a>
  <a href="https://arxiv.org/pdf/2508.06803.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.06803v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.06803v1', 'SEVADE: Self-Evolving Multi-Agent Analysis with Decoupled Evaluation for Hallucination-Resistant Irony Detection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ziqi Liu, Yangbin Chen, Ziyang Zhou, Yilin Li, Mingxuan Hu, Yushan Pan, Zhijie Xu

**分类**: cs.CL, cs.MA

**发布日期**: 2025-08-09

---

## 💡 一句话要点

**提出SEVADE以解决讽刺检测中的幻觉问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `讽刺检测` `自然语言处理` `多代理系统` `动态推理` `抗幻觉机制`

## 📋 核心要点

1. 现有讽刺检测方法在处理复杂修辞时，常受到单一视角和静态推理的限制，导致准确性不足。
2. 本文提出的SEVADE框架通过动态代理推理引擎（DARE）和解耦评估机制，提升了讽刺检测的准确性和鲁棒性。
3. 在四个基准数据集上的实验表明，SEVADE框架在准确率和宏观F1分数上均有显著提升，表现优于现有方法。

## 📝 摘要（中文）

讽刺检测是自然语言处理中的一项重要而具有挑战性的任务。现有的大型语言模型方法常常受到单一视角分析、静态推理路径以及在处理复杂讽刺修辞时易受幻觉影响的限制，影响其准确性和可靠性。为了解决这些挑战，本文提出了SEVADE，一个新颖的自我演化多代理分析框架，结合解耦评估以实现抗幻觉的讽刺检测。该框架的核心是动态代理推理引擎（DARE），利用一组基于语言理论的专业代理对文本进行多方面的解构，并生成结构化的推理链。随后，一个独立的轻量级推理裁决者（RA）仅基于该推理链进行最终分类。实验结果表明，该框架在四个基准数据集上实现了最先进的性能，准确率平均提高了6.75%，宏观F1分数提高了6.29%。

## 🔬 方法详解

**问题定义**：本文旨在解决现有讽刺检测方法在处理复杂修辞时的局限性，尤其是单一视角分析和静态推理路径导致的准确性不足以及幻觉现象。

**核心思路**：SEVADE框架通过引入动态代理推理引擎（DARE）和解耦评估机制，旨在提升讽刺检测的准确性和抗幻觉能力。通过多代理协作，进行文本的多维解构，生成结构化推理链，从而增强推理的深度和广度。

**技术框架**：该框架主要包括两个模块：动态代理推理引擎（DARE）和轻量级推理裁决者（RA）。DARE负责文本的多方面解构和推理链生成，而RA则基于推理链进行最终分类，确保推理过程与判断过程的解耦。

**关键创新**：SEVADE的主要创新在于其解耦的架构设计，通过将复杂推理与最终判断分开，显著降低了幻觉现象的风险。这一设计与现有方法的集成推理方式形成鲜明对比。

**关键设计**：在技术细节上，DARE模块采用了多代理协作机制，结合语言理论进行推理；RA模块则设计为轻量级，以提高分类效率。损失函数的设计也经过优化，以适应解耦架构的需求。

## 📊 实验亮点

实验结果显示，SEVADE框架在四个基准数据集上实现了最先进的性能，准确率平均提高了6.75%，宏观F1分数提高了6.29%。这些结果表明，SEVADE在讽刺检测任务中具有显著的优势，超越了现有的主流方法。

## 🎯 应用场景

该研究的潜在应用领域包括社交媒体内容分析、在线评论监测以及情感分析等。通过提高讽刺检测的准确性，SEVADE能够帮助企业和研究机构更好地理解用户情感和社交动态，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Sarcasm detection is a crucial yet challenging Natural Language Processing task. Existing Large Language Model methods are often limited by single-perspective analysis, static reasoning pathways, and a susceptibility to hallucination when processing complex ironic rhetoric, which impacts their accuracy and reliability. To address these challenges, we propose **SEVADE**, a novel **S**elf-**Ev**olving multi-agent **A**nalysis framework with **D**ecoupled **E**valuation for hallucination-resistant sarcasm detection. The core of our framework is a Dynamic Agentive Reasoning Engine (DARE), which utilizes a team of specialized agents grounded in linguistic theory to perform a multifaceted deconstruction of the text and generate a structured reasoning chain. Subsequently, a separate lightweight rationale adjudicator (RA) performs the final classification based solely on this reasoning chain. This decoupled architecture is designed to mitigate the risk of hallucination by separating complex reasoning from the final judgment. Extensive experiments on four benchmark datasets demonstrate that our framework achieves state-of-the-art performance, with average improvements of **6.75%** in Accuracy and **6.29%** in Macro-F1 score.

