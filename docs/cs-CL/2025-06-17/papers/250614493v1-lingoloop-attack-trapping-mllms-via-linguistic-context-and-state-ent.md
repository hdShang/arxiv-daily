---
layout: default
title: "LingoLoop Attack: Trapping MLLMs via Linguistic Context and State Entrapment into Endless Loops"
---

# LingoLoop Attack: Trapping MLLMs via Linguistic Context and State Entrapment into Endless Loops

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.14493" class="toolbar-btn" target="_blank">📄 arXiv: 2506.14493v1</a>
  <a href="https://arxiv.org/pdf/2506.14493.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.14493v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.14493v1', 'LingoLoop Attack: Trapping MLLMs via Linguistic Context and State Entrapment into Endless Loops')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiyuan Fu, Kaixun Jiang, Lingyi Hong, Jinglun Li, Haijing Guo, Dingkang Yang, Zhaoyu Chen, Wenqiang Zhang

**分类**: cs.CL, cs.CR

**发布日期**: 2025-06-17

---

## 💡 一句话要点

**提出LingoLoop攻击以解决多模态大语言模型的资源耗尽问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `资源耗尽` `词性特征` `生成路径修剪` `安全性评估` `攻击方法`

## 📋 核心要点

1. 现有能量延迟攻击方法忽视了词性特征和句子结构对输出的影响，导致效果有限。
2. 提出LingoLoop攻击，通过词性感知延迟机制和生成路径修剪机制，诱导模型生成冗长的输出。
3. 实验结果表明，LingoLoop可以使生成的token数量增加至原来的30倍，能量消耗也相应增加。

## 📝 摘要（中文）

多模态大语言模型（MLLMs）在推理过程中表现出色，但在计算资源上需求巨大。攻击者可以通过诱导过量输出，导致资源耗尽和服务降级。现有的能量延迟攻击方法未能充分考虑词性特征对EOS生成的影响及句子结构模式对输出数量的影响。为此，本文提出LingoLoop攻击，旨在诱导MLLMs生成冗长且重复的序列。通过引入词性感知延迟机制和生成路径修剪机制，LingoLoop显著提高了生成的token数量和能量消耗，揭示了MLLMs的重大脆弱性。

## 🔬 方法详解

**问题定义**：本文旨在解决多模态大语言模型在推理时的资源耗尽问题。现有方法未能充分利用词性特征和句子结构，导致攻击效果不佳。

**核心思路**：LingoLoop攻击通过调整词性信息引导注意力权重，延迟EOS token的生成，同时限制输出多样性以诱导重复循环，从而实现资源耗尽。

**技术框架**：整体架构包括两个主要模块：词性感知延迟机制和生成路径修剪机制。前者通过调整注意力权重来控制EOS生成，后者则通过限制隐藏状态的幅度来鼓励模型生成重复序列。

**关键创新**：LingoLoop的核心创新在于结合了词性特征与生成路径修剪，显著提升了攻击效果，与传统方法相比，能够更有效地诱导模型生成冗长输出。

**关键设计**：在设计中，调整了注意力权重的计算方式，以便更好地利用词性信息，同时在生成路径修剪中引入了对隐藏状态幅度的限制，确保模型输出的持续性和重复性。

## 📊 实验亮点

实验结果显示，LingoLoop攻击能够将生成的token数量提高至原来的30倍，能量消耗也相应增加，充分展示了该攻击方法在诱导模型生成冗长输出方面的有效性。这一发现揭示了多模态大语言模型在实际部署中的重大安全隐患。

## 🎯 应用场景

该研究的潜在应用领域包括对多模态大语言模型的安全性评估和防护措施的设计。通过揭示模型的脆弱性，可以为未来的模型优化和安全防护提供重要参考，确保其在实际应用中的可靠性。

## 📄 摘要（原文）

> Multimodal Large Language Models (MLLMs) have shown great promise but require substantial computational resources during inference. Attackers can exploit this by inducing excessive output, leading to resource exhaustion and service degradation. Prior energy-latency attacks aim to increase generation time by broadly shifting the output token distribution away from the EOS token, but they neglect the influence of token-level Part-of-Speech (POS) characteristics on EOS and sentence-level structural patterns on output counts, limiting their efficacy. To address this, we propose LingoLoop, an attack designed to induce MLLMs to generate excessively verbose and repetitive sequences. First, we find that the POS tag of a token strongly affects the likelihood of generating an EOS token. Based on this insight, we propose a POS-Aware Delay Mechanism to postpone EOS token generation by adjusting attention weights guided by POS information. Second, we identify that constraining output diversity to induce repetitive loops is effective for sustained generation. We introduce a Generative Path Pruning Mechanism that limits the magnitude of hidden states, encouraging the model to produce persistent loops. Extensive experiments demonstrate LingoLoop can increase generated tokens by up to 30 times and energy consumption by a comparable factor on models like Qwen2.5-VL-3B, consistently driving MLLMs towards their maximum generation limits. These findings expose significant MLLMs' vulnerabilities, posing challenges for their reliable deployment. The code will be released publicly following the paper's acceptance.

