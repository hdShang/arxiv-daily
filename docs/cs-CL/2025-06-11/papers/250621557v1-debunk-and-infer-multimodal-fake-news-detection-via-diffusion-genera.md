---
layout: default
title: "Debunk and Infer: Multimodal Fake News Detection via Diffusion-Generated Evidence and LLM Reasoning"
---

# Debunk and Infer: Multimodal Fake News Detection via Diffusion-Generated Evidence and LLM Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.21557" class="toolbar-btn" target="_blank">📄 arXiv: 2506.21557v1</a>
  <a href="https://arxiv.org/pdf/2506.21557.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.21557v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.21557v1', 'Debunk and Infer: Multimodal Fake News Detection via Diffusion-Generated Evidence and LLM Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kaiying Yan, Moyang Liu, Yukun Liu, Ruibo Fu, Zhengqi Wen, Jianhua Tao, Xuefei Liu

**分类**: cs.CL

**发布日期**: 2025-06-11

---

## 💡 一句话要点

**提出Debunk-and-Infer框架以解决假新闻检测问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `假新闻检测` `多模态学习` `辟谣扩散` `大语言模型` `信息可信度` `逻辑推理` `生成模型`

## 📋 核心要点

1. 假新闻的快速传播使得现有检测方法面临信息可信度不足和解释性差的挑战。
2. 本文提出的DIFND框架通过结合条件扩散模型和多模态大语言模型，利用辟谣知识增强检测性能。
3. 在FakeSV和FVC数据集上的实验结果表明，DIFND显著提高了检测准确性，超越了现有方法。

## 📝 摘要（中文）

假新闻在多媒体平台的快速传播对信息可信度构成了严重挑战。本文提出了一种假新闻检测的Debunk-and-Infer框架（DIFND），利用辟谣知识提升假新闻检测的性能和可解释性。DIFND结合了条件扩散模型的生成能力与多模态大语言模型（MLLM）的协同推理能力，采用辟谣扩散生成基于新闻视频多模态内容的反驳或验证证据，丰富评估过程。通过链式辟谣策略，MLLM系统生成逻辑基础的多模态推理内容和最终的真实性判断。DIFND在联合建模多模态特征、生成辟谣线索和推理丰富的验证方面取得了显著的检测准确性提升。大量实验表明，DIFND不仅优于现有方法，还能提供可信的决策。

## 🔬 方法详解

**问题定义**：本文旨在解决假新闻检测中的信息可信度不足和可解释性差的问题。现有方法往往无法有效利用多模态信息，导致检测效果不佳。

**核心思路**：DIFND框架通过结合辟谣知识与生成模型，生成多模态证据以增强假新闻检测的准确性和可解释性。采用链式辟谣策略，利用多代理MLLM系统进行逻辑推理和真实性判断。

**技术框架**：DIFND的整体架构包括三个主要模块：辟谣扩散生成模块、MLLM推理模块和最终的真实性判断模块。辟谣扩散模块生成与新闻视频内容相关的证据，MLLM模块进行逻辑推理，最后综合判断新闻的真实性。

**关键创新**：DIFND的核心创新在于将辟谣扩散与多模态推理相结合，形成一个统一的检测框架。这种方法在生成证据和推理过程中引入了多模态特征，显著提升了检测的准确性和可解释性。

**关键设计**：在技术细节上，DIFND采用了特定的损失函数来优化生成模型的输出，并设计了多代理系统以增强推理能力。网络结构上，结合了多模态输入和生成模型的输出，确保了信息的有效融合。

## 📊 实验亮点

在FakeSV和FVC数据集上的实验结果显示，DIFND在假新闻检测任务中相较于现有方法提高了检测准确性，具体提升幅度达到XX%（具体数据未知），并且在可信决策方面表现出色，验证了其有效性和可靠性。

## 🎯 应用场景

该研究的潜在应用领域包括社交媒体平台、新闻机构和信息验证服务等，能够有效提升假新闻检测的准确性和可信度。未来，DIFND框架有望在更广泛的多模态信息处理任务中发挥重要作用，推动信息安全和可信传播的发展。

## 📄 摘要（原文）

> The rapid spread of fake news across multimedia platforms presents serious challenges to information credibility. In this paper, we propose a Debunk-and-Infer framework for Fake News Detection(DIFND) that leverages debunking knowledge to enhance both the performance and interpretability of fake news detection. DIFND integrates the generative strength of conditional diffusion models with the collaborative reasoning capabilities of multimodal large language models (MLLMs). Specifically, debunk diffusion is employed to generate refuting or authenticating evidence based on the multimodal content of news videos, enriching the evaluation process with diverse yet semantically aligned synthetic samples. To improve inference, we propose a chain-of-debunk strategy where a multi-agent MLLM system produces logic-grounded, multimodal-aware reasoning content and final veracity judgment. By jointly modeling multimodal features, generative debunking cues, and reasoning-rich verification within a unified architecture, DIFND achieves notable improvements in detection accuracy. Extensive experiments on the FakeSV and FVC datasets show that DIFND not only outperforms existing approaches but also delivers trustworthy decisions.

