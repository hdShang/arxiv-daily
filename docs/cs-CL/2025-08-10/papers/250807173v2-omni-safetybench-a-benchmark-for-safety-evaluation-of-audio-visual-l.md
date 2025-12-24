---
layout: default
title: "Omni-SafetyBench: A Benchmark for Safety Evaluation of Audio-Visual Large Language Models"
---

# Omni-SafetyBench: A Benchmark for Safety Evaluation of Audio-Visual Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.07173" class="toolbar-btn" target="_blank">📄 arXiv: 2508.07173v2</a>
  <a href="https://arxiv.org/pdf/2508.07173.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.07173v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.07173v2', 'Omni-SafetyBench: A Benchmark for Safety Evaluation of Audio-Visual Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Leyi Pan, Zheyu Fu, Yunpeng Zhai, Shuchang Tao, Sheng Guan, Shiyu Huang, Lingzhe Zhang, Zhaoyang Liu, Bolin Ding, Felix Henry, Aiwei Liu, Lijie Wen

**分类**: cs.CL

**发布日期**: 2025-08-10 (更新: 2025-09-28)

**备注**: 22 pages, 10 figures, 12 tables

---

## 💡 一句话要点

**提出Omni-SafetyBench以解决音视频大语言模型安全评估问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `全模态大语言模型` `安全评估` `音视频处理` `跨模态一致性` `基准测试`

## 📋 核心要点

1. 现有方法缺乏针对OLLMs的专门基准，无法有效评估音视频联合输入的安全性和跨模态一致性。
2. 提出Omni-SafetyBench基准，包含24种模态变体和972个样本，设计了安全评分和跨模态一致性评分以评估模型安全性。
3. 评估结果显示，只有3个模型在安全评分和CMSC-score上超过0.6，复杂输入下安全防御显著减弱，部分模型在特定模态上得分低至0.14。

## 📝 摘要（中文）

随着全模态大语言模型（OLLMs）的兴起，集成视觉和听觉处理的能力，迫切需要强有力的安全评估来减轻有害输出。然而，目前尚无专门针对OLLMs的基准，现有基准无法评估联合音视频输入或跨模态一致性。为填补这一空白，我们提出了Omni-SafetyBench，这是第一个全面的OLLM安全评估基准，包含24种模态变体，每种变体有972个样本，包括音视频危害案例。我们提出了定制的评估指标：基于条件攻击成功率（C-ASR）和拒绝率（C-RR）的安全评分，以及跨模态安全一致性评分（CMSC-score），以评估模态间的一致性。对6个开源和4个闭源的OLLM进行评估，发现了关键的脆弱性，强调了增强OLLM安全性的紧迫需求。

## 🔬 方法详解

**问题定义**：本论文旨在解决当前缺乏针对全模态大语言模型（OLLMs）安全评估的专门基准的问题。现有方法无法有效评估音视频联合输入的安全性和跨模态一致性，导致模型在复杂输入下的脆弱性未被充分识别。

**核心思路**：我们提出Omni-SafetyBench，作为第一个全面的OLLM安全评估基准，设计了针对复杂模态输入的定制评估指标，以全面评估模型的安全性和一致性。

**技术框架**：Omni-SafetyBench包含24种模态变体，每种变体有972个样本，涵盖音视频危害案例。评估过程中使用了安全评分（基于C-ASR和C-RR）和CMSC-score来衡量模型在不同模态间的一致性。

**关键创新**：本研究的关键创新在于提出了针对OLLMs的专门安全评估基准和定制评估指标，填补了现有方法在音视频联合输入安全性评估方面的空白。

**关键设计**：在评估过程中，我们设置了多种模态组合，设计了安全评分和CMSC-score，以便更好地反映模型在复杂输入下的表现和一致性。

## 📊 实验亮点

实验结果表明，只有3个模型在安全评分和CMSC-score上超过0.6，显示出在复杂音视频输入下，现有模型的安全防御能力显著减弱，部分模型在特定模态上得分低至0.14，揭示了当前OLLMs的安全性亟待提升。

## 🎯 应用场景

该研究的潜在应用领域包括自动内容生成、智能助手和多模态交互系统等。通过提升OLLMs的安全性，可以有效减少有害输出，增强用户信任，推动相关技术的广泛应用与发展。

## 📄 摘要（原文）

> The rise of Omni-modal Large Language Models (OLLMs), which integrate visual and auditory processing with text, necessitates robust safety evaluations to mitigate harmful outputs. However, no dedicated benchmarks currently exist for OLLMs, and existing benchmarks fail to assess safety under joint audio-visual inputs or cross-modal consistency. To fill this gap, we introduce Omni-SafetyBench, the first comprehensive parallel benchmark for OLLM safety evaluation, featuring 24 modality variations with 972 samples each, including audio-visual harm cases. Considering OLLMs' comprehension challenges with complex omni-modal inputs and the need for cross-modal consistency evaluation, we propose tailored metrics: a Safety-score based on Conditional Attack Success Rate (C-ASR) and Refusal Rate (C-RR) to account for comprehension failures, and a Cross-Modal Safety Consistency score (CMSC-score) to measure consistency across modalities. Evaluating 6 open-source and 4 closed-source OLLMs reveals critical vulnerabilities: (1) only 3 models achieving over 0.6 in both average Safety-score and CMSC-score; (2) safety defenses weaken with complex inputs, especially audio-visual joints; (3) severe weaknesses persist, with some models scoring as low as 0.14 on specific modalities. Using Omni-SafetyBench, we evaluated existing safety alignment algorithms and identified key challenges in OLLM safety alignment: (1) Inference-time methods are inherently less effective as they cannot alter the model's underlying understanding of safety; (2) Post-training methods struggle with out-of-distribution issues due to the vast modality combinations in OLLMs; and, safety tasks involving audio-visual inputs are more complex, making even in-distribution training data less effective. Our proposed benchmark, metrics and the findings highlight urgent needs for enhanced OLLM safety.

