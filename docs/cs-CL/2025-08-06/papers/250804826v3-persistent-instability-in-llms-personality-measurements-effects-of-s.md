---
layout: default
title: "Persistent Instability in LLM's Personality Measurements: Effects of Scale, Reasoning, and Conversation History"
---

# Persistent Instability in LLM's Personality Measurements: Effects of Scale, Reasoning, and Conversation History

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.04826" class="toolbar-btn" target="_blank">📄 arXiv: 2508.04826v3</a>
  <a href="https://arxiv.org/pdf/2508.04826.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.04826v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.04826v3', 'Persistent Instability in LLM\'s Personality Measurements: Effects of Scale, Reasoning, and Conversation History')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tommaso Tosato, Saskia Helbling, Yorguin-Jose Mantilla-Ramos, Mahmood Hegazy, Alberto Tosato, David John Lemay, Irina Rish, Guillaume Dumas

**分类**: cs.CL, cs.AI

**发布日期**: 2025-08-06 (更新: 2025-12-23)

**备注**: Accepted at AAAI 2026, Track on AI Alignment

---

## 💡 一句话要点

**提出PERSIST框架以评估LLM个性测量的不稳定性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `个性测量` `评估框架` `行为一致性` `推理模式` `对话历史` `生态有效性`

## 📋 核心要点

1. 现有大型语言模型在个性测量中表现出显著的不稳定性，影响其在安全关键应用中的可靠性。
2. 本文提出PERSIST框架，通过系统评估不同模型和问卷，探讨个性测量的稳定性及其影响因素。
3. 实验结果表明，问题顺序和模型规模对个性测量的影响显著，且推理和对话历史的干预可能导致更大的变异性。

## 📝 摘要（中文）

大型语言模型（LLM）在安全部署中需要一致的行为模式，但存在显著的个性特征表达不稳定性。本文提出了PERSIST（合成文本中的个性稳定性）评估框架，测试了25个开源模型（参数从1B到685B）在超过200万条响应中的表现。通过传统（BFI、SD3）和新型LLM适应的个性问卷，系统地变化模型规模、角色、推理模式、问题顺序或改述及对话历史。研究发现，问题重排可显著改变个性测量，模型规模对稳定性的提升有限，推理和对话历史的干预反而可能增加变异性，详细的角色指令效果不一，LLM适应的问卷尽管生态有效性提高，但不稳定性与人类版本相当。这些发现表明当前LLM缺乏真正行为一致性的架构基础，可能不适用于需要可预测行为的安全关键应用。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在个性测量中的不稳定性问题，现有方法未能有效保证个性特征的一致性，影响其在实际应用中的可用性。

**核心思路**：通过引入PERSIST评估框架，系统地测试不同规模和配置的模型在多种问卷下的表现，分析影响个性测量稳定性的因素。

**技术框架**：整体架构包括数据收集、模型选择、个性问卷设计、实验实施和结果分析五个主要模块。数据收集涵盖了超过200万条响应，模型选择涵盖了25个开源模型，问卷设计包括传统和LLM适应的版本。

**关键创新**：最重要的创新在于系统性地评估了不同因素（如模型规模、问题顺序、推理模式等）对个性测量的影响，挑战了现有关于个性一致性的假设。

**关键设计**：在实验中，采用了多种个性问卷（如BFI、SD3）并进行了参数设置，确保了问卷的生态有效性，同时对模型的推理模式和对话历史进行了详细的控制和分析。

## 📊 实验亮点

实验结果显示，问题重排可导致个性测量的显著变化，且即使是400B以上的模型在5点量表上的标准差仍超过0.3。此外，推理和对话历史的干预反而增加了个性测量的变异性，这一发现对现有的模型对齐策略提出了挑战。

## 🎯 应用场景

该研究的潜在应用领域包括人机交互、情感计算和个性化推荐系统。通过提高大型语言模型在个性测量中的稳定性，可以增强其在安全关键应用中的可靠性，推动智能助手和社交机器人等技术的进步。

## 📄 摘要（原文）

> Large language models require consistent behavioral patterns for safe deployment, yet there are indications of large variability that may lead to an instable expression of personality traits in these models. We present PERSIST (PERsonality Stability in Synthetic Text), a comprehensive evaluation framework testing 25 open-source models (1B-685B parameters) across 2 million+ responses. Using traditional (BFI, SD3) and novel LLM-adapted personality questionnaires, we systematically vary model size, personas, reasoning modes, question order or paraphrasing, and conversation history. Our findings challenge fundamental assumptions: (1) Question reordering alone can introduce large shifts in personality measurements; (2) Scaling provides limited stability gains: even 400B+ models exhibit standard deviations >0.3 on 5-point scales; (3) Interventions expected to stabilize behavior, such as reasoning and inclusion of conversation history, can paradoxically increase variability; (4) Detailed persona instructions produce mixed effects, with misaligned personas showing significantly higher variability than the helpful assistant baseline; (5) The LLM-adapted questionnaires, despite their improved ecological validity, exhibit instability comparable to human-centric versions. This persistent instability across scales and mitigation strategies suggests that current LLMs lack the architectural foundations for genuine behavioral consistency. For safety-critical applications requiring predictable behavior, these findings indicate that current alignment strategies may be inadequate.

