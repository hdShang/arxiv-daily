---
layout: default
title: "Iti-Validator: A Guardrail Framework for Validating and Correcting LLM-Generated Itineraries"
---

# Iti-Validator: A Guardrail Framework for Validating and Correcting LLM-Generated Itineraries

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.24719" class="toolbar-btn" target="_blank">📄 arXiv: 2510.24719v1</a>
  <a href="https://arxiv.org/pdf/2510.24719.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.24719v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.24719v1', 'Iti-Validator: A Guardrail Framework for Validating and Correcting LLM-Generated Itineraries')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shravan Gadbail, Masumi Desai, Kamalakar Karlapalem

**分类**: cs.CL, cs.IR

**发布日期**: 2025-09-04

---

## 💡 一句话要点

**Iti-Validator：用于验证和修正LLM生成行程的保障框架**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `旅行行程规划` `时间一致性验证` `行程修正` `AeroDataBox API`

## 📋 核心要点

1. 现有LLM在生成旅行行程时，经常出现时间和空间上的不一致性，尤其是在考虑实际旅行约束时，缺乏有效验证和纠正机制。
2. 论文提出Iti-Validator框架，利用AeroDataBox API验证LLM生成的行程，并纠正时间上的不一致性，确保行程的合理性和可行性。
3. 实验表明，该框架能够系统且可靠地纠正LLM生成的行程中的时间错误，使其更适用于实际的大规模旅行规划应用。

## 📝 摘要（中文）

大型语言模型（LLM）的快速发展使其能够生成复杂的多步骤计划和行程。然而，这些生成的计划通常缺乏时间和空间上的一致性，尤其是在涉及物理旅行约束的场景中。本研究旨在研究不同LLM的时间性能，并提出了一个验证框架，用于评估和改进LLM生成的旅行行程的时间一致性。该系统采用多个最先进的LLM来生成旅行计划，并使用AeroDataBox API根据实际飞行时长约束对其进行验证。这项工作有助于理解LLM在处理像行程生成这样复杂的时序推理任务方面的能力，并提供了一个框架来纠正LLM生成的行程中的任何时间不一致性，例如重叠的旅程或不切实际的 transit 时间，然后再将行程提供给用户。我们的实验表明，虽然当前的LLM经常产生时间上不一致的行程，但可以使用我们的框架系统地、可靠地纠正这些行程，从而使其能够实际部署在大型旅行计划中。

## 🔬 方法详解

**问题定义**：现有的大型语言模型在生成旅行行程时，经常会产生时间不一致的问题，例如行程中出现时间重叠的航班，或者 transit 时间不合理的情况。这些问题使得LLM生成的行程在实际应用中不可靠，需要人工进行大量的修正。现有的方法缺乏有效的验证和纠正机制，无法保证生成行程的时间合理性。

**核心思路**：论文的核心思路是构建一个验证框架，利用外部API（AeroDataBox API）获取真实的航班信息和旅行时间，然后对LLM生成的行程进行验证，找出时间不一致的地方，并进行修正。通过这种方式，可以有效地提高LLM生成行程的时间合理性，使其更适用于实际应用。

**技术框架**：Iti-Validator框架主要包含以下几个模块：1) LLM行程生成模块：使用多个LLM生成不同的旅行行程。2) 行程验证模块：利用AeroDataBox API获取真实的航班信息和旅行时间，然后对LLM生成的行程进行验证，找出时间不一致的地方。3) 行程修正模块：根据验证结果，对行程进行修正，例如调整航班时间，或者修改 transit 时间。4) 输出模块：将修正后的行程输出给用户。

**关键创新**：该论文的关键创新在于提出了一个基于外部API的行程验证和纠正框架。与以往的研究不同，该框架不是仅仅依赖LLM自身的能力来生成行程，而是利用外部的真实数据来验证和纠正LLM生成的行程，从而有效地提高了行程的可靠性。

**关键设计**：在行程验证模块中，论文使用了AeroDataBox API来获取真实的航班信息和旅行时间。在行程修正模块中，论文设计了一系列的规则来修正时间不一致的地方，例如，如果两个航班的时间重叠，则将后一个航班的时间推迟。具体的参数设置和损失函数未知。

## 📊 实验亮点

实验结果表明，当前的LLM经常产生时间上不一致的行程，但使用Iti-Validator框架可以系统地、可靠地纠正这些行程。具体性能数据和对比基线未知，但该框架能够显著提高LLM生成行程的时间合理性，使其更适用于实际的大规模旅行规划应用。

## 🎯 应用场景

该研究成果可应用于智能旅行规划助手、在线旅行社（OTA）平台等领域，帮助用户快速生成可靠的旅行行程。通过自动验证和纠正LLM生成的行程，可以减少人工干预，提高旅行规划的效率和用户满意度。未来，该框架可以扩展到支持更多的旅行约束，例如预算、偏好等，从而提供更个性化的旅行规划服务。

## 📄 摘要（原文）

> The rapid advancement of Large Language Models (LLMs) has enabled them to generate complex, multi-step plans and itineraries. However, these generated plans often lack temporal and spatial consistency, particularly in scenarios involving physical travel constraints. This research aims to study the temporal performance of different LLMs and presents a validation framework that evaluates and improves the temporal consistency of LLM-generated travel itineraries. The system employs multiple state-of-the-art LLMs to generate travel plans and validates them against real-world flight duration constraints using the AeroDataBox API. This work contributes to the understanding of LLM capabilities in handling complex temporal reasoning tasks like itinerary generation and provides a framework to rectify any temporal inconsistencies like overlapping journeys or unrealistic transit times in the itineraries generated by LLMs before the itinerary is given to the user. Our experiments reveal that while current LLMs frequently produce temporally inconsistent itineraries, these can be systematically and reliably corrected using our framework, enabling their practical deployment in large-scale travel planning.

