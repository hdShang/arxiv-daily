---
layout: default
title: "NEFMind: Parameter-Efficient Fine-Tuning of Open-Source LLMs for Telecom APIs Automation"
---

# NEFMind: Parameter-Efficient Fine-Tuning of Open-Source LLMs for Telecom APIs Automation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.09240" class="toolbar-btn" target="_blank">📄 arXiv: 2508.09240v1</a>
  <a href="https://arxiv.org/pdf/2508.09240.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.09240v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.09240v1', 'NEFMind: Parameter-Efficient Fine-Tuning of Open-Source LLMs for Telecom APIs Automation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zainab Khan, Ahmed Hussain, Mukesh Thakur, Arto Hellas, Panos Papadimitratos

**分类**: cs.NI, cs.AI, cs.CL

**发布日期**: 2025-08-12

**备注**: 6 pages

---

## 💡 一句话要点

**提出NEFMind以解决电信API自动化中的复杂性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `电信API` `自动化` `参数高效微调` `合成数据集` `量化低秩适应` `5G服务架构` `模型优化` `性能评估`

## 📋 核心要点

1. 现代电信中，服务架构导致网络功能和API数量激增，给服务发现和管理带来复杂性。
2. NEFMind框架通过合成数据集生成、量化低秩适应和性能评估，提供了一种高效的解决方案。
3. 实验结果表明，微调后的Phi-2模型在API调用识别上实现了98-100%的准确率，并显著降低了通信开销。

## 📝 摘要（中文）

现代电信中，基于服务的架构导致网络功能和应用程序接口的数量急剧增加，给服务发现和管理带来了显著的操作复杂性。本文介绍了NEFMind框架，利用开源大型语言模型的参数高效微调来应对这些挑战。该框架集成了三个核心组件：从网络暴露功能API规范生成合成数据集，通过量化低秩适应进行模型优化，以及通过GPT-4 Ref Score和BertScore指标进行性能评估。针对5G服务架构API，我们的方法在通信开销上实现了85%的减少。使用开源Phi-2模型的实验验证显示，API调用识别性能达到98-100%的准确率。微调后的Phi-2模型在保持计算效率的同时，其性能可与更大模型如GPT-4相媲美。这些发现验证了针对特定领域的参数高效LLM策略在下一代电信网络复杂API生态系统管理中的有效性。

## 🔬 方法详解

**问题定义**：本文旨在解决现代电信中由于服务架构导致的网络功能和API数量激增所带来的服务发现和管理复杂性。现有方法在处理这些复杂性时效率低下，难以满足快速发展的电信需求。

**核心思路**：NEFMind框架通过参数高效的微调技术，结合合成数据集生成和模型优化，旨在提高API管理的效率和准确性。该设计能够在保持计算资源节约的同时，提升模型性能。

**技术框架**：NEFMind框架主要包括三个模块：首先，从网络暴露功能API规范生成合成数据集；其次，利用量化低秩适应技术对模型进行优化；最后，通过GPT-4 Ref Score和BertScore进行性能评估。这一流程确保了从数据生成到模型优化的高效衔接。

**关键创新**：NEFMind的主要创新在于其参数高效的微调策略，使得开源大型语言模型在电信API管理中表现出色，且在计算效率上优于传统方法。与现有方法相比，该框架能够在较小的模型参数下实现高精度的API调用识别。

**关键设计**：在模型优化过程中，采用了量化低秩适应技术，确保了模型在微调时的高效性。此外，损失函数和评估指标的选择（如GPT-4 Ref Score和BertScore）也经过精心设计，以确保模型性能的可靠性和有效性。

## 📊 实验亮点

实验结果显示，NEFMind框架在API调用识别上达到了98-100%的准确率，相较于传统手动发现方法，通信开销减少了85%。微调后的Phi-2模型在性能上与更大模型如GPT-4相当，同时保持了较高的计算效率，展现出显著的优势。

## 🎯 应用场景

NEFMind框架在电信行业的潜在应用广泛，尤其是在5G网络的API管理和服务发现中。其高效的API调用识别能力能够显著降低运营成本，提高服务响应速度，推动电信基础设施的智能化和自动化发展。未来，该框架还可扩展至其他领域的API管理和服务自动化。

## 📄 摘要（原文）

> The use of Service-Based Architecture in modern telecommunications has exponentially increased Network Functions (NFs) and Application Programming Interfaces (APIs), creating substantial operational complexities in service discovery and management. We introduce \textit{NEFMind}, a framework leveraging parameter-efficient fine-tuning of open-source Large Language Models (LLMs) to address these challenges. It integrates three core components: synthetic dataset generation from Network Exposure Function (NEF) API specifications, model optimization through Quantized-Low-Rank Adaptation, and performance evaluation via GPT-4 Ref Score and BertScore metrics. Targeting 5G Service-Based Architecture APIs, our approach achieves 85% reduction in communication overhead compared to manual discovery methods. Experimental validation using the open-source Phi-2 model demonstrates exceptional API call identification performance at 98-100% accuracy. The fine-tuned Phi-2 model delivers performance comparable to significantly larger models like GPT-4 while maintaining computational efficiency for telecommunications infrastructure deployment. These findings validate domain-specific, parameter-efficient LLM strategies for managing complex API ecosystems in next-generation telecommunications networks.

