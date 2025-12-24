---
layout: default
title: Scalable LLM Math Reasoning Acceleration with Low-rank Distillation
---

# Scalable LLM Math Reasoning Acceleration with Low-rank Distillation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.07861" class="toolbar-btn" target="_blank">📄 arXiv: 2505.07861v2</a>
  <a href="https://arxiv.org/pdf/2505.07861.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.07861v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.07861v2', 'Scalable LLM Math Reasoning Acceleration with Low-rank Distillation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Harry Dong, Bilge Acun, Beidi Chen, Yuejie Chi

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-05-08 (更新: 2025-09-30)

---

## 💡 一句话要点

**提出Caprese以解决大语言模型数学推理效率问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `数学推理` `蒸馏训练` `高效推理` `资源优化` `模型压缩` `前馈网络` `合成样本`

## 📋 核心要点

1. 现有高效推理方法在语言任务上表现良好，但在数学推理方面性能严重下降，导致计算资源浪费。
2. Caprese是一种资源高效的蒸馏方法，专注于恢复高效推理中丧失的数学能力，且不影响语言任务性能。
3. 实验结果表明，Caprese显著减少了活跃参数数量，并降低了推理延迟，同时提高了响应的简洁性。

## 📝 摘要（中文）

由于长时间的生成过程，大语言模型（LLM）的数学推理需要大量的计算资源和时间。尽管已有许多高效推理方法在语言任务上表现优异，但它们往往严重影响数学性能。本文提出了一种资源高效的蒸馏方法Caprese，旨在恢复在高效推理中丧失的数学能力，主要集中在前馈块上。通过不扰动原始权重，仅增加约1%的参数和20K个合成训练样本，我们能够恢复思考型LLM在高效推理中丧失的大部分数学能力，同时对指令型LLM的语言任务没有负面影响。此外，Caprese显著减少了活跃参数的数量（Gemma 2 9B和Llama 3.1 8B减少约20亿），并能无缝集成到现有模型层中，降低延迟（超过16%的时间到下一个token的减少），同时鼓励响应简洁（最多减少8.5%的token数量）。

## 🔬 方法详解

**问题定义**：本文旨在解决大语言模型在高效推理中数学推理能力的丧失问题。现有方法虽然在语言任务上表现优异，但在数学推理方面却显著下降，导致计算资源的浪费和效率低下。

**核心思路**：Caprese通过不扰动原始权重，利用少量额外参数和合成训练样本，恢复在高效推理中丧失的数学能力。该方法主要集中在前馈块的蒸馏上，以确保在保持语言任务性能的同时，提升数学推理能力。

**技术框架**：Caprese的整体架构包括参数蒸馏模块和合成样本生成模块。首先，通过合成样本训练蒸馏模型，然后将其集成到现有的前馈层中，以减少延迟和提高效率。

**关键创新**：Caprese的主要创新在于其资源高效的蒸馏策略，能够在不显著增加计算负担的情况下，恢复数学推理能力。这与传统方法的高计算需求形成鲜明对比。

**关键设计**：在设计中，Caprese仅增加约1%的参数，并使用20K个合成训练样本进行训练，确保了模型的高效性和实用性。

## 📊 实验亮点

实验结果显示，Caprese在Gemma 2 9B和Llama 3.1 8B模型中分别减少了约20亿的活跃参数，并实现了超过16%的时间到下一个token的减少，同时响应的token数量最多减少了8.5%。这些结果表明，Caprese在保持语言任务性能的同时，显著提升了数学推理能力。

## 🎯 应用场景

该研究的潜在应用场景包括教育、科学计算和金融分析等领域，能够为需要高效数学推理的任务提供支持。通过提升大语言模型在数学推理方面的能力，Caprese有望在实际应用中显著提高效率和准确性，推动智能助手和自动化系统的发展。

## 📄 摘要（原文）

> Due to long generations, large language model (LLM) math reasoning demands significant computational resources and time. While many existing efficient inference methods have been developed with excellent performance preservation on language tasks, they often severely degrade math performance. In this paper, we propose Caprese, a resource-efficient distillation method to recover lost capabilities from deploying efficient inference methods, focused primarily in feedforward blocks. With original weights unperturbed, roughly 1% of additional parameters, and only 20K synthetic training samples, we are able to recover much if not all of the math capabilities lost from efficient inference for thinking LLMs and without harm to language tasks for instruct LLMs. Moreover, Caprese slashes the number of active parameters (~2B cut for Gemma 2 9B and Llama 3.1 8B) and integrates cleanly into existing model layers to reduce latency (>16% time-to-next-token reduction) while encouraging response brevity (up to 8.5% fewer tokens).

