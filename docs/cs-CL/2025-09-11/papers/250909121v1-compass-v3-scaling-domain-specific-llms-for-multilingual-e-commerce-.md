---
layout: default
title: "Compass-v3: Scaling Domain-Specific LLMs for Multilingual E-Commerce in Southeast Asia"
---

# Compass-v3: Scaling Domain-Specific LLMs for Multilingual E-Commerce in Southeast Asia

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.09121" class="toolbar-btn" target="_blank">📄 arXiv: 2509.09121v1</a>
  <a href="https://arxiv.org/pdf/2509.09121.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.09121v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.09121v1', 'Compass-v3: Scaling Domain-Specific LLMs for Multilingual E-Commerce in Southeast Asia')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sophia Maria

**分类**: cs.CL

**发布日期**: 2025-09-11

---

## 💡 一句话要点

**Compass-v3：面向东南亚电商的多语言MoE模型，性能超越GPT-4**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `混合专家模型` `电子商务` `多语言` `东南亚` `指令对齐` `最优传输` `硬件优化`

## 📋 核心要点

1. 现有LLM在通用领域表现良好，但在电商等特定领域因数据复杂性（多语言、异构）而性能下降。
2. Compass-v3采用MoE架构，通过更大规模专家和硬件优化提升GPU利用率，并使用OTPO优化指令对齐。
3. 实验表明，Compass-v3在东南亚电商任务中超越DeepSeek-V3.1、GPT-4等模型，并在多种语言上表现出色。

## 📝 摘要（中文）

大型语言模型（LLMs）在通用领域应用中表现出色，但在需要特定领域知识的专业任务中，性能通常会下降。电子商务尤其具有挑战性，因为其数据嘈杂、异构、多语言且高度动态。我们提出了Compass-v3，一个垂直领域的混合专家（MoE）模型，总参数为245B，每个token激活71B参数，专为东南亚电子商务设计。Compass-v3采用更少但更大的专家，并结合硬件高效优化（如节点内专家并行和定制的memcpy算子）以最大化GPU利用率。该模型在12T tokens的精选多语言语料库和大规模合成电子商务指令上使用混合训练策略进行训练。为了增强对齐，我们提出了最优传输直接偏好优化（OTPO），它捕获token级别的差异，并提高商业特定场景中的指令遵循性。广泛的评估表明，Compass-v3提供了最先进的电子商务性能，超过了DeepSeek-V3.1、GPT-4系列和Qwen3-235B。此外，Compass-v3在低资源东南亚语言（印度尼西亚语、泰语、菲律宾语、越南语、马来语、塔加禄语）和葡萄牙语中表现出强大的多语言能力，同时保持了在通用基准测试中的竞争性能。它已广泛应用于Shopee的工业级电子商务平台，并逐渐取代OpenAI的流量，目前占LLM总使用量的70％以上，突显了其在专业商业知识和广泛语言能力方面的双重优势。

## 🔬 方法详解

**问题定义**：现有的大型语言模型在通用领域表现良好，但在电子商务等特定领域，由于数据噪声大、异构、多语言且动态性强，性能显著下降。尤其是在东南亚市场，多语言环境和低资源语言的存在进一步加剧了这一问题。现有方法难以有效处理这些挑战，导致电商任务的性能瓶颈。

**核心思路**：Compass-v3的核心思路是构建一个垂直领域的混合专家（MoE）模型，专注于东南亚电子商务。通过增加专家模型的规模，并结合硬件优化技术，提高模型的计算效率和GPU利用率。同时，采用最优传输直接偏好优化（OTPO）方法，增强模型在商业特定场景中的指令遵循能力，从而提升模型在电商任务中的性能。

**技术框架**：Compass-v3的整体架构是一个MoE模型，包含多个专家网络。训练流程包括：1) 使用精选的多语言语料库和大规模合成电子商务指令进行混合训练；2) 使用OTPO方法进行对齐优化，提升模型对电商指令的理解和执行能力。模型在Shopee的工业级电子商务平台上进行部署和应用。

**关键创新**：Compass-v3的关键创新点在于：1) 针对东南亚电商场景设计了垂直领域的MoE模型；2) 提出了最优传输直接偏好优化（OTPO）方法，用于增强模型在商业特定场景中的指令遵循性；3) 采用了硬件高效优化技术，如节点内专家并行和定制的memcpy算子，以最大化GPU利用率。

**关键设计**：Compass-v3模型总参数为245B，每个token激活71B参数。采用了更少但更大的专家，以提高计算效率。OTPO方法通过捕获token级别的差异，优化模型对指令的理解。硬件优化方面，节点内专家并行和定制的memcpy算子显著提升了GPU利用率。训练数据包括12T tokens的精选多语言语料库和大规模合成电子商务指令。

## 📊 实验亮点

Compass-v3在电子商务任务中表现出最先进的性能，超越了DeepSeek-V3.1、GPT-4系列和Qwen3-235B等模型。在低资源东南亚语言（如印度尼西亚语、泰语、菲律宾语等）和葡萄牙语中，Compass-v3也展现出强大的多语言能力，同时在通用基准测试中保持了竞争性能。目前，Compass-v3已占Shopee平台LLM总使用量的70%以上。

## 🎯 应用场景

Compass-v3在东南亚电子商务领域具有广泛的应用前景，可用于商品搜索、推荐系统、客户服务、内容生成等。其强大的多语言能力使其能够服务于不同语言的用户，提升用户体验。该模型已在Shopee的工业级电子商务平台中得到应用，并逐渐取代OpenAI的流量，显示了其巨大的商业价值。未来，Compass-v3有望进一步推动东南亚电子商务的发展。

## 📄 摘要（原文）

> Large language models (LLMs) excel in general-domain applications, yet their performance often degrades in specialized tasks requiring domain-specific knowledge. E-commerce is particularly challenging, as its data are noisy, heterogeneous, multilingual, and highly dynamic. We present Compass-v3, a vertical-domain Mixture-of-Experts (MoE) model with 245B total parameters and 71B active per token, designed for Southeast Asian e-commerce. Compass-v3 adopts fewer but larger experts, combined with hardware-efficient optimizations-such as intra-node expert parallelism and a customized memcpy operator-to maximize GPU utilization. The model is trained on 12T tokens of curated multilingual corpora and large-scale synthetic e-commerce instructions using a mixed-training strategy. To enhance alignment, we propose Optimal-Transport Direct Preference Optimization (OTPO), which captures token-level distinctions and improves instruction adherence in commerce-specific scenarios. Extensive evaluations demonstrate that Compass-v3 delivers state-of-the-art e-commerce performance, surpassing DeepSeek-V3.1, GPT-4 series, and Qwen3-235B. Moreover, Compass-v3 demonstrates strong multilingual capability across low-resource Southeast Asian languages (Indonesian, Thai, Filipino, Vietnamese, Malay, Taglog) and Portuguese while sustaining competitive performance on general benchmarks. It has already been widely applied in Shopee's industrial-scale e-commerce platform and is gradually replacing OpenAI's traffic, now accounting for over 70\% of total LLM usage, highlighting its dual strengths in specialized commerce expertise and broad linguistic competence.

