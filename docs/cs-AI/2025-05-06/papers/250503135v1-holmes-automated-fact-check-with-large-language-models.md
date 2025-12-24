---
layout: default
title: Holmes: Automated Fact Check with Large Language Models
---

# Holmes: Automated Fact Check with Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.03135" class="toolbar-btn" target="_blank">📄 arXiv: 2505.03135v1</a>
  <a href="https://arxiv.org/pdf/2505.03135.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.03135v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.03135v1', 'Holmes: Automated Fact Check with Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haoran Ou, Gelei Deng, Xingshuo Han, Jie Zhang, Xinlei He, Han Qiu, Shangwei Guo, Tianwei Zhang

**分类**: cs.AI

**发布日期**: 2025-05-06

---

## 💡 一句话要点

**提出Holmes框架以解决多模态虚假信息检测问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `虚假信息检测` `大型语言模型` `证据检索` `多模态融合` `自动化验证`

## 📋 核心要点

1. 现有的虚假信息检测方法在处理复杂的多模态信息时表现不足，难以有效捕捉信息的真实性。
2. 论文提出Holmes框架，通过结合LLMs与新颖的证据检索方法，提升虚假信息检测的准确性。
3. Holmes在两个开源数据集上实现了88.3%的准确率，并在实时验证任务中达到了90.2%的准确率，提升幅度显著。

## 📝 摘要（中文）

随着互联网的普及，虚假信息的传播加速，威胁到社会信任、决策和国家安全。虚假信息已从简单文本演变为复杂的多模态形式，给现有检测方法带来了挑战。传统深度学习模型难以捕捉多模态虚假信息的复杂性。本研究探索利用大型语言模型（LLMs）进行自动化虚假信息检测。实证研究表明，LLMs单独无法可靠评估声明的真实性，但提供相关证据显著提高其性能。为此，我们提出Holmes，一个端到端框架，采用新颖的证据检索方法，帮助LLMs收集高质量证据。实验结果显示，Holmes在两个开源数据集上达到了88.3%的准确率，在实时验证任务中达到了90.2%的准确率，显著提升了事实核查的准确性。

## 🔬 方法详解

**问题定义**：本研究旨在解决多模态虚假信息检测中的证据检索不足问题。现有方法在面对复杂信息时，难以有效评估信息的真实性，导致检测效果不佳。

**核心思路**：Holmes框架的核心思路是结合大型语言模型（LLMs）与高效的证据检索机制，通过提供相关证据来提升虚假信息检测的准确性。该设计旨在弥补LLMs在证据搜索能力上的不足。

**技术框架**：Holmes框架包括两个主要模块：第一，LLM驱动的摘要模块，从开放源中提取关键信息；第二，新的算法和指标用于评估证据质量。整体流程为：输入声明，检索相关证据，评估证据质量，最终生成验证结果。

**关键创新**：Holmes的关键创新在于其证据检索方法，通过LLM的能力来提取和总结信息，同时引入新的评估标准来确保证据的高质量。这与传统方法的单一信息处理方式形成了鲜明对比。

**关键设计**：在设计上，Holmes采用了特定的参数设置以优化LLM的摘要能力，并引入了新的损失函数来提升证据评估的准确性。网络结构方面，Holmes集成了多种信息处理模块，以确保信息的全面性和准确性。

## 📊 实验亮点

Holmes在两个开源数据集上达到了88.3%的准确率，并在实时验证任务中实现了90.2%的准确率。通过改进的证据检索方法，Holmes的事实核查准确性比现有方法提升了30.8%，显示出显著的性能优势。

## 🎯 应用场景

Holmes框架具有广泛的应用潜力，尤其在新闻媒体、社交网络和信息验证平台等领域。其能够有效提升虚假信息检测的准确性，帮助用户更好地判断信息的真实性，进而增强社会对信息的信任度。未来，该框架还可以扩展到其他领域，如法律文书审核和学术研究中的信息验证。

## 📄 摘要（原文）

> The rise of Internet connectivity has accelerated the spread of disinformation, threatening societal trust, decision-making, and national security. Disinformation has evolved from simple text to complex multimodal forms combining images and text, challenging existing detection methods. Traditional deep learning models struggle to capture the complexity of multimodal disinformation. Inspired by advances in AI, this study explores using Large Language Models (LLMs) for automated disinformation detection. The empirical study shows that (1) LLMs alone cannot reliably assess the truthfulness of claims; (2) providing relevant evidence significantly improves their performance; (3) however, LLMs cannot autonomously search for accurate evidence. To address this, we propose Holmes, an end-to-end framework featuring a novel evidence retrieval method that assists LLMs in collecting high-quality evidence. Our approach uses (1) LLM-powered summarization to extract key information from open sources and (2) a new algorithm and metrics to evaluate evidence quality. Holmes enables LLMs to verify claims and generate justifications effectively. Experiments show Holmes achieves 88.3% accuracy on two open-source datasets and 90.2% in real-time verification tasks. Notably, our improved evidence retrieval boosts fact-checking accuracy by 30.8% over existing methods

