---
layout: default
title: "AgentFlux: Decoupled Fine-Tuning & Inference for On-Device Agentic Systems"
---

# AgentFlux: Decoupled Fine-Tuning & Inference for On-Device Agentic Systems

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.00229" class="toolbar-btn" target="_blank">📄 arXiv: 2510.00229v4</a>
  <a href="https://arxiv.org/pdf/2510.00229.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.00229v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.00229v4', 'AgentFlux: Decoupled Fine-Tuning & Inference for On-Device Agentic Systems')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Rohan Kadekodi, Zhan Jin, Keisuke Kamahori, Yile Gu, Sean Khatiri, Noah H. Bayindirli, Sergey Gorbunov, Baris Kasikci

**分类**: cs.AI, cs.LG

**发布日期**: 2025-09-30 (更新: 2025-11-12)

---

## 💡 一句话要点

**AgentFlux：解耦微调与推理，用于端侧Agent系统，提升工具调用准确率。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `端侧Agent` `工具调用` `解耦微调` `LoRA` `参数高效微调` `分层编排` `本地LLM`

## 📋 核心要点

1. 现有本地LLM在工具调用场景中表现不佳，难以进行工具选择和参数生成，限制了端侧Agent系统的应用。
2. 提出解耦微调方法，将工具调用任务分解为工具选择和参数生成，并为每个子任务训练独立的LoRA适配器。
3. AgentFlux推理框架利用解耦微调的LoRA适配器，结合分层编排，在端侧设备上实现了高效的Agent编排，显著提升了工具调用准确率。

## 📝 摘要（中文）

大型语言模型（LLM）作为agent编排器的部署彻底改变了任务自动化，但对保护隐私、经济高效的解决方案的需求推动了端侧推理能力的发展。然而，在工具调用场景中，本地LLM的表现始终不如前沿模型，难以从大型工具集中选择工具，也难以生成复杂参数结构的准确参数。我们提出了一种方法，将工具调用任务分解为两个不同的子任务：工具选择和参数生成。我们提出“解耦微调”，这是一种新颖的后训练方法，采用LoRA微调来创建专用的LoRA适配器，用于工具选择和特定于工具的参数生成，并为每个子任务使用单独的损失掩码。此外，我们提出了AgentFlux，一个推理框架，它利用使用解耦微调创建的LoRA适配器，在终端用户设备上借助本地模型执行高效的agent编排。AgentFlux将工具调用生成步骤分解为工具选择和参数生成，并动态加载相应的LoRA适配器以生成工具调用。此外，AgentFlux实现了分层编排，以限制工具选择所需的工具数量。我们在MCP-Bench基准上的实验表明，使用解耦微调训练的Qwen-2.5-7B模型将基础模型的工具调用准确率提高了46%，并且在所有情况下都优于其他类似大小的本地推理、非推理和微调模型，并且在大多数情况下优于大2倍的模型。

## 🔬 方法详解

**问题定义**：论文旨在解决本地LLM在端侧Agent系统中工具调用能力不足的问题。现有方法在工具选择和参数生成方面存在困难，导致整体性能下降，无法满足隐私保护和成本效益的需求。

**核心思路**：论文的核心思路是将工具调用任务解耦为工具选择和参数生成两个子任务，并分别进行优化。通过针对每个子任务进行专门的微调，可以提高模型的专业性和准确性。

**技术框架**：AgentFlux框架包含离线微调和在线推理两个阶段。离线阶段，使用解耦微调方法训练LoRA适配器，分别用于工具选择和参数生成。在线推理阶段，AgentFlux首先进行工具选择，然后加载相应的LoRA适配器生成参数，最后执行工具调用。此外，AgentFlux还采用了分层编排来减少工具选择的复杂度。

**关键创新**：论文的关键创新在于解耦微调方法，它通过独立的LoRA适配器和损失掩码，实现了对工具选择和参数生成的精细化优化。这种方法能够有效提升本地LLM在复杂工具调用场景下的性能。

**关键设计**：解耦微调的关键设计包括：1) 使用LoRA进行参数高效微调；2) 为工具选择和参数生成设计独立的损失函数，并使用损失掩码来区分不同的子任务；3) AgentFlux推理框架动态加载LoRA适配器，并采用分层编排来限制工具选择的范围。

## 📊 实验亮点

实验结果表明，使用解耦微调训练的Qwen-2.5-7B模型在MCP-Bench基准测试中，工具调用准确率比基础模型提高了46%。该模型在所有情况下都优于其他类似大小的本地推理、非推理和微调模型，并且在大多数情况下优于大2倍的模型，证明了解耦微调方法的有效性。

## 🎯 应用场景

该研究成果可应用于各种需要端侧智能的场景，例如智能家居、移动办公、车载系统等。通过在本地设备上部署AgentFlux，可以实现隐私保护、低延迟和高可靠性的任务自动化，提升用户体验并降低运营成本。未来，该技术有望推动Agent系统在更广泛领域的应用。

## 📄 摘要（原文）

> The deployment of Large Language Models (LLMs) as agentic orchestrators has revolutionized task automation, but the need for privacy-preserving, cost-effective solutions demands on-device inference capabilities. However, local LLMs consistently underperform compared to frontier models in tool calling scenarios, struggling with both tool selection from large tool sets and accurate argument generation for complex parameter structures. We introduce a methodology that disaggregates a tool-calling task into two distinct subtasks: tool selection and argument generation. We propose "decoupled fine-tuning", a novel post-training approach that employs LoRA fine-tuning to create dedicated LoRA adapters for tool selection and tool-specific argument generation using separate loss masking for each of the subtasks. Furthermore, we present AgentFlux, an inference framework that leverages the LoRA adapters created using decoupled fine-tuning to perform efficient agent orchestration with the help of local models on end-user devices. AgentFlux decomposes the tool-call generation step into tool selection and argument generation, and dynamically loads the corresponding LoRA adapters to generate tool calls. Additionally, AgentFlux implements hierarchical orchestration to restrict the number of tools required for tool selection. Our experiments on the MCP-Bench benchmark demonstrate that the Qwen-2.5-7B model trained using decoupled fine-tuning improves the tool calling accuracy of the base model by 46%, and outperforms other local reasoning, non-reasoning and fine-tuned models of similar size in all cases, and models that are 2x larger, in most cases.

